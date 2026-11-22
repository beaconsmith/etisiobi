"""Reproducible, adversarial constraints for Aneke literature-derived microexamples."""
from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("lossy_channel", ROOT / "scripts/audit_nwagu_lossy_channel.py")
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class LossyChannelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(mod.MICRO.read_text(encoding="utf-8"))
        cls.labels = mod.read_jsonl(mod.LOGOS)

    def call(self, data=None, labels=None):
        return mod.audit(self.data if data is None else data, self.labels if labels is None else labels)

    def test_baseline_has_two_attested_ambiguity_groups(self):
        out = self.call()
        self.assertTrue(out["valid"], out["errors"])
        groups = {x["written_reading"]: x for x in out["attested_homography_groups"]}
        self.assertEqual(groups["bi"]["candidate_readings"], ["obi", "ubi", "ibi", "ebi"])
        self.assertEqual(groups["ma"]["candidate_readings"], ["oma", "ama", "uma"])
        self.assertEqual((groups["bi"]["documented_example_count"], groups["ma"]["documented_example_count"]), (4, 3))

    def test_uniform_entropy_is_only_an_assumption(self):
        out = self.call()
        bi, ma = out["attested_homography_groups"]
        self.assertEqual(bi["uniform_prior_entropy_bits"], 2.0)
        self.assertAlmostEqual(ma["uniform_prior_entropy_bits"], math.log2(3), places=6)
        self.assertLess(bi["synthetic_skew_prior_entropy_bits"], bi["uniform_prior_entropy_bits"])
        self.assertTrue(bi["not_empirical"])
        self.assertFalse(out["contextual_entropy_estimated_from_manuscripts"])
        self.assertFalse(out["empirical_decoding_accuracy_available"])

    def test_chart_scan_candidate_changes_onset_without_pretending_adjudication(self):
        x = self.call()["chart_transcription_sensitivity"]
        self.assertEqual(x["total_leads"], 30)
        self.assertEqual(x["repository_vowel_initial"], 29)
        self.assertEqual(x["tentative_if_scan_candidates_adjudicated"], 28)
        self.assertEqual(x["unresolved_conflicts"][0]["repo"], "uche")
        self.assertEqual(x["unresolved_conflicts"][0]["candidate_scan"], "nche")
        self.assertTrue(x["no_population_inference"])

    def test_decomposed_igbo_vowel_normalizes_correctly(self):
        self.assertEqual(mod.remove_initial_independent_vowel("u\u0323bi"), "bi")
        self.assertFalse(mod.begins_with_vowel("nche"))
        self.assertTrue(mod.begins_with_vowel("uche"))
        self.assertIsNone(mod.remove_initial_independent_vowel("ma"))

    def test_bad_candidate_cannot_be_explained_by_dropping_initial_vowel(self):
        fixture = copy.deepcopy(self.data)
        fixture["ambiguous_written_readings"][0]["candidates"][0]["reading"] = "nobi"
        result = self.call(data=fixture)
        self.assertFalse(result["valid"])
        self.assertTrue(any("not explained" in e for e in result["errors"]))

    def test_duplicate_candidate_rejected(self):
        fixture = copy.deepcopy(self.data)
        fixture["ambiguous_written_readings"][0]["candidates"][0]["reading"] = "ubi"
        self.assertFalse(self.call(data=fixture)["valid"])

    def test_missing_or_incorrect_source_ref_rejected(self):
        fixture = copy.deepcopy(self.data)
        fixture["ambiguous_written_readings"][0]["source_id"] = "NONEXISTENT"
        self.assertFalse(self.call(data=fixture)["valid"])

    def test_missing_chart_entry_causes_failed_collation(self):
        labels = copy.deepcopy(self.labels)
        labels[1]["word"] = "other"
        result = self.call(labels=labels)
        self.assertFalse(result["valid"])
        self.assertTrue(any("repo entry" in e for e in result["errors"]))

    def test_invalid_entropy_weights_rejected(self):
        with self.assertRaises(ValueError):
            mod.shannon_bits([-1, 2])
        with self.assertRaises(ValueError):
            mod.shannon_bits([0, 0])

    def test_read_only(self):
        before = json.dumps([self.data, self.labels], sort_keys=True)
        self.call()
        self.assertEqual(before, json.dumps([self.data, self.labels], sort_keys=True))


if __name__ == "__main__":
    unittest.main()
