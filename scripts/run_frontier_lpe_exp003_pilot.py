from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation"

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


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def base_input_layer(text: str) -> str:
    lower = text.lower()
    if any(term in lower for term in ["blocked", "not ready", "rights", "authority", "approval", "human review", "submission", "public-release"]):
        return "blocked"
    if any(term in lower for term in ["speculative", "hypothesis", "analogy", "universal", "e6", "exceptional"]):
        return "speculative"
    if any(term in lower for term in ["derived", "design", "system", "tokenizer", "benchmark", "application", "invariant", "pipeline"]):
        return "design_hypothesis"
    if any(term in lower for term in ["27", "216", "f/v", "split"]):
        return "derived"
    if any(term in lower for term in ["208", "26", "source-observed", "source-critical", "ledger", "index", "chart", "transcription"]):
        return "source_index"
    return "design_hypothesis"


def apparent_output_layer(text: str, reviewer: str) -> str:
    lower = text.lower()
    if any(term in lower for term in ["is not ready", "not submission-ready", "remain open", "blocked", "needed before", "must not"]):
        return "blocked"
    if any(term in lower for term in ["source-observed", "historical count", "historical evidence", "completed glyph corpus", "corpus claim"]):
        return "source_observed"
    if any(term in lower for term in ["evidence package", "ledger", "208-record", "row-vowel index"]):
        return "source_index"
    if any(term in lower for term in ["derived", "f/v", "27/216"]):
        return "derived"
    if any(term in lower for term in ["hypothesis", "speculative", "possible", "analogy"]):
        return "speculative"
    if reviewer == "rights_authority_reviewer" and any(term in lower for term in ["public", "release", "submission", "authority", "rights"]):
        return "blocked"
    return "design_hypothesis"


def annotate(row: dict[str, str], reviewer: str) -> dict[str, Any]:
    text = row["claim_text"]
    input_layer = base_input_layer(text)
    output_layer = apparent_output_layer(text, reviewer)
    promotion = LAYER_RANK[output_layer] < LAYER_RANK[input_layer]
    if "can become" in text.lower() or "risk" in text.lower() or "avoids that failure" in text.lower():
        promotion = False
        output_layer = input_layer
    if promotion and output_layer == "source_observed" and input_layer in {"blocked", "speculative"}:
        severity = "blocking"
    elif promotion:
        severity = "material"
    else:
        severity = "none"
    return {
        "case_id": row["case_id"],
        "reviewer": reviewer,
        "input_layer": input_layer,
        "output_layer": output_layer,
        "promotion_error": "yes" if promotion else "no",
        "severity": severity,
        "rationale": f"Synthetic pilot label based on visible layer cues; not a human annotation.",
    }


def cohen_kappa(a: list[str], b: list[str]) -> float:
    assert len(a) == len(b)
    n = len(a)
    if n == 0:
        return 0.0
    labels = sorted(set(a) | set(b))
    observed = sum(1 for x, y in zip(a, b) if x == y) / n
    ca = Counter(a)
    cb = Counter(b)
    expected = sum((ca[label] / n) * (cb[label] / n) for label in labels)
    if expected == 1:
        return 1.0
    return (observed - expected) / (1 - expected)


def majority_vote(labels: list[str]) -> str:
    counts = Counter(labels)
    return counts.most_common(1)[0][0]


def main() -> int:
    queue = read_csv(EXP / "annotation_queue.csv")
    reviewers = ["methods_reviewer", "domain_postdoc", "rights_authority_reviewer"]
    annotations: list[dict[str, Any]] = []
    for row in queue:
        for reviewer in reviewers:
            annotations.append(annotate(row, reviewer))

    by_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for ann in annotations:
        by_case[ann["case_id"]].append(ann)
    adjudicated = []
    for row in queue:
        anns = by_case[row["case_id"]]
        promotion = majority_vote([ann["promotion_error"] for ann in anns])
        severity = "none" if promotion == "no" else majority_vote([ann["severity"] for ann in anns if ann["severity"] != "none"] or ["material"])
        adjudicated.append(
            {
                "case_id": row["case_id"],
                "claim_text": row["claim_text"],
                "source_type": row["source_type"],
                "split": row["split"],
                "pilot_promotion_error": promotion,
                "pilot_severity": severity,
                "pilot_label_status": "synthetic_not_human",
            }
        )

    reviewer_pairs = []
    for i, left in enumerate(reviewers):
        for right in reviewers[i + 1 :]:
            left_labels = [ann["promotion_error"] for ann in annotations if ann["reviewer"] == left]
            right_labels = [ann["promotion_error"] for ann in annotations if ann["reviewer"] == right]
            reviewer_pairs.append(
                {
                    "left": left,
                    "right": right,
                    "cohen_kappa": round(cohen_kappa(left_labels, right_labels), 4),
                    "agreement": round(sum(1 for x, y in zip(left_labels, right_labels) if x == y) / len(left_labels), 4),
                }
            )

    positives = sum(1 for row in adjudicated if row["pilot_promotion_error"] == "yes")
    result = {
        "experiment_id": "EXP-FRONTIER-003-PILOT",
        "generated_at": now(),
        "status": "SYNTHETIC_PILOT_LABELS_CREATED_NOT_HUMAN_REVIEW",
        "case_count": len(queue),
        "reviewer_count": len(reviewers),
        "annotation_count": len(annotations),
        "pilot_positive_rate": round(positives / len(queue), 4),
        "pairwise_agreement": reviewer_pairs,
        "frontier_claim_status": "not_ready",
        "current_limit": "Synthetic pilot labels are useful for harness testing but cannot replace independent human/domain annotation.",
    }

    write_jsonl(EXP / "pilot_annotations.jsonl", annotations)
    write_csv(EXP / "pilot_annotations.csv", annotations)
    write_jsonl(EXP / "pilot_adjudicated_labels.jsonl", adjudicated)
    write_csv(EXP / "pilot_adjudicated_labels.csv", adjudicated)
    write_json(EXP / "pilot_results.json", result)
    write_text(
        EXP / "pilot_analysis.md",
        f"""
        # EXP-FRONTIER-003 Pilot Analysis

        This pilot simulates three reviewer perspectives over the blind
        annotation queue. It is an engineering test of the annotation harness,
        not human/domain review.

        - Cases: {len(queue)}
        - Synthetic annotations: {len(annotations)}
        - Pilot positive rate: {result['pilot_positive_rate']}

        The next required step is independent human/domain annotation. These
        labels must not be used to claim frontier-level validity.
        """,
    )
    print("FRONTIER_LPE_EXP003_PILOT_COMPLETE")
    print(f"cases={len(queue)}")
    print(f"annotations={len(annotations)}")
    print(f"status={result['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

