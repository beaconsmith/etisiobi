from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "research" / "frontier" / "nwagu_transfer_atlas" / "prior_art_verification"

MANIFEST = PACKET_DIR / "verification_manifest.json"
PACKET_MD = PACKET_DIR / "SELECTED_INFRASTRUCTURE_PRIOR_ART.md"
SOURCES_CSV = PACKET_DIR / "verified_sources.csv"
BOUNDARIES_CSV = PACKET_DIR / "claim_boundaries.csv"

REQUIRED_FILES = [
    MANIFEST,
    PACKET_MD,
    SOURCES_CSV,
    BOUNDARIES_CSV,
]

VERIFICATION_ID = "NWAGU-PRIOR-ART-VERIFY-001"
CLAIM_CEILING = "prior_art_relevance_not_frontier_claim"
SELECTED_RECORDS = {
    "ATLAS-0049": "Inspect AI",
    "ATLAS-0052": "MLAgentBench",
    "ATLAS-0039": "RO-Crate",
    "ATLAS-0040": "DataLad",
    "ATLAS-0043": "Software Heritage",
}

FORBIDDEN_TEXT = [
    "novelty cleared",
    "frontier proof",
    "paper-ready",
    "submission-ready",
    "public release approved",
    "rights cleared",
    "authority approved",
    "source-observed 27/216",
    "dependency installed",
    "model run completed",
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
    if manifest.get("verification_id") != VERIFICATION_ID:
        errors.append(f"verification_id must be {VERIFICATION_ID}")
    if manifest.get("status") != "selected_primary_source_relevance_verified_not_novelty_clearance":
        errors.append("manifest status must keep relevance verification below novelty clearance")
    if manifest.get("claim_ceiling") != CLAIM_CEILING:
        errors.append(f"manifest claim_ceiling must be {CLAIM_CEILING}")
    if manifest.get("whole_atlas_prior_art_status") != "not_verified":
        errors.append("whole_atlas_prior_art_status must remain not_verified")
    if manifest.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be empty")
    if manifest.get("dependencies_installed") is not False:
        errors.append("dependencies_installed must be false")
    if manifest.get("model_or_api_run") is not False:
        errors.append("model_or_api_run must be false")
    if manifest.get("private_data_downloaded") is not False:
        errors.append("private_data_downloaded must be false")

    records = manifest.get("selected_records", [])
    if not isinstance(records, list):
        errors.append("selected_records must be a list")
        records = []
    record_map = {record.get("atlas_id"): record.get("project") for record in records if isinstance(record, dict)}
    if record_map != SELECTED_RECORDS:
        errors.append(f"selected_records must exactly match {SELECTED_RECORDS}")
    for record in records:
        if not isinstance(record, dict):
            continue
        atlas_id = record.get("atlas_id", "")
        if record.get("verified_status") != "primary_source_relevance_verified_not_novelty_clearance":
            errors.append(f"{atlas_id}: verified_status must be primary_source_relevance_verified_not_novelty_clearance")
        if record.get("claim_ceiling") != CLAIM_CEILING:
            errors.append(f"{atlas_id}: claim_ceiling must be {CLAIM_CEILING}")
        if not record.get("bounded_next_action"):
            errors.append(f"{atlas_id}: bounded_next_action is required")


def validate_sources(errors: list[str]) -> None:
    rows = read_csv(SOURCES_CSV)
    by_atlas: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_atlas.setdefault(row.get("atlas_id", ""), []).append(row)

    missing = sorted(set(SELECTED_RECORDS) - set(by_atlas))
    if missing:
        errors.append(f"verified sources missing atlas ids: {missing}")

    for atlas_id, project in SELECTED_RECORDS.items():
        rows_for_atlas = by_atlas.get(atlas_id, [])
        if len(rows_for_atlas) < 2:
            errors.append(f"{atlas_id}: at least two primary sources are required")
        for row in rows_for_atlas:
            if row.get("project") != project:
                errors.append(f"{atlas_id}: project must be {project}")
            if row.get("source_type") != "primary_source":
                errors.append(f"{atlas_id}: every source_type must be primary_source")
            if row.get("authority_level") not in {"official_documentation", "official_repository", "primary_paper", "official_service"}:
                errors.append(f"{atlas_id}: invalid authority_level {row.get('authority_level')}")
            if row.get("verified_status") != "relevance_verified_not_novelty_clearance":
                errors.append(f"{atlas_id}: source verified_status must be relevance_verified_not_novelty_clearance")
            if row.get("claim_ceiling") != CLAIM_CEILING:
                errors.append(f"{atlas_id}: source claim_ceiling must be {CLAIM_CEILING}")
            url = row.get("source_url", "")
            if not url.startswith("https://"):
                errors.append(f"{atlas_id}: source_url must be https: {url}")
            if not row.get("relevance_summary"):
                errors.append(f"{atlas_id}: relevance_summary is required")


def validate_boundaries(errors: list[str]) -> None:
    rows = read_csv(BOUNDARIES_CSV)
    by_atlas = {row.get("atlas_id"): row for row in rows}
    if set(by_atlas) != set(SELECTED_RECORDS):
        errors.append("claim boundaries must have exactly one row per selected record")
    for atlas_id, project in SELECTED_RECORDS.items():
        row = by_atlas.get(atlas_id, {})
        if row.get("project") != project:
            errors.append(f"{atlas_id}: boundary project must be {project}")
        if row.get("allowed_claim") != "relevance_to_bounded_infrastructure_experiment":
            errors.append(f"{atlas_id}: allowed_claim must stay bounded")
        if row.get("forbidden_claim") != "novelty_frontier_or_result_claim":
            errors.append(f"{atlas_id}: forbidden_claim must block novelty/frontier/result claims")
        if row.get("next_gate") not in {
            "bounded_experiment_plan",
            "execution_approval",
            "dataset_boundary_review",
            "archive_decision_review",
        }:
            errors.append(f"{atlas_id}: next_gate is invalid")


def validate_markdown(errors: list[str]) -> None:
    lower = PACKET_MD.read_text(encoding="utf-8").lower()
    for required in [
        VERIFICATION_ID.lower(),
        CLAIM_CEILING,
        "selected infrastructure prior-art verification",
        "whole atlas remains not verified",
        "no dependency installation",
        "no model or api run",
        "no novelty clearance",
    ]:
        if required.lower() not in lower:
            errors.append(f"packet markdown missing required phrase: {required}")
    for atlas_id, project in SELECTED_RECORDS.items():
        if atlas_id.lower() not in lower or project.lower() not in lower:
            errors.append(f"packet markdown missing selected record {atlas_id} {project}")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {rel(path)}")

    if not errors:
        validate_manifest(errors)
        validate_sources(errors)
        validate_boundaries(errors)
        validate_markdown(errors)

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden prior-art verification claim: {forbidden}")

    if errors:
        print("NWAGU_PRIOR_ART_VERIFICATION_PACKET_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_PRIOR_ART_VERIFICATION_PACKET_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
