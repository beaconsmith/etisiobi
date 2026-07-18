from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
DISPATCH_DIR = EXP_DIR / "dataset_boundary" / "review_gate" / "intake" / "dispatch"
CONTACT_DIR = DISPATCH_DIR / "contact_approval"

MANIFEST = CONTACT_DIR / "contact_approval_manifest.json"
RUNBOOK = CONTACT_DIR / "CONTACT_APPROVAL_RUNBOOK.md"
SELECTION_CRITERIA = CONTACT_DIR / "reviewer_selection_criteria.csv"
CONTACT_INTAKE = CONTACT_DIR / "contact_intake_template.csv"
APPROVAL_TEMPLATE = CONTACT_DIR / "send_approval_record_template.json"

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
    SELECTION_CRITERIA,
    CONTACT_INTAKE,
    APPROVAL_TEMPLATE,
]

CONTACT_APPROVAL_ID = "BOUNDARY-REVIEW-CONTACT-APPROVAL-EXP-FRONTIER-008-001"
DISPATCH_ID = "BOUNDARY-REVIEW-DISPATCH-EXP-FRONTIER-008-001"
CLAIM_CEILING = "contact_approval_packet_ready_not_dispatch_approval"

FORBIDDEN_TEXT = [
    "sent to reviewer",
    "review request sent",
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


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_manifest(errors: list[str]) -> None:
    manifest = read_json(MANIFEST)
    if manifest.get("contact_approval_id") != CONTACT_APPROVAL_ID:
        errors.append(f"contact_approval_id must be {CONTACT_APPROVAL_ID}")
    if manifest.get("dispatch_id") != DISPATCH_ID:
        errors.append(f"dispatch_id must be {DISPATCH_ID}")
    if manifest.get("status") != "contact_approval_packet_ready_no_contacts_no_send_approval":
        errors.append("manifest status must be contact_approval_packet_ready_no_contacts_no_send_approval")
    if manifest.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"manifest claim_ceiling must be {CLAIM_CEILING}")
    if manifest.get("contacts_recorded") != 0:
        errors.append("contacts_recorded must be 0")
    if manifest.get("approvals_to_send_recorded") != 0:
        errors.append("approvals_to_send_recorded must be 0")
    if manifest.get("messages_sent") != 0:
        errors.append("messages_sent must be 0")
    if manifest.get("private_contact_data_in_repo") is not False:
        errors.append("private_contact_data_in_repo must be false")
    if manifest.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if set(manifest.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("manifest required_roles must exactly match required roles")

    files = manifest.get("files", {})
    expected_files = {
        "runbook": rel(RUNBOOK),
        "reviewer_selection_criteria": rel(SELECTION_CRITERIA),
        "contact_intake_template": rel(CONTACT_INTAKE),
        "send_approval_record_template": rel(APPROVAL_TEMPLATE),
    }
    for key, expected in expected_files.items():
        if files.get(key) != expected:
            errors.append(f"manifest files.{key} must be {expected}")


def validate_contact_intake(errors: list[str]) -> None:
    rows = read_csv(CONTACT_INTAKE)
    roles = {row.get("role_id") for row in rows}
    if roles != REQUIRED_ROLES:
        errors.append(f"contact intake roles mismatch: {sorted(roles)}")
    for row in rows:
        role = row.get("role_id", "")
        blank_fields = [
            "reviewer_name",
            "public_contact_channel",
            "public_contact_target",
            "private_contact_storage",
        ]
        for field in blank_fields:
            if row.get(field):
                errors.append(f"{role}: {field} must be blank in the repo template")
        expected_values = {
            "conflict_check_status": "not_started",
            "approval_to_contact": "no",
            "approval_to_send": "no",
            "contact_record_status": "not_collected",
            "external_action_taken": "no",
        }
        for field, expected in expected_values.items():
            if row.get(field) != expected:
                errors.append(f"{role}: {field} must be {expected}")


def validate_selection_criteria(errors: list[str]) -> None:
    rows = read_csv(SELECTION_CRITERIA)
    roles = {row.get("role_id") for row in rows}
    if roles != REQUIRED_ROLES:
        errors.append(f"selection criteria roles mismatch: {sorted(roles)}")
    for row in rows:
        role = row.get("role_id", "")
        for field in [
            "required_expertise",
            "minimum_independence_check",
            "disqualifying_conflicts",
            "review_scope",
            "authority_limit",
        ]:
            value = row.get(field, "")
            if not value:
                errors.append(f"{role}: {field} must be non-empty")
        authority_limit = row.get("authority_limit", "").lower()
        if "does not approve publication" not in authority_limit:
            errors.append(f"{role}: authority_limit must say it does not approve publication")


def validate_approval_template(errors: list[str]) -> None:
    template = read_json(APPROVAL_TEMPLATE)
    if template.get("contact_approval_id") != CONTACT_APPROVAL_ID:
        errors.append(f"approval template contact_approval_id must be {CONTACT_APPROVAL_ID}")
    if template.get("status") != "template_not_approval":
        errors.append("approval template status must be template_not_approval")
    if template.get("approval_decision") != "PENDING":
        errors.append("approval template approval_decision must be PENDING")
    if template.get("approved_roles") != []:
        errors.append("approval template approved_roles must be empty")
    if template.get("messages_sent") != 0:
        errors.append("approval template messages_sent must be 0")
    if template.get("external_action_taken") is not False:
        errors.append("approval template external_action_taken must be false")
    if set(template.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("approval template required_roles must exactly match required roles")

    required_before_send = " ".join(template.get("required_before_send", [])).lower()
    for required in [
        "reviewer identity",
        "contact target",
        "explicit approval",
        "template",
        "no private contact data",
    ]:
        if required not in required_before_send:
            errors.append(f"approval template required_before_send missing: {required}")


def validate_runbook(errors: list[str]) -> None:
    lower = RUNBOOK.read_text(encoding="utf-8").lower()
    for required in [
        "contact approval",
        "do not send",
        "no private contact data",
        "contact targets are blank",
        "explicit approval to send",
        "real human reviewer",
        CLAIM_CEILING,
    ]:
        if required.lower() not in lower:
            errors.append(f"runbook missing required phrase: {required}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {rel(path)}")

    if not errors:
        validate_manifest(errors)
        validate_contact_intake(errors)
        validate_selection_criteria(errors)
        validate_approval_template(errors)
        validate_runbook(errors)

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden contact approval claim: {forbidden}")
        for required in [
            "contact approval",
            "not sent",
            "no private contact data",
            "explicit approval to send",
            CLAIM_CEILING,
        ]:
            if required.lower() not in combined:
                errors.append(f"contact approval packet missing required phrase: {required}")

    if errors:
        print("NWAGU_DATASET_BOUNDARY_CONTACT_APPROVAL_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_DATASET_BOUNDARY_CONTACT_APPROVAL_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
