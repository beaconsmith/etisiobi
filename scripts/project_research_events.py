from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVENT_DIR = ROOT / "spine" / "events"
DEFAULT_EVENTS = EVENT_DIR / "research_events.jsonl"
DEFAULT_STATE_JSON = EVENT_DIR / "current_state.json"
DEFAULT_STATE_MD = EVENT_DIR / "current_state.md"
DEFAULT_ARTIFACT_INDEX = EVENT_DIR / "artifact_event_index.json"

REQUIRED_FIELDS = {
    "event_id",
    "timestamp",
    "event_type",
    "actor",
    "scope",
    "summary",
    "status",
    "authority_basis",
    "evidence",
    "outputs",
    "affects",
}

LOCAL_REFERENCE_FIELDS = ("evidence", "outputs", "affects")
ALLOWED_REFERENCE_PREFIXES = ("conversation:", "external:", "git:", "doi:", "arxiv:", "url:")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def is_local_reference(value: str) -> bool:
    if not value or value.endswith("/"):
        return False
    return not value.startswith(ALLOWED_REFERENCE_PREFIXES)


def load_events(path: Path = DEFAULT_EVENTS) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        event["_line_number"] = line_number
        events.append(event)
    return events


def validate_events(events: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    event_ids = {event.get("event_id") for event in events}
    for event in events:
        event_id = event.get("event_id", f"line:{event.get('_line_number')}")
        missing = REQUIRED_FIELDS - event.keys()
        if missing:
            errors.append(f"{event_id}: missing required fields {sorted(missing)}")
        if event_id in seen_ids:
            errors.append(f"{event_id}: duplicate event_id")
        seen_ids.add(event_id)
        for field in ("evidence", "outputs", "affects"):
            if not isinstance(event.get(field), list):
                errors.append(f"{event_id}: {field} must be an array")
        for superseded in event.get("supersedes_events", []):
            if superseded not in event_ids:
                errors.append(f"{event_id}: supersedes unknown event {superseded}")
        for field in LOCAL_REFERENCE_FIELDS:
            for reference in event.get(field, []):
                if not isinstance(reference, str):
                    errors.append(f"{event_id}: {field} contains non-string reference")
                    continue
                if is_local_reference(reference) and not (ROOT / reference).exists():
                    errors.append(f"{event_id}: {field} local reference does not exist: {reference}")
    return errors


def build_artifact_index(events: list[dict[str, Any]]) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for event in events:
        event_id = event["event_id"]
        for relation in ("evidence", "outputs", "affects", "supersedes_artifacts"):
            for value in event.get(relation, []):
                if value.startswith(ALLOWED_REFERENCE_PREFIXES):
                    continue
                index[value].append(
                    {
                        "event_id": event_id,
                        "relation": relation,
                        "event_type": event["event_type"],
                        "scope": event["scope"],
                        "status": event["status"],
                    }
                )
    return dict(sorted(index.items(), key=lambda item: item[0].lower()))


def project_state(events: list[dict[str, Any]], artifact_index: dict[str, list[dict[str, str]]]) -> dict[str, Any]:
    latest_by_scope: dict[str, dict[str, Any]] = {}
    gates: dict[str, dict[str, Any]] = {}
    blockers: list[dict[str, Any]] = []
    accepted_results: list[dict[str, Any]] = []
    superseded_artifacts: dict[str, str] = {}

    for event in events:
        latest_by_scope[event["scope"]] = {
            "event_id": event["event_id"],
            "timestamp": event["timestamp"],
            "event_type": event["event_type"],
            "summary": event["summary"],
            "status": event["status"],
            "next_action": event.get("next_action", ""),
        }
        if event["event_type"] == "gate_result":
            gates[event["scope"]] = latest_by_scope[event["scope"]]
        if "blocked" in event["status"].lower() or event["event_type"] == "blocker":
            blockers.append(latest_by_scope[event["scope"]])
        if event["event_type"] == "research_result" and event["status"].startswith("accepted"):
            accepted = dict(latest_by_scope[event["scope"]])
            accepted["scope"] = event["scope"]
            accepted_results.append(accepted)
        for artifact in event.get("supersedes_artifacts", []):
            superseded_artifacts[artifact] = event["event_id"]

    return {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "event_count": len(events),
        "last_event_id": events[-1]["event_id"] if events else None,
        "latest_by_scope": latest_by_scope,
        "gate_status": gates,
        "accepted_research_results": accepted_results,
        "blockers": blockers,
        "superseded_artifacts": superseded_artifacts,
        "artifact_event_index_path": rel(DEFAULT_ARTIFACT_INDEX),
        "indexed_artifact_count": len(artifact_index),
    }


def render_state_md(state: dict[str, Any], events: list[dict[str, Any]]) -> str:
    lines: list[str] = [
        "# Etisiobi Current State Projection",
        "",
        "> Generated from `spine/events/research_events.jsonl`. Do not hand-edit this projection.",
        "",
        "## Summary",
        "",
        f"- Generated at: `{state['generated_at']}`",
        f"- Event count: `{state['event_count']}`",
        f"- Last event: `{state['last_event_id']}`",
        f"- Indexed artifacts: `{state['indexed_artifact_count']}`",
        "",
        "## Current Decisions By Scope",
        "",
        "| scope | event | status | summary | next action |",
        "|---|---|---|---|---|",
    ]
    for scope, row in sorted(state["latest_by_scope"].items()):
        lines.append(
            f"| {scope} | {row['event_id']} | {row['status']} | "
            f"{row['summary'].replace('|', '/')} | {row.get('next_action', '').replace('|', '/')} |"
        )
    lines.extend(["", "## Gate Status", "", "| gate | event | status | summary |", "|---|---|---|---|"])
    for scope, row in sorted(state["gate_status"].items()):
        lines.append(f"| {scope} | {row['event_id']} | {row['status']} | {row['summary'].replace('|', '/')} |")
    lines.extend(["", "## Accepted Research Results", "", "| scope | event | status | summary |", "|---|---|---|---|"])
    for row in state["accepted_research_results"]:
        lines.append(f"| {row['scope']} | {row['event_id']} | {row['status']} | {row['summary'].replace('|', '/')} |")
    lines.extend(["", "## Superseded Artifacts", "", "| artifact | superseded by event |", "|---|---|"])
    for artifact, event_id in sorted(state["superseded_artifacts"].items()):
        lines.append(f"| {artifact} | {event_id} |")
    lines.extend(["", "## Event Log", "", "| event | type | scope | status | summary |", "|---|---|---|---|---|"])
    for event in events:
        lines.append(
            f"| {event['event_id']} | {event['event_type']} | {event['scope']} | "
            f"{event['status']} | {event['summary'].replace('|', '/')} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def write_outputs(events_path: Path = DEFAULT_EVENTS) -> tuple[dict[str, Any], list[str]]:
    events = load_events(events_path)
    errors = validate_events(events)
    if errors:
        return {}, errors
    artifact_index = build_artifact_index(events)
    state = project_state(events, artifact_index)
    EVENT_DIR.mkdir(parents=True, exist_ok=True)
    DEFAULT_ARTIFACT_INDEX.write_text(json.dumps(artifact_index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DEFAULT_STATE_JSON.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DEFAULT_STATE_MD.write_text(render_state_md(state, events), encoding="utf-8")
    return state, []


def main() -> int:
    parser = argparse.ArgumentParser(description="Project Etisiobi current state from append-only research events.")
    parser.add_argument("--events", default=str(DEFAULT_EVENTS), help="Event JSONL path.")
    args = parser.parse_args()
    events_path = Path(args.events)
    if not events_path.is_absolute():
        events_path = ROOT / events_path
    state, errors = write_outputs(events_path)
    if errors:
        print("RESEARCH_EVENTS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1
    print("RESEARCH_EVENTS_PROJECTED")
    print(f"events={state['event_count']}")
    print(f"last_event_id={state['last_event_id']}")
    print(f"indexed_artifacts={state['indexed_artifact_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
