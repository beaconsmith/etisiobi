"""Read-only decision reversibility and evidence-change audit for Etisiobi.

Never promotes, revokes, or changes a research claim. Python 3.10+ stdlib only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "decisions" / "decision_log.jsonl"


def local_path(reference: str) -> str | None:
    """Return safe repo-relative evidence path, or None for non-local refs."""
    value = reference.strip().replace("\\", "/")
    if not value or value.startswith(("/", "~")) or "://" in value:
        return None
    parts = PurePosixPath(value).parts
    if any(part in {"..", "."} for part in parts) or ":" in parts[0]:
        return None
    # A prose assertion, or a citation to a conversation, is not a repository path.
    if any(" " in part for part in parts) or len(parts) == 0:
        return None
    return PurePosixPath(*parts).as_posix()


def intersects(reference: str, changed: str) -> bool:
    """A changed artifact can match a cited file or a cited directory."""
    ref = reference.rstrip("/")
    chg = changed.rstrip("/")
    return ref == chg or ref.startswith(chg + "/") or chg.startswith(ref + "/")


def load_records(path: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {line_no}: {exc.msg}") from exc
        if not isinstance(record, dict) or not isinstance(record.get("decision_id"), str):
            raise ValueError(f"invalid decision at line {line_no}: decision_id required")
        decision_id = record["decision_id"]
        if decision_id in seen:
            raise ValueError(f"duplicate decision_id at line {line_no}: {decision_id}")
        seen.add(decision_id)
        result.append(record)
    return result


def audit(records: list[dict[str, Any]], root: Path, changed_paths: list[str]) -> dict[str, Any]:
    clean_changes: list[str] = []
    for item in changed_paths:
        path = local_path(item)
        if path is None:
            raise ValueError(f"invalid changed path: {item!r}")
        clean_changes.append(path)
    out: list[dict[str, Any]] = []
    for record in records:
        warnings: list[dict[str, str]] = []
        evidence = record.get("evidence", [])
        if not isinstance(evidence, list):
            warnings.append({"code": "invalid_evidence_list", "detail": "evidence must be an array"})
            evidence = []
        paths: list[str] = []
        for ref in evidence:
            if not isinstance(ref, str):
                warnings.append({"code": "non_string_evidence", "detail": str(ref)})
                continue
            path = local_path(ref)
            if path is None:
                warnings.append({"code": "unverifiable_reference", "detail": ref})
            else:
                paths.append(path)
                if not (root / path).exists():
                    warnings.append({"code": "missing_local_evidence", "detail": path})
        if not str(record.get("reversal_condition", "")).strip():
            warnings.append({"code": "missing_reversal_condition", "detail": "No recorded trigger to reconsider this decision"})
        if not str(record.get("risk", "")).strip():
            warnings.append({"code": "missing_risk", "detail": "No explicit risk recorded"})
        matched = sorted({change for change in clean_changes for ref in paths if intersects(ref, change)})
        out.append({
            "decision_id": record["decision_id"],
            "scope": record.get("scope", ""),
            "status": record.get("status", ""),
            "affected_by_changes": matched,
            "review_required": bool(matched),
            "warnings": warnings,
        })
    return {
        "report_type": "etisiobi_epistemic_tripwire_v1",
        "mode": "read_only_no_automatic_promotion_or_revocation",
        "changed_paths": sorted(set(clean_changes)),
        "decisions_scanned": len(out),
        "affected_decisions": sum(1 for row in out if row["review_required"]),
        "decisions_with_warnings": sum(1 for row in out if row["warnings"]),
        "decisions": out,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--changed", action="append", default=[], metavar="REPO_PATH")
    parser.add_argument("--changed-file-list", type=Path, help="newline-delimited repo-relative changed paths")
    args = parser.parse_args(argv)
    changes = list(args.changed)
    if args.changed_file_list:
        changes += [x for x in args.changed_file_list.read_text(encoding="utf-8").splitlines() if x.strip()]
    try:
        report = audit(load_records(args.ledger), args.root, changes)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
