"""Bounded tests: 208 chart slots do not prove 208 observed glyph signs."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("nwagu_encoding_topology", ROOT / "scripts/audit_nwagu_encoding_topology.py")
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)


class NwaguEncodingTopologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bmc = mod.read_jsonl(mod.BMC)
        cls.tokens = mod.read_jsonl(mod.SOURCE_TOKENS)
        cls.logographs = mod.read_jsonl(mod.LOGOGRAPHS)
        cls.published = json.loads(mod.PUBLISHED.read_text(encoding="utf-8"))

    def result(self, bmc=None, tokens=None, logographs=None, published=None):
        return mod.audit(
            self.bmc if bmc is None else bmc,
            self.tokens if tokens is None else tokens,
            self.logographs if logographs is None else logographs,
            self.published if published is None else published,
        )

    def test_actual_repo_chart_index_and_glyph_evidence_gap(self):
        result = self.result()
        self.assertTrue(result["valid_internal_index"], result["errors"])
        self.assertEqual(result["chart_index"]["row_labels"], 26)
        self.assertEqual(result["chart_index"]["vowel_labels"], 8)
        self.assertEqual(result["chart_index"]["grid_slots"], 208)
        self.assertEqual(result["glyph_evidence"]["locatable_cell_regions"], 0)
        self.assertEqual(result["glyph_evidence"]["reviewed_locatable_cell_regions"], 0)
        self.assertEqual(result["glyph_evidence"]["unreviewed_cell_slots"], 208)
        self.assertEqual(result["glyph_evidence"]["distinct_glyph_observation_references"], 26)
        self.assertEqual(result["glyph_evidence"]["maximum_slots_per_observation_reference"], 8)
        self.assertFalse(result["glyph_evidence"]["glyph_repertoire_count_established"])

    def test_vowel_initial_counts_are_exploratory_not_historical_census(self):
        onsets = self.result()["exploratory_full_word_onsets"]
        self.assertEqual((onsets["chart_transcription"]["vowel_initial"], onsets["chart_transcription"]["total"]), (29, 30))
        self.assertEqual(onsets["chart_transcription"]["consonant_initial_labels"], ["nga"])
        self.assertEqual((onsets["published_examples"]["vowel_initial"], onsets["published_examples"]["total"]), (15, 15))
        self.assertIn("not_population_estimate", onsets["published_examples"]["status"])

    def test_literature_counts_do_not_become_glyph_inventory(self):
        result = self.result()
        self.assertEqual(result["literature_claims"]["counts"]["distinct_graphic_signs"], 164)
        self.assertEqual(result["literature_claims"]["counts"]["ideal_syllabic_coverage"], 224)
        self.assertFalse(result["glyph_evidence"]["glyph_repertoire_count_established"])

    def test_fake_review_flag_cannot_create_located_glyph_evidence(self):
        bmc = copy.deepcopy(self.bmc)
        bmc[0]["review_status"] = "approved"
        bmc[0]["status"] = "verified"
        result = self.result(bmc=bmc)
        self.assertEqual(result["glyph_evidence"]["locatable_cell_regions"], 0)
        self.assertEqual(result["glyph_evidence"]["reviewed_locatable_cell_regions"], 0)

    def test_unlocated_reused_observation_ids_do_not_count_as_glyphs(self):
        bmc = copy.deepcopy(self.bmc)
        for i, row in enumerate(bmc):
            row["glyph_observation_id"] = f"FAKE-CELL-{i:03d}"
        result = self.result(bmc=bmc)
        self.assertEqual(result["glyph_evidence"]["distinct_glyph_observation_references"], 208)
        self.assertEqual(result["glyph_evidence"]["locatable_cell_regions"], 0)
        self.assertFalse(result["glyph_evidence"]["glyph_repertoire_count_established"])

    def test_corrupted_source_token_projection_fails(self):
        tokens = copy.deepcopy(self.tokens)
        tokens[0]["reading"] = "not-a-source-reading"
        result = self.result(tokens=tokens)
        self.assertFalse(result["valid_internal_index"])
        self.assertTrue(any("projection does not match" in e for e in result["errors"]))

    def test_missing_cell_index_fails(self):
        result = self.result(bmc=self.bmc[:-1])
        self.assertFalse(result["valid_internal_index"])

    def test_duplicate_row_vowel_pair_fails(self):
        bmc = copy.deepcopy(self.bmc)
        bmc[1]["row_label"] = bmc[0]["row_label"]
        bmc[1]["vowel_label"] = bmc[0]["vowel_label"]
        self.assertFalse(self.result(bmc=bmc)["valid_internal_index"])

    def test_unicode_normalization_and_non_vowel(self):
        self.assertTrue(mod.begins_with_vowel("u\u0323bọsi"))  # decomposed ụ
        self.assertTrue(mod.begins_with_vowel("ỌGỤ"))
        self.assertFalse(mod.begins_with_vowel("nga"))
        self.assertFalse(mod.begins_with_vowel(""))

    def test_audit_is_read_only(self):
        original = json.dumps([self.bmc, self.tokens, self.logographs, self.published], sort_keys=True)
        self.result()
        self.assertEqual(original, json.dumps([self.bmc, self.tokens, self.logographs, self.published], sort_keys=True))


if __name__ == "__main__":
    unittest.main()
