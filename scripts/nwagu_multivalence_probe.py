"""Exploratory sign↔reading multivalence analysis for reviewed Nwagụ Aneke mappings.

Input must be an *adjudicated* sign-reading edge list. No built-in historical
glyph mappings exist; this tool cannot establish historical claims by itself.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations
import json
from pathlib import Path
from random import Random
from typing import Any


def read_edges(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        if not isinstance(record, dict):
            raise ValueError(f"line {i}: edge must be an object")
        rows.append(record)
    return rows


def study(edges: list[dict[str, Any]], *, permutations: int = 999, seed: int = 0) -> dict[str, Any]:
    if not edges:
        raise ValueError("no reviewed mapping edges; do not manufacture a result")
    if permutations < 1:
        raise ValueError("permutations must be positive")
    sign_to_readings: dict[str, set[str]] = defaultdict(set)
    reading_to_signs: dict[str, set[str]] = defaultdict(set)
    labels: dict[str, str | None] = {}
    unique_edges: set[tuple[str, str]] = set()
    for i, edge in enumerate(edges):
        sign, reading, locator = (edge.get(k) for k in ("sign_id", "reading_id", "source_locator"))
        if not all(isinstance(x, str) and x.strip() for x in (sign, reading, locator)):
            raise ValueError(f"edge[{i}]: nonempty sign_id, reading_id, source_locator required")
        if edge.get("review_status") != "human_adjudicated":
            raise ValueError(f"edge[{i}]: mapping not human_adjudicated")
        cls = edge.get("harmony_class")
        if cls is not None and (not isinstance(cls, str) or not cls.strip()):
            raise ValueError(f"edge[{i}]: invalid harmony_class")
        if reading in labels and labels[reading] != cls:
            raise ValueError(f"edge[{i}]: conflicting harmony classes for {reading}")
        labels[reading] = cls
        if (sign, reading) in unique_edges:
            raise ValueError(f"edge[{i}]: duplicate sign-reading pair")
        unique_edges.add((sign, reading))
        sign_to_readings[sign].add(reading)
        reading_to_signs[reading].add(sign)

    polyphonic = {k: v for k, v in sign_to_readings.items() if len(v) > 1}
    allographic = {k: v for k, v in reading_to_signs.items() if len(v) > 1}
    pairs = [
        (left, right)
        for readings in polyphonic.values()
        for left, right in combinations(sorted(readings), 2)
        if labels[left] is not None and labels[right] is not None
    ]
    eligible = len(pairs)
    observed = sum(labels[a] == labels[b] for a, b in pairs) / eligible if eligible else None

    # Shuffle *reading-class assignments*, not sign-reading edges. This
    # preserves the graph, all sign and reading degrees, and class frequencies.
    # It does not preserve dialectal CV restrictions or word/token frequency.
    distribution = Counter(x for x in labels.values() if x is not None)
    null: list[float] = []
    if eligible and len(distribution) >= 2:
        rng = Random(seed)
        known = sorted(k for k, v in labels.items() if v is not None)
        original_labels = [labels[k] for k in known]
        for _ in range(permutations):
            shuffled = list(original_labels)
            rng.shuffle(shuffled)
            assignment = dict(zip(known, shuffled))
            null.append(sum(assignment[a] == assignment[b] for a, b in pairs) / eligible)
    p_value = ((1 + sum(x >= observed for x in null)) / (len(null) + 1)) if null else None

    return {
        "status": "EXPLORATORY_REVIEWED_SAMPLE_NOT_REPERTOIRE_COMPLETENESS",
        "signs_in_sample": len(sign_to_readings),
        "readings_in_sample": len(reading_to_signs),
        "incidence_edges": len(unique_edges),
        "signs_with_multiple_readings": len(polyphonic),
        "readings_with_multiple_signs": len(allographic),
        "eligible_within_sign_reading_pairs": eligible,
        "same_class_pair_fraction": observed,
        "null_mean_same_class_fraction": sum(null) / len(null) if null else None,
        "permutation_tail_probability_exploratory": p_value,
        "permutations": len(null),
        "limits": [
            "Input sign identities and readings require independent domain adjudication.",
            "Vowel harmony classes must be preregistered for Umuleri, including treatment of neutral/unknown vowels.",
            "The permutation null preserves edges/degrees and class totals but not lexical frequencies or phonotactics.",
            "No result establishes a complete sign inventory or decipherment.",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edges", type=Path, required=True, help="Reviewed sign/reading JSONL, not a chart-cell index")
    parser.add_argument("--permutations", type=int, default=999)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args(argv)
    try:
        result = study(read_edges(args.edges), permutations=args.permutations, seed=args.seed)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
