"""Read-only Nwagụ Aneke encoding-topology audit.

Distinguishes source-chart grid slots from glyph observations and checks an
exploratory vowel-onset hypothesis in two *selected* full-word lists. It does
not authenticate glyphs, estimate population prevalence, or prove intent.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import unicodedata
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BMC = ROOT / "corpus/base_modifier_cache.jsonl"
SOURCE_TOKENS = ROOT / "experiments/EXP-APP-001-count-layer-design-grammar/tokens_source_layer.jsonl"
LOGOGRAPHS = ROOT / "experiments/EXP-NA-004-logograph-ledger/data/logograph_leads.jsonl"
PUBLISHED = ROOT / "experiments/EXP-NA-021-contextual-encoding-topology/published_full_word_examples.json"
IGBO_VOWELS = frozenset("aeiouịọụẹ")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{n} must contain an object")
        rows.append(row)
    return rows


def begins_with_vowel(word: str) -> bool:
    normalized = unicodedata.normalize("NFC", word).strip().lower()
    return bool(normalized) and normalized[0] in IGBO_VOWELS


def audit(
    bmc: list[dict[str, Any]],
    source_tokens: list[dict[str, Any]],
    logographs: list[dict[str, Any]],
    published: dict[str, Any],
) -> dict[str, Any]:
    errors: list[str] = []
    bmc_by_id: dict[str, dict[str, Any]] = {}
    slots: set[tuple[str, str]] = set()
    row_labels: set[str] = set()
    vowels: set[str] = set()
    for i, row in enumerate(bmc):
        identifier = row.get("bmc_id")
        pair = (row.get("row_label"), row.get("vowel_label"))
        if not all(isinstance(v, str) and v for v in (identifier, *pair)):
            errors.append(f"BMC[{i}]: missing bmc_id, row_label, or vowel_label")
            continue
        if identifier in bmc_by_id or pair in slots:
            errors.append(f"BMC[{i}]: duplicated BMC identity or row/vowel pair")
        bmc_by_id[identifier] = row
        slots.add(pair)
        row_labels.add(pair[0])
        vowels.add(pair[1])

    if len(slots) != len(row_labels) * len(vowels):
        errors.append("BMC: row/vowel slots do not form a complete cartesian index")

    token_ids: set[str] = set()
    for i, token in enumerate(source_tokens):
        identifier = token.get("source_bmc_id")
        parent = bmc_by_id.get(identifier)
        if parent is None:
            errors.append(f"source_token[{i}]: unknown BMC parent {identifier!r}")
            continue
        if token.get("layer") != "source_observed" or token.get("source_observed") is not True:
            errors.append(f"source_token[{i}]: wrong source-layer label")
        if (token.get("token_id"), token.get("base"), token.get("modifier"), token.get("reading")) != (
            parent.get("cell_id"), parent.get("row_label"), parent.get("vowel_label"), parent.get("reading")
        ):
            errors.append(f"source_token[{i}]: grid-slot projection does not match parent")
        if identifier in token_ids:
            errors.append(f"source_token[{i}]: duplicate parent identity")
        token_ids.add(identifier)
    if len(token_ids) != len(bmc_by_id):
        errors.append("source tokens: not a one-to-one projection of BMC grid slots")

    for i, row in enumerate(logographs):
        if not isinstance(row.get("word"), str) or not row["word"].strip():
            errors.append(f"logograph[{i}]: missing word label")
    if not isinstance(published, dict) or not isinstance(published.get("words"), list):
        errors.append("published example record: missing words list")
        published_words = []
    else:
        published_words = published["words"]
        if not all(isinstance(w, str) and w.strip() for w in published_words):
            errors.append("published example record: malformed word label")
            published_words = [w for w in published_words if isinstance(w, str) and w.strip()]

    region_status = Counter(row.get("source_region_status", "missing") for row in bmc)
    review_status = Counter(row.get("review_status", "missing") for row in bmc)
    observation_ids = [row.get("glyph_observation_id") for row in bmc if row.get("glyph_observation_id")]
    observation_counts = Counter(observation_ids)
    locatable = sum(row.get("source_region") is not None for row in bmc)
    reviewed_locatable = sum(
        row.get("source_region") is not None
        and row.get("review_status") in {"human_reviewed", "approved", "verified"}
        for row in bmc
    )
    unreviewed = sum(row.get("review_status") == "human_review_needed" for row in bmc)
    chart_words = [row["word"] for row in logographs if isinstance(row.get("word"), str) and row["word"].strip()]
    author_counts = published.get("author_reported_counts", {})
    if not isinstance(author_counts, dict):
        author_counts = {}

    return {
        "valid_internal_index": not errors,
        "errors": errors,
        "chart_index": {
            "row_labels": len(row_labels),
            "vowel_labels": len(vowels),
            "grid_slots": len(bmc),
            "projected_source_tokens": len(source_tokens),
            "slot_type": "source_chart_row_vowel_index_not_verified_glyph_inventory",
        },
        "glyph_evidence": {
            "locatable_cell_regions": locatable,
            "reviewed_locatable_cell_regions": reviewed_locatable,
            "unreviewed_cell_slots": unreviewed,
            "distinct_glyph_observation_references": len(observation_counts),
            "reused_observation_references": sum(n > 1 for n in observation_counts.values()),
            "maximum_slots_per_observation_reference": max(observation_counts.values(), default=0),
            "source_region_status": dict(sorted(region_status.items())),
            "review_status": dict(sorted(review_status.items())),
            "glyph_repertoire_count_established": False,
        },
        "exploratory_full_word_onsets": {
            "chart_transcription": {
                "total": len(chart_words),
                "vowel_initial": sum(begins_with_vowel(w) for w in chart_words),
                "consonant_initial_labels": [w for w in chart_words if not begins_with_vowel(w)],
                "status": "selected_unreviewed_chart_transcription_not_population_estimate",
            },
            "published_examples": {
                "total": len(published_words),
                "vowel_initial": sum(begins_with_vowel(w) for w in published_words),
                "status": "selected_author_examples_not_population_estimate",
                "source_url": published.get("url"),
            },
        },
        "literature_claims": {
            "counts": author_counts,
            "status": "reported_by_author_not_independently_recounted_not_subtractable_from_grid_slots",
        },
        "research_decision": "CONTEXTUAL_ENCODING_HYPOTHESIS_TESTABLE_GLYPH_LEVEL_RECONSTRUCTION_BLOCKED",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bmc", type=Path, default=BMC)
    parser.add_argument("--source-tokens", type=Path, default=SOURCE_TOKENS)
    parser.add_argument("--logographs", type=Path, default=LOGOGRAPHS)
    parser.add_argument("--published", type=Path, default=PUBLISHED)
    args = parser.parse_args(argv)
    try:
        result = audit(
            read_jsonl(args.bmc),
            read_jsonl(args.source_tokens),
            read_jsonl(args.logographs),
            json.loads(args.published.read_text(encoding="utf-8")),
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid_internal_index": False, "errors": [str(exc)]}))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid_internal_index"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
