from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
CRATE_PATH = EXP_DIR / "ro-crate-metadata.json"
README_PATH = EXP_DIR / "README.md"
POLICY_PATH = EXP_DIR / "RELEASE_POLICY.md"
MANIFEST_PATH = EXP_DIR / "crate_manifest.csv"

REQUIRED_FILES = [
    CRATE_PATH,
    README_PATH,
    POLICY_PATH,
    MANIFEST_PATH,
]

REQUIRED_PARTS = {
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

FORBIDDEN_PART_SNIPPETS = [
    "primary_sources/",
    "azuonye_1992.pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
]

FORBIDDEN_TEXT = [
    "publication-ready",
    "paper-ready",
    "submission-ready",
    "public release approved",
    "source-observed 27/216",
    "rights cleared",
    "authority approved",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        crate = json.loads(CRATE_PATH.read_text(encoding="utf-8"))
        graph = crate.get("@graph")
        if crate.get("@context") != "https://w3id.org/ro/crate/1.3/context":
            errors.append("crate must use RO-Crate 1.3 JSON-LD context")
        if not isinstance(graph, list):
            errors.append("crate @graph must be a list")
            graph = []

        by_id = {node.get("@id"): node for node in graph if isinstance(node, dict)}
        metadata = by_id.get("ro-crate-metadata.json")
        root = by_id.get("./")
        if not metadata:
            errors.append("crate missing metadata descriptor node")
        else:
            conforms = metadata.get("conformsTo", {})
            if conforms.get("@id") != "https://w3id.org/ro/crate/1.3":
                errors.append("metadata descriptor must conform to RO-Crate 1.3")
        if not root:
            errors.append("crate missing root dataset node")
        else:
            if root.get("@type") != "Dataset":
                errors.append("root node must be Dataset")
            if root.get("claimCeiling") != "packaging_not_clearance":
                errors.append("root claimCeiling must be packaging_not_clearance")
            if root.get("status") != "DETACHED_METADATA_PACKAGE_INTERNAL_NOT_RELEASED":
                errors.append("root status must remain internal and not released")
            blockers = set(root.get("blockingGates", []))
            for blocker in [
                "rights review",
                "authority review",
                "source-image exclusion",
                "no publication readiness claim",
            ]:
                if blocker not in blockers:
                    errors.append(f"root missing blocking gate: {blocker}")

            parts = {
                item.get("@id")
                for item in root.get("hasPart", [])
                if isinstance(item, dict) and item.get("@id")
            }
            missing_parts = sorted(REQUIRED_PARTS - parts)
            if missing_parts:
                errors.append(f"crate missing required parts: {missing_parts}")
            for part in parts:
                for forbidden in FORBIDDEN_PART_SNIPPETS:
                    if forbidden.lower() in part.lower():
                        errors.append(f"forbidden sensitive/binary part: {part}")

        for part in REQUIRED_PARTS:
            path = ROOT / part
            if not path.exists():
                errors.append(f"required part does not exist: {part}")
                continue
            node = by_id.get(part)
            if not node:
                errors.append(f"missing file node for {part}")
                continue
            if node.get("@type") != "File":
                errors.append(f"{part}: node must be File")
            if node.get("sha256") != sha256(path):
                errors.append(f"{part}: sha256 mismatch")
            if node.get("contentSize") != path.stat().st_size:
                errors.append(f"{part}: contentSize mismatch")
            if node.get("encodingFormat") not in {
                "text/markdown",
                "application/json",
                "application/jsonl",
                "application/jsonlines",
                "text/csv",
                "text/x-python",
            }:
                errors.append(f"{part}: missing or invalid encodingFormat")

        combined_text = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in [README_PATH, POLICY_PATH, CRATE_PATH]
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined_text:
                errors.append(f"forbidden crate text: {forbidden}")

    if errors:
        print("NWAGU_FRONTIER_RO_CRATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_FRONTIER_RO_CRATE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
