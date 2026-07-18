from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "research" / "frontier" / "nwagu_aneke" / "interfaces" / "usability"
README_PATH = PACKET_DIR / "README.md"
PROTOCOL_PATH = PACKET_DIR / "count_layer_comprehension_protocol.md"
QUESTIONS_PATH = PACKET_DIR / "count_layer_comprehension_questions.csv"
RESULTS_TEMPLATE_PATH = PACKET_DIR / "count_layer_comprehension_results_template.csv"
SELF_AUDIT_PATH = PACKET_DIR / "internal_self_audit.md"
RUN_SHEET_PATH = PACKET_DIR / "count_layer_reader_run_sheet.md"
SCORING_GUIDE_PATH = PACKET_DIR / "count_layer_response_scoring_guide.md"
RESPONSES_README_PATH = PACKET_DIR / "responses" / "README.md"
SCORER_PATH = ROOT / "scripts" / "score_count_layer_comprehension_results.py"

REQUIRED_FILES = [
    README_PATH,
    PROTOCOL_PATH,
    QUESTIONS_PATH,
    RESULTS_TEMPLATE_PATH,
    SELF_AUDIT_PATH,
    RUN_SHEET_PATH,
    SCORING_GUIDE_PATH,
    RESPONSES_README_PATH,
    SCORER_PATH,
]

QUESTION_FIELDS = {
    "question_id",
    "task_type",
    "target_record_id",
    "target_layer",
    "prompt",
    "expected_answer",
    "pass_rule",
    "confusion_type_if_wrong",
}

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

REQUIRED_QUESTION_COVERAGE = {
    "source_26_208": ("NA-FIX-001", "source_observed", ["26/208", "26 x 8", "208"]),
    "derived_27_216": ("NA-FIX-002", "derived_f_v", ["27/216", "derived", "not source-observed"]),
    "appendix_ii": ("NA-FIX-006", "restricted_blocked", ["Appendix II", "unrecovered"]),
    "speculative_pagc": ("NA-FIX-004", "speculative_frontier", ["PAGC", "speculative"]),
    "applied_design": ("NA-FIX-005", "applied_design", ["design", "lineage"]),
    "computational": ("NA-FIX-007", "computational_evaluation", ["computational", "not source evidence"]),
    "contested_counts": ("NA-FIX-008", "contested_counts", ["164", "224", "separate"]),
    "dropped_27_216": ("NA-FIX-010", "dropped_branches", ["source-observed 27/216", "dropped"]),
}

PROTOCOL_REQUIRED_PHRASES = [
    "not human evidence yet",
    "minimum pass threshold",
    "80%",
    "revise labels",
    "27/216",
    "26/208",
    "rights",
    "authority",
    "no source images",
    "score_count_layer_comprehension_results.py",
    "PASS_INTERNAL_COMPREHENSION_CHECK",
    "FAIL_LABEL_REVISION_REQUIRED",
    "human_comprehension_signal_not_source_evidence",
    "3-5 readers",
]

FORBIDDEN_PHRASES = [
    "public-ready",
    "publication-ready",
    "paper-ready",
    "ready for public release",
    "submission-ready",
    "source-observed 27/216 is valid",
    "human usability evidence complete",
]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def row_text(row: dict[str, str]) -> str:
    return " ".join(str(value) for value in row.values())


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        protocol = PROTOCOL_PATH.read_text(encoding="utf-8")
        readme = README_PATH.read_text(encoding="utf-8")
        self_audit = SELF_AUDIT_PATH.read_text(encoding="utf-8")
        run_sheet = RUN_SHEET_PATH.read_text(encoding="utf-8")
        scoring_guide = SCORING_GUIDE_PATH.read_text(encoding="utf-8")
        responses_readme = RESPONSES_README_PATH.read_text(encoding="utf-8")
        combined_markdown = "\n".join([protocol, readme, self_audit, run_sheet, scoring_guide, responses_readme])
        normalized_markdown = normalize(combined_markdown)

        for phrase in PROTOCOL_REQUIRED_PHRASES:
            if normalize(phrase) not in normalized_markdown:
                errors.append(f"missing protocol/readme/self-audit phrase: {phrase}")

        for phrase in FORBIDDEN_PHRASES:
            if normalize(phrase) in normalized_markdown:
                errors.append(f"forbidden readiness or promotion phrase: {phrase}")

        question_rows = load_csv(QUESTIONS_PATH)
        result_rows = load_csv(RESULTS_TEMPLATE_PATH)

        if not question_rows:
            errors.append("question CSV must contain at least one question row")
        else:
            missing_fields = sorted(QUESTION_FIELDS - set(question_rows[0].keys()))
            if missing_fields:
                errors.append(f"question CSV missing fields {missing_fields}")

        if not result_rows:
            errors.append("results template CSV must contain at least one example/header row")
        else:
            missing_result_fields = sorted(RESULT_FIELDS - set(result_rows[0].keys()))
            if missing_result_fields:
                errors.append(f"results template CSV missing fields {missing_result_fields}")

        if question_rows and QUESTION_FIELDS.issubset(question_rows[0].keys()):
            seen_ids: set[str] = set()
            for index, row in enumerate(question_rows, start=2):
                question_id = row.get("question_id", "").strip()
                if not question_id:
                    errors.append(f"questions row {index}: missing question_id")
                elif question_id in seen_ids:
                    errors.append(f"{question_id}: duplicate question_id")
                seen_ids.add(question_id)

                for field in QUESTION_FIELDS:
                    if not row.get(field, "").strip():
                        errors.append(f"{question_id or 'questions row ' + str(index)}: empty {field}")

            for coverage_name, (record_id, layer, required_phrases) in REQUIRED_QUESTION_COVERAGE.items():
                matches = [
                    row
                    for row in question_rows
                    if row.get("target_record_id") == record_id and row.get("target_layer") == layer
                ]
                if not matches:
                    errors.append(f"missing question coverage: {coverage_name}")
                    continue

                matched_text = normalize(" ".join(row_text(row) for row in matches))
                for phrase in required_phrases:
                    if normalize(phrase) not in matched_text:
                        errors.append(f"{coverage_name}: missing required phrase {phrase!r}")

    if errors:
        print("COUNT_LAYER_USABILITY_PACKET_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("COUNT_LAYER_USABILITY_PACKET_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
