from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-008-nwagu-ro-crate"
DECISION_DIR = EXP_DIR / "preservation_decision"
DECISION_JSON = DECISION_DIR / "decision.json"
DECISION_MD = DECISION_DIR / "PRESERVATION_DECISION.md"
DECISION_MATRIX = DECISION_DIR / "decision_matrix.csv"
DEFERRED_ACTIONS = DECISION_DIR / "deferred_actions.md"

REQUIRED_FILES = [
    DECISION_JSON,
    DECISION_MD,
    DECISION_MATRIX,
    DEFERRED_ACTIONS,
]

REQUIRED_PRIMARY_SOURCES = {
    "https://www.datalad.org/",
    "https://handbook.datalad.org/en/latest/book_main.html",
    "https://www.softwareheritage.org/",
    "https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html",
}

REQUIRED_BLOCKERS = {
    "rights review",
    "authority review",
    "public release approval",
    "source-image exclusion",
    "private-data exclusion",
    "dataset boundary review",
}

FORBIDDEN_TEXT = [
    "swhid assigned",
    "archived by software heritage",
    "datalad dataset created",
    "public release approved",
    "rights cleared",
    "authority approved",
    "paper-ready",
    "submission-ready",
    "source-observed 27/216",
]

REQUIRED_MATRIX_ROUTES = {
    "repo_local_internal_metadata_package",
    "datalad_versioned_dataset",
    "software_heritage_archive_identifier",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_decision_json(errors: list[str]) -> None:
    decision = read_json(DECISION_JSON)
    if decision.get("decision_id") != "PRESERVE-EXP-FRONTIER-008-001":
        errors.append("decision_id must be PRESERVE-EXP-FRONTIER-008-001")
    if decision.get("experiment_id") != "EXP-FRONTIER-008":
        errors.append("experiment_id must be EXP-FRONTIER-008")
    if decision.get("status") != "repo_local_internal_now":
        errors.append("status must be repo_local_internal_now")
    if decision.get("selected_path") != "repo_local_internal_metadata_package":
        errors.append("selected_path must stay repo-local for now")
    if decision.get("claim_ceiling") != "preservation_route_decision_not_release":
        errors.append("claim_ceiling must be preservation_route_decision_not_release")
    if decision.get("external_actions_taken") != []:
        errors.append("external_actions_taken must be an empty list")

    routes = decision.get("routes")
    if not isinstance(routes, dict):
        errors.append("routes must be an object")
        routes = {}

    expected_route_decisions = {
        "repo_local_internal_metadata_package": "selected_now",
        "datalad_versioned_dataset": "defer_until_dataset_boundary_review",
        "software_heritage_archive_identifier": "defer_until_public_release_or_archive_approval",
    }
    for route_id, expected in expected_route_decisions.items():
        route = routes.get(route_id)
        if not isinstance(route, dict):
            errors.append(f"missing route: {route_id}")
            continue
        if route.get("decision") != expected:
            errors.append(f"{route_id} decision must be {expected}")
        if route.get("external_action_now") is not False:
            errors.append(f"{route_id} external_action_now must be false")

    primary_sources = {
        url
        for urls in decision.get("primary_sources", {}).values()
        for url in urls
        if isinstance(url, str)
    }
    missing_sources = sorted(REQUIRED_PRIMARY_SOURCES - primary_sources)
    if missing_sources:
        errors.append(f"decision missing primary sources: {missing_sources}")

    blockers = set(decision.get("blockers", []))
    missing_blockers = sorted(REQUIRED_BLOCKERS - blockers)
    if missing_blockers:
        errors.append(f"decision missing blockers: {missing_blockers}")

    forbidden_actions = set(decision.get("forbidden_current_actions", []))
    for required_action in [
        "create DataLad dataset",
        "request Software Heritage save",
        "claim SWHID",
        "deposit public release",
        "include restricted source material",
    ]:
        if required_action not in forbidden_actions:
            errors.append(f"missing forbidden current action: {required_action}")


def validate_matrix(errors: list[str]) -> None:
    rows = read_csv(DECISION_MATRIX)
    routes = {row.get("route_id") for row in rows}
    missing_routes = sorted(REQUIRED_MATRIX_ROUTES - routes)
    if missing_routes:
        errors.append(f"decision matrix missing routes: {missing_routes}")
    for row in rows:
        route_id = row.get("route_id", "")
        if route_id in REQUIRED_MATRIX_ROUTES and row.get("external_action_now") != "no":
            errors.append(f"{route_id} must have external_action_now=no")
        if route_id == "repo_local_internal_metadata_package" and row.get("decision") != "selected_now":
            errors.append("repo-local matrix route must be selected_now")
        if route_id == "datalad_versioned_dataset" and row.get("decision") != "defer_until_dataset_boundary_review":
            errors.append("DataLad matrix route must be deferred for dataset boundary review")
        if route_id == "software_heritage_archive_identifier" and row.get("decision") != "defer_until_public_release_or_archive_approval":
            errors.append("Software Heritage matrix route must be deferred for public-release/archive approval")


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        validate_decision_json(errors)
        validate_matrix(errors)

        combined = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in REQUIRED_FILES
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden preservation claim: {forbidden}")

        for required in [
            "DataLad",
            "Software Heritage",
            "repo-local",
            "no external submission",
            "no dependency installation",
            "metadata package",
            "preservation_route_decision_not_release",
        ]:
            if required.lower() not in combined:
                errors.append(f"decision packet missing required phrase: {required}")

    if errors:
        print("NWAGU_PRESERVATION_DECISION_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("NWAGU_PRESERVATION_DECISION_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
