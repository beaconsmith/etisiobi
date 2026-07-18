from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_retrieval_manifest import DEFAULT_MANIFEST, load_manifest_artifacts, validate_manifest  # noqa: E402


FOUNDATION_SOURCE = "research/pagc/primary_sources/nwagu_aneke/CHART_TRANSCRIPTION.md"
KNOWN_STALE_PAGC = {
    "research/pagc/INDEX.md",
    "research/pagc/paper/autoreason_draft_v3.md",
    "quarantine/legacy_prompt_driven/run_autoreason.py",
}


def canonical_paths() -> set[str]:
    errors, artifacts = validate_manifest(DEFAULT_MANIFEST)
    assert not errors, "\n".join(errors)
    return {
        path
        for path, artifact in artifacts.items()
        if "canonical" in set(artifact.get("retrieval_profiles") or [])
    }


def test_foundation_source_is_canonical_retrievable() -> None:
    paths = canonical_paths()
    assert FOUNDATION_SOURCE in paths


def test_stale_pagc_overclaim_files_are_excluded_from_canonical_retrieval() -> None:
    paths = canonical_paths()
    leaked = sorted(KNOWN_STALE_PAGC.intersection(paths))
    assert not leaked, f"stale PAGC files leaked into canonical retrieval: {leaked}"


def test_canonical_pagc_foundation_query_has_layered_count_not_e6_claim() -> None:
    paths = canonical_paths()
    artifacts = load_manifest_artifacts(DEFAULT_MANIFEST)
    candidate_text = []
    for path in sorted(paths):
        if "pagc" not in path.lower() and "nwagu" not in path.lower():
            continue
        file_path = ROOT / path
        if file_path.suffix.lower() not in {".md", ".txt"} or not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8", errors="replace").lower()
        if any(term in text for term in ("26", "208", "f/v", "27", "216", "foundation")):
            candidate_text.append((path, text))
    joined = "\n".join(text for _, text in candidate_text)
    assert "26" in joined and "8" in joined and "f/v" in joined
    forbidden_positive = [
        "e₆ symmetry claim *(mathematics",
        "pagc is a provably optimal universal compression",
        "universal compression engine underlying",
    ]
    for phrase in forbidden_positive:
        assert phrase not in joined
    assert artifacts[FOUNDATION_SOURCE]["status"] == "current"


if __name__ == "__main__":
    test_foundation_source_is_canonical_retrievable()
    test_stale_pagc_overclaim_files_are_excluded_from_canonical_retrieval()
    test_canonical_pagc_foundation_query_has_layered_count_not_e6_claim()
    print("STALE_PAGC_EXCLUSION_PASS")
