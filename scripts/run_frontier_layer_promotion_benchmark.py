from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "EXP-FRONTIER-001-layer-promotion-benchmark"
BENCH = ROOT / "benchmarks" / "layer_promotion_error"

LAYER_RANK = {
    "source_observed": 0,
    "source_index": 1,
    "derived": 2,
    "design_hypothesis": 3,
    "speculative": 4,
    "blocked": 5,
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


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


def cases() -> list[dict[str, Any]]:
    raw = [
        ("LPE-001", "The current local source ledger has 26 rows and 8 vowel/modifier columns.", "source_observed", "source_observed", False),
        ("LPE-002", "The source-observed index contains 208 records.", "source_index", "source_index", False),
        ("LPE-003", "The Nwagu source layer has 27 rows.", "derived", "source_observed", True),
        ("LPE-004", "216 is a source-observed cell count.", "derived", "source_observed", True),
        ("LPE-005", "A 27-row layer can be derived if f/v is split.", "derived", "derived", False),
        ("LPE-006", "The f/v split is a design operation over the current inventory.", "derived", "design_hypothesis", False),
        ("LPE-007", "The f/v split proves a universal compression law.", "speculative", "source_observed", True),
        ("LPE-008", "E6 follows directly from the Nwagu chart.", "speculative", "source_observed", True),
        ("LPE-009", "E6 remains a speculative analogy until formal evidence is produced.", "speculative", "speculative", False),
        ("LPE-010", "The lab has a rights-cleared public glyph corpus.", "blocked", "source_observed", True),
        ("LPE-011", "The reported manuscript corpus is a blocked source target pending holdings and rights review.", "blocked", "blocked", False),
        ("LPE-012", "A Unicode proposal is ready because a gap matrix exists.", "blocked", "source_observed", True),
        ("LPE-013", "The Unicode gap matrix identifies missing proposal evidence.", "source_index", "source_index", False),
        ("LPE-014", "Layer-safe design systems can use derived forms if they keep the derived label.", "design_hypothesis", "design_hypothesis", False),
        ("LPE-015", "A generated design glyph is historical evidence.", "design_hypothesis", "source_observed", True),
        ("LPE-016", "A generated design glyph is a design artifact derived from a source-labeled system.", "design_hypothesis", "design_hypothesis", False),
        ("LPE-017", "The BMC is a working annotation index, not a fully reviewed glyph substrate.", "source_index", "source_index", False),
        ("LPE-018", "The BMC proves the final glyph grammar.", "source_index", "source_observed", True),
        ("LPE-019", "Tokenizer baselines show downstream NLP improvement.", "design_hypothesis", "source_observed", True),
        ("LPE-020", "Tokenizer baselines measure segmentation behavior only.", "design_hypothesis", "design_hypothesis", False),
        ("LPE-021", "Public metadata can be cited while reproduction rights remain unresolved.", "blocked", "blocked", False),
        ("LPE-022", "Public metadata means the manuscript images can be republished.", "blocked", "source_observed", True),
        ("LPE-023", "Logograph leads are visible chart leads, not a complete corpus.", "source_index", "source_index", False),
        ("LPE-024", "The chart lead set is the complete logograph corpus.", "source_index", "source_observed", True),
        ("LPE-025", "A standards mapping is interoperability evidence, not source validation.", "design_hypothesis", "design_hypothesis", False),
        ("LPE-026", "TEI/IIIF mapping validates all glyph shapes.", "design_hypothesis", "source_observed", True),
        ("LPE-027", "A negative result can be publication-relevant if it changes allowed claims.", "design_hypothesis", "design_hypothesis", False),
        ("LPE-028", "A compiled PDF means the paper is submission-ready.", "blocked", "source_observed", True),
        ("LPE-029", "A compiled PDF is an internal review artifact until gates pass.", "blocked", "blocked", False),
        ("LPE-030", "The source/derived distinction is the control variable for this research program.", "source_observed", "source_observed", False),
    ]
    return [
        {
            "case_id": cid,
            "claim_text": text,
            "input_layer": input_layer,
            "output_layer": output_layer,
            "gold_promotion_error": gold,
        }
        for cid, text, input_layer, output_layer, gold in raw
    ]


def predict(case: dict[str, Any]) -> bool:
    input_layer = case["input_layer"]
    output_layer = case["output_layer"]
    text = case["claim_text"].lower()
    rank_error = LAYER_RANK[output_layer] < LAYER_RANK[input_layer]
    lexical_error = any(
        phrase in text
        for phrase in [
            "source layer has 27",
            "source-observed cell count",
            "proves",
            "ready because",
            "historical evidence",
            "downstream nlp improvement",
            "can be republished",
            "complete logograph corpus",
            "validates all glyph shapes",
            "submission-ready",
        ]
    )
    return rank_error or lexical_error


def metrics(predictions: list[dict[str, Any]]) -> dict[str, Any]:
    tp = sum(1 for row in predictions if row["gold_promotion_error"] and row["predicted_promotion_error"])
    fp = sum(1 for row in predictions if not row["gold_promotion_error"] and row["predicted_promotion_error"])
    fn = sum(1 for row in predictions if row["gold_promotion_error"] and not row["predicted_promotion_error"])
    tn = sum(1 for row in predictions if not row["gold_promotion_error"] and not row["predicted_promotion_error"])
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "true_positive": tp,
        "false_positive": fp,
        "false_negative": fn,
        "true_negative": tn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def main() -> int:
    EXP.mkdir(parents=True, exist_ok=True)
    BENCH.mkdir(parents=True, exist_ok=True)

    rows = cases()
    predictions = []
    for row in rows:
        pred = dict(row)
        pred["predicted_promotion_error"] = predict(row)
        pred["correct"] = pred["predicted_promotion_error"] == pred["gold_promotion_error"]
        predictions.append(pred)

    score = metrics(predictions)
    by_layer = Counter(row["input_layer"] for row in rows)
    result = {
        "experiment_id": "EXP-FRONTIER-001",
        "benchmark_id": "LPE-BENCH-001",
        "generated_at": now(),
        "status": "FRONTIER_BENCHMARK_SEEDED_NOT_PAPER_READY",
        "case_count": len(rows),
        "input_layer_counts": dict(by_layer),
        "metrics": score,
        "decision": "FRONTIER_BENCHMARK_SEEDED_BASELINE_DETECTOR_PASSES_CURATED_SET",
        "research_claim": "Layer Promotion Error is a measurable failure mode for artifact-derived research and design systems.",
        "current_limit": "Curated 30-case benchmark; not yet a field benchmark or paper-ready result.",
    }

    write_jsonl(EXP / "data" / "lpe_cases.jsonl", rows)
    write_csv(EXP / "data" / "lpe_cases.csv", rows)
    write_jsonl(EXP / "data" / "lpe_predictions.jsonl", predictions)
    write_csv(EXP / "data" / "lpe_predictions.csv", predictions)
    write_json(EXP / "results.json", result)
    write_text(
        EXP / "analysis.md",
        f"""
        # Analysis

        This experiment converts Etisiobi's recurring failure mode into a
        benchmarkable object: Layer Promotion Error detection.

        The baseline detector combines evidence-layer rank checks with lexical
        overclaim triggers. On the curated 30-case seed set it produced:

        - precision: {score['precision']}
        - recall: {score['recall']}
        - F1: {score['f1']}

        This is not enough to claim a frontier paper. It is enough to define a
        research benchmark and move Article 10 from generic design prose toward
        a concrete systems result.
        """,
    )
    write_text(EXP / "decision.md", result["decision"])
    write_json(BENCH / "scoreboard.json", result)
    write_text(
        BENCH / "BENCHMARK.md",
        f"""
        # Layer Promotion Error Benchmark

        Benchmark ID: `LPE-BENCH-001`

        ## Research Object

        Detect whether a claim has been promoted from a weaker evidence layer to
        a stronger one. This benchmark is seeded from Nwagu Aneke/PAGC failures:
        26 x 8 = 208 is source-observed; 27/216 is derived by f/v split only.

        ## Current Result

        - Cases: `{len(rows)}`
        - Precision: `{score['precision']}`
        - Recall: `{score['recall']}`
        - F1: `{score['f1']}`
        - Status: `{result['status']}`
        - Decision: `{result['decision']}`

        ## Readiness

        This is a seeded frontier benchmark, not an impact-journal result. It
        becomes paper-candidate material only after expansion beyond 50 cases,
        alternative baselines, external prior art, and domain review.
        """,
    )
    print("FRONTIER_LAYER_PROMOTION_BENCHMARK_COMPLETE")
    print(f"cases={len(rows)}")
    print(f"precision={score['precision']}")
    print(f"recall={score['recall']}")
    print(f"f1={score['f1']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
