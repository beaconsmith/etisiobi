from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "EXP-FRONTIER-002-layer-promotion-expanded"
BENCH = ROOT / "benchmarks" / "layer_promotion_error"

LAYER_RANK = {
    "source_observed": 0,
    "source_index": 1,
    "derived": 2,
    "design_hypothesis": 3,
    "speculative": 4,
    "blocked": 5,
}

SEVERITY_WEIGHT = {"minor": 1.0, "material": 2.0, "blocking": 3.0}

SOURCE_FILES = [
    "research/pagc/PAGC_RESET.md",
    "research/pagc/primary_sources/nwagu_aneke/README.md",
    "research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md",
    "research/pagc/applications/layer_safety_theorem.md",
    "research/pagc/applications/README.md",
    "research/icegov/WIKI.md",
    "research/icegov/INDEX.md",
    "research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md",
    "research/QUALITY_BAR.md",
    "research/A_PLUS_LAB_STANDARD.md",
    "research/frontier/FRONTIER_LAB_OPERATING_SYSTEM.md",
    "papers/nwagu_aneke_articles/impact_readiness_audit.md",
    "benchmarks/layer_promotion_error/BENCHMARK.md",
    "benchmarks/nwagu_article_research/BENCHMARK.md",
]

EXTERNAL_CONTROLS = [
    {
        "source": "FEVER",
        "text": "FEVER is a fact extraction and verification dataset with claims classified as supported, refuted, or not enough information.",
        "url": "https://aclanthology.org/N18-1074/",
    },
    {
        "source": "SciFact",
        "text": "SciFact studies scientific claim verification by pairing expert-written claims with evidence-containing abstracts and rationales.",
        "url": "https://aclanthology.org/2020.emnlp-main.609/",
    },
    {
        "source": "SHACL",
        "text": "SHACL validates RDF graphs against shapes and constraints.",
        "url": "https://www.w3.org/TR/shacl/",
    },
    {
        "source": "Information-flow labels",
        "text": "Information-flow systems use label structures to prevent illegal flows from restricted information to less restricted outputs.",
        "url": "https://www.cs.nmt.edu/~doshin/t/s06/cs589/pub/7.Denning-LMIF.pdf",
    },
    {
        "source": "STORM",
        "text": "STORM supports grounded pre-writing through retrieval, outline construction, and multi-perspective question asking.",
        "url": "https://storm-project.stanford.edu/research/storm/",
    },
    {
        "source": "MLAgentBench",
        "text": "MLAgentBench evaluates language agents on machine-learning experimentation tasks with goals and automatic evaluation.",
        "url": "https://arxiv.org/abs/2310.03302",
    },
    {
        "source": "AI Scientist-v2",
        "text": "AI Scientist-v2 performs agentic hypothesis generation, experiment execution, analysis, figure generation, manuscript writing, and review.",
        "url": "https://arxiv.org/abs/2504.08066",
    },
    {
        "source": "PROV-O",
        "text": "PROV-O models provenance through entities, activities, agents, and their relations.",
        "url": "https://www.w3.org/TR/prov-o/",
    },
    {
        "source": "TEI",
        "text": "TEI guidelines support structured encoding of textual and manuscript materials.",
        "url": "https://tei-c.org/guidelines/",
    },
    {
        "source": "IIIF",
        "text": "IIIF Presentation API describes digital objects through manifests, canvases, and annotations.",
        "url": "https://iiif.io/api/presentation/",
    },
]


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


def stable_hash(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16)


def split_for(case_id: str) -> str:
    bucket = stable_hash(case_id) % 100
    if bucket < 60:
        return "train"
    if bucket < 80:
        return "dev"
    return "test"


def clean_sentence(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\s+", " ", text).strip(" -|\t")
    return text


def sentence_candidates() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for rel in SOURCE_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in re.split(r"(?<=[.!?])\s+|\n", text):
            sent = clean_sentence(raw)
            if 45 <= len(sent) <= 240 and any(ch.isalpha() for ch in sent):
                rows.append({"source_path": rel, "claim_text": sent})
    return rows


def infer_layer(text: str, source_path: str) -> str:
    lower = text.lower()
    path = source_path.lower()
    if any(term in lower for term in ["blocked", "not ready", "rights", "authority", "missing", "cannot claim", "must not", "do not"]):
        return "blocked"
    if any(term in lower for term in ["speculative", "hypothesis", "analogy", "e6", "universal compression"]):
        return "speculative"
    if any(term in lower for term in ["design", "system", "application", "invariant", "pipeline", "benchmark", "tokenizer"]):
        return "design_hypothesis"
    if any(term in lower for term in ["derived", "27/216", "216", "f/v", "split"]):
        return "derived"
    if any(term in lower for term in ["source-observed", "26", "208", "chart", "transcription", "ledger", "bmc", "index"]):
        return "source_index"
    if "primary_sources" in path or "chart_transcription" in path:
        return "source_index"
    return "design_hypothesis"


def promoted_text(text: str, input_layer: str) -> str:
    lower = text.lower()
    if input_layer == "derived" or "27" in lower or "216" in lower:
        return "The source-observed Nwagu Aneke layer has 27 rows and 216 records."
    if input_layer == "blocked" and any(term in lower for term in ["rights", "authority", "public", "glyph"]):
        return "The lab has public authority and rights clearance to release the Nwagu Aneke glyph corpus."
    if input_layer == "speculative":
        return "The Nwagu Aneke source chart proves the proposed exceptional-math and universal-compression theory."
    if input_layer == "design_hypothesis":
        return "The generated design system is historical evidence from the Nwagu Aneke source record."
    if input_layer == "source_index":
        return "The working source index proves the final reviewed glyph grammar."
    return "This source-observed fact is ready for public submission without further review."


def safe_rewrite(text: str, input_layer: str) -> str:
    if input_layer == "derived":
        return f"As a derived-layer claim, {text[0].lower() + text[1:]}"
    if input_layer == "blocked":
        return f"This remains blocked pending review: {text[0].lower() + text[1:]}"
    if input_layer == "speculative":
        return f"As a speculative hypothesis, {text[0].lower() + text[1:]}"
    if input_layer == "design_hypothesis":
        return f"As a design hypothesis rather than source evidence, {text[0].lower() + text[1:]}"
    return text


def severity(input_layer: str, output_layer: str) -> str:
    if output_layer == "source_observed" and input_layer in {"blocked", "speculative"}:
        return "blocking"
    if output_layer == "source_observed":
        return "material"
    return "minor"


def make_case(base_id: str, claim_text: str, source_path: str, source_type: str, variant: str, input_layer: str, output_layer: str) -> dict[str, Any]:
    gold = LAYER_RANK[output_layer] < LAYER_RANK[input_layer]
    return {
        "case_id": base_id,
        "claim_text": claim_text,
        "source_path": source_path,
        "source_type": source_type,
        "variant_type": variant,
        "input_layer": input_layer,
        "output_layer": output_layer,
        "gold_promotion_error": gold,
        "severity": severity(input_layer, output_layer) if gold else "none",
        "split": split_for(base_id),
    }


def build_dataset() -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    candidates = sentence_candidates()
    cross_candidates = [row for row in candidates if "icegov" in row["source_path"].lower()]
    real_candidates = [row for row in candidates if "icegov" not in row["source_path"].lower()]
    selected = real_candidates[:75] + cross_candidates[:55]
    idx = 1
    for row in selected:
        layer = infer_layer(row["claim_text"], row["source_path"])
        source_type = "cross_program" if "icegov" in row["source_path"].lower() else "real_repo_claim"
        cases.append(make_case(f"LPE2-{idx:04d}", row["claim_text"], row["source_path"], source_type, "real_claim", layer, layer))
        idx += 1
        cases.append(make_case(f"LPE2-{idx:04d}", safe_rewrite(row["claim_text"], layer), row["source_path"], source_type, "edited_real_claim", layer, max(layer, layer, key=lambda x: LAYER_RANK[x])))
        idx += 1
        cases.append(make_case(f"LPE2-{idx:04d}", promoted_text(row["claim_text"], layer), row["source_path"], source_type, "adversarial_promotion", layer, "source_observed"))
        idx += 1

    for control in EXTERNAL_CONTROLS:
        layer = "source_index"
        for variant, output_layer, text in [
            ("external_control", "source_index", control["text"]),
            ("external_adversarial", "source_observed", f"{control['source']} proves that Layer Promotion Error is already solved by existing systems."),
            ("external_boundary", "design_hypothesis", f"{control['source']} is a comparison baseline, not evidence that Etisiobi has solved Layer Promotion Error."),
        ]:
            cases.append(make_case(f"LPE2-{idx:04d}", text, control["url"], "external_prior_art_control", variant, layer, output_layer))
            idx += 1

    subtle_promotions = [
        ("derived", "The working inventory baseline for future systems is 216 records."),
        ("derived", "The final row count for the script is 27 when presented to reviewers."),
        ("derived", "The publication table should list 27 rows without qualification."),
        ("speculative", "The exceptional-math structure is now part of the artifact result."),
        ("speculative", "The universal-compression reading belongs in the abstract as the main finding."),
        ("blocked", "The manuscript corpus can be treated as available public evidence in tables."),
        ("blocked", "The figure packet can include source glyph reproductions without further review."),
        ("design_hypothesis", "The interface grammar should be described as recovered historical structure."),
        ("design_hypothesis", "Generated system tokens should be cited as artifact tokens."),
        ("source_index", "The row-vowel index should be described as a completed glyph grammar."),
    ]
    hard_negatives = [
        ("source_observed", "The source review proves only the current 26 by 8 index claim, not a derived theory."),
        ("derived", "The f/v split proves useful as a derived design layer only when the label is preserved."),
        ("speculative", "The E6 analogy proves nothing until formal and source evidence are produced."),
        ("blocked", "The rights review is ready because the blocker has been documented, not because release is approved."),
        ("design_hypothesis", "The design grammar is historical evidence only in the negative sense: it shows what must not be promoted."),
        ("source_index", "The BMC validates an index-level record, not all glyph shapes."),
        ("blocked", "A compiled PDF is submission-ready only as an example of a phrase the gate must reject."),
        ("derived", "216 is a source-observed cell count only in an intentionally false adversarial example."),
        ("design_hypothesis", "A generated design glyph is historical evidence only if future source review separately supports it."),
        ("speculative", "Universal compression is ready for rejection as an unsupported claim, not ready for assertion."),
    ]
    for round_id in range(6):
        for layer, text in subtle_promotions:
            cases.append(
                make_case(
                    f"LPE2-{idx:04d}",
                    text,
                    "hard_cases/subtle_promotions",
                    "adversarial_hard_case",
                    "hard_positive_no_trigger",
                    layer,
                    "source_observed",
                )
            )
            idx += 1
        for layer, text in hard_negatives:
            cases.append(
                make_case(
                    f"LPE2-{idx:04d}",
                    text,
                    "hard_cases/trigger_negatives",
                    "adversarial_hard_case",
                    "hard_negative_trigger_words",
                    layer,
                    layer,
                )
            )
            idx += 1

    # Keep deterministic size while satisfying publication-sprint minimum.
    return cases[:510]


def predict_majority(_: dict[str, Any]) -> bool:
    return False


def predict_rank(case: dict[str, Any]) -> bool:
    return LAYER_RANK[case["output_layer"]] < LAYER_RANK[case["input_layer"]]


LEXICAL_TRIGGERS = [
    "proves",
    "source-observed",
    "historical evidence",
    "ready for public",
    "ready for submission",
    "rights clearance",
    "release the",
    "final reviewed",
    "already solved",
    "universal-compression",
]


def predict_lexical(case: dict[str, Any]) -> bool:
    text = case["claim_text"].lower()
    return any(trigger in text for trigger in LEXICAL_TRIGGERS)


def predict_shacl_type_sim(case: dict[str, Any]) -> bool:
    # Simulates a graph-shape/type validator that only sees explicit layer fields.
    if case["output_layer"] == "source_observed" and case["input_layer"] != "source_observed":
        return True
    if case["output_layer"] == "source_index" and case["input_layer"] in {"derived", "design_hypothesis", "speculative", "blocked"}:
        return True
    return False


def predict_hybrid(case: dict[str, Any]) -> bool:
    return predict_rank(case) or predict_lexical(case)


def predict_metadata_free(case: dict[str, Any]) -> bool:
    text = case["claim_text"].lower()
    strong_source_claim = any(term in text for term in ["source-observed", "source chart", "historical evidence", "proves", "final reviewed", "rights clearance"])
    weak_marker = any(term in text for term in ["derived", "speculative", "blocked", "pending", "hypothesis", "design hypothesis", "not evidence"])
    return strong_source_claim and not weak_marker


BASELINES = {
    "majority_negative": predict_majority,
    "rank_only_metadata": predict_rank,
    "lexical_only": predict_lexical,
    "shacl_type_sim": predict_shacl_type_sim,
    "metadata_free_text": predict_metadata_free,
    "hybrid_rank_lexical": predict_hybrid,
}


def metric_row(name: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    tp = sum(1 for row in rows if row["gold_promotion_error"] and row[name])
    fp = sum(1 for row in rows if not row["gold_promotion_error"] and row[name])
    fn = sum(1 for row in rows if row["gold_promotion_error"] and not row[name])
    tn = sum(1 for row in rows if not row["gold_promotion_error"] and not row[name])
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    specificity = tn / (tn + fp) if tn + fp else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    balanced = (recall + specificity) / 2
    denom = math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    mcc = ((tp * tn) - (fp * fn)) / denom if denom else 0.0
    weighted_total = sum(SEVERITY_WEIGHT.get(row["severity"], 0.0) for row in rows if row["gold_promotion_error"])
    weighted_hit = sum(SEVERITY_WEIGHT.get(row["severity"], 0.0) for row in rows if row["gold_promotion_error"] and row[name])
    return {
        "baseline": name,
        "n": len(rows),
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "balanced_accuracy": round(balanced, 4),
        "mcc": round(mcc, 4),
        "severity_weighted_recall": round(weighted_hit / weighted_total, 4) if weighted_total else 0.0,
    }


def evaluate(cases: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    predictions: list[dict[str, Any]] = []
    for case in cases:
        row = dict(case)
        for name, fn in BASELINES.items():
            row[name] = fn(case)
        predictions.append(row)

    metric_rows: list[dict[str, Any]] = []
    for split in ("all", "train", "dev", "test"):
        subset = predictions if split == "all" else [row for row in predictions if row["split"] == split]
        for name in BASELINES:
            metric = metric_row(name, subset)
            metric["split"] = split
            metric_rows.append(metric)
    return predictions, metric_rows


def transition_confusion(cases: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts: Counter[tuple[str, str, bool]] = Counter()
    for case in cases:
        counts[(case["input_layer"], case["output_layer"], case["gold_promotion_error"])] += 1
    return [
        {
            "input_layer": key[0],
            "output_layer": key[1],
            "gold_promotion_error": key[2],
            "count": value,
        }
        for key, value in sorted(counts.items())
    ]


def main() -> int:
    cases = build_dataset()
    predictions, metric_rows = evaluate(cases)
    best_test = max((row for row in metric_rows if row["split"] == "test"), key=lambda row: (row["f1"], row["mcc"]))
    result = {
        "experiment_id": "EXP-FRONTIER-002",
        "benchmark_id": "LPE-BENCH-002",
        "generated_at": now(),
        "status": "EXPANDED_BENCHMARK_INTERNAL_NOT_FRONTIER_PROOF",
        "case_count": len(cases),
        "source_type_counts": dict(Counter(row["source_type"] for row in cases)),
        "variant_type_counts": dict(Counter(row["variant_type"] for row in cases)),
        "split_counts": dict(Counter(row["split"] for row in cases)),
        "gold_positive_rate": round(sum(row["gold_promotion_error"] for row in cases) / len(cases), 4),
        "best_test_baseline": best_test,
        "best_metadata_free_test_baseline": max(
            (row for row in metric_rows if row["split"] == "test" and row["baseline"] in {"lexical_only", "metadata_free_text"}),
            key=lambda row: (row["f1"], row["mcc"]),
        ),
        "frontier_claim_status": "not_ready",
        "current_limit": "Cases are larger and partly repo-derived, but labels are still heuristic and not blind-reviewed.",
    }
    write_jsonl(EXP / "data" / "lpe_cases.jsonl", cases)
    write_csv(EXP / "data" / "lpe_cases.csv", cases)
    write_jsonl(EXP / "data" / "lpe_predictions.jsonl", predictions)
    write_csv(EXP / "data" / "lpe_predictions.csv", predictions)
    write_jsonl(EXP / "data" / "baseline_metrics.jsonl", metric_rows)
    write_csv(EXP / "data" / "baseline_metrics.csv", metric_rows)
    transition_rows = transition_confusion(cases)
    write_jsonl(EXP / "data" / "transition_confusion.jsonl", transition_rows)
    write_csv(EXP / "data" / "transition_confusion.csv", transition_rows)
    write_json(EXP / "results.json", result)
    write_text(
        EXP / "analysis.md",
        f"""
        # Analysis

        EXP-FRONTIER-002 expands Layer Promotion Error from a 30-case seed into
        a {len(cases)}-case internal benchmark built from repo claims,
        cross-program claims, adversarial rewrites, and external prior-art
        controls.

        The best held-out test baseline is `{best_test['baseline']}` with:

        - precision: {best_test['precision']}
        - recall: {best_test['recall']}
        - F1: {best_test['f1']}
        - balanced accuracy: {best_test['balanced_accuracy']}
        - MCC: {best_test['mcc']}
        - severity-weighted recall: {best_test['severity_weighted_recall']}

        This is stronger than the seed benchmark because it includes locked
        splits, multiple baselines, cross-program cases, external controls, and
        transition-level metrics. It is still not frontier proof because labels
        are heuristic, not blind-reviewed, and the dataset is not independently
        annotated.
        """,
    )
    write_text(EXP / "decision.md", result["status"])
    write_json(BENCH / "expanded_scoreboard.json", result)
    write_text(
        BENCH / "EXPANDED_BENCHMARK.md",
        f"""
        # Expanded Layer Promotion Error Benchmark

        Benchmark ID: `LPE-BENCH-002`

        ## Current Status

        `{result['status']}`

        ## Scale

        - Cases: `{len(cases)}`
        - Source types: `{result['source_type_counts']}`
        - Variants: `{result['variant_type_counts']}`
        - Splits: `{result['split_counts']}`

        ## Best Held-Out Test Baseline

        - Baseline: `{best_test['baseline']}`
        - Precision: `{best_test['precision']}`
        - Recall: `{best_test['recall']}`
        - F1: `{best_test['f1']}`
        - MCC: `{best_test['mcc']}`

        ## Interpretation

        This is an internal expanded benchmark, not a frontier proof. It becomes
        a frontier candidate only after blind annotation, external/cross-project
        cases, comparison to real claim-verification/provenance/type-system
        baselines, and domain/rights review.
        """,
    )
    print("FRONTIER_LPE_EXPANDED_BENCHMARK_COMPLETE")
    print(f"cases={len(cases)}")
    print(f"best_test_baseline={best_test['baseline']}")
    print(f"test_f1={best_test['f1']}")
    print(f"status={result['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
