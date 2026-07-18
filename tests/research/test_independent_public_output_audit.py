from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "research_runs" / "public_release_triage" / "independent_public_output_audit.json"


class IndependentPublicOutputAuditTest(unittest.TestCase):
    def test_audit_classifies_all_registry_candidates_without_overclaiming(self):
        result = subprocess.run(
            [sys.executable, "scripts/audit_independent_public_output.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(REPORT.exists())

        report = json.loads(REPORT.read_text(encoding="utf-8"))
        self.assertEqual(report["checked_count"], 10)
        self.assertEqual(len(report["outputs"]), 10)
        self.assertEqual(report["public_journal_candidate_count"], 0)
        self.assertEqual(report["external_reader_pass_count"], 1)

        allowed_classes = {
            "PUBLIC_JOURNAL_MANUSCRIPT_CANDIDATE",
            "PUBLIC_PREPRINT_CANDIDATE",
            "PUBLIC_TECHNICAL_REPORT",
            "PUBLIC_DATASET_OR_NOTE",
            "MERGE_INTO_STRONGER_MANUSCRIPT",
            "INTERNAL_ONLY",
            "KILL_OR_PARK",
        }
        self.assertLessEqual(
            {row["release_class"] for row in report["outputs"]},
            allowed_classes,
        )

        failing_rows = [
            row
            for row in report["outputs"]
            if not row["external_reader_legitimacy_pass"]
        ]
        self.assertEqual(len(failing_rows), 9)
        self.assertTrue(
            all(
                row["release_class"] != "PUBLIC_JOURNAL_MANUSCRIPT_CANDIDATE"
                for row in failing_rows
            )
        )

    def test_article_006_is_the_only_current_public_facing_candidate(self):
        subprocess.run(
            [sys.executable, "scripts/audit_independent_public_output.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        report = json.loads(REPORT.read_text(encoding="utf-8"))

        public_facing = [
            row["article_id"]
            for row in report["outputs"]
            if row["release_class"] in {"PUBLIC_PREPRINT_CANDIDATE", "PUBLIC_TECHNICAL_REPORT"}
        ]

        self.assertEqual(public_facing, ["ARTICLE-NA-006"])


if __name__ == "__main__":
    unittest.main()
