from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


GOAL_IDS = [f"GOAL-{idx:03d}" for idx in range(1, 11)]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def check(name: str, passed: bool, evidence: str, failures: list[str]) -> None:
    if not passed:
        failures.append(f"{name}: {evidence}")


def main() -> int:
    failures: list[str] = []

    bmc = read_jsonl(ROOT / "corpus" / "base_modifier_cache.jsonl")
    check("GOAL-001 BMC has 208 records", len(bmc) == 208, "corpus/base_modifier_cache.jsonl", failures)
    required_bmc = {"bmc_id", "base_id", "modifier_id", "row_label", "vowel_label", "cell_id", "tei_locator", "iiif_canvas", "certainty", "provenance_activity", "kg_node", "claim_dependencies", "status"}
    check("GOAL-001 BMC records have required schema fields", all(required_bmc <= set(row) for row in bmc), "corpus/base_modifier_cache.jsonl", failures)

    count = read_json(ROOT / "corpus" / "bmc_count_reconciliation.json")
    check("GOAL-002 count decision is multi-layer valid", count.get("decision") == "MULTI_LAYER_COUNT_VALID", "corpus/bmc_count_reconciliation.json", failures)
    check("GOAL-002 counts reconcile 26x8=208", count["checks"]["bmc_rows"] == 26 and count["checks"]["bmc_vowels"] == 8 and count["checks"]["bmc_cells"] == 208, "corpus/bmc_count_reconciliation.json", failures)

    gate = read_jsonl(ROOT / "corpus" / "bmc_claim_gate.jsonl")
    statuses = {row["status"] for row in gate}
    check("GOAL-003 claim gate includes ready and blocking statuses", {"READY", "REWRITE_AS_LIMITATION", "REMOVE"} <= statuses, "corpus/bmc_claim_gate.jsonl", failures)

    grammar = read_json(ROOT / "corpus" / "bmc_induced_grammar.json")
    grammar_result = read_json(ROOT / "experiments" / "EXP-BMC-004" / "results.json")
    check("GOAL-004 grammar is partial structural grammar", grammar.get("status") == "partial_structural_grammar" and grammar_result["row_vowel_reading_coverage"] == 1.0, "corpus/bmc_induced_grammar.json", failures)

    mdl = read_json(ROOT / "corpus" / "bmc_compression_mdl.json")
    check("GOAL-005 compression result is scoped", mdl["decision"] == "COMPRESSION_POSITIVE_FOR_ROW_VOWEL_INDEX_ONLY", "corpus/bmc_compression_mdl.json", failures)
    check("GOAL-005 row-vowel table is shorter than flat list", mdl["row_vowel_vs_flat_ratio"] < 1.0, "corpus/bmc_compression_mdl.json", failures)

    certainty = read_jsonl(ROOT / "corpus" / "bmc_certainty_propagation.jsonl")
    check("GOAL-006 certainty covers every BMC record", len(certainty) == len(bmc), "corpus/bmc_certainty_propagation.jsonl", failures)

    kg = read_json(ROOT / "knowledge_graph" / "bmc_kg.jsonld")
    bmc_nodes = [node for node in kg["@graph"] if node.get("@type") == "BMCObject"]
    check("GOAL-007 KG has every BMC object", len(bmc_nodes) == len(bmc), "knowledge_graph/bmc_kg.jsonld", failures)

    benchmarks = read_jsonl(ROOT / "benchmarks" / "bmc_benchmark_tasks.jsonl")
    check("GOAL-008 defines 10 benchmark tasks", len(benchmarks) == 10, "benchmarks/bmc_benchmark_tasks.jsonl", failures)

    review = read_jsonl(ROOT / "authority" / "bmc_review_states.jsonl")
    check("GOAL-009 authority review covers every BMC record", len(review) == len(bmc), "authority/bmc_review_states.jsonl", failures)
    check("GOAL-009 public release remains blocked by default", all(row["publication_state"] == "publication_blocked" for row in review), "authority/bmc_review_states.jsonl", failures)

    hyperloop = read_json(ROOT / "corpus" / "bmc_hyperloop_result.json")
    check("GOAL-010 hyperloop has no-submission decision", hyperloop["decision"] == "NO_BMC_ARXIV_SUBMISSION_YET", "corpus/bmc_hyperloop_result.json", failures)

    completion = read_json(ROOT / "research_goals" / "bmc" / "completion_audit.json")
    completed = {row["goal_id"] for row in completion["goals"] if row["status"] == "completed"}
    check("Completion audit records all 10 goals complete", completed == set(GOAL_IDS), "research_goals/bmc/completion_audit.json", failures)

    for goal_id in GOAL_IDS:
        exp = ROOT / "experiments" / f"EXP-BMC-{goal_id.split('-')[1]}"
        check(f"{goal_id} experiment has plan/results/analysis/decision", all((exp / name).exists() for name in ["plan.md", "results.json", "analysis.md", "decision.md"]), str(exp), failures)

    if failures:
        print(f"BMC GOAL VALIDATION FAIL: {len(failures)} failing checks")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("BMC GOAL VALIDATION PASS: all 10 goals complete with repo-local experiment artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
