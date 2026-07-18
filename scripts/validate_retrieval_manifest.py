from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "spine" / "retrieval_manifest.yaml"
REQUIRED_FIELDS = {
    "path",
    "artifact_class",
    "authority",
    "status",
    "retrieval_profiles",
    "superseded_by",
    "source_event_id",
    "content_hash",
    "last_reviewed_at",
}

FORBIDDEN_CANONICAL_CLASSES = {
    "working",
    "generated",
    "stale",
    "do-not-cite",
    "quarantine-candidate",
    "unknown-needs-review",
}


def unquote(value: str) -> str | None:
    value = value.strip()
    if value == "null":
        return None
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


def load_manifest_artifacts(path: Path = DEFAULT_MANIFEST) -> dict[str, dict[str, Any]]:
    artifacts: dict[str, dict[str, Any]] = {}
    current: dict[str, Any] | None = None
    current_list: str | None = None
    in_artifacts = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line == "artifacts:":
            in_artifacts = True
            current_list = None
            continue
        if not in_artifacts:
            continue
        match = re.match(r"^  - path: (.+)$", line)
        if match:
            if current and current.get("path"):
                artifacts[current["path"]] = current
            current = {"path": unquote(match.group(1)), "retrieval_profiles": [], "flags": []}
            current_list = None
            continue
        if current is None:
            continue
        field_match = re.match(r"^    ([a-z_]+):(?: (.*))?$", line)
        if field_match:
            key, value = field_match.groups()
            if value is None:
                current_list = key
                if key not in current:
                    current[key] = []
            else:
                current[key] = unquote(value)
                current_list = None
            continue
        list_match = re.match(r"^      - (.+)$", line)
        if list_match and current_list:
            current.setdefault(current_list, []).append(unquote(list_match.group(1)))
    if current and current.get("path"):
        artifacts[current["path"]] = current
    return artifacts


def validate_manifest(path: Path = DEFAULT_MANIFEST) -> tuple[list[str], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing manifest: {path}"], {}
    text = path.read_text(encoding="utf-8")
    for required in (
        'default_profile: "canonical"',
        "profiles:",
        "  canonical:",
        "  investigation:",
        "  forensic:",
        "forbid_claim_promotion: true",
    ):
        if required not in text:
            errors.append(f"missing required profile marker: {required}")
    artifacts = load_manifest_artifacts(path)
    if not artifacts:
        errors.append("manifest contains no artifacts")
    for artifact_path, artifact in artifacts.items():
        missing = REQUIRED_FIELDS - artifact.keys()
        if missing:
            errors.append(f"{artifact_path}: missing fields {sorted(missing)}")
        profiles = set(artifact.get("retrieval_profiles") or [])
        artifact_class = artifact.get("artifact_class")
        if "forensic" not in profiles:
            errors.append(f"{artifact_path}: forensic profile is mandatory")
        if artifact_class in FORBIDDEN_CANONICAL_CLASSES and "canonical" in profiles:
            errors.append(f"{artifact_path}: forbidden class is canonical-retrievable")
        if artifact_class in {"generated", "stale", "do-not-cite", "quarantine-candidate", "unknown-needs-review"} and "investigation" in profiles:
            errors.append(f"{artifact_path}: forbidden class is investigation-retrievable")
        if artifact.get("status") in {"stale", "do-not-cite", "quarantine-candidate", "review-required"} and "canonical" in profiles:
            errors.append(f"{artifact_path}: unsafe status is canonical-retrievable")
        content_hash = artifact.get("content_hash") or ""
        if not isinstance(content_hash, str) or not content_hash.startswith("sha256:"):
            errors.append(f"{artifact_path}: content_hash must start with sha256:")
    return errors, artifacts


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate retrieval firewall manifest.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="Manifest path.")
    args = parser.parse_args()
    manifest = Path(args.manifest)
    if not manifest.is_absolute():
        manifest = ROOT / manifest
    errors, artifacts = validate_manifest(manifest)
    if errors:
        print("RETRIEVAL_MANIFEST_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        if len(errors) > 200:
            print(f"- ... {len(errors) - 200} additional errors")
        return 1
    print("RETRIEVAL_MANIFEST_VALID")
    print(f"artifacts={len(artifacts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
