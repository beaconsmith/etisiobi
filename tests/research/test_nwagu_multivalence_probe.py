"""All examples are SYNTHETIC. They do not claim historical Nwagụ mappings."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "scripts" / "nwagu_multivalence_probe.py"
SPEC = importlib.util.spec_from_file_location("nwagu_multivalence_probe", MODULE)
probe = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(probe)


def edge(sign, reading, harmony):
    return {
        "sign_id": sign,
        "reading_id": reading,
        "harmony_class": harmony,
        "source_locator": "synthetic:test-only",
        "review_status": "human_adjudicated",
    }


class NwaguMultivalenceProbeTests(unittest.TestCase):
    def setUp(self):
        # Synthetic test fixture: one sign is polyphonic, one reading has two
        # alternative signs. These are not observed Nwagụ signs or readings.
        self.sample = [
            edge("S-A", "R-1", "H-A"),
            edge("S-A", "R-2", "H-A"),
            edge("S-B", "R-1", "H-A"),
            edge("S-B", "R-3", "H-B"),
        ]

    def test_reject_empty_historical_mapping(self):
        with self.assertRaisesRegex(ValueError, "no reviewed mapping"):
            probe.study([])

    def test_counts_sign_to_reading_and_reading_to_sign_multiplicity(self):
        r = probe.study(self.sample, permutations=99, seed=10)
        self.assertEqual(r["signs_in_sample"], 2)
        self.assertEqual(r["readings_in_sample"], 3)
        self.assertEqual(r["incidence_edges"], 4)
        self.assertEqual(r["signs_with_multiple_readings"], 2)
        self.assertEqual(r["readings_with_multiple_signs"], 1)
        self.assertEqual(r["eligible_within_sign_reading_pairs"], 2)
        self.assertEqual(r["same_class_pair_fraction"], 0.5)
        self.assertEqual(r["permutations"], 99)
        self.assertIn("NOT_REPERTOIRE_COMPLETENESS", r["status"])

    def test_deterministic_for_frozen_seed(self):
        a = probe.study(self.sample, permutations=99, seed=7)
        b = probe.study(self.sample, permutations=99, seed=7)
        self.assertEqual(a, b)

    def test_refuses_unadjudicated_edge(self):
        mutated = copy.deepcopy(self.sample)
        mutated[0]["review_status"] = "ai_guess"
        with self.assertRaisesRegex(ValueError, "human_adjudicated"):
            probe.study(mutated)

    def test_refuses_missing_source_locator(self):
        mutated = copy.deepcopy(self.sample)
        mutated[0]["source_locator"] = ""
        with self.assertRaisesRegex(ValueError, "source_locator"):
            probe.study(mutated)

    def test_refuses_duplicate_edge(self):
        with self.assertRaisesRegex(ValueError, "duplicate sign-reading pair"):
            probe.study(self.sample + [copy.deepcopy(self.sample[0])])

    def test_refuses_conflicting_harmony_class_for_reading(self):
        mutated = copy.deepcopy(self.sample)
        mutated[2]["harmony_class"] = "H-B"
        with self.assertRaisesRegex(ValueError, "conflicting harmony"):
            probe.study(mutated)

    def test_unknown_classes_do_not_get_invented(self):
        sample = [edge("S-A", "R-1", None), edge("S-A", "R-2", "H-A")]
        r = probe.study(sample)
        self.assertEqual(r["eligible_within_sign_reading_pairs"], 0)
        self.assertIsNone(r["same_class_pair_fraction"])
        self.assertIsNone(r["permutation_tail_probability_exploratory"])

    def test_no_significance_without_multiple_classes(self):
        sample = [edge("S-A", "R-1", "H-A"), edge("S-A", "R-2", "H-A")]
        r = probe.study(sample)
        self.assertIsNone(r["permutation_tail_probability_exploratory"])

    def test_cli_requires_explicit_reviewed_dataset(self):
        r = subprocess.run([sys.executable, str(MODULE)], text=True, capture_output=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--edges", r.stderr)


if __name__ == "__main__":
    unittest.main()
