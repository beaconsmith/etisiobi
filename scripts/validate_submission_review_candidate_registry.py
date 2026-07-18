from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research_runs" / "journal_submission_readiness" / "candidate_registry.json"

TARGET = 10
ALLOWED_STATUS = "SUBMISSION_REVIEW_CANDIDATE_HUMAN_SIGNOFF_BLOCKED"
REQUIRED_KEYS = {
    "article_id",
    "title",
    "status",
    "target_venue",
    "independent_contribution",
    "reproducible_evidence_package",
    "target_venue_fit",
    "review_team_trace",
    "signoff_packet",
    "remaining_blockers",
}
HUMAN_SIGNOFF_TERMS = (
    "human",
    "author",
    "source",
    "rights",
    "authority",
    "apc",
    "funding",
    "waiver",
    "competing-interest",
    "ai-assistance",
    "submission package approval",
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_candidate(candidate: dict) -> list[str]:
    errors: list[str] = []
    article_id = candidate.get("article_id", "<missing>")

    missing = sorted(REQUIRED_KEYS - set(candidate))
    if missing:
        errors.append(f"{article_id}: missing keys {missing}")

    if candidate.get("status") != ALLOWED_STATUS:
        errors.append(f"{article_id}: status must be {ALLOWED_STATUS}")

    for key in (
        "reproducible_evidence_package",
        "target_venue_fit",
        "review_team_trace",
        "signoff_packet",
    ):
        rel_path = candidate.get(key)
        if not rel_path:
            continue
        if not (ROOT / rel_path).exists():
            errors.append(f"{article_id}: {key} path missing: {rel_path}")

    blockers = candidate.get("remaining_blockers", [])
    if not isinstance(blockers, list) or not blockers:
        errors.append(f"{article_id}: remaining_blockers must be a non-empty list")
    else:
        for blocker in blockers:
            lowered = str(blocker).lower()
            if not any(term in lowered for term in HUMAN_SIGNOFF_TERMS):
                errors.append(f"{article_id}: non-human-signoff blocker remains: {blocker}")

    for key in ("target_venue", "independent_contribution"):
        if len(str(candidate.get(key, "")).split()) < 4:
            errors.append(f"{article_id}: {key} is too thin")

    return errors


def main() -> int:
    errors: list[str] = []
    if not REGISTRY.exists():
        print("SUBMISSION_REVIEW_CANDIDATE_REGISTRY_INVALID")
        print(f"- missing {REGISTRY.relative_to(ROOT).as_posix()}")
        return 1

    registry = load_json(REGISTRY)
    if registry.get("target_count") != TARGET:
        errors.append("target_count must be 10")
    candidates = registry.get("candidates", [])
    if not isinstance(candidates, list):
        errors.append("candidates must be a list")
        candidates = []
    if registry.get("submission_review_candidate_count") != len(candidates):
        errors.append("submission_review_candidate_count must equal candidates length")
    if len(candidates) > TARGET:
        errors.append("candidate count cannot exceed target")
    if len(candidates) == TARGET and registry.get("status") != "TEN_CANDIDATE_GOAL_MET_HUMAN_SIGNOFF_BLOCKED":
        errors.append("registry status must mark the goal met when 10 candidates exist")
    if len(candidates) < TARGET and registry.get("status") != "TEN_CANDIDATE_GOAL_IN_PROGRESS":
        errors.append("registry status must remain TEN_CANDIDATE_GOAL_IN_PROGRESS until 10 candidates exist")

    seen: set[str] = set()
    for candidate in candidates:
        article_id = str(candidate.get("article_id", ""))
        if article_id in seen:
            errors.append(f"duplicate candidate: {article_id}")
        seen.add(article_id)
        errors.extend(validate_candidate(candidate))

    queue = registry.get("next_candidate_queue", [])
    if len(candidates) < TARGET and not queue:
        errors.append("next_candidate_queue must be non-empty until target is met")

    if errors:
        print("SUBMISSION_REVIEW_CANDIDATE_REGISTRY_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("SUBMISSION_REVIEW_CANDIDATE_REGISTRY_VALID")
    print(f"candidates={len(candidates)}/{TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
