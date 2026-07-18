from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port"
GATE_DIR = EXP_DIR / "execution_gate"
REVIEW_DIR = GATE_DIR / "review"
REVIEW_MANIFEST_PATH = REVIEW_DIR / "review_manifest.json"
REVIEW_NOTE_PATH = REVIEW_DIR / "EXECUTION_GATE_REVIEW.md"
DECISION_PATH = GATE_DIR / "execution_decision.json"
CHECKLIST_PATH = GATE_DIR / "approval_checklist.csv"
BASE_VALIDATOR = ROOT / "scripts" / "validate_inspect_execution_gate.py"

READY_RE = re.compile(r"\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|\bSUBMISSION_READY\b|\bPUBLIC_RELEASE_READY\b")

REQUIRED_FIELDS = {
    "review_id",
    "experiment_id",
    "atlas_id",
    "reviewed_at",
    "review_status",
    "decision_status_after_review",
    "recommendation",
    "claim_ceiling",
    "external_actions_taken",
    "dependencies_installed",
    "model_or_api_run",
    "private_data_downloaded",
    "approval_gates_checked",
    "blocking_gates_remaining",
    "forbidden_actions_confirmed",
    "evidence_paths",
    "oroma_learning",
    "exact_next_action",
}

REQUIRED_GATE_IDS = {
    "DEP-001",
    "KEY-001",
    "DATA-001",
    "LABEL-001",
    "SECRET-001",
    "OUTPUT-001",
    "SANDBOX-001",
}

REQUIRED_BLOCKERS = {
    "explicit dependency approval",
    "model/API key approval",
    "no private or restricted source data",
    "human/domain review of seed labels",
    "no secrets in repo or logs",
    "output claim ceiling accepted",
    "execution isolation reviewed",
}

REQUIRED_FORBIDDEN_ACTIONS = {
    "dependency installation",
    "model/API call",
    "external submission",
    "publication PDF generation",
    "readiness claim",
    "private data download",
}

REQUIRED_NOTE_PHRASES = [
    "do not execute",
    "pending_user_approval",
    "no dependency installation",
    "no model/api call",
    "no private or restricted source data",
    "eval_harness_relevance_not_model_claim",
    "not a model result",
    "what this teaches oroma",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []

    for path in [BASE_VALIDATOR, DECISION_PATH, CHECKLIST_PATH, REVIEW_MANIFEST_PATH, REVIEW_NOTE_PATH]:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        review = read_json(REVIEW_MANIFEST_PATH)
        decision = read_json(DECISION_PATH)
        missing = sorted(REQUIRED_FIELDS - review.keys())
        if missing:
            errors.append(f"review manifest missing fields: {missing}")

        if review.get("experiment_id") != "EXP-FRONTIER-007":
            errors.append("review experiment_id must be EXP-FRONTIER-007")
        if review.get("atlas_id") != "ATLAS-0049":
            errors.append("review atlas_id must be ATLAS-0049")
        if review.get("review_status") != "reviewed_keep_pending_do_not_execute":
            errors.append("review_status must keep execution pending and blocked")
        if review.get("decision_status_after_review") != "pending_user_approval":
            errors.append("decision_status_after_review must be pending_user_approval")
        if decision.get("decision_status") != "pending_user_approval":
            errors.append("execution_decision.json must remain pending_user_approval")
        if decision.get("approved_actions") != []:
            errors.append("execution_decision.json must not approve actions")
        if review.get("recommendation") != "do_not_execute_without_explicit_user_or_lab_approval":
            errors.append("recommendation must block execution without explicit approval")
        if review.get("claim_ceiling") != "eval_harness_relevance_not_model_claim":
            errors.append("review must preserve eval harness claim ceiling")

        if review.get("external_actions_taken") != []:
            errors.append("review must record no external actions")
        for field in ["dependencies_installed", "model_or_api_run", "private_data_downloaded"]:
            if review.get(field) is not False:
                errors.append(f"{field} must be false")

        gate_ids = set(review.get("approval_gates_checked", []))
        if not REQUIRED_GATE_IDS.issubset(gate_ids):
            errors.append("review must check every approval gate id")

        blockers = set(review.get("blocking_gates_remaining", []))
        missing_blockers = sorted(REQUIRED_BLOCKERS - blockers)
        if missing_blockers:
            errors.append(f"review missing blocking gates: {missing_blockers}")

        forbidden_actions = set(review.get("forbidden_actions_confirmed", []))
        missing_forbidden = sorted(REQUIRED_FORBIDDEN_ACTIONS - forbidden_actions)
        if missing_forbidden:
            errors.append(f"review missing forbidden actions: {missing_forbidden}")

        for evidence in review.get("evidence_paths", []):
            evidence_path = ROOT / evidence
            if not evidence_path.exists():
                errors.append(f"review evidence path missing: {evidence}")

        next_action = str(review.get("exact_next_action", "")).lower()
        if "explicit user/lab approval or rejection" not in next_action:
            errors.append("exact_next_action must ask for explicit user/lab approval or rejection")
        if "model" in next_action and "without" not in next_action:
            errors.append("exact_next_action must not imply a model run")

        note = REVIEW_NOTE_PATH.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_NOTE_PHRASES:
            if phrase not in note:
                errors.append(f"review note missing phrase: {phrase}")
        if READY_RE.search(note) or READY_RE.search(json.dumps(review, ensure_ascii=False)):
            errors.append("review packet contains forbidden readiness language")

    if errors:
        print("INSPECT_EXECUTION_GATE_REVIEW_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("INSPECT_EXECUTION_GATE_REVIEW_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
