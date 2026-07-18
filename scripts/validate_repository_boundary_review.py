from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-012-repository-boundary-review"
MANIFEST_PATH = EXP_DIR / "manifest.json"
REVIEW_MD = EXP_DIR / "REPOSITORY_BOUNDARY_REVIEW.md"
INVENTORY_PATH = EXP_DIR / "repository_asset_inventory.csv"
EXCLUSIONS_PATH = EXP_DIR / "excluded_repository_paths.csv"
CHECKLIST_PATH = EXP_DIR / "future_public_package_checklist.json"
QUESTIONS_PATH = EXP_DIR / "reviewer_questions.csv"

REQUIRED_FILES = [
    MANIFEST_PATH,
    REVIEW_MD,
    INVENTORY_PATH,
    EXCLUSIONS_PATH,
    CHECKLIST_PATH,
    QUESTIONS_PATH,
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
    "private_data_downloaded",
    "repository_export_created",
    "software_heritage_request_made",
    "archive_identifier_claimed",
    "repository_deposited",
    "public_release_claimed",
    "public_package_approved",
    "candidate_inventory_status",
    "blocked_promotions",
    "required_before_release_or_archive",
    "exact_next_action",
}

REQUIRED_LOCAL_CONTEXT = {
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/ro-crate-metadata.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/candidate_files.csv",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/boundary_review.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/manifest.json",
    "research/frontier/nwagu_transfer_atlas/prior_art_verification/verification_manifest.json",
}

REQUIRED_RELEASE_GATES = {
    "repository path audit complete",
    "restricted and source-material exclusion review",
    "rights and authority review",
    "license and citation metadata review",
    "private-data and contact-data exclusion review",
    "human preservation-infrastructure review",
    "explicit user/lab release and archive approval",
}

REQUIRED_CANDIDATE_PATHS = {
    "scripts/continuous_research_loop.py",
    "scripts/validate_continuous_research_loop.py",
    "scripts/validate_software_heritage_no_identifier_decision.py",
    "scripts/validate_repository_boundary_review.py",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/ro-crate-metadata.json",
    "experiments/EXP-FRONTIER-011-software-heritage-no-identifier-decision/manifest.json",
    "experiments/EXP-FRONTIER-012-repository-boundary-review/manifest.json",
    "research/frontier/nwagu_aneke/FRONTIER_LAB_STATUS.json",
    "research/frontier/nwagu_transfer_atlas/prior_art_verification/verification_manifest.json",
    "Makefile",
}

FORBIDDEN_CANDIDATE_SNIPPETS = [
    "primary_sources/",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".tif",
    ".tiff",
    "private_data",
    "contact_records",
    ".env",
    "secret",
    "credential",
]

REQUIRED_EXCLUSION_PATTERNS = {
    "research/pagc/primary_sources/",
    "research/frontier/nwagu_aneke/primary_sources/",
    "primary_sources/",
    "*.pdf",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.tif",
    "*.tiff",
    ".env",
    "private_data",
    "contact_records",
    "human_reader_response_csv",
    "restricted_manuscript_material",
}

REQUIRED_REVIEW_ROLES = {
    "repository_boundary_reviewer",
    "rights_authority_reviewer",
    "source_dossier_reviewer",
    "preservation_infrastructure_reviewer",
    "data_protection_reviewer",
}

REQUIRED_CHECKLIST_ITEMS = {
    "PATH_AUDIT_COMPLETE",
    "RESTRICTED_EXCLUSION_VALIDATED",
    "RIGHTS_AUTHORITY_REVIEWED",
    "LICENSE_CITATION_REVIEWED",
    "PRIVATE_CONTACT_EXCLUSION_VALIDATED",
    "PRESERVATION_REVIEW_COMPLETE",
    "EXPLICIT_RELEASE_ARCHIVE_APPROVAL",
}

FORBIDDEN_TEXT = [
    "public release approved",
    "rights cleared",
    "authority approved",
    "software heritage save requested",
    "save code now completed",
    "save code now requested",
    "swhid assigned",
    "archive identifier assigned",
    "archived by software heritage",
    "archive deposit complete",
    "paper-ready",
    "submission-ready",
    "source-observed 27/216",
]

REQUIRED_MARKDOWN_PHRASES = [
    "repository-boundary review",
    "candidate internal review only",
    "excluded repository paths",
    "repository_boundary_review_not_public_release",
    "no archive action",
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

        if manifest.get("experiment_id") != "EXP-FRONTIER-012":
            errors.append("manifest experiment_id must be EXP-FRONTIER-012")
        if manifest.get("atlas_id") != "ATLAS-0043":
            errors.append("manifest atlas_id must be ATLAS-0043")
        if manifest.get("status") != "REPOSITORY_BOUNDARY_REVIEW_OPEN_NOT_APPROVED":
            errors.append("manifest status must open review without approval")
        if manifest.get("decision") != "open_repository_boundary_review_without_release_or_archive_action":
            errors.append("manifest decision must open review without release/archive action")
        if manifest.get("claim_ceiling") != "repository_boundary_review_not_public_release":
            errors.append("manifest claim ceiling must block public-release claims")
        if manifest.get("candidate_inventory_status") != "draft_internal_candidates_only":
            errors.append("manifest candidate inventory status must remain draft/internal")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")

        for field in [
            "dependencies_installed",
            "private_data_downloaded",
            "repository_export_created",
            "software_heritage_request_made",
            "archive_identifier_claimed",
            "repository_deposited",
            "public_release_claimed",
            "public_package_approved",
        ]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")

        local_context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_LOCAL_CONTEXT - local_context)
        if missing_context:
            errors.append(f"manifest missing local_context paths: {missing_context}")
        for rel_path in local_context:
            if not (ROOT / rel_path).exists():
                errors.append(f"manifest local_context does not exist: {rel_path}")

        required_before = set(manifest.get("required_before_release_or_archive", []))
        missing_gates = sorted(REQUIRED_RELEASE_GATES - required_before)
        if missing_gates:
            errors.append(f"manifest missing release/archive gates: {missing_gates}")

        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "public repository package",
            "Software Heritage archive action",
            "archive identifier assignment",
            "rights or authority clearance claim",
            "article or submission maturity status",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        candidates = read_csv(INVENTORY_PATH)
        candidate_paths = {row.get("path") for row in candidates}
        missing_candidates = sorted(REQUIRED_CANDIDATE_PATHS - candidate_paths)
        if missing_candidates:
            errors.append(f"repository asset inventory missing paths: {missing_candidates}")
        for row in candidates:
            path = row.get("path", "")
            if not path:
                errors.append("candidate row missing path")
                continue
            if not (ROOT / path).exists():
                errors.append(f"candidate path does not exist: {path}")
            for forbidden in FORBIDDEN_CANDIDATE_SNIPPETS:
                if forbidden.lower() in path.lower():
                    errors.append(f"candidate path must not include restricted/release-blocked material: {path}")
            if row.get("current_boundary_status") != "candidate_internal_review_only":
                errors.append(f"{path}: current_boundary_status must be candidate_internal_review_only")
            if row.get("external_release_now") != "no":
                errors.append(f"{path}: external_release_now must be no")
            if row.get("required_review") != "repository_boundary_review":
                errors.append(f"{path}: required_review must be repository_boundary_review")

        exclusions = read_csv(EXCLUSIONS_PATH)
        patterns = {row.get("pattern") for row in exclusions}
        missing_patterns = sorted(REQUIRED_EXCLUSION_PATTERNS - patterns)
        if missing_patterns:
            errors.append(f"excluded repository paths missing patterns: {missing_patterns}")
        for row in exclusions:
            pattern = row.get("pattern", "")
            if row.get("current_status") != "excluded_pending_review":
                errors.append(f"{pattern}: current_status must be excluded_pending_review")
            if row.get("allowed_without_review") != "no":
                errors.append(f"{pattern}: allowed_without_review must be no")
            if not row.get("validator_control"):
                errors.append(f"{pattern}: validator_control is required")

        questions = read_csv(QUESTIONS_PATH)
        roles = {row.get("review_role") for row in questions}
        missing_roles = sorted(REQUIRED_REVIEW_ROLES - roles)
        if missing_roles:
            errors.append(f"reviewer questions missing roles: {missing_roles}")
        for row in questions:
            role = row.get("review_role", "")
            if row.get("current_status") != "unanswered":
                errors.append(f"{role}: current_status must be unanswered")
            if row.get("required_before") != "repository_boundary_decision":
                errors.append(f"{role}: required_before must be repository_boundary_decision")

        checklist = read_json(CHECKLIST_PATH)
        if checklist.get("checklist_id") != "REPO-BOUNDARY-REVIEW-CHECKLIST-001":
            errors.append("future package checklist id is invalid")
        if checklist.get("status") != "review_open_not_approved":
            errors.append("future package checklist status must be review_open_not_approved")
        if checklist.get("claim_ceiling") != "repository_boundary_review_not_public_release":
            errors.append("future package checklist claim ceiling must block public release")
        if checklist.get("all_items_required_before_release_or_archive") is not True:
            errors.append("future package checklist must require all items before release/archive")
        checklist_items = {
            item.get("item_id"): item
            for item in checklist.get("items", [])
            if isinstance(item, dict)
        }
        missing_items = sorted(REQUIRED_CHECKLIST_ITEMS - checklist_items.keys())
        if missing_items:
            errors.append(f"future package checklist missing items: {missing_items}")
        for item_id in REQUIRED_CHECKLIST_ITEMS & checklist_items.keys():
            if checklist_items[item_id].get("current_status") != "not_satisfied":
                errors.append(f"{item_id}: current_status must be not_satisfied")

        markdown = REVIEW_MD.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in markdown:
                errors.append(f"review markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden repository-boundary text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in repository-boundary packet")

    if errors:
        print("REPOSITORY_BOUNDARY_REVIEW_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("REPOSITORY_BOUNDARY_REVIEW_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
