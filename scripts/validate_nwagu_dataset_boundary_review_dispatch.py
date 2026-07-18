from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
DISPATCH_DIR = EXP_DIR / "dataset_boundary" / "review_gate" / "intake" / "dispatch"
TEMPLATE_DIR = DISPATCH_DIR / "invitation_templates"
CONTACT_DIR = DISPATCH_DIR / "contact_approval"

MANIFEST = DISPATCH_DIR / "dispatch_manifest.json"
RUNBOOK = DISPATCH_DIR / "DISPATCH_RUNBOOK.md"
TRACKER = DISPATCH_DIR / "dispatch_tracker.csv"
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
    TRACKER,
    CONTACT_MANIFEST,
    CONTACT_RUNBOOK,
    CONTACT_SELECTION_CRITERIA,
    CONTACT_INTAKE,
    CONTACT_APPROVAL_TEMPLATE,
]

CLAIM_CEILING = "dispatch_packet_ready_not_sent"

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


def template_path(role: str) -> Path:
    return TEMPLATE_DIR / f"{role}_invitation.md"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_manifest(errors: list[str]) -> None:
    manifest = read_json(MANIFEST)
    if manifest.get("dispatch_id") != "BOUNDARY-REVIEW-DISPATCH-EXP-FRONTIER-008-001":
        errors.append("dispatch_id must be BOUNDARY-REVIEW-DISPATCH-EXP-FRONTIER-008-001")
    if manifest.get("intake_id") != "BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001":
        errors.append("intake_id must be BOUNDARY-REVIEW-INTAKE-EXP-FRONTIER-008-001")
    if manifest.get("status") != "ready_to_prepare_contacts_not_sent":
        errors.append("manifest status must be ready_to_prepare_contacts_not_sent")
    if manifest.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"manifest claim_ceiling must be {CLAIM_CEILING}")
    if manifest.get("messages_sent") != 0:
        errors.append("messages_sent must be 0")
    if manifest.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if manifest.get("approval_to_send_recorded") is not False:
        errors.append("approval_to_send_recorded must be false")
    if manifest.get("contact_approval_packet") != (
        "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/"
        "review_gate/intake/dispatch/contact_approval/contact_approval_manifest.json"
    ):
        errors.append("manifest contact_approval_packet must point to contact approval manifest")
    if set(manifest.get("required_roles", [])) != REQUIRED_ROLES:
        errors.append("manifest required_roles must exactly match required roles")
    templates = manifest.get("invitation_templates", {})
    for role in REQUIRED_ROLES:
        expected = (
            "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/"
            f"review_gate/intake/dispatch/invitation_templates/{role}_invitation.md"
        )
        if templates.get(role) != expected:
            errors.append(f"{role}: invitation_templates path must be {expected}")


def validate_tracker(errors: list[str]) -> None:
    rows = read_csv(TRACKER)
    roles = {row.get("role_id") for row in rows}
    if roles != REQUIRED_ROLES:
        errors.append(f"dispatch tracker roles mismatch: {sorted(roles)}")
    for row in rows:
        role = row.get("role_id", "")
        if row.get("dispatch_status") != "not_sent_missing_reviewer_contact":
            errors.append(f"{role}: dispatch_status must be not_sent_missing_reviewer_contact")
        for field in ["reviewer_name", "contact_channel", "contact_target", "sent_at", "sent_by"]:
            if row.get(field):
                errors.append(f"{role}: {field} must be blank until dispatch is approved and sent")
        if row.get("approval_to_send") != "no":
            errors.append(f"{role}: approval_to_send must be no")
        if row.get("external_action_taken") != "no":
            errors.append(f"{role}: external_action_taken must be no")
        if row.get("template_path") != template_path(role).relative_to(ROOT).as_posix():
            errors.append(f"{role}: template_path must point to role invitation template")


def validate_templates(errors: list[str]) -> None:
    for role in REQUIRED_ROLES:
        path = template_path(role)
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")
            continue
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for required in [
            role,
            "subject:",
            "message:",
            "review packet",
            "pass",
            "reject",
            "revise",
            "schema-valid",
            "real human review",
            "agent may not approve",
            CLAIM_CEILING,
        ]:
            if required.lower() not in lower:
                errors.append(f"{role}: invitation template missing required phrase: {required}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        validate_manifest(errors)
        validate_tracker(errors)
        validate_templates(errors)

        all_paths = REQUIRED_FILES + [template_path(role) for role in sorted(REQUIRED_ROLES)]
        combined = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in all_paths
            if path.exists()
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden dispatch claim: {forbidden}")
        for required in [
            "review dispatch",
            "not sent",
            "missing reviewer contact",
            "approval to send",
            "role-specific invitation",
            "contact approval",
            CLAIM_CEILING,
        ]:
            if required.lower() not in combined:
                errors.append(f"dispatch packet missing required phrase: {required}")

    if errors:
        print("NWAGU_DATASET_BOUNDARY_REVIEW_DISPATCH_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_DATASET_BOUNDARY_REVIEW_DISPATCH_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
