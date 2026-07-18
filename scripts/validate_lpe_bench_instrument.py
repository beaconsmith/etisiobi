from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTRUMENT = ROOT / "instruments" / "lpe_bench"
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def csv_count(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def main() -> int:
    errors: list[str] = []
    required = [
        INSTRUMENT / "manifest.json",
        INSTRUMENT / "README.md",
        INSTRUMENT / "VALIDATION.md",
        INSTRUMENT / "BENCHMARK_CARD.md",
        INSTRUMENT / "NEXT_EXPERIMENT.md",
        INSTRUMENT / "leaderboard_internal.csv",
        INSTRUMENT / "leaderboard_internal.json",
        INSTRUMENT / "data_summary.json",
        INSTRUMENT / "demo.html",
        EXP5 / "plan.md",
        EXP5 / "manifest.json",
        EXP5 / "README.md",
        EXP5 / "ANNOTATION_PROTOCOL.md",
        EXP5 / "AGENT_RUN_PROTOCOL.md",
        EXP5 / "frozen_annotation_queue.csv",
        EXP5 / "gold_labels_template.csv",
        EXP5 / "annotation_agreement.json",
        EXP5 / "adjudication_report.md",
        EXP5 / "agent_prompts" / "manifest.json",
        EXP5 / "agent_runs" / "manifest.json",
        EXP5 / "scoreboard.csv",
        EXP5 / "scoreboard.md",
        EXP5 / "annotation_inputs" / "domain_source_reviewer.csv",
        EXP5 / "annotation_inputs" / "methods_reviewer.csv",
        EXP5 / "annotation_inputs" / "adversarial_impact_reviewer.csv",
        EXP5 / "agent_run_templates" / "C0_no_layer_labels.csv",
        EXP5 / "agent_run_templates" / "C1_layer_labels.csv",
        EXP5 / "agent_run_templates" / "C2_claim_gate.csv",
        EXP5 / "agent_run_templates" / "C3_adversarial_review.csv",
        EXP5 / "scores.json",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        manifest = read_json(INSTRUMENT / "manifest.json")
        exp5_manifest = read_json(EXP5 / "manifest.json")
        scores = read_json(EXP5 / "scores.json")
        if manifest.get("instrument_id") != "LPE-Bench":
            errors.append("LPE-Bench manifest must identify the instrument")
        if manifest.get("status") != "PUBLIC_INSTRUMENT_DRAFT_NOT_FRONTIER_PROOF":
            errors.append("LPE-Bench must remain not-frontier-proof until EXP-005 gates pass")
        if exp5_manifest.get("status") != "ANNOTATION_AND_AGENT_RUN_TEMPLATES_READY_NOT_SCORED":
            errors.append("EXP-005 manifest must say templates are ready but not scored")
        if exp5_manifest.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-005 must not claim frontier readiness")
        if scores.get("status") not in {"NOT_SCORED_MISSING_GOLD_OR_AGENT_RUNS", "SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM"}:
            errors.append("EXP-005 score status is invalid")
        if scores.get("frontier_claim_status") != "not_ready":
            errors.append("EXP-005 scores must not claim frontier readiness")
        queue_count = csv_count(EXP5 / "frozen_annotation_queue.csv")
        if queue_count != exp5_manifest.get("case_count"):
            errors.append("EXP-005 frozen queue count must match manifest")
        for role in exp5_manifest.get("annotation_roles", []):
            path = EXP5 / "annotation_inputs" / f"{role}.csv"
            if path.exists() and csv_count(path) != queue_count:
                errors.append(f"annotation template count mismatch for {role}")
        for condition in exp5_manifest.get("agent_conditions", []):
            path = EXP5 / "agent_run_templates" / f"{condition}.csv"
            if path.exists() and csv_count(path) != queue_count:
                errors.append(f"agent template count mismatch for {condition}")

    if errors:
        print("LPE_BENCH_INSTRUMENT_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1
    print("LPE_BENCH_INSTRUMENT_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
