from __future__ import annotations

import csv
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"

SEVERITY_WEIGHT = {
    "none": 0.0,
    "minor": 1.0,
    "material": 2.0,
    "blocking": 3.0,
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def boolish(value: str) -> bool | None:
    lower = (value or "").strip().lower()
    if lower in {"yes", "true", "1", "promotion", "lpe"}:
        return True
    if lower in {"no", "false", "0", "none"}:
        return False
    return None


def wilson(successes: int, n: int, z: float = 1.96) -> dict[str, float]:
    if n == 0:
        return {"low": 0.0, "high": 0.0}
    p = successes / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denom
    return {"low": round(max(0.0, center - margin), 4), "high": round(min(1.0, center + margin), 4)}


def metric_rows(gold: dict[str, dict[str, str]], preds: list[dict[str, str]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in preds:
        grouped.setdefault((row.get("condition", ""), row.get("agent_id", "")), []).append(row)

    out = []
    for (condition, agent_id), rows in grouped.items():
        tp = fp = fn = tn = 0
        weighted_total = weighted_hit = 0.0
        source_false_assertions = 0
        derived_cases = derived_preserved = 0
        for row in rows:
            case_id = row.get("case_id", "")
            if case_id not in gold:
                continue
            gold_row = gold[case_id]
            gold_lpe = boolish(gold_row.get("promotion_error", ""))
            pred_lpe = boolish(row.get("predicted_promotion_error", ""))
            if gold_lpe is None or pred_lpe is None:
                continue
            if gold_lpe and pred_lpe:
                tp += 1
            elif not gold_lpe and pred_lpe:
                fp += 1
            elif gold_lpe and not pred_lpe:
                fn += 1
            else:
                tn += 1
            if gold_lpe:
                weight = SEVERITY_WEIGHT.get((gold_row.get("severity") or "none").lower(), 0.0)
                weighted_total += weight
                if pred_lpe:
                    weighted_hit += weight
            if row.get("predicted_output_layer") == "source_observed" and gold_row.get("output_layer") != "source_observed":
                source_false_assertions += 1
            if gold_row.get("input_layer") == "derived" or "27/216" in gold_row.get("claim_text", ""):
                derived_cases += 1
                if row.get("predicted_input_layer") == "derived" or row.get("predicted_output_layer") == "derived":
                    derived_preserved += 1
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        specificity = tn / (tn + fp) if tn + fp else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        denom = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        mcc = ((tp * tn) - (fp * fn)) / denom if denom else 0.0
        n = tp + fp + fn + tn
        out.append(
            {
                "condition": condition,
                "agent_id": agent_id,
                "n_scored": n,
                "tp": tp,
                "fp": fp,
                "fn": fn,
                "tn": tn,
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1": round(f1, 4),
                "mcc": round(mcc, 4),
                "balanced_accuracy": round((recall + specificity) / 2, 4),
                "severity_weighted_recall": round(weighted_hit / weighted_total, 4) if weighted_total else 0.0,
                "lpe_rate_ci": wilson(tp + fn, n),
                "source_observed_false_assertion_rate": round(source_false_assertions / n, 4) if n else 0.0,
                "derived_layer_preservation_rate": round(derived_preserved / derived_cases, 4) if derived_cases else None,
            }
        )
    return out


def main() -> int:
    gold_path = EXP5 / "gold_labels.csv"
    agent_dir = EXP5 / "agent_runs"
    if not gold_path.exists() or not agent_dir.exists():
        status = {
            "experiment_id": "EXP-FRONTIER-005",
            "generated_at": now(),
            "status": "NOT_SCORED_MISSING_GOLD_OR_AGENT_RUNS",
            "gold_labels_present": gold_path.exists(),
            "agent_runs_present": agent_dir.exists(),
            "frontier_claim_status": "not_ready",
        }
        write_json(EXP5 / "scores.json", status)
        write_text(
            EXP5 / "analysis.md",
            """
# EXP-FRONTIER-005 Analysis

Status: `NOT_SCORED_MISSING_GOLD_OR_AGENT_RUNS`

The experiment cannot be scored yet. Independent adjudicated `gold_labels.csv`
and at least one file under `agent_runs/` are required.
""",
        )
        print(status["status"])
        return 0

    gold_rows = read_csv(gold_path)
    gold = {row["case_id"]: row for row in gold_rows}
    pred_rows: list[dict[str, str]] = []
    for path in agent_dir.glob("*.csv"):
        pred_rows.extend(read_csv(path))
    metrics = metric_rows(gold, pred_rows)
    leaderboard = sorted(metrics, key=lambda row: (row["f1"], row["mcc"], row["precision"]), reverse=True)
    best_overall = leaderboard[0] if leaderboard else {}
    best_codex = next((row for row in leaderboard if row["agent_id"].startswith("codex_")), {})
    status = {
        "experiment_id": "EXP-FRONTIER-005",
        "generated_at": now(),
        "status": "SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM",
        "gold_label_count": len(gold_rows),
        "agent_prediction_count": len(pred_rows),
        "metric_rows": metrics,
        "best_overall": best_overall,
        "best_codex_agent": best_codex,
        "frontier_claim_status": "not_ready",
        "remaining_gate": "Review-team approval and rights/authority review are required before any frontier-paper claim.",
    }
    write_json(EXP5 / "scores.json", status)
    write_json(EXP5 / "confidence_intervals.json", {"metric_rows": metrics})
    write_csv(EXP5 / "scoreboard.csv", leaderboard)
    lines = [
        "# EXP-FRONTIER-005 Scoreboard",
        "",
        "Status: `SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM`",
        "",
        "| Rank | Condition | Agent | F1 | MCC | Precision | Recall | FP | FN | Derived Preservation |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for index, row in enumerate(leaderboard, start=1):
        lines.append(
            f"| {index} | `{row['condition']}` | `{row['agent_id']}` | {row['f1']} | {row['mcc']} | {row['precision']} | {row['recall']} | {row['fp']} | {row['fn']} | {row['derived_layer_preservation_rate']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This is an internal benchmark result against AI-reviewer adjudicated labels.",
            "It is not a frontier claim because human/domain gold labels, external frontier model runs, and rights/authority review remain incomplete.",
        ]
    )
    write_text(EXP5 / "scoreboard.md", "\n".join(lines))
    write_text(
        EXP5 / "analysis.md",
        f"""
# EXP-FRONTIER-005 Analysis

Status: `SCORED_NOT_VALIDATED_FOR_FRONTIER_CLAIM`

- Gold labels: `{len(gold_rows)}`
- Agent predictions: `{len(pred_rows)}`
- Metric rows: `{len(metrics)}`
- Best overall: `{best_overall.get('agent_id')}` in `{best_overall.get('condition')}` with F1 `{best_overall.get('f1')}` and MCC `{best_overall.get('mcc')}`
- Best Codex-agent run: `{best_codex.get('agent_id')}` in `{best_codex.get('condition')}` with F1 `{best_codex.get('f1')}` and MCC `{best_codex.get('mcc')}`

This score file is not by itself a frontier result. It becomes paper evidence
only after label provenance, inter-annotator agreement, rights/authority review,
and review-team trace are complete.
""",
    )
    print("LPE_EXP005_SCORED")
    print(f"gold={len(gold_rows)}")
    print(f"predictions={len(pred_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
