import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class ExpNa010LayerSafetyTest(unittest.TestCase):
    def test_expanded_layer_safety_gate_beats_shallow_baselines(self):
        result = subprocess.run(
            [
                sys.executable,
                "experiments/EXP-NA-010-layer-safety-tests/run_layer_safety_analysis.py",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

        expanded = json.loads(
            (
                ROOT
                / "experiments/EXP-NA-010-layer-safety-tests/expanded_results.json"
            ).read_text(encoding="utf-8")
        )
        baselines = json.loads(
            (
                ROOT
                / "experiments/EXP-NA-010-layer-safety-tests/baseline_comparison.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(
            expanded["decision"], "EXPANDED_LAYER_SAFETY_BASELINE_COMPARISON_PASS"
        )
        self.assertGreaterEqual(expanded["test_cases"], 20)
        self.assertEqual(expanded["promotion_error_detection_rate"], 1.0)
        self.assertEqual(
            baselines["layer_gate_false_negatives_on_promotion_errors"], 0
        )
        self.assertGreater(
            baselines["baselines"]["provenance_only"][
                "false_negatives_on_promotion_errors"
            ],
            0,
        )
        self.assertGreater(
            baselines["baselines"]["citation_only"][
                "false_negatives_on_promotion_errors"
            ],
            0,
        )


if __name__ == "__main__":
    unittest.main()
