"""Source/derived f/v accounting, not an historical glyph census."""
from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "experiments" / "EXP-APP-001-count-layer-design-grammar"


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


class NwaguFVReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = rows(APP / "tokens_source_layer.jsonl")
        cls.derived = rows(APP / "tokens_derived_layer.jsonl")

    def test_eight_combined_source_cells_become_sixteen_derived_reading_objects(self):
        fv_sources = [r for r in self.source if r["base"] == "f/v"]
        self.assertEqual(len(fv_sources), 8)
        group = defaultdict(list)
        for record in self.derived:
            group[record["source_bmc_id"]].append(record)
        self.assertEqual(len(self.source), 208)
        self.assertEqual(len(self.derived), 216)
        self.assertEqual(len(self.derived) - len(self.source), 8)

        for source in fv_sources:
            children = group[source["source_bmc_id"]]
            self.assertEqual(len(children), 2)
            self.assertEqual({child["base"] for child in children}, {"f", "v"})
            self.assertEqual({child["modifier"] for child in children}, {source["modifier"]})
            self.assertTrue(all(child["derived_rule"] == "split f/v row into f and v" for child in children))
            # Parent identity is preserved, not evidence of two historical signs.
            self.assertTrue(all(child["source_bmc_id"] == source["source_bmc_id"] for child in children))

    def test_derived_layer_has_200_unmodified_carry_through_objects(self):
        inherited = [r for r in self.derived if not r.get("derived_rule")]
        self.assertEqual(len(inherited), 200)
        original = {r["source_bmc_id"]: r for r in self.source}
        for record in inherited:
            parent = original[record["source_bmc_id"]]
            self.assertEqual([record[k] for k in ("token_id", "base", "modifier", "reading")],
                             [parent[k] for k in ("token_id", "base", "modifier", "reading")])

    def test_inventory_has_no_verified_historical_glyph_ids_yet(self):
        inventory = rows(ROOT / "artifacts/nwagu_aneke/symbol_inventory.jsonl")
        self.assertEqual(len([r for r in inventory if r["record_type"] == "row_label"]), 26)
        self.assertEqual(len([r for r in inventory if r["record_type"] == "vowel_column"]), 8)
        self.assertFalse(any(r["glyph_id"] is not None for r in inventory))


if __name__ == "__main__":
    unittest.main()
