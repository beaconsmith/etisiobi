import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

MODULE_PATH = Path(__file__).resolve().parents[2] / "scripts" / "decision_tripwire.py"
spec = importlib.util.spec_from_file_location("decision_tripwire", MODULE_PATH)
tripwire = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tripwire)


class DecisionTripwireTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "corpus").mkdir()
        (self.root / "corpus" / "count.json").write_text("{}", encoding="utf-8")
        self.records = [
            {"decision_id": "D-1", "scope": "source_count", "status": "accepted",
             "evidence": ["corpus/count.json", "user confirmation in current thread"],
             "reversal_condition": "New manuscript contradicts count.", "risk": "Source incomplete"},
            {"decision_id": "D-2", "scope": "application", "status": "active",
             "evidence": ["corpus/"], "reversal_condition": "", "risk": ""},
        ]

    def test_changed_file_triggers_file_and_directory_citations(self):
        result = tripwire.audit(self.records, self.root, ["corpus/count.json"])
        self.assertEqual(result["affected_decisions"], 2)
        self.assertTrue(all(row["review_required"] for row in result["decisions"]))

    def test_changed_parent_directory_triggers_file_reference(self):
        result = tripwire.audit(self.records, self.root, ["corpus/"])
        self.assertEqual(result["affected_decisions"], 2)

    def test_prefix_collision_does_not_trigger(self):
        result = tripwire.audit(self.records, self.root, ["corpus-other/count.json"])
        self.assertEqual(result["affected_decisions"], 0)

    def test_warns_on_ephemeral_reference_and_missing_reversal(self):
        result = tripwire.audit(self.records, self.root, [])
        self.assertIn("unverifiable_reference", {w["code"] for w in result["decisions"][0]["warnings"]})
        self.assertEqual({w["code"] for w in result["decisions"][1]["warnings"]},
                         {"missing_reversal_condition", "missing_risk"})

    def test_missing_local_evidence_is_not_silently_accepted(self):
        record = {**self.records[0], "evidence": ["corpus/missing.json"]}
        result = tripwire.audit([record], self.root, [])
        self.assertEqual(result["decisions"][0]["warnings"][0]["code"], "missing_local_evidence")

    def test_rejects_unsafe_changed_paths(self):
        for path in ["../secrets", "/etc/passwd", "https://example.com/file"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                tripwire.audit(self.records, self.root, [path])

    def test_invalid_jsonl_and_duplicate_decisions_fail_closed(self):
        ledger = self.root / "decisions.jsonl"
        ledger.write_text('{"broken":', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "invalid JSONL"):
            tripwire.load_records(ledger)
        ledger.write_text("\n".join(json.dumps(r) for r in [self.records[0]] * 2), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate decision_id"):
            tripwire.load_records(ledger)

    def test_read_only_audit_does_not_change_source(self):
        before = (self.root / "corpus/count.json").read_bytes()
        tripwire.audit(self.records, self.root, ["corpus/count.json"])
        self.assertEqual((self.root / "corpus/count.json").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
