from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "run_toy_baseline.py"
GATE = ROOT / "run_global_benchmark_gate.py"
GATE_RESULTS = ROOT / "global_benchmark_gate_results.json"


class Dh001GlobalBenchmarkGateTest(unittest.TestCase):
    def test_global_benchmark_gate_parks_label_dependent_branch(self) -> None:
        subprocess.run([sys.executable, str(RUNNER)], check=True, cwd=ROOT)
        subprocess.run([sys.executable, str(GATE)], check=True, cwd=ROOT)
        output = json.loads(GATE_RESULTS.read_text(encoding="utf-8"))

        self.assertEqual(
            output["status"],
            "GLOBAL_BENCHMARK_NEGATIVE_BREAKTHROUGH_PARK_DH001",
        )
        self.assertEqual(output["criteria_passed"], 6)
        self.assertEqual(output["criteria_failed"], 1)
        self.assertEqual(output["failed_criteria"], ["non_label_generalization"])
        self.assertEqual(output["decision"], "PARK_DH001_BEFORE_PAPER_CANDIDATE")
        self.assertEqual(output["global_benchmark_claim"], "not_met")
        self.assertTrue(output["celebration_worthy"])


if __name__ == "__main__":
    unittest.main()
