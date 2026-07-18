from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP3 = ROOT / "experiments" / "EXP-FRONTIER-003-blind-lpe-annotation"
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"

ROLES = [
    "domain_source_reviewer",
    "methods_reviewer",
    "adversarial_impact_reviewer",
]


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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def annotation_template(rows: list[dict[str, str]], role: str) -> list[dict[str, Any]]:
    template = []
    for row in rows:
        template.append(
            {
                "case_id": row["case_id"],
                "role": role,
                "claim_text": row["claim_text"],
                "source_path": row["source_path"],
                "source_type": row["source_type"],
                "split": row["split"],
                "input_layer": "",
                "output_layer": "",
                "promotion_error": "",
                "severity": "",
                "confidence": "",
                "rationale": "",
                "public_release_ok": "",
            }
        )
    return template


def agent_template(rows: list[dict[str, str]], condition: str) -> list[dict[str, Any]]:
    return [
        {
            "case_id": row["case_id"],
            "condition": condition,
            "agent_id": "",
            "input_claim_text": row["claim_text"],
            "output_claim_text": "",
            "predicted_promotion_error": "",
            "predicted_input_layer": "",
            "predicted_output_layer": "",
            "confidence": "",
            "source_ids_used": "",
            "raw_output_path": "",
        }
        for row in rows
    ]


def main() -> int:
    source = EXP3 / "annotation_queue.csv"
    if not source.exists():
        raise FileNotFoundError(source)
    rows = read_csv(source)
    EXP5.mkdir(parents=True, exist_ok=True)
    write_csv(EXP5 / "frozen_annotation_queue.csv", rows)
    for role in ROLES:
        write_csv(EXP5 / "annotation_inputs" / f"{role}.csv", annotation_template(rows, role))
    for condition in ("C0_no_layer_labels", "C1_layer_labels", "C2_claim_gate", "C3_adversarial_review"):
        write_csv(EXP5 / "agent_run_templates" / f"{condition}.csv", agent_template(rows, condition))
    write_csv(
        EXP5 / "gold_labels_template.csv",
        [
            {
                "case_id": row["case_id"],
                "claim_text": row["claim_text"],
                "input_layer": "",
                "output_layer": "",
                "promotion_error": "",
                "severity": "",
                "adjudication_rationale": "",
                "source_review_status": "",
                "public_release_ok": "",
            }
            for row in rows
        ],
    )

    manifest = {
        "experiment_id": "EXP-FRONTIER-005",
        "generated_at": now(),
        "status": "ANNOTATION_AND_AGENT_RUN_TEMPLATES_READY_NOT_SCORED",
        "source_queue": source.relative_to(ROOT).as_posix(),
        "source_queue_sha256": sha256(source),
        "case_count": len(rows),
        "annotation_roles": ROLES,
        "agent_conditions": [
            "C0_no_layer_labels",
            "C1_layer_labels",
            "C2_claim_gate",
            "C3_adversarial_review",
        ],
        "gold_labels_required": True,
        "agent_outputs_required": True,
        "frontier_claim_status": "not_ready",
        "next_required_action": "Complete independent annotation inputs, adjudicate gold_labels.csv, then collect agent outputs before scoring.",
    }
    write_json(EXP5 / "manifest.json", manifest)
    write_text(
        EXP5 / "README.md",
        """
# EXP-FRONTIER-005 Runner Packet

This directory contains the frozen input packet for real Layer Promotion Error
evaluation.

## Files

- `frozen_annotation_queue.csv`: frozen cases copied from EXP-FRONTIER-003.
- `annotation_inputs/*.csv`: independent reviewer templates.
- `agent_run_templates/*.csv`: output templates for agent conditions.
- `manifest.json`: packet checksum and status.

## Rule

Do not score this experiment until `gold_labels.csv` and agent run files exist.
Synthetic labels are allowed only for pilot testing and must not be reported as
frontier evidence.
""",
    )
    write_text(
        EXP5 / "ANNOTATION_PROTOCOL.md",
        """
# EXP-FRONTIER-005 Annotation Protocol

## Goal

Produce independent labels for Layer Promotion Error without letting annotators
see benchmark predictions or agent-condition outputs.

## Required Reviewers

- `domain_source_reviewer`: decides what the claim requires from the Nwagu/PAGC
  source dossier.
- `methods_reviewer`: checks whether the evidence layer is methodologically
  sufficient.
- `adversarial_impact_reviewer`: labels how a hostile reviewer would classify
  the claim in a paper.

## Layer Definitions

- `source_observed`: directly observed in source evidence.
- `source_index`: represented in a transcription, ledger, or structured index,
  but not fully source-reviewed.
- `derived`: produced by an explicit operation, such as the f/v split.
- `design_hypothesis`: system-design or application claim inspired by the
  artifact.
- `speculative`: analogy, theory, or possibility not yet validated.
- `blocked`: unavailable, rights-blocked, authority-blocked, or missing evidence.

## Promotion Error Rule

A Layer Promotion Error occurs when a claim asserts a stronger evidence layer
than the available evidence supports.

Examples:

- `derived -> source_observed`: promotion error.
- `blocked -> publication_ready`: promotion error.
- `design_hypothesis -> historical source claim`: promotion error.
- `derived -> derived`: no promotion error if the derived status is preserved.

## Severity

- `none`: no promotion.
- `minor`: wording imprecision that does not affect the main claim.
- `material`: claim would mislead a reader or reviewer.
- `blocking`: claim would invalidate a paper, public release, or source-rights
  decision.

## Adjudication

The adjudicator must create `gold_labels.csv` only after all three reviewer
files are complete. If reviewers disagree, choose the more conservative label
unless the source dossier directly supports a stronger layer.
""",
    )
    write_text(
        EXP5 / "AGENT_RUN_PROTOCOL.md",
        """
# EXP-FRONTIER-005 Agent Run Protocol

## Conditions

- `C0_no_layer_labels`: agent receives claim text only.
- `C1_layer_labels`: agent receives layer definitions.
- `C2_claim_gate`: agent receives layer definitions plus rejection rules.
- `C3_adversarial_review`: agent receives layer definitions, claim gate, and an
  adversarial reviewer instruction.

## Output Contract

Each row in `agent_runs/*.csv` must fill:

- `case_id`
- `condition`
- `agent_id`
- `output_claim_text`
- `predicted_promotion_error`
- `predicted_input_layer`
- `predicted_output_layer`
- `confidence`
- `source_ids_used`
- `raw_output_path`

## Anti-Leakage Rules

- Agents must not see `gold_labels.csv`.
- Test split evaluation must happen once after prompts and thresholds are frozen.
- Any prompt revision after seeing scores creates a new run ID.
""",
    )
    print("LPE_EXP005_PACKET_READY")
    print(f"cases={len(rows)}")
    print(f"status={manifest['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
