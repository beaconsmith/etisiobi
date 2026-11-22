"""Falsification tests for the EXP-APP-003 proof's promotion precondition."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "scripts/validate_promotion_graph.py"
SPEC = importlib.util.spec_from_file_location("promotion_graph_validator", MODULE)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)
RULES_FILE = ROOT / "experiments/EXP-APP-003-layer-safety-proof/promotion_rules.json"


class PromotionGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = json.loads(RULES_FILE.read_text(encoding="utf-8"))

    def test_committed_graph_satisfies_the_invariant(self):
        result = validator.verify_rules(self.original)
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["counterexamples"], [])

    def test_published_gate_flags_do_not_detect_mutant(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"].append({
            "from": "publishable_claim", "to": "source_observed",
            "operation": "bad_retroactive_evidence_promotion", "requires": []
        })
        # EXP-APP-003's current generator tests for the EXISTENCE of these
        # forbidden declarations, not graph reachability or contradictions.
        for src in ("derived_fv_split", "domain_mapped_from_pagc_count_layer"):
            self.assertTrue(any(r["from"] == src and r["to"] == "source_observed"
                                for r in mutant["forbidden_promotions"]))
        result = validator.verify_rules(mutant)
        self.assertFalse(result["valid"])
        witnesses = [row["path"] for row in result["counterexamples"]]
        self.assertIn([
            "derived_fv_split",
            "domain_mapped_from_pagc_count_layer",
            "publishable_claim",
            "source_observed",
        ], witnesses)

    def test_unlisted_blocked_layer_cannot_become_source(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"].append({
            "from": "blocked", "to": "source_observed", "operation": "unsafe", "requires": []
        })
        result = validator.verify_rules(mutant)
        self.assertFalse(result["valid"])
        self.assertIn(["blocked", "source_observed"], [r["path"] for r in result["counterexamples"]])

    def test_direct_conflict_with_forbidden_rules_fails(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"].append({
            "from": "derived_fv_split", "to": "source_observed",
            "operation": "unsafe", "requires": []
        })
        result = validator.verify_rules(mutant)
        self.assertFalse(result["valid"])
        self.assertTrue(any("conflicts" in error for error in result["errors"]))

    def test_unknown_endpoint_fails_closed(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"].append({
            "from": "unregistered_layer", "to": "source_observed",
            "operation": "unknown", "requires": []
        })
        self.assertFalse(validator.verify_rules(mutant)["valid"])

    def test_invalid_rule_shape_fails_closed(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"] = "not a list"
        self.assertFalse(validator.verify_rules(mutant)["valid"])

    def test_missing_source_layer_fails_closed(self):
        mutant = copy.deepcopy(self.original)
        mutant["layers"].remove("source_observed")
        self.assertFalse(validator.verify_rules(mutant)["valid"])

    def test_added_safe_non_source_transition_is_allowed(self):
        mutant = copy.deepcopy(self.original)
        mutant["allowed_promotions"].append({
            "from": "blocked", "to": "speculative",
            "operation": "reopen_as_speculation", "requires": []
        })
        self.assertTrue(validator.verify_rules(mutant)["valid"])


if __name__ == "__main__":
    unittest.main()
