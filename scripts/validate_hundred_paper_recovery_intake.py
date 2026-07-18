from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-015-hundred-paper-recovery-intake"
MANIFEST_PATH = EXP_DIR / "manifest.json"
INTAKE_MD = EXP_DIR / "HUNDRED_PAPER_RECOVERY_INTAKE.md"
SEEDS_CSV = EXP_DIR / "research_seeds.csv"
SCHEMA_PATH = EXP_DIR / "research_seed_schema.json"
CLAIM_GATES_CSV = EXP_DIR / "claim_gate_matrix.csv"
SPRINT_SELECTION_PATH = EXP_DIR / "sprint_selection.json"

REQUIRED_FILES = [
    MANIFEST_PATH,
    INTAKE_MD,
    SEEDS_CSV,
    SCHEMA_PATH,
    CLAIM_GATES_CSV,
    SPRINT_SELECTION_PATH,
]

EXPECTED_STATUS = "HUNDRED_PAPER_RECOVERY_INTAKE_READY_SEEDS_ONLY"
EXPECTED_DECISION = "seed_100_research_questions_without_paper_or_readiness_claims"
EXPECTED_CLAIM_CEILING = "research_intake_not_paper_pipeline_completion"
SEED_STATUS = "seed_only_not_paper_candidate"
SEED_CLAIM_CEILING = "research_seed_not_paper_claim"

REQUIRED_LOCAL_CONTEXT = {
    "wiki/index.md",
    "research/frontier/nwagu_aneke/FRONTIER_LAB_STATUS.json",
    "research/frontier/nwagu_aneke/FRONTIER_OPPORTUNITY_REGISTER.md",
    "research/frontier/nwagu_aneke/FRONTIER_PORTFOLIO_SCORECARD.md",
    "research/frontier/nwagu_aneke/EXPERIMENT_BACKLOG.md",
    "research/frontier/nwagu_aneke/ARTICLE_AND_PRODUCT_PORTFOLIO.md",
}

REQUIRED_SEED_FIELDS = {
    "seed_id",
    "lane_id",
    "opportunity_id",
    "working_title",
    "research_question",
    "evidence_layer",
    "first_artifact",
    "falsification_gate",
    "rights_authority_gate",
    "product_or_lab_payoff",
    "status",
    "claim_ceiling",
    "next_action",
}

REQUIRED_EVIDENCE_LAYERS = {
    "source_observed",
    "derived",
    "speculative",
    "application",
    "infrastructure",
    "authority_rights",
}

REQUIRED_LANE_IDS = {str(index) for index in range(1, 13)}
REQUIRED_OPPORTUNITY_IDS = {f"OPP-{index:03d}" for index in range(1, 13)}

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "status",
    "decision",
    "claim_ceiling",
    "paper_count_target",
    "seed_count",
    "local_context",
    "external_actions_taken",
    "dependencies_installed",
    "papers_generated",
    "manuscripts_generated",
    "publication_pdf_generated",
    "private_data_downloaded",
    "human_review_completed",
    "rights_or_authority_cleared",
    "public_release_claimed",
    "blocked_promotions",
    "exact_next_action",
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
]

REQUIRED_MARKDOWN_PHRASES = [
    "100-paper recovery intake",
    "100 research seeds",
    "seed-only",
    "zero manuscript outputs",
    EXPECTED_CLAIM_CEILING,
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
        missing_manifest = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
        if missing_manifest:
            errors.append(f"manifest missing fields: {missing_manifest}")

        if manifest.get("experiment_id") != "EXP-FRONTIER-015":
            errors.append("manifest experiment_id must be EXP-FRONTIER-015")
        if manifest.get("status") != EXPECTED_STATUS:
            errors.append(f"manifest status must be {EXPECTED_STATUS}")
        if manifest.get("decision") != EXPECTED_DECISION:
            errors.append(f"manifest decision must be {EXPECTED_DECISION}")
        if manifest.get("claim_ceiling") != EXPECTED_CLAIM_CEILING:
            errors.append(f"manifest claim_ceiling must be {EXPECTED_CLAIM_CEILING}")
        if manifest.get("paper_count_target") != 100:
            errors.append("manifest paper_count_target must be 100")
        if manifest.get("seed_count") != 100:
            errors.append("manifest seed_count must be 100")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")

        for field in [
            "dependencies_installed",
            "papers_generated",
            "manuscripts_generated",
            "publication_pdf_generated",
            "private_data_downloaded",
            "human_review_completed",
            "rights_or_authority_cleared",
            "public_release_claimed",
        ]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")

        local_context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_LOCAL_CONTEXT - local_context)
        if missing_context:
            errors.append(f"manifest missing local_context: {missing_context}")
        for rel_path in local_context:
            if not (ROOT / rel_path).exists():
                errors.append(f"manifest local_context path does not exist: {rel_path}")

        blocked_promotions = set(manifest.get("blocked_promotions", []))
        for blocked in [
            "paper maturity claim",
            "external submission",
            "publication package",
            "rights or authority clearance claim",
            "derived layer source promotion",
            "frontier novelty claim",
        ]:
            if blocked not in blocked_promotions:
                errors.append(f"manifest missing blocked promotion: {blocked}")

        schema = read_json(SCHEMA_PATH)
        if schema.get("schema_id") != "HUNDRED-PAPER-RECOVERY-SEED-SCHEMA-001":
            errors.append("schema_id must be HUNDRED-PAPER-RECOVERY-SEED-SCHEMA-001")
        if set(schema.get("required", [])) != REQUIRED_SEED_FIELDS:
            errors.append("schema required fields must exactly match seed fields")
        if schema.get("additionalProperties") is not False:
            errors.append("schema additionalProperties must be false")
        layer_enum = set(schema.get("properties", {}).get("evidence_layer", {}).get("enum", []))
        if layer_enum != REQUIRED_EVIDENCE_LAYERS:
            errors.append("schema evidence_layer enum must match lab evidence layers")

        rows = read_csv(SEEDS_CSV)
        if len(rows) != 100:
            errors.append(f"research_seeds.csv must contain exactly 100 rows, found {len(rows)}")
        if rows and set(rows[0].keys()) != REQUIRED_SEED_FIELDS:
            errors.append("research_seeds.csv header must exactly match required seed fields")
        seed_ids = [row.get("seed_id", "") for row in rows]
        if len(seed_ids) != len(set(seed_ids)):
            errors.append("research seed ids must be unique")
        if any(not re.fullmatch(r"NWR-\d{3}", seed_id) for seed_id in seed_ids):
            errors.append("research seed ids must use NWR-### format")

        lane_ids = {row.get("lane_id", "") for row in rows}
        missing_lanes = sorted(REQUIRED_LANE_IDS - lane_ids, key=int)
        if missing_lanes:
            errors.append(f"research seeds missing lane ids: {missing_lanes}")
        opportunity_ids = {row.get("opportunity_id", "") for row in rows}
        missing_opportunities = sorted(REQUIRED_OPPORTUNITY_IDS - opportunity_ids)
        if missing_opportunities:
            errors.append(f"research seeds missing opportunity ids: {missing_opportunities}")
        evidence_layers = {row.get("evidence_layer", "") for row in rows}
        missing_layers = sorted(REQUIRED_EVIDENCE_LAYERS - evidence_layers)
        if missing_layers:
            errors.append(f"research seeds missing evidence layers: {missing_layers}")

        for index, row in enumerate(rows, start=2):
            for field in REQUIRED_SEED_FIELDS:
                if not row.get(field):
                    errors.append(f"research_seeds.csv line {index} missing {field}")
            if row.get("status") != SEED_STATUS:
                errors.append(f"research_seeds.csv line {index} status must be {SEED_STATUS}")
            if row.get("claim_ceiling") != SEED_CLAIM_CEILING:
                errors.append(f"research_seeds.csv line {index} claim_ceiling must be {SEED_CLAIM_CEILING}")
            if row.get("evidence_layer") not in REQUIRED_EVIDENCE_LAYERS:
                errors.append(f"research_seeds.csv line {index} has invalid evidence_layer")
            if row.get("lane_id") not in REQUIRED_LANE_IDS:
                errors.append(f"research_seeds.csv line {index} has invalid lane_id")
            if row.get("opportunity_id") not in REQUIRED_OPPORTUNITY_IDS:
                errors.append(f"research_seeds.csv line {index} has invalid opportunity_id")

        gate_rows = read_csv(CLAIM_GATES_CSV)
        if len(gate_rows) < 6:
            errors.append("claim_gate_matrix.csv must contain at least six gate rows")
        gate_layers = {row.get("evidence_layer", "") for row in gate_rows}
        missing_gate_layers = sorted(REQUIRED_EVIDENCE_LAYERS - gate_layers)
        if missing_gate_layers:
            errors.append(f"claim_gate_matrix.csv missing layers: {missing_gate_layers}")
        for index, row in enumerate(gate_rows, start=2):
            if row.get("promotion_allowed") != "no":
                errors.append(f"claim_gate_matrix.csv line {index} promotion_allowed must be no")
            if not row.get("required_before_promotion"):
                errors.append(f"claim_gate_matrix.csv line {index} missing required_before_promotion")

        sprint_selection = read_json(SPRINT_SELECTION_PATH)
        if sprint_selection.get("selection_status") != "seed_selection_only_not_execution":
            errors.append("sprint selection must remain seed_selection_only_not_execution")
        selected = sprint_selection.get("selected_seed_ids", [])
        if len(selected) != 12:
            errors.append("sprint selection must choose exactly 12 seed ids for the next pass")
        unknown_selected = sorted(set(selected) - set(seed_ids))
        if unknown_selected:
            errors.append(f"sprint selection contains unknown seed ids: {unknown_selected}")
        if sprint_selection.get("external_actions_taken") != []:
            errors.append("sprint selection external_actions_taken must be empty")

        markdown = INTAKE_MD.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase.lower() not in markdown:
                errors.append(f"intake markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden recovery-intake text: {forbidden}")

    if errors:
        print("HUNDRED_PAPER_RECOVERY_INTAKE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("HUNDRED_PAPER_RECOVERY_INTAKE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
