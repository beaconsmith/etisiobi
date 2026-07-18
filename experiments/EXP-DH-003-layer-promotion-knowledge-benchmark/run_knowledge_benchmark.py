import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXP_DIR = ROOT / "experiments" / "EXP-DH-003-layer-promotion-knowledge-benchmark"
DATA_PATH = EXP_DIR / "data" / "knowledge_units.csv"
RESULTS_PATH = EXP_DIR / "results.json"

LPE2_RESULTS = ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded" / "results.json"
LPE2_CASES = ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded" / "data" / "lpe_cases.jsonl"
QUALITY_RESULTS = ROOT / "experiments" / "EXP-FRONTIER-017-lpe-label-quality-gate" / "pilot_results.json"
PROOF_RESULTS = ROOT / "experiments" / "EXP-APP-003-layer-safety-proof" / "verification_report.json"
DH001_GATE = ROOT / "experiments" / "EXP-DH-001-derived-completion-baseline" / "global_benchmark_gate_results.json"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_units():
    with DATA_PATH.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def evaluate_required_signal(signal, metrics):
    if signal == "collision_count>=200":
        return metrics["collision_count"] >= 200
    if signal == "rank_only_metadata_test_f1==1.0":
        return metrics["rank_only_metadata_test_f1"] == 1.0
    if signal == "lexical_only_test_f1<0.9":
        return metrics["lexical_only_test_f1"] < 0.9
    if signal == "hard_positive_no_trigger_count>=50":
        return metrics["variant_counts"].get("hard_positive_no_trigger", 0) >= 50
    if signal == "hard_negative_trigger_words_count>=40":
        return metrics["variant_counts"].get("hard_negative_trigger_words", 0) >= 40
    if signal == "source_index_cases_present":
        return metrics["source_index_cases"] > 0
    if signal == "derived_to_derived_negatives_present":
        return metrics["derived_to_derived_negatives"] > 0 and metrics["dh001_global_claim"] == "not_met"
    if signal == "blocked_public_release_count>=8":
        return metrics["blocked_public_release_count"] >= 8
    if signal == "needs_adjudication_count>=5":
        return metrics["needs_adjudication_count"] >= 5
    if signal == "paper_claim_status==not_ready":
        return metrics["paper_claim_status"] == "not_ready"
    raise ValueError(f"Unknown required signal: {signal}")


def main():
    lpe2 = load_json(LPE2_RESULTS)
    proof = load_json(PROOF_RESULTS)
    quality = load_json(QUALITY_RESULTS)
    dh001 = load_json(DH001_GATE)
    cases = load_jsonl(LPE2_CASES)
    units = load_units()

    proof_checks = proof["proof_checks"]
    metrics = {
        "source_case_count": lpe2["case_count"],
        "variant_counts": lpe2["variant_type_counts"],
        "rank_only_metadata_test_f1": lpe2["best_test_baseline"]["f1"],
        "lexical_only_test_f1": lpe2["best_metadata_free_test_baseline"]["f1"],
        "collision_count": proof_checks["unqualified_collision_count"],
        "qualified_unique_count": proof_checks["qualified_unique_count"],
        "quality_gate_sample_count": quality["sample_case_count"],
        "blocked_public_release_count": quality["blocked_public_release_count"],
        "needs_adjudication_count": quality["needs_adjudication_count"],
        "paper_claim_status": quality["paper_claim_status"],
        "dh001_global_claim": dh001["global_benchmark_claim"],
        "source_index_cases": sum(1 for row in cases if row["input_layer"] == "source_index"),
        "derived_to_derived_negatives": sum(
            1
            for row in cases
            if row["input_layer"] == "derived"
            and row["output_layer"] == "derived"
            and not row["gold_promotion_error"]
        ),
    }

    evaluations = []
    failed_units = []
    for unit in units:
        passed = evaluate_required_signal(unit["required_signal"], metrics)
        evaluations.append(
            {
                "unit_id": unit["unit_id"],
                "title": unit["title"],
                "benchmark_dimension": unit["benchmark_dimension"],
                "knowledge_type": unit["knowledge_type"],
                "claim_ceiling": unit["claim_ceiling"],
                "required_signal": unit["required_signal"],
                "status": "PASS" if passed else "FAIL",
            }
        )
        if not passed:
            failed_units.append(unit["unit_id"])

    status = (
        "SIGNIFICANT_INTERNAL_KNOWLEDGE_BREAKTHROUGH_DH003"
        if len(units) == 10 and not failed_units
        else "DH003_KNOWLEDGE_GATE_NOT_READY"
    )

    result = {
        "experiment_id": "EXP-DH-003-layer-promotion-knowledge-benchmark",
        "hypothesis_id": "DH-003",
        "status": status,
        "knowledge_unit_count": len(units),
        "passed_units": len(units) - len(failed_units),
        "failed_units": failed_units,
        "source_case_count": metrics["source_case_count"],
        "collision_count": metrics["collision_count"],
        "quality_gate_sample_count": metrics["quality_gate_sample_count"],
        "rank_only_metadata_test_f1": metrics["rank_only_metadata_test_f1"],
        "lexical_only_test_f1": metrics["lexical_only_test_f1"],
        "global_benchmark_claim": "not_met",
        "novelty_scope": "internal_repo_knowledge",
        "paper_claim_status": "not_ready",
        "public_release_status": "blocked",
        "celebration_worthy": status == "SIGNIFICANT_INTERNAL_KNOWLEDGE_BREAKTHROUGH_DH003",
        "claim_ceiling": "Ten internal knowledge units for DH-003 benchmark design; not a global novelty, paper, public benchmark, or submission-readiness claim.",
        "evaluations": evaluations,
        "next_action": "Expand EXP-FRONTIER-017 quality routing from 24 pilot labels to the full label set, then run blind review before any paper-candidate decision.",
    }

    RESULTS_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
