from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-014-safe-role-assignment-recorder"
MANIFEST_PATH = EXP_DIR / "manifest.json"
RECORDER_MD = EXP_DIR / "SAFE_ROLE_ASSIGNMENT_RECORDER.md"
SCHEMA_PATH = EXP_DIR / "approved_role_assignment_schema.json"
TEMPLATE_PATH = EXP_DIR / "approved_role_assignment_template.json"
REDACTION_RULES_PATH = EXP_DIR / "redaction_rules.csv"
ASSIGNMENTS_PATH = EXP_DIR / "approved_role_assignments.jsonl"

REQUIRED_FILES = [
    MANIFEST_PATH,
    RECORDER_MD,
    SCHEMA_PATH,
    TEMPLATE_PATH,
    REDACTION_RULES_PATH,
    ASSIGNMENTS_PATH,
]

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "atlas_id",
    "status",
    "decision",
    "claim_ceiling",
    "local_context",
    "external_actions_taken",
    "dependencies_installed",
    "reviewer_identities_recorded",
    "private_contact_data_recorded",
    "approved_assignments_recorded",
    "invitations_sent",
    "reviews_collected",
    "adjudication_completed",
    "public_package_approved",
    "public_release_claimed",
    "software_heritage_request_made",
    "archive_identifier_claimed",
    "allowed_record_fields",
    "blocked_promotions",
    "exact_next_action",
}

REQUIRED_LOCAL_CONTEXT = {
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/manifest.json",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/reviewer_assignment_tracker.csv",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/conflict_of_interest_checklist.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/reviewer_questions.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/contact_approval_manifest.json",
}

REQUIRED_ALLOWED_FIELDS = {
    "assignment_id",
    "review_role",
    "reviewer_ref",
    "selection_basis",
    "approval_record_ref",
    "contact_data_location",
    "private_contact_data_in_repo",
    "assignment_status",
    "scope",
}

REQUIRED_ROLES = {
    "repository_boundary_reviewer",
    "rights_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

REQUIRED_REDACTION_RULES = {
    "no_real_names",
    "no_email_addresses",
    "no_phone_numbers",
    "no_messaging_handles",
    "no_private_contact_locations",
    "no_review_content",
}

FORBIDDEN_TEXT = [
    "reviewer assigned",
    "reviewers assigned",
    "identity recorded",
    "contact recorded",
    "invitation sent",
    "review collected",
    "adjudication complete",
    "public package approved",
    "public release approved",
    "rights cleared",
    "authority approved",
    "software heritage save requested",
    "save code now requested",
    "swhid assigned",
    "archive identifier assigned",
    "paper-ready",
    "submission-ready",
    "source-observed 27/216",
]

REQUIRED_MARKDOWN_PHRASES = [
    "safe role-assignment recorder",
    "no assignments recorded",
    "no reviewer identities recorded",
    "no private contact data",
    "safe_role_assignment_recorder_not_assignment_completion",
    "pseudonymous reviewer references",
    "what this teaches oroma",
    "exact next action",
]

PRIVATE_DATA_PATTERNS = [
    re.compile(r"[\w.\-+]+@[\w.\-]+\.[a-z]{2,}", re.I),
    re.compile(r"\+?\d[\d\s().-]{7,}\d"),
    re.compile(r"whatsapp|telegram|signal|phone|email", re.I),
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def jsonl_rows(path: Path) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.name}:{line_number}: invalid jsonl: {exc}") from exc
    return rows


def contains_private_data(text: str) -> bool:
    return any(pattern.search(text) for pattern in PRIVATE_DATA_PATTERNS)


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        manifest = read_json(MANIFEST_PATH)
        missing_fields = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
        if missing_fields:
            errors.append(f"manifest missing fields: {missing_fields}")

        if manifest.get("experiment_id") != "EXP-FRONTIER-014":
            errors.append("manifest experiment_id must be EXP-FRONTIER-014")
        if manifest.get("atlas_id") != "ATLAS-0043":
            errors.append("manifest atlas_id must be ATLAS-0043")
        if manifest.get("status") != "SAFE_ROLE_ASSIGNMENT_RECORDER_READY_NO_ASSIGNMENTS_RECORDED":
            errors.append("manifest status must be recorder ready with no assignments recorded")
        if manifest.get("decision") != "prepare_safe_assignment_recording_without_identity_or_contact_data":
            errors.append("manifest decision must prepare safe recording without identity/contact data")
        if manifest.get("claim_ceiling") != "safe_role_assignment_recorder_not_assignment_completion":
            errors.append("manifest claim ceiling must block assignment-completion claims")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")

        for field in [
            "dependencies_installed",
            "reviewer_identities_recorded",
            "private_contact_data_recorded",
            "approved_assignments_recorded",
            "invitations_sent",
            "reviews_collected",
            "adjudication_completed",
            "public_package_approved",
            "public_release_claimed",
            "software_heritage_request_made",
            "archive_identifier_claimed",
        ]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")

        allowed_fields = set(manifest.get("allowed_record_fields", []))
        if allowed_fields != REQUIRED_ALLOWED_FIELDS:
            errors.append("manifest allowed_record_fields must exactly match safe assignment schema fields")

        local_context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_LOCAL_CONTEXT - local_context)
        if missing_context:
            errors.append(f"manifest missing local_context paths: {missing_context}")
        for rel_path in local_context:
            if not (ROOT / rel_path).exists():
                errors.append(f"manifest local_context does not exist: {rel_path}")

        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "reviewer assignment completion claim",
            "review completion claim",
            "private contact data in repo",
            "public repository package",
            "Software Heritage archive action",
            "rights or authority clearance claim",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        schema = read_json(SCHEMA_PATH)
        if schema.get("schema_id") != "SAFE-ROLE-ASSIGNMENT-SCHEMA-001":
            errors.append("schema id is invalid")
        if schema.get("claim_ceiling") != "safe_role_assignment_recorder_not_assignment_completion":
            errors.append("schema claim ceiling must block assignment-completion claims")
        if set(schema.get("required", [])) != REQUIRED_ALLOWED_FIELDS:
            errors.append("schema required fields must exactly match allowed assignment fields")
        role_enum = set(schema.get("properties", {}).get("review_role", {}).get("enum", []))
        if role_enum != REQUIRED_ROLES:
            errors.append("schema review_role enum must match required roles")
        if schema.get("additionalProperties") is not False:
            errors.append("schema additionalProperties must be false")

        template = read_json(TEMPLATE_PATH)
        if set(template.keys()) != REQUIRED_ALLOWED_FIELDS:
            errors.append("assignment template fields must exactly match allowed fields")
        if template.get("private_contact_data_in_repo") is not False:
            errors.append("assignment template private_contact_data_in_repo must be false")
        if template.get("assignment_status") != "template_only_not_recorded":
            errors.append("assignment template status must be template_only_not_recorded")
        if contains_private_data(json.dumps(template)):
            errors.append("assignment template must not contain private contact data patterns")

        redaction_rows = read_csv(REDACTION_RULES_PATH)
        rule_ids = {row.get("rule_id") for row in redaction_rows}
        missing_rules = sorted(REQUIRED_REDACTION_RULES - rule_ids)
        if missing_rules:
            errors.append(f"redaction rules missing ids: {missing_rules}")
        for row in redaction_rows:
            rule_id = row.get("rule_id", "")
            if row.get("current_status") != "active_required":
                errors.append(f"{rule_id}: current_status must be active_required")
            if row.get("allowed_in_repo") != "no":
                errors.append(f"{rule_id}: allowed_in_repo must be no")
            if not row.get("replacement"):
                errors.append(f"{rule_id}: replacement is required")

        try:
            assignment_rows = jsonl_rows(ASSIGNMENTS_PATH)
        except ValueError as exc:
            errors.append(str(exc))
            assignment_rows = []
        if assignment_rows:
            errors.append("approved_role_assignments.jsonl must remain empty until human-approved assignments exist")
        if contains_private_data(ASSIGNMENTS_PATH.read_text(encoding="utf-8")):
            errors.append("approved_role_assignments.jsonl must not contain private contact data")

        markdown = RECORDER_MD.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in markdown:
                errors.append(f"recorder markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden safe assignment recorder text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in safe assignment recorder packet")

    if errors:
        print("SAFE_ROLE_ASSIGNMENT_RECORDER_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("SAFE_ROLE_ASSIGNMENT_RECORDER_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
