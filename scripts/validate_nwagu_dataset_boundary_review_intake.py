from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
INTAKE_DIR = EXP_DIR / "dataset_boundary" / "review_gate" / "intake"
FORMS_DIR = INTAKE_DIR / "role_forms"
COLLECTED_DIR = INTAKE_DIR / "collected_reviews"
DISPATCH_DIR = INTAKE_DIR / "dispatch"
DISPATCH_TEMPLATES_DIR = DISPATCH_DIR / "invitation_templates"
CONTACT_DIR = DISPATCH_DIR / "contact_approval"

MANIFEST = INTAKE_DIR / "review_intake_manifest.json"
RUNBOOK = INTAKE_DIR / "REVIEW_INTAKE_RUNBOOK.md"
SCHEMA = INTAKE_DIR / "review_submission_schema.json"
COLLECTED_README = COLLECTED_DIR / "README.md"
DISPATCH_MANIFEST = DISPATCH_DIR / "dispatch_manifest.json"
DISPATCH_RUNBOOK = DISPATCH_DIR / "DISPATCH_RUNBOOK.md"
DISPATCH_TRACKER = DISPATCH_DIR / "dispatch_tracker.csv"
CONTACT_MANIFEST = CONTACT_DIR / "contact_approval_manifest.json"
CONTACT_RUNBOOK = CONTACT_DIR / "CONTACT_APPROVAL_RUNBOOK.md"
CONTACT_SELECTION_CRITERIA = CONTACT_DIR / "reviewer_selection_criteria.csv"
CONTACT_INTAKE = CONTACT_DIR / "contact_intake_template.csv"
CONTACT_APPROVAL_TEMPLATE = CONTACT_DIR / "send_approval_record_template.json"

REQUIRED_ROLES = {
    "rights_authority_reviewer",
    "community_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

REQUIRED_FILES = [
    MANIFEST,
    RUNBOOK,
    SCHEMA,
    COLLECTED_README,
    DISPATCH_MANIFEST,
    DISPATCH_RUNBOOK,
    DISPATCH_TRACKER,
    CONTACT_MANIFEST,
    CONTACT_RUNBOOK,
    CONTACT_SELECTION_CRITERIA,
    CONTACT_INTAKE,
    CONTACT_APPROVAL_TEMPLATE,
]

CLAIM_CEILING = "review_intake_ready_not_human_review"

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


def role_form_path(role: str) -> Path:
    return FORMS_DIR / f"{role}.md"


def dispatch_template_path(role: str) -> Path:
    return DISPATCH_TEMPLATES_DIR / f"{role}_invitation.md"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_manifest(errors: list[str]) -> None:
    manifest = read_json(MANIFEST)
    if manifest.get("intake_id") != "BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001":
        errors.append("intake_id must be BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001")
    if manifest.get("gate_id") != "BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001":
        errors.append("gate_id must be BOUNDARY-REVIEW-GATE-EXP-FRONTIER-008-001")
    if manifest.get("status") != "intake_ready_no_reviews_collected":
        errors.append("manifest status must be intake_ready_no_reviews_collected")
    if manifest.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"manifest claim_ceiling must be {CLAIM_CEILING}")
    if manifest.get("reviews_collected") != 0:
        errors.append("reviews_collected must be 0 until real review rows are added")
    if manifest.get("approvals_recorded") != []:
        errors.append("approvals_recorded must be empty")
    if manifest.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if set(manifest.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("manifest required_roles must exactly match required roles")

    forms = manifest.get("role_forms", {})
    for role in REQUIRED_ROLES:
        expected = f"experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/{role}.md"
        if forms.get(role) != expected:
            errors.append(f"{role}: role_forms path must be {expected}")


def validate_schema(errors: list[str]) -> None:
    schema = read_json(SCHEMA)
    if schema.get("$id") != "etisiobi:nwagu:dataset-boundary-review-submission:v1":
        errors.append("schema $id must be etisiobi:nwagu:dataset-boundary-review-submission:v1")
    if schema.get("status") != "schema_for_future_human_rows_not_current_review":
        errors.append("schema status must be schema_for_future_human_rows_not_current_review")
    if schema.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"schema claim_ceiling must be {CLAIM_CEILING}")

    properties = schema.get("properties", {})
    for field in [
        "role",
        "reviewer_name",
        "reviewed_at",
        "status",
        "summary",
        "files_reviewed",
        "blocking_issues",
        "attestation",
        "agent_generated_placeholder",
        "may_approve_boundary_alone",
    ]:
        if field not in properties:
            errors.append(f"schema missing property: {field}")

    required = set(schema.get("required", []))
    for field in [
        "role",
        "reviewer_name",
        "reviewed_at",
        "status",
        "summary",
        "files_reviewed",
        "blocking_issues",
        "attestation",
        "agent_generated_placeholder",
        "may_approve_boundary_alone",
    ]:
        if field not in required:
            errors.append(f"schema required missing: {field}")

    role_enum = set(properties.get("role", {}).get("enum", []))
    if role_enum != REQUIRED_ROLES:
        errors.append("schema role enum must exactly match required roles")
    status_enum = properties.get("status", {}).get("enum", [])
    if status_enum != ["PASS", "REJECT", "REVISE"]:
        errors.append("schema status enum must be PASS, REJECT, REVISE")


def validate_role_forms(errors: list[str]) -> None:
    for role in REQUIRED_ROLES:
        path = role_form_path(role)
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for required in [
            role,
            "review packet",
            "pass",
            "reject",
            "revise",
            "blocking issues",
            "attestation",
            "agent may not approve",
            CLAIM_CEILING,
        ]:
            if required.lower() not in lower:
                errors.append(f"{role}: form missing required phrase: {required}")


def validate_collected_readme(errors: list[str]) -> None:
    text = COLLECTED_README.read_text(encoding="utf-8")
    lower = text.lower()
    for required in [
        "no review rows collected yet",
        "do not add agent-generated approvals",
        "real human review rows",
        CLAIM_CEILING,
    ]:
        if required.lower() not in lower:
            errors.append(f"collected reviews README missing required phrase: {required}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        validate_manifest(errors)
        validate_schema(errors)
        validate_role_forms(errors)
        validate_collected_readme(errors)

        all_paths = REQUIRED_FILES + [role_form_path(role) for role in sorted(REQUIRED_ROLES)]
        all_paths += [dispatch_template_path(role) for role in sorted(REQUIRED_ROLES)]
        combined = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in all_paths
            if path.exists()
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden intake claim: {forbidden}")
        for required in [
            "review intake",
            "role-specific form",
            "real human review rows",
            "agent may not approve",
            "contact approval",
            CLAIM_CEILING,
        ]:
            if required.lower() not in combined:
                errors.append(f"intake packet missing required phrase: {required}")

    if errors:
        print("NWAGU_DATASET_BOUNDARY_REVIEW_INTAKE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_DATASET_BOUNDARY_REVIEW_INTAKE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
