"""Evaluate DH-001 against a global-style benchmark gate."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results.json"
CRITERIA = ROOT / "data" / "global_benchmark_criteria.csv"
GATE_RESULTS = ROOT / "global_benchmark_gate_results.json"


def read_criteria() -> list[dict[str, str]]:
    with CRITERIA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def criterion_passed(criterion_id: str, results: dict[str, object]) -> bool:
    derived = results["models"]["derived_27x8_role_split"]
    if criterion_id == "GB-001":
        return (ROOT / "run_toy_baseline.py").exists() and (
            ROOT / "test_toy_baseline.py"
        ).exists()
    if criterion_id == "GB-002":
        required = [
            "dataset",
            "counterexample_dataset",
            "source_constraint_dataset",
            "source_record_dataset",
            "adversarial_variant_dataset",
            "source_feature_task_dataset",
        ]
        return all(name in results for name in required)
    if criterion_id == "GB-003":
        return set(results["models"]) == {
            "source_26x8_collapsed",
            "derived_27x8_role_split",
            "shuffled_completion",
        }
    if criterion_id == "GB-004":
        return (
            derived["unsafe_source_claim_rejections"] == 3
            and derived["adversarial_overclaim_rejections"] == 6
        )
    if criterion_id == "GB-005":
        required = [
            "role_recovery_accuracy",
            "counterexample_gate_accuracy",
            "source_record_gate_accuracy",
            "source_feature_task_accuracy",
        ]
        return all(name in derived for name in required)
    if criterion_id == "GB-006":
        return (
            results["source_layer"] == {"rows": 26, "columns": 8, "records": 208}
            and results["derived_layer"]["claim_type"] == "derived formal hypothesis"
        )
    if criterion_id == "GB-007":
        return (
            results["source_feature_value_status"] != "PARK_LABEL_DEPENDENT"
            and derived["source_feature_positive_support_count"] > 0
        )
    raise ValueError(f"unknown criterion: {criterion_id}")


def main() -> None:
    results = json.loads(RESULTS.read_text(encoding="utf-8"))
    criteria = read_criteria()
    evaluations = []
    for criterion in criteria:
        passed = criterion_passed(criterion["criterion_id"], results)
        evaluations.append(
            {
                "criterion_id": criterion["criterion_id"],
                "criterion_name": criterion["criterion_name"],
                "global_reference": criterion["global_reference"],
                "status": "PASS" if passed else "FAIL",
                "pass_condition": criterion["pass_condition"],
            }
        )

    failed = [item["criterion_name"] for item in evaluations if item["status"] == "FAIL"]
    passed_count = sum(1 for item in evaluations if item["status"] == "PASS")
    output = {
        "experiment_id": "EXP-DH-001-derived-completion-baseline",
        "hypothesis_id": "DH-001",
        "status": "GLOBAL_BENCHMARK_NEGATIVE_BREAKTHROUGH_PARK_DH001",
        "criteria_passed": passed_count,
        "criteria_failed": len(failed),
        "failed_criteria": failed,
        "global_benchmark_claim": "not_met",
        "decision": "PARK_DH001_BEFORE_PAPER_CANDIDATE",
        "celebration_worthy": failed == ["non_label_generalization"],
        "reason": (
            "DH-001 passes reproducibility, data, baseline, adversarial, "
            "transparency, and source-boundary checks, but fails the global "
            "breakthrough criterion because value beyond labels is not "
            "demonstrated."
        ),
        "evaluations": evaluations,
        "next_action": (
            "Park DH-001 unless a future source or corpus-usage event supplies "
            "non-label evidence for the f/v split."
        ),
    }
    GATE_RESULTS.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
