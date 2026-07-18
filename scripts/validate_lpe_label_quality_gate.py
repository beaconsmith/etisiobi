from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate"
MANIFEST_PATH = EXP_DIR / "manifest.json"
CARD_PATH = EXP_DIR / "LPE_LABEL_QUALITY_GATE.md"
SCHEMA_PATH = EXP_DIR / "label_quality_gate_schema.json"
MATRIX_PATH = EXP_DIR / "quality_gate_matrix.csv"
SAMPLE_PATH = EXP_DIR / "pilot_sample.csv"
RESULTS_PATH = EXP_DIR / "pilot_results.json"
FAILURES_PATH = EXP_DIR / "failure_cases.md"
PATHWAY_PATH = EXP_DIR / "paper_pathway.md"

REQUIRED_FILES = [
    MANIFEST_PATH,
    CARD_PATH,
    SCHEMA_PATH,
    MATRIX_PATH,
    SAMPLE_PATH,
    RESULTS_PATH,
    FAILURES_PATH,
    PATHWAY_PATH,
]

REQUIRED_CONTEXT = {
    "experiments/EXP-FRONTIER-016-selected-seed-artifact-sprint/artifacts/NWR-049-lpe-label-quality-audit.md",
    "experiments/EXP-FRONTIER-005-real-agent-lpe-eval/gold_labels.csv",
    "experiments/EXP-FRONTIER-005-real-agent-lpe-eval/scores.json",
    "experiments/EXP-FRONTIER-005-real-agent-lpe-eval/annotation_agreement.json",
    "instruments/lpe_bench/manifest.json",
}

REQUIRED_SAMPLE_FIELDS = {
    "case_id",
    "input_layer",
    "output_layer",
    "promotion_error",
    "severity",
    "source_review_status",
    "public_release_ok",
    "evidence_anchor_check",
    "layer_contrast_check",
    "disagreement_state_check",
    "adjudication_need_check",
    "quality_gate_status",
}

REQUIRED_MATRIX_CHECKS = {
    "evidence_anchor_check",
    "layer_contrast_check",
    "disagreement_state_check",
    "adjudication_need_check",
}

FORBIDDEN_TEXT = [
    "paper-ready",
    "submission-ready",
    "ready_for_human_arxiv_review",
    "public_release_ready",
    "frontier proof",
    "novelty clearance",
    "rights cleared",
    "authority approved",
    "source-observed 27/216",
    "accepted paper",
    "ready for external submission",
    "arxiv-ready",
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
        if manifest.get("experiment_id") != "EXP-FRONTIER-017":
            errors.append("manifest experiment_id must be EXP-FRONTIER-017")
        if manifest.get("source_seed_id") != "NWR-049":
            errors.append("manifest source_seed_id must be NWR-049")
        if manifest.get("status") != "LPE_LABEL_QUALITY_GATE_PILOT_INTERNAL_NOT_FRONTIER_RESULT":
            errors.append("manifest status must keep pilot internal and not frontier result")
        if manifest.get("decision") != "promote_nwr_049_into_branch_specific_quality_gate_pilot":
            errors.append("manifest decision must promote NWR-049 into quality gate pilot")
        if manifest.get("claim_ceiling") != "quality_gate_pilot_not_paper_result":
            errors.append("manifest claim ceiling must be quality_gate_pilot_not_paper_result")
        if manifest.get("sample_case_count") != 24:
            errors.append("manifest sample_case_count must be 24")
        if manifest.get("source_gold_label_count") != 360:
            errors.append("manifest source_gold_label_count must be 360")
        if manifest.get("external_actions_taken") != []:
            errors.append("external_actions_taken must be empty")
        for field in [
            "dependencies_installed",
            "model_or_api_run",
            "new_agent_run",
            "human_domain_review_completed",
            "rights_or_authority_cleared",
            "publication_pdf_generated",
            "external_submission_made",
            "public_release_claimed",
        ]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")

        context = set(manifest.get("local_context", []))
        missing_context = sorted(REQUIRED_CONTEXT - context)
        if missing_context:
            errors.append(f"manifest missing context paths: {missing_context}")
        for rel_path in context:
            if not (ROOT / rel_path).exists():
                errors.append(f"context path does not exist: {rel_path}")

        schema = read_json(SCHEMA_PATH)
        if schema.get("schema_id") != "LPE-LABEL-QUALITY-GATE-SCHEMA-001":
            errors.append("schema_id must be LPE-LABEL-QUALITY-GATE-SCHEMA-001")
        if schema.get("claim_ceiling") != "quality_gate_pilot_not_paper_result":
            errors.append("schema claim ceiling must match pilot claim ceiling")
        if set(schema.get("required", [])) != REQUIRED_SAMPLE_FIELDS:
            errors.append("schema required fields must match sample fields")
        if schema.get("additionalProperties") is not False:
            errors.append("schema additionalProperties must be false")

        matrix_rows = read_csv(MATRIX_PATH)
        check_ids = {row.get("check_id") for row in matrix_rows}
        missing_checks = sorted(REQUIRED_MATRIX_CHECKS - check_ids)
        if missing_checks:
            errors.append(f"quality gate matrix missing checks: {missing_checks}")
        for row in matrix_rows:
            if row.get("current_status") != "active_internal_pilot":
                errors.append(f"{row.get('check_id')}: current_status must be active_internal_pilot")
            if row.get("paper_promotion_allowed") != "no":
                errors.append(f"{row.get('check_id')}: paper_promotion_allowed must be no")

        sample_rows = read_csv(SAMPLE_PATH)
        if len(sample_rows) != 24:
            errors.append(f"pilot_sample.csv must contain 24 rows, found {len(sample_rows)}")
        if sample_rows and set(sample_rows[0].keys()) != REQUIRED_SAMPLE_FIELDS:
            errors.append("pilot_sample.csv header must match required fields")
        statuses = {row.get("quality_gate_status") for row in sample_rows}
        if "review_ready_internal" not in statuses:
            errors.append("pilot sample must include at least one review_ready_internal row")
        if "needs_adjudication" not in statuses:
            errors.append("pilot sample must include at least one needs_adjudication row")
        if "blocked_public_release" not in statuses:
            errors.append("pilot sample must include at least one blocked_public_release row")
        for row in sample_rows:
            for field in REQUIRED_SAMPLE_FIELDS:
                if not row.get(field):
                    errors.append(f"{row.get('case_id', 'unknown')}: missing {field}")
            if row.get("public_release_ok") == "ok":
                errors.append(f"{row.get('case_id')}: public_release_ok must not be ok in internal pilot")

        results = read_json(RESULTS_PATH)
        if results.get("status") != "QUALITY_GATE_PILOT_COMPLETE_INTERNAL_NOT_FRONTIER_RESULT":
            errors.append("pilot results status must remain internal and not frontier result")
        if results.get("claim_ceiling") != "quality_gate_pilot_not_paper_result":
            errors.append("pilot results claim ceiling must match")
        if results.get("sample_case_count") != 24:
            errors.append("pilot results sample_case_count must be 24")
        if results.get("source_gold_label_count") != 360:
            errors.append("pilot results source_gold_label_count must be 360")
        if results.get("paper_claim_status") != "not_ready":
            errors.append("paper_claim_status must remain not_ready")
        if results.get("frontier_claim_status") != "not_ready":
            errors.append("frontier_claim_status must remain not_ready")
        if results.get("review_ready_internal_count", 0) <= 0:
            errors.append("pilot must report review_ready_internal_count > 0")
        if results.get("needs_adjudication_count", 0) <= 0:
            errors.append("pilot must report needs_adjudication_count > 0")
        if results.get("blocked_public_release_count", 0) <= 0:
            errors.append("pilot must report blocked_public_release_count > 0")

        for path in [CARD_PATH, FAILURES_PATH, PATHWAY_PATH]:
            lower = path.read_text(encoding="utf-8").lower()
            for phrase in [
                "lpe label quality gate",
                "quality_gate_pilot_not_paper_result",
                "what this teaches oroma",
                "next action",
            ]:
                if phrase not in lower:
                    errors.append(f"{path.name} missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden LPE quality gate text: {forbidden}")

    if errors:
        print("LPE_LABEL_QUALITY_GATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("LPE_LABEL_QUALITY_GATE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
