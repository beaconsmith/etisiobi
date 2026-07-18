from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
BOUNDARY_DIR = EXP_DIR / "dataset_boundary"
GATE_DIR = BOUNDARY_DIR / "review_gate"

GATE_JSON = GATE_DIR / "review_gate.json"
GATE_MD = GATE_DIR / "REVIEW_GATE.md"
REQUESTS_CSV = GATE_DIR / "review_requests.csv"
TRACE_TEMPLATE = GATE_DIR / "review_trace_template.jsonl"
DECISION_TEMPLATE = GATE_DIR / "decision_record_template.json"

REQUIRED_FILES = [
    GATE_JSON,
    GATE_MD,
    REQUESTS_CSV,
    TRACE_TEMPLATE,
    DECISION_TEMPLATE,
]

REQUIRED_ROLES = {
    "rights_authority_reviewer",
    "community_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

CLAIM_CEILING = "review_gate_pending_not_boundary_approval"

FORBIDDEN_TEXT = [
    "boundary approved",
    "dataset boundary approved",
    "public release approved",
    "rights cleared",
    "authority approved",
    "datalad dataset created",
    "software heritage save requested",
    "swhid assigned",
    "paper-ready",
    "submission-ready",
    "source-observed 27/216",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_gate(errors: list[str]) -> None:
    gate = read_json(GATE_JSON)
    if gate.get("gate_id") != "BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001":
        errors.append("gate_id must be BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001")
    if gate.get("boundary_id") != "BOUNDARY-EXP-FRONTIER-008-001":
        errors.append("boundary_id must be BOUNDARY-EXP-FRONTIER-008-001")
    if gate.get("status") != "pending_human_review":
        errors.append("gate status must be pending_human_review")
    if gate.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"gate claim_ceiling must be {CLAIM_CEILING}")
    if gate.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if gate.get("approvals_recorded") != []:
        errors.append("approvals_recorded must be empty")
    if set(gate.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("gate required_roles must exactly match required boundary roles")

    for action in [
        "approve dataset boundary",
        "create DataLad dataset",
        "request Software Heritage save",
        "deposit public package",
        "include restricted source material",
        "claim release readiness",
    ]:
        if action not in set(gate.get("forbidden_agent_actions", [])):
            errors.append(f"gate missing forbidden agent action: {action}")


def validate_requests(errors: list[str]) -> None:
    rows = read_csv(REQUESTS_CSV)
    roles = {row.get("role_id") for row in rows}
    if roles != REQUIRED_ROLES:
        errors.append(f"review requests roles mismatch: {sorted(roles)}")
    for row in rows:
        role = row.get("role_id", "")
        if row.get("request_status") != "pending_human_review":
            errors.append(f"{role}: request_status must be pending_human_review")
        if row.get("may_agent_approve") != "no":
            errors.append(f"{role}: may_agent_approve must be no")
        if row.get("required_output") != "PASS_OR_REJECT_OR_REVISE_WITH_BLOCKERS":
            errors.append(f"{role}: required_output must be PASS_OR_REJECT_OR_REVISE_WITH_BLOCKERS")
        if not row.get("review_packet"):
            errors.append(f"{role}: review_packet is required")


def validate_trace_template(errors: list[str]) -> None:
    rows = read_jsonl(TRACE_TEMPLATE)
    roles = {row.get("role") for row in rows}
    if roles != REQUIRED_ROLES:
        errors.append(f"trace template roles mismatch: {sorted(roles)}")
    for row in rows:
        role = row.get("role", "")
        if row.get("status") != "PENDING_HUMAN_REVIEW":
            errors.append(f"{role}: trace status must be PENDING_HUMAN_REVIEW")
        if row.get("agent_generated_placeholder") is not True:
            errors.append(f"{role}: trace row must be marked agent_generated_placeholder=true")
        if row.get("may_be_used_as_approval") is not False:
            errors.append(f"{role}: trace row may_be_used_as_approval must be false")
        if row.get("blocking_issues") != ["human review not yet recorded"]:
            errors.append(f"{role}: blocking issue must state human review not yet recorded")


def validate_decision_template(errors: list[str]) -> None:
    decision = read_json(DECISION_TEMPLATE)
    if decision.get("decision_id") != "BOUNDARY-DECISION-EXP-FRONTIER-008-TEMPLATE":
        errors.append("decision template id must be BOUNDARY-DECISION-EXP-FRONTIER-008-TEMPLATE")
    if decision.get("status") != "template_not_decision":
        errors.append("decision template status must be template_not_decision")
    if decision.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"decision template claim_ceiling must be {CLAIM_CEILING}")
    if decision.get("may_be_used_as_approval") is not False:
        errors.append("decision template may_be_used_as_approval must be false")
    if decision.get("allowed_final_decisions") != ["PASS", "REJECT", "REVISE"]:
        errors.append("decision template allowed_final_decisions must be PASS, REJECT, REVISE")
    if set(decision.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("decision template required_roles must exactly match required roles")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        validate_gate(errors)
        validate_requests(errors)
        validate_trace_template(errors)
        validate_decision_template(errors)

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden review-gate claim: {forbidden}")
        for required in [
            "pending human review",
            "agent may not approve",
            "review gate",
            "review trace template",
            "decision record template",
            CLAIM_CEILING,
        ]:
            if required.lower() not in combined:
                errors.append(f"review gate missing required phrase: {required}")

    if errors:
        print("NWAGU_DATASET_BOUNDARY_REVIEW_GATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_DATASET_BOUNDARY_REVIEW_GATE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
