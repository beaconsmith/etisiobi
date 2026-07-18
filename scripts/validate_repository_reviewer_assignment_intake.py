from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-013-repository-reviewer-assignment-intake"
MANIFEST_PATH = EXP_DIR / "manifest.json"
INTAKE_MD = EXP_DIR / "REVIEWER_ASSIGNMENT_INTAKE.md"
TRACKER_PATH = EXP_DIR / "reviewer_assignment_tracker.csv"
MATRIX_PATH = EXP_DIR / "candidate_adjudication_matrix.csv"
CONFLICTS_PATH = EXP_DIR / "conflict_of_interest_checklist.json"
DECISION_TEMPLATE_PATH = EXP_DIR / "decision_record_template.json"

REQUIRED_FILES = [
    MANIFEST_PATH,
    INTAKE_MD,
    TRACKER_PATH,
    MATRIX_PATH,
    CONFLICTS_PATH,
    DECISION_TEMPLATE_PATH,
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
    "invitations_sent",
    "reviews_collected",
    "adjudication_completed",
    "public_package_approved",
    "public_release_claimed",
    "software_heritage_request_made",
    "archive_identifier_claimed",
    "required_roles",
    "blocked_promotions",
    "exact_next_action",
}

REQUIRED_LOCAL_CONTEXT = {
    "experiments/EXP-FRONTIER-012-repository-boundary-review/manifest.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/reviewer_questions.csv",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/repository_asset_inventory.csv",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/excluded_repository_paths.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/contact_approval_manifest.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/manifest.json",
}

REQUIRED_ROLES = {
    "repository_boundary_reviewer",
    "rights_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

REQUIRED_MATRIX_AREAS = {
    "candidate_inventory",
    "excluded_paths",
    "license_citation",
    "rights_authority",
    "private_contact_data",
}

REQUIRED_CONFLICT_ITEMS = {
    "NO_SELF_APPROVAL",
    "NO_PRIVATE_CONTACTS_IN_REPO",
    "NO_UNAPPROVED_AUTHORITY_SUBSTITUTION",
    "NO_RELEASE_OR_ARCHIVE_ACTION",
    "NO_SOURCE_MATERIAL_EXPOSURE",
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
    "reviewer-assignment intake",
    "no reviewer identities recorded",
    "no invitations sent",
    "no reviews collected",
    "reviewer_assignment_intake_not_review_completion",
    "candidate adjudication matrix",
    "what this teaches oroma",
    "exact next action",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


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

        if manifest.get("experiment_id") != "EXP-FRONTIER-013":
            errors.append("manifest experiment_id must be EXP-FRONTIER-013")
        if manifest.get("atlas_id") != "ATLAS-0043":
            errors.append("manifest atlas_id must be ATLAS-0043")
        if manifest.get("status") != "REPOSITORY_REVIEWER_ASSIGNMENT_INTAKE_READY_NO_ASSIGNMENTS":
            errors.append("manifest status must be intake ready with no assignments")
        if manifest.get("decision") != "prepare_assignment_and_adjudication_intake_without_contact_or_approval":
            errors.append("manifest decision must prepare intake without contact or approval")
        if manifest.get("claim_ceiling") != "reviewer_assignment_intake_not_review_completion":
            errors.append("manifest claim ceiling must block review-completion claims")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")

        for field in [
            "dependencies_installed",
            "reviewer_identities_recorded",
            "private_contact_data_recorded",
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

        if set(manifest.get("required_roles", [])) != REQUIRED_ROLES:
            errors.append("manifest required_roles must exactly match repository-boundary roles")

        local_context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_LOCAL_CONTEXT - local_context)
        if missing_context:
            errors.append(f"manifest missing local_context paths: {missing_context}")
        for rel_path in local_context:
            if not (ROOT / rel_path).exists():
                errors.append(f"manifest local_context does not exist: {rel_path}")

        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "reviewer assignment claim",
            "review completion claim",
            "adjudication completion claim",
            "public repository package",
            "Software Heritage archive action",
            "rights or authority clearance claim",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        tracker_rows = read_csv(TRACKER_PATH)
        tracker_roles = {row.get("review_role") for row in tracker_rows}
        missing_roles = sorted(REQUIRED_ROLES - tracker_roles)
        if missing_roles:
            errors.append(f"assignment tracker missing roles: {missing_roles}")
        for row in tracker_rows:
            role = row.get("review_role", "")
            if row.get("assignment_status") != "unassigned_pending_human_selection":
                errors.append(f"{role}: assignment_status must be unassigned_pending_human_selection")
            if row.get("identity_recorded") != "no":
                errors.append(f"{role}: identity_recorded must be no")
            if row.get("private_contact_data_recorded") != "no":
                errors.append(f"{role}: private_contact_data_recorded must be no")
            if row.get("invitation_sent") != "no":
                errors.append(f"{role}: invitation_sent must be no")
            if row.get("review_collected") != "no":
                errors.append(f"{role}: review_collected must be no")
            if row.get("required_before") != "repository_boundary_decision":
                errors.append(f"{role}: required_before must be repository_boundary_decision")

        matrix_rows = read_csv(MATRIX_PATH)
        matrix_areas = {row.get("review_area") for row in matrix_rows}
        missing_areas = sorted(REQUIRED_MATRIX_AREAS - matrix_areas)
        if missing_areas:
            errors.append(f"candidate adjudication matrix missing areas: {missing_areas}")
        for row in matrix_rows:
            area = row.get("review_area", "")
            if row.get("current_status") != "pending_reviewer_adjudication":
                errors.append(f"{area}: current_status must be pending_reviewer_adjudication")
            if row.get("approval_recorded") != "no":
                errors.append(f"{area}: approval_recorded must be no")
            if not row.get("decision_question"):
                errors.append(f"{area}: decision_question is required")

        conflicts = read_json(CONFLICTS_PATH)
        if conflicts.get("checklist_id") != "REPO-REVIEWER-CONFLICT-CHECKLIST-001":
            errors.append("conflict checklist id is invalid")
        if conflicts.get("status") != "not_satisfied_no_reviewers_selected":
            errors.append("conflict checklist status must be no reviewers selected")
        if conflicts.get("claim_ceiling") != "reviewer_assignment_intake_not_review_completion":
            errors.append("conflict checklist claim ceiling must block review completion")
        conflict_items = {
            item.get("item_id"): item
            for item in conflicts.get("items", [])
            if isinstance(item, dict)
        }
        missing_conflicts = sorted(REQUIRED_CONFLICT_ITEMS - conflict_items.keys())
        if missing_conflicts:
            errors.append(f"conflict checklist missing items: {missing_conflicts}")
        for item_id in REQUIRED_CONFLICT_ITEMS & conflict_items.keys():
            if conflict_items[item_id].get("current_status") != "not_satisfied":
                errors.append(f"{item_id}: current_status must be not_satisfied")

        decision_template = read_json(DECISION_TEMPLATE_PATH)
        if decision_template.get("template_id") != "REPO-BOUNDARY-DECISION-TEMPLATE-001":
            errors.append("decision record template id is invalid")
        if decision_template.get("status") != "template_only_not_decision_record":
            errors.append("decision template status must be template only")
        if decision_template.get("claim_ceiling") != "reviewer_assignment_intake_not_review_completion":
            errors.append("decision template claim ceiling must block review completion")
        for field in [
            "reviewer_assignments",
            "candidate_path_decisions",
            "excluded_path_decisions",
            "blocking_issues",
            "required_follow_up",
        ]:
            if field not in decision_template:
                errors.append(f"decision template missing field: {field}")

        markdown = INTAKE_MD.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in markdown:
                errors.append(f"intake markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden reviewer-assignment text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in reviewer-assignment packet")

    if errors:
        print("REPOSITORY_REVIEWER_ASSIGNMENT_INTAKE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("REPOSITORY_REVIEWER_ASSIGNMENT_INTAKE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
