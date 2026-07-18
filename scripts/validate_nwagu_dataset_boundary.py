from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
BOUNDARY_DIR = EXP_DIR / "dataset_boundary"
BOUNDARY_JSON = BOUNDARY_DIR / "boundary_review.json"
CHECKLIST_MD = BOUNDARY_DIR / "DATASET_BOUNDARY_CHECKLIST.md"
CANDIDATE_FILES = BOUNDARY_DIR / "candidate_files.csv"
EXCLUDED_FILES = BOUNDARY_DIR / "excluded_files.csv"
REVIEWER_ROLES = BOUNDARY_DIR / "reviewer_roles.csv"
VALIDATOR_CONTROLS = BOUNDARY_DIR / "validator_controls.json"
REVIEW_GATE_DIR = BOUNDARY_DIR / "review_gate"
REVIEW_GATE_JSON = REVIEW_GATE_DIR / "review_gate.json"
REVIEW_GATE_MD = REVIEW_GATE_DIR / "REVIEW_GATE.md"
REVIEW_REQUESTS = REVIEW_GATE_DIR / "review_requests.csv"
REVIEW_TRACE_TEMPLATE = REVIEW_GATE_DIR / "review_trace_template.jsonl"
DECISION_RECORD_TEMPLATE = REVIEW_GATE_DIR / "decision_record_template.json"

REQUIRED_FILES = [
    BOUNDARY_JSON,
    CHECKLIST_MD,
    CANDIDATE_FILES,
    EXCLUDED_FILES,
    REVIEWER_ROLES,
    VALIDATOR_CONTROLS,
    REVIEW_GATE_JSON,
    REVIEW_GATE_MD,
    REVIEW_REQUESTS,
    REVIEW_TRACE_TEMPLATE,
    DECISION_RECORD_TEMPLATE,
]

CLAIM_CEILING = "dataset_boundary_checklist_not_dataset_release"

REQUIRED_CANDIDATE_PATHS = {
    "research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl",
    "research/frontier/nwagu_aneke/interfaces/count_layer_data_to_view_map.jsonl",
    "research/frontier/nwagu_aneke/interfaces/count_layer_view_outline.md",
    "research/frontier/nwagu_aneke/interfaces/usability/README.md",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/manifest.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/execution_decision.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/review/review_manifest.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/review/EXECUTION_GATE_REVIEW.md",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/manifest.json",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/KEEP_REJECT_LOOP_DESIGN.md",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/task_cards.csv",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/decision_schema.json",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/negative_control.md",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/manifest.json",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/NO_CONVERSION_DECISION.md",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/conversion_blockers.csv",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/future_readiness_checklist.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/manifest.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/NO_ARCHIVE_IDENTIFIER_DECISION.md",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/archive_blockers.csv",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/future_readiness_checklist.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/manifest.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/REPOSITORY_BOUNDARY_REVIEW.md",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/repository_asset_inventory.csv",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/excluded_repository_paths.csv",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/future_public_package_checklist.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/reviewer_questions.csv",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/manifest.json",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/REVIEWER_ASSIGNMENT_INTAKE.md",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/reviewer_assignment_tracker.csv",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/candidate_adjudication_matrix.csv",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/conflict_of_interest_checklist.json",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/decision_record_template.json",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/manifest.json",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/SAFE_ROLE_ASSIGNMENT_RECORDER.md",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/approved_role_assignment_schema.json",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/approved_role_assignment_template.json",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/redaction_rules.csv",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/approved_role_assignments.jsonl",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/manifest.json",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/HUNDRED_PAPER_RECOVERY_INTAKE.md",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/research_seeds.csv",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/research_seed_schema.json",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/claim_gate_matrix.csv",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/sprint_selection.json",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/manifest.json",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/SELECTED_SEED_ARTIFACT_SPRINT.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifact_index.csv",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/approval_record.json",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-001-source-acquisition-decision-note.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-009-authority-role-map.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-017-reader-response-protocol.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-025-logograph-uncertainty-ledger.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-033-unicode-gap-map.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-041-modifier-operation-sketch.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-049-lpe-label-quality-audit.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-057-ro-crate-boundary-audit.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-065-layered-explainer-storyboard.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-073-layer-lineage-card.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-081-cross-domain-transfer-grid.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-089-portfolio-acceleration-dashboard-spec.md",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/manifest.json",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/LPE_LABEL_QUALITY_GATE.md",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/label_quality_gate_schema.json",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/quality_gate_matrix.csv",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/pilot_sample.csv",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/pilot_results.json",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/failure_cases.md",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/paper_pathway.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/decision.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/PRESERVATION_DECISION.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/decision_matrix.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/deferred_actions.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/boundary_review.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/DATASET_BOUNDARY_CHECKLIST.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/candidate_files.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/excluded_files.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/reviewer_roles.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/validator_controls.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/review_gate.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/REVIEW_GATE.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/review_requests.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/review_trace_template.jsonl",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/decision_record_template.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/review_intake_manifest.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/REVIEW_INTAKE_RUNBOOK.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/review_submission_schema.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/collected_reviews/README.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/rights_authority_reviewer.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/community_authority_reviewer.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/source_dossier_reviewer.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/preservation_infrastructure_reviewer.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/role_forms/data_protection_reviewer.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/dispatch_manifest.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/DISPATCH_RUNBOOK.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/dispatch_tracker.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/contact_approval_manifest.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/CONTACT_APPROVAL_RUNBOOK.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/reviewer_selection_criteria.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/contact_intake_template.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/send_approval_record_template.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/invitation_templates/rights_authority_reviewer_invitation.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/invitation_templates/community_authority_reviewer_invitation.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/invitation_templates/source_dossier_reviewer_invitation.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/invitation_templates/preservation_infrastructure_reviewer_invitation.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/invitation_templates/data_protection_reviewer_invitation.md",
    "scripts/validate_claim_layer_fixtures.py",
    "scripts/validate_count_layer_view_map.py",
    "scripts/validate_inspect_lpe_port.py",
    "scripts/validate_inspect_execution_gate.py",
    "scripts/validate_inspect_execution_gate_review.py",
    "scripts/validate_mlagentbench_keep_reject_design.py",
    "scripts/validate_datalad_no_conversion_decision.py",
    "scripts/validate_software_heritage_no_identifier_decision.py",
    "scripts/validate_repository_boundary_review.py",
    "scripts/validate_repository_reviewer_assignment_intake.py",
    "scripts/validate_safe_role_assignment_recorder.py",
    "scripts/validate_hundred_paper_recovery_intake.py",
    "scripts/validate_selected_seed_artifact_sprint.py",
    "scripts/validate_lpe_label_quality_gate.py",
    "scripts/validate_nwagu_frontier_ro_crate.py",
    "scripts/validate_nwagu_preservation_decision.py",
    "scripts/validate_nwagu_dataset_boundary.py",
    "scripts/validate_nwagu_dataset_boundary_review_gate.py",
    "scripts/validate_nwagu_dataset_boundary_review_intake.py",
    "scripts/validate_nwagu_dataset_boundary_review_dispatch.py",
    "scripts/validate_nwagu_dataset_boundary_contact_approval.py",
}

REQUIRED_EXCLUSION_PATTERNS = {
    "research/frontier/nwagu_aneke/primary_sources/",
    "primary_sources/",
    "*.pdf",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.tif",
    "*.tiff",
    "glyph_reproductions",
    "restricted_manuscript_material",
    "private_data",
    "human_reader_response_csv",
}

REQUIRED_REVIEWER_ROLES = {
    "rights_authority_reviewer",
    "community_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

FORBIDDEN_CANDIDATE_SNIPPETS = [
    "primary_sources/",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    "glyph_reproductions",
    "restricted",
    "private_data",
    "responses/",
]

FORBIDDEN_TEXT = [
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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_boundary_json(errors: list[str]) -> None:
    boundary = read_json(BOUNDARY_JSON)
    if boundary.get("boundary_id") != "BOUNDARY-EXP-FRONTIER-008-001":
        errors.append("boundary_id must be BOUNDARY-EXP-FRONTIER-008-001")
    if boundary.get("experiment_id") != "EXP-FRONTIER-008":
        errors.append("experiment_id must be EXP-FRONTIER-008")
    if boundary.get("status") != "checklist_ready_for_review_not_approved":
        errors.append("status must be checklist_ready_for_review_not_approved")
    if boundary.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"claim_ceiling must be {CLAIM_CEILING}")
    if boundary.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be an empty list")
    if boundary.get("current_package_route") != "repo_local_internal_metadata_package":
        errors.append("current_package_route must remain repo_local_internal_metadata_package")

    required_before_promotion = set(boundary.get("required_before_promotion", []))
    for required in [
        "rights review",
        "authority review",
        "dataset boundary approval",
        "public release approval",
        "restricted-material exclusion audit",
    ]:
        if required not in required_before_promotion:
            errors.append(f"boundary missing promotion requirement: {required}")

    forbidden_actions = set(boundary.get("forbidden_current_actions", []))
    for action in [
        "create DataLad dataset",
        "request Software Heritage save",
        "copy raw sources",
        "include source images",
        "include restricted manuscript material",
        "include private data",
        "claim public release readiness",
    ]:
        if action not in forbidden_actions:
            errors.append(f"boundary missing forbidden action: {action}")


def validate_candidates(errors: list[str]) -> None:
    rows = read_csv(CANDIDATE_FILES)
    paths = {row.get("path") for row in rows}
    missing = sorted(REQUIRED_CANDIDATE_PATHS - paths)
    if missing:
        errors.append(f"candidate file list missing paths: {missing}")

    for row in rows:
        path = row.get("path", "")
        if not path:
            errors.append("candidate row missing path")
            continue
        for forbidden in FORBIDDEN_CANDIDATE_SNIPPETS:
            if forbidden.lower() in path.lower():
                errors.append(f"candidate path must not include restricted material: {path}")
        if row.get("candidate_status") != "candidate_internal_metadata_only":
            errors.append(f"{path}: candidate_status must be candidate_internal_metadata_only")
        if row.get("external_release_now") != "no":
            errors.append(f"{path}: external_release_now must be no")
        if row.get("approval_required") != "boundary_review":
            errors.append(f"{path}: approval_required must be boundary_review")


def validate_exclusions(errors: list[str]) -> None:
    rows = read_csv(EXCLUDED_FILES)
    patterns = {row.get("pattern") for row in rows}
    missing = sorted(REQUIRED_EXCLUSION_PATTERNS - patterns)
    if missing:
        errors.append(f"excluded file list missing patterns: {missing}")
    for row in rows:
        pattern = row.get("pattern", "")
        if row.get("current_status") != "excluded_from_candidate_boundary":
            errors.append(f"{pattern}: current_status must be excluded_from_candidate_boundary")
        if row.get("allowed_without_review") != "no":
            errors.append(f"{pattern}: allowed_without_review must be no")
        if not row.get("validator_control"):
            errors.append(f"{pattern}: validator_control is required")


def validate_reviewers(errors: list[str]) -> None:
    rows = read_csv(REVIEWER_ROLES)
    roles = {row.get("role_id") for row in rows}
    missing = sorted(REQUIRED_REVIEWER_ROLES - roles)
    if missing:
        errors.append(f"reviewer role list missing roles: {missing}")
    for row in rows:
        role_id = row.get("role_id", "")
        if row.get("required_before") != "dataset_boundary_approval":
            errors.append(f"{role_id}: required_before must be dataset_boundary_approval")
        if row.get("current_status") != "not_reviewed":
            errors.append(f"{role_id}: current_status must be not_reviewed")
        if row.get("may_approve_current_public_release") != "no":
            errors.append(f"{role_id}: may_approve_current_public_release must be no")


def validate_controls(errors: list[str]) -> None:
    controls = read_json(VALIDATOR_CONTROLS)
    if controls.get("control_id") != "BOUNDARY-CONTROL-EXP-FRONTIER-008-001":
        errors.append("control_id must be BOUNDARY-CONTROL-EXP-FRONTIER-008-001")
    if controls.get("status") != "active_boundary_control_not_release":
        errors.append("control status must be active_boundary_control_not_release")
    if controls.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"control claim_ceiling must be {CLAIM_CEILING}")
    forbidden_fragments = set(controls.get("forbidden_path_fragments", []))
    for fragment in FORBIDDEN_CANDIDATE_SNIPPETS:
        if fragment not in forbidden_fragments:
            errors.append(f"validator controls missing forbidden path fragment: {fragment}")
    required_validators = set(controls.get("required_validators", []))
    for validator in [
        "scripts/validate_nwagu_dataset_boundary.py",
        "scripts/validate_nwagu_frontier_ro_crate.py",
        "scripts/validate_nwagu_preservation_decision.py",
        "scripts/validate_nwagu_dataset_boundary_contact_approval.py",
    ]:
        if validator not in required_validators:
            errors.append(f"validator controls missing required validator: {validator}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        validate_boundary_json(errors)
        validate_candidates(errors)
        validate_exclusions(errors)
        validate_reviewers(errors)
        validate_controls(errors)

        combined = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in REQUIRED_FILES
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden boundary claim: {forbidden}")
        for required in [
            "dataset boundary",
            "candidate files",
            "excluded files",
            "reviewer roles",
            "validator behavior",
            "no external submission",
            CLAIM_CEILING,
        ]:
            if required.lower() not in combined:
                errors.append(f"boundary packet missing required phrase: {required}")

    if errors:
        print("NWAGU_DATASET_BOUNDARY_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_DATASET_BOUNDARY_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
