from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUESTIONS = (
    ROOT
    / "research"
    / "frontier"
    / "nwagu_aneke"
    / "interfaces"
    / "usability"
    / "count_layer_comprehension_questions.csv"
)

RESULT_FIELDS = {
    "respondent_id",
    "date",
    "role",
    "question_id",
    "answer",
    "expected_layer",
    "correct",
    "confusion_type",
    "notes",
}

MIN_READERS = 3
MAX_READERS = 5
MIN_PASS_RATE = 0.8
DERIVED_27_216_QUESTION_IDS = {"Q02"}
HARD_STOP_CONFUSIONS = {
    "source_derived_collapse",
    "absence_claim_error",
    "speculation_promoted",
    "computation_promoted",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_score(value: str) -> str:
    normalized = value.strip().lower()
    if normalized in {"correct", "true", "yes", "1"}:
        return "correct"
    if normalized in {"partial", "partly", "maybe"}:
        return "partial"
    if normalized in {"incorrect", "false", "no", "0", "wrong"}:
        return "incorrect"
    return normalized


def correct_rate(rows: list[dict[str, str]]) -> float:
    if not rows:
        return 0.0
    return sum(1 for row in rows if normalize_score(row.get("correct", "")) == "correct") / len(rows)


def score_results(questions_path: Path, results_path: Path) -> dict[str, Any]:
    questions = load_csv(questions_path)
    results = load_csv(results_path)
    question_layers = {row["question_id"]: row["target_layer"] for row in questions}
    required_question_ids = set(question_layers)
    blocking_issues: list[str] = []
    invalid_issues: list[str] = []

    if not results:
        invalid_issues.append("no result rows")
        return build_report("INVALID_READER_RUN", 0, 0.0, 0.0, invalid_issues)

    missing_fields = sorted(RESULT_FIELDS - set(results[0].keys()))
    if missing_fields:
        invalid_issues.append(f"results CSV missing fields: {', '.join(missing_fields)}")
        return build_report("INVALID_READER_RUN", 0, 0.0, 0.0, invalid_issues)

    by_respondent: dict[str, list[dict[str, str]]] = {}
    for line_number, row in enumerate(results, start=2):
        respondent_id = row.get("respondent_id", "").strip()
        question_id = row.get("question_id", "").strip()
        if not respondent_id:
            invalid_issues.append(f"row {line_number} missing respondent_id")
            continue
        if question_id not in required_question_ids:
            invalid_issues.append(f"{respondent_id} unknown question: {question_id or '<blank>'}")
            continue

        expected_layer = row.get("expected_layer", "").strip()
        if expected_layer != question_layers[question_id]:
            invalid_issues.append(
                f"{respondent_id} {question_id} expected_layer mismatch: "
                f"{expected_layer or '<blank>'} != {question_layers[question_id]}"
            )

        by_respondent.setdefault(respondent_id, []).append(row)

    reader_count = len(by_respondent)
    if reader_count < MIN_READERS or reader_count > MAX_READERS:
        invalid_issues.append(f"reader count must be 3-5, got {reader_count}")

    for respondent_id, rows in sorted(by_respondent.items()):
        seen: set[str] = set()
        duplicates: set[str] = set()
        for row in rows:
            question_id = row["question_id"]
            if question_id in seen:
                duplicates.add(question_id)
            seen.add(question_id)

        missing = sorted(required_question_ids - seen)
        if missing:
            invalid_issues.append(f"{respondent_id} missing questions: {', '.join(missing)}")
        if duplicates:
            invalid_issues.append(f"{respondent_id} duplicate questions: {', '.join(sorted(duplicates))}")

    overall = correct_rate(results)
    derived_rows = [row for row in results if row.get("question_id") in DERIVED_27_216_QUESTION_IDS]
    derived_rate = correct_rate(derived_rows)

    if invalid_issues:
        return build_report("INVALID_READER_RUN", reader_count, overall, derived_rate, invalid_issues)

    if overall < MIN_PASS_RATE:
        blocking_issues.append("overall comprehension below 80%")
    if derived_rate < MIN_PASS_RATE:
        blocking_issues.append("27/216 derived distinction below 80%")

    for row in results:
        score = normalize_score(row.get("correct", ""))
        confusion = row.get("confusion_type", "").strip()
        if score == "incorrect" and confusion in HARD_STOP_CONFUSIONS:
            blocking_issues.append(f"hard-stop confusion: {row['respondent_id']} {row['question_id']} {confusion}")

    if blocking_issues:
        return build_report(
            "FAIL_LABEL_REVISION_REQUIRED",
            reader_count,
            overall,
            derived_rate,
            sorted(set(blocking_issues)),
        )

    return build_report(
        "PASS_INTERNAL_COMPREHENSION_CHECK",
        reader_count,
        overall,
        derived_rate,
        [],
    )


def build_report(
    status: str,
    reader_count: int,
    overall_correct_rate: float,
    derived_27_216_correct_rate: float,
    blocking_issues: list[str],
) -> dict[str, Any]:
    return {
        "status": status,
        "reader_count": reader_count,
        "overall_correct_rate": round(overall_correct_rate, 4),
        "derived_27_216_correct_rate": round(derived_27_216_correct_rate, 4),
        "minimum_pass_rate": MIN_PASS_RATE,
        "blocking_issues": blocking_issues,
        "claim_ceiling": "human_comprehension_signal_not_source_evidence",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Score Nwagu Aneke count-layer comprehension results.")
    parser.add_argument("results", type=Path, help="CSV file with human reader responses.")
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS, help="Question CSV path.")
    args = parser.parse_args(argv)

    report = score_results(args.questions, args.results)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "PASS_INTERNAL_COMPREHENSION_CHECK" else 1


if __name__ == "__main__":
    raise SystemExit(main())
