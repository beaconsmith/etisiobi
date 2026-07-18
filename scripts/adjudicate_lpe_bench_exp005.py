from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"
ROLES = [
    "domain_source_reviewer",
    "methods_reviewer",
    "adversarial_impact_reviewer",
]


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def filled(row: dict[str, str]) -> bool:
    required = ["input_layer", "output_layer", "promotion_error", "severity", "rationale"]
    return all((row.get(key) or "").strip() for key in required)


def normalize_binary(value: str) -> str:
    lower = (value or "").strip().lower()
    if lower in {"yes", "true", "1", "lpe", "promotion"}:
        return "yes"
    if lower in {"no", "false", "0", "none"}:
        return "no"
    return lower


def normalize_severity(value: str) -> str:
    lower = (value or "").strip().lower()
    if lower in {"none", "minor", "material", "blocking"}:
        return lower
    return lower or "none"


def fleiss_kappa(label_matrix: list[list[str]]) -> float | None:
    if not label_matrix:
        return None
    n = len(label_matrix)
    m = len(label_matrix[0])
    if m < 2:
        return None
    categories = sorted({label for row in label_matrix for label in row})
    p_j = {cat: 0 for cat in categories}
    p_i_values = []
    for labels in label_matrix:
        counts = Counter(labels)
        p_i_values.append((sum(count * count for count in counts.values()) - m) / (m * (m - 1)))
        for cat in categories:
            p_j[cat] += counts.get(cat, 0)
    p_bar = sum(p_i_values) / n
    p_e = sum((count / (n * m)) ** 2 for count in p_j.values())
    if p_e == 1:
        return 1.0
    return round((p_bar - p_e) / (1 - p_e), 4)


def main() -> int:
    role_paths = [EXP5 / "annotation_inputs" / f"{role}.csv" for role in ROLES]
    if not all(path.exists() for path in role_paths):
        status = {
            "experiment_id": "EXP-FRONTIER-005",
            "generated_at": now(),
            "status": "ANNOTATION_FILES_MISSING",
            "frontier_claim_status": "not_ready",
        }
        write_json(EXP5 / "annotation_agreement.json", status)
        print(status["status"])
        return 0

    rows_by_role = {role: read_csv(path) for role, path in zip(ROLES, role_paths)}
    completion = {role: sum(1 for row in rows if filled(row)) for role, rows in rows_by_role.items()}
    total = len(next(iter(rows_by_role.values()))) if rows_by_role else 0
    if any(count < total for count in completion.values()):
        status = {
            "experiment_id": "EXP-FRONTIER-005",
            "generated_at": now(),
            "status": "ANNOTATION_INCOMPLETE_NOT_ADJUDICATED",
            "case_count": total,
            "completion_by_role": completion,
            "frontier_claim_status": "not_ready",
        }
        write_json(EXP5 / "annotation_agreement.json", status)
        write_text(
            EXP5 / "adjudication_report.md",
            f"""
# EXP-FRONTIER-005 Adjudication Report

Status: `ANNOTATION_INCOMPLETE_NOT_ADJUDICATED`

Completion by role:

{json.dumps(completion, indent=2)}

No gold labels were produced.
""",
        )
        print(status["status"])
        return 0

    by_case: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for role, rows in rows_by_role.items():
        for row in rows:
            by_case[row["case_id"]][role] = row

    promotion_matrix = []
    severity_matrix = []
    gold_rows: list[dict[str, Any]] = []
    for case_id, role_rows in sorted(by_case.items()):
        if len(role_rows) != len(ROLES):
            continue
        promotion_labels = [normalize_binary(role_rows[role]["promotion_error"]) for role in ROLES]
        severity_labels = [normalize_severity(role_rows[role]["severity"]) for role in ROLES]
        promotion_matrix.append(promotion_labels)
        severity_matrix.append(severity_labels)
        promo_vote = Counter(promotion_labels).most_common(1)[0][0]
        severity_vote = Counter(severity_labels).most_common(1)[0][0]
        # Conservative tie-break: any blocking/material concern remains visible.
        if len(Counter(severity_labels)) > 1 and "blocking" in severity_labels:
            severity_vote = "blocking"
        if len(Counter(severity_labels)) > 1 and severity_vote == "none" and "material" in severity_labels:
            severity_vote = "material"
        first = role_rows[ROLES[0]]
        gold_rows.append(
            {
                "case_id": case_id,
                "claim_text": first["claim_text"],
                "input_layer": Counter([role_rows[role]["input_layer"].strip() for role in ROLES]).most_common(1)[0][0],
                "output_layer": Counter([role_rows[role]["output_layer"].strip() for role in ROLES]).most_common(1)[0][0],
                "promotion_error": promo_vote,
                "severity": severity_vote,
                "adjudication_rationale": "Majority vote with conservative severity tie-break.",
                "source_review_status": "reviewed_by_three_roles",
                "public_release_ok": "needs_rights_review",
            }
        )

    agreement = {
        "experiment_id": "EXP-FRONTIER-005",
        "generated_at": now(),
        "status": "ANNOTATION_ADJUDICATED_GOLD_CREATED_AI_REVIEW_NOT_HUMAN_FRONTIER_READY",
        "case_count": len(gold_rows),
        "promotion_error_fleiss_kappa": fleiss_kappa(promotion_matrix),
        "severity_fleiss_kappa": fleiss_kappa(severity_matrix),
        "completion_by_role": completion,
        "annotation_source": "ai_reviewer_team",
        "human_domain_review_status": "missing",
        "frontier_claim_status": "not_ready",
        "remaining_gate": "Human/domain labels, agent runs, rights review, and review-team approval still required.",
    }
    write_csv(EXP5 / "gold_labels.csv", gold_rows)
    write_json(EXP5 / "annotation_agreement.json", agreement)
    write_text(
        EXP5 / "adjudication_report.md",
        f"""
# EXP-FRONTIER-005 Adjudication Report

Status: `{agreement['status']}`

- Cases: `{agreement['case_count']}`
- Promotion-error Fleiss kappa: `{agreement['promotion_error_fleiss_kappa']}`
- Severity Fleiss kappa: `{agreement['severity_fleiss_kappa']}`

Gold labels were produced by majority vote with conservative severity
tie-breaks. They are still not sufficient for frontier claims until agent runs,
rights review, and review-team approval are complete.
""",
    )
    print("LPE_EXP005_ADJUDICATED")
    print(f"cases={len(gold_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
