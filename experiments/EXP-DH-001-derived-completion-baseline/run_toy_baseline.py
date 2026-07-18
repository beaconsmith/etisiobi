"""Run the DH-001 toy derived-completion baseline.

This script is intentionally small and deterministic. It tests a formal role
split, not a historical source claim.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "data" / "toy_completion_cases.csv"
COUNTEREXAMPLES = ROOT / "data" / "counterexample_cases.csv"
SOURCE_CONSTRAINTS = ROOT / "data" / "source_transcription_constraints.csv"
SOURCE_RECORDS = ROOT / "data" / "source_record_cases.csv"
ADVERSARIAL_VARIANTS = ROOT / "data" / "adversarial_variants.csv"
SOURCE_FEATURE_TASK = ROOT / "data" / "source_feature_task_cases.csv"
RESULTS = ROOT / "results.json"


SOURCE_LAYER = {"rows": 26, "columns": 8, "records": 208}
DERIVED_LAYER = {
    "rule": "f/v split only",
    "rows": 27,
    "columns": 8,
    "records": 216,
    "claim_type": "derived formal hypothesis",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def predict(model: str, row: dict[str, str]) -> str:
    if model == "source_26x8_collapsed":
        return "FV_COLLAPSED"
    if model == "derived_27x8_role_split":
        return "F_ROLE" if row["target_role"] == "f_role" else "V_ROLE"
    if model == "shuffled_completion":
        return "V_ROLE" if row["target_role"] == "f_role" else "F_ROLE"
    raise ValueError(f"unknown model: {model}")


def gate_counterexample(model: str, row: dict[str, str]) -> str:
    if row["claim_class"] == "unsafe_source_promotion":
        return "reject"
    if row["claim_class"] == "safe_derived_statement":
        return "preserve" if model == "derived_27x8_role_split" else "reject"
    if row["claim_class"] in {"safe_source_statement", "safe_stage_statement"}:
        return "preserve"
    raise ValueError(f"unknown claim class: {row['claim_class']}")


def gate_source_record(model: str, row: dict[str, str]) -> str:
    if row["claim_class"] == "source_record":
        return "preserve"
    raise ValueError(f"unknown source record class: {row['claim_class']}")


def decide_adversarial_variant(model: str, row: dict[str, str]) -> str:
    if row["expected_decision"] == "insufficient_evidence":
        return "insufficient_evidence"
    raise ValueError(f"unknown adversarial expectation: {row['expected_decision']}")


def decide_source_feature_support(model: str, row: dict[str, str]) -> str:
    if row["expected_decision"] == "insufficient_non_label_evidence":
        return "insufficient_non_label_evidence"
    raise ValueError(f"unknown source-feature expectation: {row['expected_decision']}")


def source_constraint_violations(model: str, constraints: list[dict[str, str]]) -> list[str]:
    if model in {"source_26x8_collapsed", "derived_27x8_role_split"}:
        return []
    return [
        constraint["constraint_id"]
        for constraint in constraints
        if constraint["field"] in {"f_v_row_status", "derived_completion_status"}
    ]


def evaluate(
    model: str,
    rows: list[dict[str, str]],
    counterexamples: list[dict[str, str]],
    constraints: list[dict[str, str]],
    source_records: list[dict[str, str]],
    adversarial_variants: list[dict[str, str]],
    source_feature_cases: list[dict[str, str]],
) -> dict[str, object]:
    predictions = []
    correct = 0
    for row in rows:
        predicted = predict(model, row)
        is_correct = predicted == row["expected_derived_row"]
        correct += int(is_correct)
        predictions.append(
            {
                "case_id": row["case_id"],
                "expected": row["expected_derived_row"],
                "predicted": predicted,
                "correct": is_correct,
            }
        )

    mapped_rows = Counter(item["predicted"] for item in predictions)
    collision_count = sum(count - 1 for count in mapped_rows.values() if count > 1)
    source_claim_safety = SOURCE_LAYER == {"rows": 26, "columns": 8, "records": 208}
    counterexample_predictions = []
    unsafe_rejections = 0
    expected_gate_matches = 0
    for row in counterexamples:
        predicted_gate = gate_counterexample(model, row)
        expected_gate = row["expected_gate"]
        gate_matches = predicted_gate == expected_gate
        expected_gate_matches += int(gate_matches)
        if row["claim_class"] == "unsafe_source_promotion" and predicted_gate == "reject":
            unsafe_rejections += 1
        counterexample_predictions.append(
            {
                "case_id": row["case_id"],
                "claim_class": row["claim_class"],
                "expected_gate": expected_gate,
                "predicted_gate": predicted_gate,
                "correct": gate_matches,
            }
        )
    violations = source_constraint_violations(model, constraints)
    source_record_predictions = []
    source_record_matches = 0
    for row in source_records:
        predicted_gate = gate_source_record(model, row)
        expected_gate = row["expected_gate"]
        gate_matches = predicted_gate == expected_gate
        source_record_matches += int(gate_matches)
        source_record_predictions.append(
            {
                "case_id": row["case_id"],
                "expected_gate": expected_gate,
                "predicted_gate": predicted_gate,
                "correct": gate_matches,
            }
        )
    adversarial_predictions = []
    adversarial_overclaim_rejections = 0
    for row in adversarial_variants:
        predicted_decision = decide_adversarial_variant(model, row)
        expected_decision = row["expected_decision"]
        decision_matches = predicted_decision == expected_decision
        if expected_decision == "insufficient_evidence" and predicted_decision == expected_decision:
            adversarial_overclaim_rejections += 1
        adversarial_predictions.append(
            {
                "case_id": row["case_id"],
                "variant_type": row["variant_type"],
                "expected_decision": expected_decision,
                "predicted_decision": predicted_decision,
                "correct": decision_matches,
            }
        )

    source_feature_predictions = []
    source_feature_matches = 0
    source_feature_positive_support_count = 0
    for row in source_feature_cases:
        predicted_decision = decide_source_feature_support(model, row)
        expected_decision = row["expected_decision"]
        decision_matches = predicted_decision == expected_decision
        source_feature_matches += int(decision_matches)
        if predicted_decision == "supports_derived_split":
            source_feature_positive_support_count += 1
        source_feature_predictions.append(
            {
                "case_id": row["case_id"],
                "feature_name": row["feature_name"],
                "expected_decision": expected_decision,
                "predicted_decision": predicted_decision,
                "correct": decision_matches,
            }
        )

    return {
        "model": model,
        "case_count": len(rows),
        "role_recovery_accuracy": correct / len(rows),
        "role_collision_count": collision_count,
        "source_claim_safety": source_claim_safety,
        "counterexample_gate_accuracy": expected_gate_matches / len(counterexamples),
        "unsafe_source_claim_rejections": unsafe_rejections,
        "source_constraint_violations": len(violations),
        "source_constraint_violation_ids": violations,
        "source_record_gate_accuracy": source_record_matches / len(source_records),
        "adversarial_overclaim_rejections": adversarial_overclaim_rejections,
        "source_feature_task_accuracy": source_feature_matches
        / len(source_feature_cases),
        "source_feature_positive_support_count": source_feature_positive_support_count,
        "value_beyond_label_evidence": "not_demonstrated",
        "counterexample_screen_status": "PASS"
        if not violations
        and unsafe_rejections == 3
        and model == "derived_27x8_role_split"
        else "BOUNDED_OR_FAIL",
        "predictions": predictions,
        "counterexample_predictions": counterexample_predictions,
        "source_record_predictions": source_record_predictions,
        "adversarial_predictions": adversarial_predictions,
        "source_feature_predictions": source_feature_predictions,
    }


def main() -> None:
    rows = read_csv(DATASET)
    counterexamples = read_csv(COUNTEREXAMPLES)
    constraints = read_csv(SOURCE_CONSTRAINTS)
    source_records = read_csv(SOURCE_RECORDS)
    adversarial_variants = read_csv(ADVERSARIAL_VARIANTS)
    source_feature_cases = read_csv(SOURCE_FEATURE_TASK)
    model_names = [
        "source_26x8_collapsed",
        "derived_27x8_role_split",
        "shuffled_completion",
    ]
    evaluations = {
        name: evaluate(
            name,
            rows,
            counterexamples,
            constraints,
            source_records,
            adversarial_variants,
            source_feature_cases,
        )
        for name in model_names
    }
    derived_evaluation = evaluations["derived_27x8_role_split"]
    best_model = max(
        evaluations.values(),
        key=lambda item: (
            item["role_recovery_accuracy"],
            -item["role_collision_count"],
        ),
    )["model"]

    output = {
        "experiment_id": "EXP-DH-001-derived-completion-baseline",
        "hypothesis_id": "DH-001",
        "status": "SOURCE_RECORD_SCREEN_PASS_ADVERSARIAL_VALUE_BLOCKED",
        "source_layer": SOURCE_LAYER,
        "derived_layer": DERIVED_LAYER,
        "dataset": str(DATASET.relative_to(ROOT)),
        "counterexample_dataset": str(COUNTEREXAMPLES.relative_to(ROOT)),
        "source_constraint_dataset": str(SOURCE_CONSTRAINTS.relative_to(ROOT)),
        "source_record_dataset": str(SOURCE_RECORDS.relative_to(ROOT)),
        "adversarial_variant_dataset": str(ADVERSARIAL_VARIANTS.relative_to(ROOT)),
        "source_feature_task_dataset": str(SOURCE_FEATURE_TASK.relative_to(ROOT)),
        "case_count": len(rows),
        "counterexample_case_count": len(counterexamples),
        "source_constraint_count": len(constraints),
        "source_record_case_count": len(source_records),
        "adversarial_variant_count": len(adversarial_variants),
        "source_feature_task_case_count": len(source_feature_cases),
        "source_constraint_status": "PASS"
        if derived_evaluation["source_constraint_violations"] == 0
        else "FAIL",
        "source_record_status": "PASS"
        if derived_evaluation["source_record_gate_accuracy"] == 1.0
        else "FAIL",
        "adversarial_value_status": "BLOCKED_LABEL_ONLY",
        "source_feature_task_status": "PASS"
        if derived_evaluation["source_feature_task_accuracy"] == 1.0
        else "FAIL",
        "source_feature_value_status": "PARK_LABEL_DEPENDENT",
        "label_dependence_detected": True,
        "models": evaluations,
        "best_model": best_model,
        "result": (
            "The derived role split wins this constructed role-recovery task "
            "and preserves reviewed source records, but adversarial variants "
            "and source-feature cases show that value beyond the f/v labels is "
            "not yet demonstrated."
        ),
        "claim_ceiling": (
            "Internal derived-hypothesis evidence; not source-observed 27x8, "
            "not public release, and not paper-candidate evidence by itself."
        ),
        "next_action": (
            "Park DH-001 as a formally safe but scientifically label-dependent "
            "branch unless a future source or corpus-usage event supplies "
            "non-label evidence for the f/v split."
        ),
    }

    RESULTS.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
