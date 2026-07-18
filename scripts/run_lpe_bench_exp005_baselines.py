from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"
OUT = EXP5 / "agent_runs"


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def layer_guess(text: str, condition: str) -> tuple[str, str, str, float]:
    lower = text.lower()
    strong_claim = any(
        token in lower
        for token in [
            "proves",
            "source-observed",
            "submission-ready",
            "submittable",
            "public release",
            "rights clearance",
            "universal compression",
            "e6",
            "216",
            "27",
            "final",
        ]
    )
    weak_marker = any(
        token in lower
        for token in [
            "derived",
            "hypothesis",
            "speculative",
            "blocked",
            "not ready",
            "requires",
            "pending",
            "must not",
            "cannot",
            "needs",
        ]
    )
    if "27/216" in lower or "216" in lower or "f/v" in lower:
        input_layer = "derived"
    elif any(token in lower for token in ["rights", "authority", "public release", "blocked"]):
        input_layer = "blocked"
    elif any(token in lower for token in ["hypothesis", "speculative", "e6", "universal compression"]):
        input_layer = "speculative"
    elif any(token in lower for token in ["design", "application", "system", "benchmark"]):
        input_layer = "design_hypothesis"
    elif any(token in lower for token in ["26", "208", "source", "transcription", "ledger"]):
        input_layer = "source_index"
    else:
        input_layer = "design_hypothesis"

    if condition == "C0_no_layer_labels":
        predicted = strong_claim and not weak_marker
    elif condition == "C1_layer_labels":
        predicted = strong_claim and input_layer in {"derived", "speculative", "blocked", "design_hypothesis"}
    elif condition == "C2_claim_gate":
        predicted = (strong_claim and input_layer != "source_observed") or ("source-observed" in lower and input_layer != "source_observed")
    else:
        predicted = (strong_claim or "ready" in lower or "proves" in lower) and input_layer != "source_observed"

    if predicted:
        output_layer = "source_observed"
        confidence = 0.82 if condition != "C0_no_layer_labels" else 0.64
    else:
        output_layer = input_layer
        confidence = 0.72 if weak_marker else 0.58
    return ("yes" if predicted else "no", input_layer, output_layer, confidence)


def run_condition(condition: str, rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        pred, input_layer, output_layer, confidence = layer_guess(row["claim_text"], condition)
        out.append(
            {
                "case_id": row["case_id"],
                "condition": condition,
                "agent_id": f"baseline_{condition}",
                "input_claim_text": row["claim_text"],
                "output_claim_text": row["claim_text"],
                "predicted_promotion_error": pred,
                "predicted_input_layer": input_layer,
                "predicted_output_layer": output_layer,
                "confidence": confidence,
                "source_ids_used": row["source_path"],
                "raw_output_path": "",
            }
        )
    return out


def main() -> int:
    queue = read_csv(EXP5 / "frozen_annotation_queue.csv")
    conditions = ["C0_no_layer_labels", "C1_layer_labels", "C2_claim_gate", "C3_adversarial_review"]
    counts = {}
    for condition in conditions:
        rows = run_condition(condition, queue)
        write_csv(OUT / f"{condition}.csv", rows)
        counts[condition] = len(rows)
    manifest = {
        "experiment_id": "EXP-FRONTIER-005",
        "generated_at": now(),
        "status": "BASELINE_AGENT_RUNS_CREATED",
        "agent_run_type": "deterministic_local_baselines_not_frontier_models",
        "counts": counts,
        "frontier_claim_status": "not_ready",
    }
    write_json(OUT / "manifest.json", manifest)
    print("LPE_EXP005_BASELINE_AGENT_RUNS_CREATED")
    print(f"conditions={len(conditions)}")
    print(f"rows_per_condition={len(queue)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
