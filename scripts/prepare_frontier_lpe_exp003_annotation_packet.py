from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation"

SOURCE_ROOTS = [
    ("real_agent_output", ROOT / "papers" / "nwagu_aneke_articles"),
    ("real_agent_output", ROOT / "outputs"),
    ("program_source", ROOT / "research" / "pagc"),
    ("cross_program", ROOT / "research" / "icegov"),
    ("cross_program", ROOT / "research" / "papers"),
    ("lab_control", ROOT / "research" / "frontier"),
]

EXCLUDED_FILE_NAMES = {
    "manifest.json",
    "compile_report.md",
    "lpe_cases.jsonl",
    "lpe_predictions.jsonl",
    "baseline_metrics.jsonl",
}

EXTERNAL_PROMPTS = [
    ("FEVER", "Fact verification benchmarks classify claims against evidence, but do not directly ask whether an evidence status was promoted between artifact layers."),
    ("SciFact", "Scientific claim verification evaluates support or refutation from paper abstracts and rationales."),
    ("SHACL", "Graph constraint systems can validate shape rules over RDF data graphs."),
    ("Information flow", "Label lattices prevent prohibited flows across security levels and are a useful comparator for evidence-layer monotonicity."),
    ("PROV-O", "Provenance models can record entities, activities, agents, and derivation relations."),
    ("TEI", "Text encoding can represent source transcription and editorial intervention."),
    ("IIIF", "Image interoperability systems can identify canvases and regions of source artifacts."),
    ("Web Annotation", "Annotation models can connect bodies, targets, motivations, and selectors."),
    ("CIDOC CRM", "Cultural heritage ontologies can model objects, events, actors, and interpretations."),
    ("CARE", "Community data governance requires authority, responsibility, ethics, and collective benefit."),
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
    text = re.sub(r"\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})?", " ", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -|\t")
    return text


def is_claim_like(sent: str) -> bool:
    lower = sent.lower()
    if len(sent.split()) < 9:
        return False
    if sent.count("/") >= 2 or sent.count("\\") >= 1:
        return False
    if lower.startswith(("{", "}", "\"", "|", "- ", "#", "generated:", "benchmark path:")):
        return False
    if re.search(r"\.(pdf|tex|json|jsonl|csv|md)\b", lower):
        return False
    if not re.search(r"[.!?]$", lower):
        return False
    useful_terms = [
        "source", "derived", "claim", "evidence", "rights", "authority", "glyph",
        "benchmark", "review", "ready", "proves", "supports", "blocks", "public",
        "count", "27", "216", "26", "208", "governance", "artifact", "paper",
        "submission", "research", "layer", "speculative", "human", "method",
    ]
    return any(term in lower for term in useful_terms)


def extract_sentences() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for source_type, root in SOURCE_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in {".md", ".tex", ".json", ".jsonl"}:
                continue
            if path.name in EXCLUDED_FILE_NAMES:
                continue
            if any(part in {"compile_logs", "__pycache__"} for part in path.parts):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            text = re.sub(r"\n(?!\n)", " ", text)
            for raw in re.split(r"(?<=[.!?])\s+|\n\n+", text):
                sent = clean_sentence(raw)
                if not (70 <= len(sent) <= 280):
                    continue
                if not is_claim_like(sent):
                    continue
                key = sent.lower()
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    {
                        "source_type": source_type,
                        "source_path": path.relative_to(ROOT).as_posix(),
                        "claim_text": sent,
                    }
                )
    return rows


def build_queue() -> list[dict[str, Any]]:
    rows = extract_sentences()
    real_agent = [row for row in rows if row["source_type"] == "real_agent_output"][:130]
    cross = [row for row in rows if row["source_type"] == "cross_program"][:90]
    program = [row for row in rows if row["source_type"] == "program_source"][:110]
    selected = real_agent + cross + program
    queue: list[dict[str, Any]] = []
    idx = 1
    for row in selected:
        case_id = f"LPE3-{idx:04d}"
        queue.append(
            {
                "case_id": case_id,
                "claim_text": row["claim_text"],
                "source_path": row["source_path"],
                "source_type": row["source_type"],
                "model_visible_text": row["claim_text"],
                "split": split_for(case_id),
                "annotation_status": "unlabeled",
                "input_layer": "",
                "output_layer": "",
                "promotion_error": "",
                "severity": "",
                "annotator_rationale": "",
            }
        )
        idx += 1
    for source, text in EXTERNAL_PROMPTS:
        for variant in (
            text,
            f"{source} should be treated as a comparator, not as evidence that Layer Promotion Error is solved.",
            f"A careless paper could cite {source} as if it already validates the Etisiobi benchmark.",
        ):
            case_id = f"LPE3-{idx:04d}"
            queue.append(
                {
                    "case_id": case_id,
                    "claim_text": variant,
                    "source_path": f"external_prior_art/{source}",
                    "source_type": "external_prior_art_control",
                    "model_visible_text": variant,
                    "split": split_for(case_id),
                    "annotation_status": "unlabeled",
                    "input_layer": "",
                    "output_layer": "",
                    "promotion_error": "",
                    "severity": "",
                    "annotator_rationale": "",
                }
            )
            idx += 1
    return queue[:420]


def main() -> int:
    queue = build_queue()
    counts = Counter(row["source_type"] for row in queue)
    manifest = {
        "experiment_id": "EXP-FRONTIER-003",
        "generated_at": now(),
        "status": "BLIND_ANNOTATION_PACKET_READY_UNLABELED",
        "case_count": len(queue),
        "source_type_counts": dict(counts),
        "split_counts": dict(Counter(row["split"] for row in queue)),
        "annotation_required": True,
        "labels_frozen": False,
        "frontier_claim_status": "not_ready",
        "minimum_annotators": 3,
        "required_next_step": "Independent annotators must label input_layer, output_layer, promotion_error, severity, and rationale before scoring.",
    }
    write_jsonl(EXP / "annotation_queue.jsonl", queue)
    write_csv(EXP / "annotation_queue.csv", queue)
    write_json(EXP / "manifest.json", manifest)
    write_text(
        EXP / "annotation_codebook.md",
        """
        # EXP-FRONTIER-003 Annotation Codebook

        ## Task

        Label whether a claim promotes a weaker evidence layer into a stronger
        claim than the evidence permits.

        ## Layers

        - `source_observed`: directly observed in primary/local source evidence.
        - `source_index`: represented in a structured index or transcription but
          not fully source-reviewed.
        - `derived`: produced by an explicitly stated operation such as the f/v
          split.
        - `design_hypothesis`: system-design or application claim inspired by
          the artifact.
        - `speculative`: analogy, theory, or possibility not yet validated.
        - `blocked`: unavailable, rights-blocked, authority-blocked, or missing
          evidence.

        ## Labels To Fill

        - `input_layer`: weakest evidence layer needed to support the claim.
        - `output_layer`: layer the claim appears to assert.
        - `promotion_error`: `yes`, `no`, or `unclear`.
        - `severity`: `none`, `minor`, `material`, or `blocking`.
        - `annotator_rationale`: one sentence with evidence.

        ## Rule

        A promotion error occurs when the output layer is stronger than the
        evidence layer. The most dangerous errors are derived/speculative/blocked
        claims stated as source-observed or publication-ready facts.
        """,
    )
    write_text(
        EXP / "plan.md",
        """
        # EXP-FRONTIER-003: Blind LPE Annotation Packet

        This experiment prepares the first label-free queue for independent
        Layer Promotion Error annotation. It intentionally does not score a
        detector. Scoring before independent labels would repeat the EXP-002
        construct-leakage problem.

        Next required action: assign at least three independent annotators and
        freeze their labels before running metadata-free baselines.
        """,
    )
    print("FRONTIER_LPE_EXP003_PACKET_READY")
    print(f"cases={len(queue)}")
    print(f"status={manifest['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
