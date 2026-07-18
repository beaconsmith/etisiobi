from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET_DIR = ROOT / "research_runs" / "human_source_rights_review"
INDEX = PACKET_DIR / "packet_index.json"

FORBIDDEN_READY_RE = re.compile(
    r"\bREADY_FOR_SUBMISSION\b|\bSUBMISSION_READY\b|\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|"
    r"\bIMPACT_JOURNAL_READY\b|\bPUBLIC_JOURNAL_MANUSCRIPT_CANDIDATE\b",
    flags=re.I,
)

REQUIRED_ARTICLES = {"ARTICLE-NA-002", "ARTICLE-NA-006", "ARTICLE-NA-010"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    errors: list[str] = []
    current = PACKET_DIR / "CURRENT.md"
    if not current.exists():
        errors.append(f"missing {rel(current)}")
    if not INDEX.exists():
        errors.append(f"missing {rel(INDEX)}")
    if errors:
        print("HUMAN_SOURCE_RIGHTS_PACKETS_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    index = read_json(INDEX)
    if index.get("status") != "HUMAN_SOURCE_RIGHTS_REVIEW_PACKETS_PREPARED_PUBLIC_RELEASE_BLOCKED":
        errors.append("packet index status must remain public-release blocked")
    if index.get("public_journal_candidate_count") != 0:
        errors.append("human source/rights packet index cannot contain public journal candidates")
    if index.get("public_preprint_candidate_count") != 3:
        errors.append("human source/rights packet index must record three public preprint candidates")

    packets = index.get("packets", [])
    if not isinstance(packets, list):
        errors.append("packet index packets must be a list")
        packets = []

    seen = {str(packet.get("article_id", "")) for packet in packets if isinstance(packet, dict)}
    if seen != REQUIRED_ARTICLES:
        errors.append("packet index must cover ARTICLE-NA-002, ARTICLE-NA-006, and ARTICLE-NA-010 exactly")

    paths = [current]
    for packet in packets:
        if not isinstance(packet, dict):
            errors.append("packet index row must be an object")
            continue
        article_id = str(packet.get("article_id", ""))
        path = ROOT / str(packet.get("packet", ""))
        if not path.exists():
            errors.append(f"{article_id}: missing packet file {rel(path)}")
            continue
        paths.append(path)
        if packet.get("current_release_class") != "PUBLIC_PREPRINT_CANDIDATE":
            errors.append(f"{article_id}: current release class must be PUBLIC_PREPRINT_CANDIDATE")
        if packet.get("decision") != "PUBLIC_PREPRINT_CANDIDATE_HUMAN_REVIEW_REQUIRED":
            errors.append(f"{article_id}: decision must require human review")

    for path in paths:
        text = read_text(path)
        allowed_contexts = [
            "Forbidden current statuses:",
            "forbidden_current_statuses",
            "not arXiv-ready",
            "not submission-ready",
            "not impact-journal-ready",
            "not public journal-manuscript candidates",
        ]
        if FORBIDDEN_READY_RE.search(text) and not any(context in text for context in allowed_contexts):
            errors.append(f"{rel(path)} contains an unsupported readiness phrase")
        for phrase in (
            "Human Decisions Required",
            "Do not promote beyond this status without signed human decisions",
        ):
            if path.name.startswith("ARTICLE-NA") and phrase not in text:
                errors.append(f"{rel(path)} missing phrase: {phrase}")

    if errors:
        print("HUMAN_SOURCE_RIGHTS_PACKETS_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("HUMAN_SOURCE_RIGHTS_PACKETS_VALID")
    print("packets=3")
    print("public_journal_candidates=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
