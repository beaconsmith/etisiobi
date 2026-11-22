"""Adversarial and baseline checks for PAGC source/derived token lineage."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("token_lineage", ROOT / "scripts/validate_pagc_token_lineage.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PagcTokenLineageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = validator.read_jsonl(validator.SOURCE_PATH)
        cls.derived = validator.read_jsonl(validator.DERIVED_PATH)
        cls.domain = validator.read_jsonl(validator.DOMAIN_PATH)

    def test_repository_layers_and_derived_composition(self):
        result = validator.validate_lineage(self.source, self.derived, self.domain)
        self.assertTrue(result["valid"], result["errors"][:10])
        self.assertEqual(result["counts"], {
            "source_observed": 208,
            "derived_fv_split": 216,
            "derived_carry_through": 200,
            "derived_explicit_fv_split": 16,
            "domain_mapped_design_hypotheses": 48,
        })

    def test_pairwise_layer_swap_bypasses_old_count_and_id_checks(self):
        source, derived = copy.deepcopy(self.source), copy.deepcopy(self.derived)
        idx = next(i for i, row in enumerate(derived) if row["token_id"] == source[0]["token_id"])
        source[0]["layer"], derived[idx]["layer"] = derived[idx]["layer"], source[0]["layer"]
        # Existing EXP-APP-003 gate counts layer membership + qualified-ID uniqueness.
        combined = source + derived + self.domain
        counts = {label: sum(row["layer"] == label for row in combined)
                  for label in ("source_observed", "derived_fv_split", "domain_mapped_from_pagc_count_layer")}
        qualified_ids = [row["layer"] + "::" + row["token_id"] for row in combined]
        self.assertEqual(counts, {
            "source_observed": 208, "derived_fv_split": 216,
            "domain_mapped_from_pagc_count_layer": 48,
        })
        self.assertEqual(len(set(qualified_ids)), len(qualified_ids))
        # Yet the classifications now contradict their source and derived input provenance.
        self.assertFalse(validator.validate_lineage(source, derived, self.domain)["valid"])

    def test_swapped_labels_and_flags_still_fail_by_input_boundary(self):
        source, derived = copy.deepcopy(self.source), copy.deepcopy(self.derived)
        idx = next(i for i, row in enumerate(derived) if row["token_id"] == source[0]["token_id"])
        source[0]["layer"] = "derived_fv_split"
        source[0]["source_observed"] = False
        derived[idx]["layer"] = "source_observed"
        derived[idx]["source_observed"] = True
        self.assertFalse(validator.validate_lineage(source, derived, self.domain)["valid"])

    def test_missing_parent_is_rejected(self):
        derived = copy.deepcopy(self.derived)
        derived[0]["source_bmc_id"] = "BMC-DOES-NOT-EXIST"
        result = validator.validate_lineage(self.source, derived, self.domain)
        self.assertFalse(result["valid"])
        self.assertTrue(any("unrecognized source parent" in err for err in result["errors"]))

    def test_incorrect_split_rule_is_rejected(self):
        derived = copy.deepcopy(self.derived)
        idx = next(i for i, row in enumerate(derived) if row.get("derived_rule"))
        derived[idx]["derived_rule"] = None
        result = validator.validate_lineage(self.source, derived, self.domain)
        self.assertFalse(result["valid"])
        self.assertTrue(any("valid f/v split lineage" in err for err in result["errors"]))

    def test_fake_source_label_in_domain_mapping_is_rejected(self):
        domain = copy.deepcopy(self.domain)
        domain[0]["layer"] = "source_observed"
        domain[0]["source_observed"] = True
        self.assertFalse(validator.validate_lineage(self.source, self.derived, domain)["valid"])

    def test_unsupported_domain_promotion_is_rejected(self):
        domain = copy.deepcopy(self.domain)
        domain[0]["evidence_status"] = "experiment_supported"
        self.assertFalse(validator.validate_lineage(self.source, self.derived, domain)["valid"])

    def test_duplicate_derived_identity_is_rejected(self):
        derived = copy.deepcopy(self.derived)
        derived[1]["token_id"] = derived[0]["token_id"]
        self.assertFalse(validator.validate_lineage(self.source, derived, self.domain)["valid"])

    def test_validation_is_read_only(self):
        before = json.dumps([self.source, self.derived, self.domain], sort_keys=True)
        validator.validate_lineage(self.source, self.derived, self.domain)
        self.assertEqual(before, json.dumps([self.source, self.derived, self.domain], sort_keys=True))


if __name__ == "__main__":
    unittest.main()
