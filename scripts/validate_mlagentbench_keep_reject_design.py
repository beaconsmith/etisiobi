from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-009-mlagentbench-keep-reject-loop"
MANIFEST_PATH = EXP_DIR / "manifest.json"
DESIGN_PATH = EXP_DIR / "KEEP_REJECT_LOOP_DESIGN.md"
TASKS_PATH = EXP_DIR / "task_cards.csv"
DECISION_SCHEMA_PATH = EXP_DIR / "decision_schema.json"
NEGATIVE_CONTROL_PATH = EXP_DIR / "negative_control.md"

REQUIRED_FILES = [
    MANIFEST_PATH,
    DESIGN_PATH,
    TASKS_PATH,
    DECISION_SCHEMA_PATH,
    NEGATIVE_CONTROL_PATH,
]

REQUIRED_MANIFEST_FIELDS = {
    "experiment_id",
    "atlas_id",
    "status",
    "claim_ceiling",
    "primary_sources",
    "local_inputs",
    "external_actions_taken",
    "dependencies_installed",
    "agents_run",
    "model_or_api_run",
    "private_data_downloaded",
    "task_card_count",
    "decision_labels",
    "blocking_gates",
    "exact_next_action",
}

PRIMARY_SOURCES = {
    "https://arxiv.org/abs/2310.03302",
    "https://github.com/snap-stanford/MLAgentBench",
}

REQUIRED_TASK_FIELDS = {
    "task_id",
    "task_name",
    "research_object",
    "input_layer",
    "goal",
    "allowed_actions",
    "required_logs",
    "metric",
    "keep_condition",
    "reject_condition",
    "negative_control",
    "claim_ceiling",
}

REQUIRED_RESEARCH_OBJECTS = {
    "lpe_detection",
    "glyph_layer_boundary",
}

REQUIRED_DECISION_LABELS = {
    "keep_for_review",
    "revise_before_run",
    "reject_as_overclaim",
    "blocked_missing_authority",
}

FORBIDDEN_TEXT = [
    "agents were run",
    "agent run completed",
    "model result",
    "benchmark result",
    "paper-ready",
    "submission-ready",
    "public release approved",
    "source-observed 27/216",
    "proves layer promotion error is solved",
    "dependency installed",
    "kaggle credentials",
]

REQUIRED_MARKDOWN_PHRASES = [
    "no agents are run",
    "no dependency installation",
    "no model/api call",
    "agent_evaluation_design_not_research_result",
    "keep/reject",
    "what this teaches oroma",
    "mlagentbench",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        manifest = read_json(MANIFEST_PATH)
        missing_fields = sorted(REQUIRED_MANIFEST_FIELDS - manifest.keys())
        if missing_fields:
            errors.append(f"manifest missing fields: {missing_fields}")

        if manifest.get("experiment_id") != "EXP-FRONTIER-009":
            errors.append("manifest experiment_id must be EXP-FRONTIER-009")
        if manifest.get("atlas_id") != "ATLAS-0052":
            errors.append("manifest atlas_id must be ATLAS-0052")
        if manifest.get("status") != "MLAGENTBENCH_KEEP_REJECT_DESIGN_READY_NO_AGENT_RUN":
            errors.append("manifest status must be design-ready with no agent run")
        if manifest.get("claim_ceiling") != "agent_evaluation_design_not_research_result":
            errors.append("manifest claim ceiling must block research-result claims")
        if set(manifest.get("primary_sources", [])) != PRIMARY_SOURCES:
            errors.append("manifest primary_sources must exactly match MLAgentBench primary sources")
        if manifest.get("external_actions_taken") != []:
            errors.append("manifest external_actions_taken must be empty")
        for field in ["dependencies_installed", "agents_run", "model_or_api_run", "private_data_downloaded"]:
            if manifest.get(field) is not False:
                errors.append(f"{field} must be false")
        if set(manifest.get("decision_labels", [])) != REQUIRED_DECISION_LABELS:
            errors.append("manifest decision_labels must match required label set")

        local_inputs = set(manifest.get("local_inputs", []))
        for required in [
            "instruments/lpe_bench/manifest.json",
            "research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl",
            "experiments/EXP-FRONTIER-002-layer-promotion-expanded/data/lpe_cases.jsonl",
        ]:
            if required not in local_inputs:
                errors.append(f"manifest missing local input: {required}")
            elif not (ROOT / required).exists():
                errors.append(f"manifest local input does not exist: {required}")

        blockers = set(manifest.get("blocking_gates", []))
        for blocker in [
            "human/domain review of task cards",
            "explicit agent-run approval",
            "model/API key approval",
            "no private or restricted source data",
            "claim ceiling accepted",
        ]:
            if blocker not in blockers:
                errors.append(f"manifest missing blocker: {blocker}")

        tasks = read_csv(TASKS_PATH)
        if manifest.get("task_card_count") != len(tasks):
            errors.append("manifest task_card_count must match task_cards.csv")
        if len(tasks) < 4:
            errors.append("task_cards.csv must include at least four tasks")

        seen_objects: set[str] = set()
        seen_labels: set[str] = set()
        for row in tasks:
            task_id = row.get("task_id", "")
            missing_task_fields = sorted(REQUIRED_TASK_FIELDS - set(row.keys()))
            if missing_task_fields:
                errors.append(f"{task_id}: missing task fields {missing_task_fields}")
                continue
            seen_objects.add(row.get("research_object", ""))
            for label in [row.get("keep_condition", ""), row.get("reject_condition", "")]:
                for decision_label in REQUIRED_DECISION_LABELS:
                    if decision_label in label:
                        seen_labels.add(decision_label)
            if row.get("claim_ceiling") != "agent_evaluation_design_not_research_result":
                errors.append(f"{task_id}: claim ceiling must block research-result claims")
            if "run agent" in row.get("allowed_actions", "").lower():
                errors.append(f"{task_id}: allowed_actions must not include running agents")
            if not row.get("negative_control"):
                errors.append(f"{task_id}: negative_control is required")

        if not REQUIRED_RESEARCH_OBJECTS.issubset(seen_objects):
            errors.append("task cards must cover LPE detection and glyph layer boundary")
        if not REQUIRED_DECISION_LABELS.issubset(seen_labels):
            errors.append("task cards must exercise all decision labels")

        schema = read_json(DECISION_SCHEMA_PATH)
        if schema.get("schema_id") != "MLAGENTBENCH-KEEP-REJECT-DECISION-SCHEMA-001":
            errors.append("decision schema id is invalid")
        if set(schema.get("allowed_decisions", [])) != REQUIRED_DECISION_LABELS:
            errors.append("decision schema must define all required decisions")
        if schema.get("claim_ceiling") != "agent_evaluation_design_not_research_result":
            errors.append("decision schema must preserve claim ceiling")

        markdown = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in [DESIGN_PATH, NEGATIVE_CONTROL_PATH]
        )
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in markdown:
                errors.append(f"design markdown missing phrase: {phrase}")

        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in REQUIRED_FILES)
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in combined:
                errors.append(f"forbidden MLAgentBench design text: {forbidden}")
        if re.search(r"\bready_for_human_arxiv_review\b|\bsubmission_ready\b|\bpublic_release_ready\b", combined):
            errors.append("forbidden readiness token in MLAgentBench design packet")

    if errors:
        print("MLAGENTBENCH_KEEP_REJECT_DESIGN_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("MLAGENTBENCH_KEEP_REJECT_DESIGN_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
