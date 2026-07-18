from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-FRONTIER-007-inspect-ai-lpe-port"
GATE_DIR = EXP_DIR / "execution_gate"
DECISION_PATH = GATE_DIR / "execution_decision.json"
CHECKLIST_PATH = GATE_DIR / "approval_checklist.csv"
RUNBOOK_PATH = GATE_DIR / "execution_runbook.md"
RISK_PATH = GATE_DIR / "risk_register.md"
OUTPUT_POLICY_PATH = GATE_DIR / "output_handling_policy.md"
BASE_VALIDATOR = ROOT / "scripts" / "validate_inspect_lpe_port.py"

REQUIRED_FILES = [
    DECISION_PATH,
    CHECKLIST_PATH,
    RUNBOOK_PATH,
    RISK_PATH,
    OUTPUT_POLICY_PATH,
]

REQUIRED_DECISION_FIELDS = {
    "experiment_id",
    "decision_status",
    "approval_scope",
    "approved_actions",
    "forbidden_actions",
    "claim_ceiling",
    "required_before_execution",
    "exact_next_action",
}

REQUIRED_CHECKLIST_FIELDS = {
    "gate_id",
    "gate",
    "required_state",
    "current_state",
    "evidence_path",
    "blocks_execution",
}

REQUIRED_GATE_IDS = {
    "DEP-001": "explicit dependency approval",
    "KEY-001": "model/API key approval",
    "DATA-001": "no private or restricted source data",
    "LABEL-001": "human/domain review of seed labels",
    "SECRET-001": "no secrets in repo or logs",
    "OUTPUT-001": "output claim ceiling accepted",
    "SANDBOX-001": "execution isolation reviewed",
}

FORBIDDEN_TEXT = [
    "decision_status\": \"approved",
    "approved_actions\": [\"install",
    "paper-ready",
    "submission-ready",
    "frontier-ready",
    "public release approved",
    "source-observed 27/216",
    "model result proves",
]

REQUIRED_MARKDOWN_PHRASES = [
    "no dependency installation",
    "no model/api call",
    "no private or restricted source data",
    "no paper or public-release claim",
    "eval_harness_relevance_not_model_claim",
    "human/domain review",
]


def main() -> int:
    errors: list[str] = []

    if not BASE_VALIDATOR.exists():
        errors.append("missing base Inspect port validator")

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT).as_posix()}")

    if not errors:
        decision = json.loads(DECISION_PATH.read_text(encoding="utf-8"))
        missing_decision = sorted(REQUIRED_DECISION_FIELDS - decision.keys())
        if missing_decision:
            errors.append(f"decision missing fields: {missing_decision}")

        if decision.get("experiment_id") != "EXP-FRONTIER-007":
            errors.append("decision experiment_id must be EXP-FRONTIER-007")
        if decision.get("decision_status") != "pending_user_approval":
            errors.append("execution decision must remain pending_user_approval")
        if decision.get("claim_ceiling") != "eval_harness_relevance_not_model_claim":
            errors.append("execution gate must preserve eval harness claim ceiling")
        if decision.get("approved_actions") != []:
            errors.append("execution gate must not pre-approve actions")

        forbidden_actions = set(decision.get("forbidden_actions", []))
        for action in [
            "dependency installation",
            "model/API call",
            "external submission",
            "publication PDF generation",
            "readiness claim",
            "private data download",
        ]:
            if action not in forbidden_actions:
                errors.append(f"decision missing forbidden action: {action}")

        required_before = set(decision.get("required_before_execution", []))
        for gate in REQUIRED_GATE_IDS.values():
            if gate not in required_before:
                errors.append(f"decision missing required gate: {gate}")

        with CHECKLIST_PATH.open("r", encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if not rows:
            errors.append("approval checklist must contain rows")
        else:
            missing_fields = sorted(REQUIRED_CHECKLIST_FIELDS - set(rows[0].keys()))
            if missing_fields:
                errors.append(f"approval checklist missing fields: {missing_fields}")
            seen = {row.get("gate_id", ""): row for row in rows}
            for gate_id, gate_name in REQUIRED_GATE_IDS.items():
                row = seen.get(gate_id)
                if row is None:
                    errors.append(f"approval checklist missing {gate_id}")
                    continue
                if row.get("gate") != gate_name:
                    errors.append(f"{gate_id}: expected gate {gate_name}")
                if row.get("current_state") != "pending":
                    errors.append(f"{gate_id}: current_state must remain pending")
                if row.get("blocks_execution") != "true":
                    errors.append(f"{gate_id}: must block execution")

        combined_text = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in [RUNBOOK_PATH, RISK_PATH, OUTPUT_POLICY_PATH]
        )
        for phrase in REQUIRED_MARKDOWN_PHRASES:
            if phrase not in combined_text:
                errors.append(f"gate docs missing phrase: {phrase}")

        all_text = "\n".join(
            path.read_text(encoding="utf-8").lower()
            for path in REQUIRED_FILES
        )
        for forbidden in FORBIDDEN_TEXT:
            if forbidden in all_text:
                errors.append(f"forbidden execution-gate text: {forbidden}")

    if errors:
        print("INSPECT_EXECUTION_GATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("INSPECT_EXECUTION_GATE_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
