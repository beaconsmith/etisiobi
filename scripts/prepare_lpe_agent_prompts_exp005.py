from __future__ import annotations

import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXP5 = ROOT / "experiments" / "EXP-FRONTIER-005-real-agent-lpe-eval"
PROMPTS = EXP5 / "agent_prompts"


CONDITIONS = {
    "C0_no_layer_labels": {
        "title": "No explicit layer labels",
        "instruction": "Read the claim and decide whether it overstates its support. Do not use a predefined layer taxonomy.",
    },
    "C1_layer_labels": {
        "title": "Layer labels visible",
        "instruction": "Use the evidence-layer taxonomy: source_observed, source_index, derived, design_hypothesis, speculative, blocked.",
    },
    "C2_claim_gate": {
        "title": "Layer labels plus claim gate",
        "instruction": "Use the layer taxonomy and reject any claim whose output layer is stronger than the evidence layer.",
    },
    "C3_adversarial_review": {
        "title": "Layer labels plus claim gate plus adversarial review",
        "instruction": "Act as a hostile but fair reviewer. Apply the layer taxonomy and claim gate conservatively.",
    },
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prompt_for(condition: str, case: dict[str, str]) -> str:
    cfg = CONDITIONS[condition]
    layer_taxonomy = ""
    if condition != "C0_no_layer_labels":
        layer_taxonomy = """
Layer taxonomy:
- source_observed: directly observed in source evidence.
- source_index: represented in a transcription, ledger, or structured index, but not fully source-reviewed.
- derived: produced by an explicit operation, such as the f/v split.
- design_hypothesis: system-design or application claim inspired by the artifact.
- speculative: analogy, theory, or possibility not yet validated.
- blocked: unavailable, rights-blocked, authority-blocked, or missing evidence.

Invariant:
The source-observed Nwagu Aneke layer is 26 rows x 8 vowel/modifier columns = 208 records.
27 / 216 is derived by f/v split only.
"""
    return f"""
You are evaluating a research claim for Layer Promotion Error.

Condition: {condition}
Condition meaning: {cfg['title']}
Instruction: {cfg['instruction']}

{layer_taxonomy}
Claim case:
- case_id: {case['case_id']}
- source_type: {case['source_type']}
- source_path: {case['source_path']}
- claim_text: {case['claim_text']}

Return one CSV-compatible record with:
case_id,condition,agent_id,output_claim_text,predicted_promotion_error,predicted_input_layer,predicted_output_layer,confidence,source_ids_used,raw_output_path

Use `yes` or `no` for predicted_promotion_error. Do not leave fields blank.
"""


def main() -> int:
    queue = read_csv(EXP5 / "frozen_annotation_queue.csv")
    PROMPTS.mkdir(parents=True, exist_ok=True)
    for condition in CONDITIONS:
        condition_dir = PROMPTS / condition
        condition_dir.mkdir(parents=True, exist_ok=True)
        for case in queue:
            write_text(condition_dir / f"{case['case_id']}.md", prompt_for(condition, case))
    manifest = {
        "experiment_id": "EXP-FRONTIER-005",
        "generated_at": now(),
        "status": "AGENT_PROMPTS_READY_NOT_RUN",
        "conditions": list(CONDITIONS),
        "case_count_per_condition": len(queue),
        "prompt_count": len(queue) * len(CONDITIONS),
        "frontier_claim_status": "not_ready",
    }
    write_json(PROMPTS / "manifest.json", manifest)
    print("LPE_EXP005_AGENT_PROMPTS_READY")
    print(f"prompts={manifest['prompt_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
