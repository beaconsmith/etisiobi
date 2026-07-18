from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUS_JSON = ROOT / "research" / "frontier" / "nwagu_aneke" / "FRONTIER_LAB_STATUS.json"
STATUS_MD = ROOT / "research" / "frontier" / "nwagu_aneke" / "FRONTIER_LAB_STATUS.md"

REQUIRED_FILES = [STATUS_JSON, STATUS_MD]

STATUS_ID = "NWAGU-FRONTIER-LAB-STATUS-001"
PROGRAM = "nwagu_aneke_frontier"
CLAIM_CEILING = "status_surface_not_research_result"

REQUIRED_LANE_IDS = {str(index) for index in range(1, 13)}
REQUIRED_LAYER_LABELS = {
    "source_observed",
    "derived",
    "speculative",
    "application",
    "infrastructure",
    "authority_rights",
}
REQUIRED_ANCHOR_PATHS = {
    "wiki/index.md",
    "research/frontier/nwagu_aneke/FRONTIER_PROGRAM_MAP.md",
    "research/frontier/nwagu_aneke/FRONTIER_OPPORTUNITY_REGISTER.md",
    "research/frontier/nwagu_aneke/FRONTIER_PORTFOLIO_SCORECARD.md",
    "research/frontier/nwagu_aneke/FRONTIER_DEPENDENCY_GRAPH.md",
    "research/frontier/nwagu_aneke/EXPERIMENT_BACKLOG.md",
    "research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl",
    "research/frontier/nwagu_aneke/interfaces/count_layer_view_outline.md",
    "research/frontier/nwagu_transfer_atlas/prior_art_verification/verification_manifest.json",
    "research/frontier/nwagu_transfer_atlas/prior_art_verification/SELECTED_INFRASTRUCTURE_PRIOR_ART.md",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/manifest.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/execution_decision.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/review/review_manifest.json",
    "experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/execution_gate/review/EXECUTION_GATE_REVIEW.md",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/manifest.json",
    "experiments/EXP-FRONTIER-009-mlagentbench-keep-reject-loop/KEEP_REJECT_LOOP_DESIGN.md",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/manifest.json",
    "experiments/EXP-FRONTIER-010-datalad-no-conversion-decision/NO_CONVERSION_DECISION.md",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/manifest.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/NO_ARCHIVE_IDENTIFIER_DECISION.md",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/manifest.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/REPOSITORY_BOUNDARY_REVIEW.md",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/manifest.json",
    "experiments/EXP-FRONTIER-013-repository-reviewer-assignment-intake/REVIEWER_ASSIGNMENT_INTAKE.md",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/manifest.json",
    "experiments/EXP-FRONTIER-014-safe-role-assignment-recorder/SAFE_ROLE_ASSIGNMENT_RECORDER.md",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/manifest.json",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/HUNDRED_PAPER_RECOVERY_INTAKE.md",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/manifest.json",
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/SELECTED_SEED_ARTIFACT_SPRINT.md",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/manifest.json",
    "experiments/EXP-FRONTIER-017-lpe-label-quality-gate/LPE_LABEL_QUALITY_GATE.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/README.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/review_gate/intake/dispatch/contact_approval/contact_approval_manifest.json",
}
REQUIRED_VALIDATORS = {
    "scripts/validate_nwagu_frontier_lab_status.py",
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
    "scripts/validate_nwagu_dataset_boundary_contact_approval.py",
    "scripts/validate_nwagu_prior_art_verification_packet.py",
    "scripts/validate_lab_standard.py",
    "scripts/validate_review_team_gate.py",
}

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
    "frontier proof",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require_non_empty(value: object, label: str, errors: list[str]) -> None:
    if value in (None, "", [], {}):
        errors.append(f"{label} must be non-empty")


def validate_json(errors: list[str]) -> None:
    status = read_json(STATUS_JSON)
    if status.get("status_id") != STATUS_ID:
        errors.append(f"status_id must be {STATUS_ID}")
    if status.get("program") != PROGRAM:
        errors.append(f"program must be {PROGRAM}")
    if status.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"claim_ceiling must be {CLAIM_CEILING}")
    if status.get("promotion_state") != "not_ready":
        errors.append("promotion_state must remain not_ready")
    if status.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if status.get("source_observed_invariant") != "26 rows x 8 vowel/modifier columns = 208 records":
        errors.append("source_observed_invariant must preserve 26x8=208")
    if status.get("derived_layer_rule") != "27/216 remains a derived f/v split layer unless later source evidence promotes it":
        errors.append("derived_layer_rule must keep 27/216 derived")

    layer_labels = set(status.get("layer_labels", []))
    missing_layers = sorted(REQUIRED_LAYER_LABELS - layer_labels)
    if missing_layers:
        errors.append(f"missing layer labels: {missing_layers}")

    lanes = status.get("lanes", [])
    if not isinstance(lanes, list):
        errors.append("lanes must be a list")
        lanes = []
    lane_ids = {str(lane.get("lane_id")) for lane in lanes if isinstance(lane, dict)}
    missing_lanes = sorted(REQUIRED_LANE_IDS - lane_ids, key=int)
    if missing_lanes:
        errors.append(f"missing lane ids: {missing_lanes}")
    for lane in lanes:
        if not isinstance(lane, dict):
            errors.append("each lane must be an object")
            continue
        lane_id = lane.get("lane_id")
        for field in ["name", "layer_focus", "current_state", "main_blocker", "next_action", "claim_ceiling"]:
            require_non_empty(lane.get(field), f"lane {lane_id} {field}", errors)
        if lane.get("claim_ceiling") in {"ready", "released", "approved"}:
            errors.append(f"lane {lane_id} claim_ceiling is overstrong")
        anchors = lane.get("anchor_files", [])
        if not anchors:
            errors.append(f"lane {lane_id} anchor_files must be non-empty")
        for anchor in anchors:
            path = ROOT / anchor
            if not path.exists():
                errors.append(f"lane {lane_id} anchor file does not exist: {anchor}")

    anchors = status.get("anchor_files", [])
    if not isinstance(anchors, list):
        errors.append("anchor_files must be a list")
        anchors = []
    anchor_paths = {item.get("path") for item in anchors if isinstance(item, dict)}
    missing_anchors = sorted(REQUIRED_ANCHOR_PATHS - anchor_paths)
    if missing_anchors:
        errors.append(f"missing required anchor paths: {missing_anchors}")
    for item in anchors:
        if not isinstance(item, dict):
            errors.append("anchor file entries must be objects")
            continue
        path_value = item.get("path")
        if not path_value:
            errors.append("anchor file entry missing path")
            continue
        path = ROOT / path_value
        if not path.exists():
            errors.append(f"anchor path does not exist: {path_value}")
        for field in ["role", "evidence_layer", "claim_ceiling"]:
            require_non_empty(item.get(field), f"anchor {path_value} {field}", errors)

    validators = set(status.get("validators", []))
    missing_validators = sorted(REQUIRED_VALIDATORS - validators)
    if missing_validators:
        errors.append(f"missing validators: {missing_validators}")
    for validator in validators:
        path = ROOT / validator
        if not path.exists():
            errors.append(f"validator path does not exist: {validator}")

    next_actions = status.get("exact_next_actions", [])
    if not isinstance(next_actions, list) or len(next_actions) < 5:
        errors.append("exact_next_actions must contain at least five actions")
    else:
        action_text = " ".join(str(action.get("action", "")) for action in next_actions if isinstance(action, dict)).lower()
        for required in [
            "reviewer identities",
            "azuonye",
            "reader response",
            "inspect",
            "prior-art",
            "bounded experiment",
        ]:
            if required not in action_text:
                errors.append(f"exact_next_actions missing theme: {required}")


def validate_markdown(errors: list[str]) -> None:
    text = STATUS_MD.read_text(encoding="utf-8")
    lower = text.lower()
    for required in [
        "# nwagu aneke frontier lab status",
        STATUS_ID.lower(),
        CLAIM_CEILING,
        "26 rows x 8 vowel/modifier columns = 208 records",
        "27/216 remains a derived f/v split layer",
        "promotion state: not_ready",
        "exact next actions",
        "blocked promotions",
    ]:
        if required.lower() not in lower:
            errors.append(f"status markdown missing required phrase: {required}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {rel(path)}")

    if not errors:
        validate_json(errors)
        validate_markdown(errors)

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden status claim: {forbidden}")

    if errors:
        print("NWAGU_FRONTIER_LAB_STATUS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_FRONTIER_LAB_STATUS_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
