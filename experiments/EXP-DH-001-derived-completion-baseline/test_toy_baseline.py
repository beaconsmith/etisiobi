from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "run_toy_baseline.py"
RESULTS = ROOT / "results.json"


class Dh001ToyBaselineTest(unittest.TestCase):
    def test_runner_scores_counterexamples_and_source_constraints(self) -> None:
        subprocess.run([sys.executable, str(RUNNER)], check=True, cwd=ROOT)
        output = json.loads(RESULTS.read_text(encoding="utf-8"))

        self.assertEqual(
            output["status"],
            "SOURCE_RECORD_SCREEN_PASS_ADVERSARIAL_VALUE_BLOCKED",
        )
        self.assertEqual(output["counterexample_case_count"], 6)
        self.assertEqual(output["source_constraint_count"], 6)
        self.assertEqual(output["source_constraint_status"], "PASS")
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "unsafe_source_claim_rejections"
            ],
            3,
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "source_constraint_violations"
            ],
            0,
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "counterexample_screen_status"
            ],
            "PASS",
        )

    def test_runner_scores_source_records_and_adversarial_label_value(self) -> None:
        subprocess.run([sys.executable, str(RUNNER)], check=True, cwd=ROOT)
        output = json.loads(RESULTS.read_text(encoding="utf-8"))

        self.assertEqual(
            output["status"],
            "SOURCE_RECORD_SCREEN_PASS_ADVERSARIAL_VALUE_BLOCKED",
        )
        self.assertEqual(output["source_record_case_count"], 8)
        self.assertEqual(output["adversarial_variant_count"], 6)
        self.assertEqual(output["source_record_status"], "PASS")
        self.assertEqual(output["adversarial_value_status"], "BLOCKED_LABEL_ONLY")
        self.assertTrue(output["label_dependence_detected"])
        self.assertEqual(
            output["models"]["derived_27x8_role_split"]["source_record_gate_accuracy"],
            1.0,
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"]["adversarial_overclaim_rejections"],
            6,
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "value_beyond_label_evidence"
            ],
            "not_demonstrated",
        )

    def test_runner_scores_source_feature_non_label_task(self) -> None:
        subprocess.run([sys.executable, str(RUNNER)], check=True, cwd=ROOT)
        output = json.loads(RESULTS.read_text(encoding="utf-8"))

        self.assertEqual(output["source_feature_task_case_count"], 5)
        self.assertEqual(output["source_feature_task_status"], "PASS")
        self.assertEqual(
            output["source_feature_value_status"],
            "PARK_LABEL_DEPENDENT",
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "source_feature_task_accuracy"
            ],
            1.0,
        )
        self.assertEqual(
            output["models"]["derived_27x8_role_split"][
                "source_feature_positive_support_count"
            ],
            0,
        )


if __name__ == "__main__":
    unittest.main()
