#!/usr/bin/env python3
"""Validate review_team_trace.jsonl files before paper-readiness claims."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

TRACE_NAME = "review_team_trace.jsonl"
REQUIRED_ROLES = {
    "research_lead",
    "domain_postdoc",
    "methods_reviewer",
    "adversarial_impact_reviewer",
    "citation_evidence_reviewer",
    "rights_authority_reviewer",
}
REQUIRED_FIELDS = {
    "role",
    "agent_id",
    "status",
    "summary",
    "files_reviewed",
    "blocking_issues",
    "reviewed_at",
}


def parse_time(value: object) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("reviewed_at must be a non-empty ISO 8601 string")
    normalized = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError("reviewed_at must include a timezone")
    return parsed


def validate(trace: Path) -> list[str]:
    errors: list[str] = []
    latest: dict[str, tuple[datetime, dict[str, object], int]] = {}

    if not trace.is_file():
        return [f"missing trace: {trace}"]

    for line_number, line in enumerate(trace.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(row, dict):
            errors.append(f"line {line_number}: row must be a JSON object")
            continue

        missing = sorted(REQUIRED_FIELDS - row.keys())
        if missing:
            errors.append(f"line {line_number}: missing fields: {', '.join(missing)}")
            continue

        role = row["role"]
        if not isinstance(role, str) or not role.strip():
            errors.append(f"line {line_number}: role must be a non-empty string")
            continue

        try:
            reviewed_at = parse_time(row["reviewed_at"])
        except ValueError as exc:
            errors.append(f"line {line_number}: {exc}")
            continue

        previous = latest.get(role)
        if previous is None or reviewed_at > previous[0]:
            latest[role] = (reviewed_at, row, line_number)

    missing_roles = sorted(REQUIRED_ROLES - latest.keys())
    if missing_roles:
        errors.append(f"missing required roles: {', '.join(missing_roles)}")

    identities: dict[str, list[str]] = {}
    for role in sorted(REQUIRED_ROLES & latest.keys()):
        _, row, line_number = latest[role]
        agent_id = row["agent_id"]
        summary = row["summary"]
        files_reviewed = row["files_reviewed"]
        blocking_issues = row["blocking_issues"]

        if row["status"] != "PASS":
            errors.append(f"{role}: latest status must be PASS (line {line_number})")
        if not isinstance(agent_id, str) or not agent_id.strip():
            errors.append(f"{role}: agent_id must be non-empty (line {line_number})")
        else:
            identities.setdefault(agent_id.strip(), []).append(role)
        if not isinstance(summary, str) or not summary.strip():
            errors.append(f"{role}: summary must be non-empty (line {line_number})")
        if not isinstance(files_reviewed, list) or not files_reviewed:
            errors.append(f"{role}: files_reviewed must be a non-empty list (line {line_number})")
        if not isinstance(blocking_issues, list):
            errors.append(f"{role}: blocking_issues must be a list (line {line_number})")
        elif blocking_issues:
            errors.append(f"{role}: unresolved blocking issues remain (line {line_number})")

    for agent_id, roles in sorted(identities.items()):
        if len(roles) > 1:
            errors.append(
                f"agent_id {agent_id!r} covers multiple required roles: {', '.join(roles)}"
            )

    return errors


def find_traces(targets: list[Path]) -> list[Path]:
    if targets:
        return [target / TRACE_NAME if target.is_dir() else target for target in targets]
    return sorted(Path("research").rglob(TRACE_NAME)) if Path("research").exists() else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", type=Path)
    args = parser.parse_args()

    traces = find_traces(args.targets)
    if not traces:
        print(
            f"No {TRACE_NAME} found. Readiness status: NOT_READY_REVIEW_TEAM_BLOCKED.",
            file=sys.stderr,
        )
        return 2

    failed = False
    for trace in traces:
        errors = validate(trace)
        if errors:
            failed = True
            print(f"[FAIL] {trace}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[PASS] {trace}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
