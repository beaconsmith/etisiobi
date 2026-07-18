import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate"
RESULTS = EXP_DIR / "full_quality_gate_results.json"
FULL_TABLE = EXP_DIR / "full_quality_gate.csv"
ALIGNMENT = EXP_DIR / "score_gate_alignment.json"
REVIEW_PACKET = EXP_DIR / "human_domain_review_packet.csv"
REVIEW_PACKET_MD = EXP_DIR / "human_domain_review_packet.md"


class FullQualityGateTest(unittest.TestCase):
    def test_full_gate_routes_all_labels_and_keeps_submission_blocked(self):
        subprocess.run(
            [sys.executable, str(EXP_DIR / "run_full_quality_gate.py")],
            cwd=ROOT,
            check=True,
        )

        data = json.loads(RESULTS.read_text(encoding="utf-8"))
        alignment = json.loads(ALIGNMENT.read_text(encoding="utf-8"))

        self.assertEqual(
            data["status"],
            "FULL_LABEL_QUALITY_GATE_COMPLETE_INTERNAL_NOT_SUBMISSION_READY",
        )
        self.assertEqual(data["claim_ceiling"], "full_quality_gate_internal_not_paper_result")
        self.assertEqual(data["full_case_count"], 360)
        self.assertEqual(data["source_gold_label_count"], 360)
        self.assertEqual(data["paper_claim_status"], "not_ready")
        self.assertEqual(data["frontier_claim_status"], "not_ready")
        self.assertEqual(data["public_release_status"], "blocked")
        self.assertGreater(data["review_ready_internal_count"], 0)
        self.assertGreater(data["needs_adjudication_count"], 0)
        self.assertGreater(data["blocked_public_release_count"], 0)
        self.assertEqual(data["human_domain_review_status"], "missing")
        self.assertEqual(data["external_actions_taken"], [])
        self.assertEqual(data["compared_agent_condition_count"], 8)
        self.assertEqual(alignment["best_overall_condition"], "C0_no_layer_labels")
        self.assertEqual(alignment["best_overall_f1"], 0.7692)
        self.assertTrue(FULL_TABLE.exists())
        self.assertTrue(REVIEW_PACKET.exists())
        self.assertTrue(REVIEW_PACKET_MD.exists())
        self.assertEqual(data["human_domain_review_packet_rows"], 70)


if __name__ == "__main__":
    unittest.main()
