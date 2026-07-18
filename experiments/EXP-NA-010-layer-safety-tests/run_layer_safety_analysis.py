from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "expanded_layer_safety_cases.csv"
EXPANDED_JSONL = ROOT / "data" / "expanded_layer_safety_cases.jsonl"
EXPANDED_RESULTS = ROOT / "expanded_results.json"
BASELINE_RESULTS = ROOT / "baseline_comparison.json"

RANK = {
    "source_observed": 0,
    "derived": 1,
    "speculative": 2,
    "blocked": 3,
}


def as_bool(value: str) -> bool:
    return value.strip().lower() == "yes"


def layer_gate(input_label: str, output_label: str) -> str:
    return "reject" if RANK[output_label] < RANK[input_label] else "allow"


def provenance_only(row: dict[str, str]) -> str:
    return "allow" if as_bool(row["provenance_link"]) else "reject"


def citation_only(row: dict[str, str]) -> str:
    return "allow" if as_bool(row["citation_present"]) else "reject"


def no_label_gate(row: dict[str, str]) -> str:
    return "allow"


def main() -> int:
    rows = [
        {key: value.strip() for key, value in row.items()}
        for row in csv.DictReader(DATA.read_text(encoding="utf-8").splitlines())
    ]
    mismatches: list[str] = []
    evaluated: list[dict[str, object]] = []
    baseline_false_negatives = {
        "provenance_only": 0,
        "citation_only": 0,
        "no_label_gate": 0,
    }
    promotion_errors = 0
    detected = 0

    for row in rows:
        expected = row["expected_gate_decision"].strip()
        actual = layer_gate(row["input_label"].strip(), row["output_label"].strip())
        promotion_error = actual == "reject"
        promotion_errors += int(promotion_error)
        detected += int(promotion_error and actual == expected)

        base_decisions = {
            "provenance_only": provenance_only(row),
            "citation_only": citation_only(row),
            "no_label_gate": no_label_gate(row),
        }
        for name, decision in base_decisions.items():
            if promotion_error and decision == "allow":
                baseline_false_negatives[name] += 1

        if actual != expected:
            mismatches.append(f"{row['case_id']}: expected {expected}, got {actual}")

        evaluated.append(
            {
                **row,
                "promotion_error": promotion_error,
                "layer_gate_decision": actual,
                "baseline_decisions": base_decisions,
            }
        )

    EXPANDED_JSONL.write_text(
        "\n".join(json.dumps(row, sort_keys=True) for row in evaluated) + "\n",
        encoding="utf-8",
    )
    EXPANDED_RESULTS.write_text(
        json.dumps(
            {
                "experiment_id": "EXP-NA-010",
                "result_type": "expanded layer-safety invariant evaluation",
                "test_cases": len(rows),
                "promotion_errors": promotion_errors,
                "promotion_errors_detected": detected,
                "promotion_error_detection_rate": detected / promotion_errors
                if promotion_errors
                else 1.0,
                "gate_mismatches": mismatches,
                "decision": "EXPANDED_LAYER_SAFETY_BASELINE_COMPARISON_PASS"
                if not mismatches
                else "EXPANDED_LAYER_SAFETY_BASELINE_COMPARISON_FAIL",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    BASELINE_RESULTS.write_text(
        json.dumps(
            {
                "experiment_id": "EXP-NA-010",
                "baselines": {
                    "provenance_only": {
                        "false_negatives_on_promotion_errors": baseline_false_negatives[
                            "provenance_only"
                        ],
                        "interpretation": "A provenance link can coexist with unsafe layer promotion.",
                    },
                    "citation_only": {
                        "false_negatives_on_promotion_errors": baseline_false_negatives[
                            "citation_only"
                        ],
                        "interpretation": "A citation can coexist with unsafe layer promotion.",
                    },
                    "no_label_gate": {
                        "false_negatives_on_promotion_errors": baseline_false_negatives[
                            "no_label_gate"
                        ],
                        "interpretation": "A gate without evidence-layer labels cannot reject promotions.",
                    },
                },
                "layer_gate_false_negatives_on_promotion_errors": len(mismatches),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    if mismatches:
        print("EXP_NA_010_LAYER_SAFETY_FAIL")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1

    print("EXP_NA_010_LAYER_SAFETY_PASS")
    print(f"cases={len(rows)}")
    print(f"promotion_errors={promotion_errors}")
    print("baselines_false_negatives=" + json.dumps(baseline_false_negatives, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
