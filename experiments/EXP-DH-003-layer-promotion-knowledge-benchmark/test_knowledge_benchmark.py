import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXP_DIR = ROOT / "experiments" / "EXP-DH-003-layer-promotion-knowledge-benchmark"
RESULTS = EXP_DIR / "results.json"


class KnowledgeBenchmarkTest(unittest.TestCase):
    def test_ten_bounded_knowledge_units_pass_internal_gate(self):
        subprocess.run(
            [sys.executable, str(EXP_DIR / "run_knowledge_benchmark.py")],
            cwd=ROOT,
            check=True,
        )

        data = json.loads(RESULTS.read_text(encoding="utf-8"))

        self.assertEqual(
            data["status"],
            "SIGNIFICANT_INTERNAL_KNOWLEDGE_BREAKTHROUGH_DH003",
        )
        self.assertEqual(data["knowledge_unit_count"], 10)
        self.assertEqual(data["global_benchmark_claim"], "not_met")
        self.assertEqual(data["novelty_scope"], "internal_repo_knowledge")
        self.assertEqual(data["paper_claim_status"], "not_ready")
        self.assertEqual(data["public_release_status"], "blocked")
        self.assertGreaterEqual(data["source_case_count"], 510)
        self.assertEqual(data["collision_count"], 200)
        self.assertEqual(data["quality_gate_sample_count"], 24)
        self.assertEqual(data["failed_units"], [])
        self.assertTrue(data["celebration_worthy"])


if __name__ == "__main__":
    unittest.main()
