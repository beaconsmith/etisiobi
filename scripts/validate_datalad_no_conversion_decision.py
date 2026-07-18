from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-010-datalad-no-conversion-decision"
MANIFEST_PATH = EXP_DIR / "manifest.json"
DECISION_MD = EXP_DIR / "NO_CONVERSION_DECISION.md"
BLOCKERS_PATH = EXP_DIR / "conversion_blockers.csv"
READINESS_PATH = EXP_DIR / "future_readiness_checklist.json"

REQUIRED_FILES = [
    MANIFEST_PATH,
    DECISION_MD,
    BLOCKERS_PATH,
    READINESS_PATH,
]

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "atlas_id",
    "status",
    "decision",
    "claim_ceiling",
    "primary_sources",
    "local_context",
    "external_actions_taken",
    "dependencies_installed",
    "datalad_installed",
    "datalad_command_run",
    "dataset_created",
    "private_data_downloaded",
    "public_release_claimed",
    "blocked_promotions",
    "required_before_conversion",
    "exact_next_action",
}

PRIMARY_SOURCES = {
    "https://www.datalad.org/",
    "https://docs.datalad.org/en/stable/",
    "https://handbook.datalad.org/en/latest/book_main.html",
}

REQUIRED_LOCAL_CONTEXT = {
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/decision.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/preservation_decision/PRESERVATION_DECISION.md",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/boundary_review.json",
    "experiments/EXP-FRONTIER-008-nwagu-ro-crate/dataset_boundary/candidate_files.csv",
    "research/frontier/nwagu_transfer_atlas/prior_art_verification/verification_manifest.json",
}

REQUIRED_CONVERSION_GATES = {
    "dataset boundary approval",
    "rights review",
    "authority review",
    "restricted-material exclusion audit",
    "private-data exclusion audit",
    "annex policy for large or sensitive files",
    "human preservation-infrastructure review",
    "explicit user/lab conversion approval",
}

REQUIRED_BLOCKER_IDS = {
    "dataset_boundary_unapproved",
    "rights_authority_unreviewed",
    "restricted_material_policy_unsettled",
    "annex_policy_absent",
    "public_release_not_approved",
}

FORBIDDEN_TEXT = [
    "datalad dataset created",
    "datalad installed",
    "datalad create",
    "datalad save",
    "datalad push",
    "conversion complete",
    "public release approved",
    "rights cleared",
    "authority approved",
    "paper-ready",
    "submission-ready",
    "source-observed 27/216",
]

REQUIRED_MARKDOWN_PHRASES = [
    "no-conversion decision",
    "no dependency installation",
    "no datalad command",
    "reproducibility_planning_not_dataset_conversion",
    "dataset boundary approval",
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

        if manifest.get("experiment_id") != "EXP-FRONTIER-010":
            errors.append("manifest experiment_id must be EXP-FRONTIER-010")
        if manifest.get("atlas_id") != "ATLAS-0040":
            errors.append("manifest atlas_id must be ATLAS-0040")
        if manifest.get("status") != "DATALAD_NO_CONVERSION_DECISION_READY_NOT_EXECUTED":
            errors.append("manifest status must be no-conversion ready and not executed")
        if manifest.get("decision") != "defer_conversion_until_boundary_and_authority_gates":
            errors.append("manifest decision must defer conversion until boundary and authority gates")
        if manifest.get("claim_ceiling") != "reproducibility_planning_not_dataset_conversion":
            errors.append("manifest claim ceiling must block dataset-conversion claims")
        if set(manifest.get("primary_sources", [])) != PRIMARY_SOURCES:
            errors.append("manifest primary_sources must exactly match DataLad primary sources")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")

        for field in [
            "dependencies_installed",
            "datalad_installed",
            "datalad_command_run",
            "dataset_created",
            "private_data_downloaded",
            "public_release_claimed",
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

        required_before = set(manifest.get("required_before_conversion", []))
        missing_gates = sorted(REQUIRED_CONVERSION_GATES - required_before)
        if missing_gates:
            errors.append(f"manifest missing required conversion gates: {missing_gates}")

        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "DataLad dataset conversion",
            "public dataset release",
            "rights or authority clearance claim",
            "derived-layer source-status promotion",
            "article or submission maturity status",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        blockers = read_csv(BLOCKERS_PATH)
        blocker_ids = {row.get("blocker_id") for row in blockers}
        missing_blockers = sorted(REQUIRED_BLOCKER_IDS - blocker_ids)
        if missing_blockers:
            errors.append(f"conversion_blockers.csv missing blockers: {missing_blockers}")
        for row in blockers:
            blocker_id = row.get("blocker_id", "")
            if row.get("current_status") != "blocks_conversion":
                errors.append(f"{blocker_id}: current_status must be blocks_conversion")
            if row.get("external_action_allowed") != "no":
                errors.append(f"{blocker_id}: external_action_allowed must be no")
            if not row.get("required_resolution"):
                errors.append(f"{blocker_id}: required_resolution is required")

        readiness = read_json(READINESS_PATH)
        if readiness.get("checklist_id") != "DATALAD-NO-CONVERSION-CHECKLIST-001":
            errors.append("future readiness checklist id is invalid")
        if readiness.get("status") != "not_ready_for_conversion":
            errors.append("future readiness status must be not_ready_for_conversion")
        if readiness.get("claim_ceiling") != "reproducibility_planning_not_dataset_conversion":
            errors.append("future readiness claim ceiling must block conversion claims")
        if readiness.get("all_items_required_before_conversion") is not True:
            errors.append("future readiness checklist must require all items before conversion")
        readiness_items = {item.get("item_id"): item for item in readiness.get("items", []) if isinstance(item, dict)}
        for required_item in [
            "BOUNDARY_APPROVED",
            "RIGHTS_AUTHORITY_REVIEWED",
            "RESTRICTED_EXCLUSION_VALIDATED",
            "ANNEX_POLICY_DEFINED",
            "CONVERSION_APPROVED",
        ]:
            item = readiness_items.get(required_item)
            if not item:
                errors.append(f"future readiness missing item: {required_item}")
                continue
            if item.get("current_status") != "not_satisfied":
                errors.append(f"{required_item}: current_status must be not_satisfied")

        markdown = DECISION_MD.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in markdown:
                errors.append(f"decision markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden DataLad no-conversion text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in DataLad no-conversion packet")

    if errors:
        print("DATALAD_NO_CONVERSION_DECISION_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("DATALAD_NO_CONVERSION_DECISION_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
