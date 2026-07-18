from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-016-selected-seed-artifact-sprint"
ARTIFACT_DIR = EXP_DIR / "artifacts"
MANIFEST_PATH = EXP_DIR / "manifest.json"
SPRINT_MD = EXP_DIR / "SELECTED_SEED_ARTIFACT_SPRINT.md"
INDEX_PATH = EXP_DIR / "artifact_index.csv"
APPROVAL_PATH = EXP_DIR / "approval_record.json"
SOURCE_SELECTION = ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "sprint_selection.json"
SOURCE_SEEDS = ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake" / "research_seeds.csv"

EXPECTED_SELECTED_IDS = [
    "NWR-001",
    "NWR-009",
    "NWR-017",
    "NWR-025",
    "NWR-033",
    "NWR-041",
    "NWR-049",
    "NWR-057",
    "NWR-065",
    "NWR-073",
    "NWR-081",
    "NWR-089",
]

EXPECTED_ARTIFACTS = {
    "NWR-001": "artifacts/NWR-001-source-acquisition-decision-note.md",
    "NWR-009": "artifacts/NWR-009-authority-role-map.md",
    "NWR-017": "artifacts/NWR-017-reader-response-protocol.md",
    "NWR-025": "artifacts/NWR-025-logograph-uncertainty-ledger.md",
    "NWR-033": "artifacts/NWR-033-unicode-gap-map.md",
    "NWR-041": "artifacts/NWR-041-modifier-operation-sketch.md",
    "NWR-049": "artifacts/NWR-049-lpe-label-quality-audit.md",
    "NWR-057": "artifacts/NWR-057-ro-crate-boundary-audit.md",
    "NWR-065": "artifacts/NWR-065-layered-explainer-storyboard.md",
    "NWR-073": "artifacts/NWR-073-layer-lineage-card.md",
    "NWR-081": "artifacts/NWR-081-cross-domain-transfer-grid.md",
    "NWR-089": "artifacts/NWR-089-portfolio-acceleration-dashboard-spec.md",
}

REQUIRED_FILES = [
    MANIFEST_PATH,
    SPRINT_MD,
    INDEX_PATH,
    APPROVAL_PATH,
    *[EXP_DIR / rel_path for rel_path in EXPECTED_ARTIFACTS.values()],
]

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "status",
    "decision",
    "claim_ceiling",
    "source_intake_experiment_id",
    "selected_seed_count",
    "artifact_count",
    "lab_execution_approval_recorded",
    "approval_record",
    "local_context",
    "external_actions_taken",
    "dependencies_installed",
    "papers_generated",
    "manuscripts_generated",
    "publication_pdf_generated",
    "private_data_downloaded",
    "external_submission_made",
    "rights_or_authority_cleared",
    "human_reviewer_identity_recorded",
    "public_release_claimed",
    "blocked_promotions",
    "artifact_paths",
    "exact_next_action",
}

REQUIRED_LOCAL_CONTEXT = {
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/manifest.json",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/research_seeds.csv",
    "experiments/EXP-FRONTIER-015-hundred-paper-recovery-intake/sprint_selection.json",
    "research/frontier/nwagu_aneke/FRONTIER_LAB_STATUS.json",
}

INDEX_FIELDS = {
    "seed_id",
    "lane_id",
    "evidence_layer",
    "artifact_path",
    "artifact_type",
    "status",
    "claim_ceiling",
    "next_action",
}

ALLOWED_EVIDENCE_LAYERS = {
    "source_observed",
    "derived",
    "speculative",
    "application",
    "infrastructure",
    "authority_rights",
}

FORBIDDEN_TEXT = [
    "paper-ready",
    "submission-ready",
    "ready_for_human_arxiv_review",
    "public_release_ready",
    "frontier proof",
    "novelty clearance",
    "publication pdf generated",
    "rights cleared",
    "authority approved",
    "source-observed 27/216",
    "100 papers generated",
    "manuscripts generated",
    "accepted paper",
    "ready for external submission",
    "public release approved",
]

REQUIRED_ARTIFACT_PHRASES = [
    "bounded artifact",
    "evidence layer",
    "falsification gate",
    "rights and authority guardrail",
    "what this teaches oroma",
    "next action",
    "artifact_not_paper_candidate",
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
        if manifest.get("experiment_id") != "EXP-FRONTIER-016":
            errors.append("manifest experiment_id must be EXP-FRONTIER-016")
        if manifest.get("status") != "SELECTED_SEED_ARTIFACTS_READY_INTERNAL_ONLY":
            errors.append("manifest status must be selected seed artifacts ready internal only")
        if manifest.get("decision") != "create_bounded_artifacts_from_approved_seed_selection_without_maturity_claims":
            errors.append("manifest decision must create bounded artifacts without maturity claims")
        if manifest.get("claim_ceiling") != "selected_seed_artifacts_not_paper_candidates":
            errors.append("manifest claim ceiling must block paper-candidate claims")
        if manifest.get("source_intake_experiment_id") != "EXP-FRONTIER-015":
            errors.append("manifest must link to EXP-FRONTIER-015")
        if manifest.get("selected_seed_count") != 12 or manifest.get("artifact_count") != 12:
            errors.append("manifest must record 12 selected seeds and 12 artifacts")
        if manifest.get("lab_execution_approval_recorded") is not True:
            errors.append("manifest must record lab execution approval")
        if manifest.get("approval_record") != "approval_record.json":
            errors.append("manifest approval_record must be approval_record.json")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")
        for field in [
            "dependencies_installed",
            "papers_generated",
            "manuscripts_generated",
            "publication_pdf_generated",
            "private_data_downloaded",
            "external_submission_made",
            "rights_or_authority_cleared",
            "human_reviewer_identity_recorded",
            "public_release_claimed",
        ]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")
        local_context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_LOCAL_CONTEXT - local_context)
        if missing_context:
            errors.append(f"manifest missing local_context: {missing_context}")
        artifact_paths = set(manifest.get("artifact_paths", []))
        expected_paths = set(EXPECTED_ARTIFACTS.values())
        if artifact_paths != expected_paths:
            errors.append("manifest artifact_paths must exactly match expected selected seed artifacts")
        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "paper candidate claim",
            "manuscript set claim",
            "public release claim",
            "rights or authority clearance claim",
            "external submission",
            "frontier novelty claim",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        approval = read_json(APPROVAL_PATH)
        if approval.get("approval_id") != "LAB-EXEC-APPROVAL-20260623-USER":
            errors.append("approval id must record the user lab approval")
        if approval.get("approval_scope") != "internal_bounded_artifact_creation_for_selected_seed_sprint":
            errors.append("approval scope must be internal bounded artifact creation")
        if approval.get("external_authority_review_completed") is not False:
            errors.append("approval must not claim external authority review")
        if approval.get("rights_or_authority_cleared") is not False:
            errors.append("approval must not claim rights or authority clearance")
        if approval.get("external_actions_taken") != []:
            errors.append("approval external_actions_taken must be empty")

        selection = read_json(SOURCE_SELECTION)
        if selection.get("selected_seed_ids") != EXPECTED_SELECTED_IDS:
            errors.append("EXP-FRONTIER-015 selected_seed_ids changed unexpectedly")
        source_rows = {row["seed_id"]: row for row in read_csv(SOURCE_SEEDS)}

        index_rows = read_csv(INDEX_PATH)
        if len(index_rows) != 12:
            errors.append(f"artifact_index.csv must contain 12 rows, found {len(index_rows)}")
        if index_rows and set(index_rows[0].keys()) != INDEX_FIELDS:
            errors.append("artifact_index.csv header must exactly match required fields")
        indexed_ids = [row.get("seed_id", "") for row in index_rows]
        if indexed_ids != EXPECTED_SELECTED_IDS:
            errors.append("artifact_index.csv seed order must match selected seed ids")
        for row in index_rows:
            seed_id = row.get("seed_id", "")
            source = source_rows.get(seed_id, {})
            expected_path = EXPECTED_ARTIFACTS.get(seed_id)
            if row.get("artifact_path") != expected_path:
                errors.append(f"{seed_id}: artifact_path must be {expected_path}")
            if row.get("lane_id") != source.get("lane_id"):
                errors.append(f"{seed_id}: lane_id must match source seed")
            if row.get("evidence_layer") != source.get("evidence_layer"):
                errors.append(f"{seed_id}: evidence_layer must match source seed")
            if row.get("evidence_layer") not in ALLOWED_EVIDENCE_LAYERS:
                errors.append(f"{seed_id}: invalid evidence_layer")
            if row.get("status") != "bounded_artifact_internal_only":
                errors.append(f"{seed_id}: status must be bounded_artifact_internal_only")
            if row.get("claim_ceiling") != "artifact_not_paper_candidate":
                errors.append(f"{seed_id}: claim_ceiling must be artifact_not_paper_candidate")
            if not row.get("next_action"):
                errors.append(f"{seed_id}: next_action is required")

        for seed_id, rel_path in EXPECTED_ARTIFACTS.items():
            path = EXP_DIR / rel_path
            text = path.read_text(encoding="utf-8")
            lower = text.lower()
            if seed_id.lower() not in lower:
                errors.append(f"{rel_path}: missing seed id")
            source = source_rows.get(seed_id, {})
            if source.get("evidence_layer", "").lower() not in lower:
                errors.append(f"{rel_path}: missing source evidence layer")
            if source.get("research_question", "").lower() not in lower:
                errors.append(f"{rel_path}: missing source research question")
            for phrase in REQUIRED_ARTIFACT_PHRASES:
                if phrase not in lower:
                    errors.append(f"{rel_path}: missing phrase {phrase}")

        markdown = SPRINT_MD.read_text(encoding="utf-8").lower()
        for phrase in [
            "selected seed artifact sprint",
            "12 bounded artifacts",
            "lab execution approval",
            "not rights or authority clearance",
            "selected_seed_artifacts_not_paper_candidates",
            "what this teaches oroma",
            "exact next action",
        ]:
            if phrase not in markdown:
                errors.append(f"sprint markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden selected-seed artifact text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in selected seed artifact packet")

    if errors:
        print("SELECTED_SEED_ARTIFACT_SPRINT_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("SELECTED_SEED_ARTIFACT_SPRINT_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
