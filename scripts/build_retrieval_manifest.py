from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import research_reset_audit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "spine" / "retrieval_manifest.yaml"
EVENT_INDEX = ROOT / "spine" / "events" / "artifact_event_index.json"

DANGEROUS_FLAGS = {
    "retrieval_risk",
    "stale_count_claim",
    "unqualified_overclaim_language",
}

RESET_SAFE_PATHS = {
    "README.md",
    "research/pagc/PAGC_RESET.md",
    "research/pagc/DERIVED_HYPOTHESIS_CHARTER.md",
    "research/pagc/primary_sources/nwagu_aneke/README.md",
    "research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md",
    "research/pagc/primary_sources/nwagu_aneke/SOURCE_AUDIT.md",
    "research/pagc/nwagu_aneke/NWAGU_ANEKE_RESEARCH_MAP.md",
}

KNOWN_SUPERSEDERS = {
    "research/pagc/INDEX.md": "research/pagc/PAGC_RESET.md",
    "research/pagc/WIKI.md": "research/pagc/PAGC_RESET.md",
    "research/pagc/paper/autoreason_draft.md": "research/pagc/PAGC_RESET.md",
    "research/pagc/paper/autoreason_draft_v2.md": "research/pagc/PAGC_RESET.md",
    "research/pagc/paper/autoreason_draft_v3.md": "research/pagc/PAGC_RESET.md",
    "quarantine/legacy_prompt_driven/run_autoreason.py": "research/pagc/PAGC_RESET.md",
}


def q(value: Any) -> str:
    if value is None:
        return "null"
    text = str(value)
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def artifact_status(artifact: research_reset_audit.Artifact) -> str:
    if artifact.path in RESET_SAFE_PATHS:
        return "current"
    if artifact.classification == "stale":
        return "stale"
    if artifact.classification == "do-not-cite":
        return "do-not-cite"
    if artifact.classification == "quarantine-candidate":
        return "quarantine-candidate"
    if artifact.classification == "generated":
        return "generated"
    if artifact.classification == "unknown-needs-review":
        return "unknown-needs-review"
    if DANGEROUS_FLAGS.intersection(artifact.flags):
        return "review-required"
    return "current"


def artifact_authority(artifact: research_reset_audit.Artifact) -> str:
    if artifact.classification == "canonical":
        return "canonical-control"
    if artifact.classification == "source":
        return "source-evidence"
    if artifact.classification == "working":
        return "working-memory"
    if artifact.classification == "generated":
        return "generated-projection"
    if artifact.classification == "do-not-cite":
        return "historical-do-not-cite"
    if artifact.classification == "quarantine-candidate":
        return "forensic-only"
    if artifact.classification == "stale":
        return "superseded"
    return "unknown"


def retrieval_profiles(artifact: research_reset_audit.Artifact) -> list[str]:
    profiles = ["forensic"]
    status = artifact_status(artifact)
    safe = status == "current" or artifact.path in RESET_SAFE_PATHS
    if artifact.classification in {"source", "canonical"} and safe:
        profiles.insert(0, "investigation")
        profiles.insert(0, "canonical")
    elif artifact.classification == "working" and safe:
        profiles.insert(0, "investigation")
    return profiles


def superseded_by(artifact: research_reset_audit.Artifact) -> str | None:
    if artifact.path in KNOWN_SUPERSEDERS:
        return KNOWN_SUPERSEDERS[artifact.path]
    if artifact.classification in {"stale", "do-not-cite"} and artifact.path.startswith("research/pagc/"):
        return "research/pagc/PAGC_RESET.md"
    return None


def load_event_index(path: Path = EVENT_INDEX) -> dict[str, list[dict[str, str]]]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(data, dict):
        return {}
    return data


def source_event_id(path: str, event_index: dict[str, list[dict[str, str]]]) -> str | None:
    events = event_index.get(path) or []
    if not events:
        return None
    last = events[-1]
    event_id = last.get("event_id")
    return event_id if event_id else None


def build_manifest_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    event_index = load_event_index()
    artifacts = research_reset_audit.gather_artifacts()
    for artifact in sorted(artifacts, key=lambda item: item.path.lower()):
        rows.append(
            {
                "path": artifact.path,
                "artifact_class": artifact.classification,
                "authority": artifact_authority(artifact),
                "status": artifact_status(artifact),
                "retrieval_profiles": retrieval_profiles(artifact),
                "superseded_by": superseded_by(artifact),
                "source_event_id": source_event_id(artifact.path, event_index),
                "content_hash": f"sha256:{artifact.sha256}",
                "last_reviewed_at": None,
                "flags": artifact.flags,
            }
        )
    return rows


def render_manifest(rows: list[dict[str, Any]]) -> str:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "# Generated by scripts/build_retrieval_manifest.py. Do not hand-edit without regenerating.",
        "version: 1",
        f"generated_at: {q(generated_at)}",
        "generated_from: \"research_reset_audit.md + spine/events/artifact_event_index.json\"",
        "default_profile: \"canonical\"",
        "profiles:",
        "  canonical:",
        "    allow_classes:",
        "      - \"source\"",
        "      - \"canonical\"",
        "    deny_classes:",
        "      - \"working\"",
        "      - \"generated\"",
        "      - \"stale\"",
        "      - \"do-not-cite\"",
        "      - \"quarantine-candidate\"",
        "      - \"unknown-needs-review\"",
        "  investigation:",
        "    allow_classes:",
        "      - \"source\"",
        "      - \"canonical\"",
        "      - \"working\"",
        "    require_explicit_working_paths: true",
        "    deny_classes:",
        "      - \"generated\"",
        "      - \"stale\"",
        "      - \"do-not-cite\"",
        "      - \"quarantine-candidate\"",
        "      - \"unknown-needs-review\"",
        "  forensic:",
        "    allow_classes:",
        "      - \"*\"",
        "    inject_status_warning: true",
        "    forbid_claim_promotion: true",
        "artifacts:",
    ]
    for row in rows:
        lines.append(f"  - path: {q(row['path'])}")
        lines.append(f"    artifact_class: {q(row['artifact_class'])}")
        lines.append(f"    authority: {q(row['authority'])}")
        lines.append(f"    status: {q(row['status'])}")
        lines.append("    retrieval_profiles:")
        for profile in row["retrieval_profiles"]:
            lines.append(f"      - {q(profile)}")
        lines.append(f"    superseded_by: {q(row['superseded_by'])}")
        lines.append(f"    source_event_id: {q(row['source_event_id'])}")
        lines.append(f"    content_hash: {q(row['content_hash'])}")
        lines.append(f"    last_reviewed_at: {q(row['last_reviewed_at'])}")
        lines.append("    flags:")
        if row["flags"]:
            for flag in row["flags"]:
                lines.append(f"      - {q(flag)}")
        else:
            lines.append("      []")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build retrieval firewall manifest from reset audit classifications.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output YAML path.")
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = build_manifest_rows()
    output.write_text(render_manifest(rows), encoding="utf-8")
    print(f"wrote {output}")
    print(f"artifacts={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
