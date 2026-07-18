from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

READY_STATUSES = {
    "READY_FOR_HUMAN_ARXIV_REVIEW",
    "READY_FOR_SUBMISSION",
    "SUBMISSION_READY",
    "READY",
}

REQUIRED_ROLES = (
    "research_lead",
    "domain_postdoc",
    "methods_reviewer",
    "adversarial_impact_reviewer",
    "citation_evidence_reviewer",
    "rights_authority_reviewer",
)

READY_FILE_NAMES = {
    "final_submission_readiness_decision.md",
    "submission_readiness_decision.md",
    "PAPER_STATUS.md",
    "STATUS.md",
    "manifest.json",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_ready_status(path: Path) -> bool:
    text = read_text(path)
    if path.suffix.lower() == ".json":
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return False
        if data.get("submission_ready") is True:
            return True
        status_values = [str(data.get("status", "")), str(data.get("readiness_status", ""))]
        status_values.extend(str(item.get("readiness_status", "")) for item in data.get("articles", []) if isinstance(item, dict))
        return any(value in READY_STATUSES for value in status_values)
    return any(re.search(rf"\b{re.escape(status)}\b", text) for status in READY_STATUSES)


def candidate_ready_files(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "__pycache__", "compile_logs"} for part in path.parts):
            continue
        if path.name in READY_FILE_NAMES and contains_ready_status(path):
            candidates.append(path)
    return candidates


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(read_text(path).splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.as_posix()}:{line_number}: invalid JSONL: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path.as_posix()}:{line_number}: row must be an object")
        rows.append(value)
    return rows


def validate_trace(trace_path: Path, paper_dir: Path) -> list[str]:
    errors: list[str] = []
    try:
        rows = parse_jsonl(trace_path)
    except ValueError as exc:
        return [str(exc)]
    by_role = {str(row.get("role", "")): row for row in rows}
    for role in REQUIRED_ROLES:
        row = by_role.get(role)
        if row is None:
            errors.append(f"{paper_dir.as_posix()}: review_team_trace.jsonl missing role {role}")
            continue
        if row.get("status") != "PASS":
            errors.append(f"{paper_dir.as_posix()}: role {role} status must be PASS")
        if not str(row.get("agent_id", "")).strip():
            errors.append(f"{paper_dir.as_posix()}: role {role} missing agent_id")
        if not str(row.get("summary", "")).strip():
            errors.append(f"{paper_dir.as_posix()}: role {role} missing summary")
        files_reviewed = row.get("files_reviewed", [])
        if not isinstance(files_reviewed, list) or not files_reviewed:
            errors.append(f"{paper_dir.as_posix()}: role {role} must list files_reviewed")
        blocking = row.get("blocking_issues", [])
        if blocking not in ([], None):
            errors.append(f"{paper_dir.as_posix()}: role {role} has blocking_issues")
    return errors


def validate_root(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for ready_file in candidate_ready_files(root):
        paper_dir = ready_file.parent
        trace_path = paper_dir / "review_team_trace.jsonl"
        if not trace_path.exists():
            errors.append(f"{paper_dir.as_posix()}: ready status in {ready_file.name} but missing review_team_trace.jsonl")
            continue
        errors.extend(validate_trace(trace_path, paper_dir))
    return errors


def main() -> int:
    errors = validate_root(ROOT)
    if errors:
        print("REVIEW_TEAM_GATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1
    print("REVIEW_TEAM_GATE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
