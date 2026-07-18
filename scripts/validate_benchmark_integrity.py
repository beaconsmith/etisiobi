from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    ROOT / "research" / "BENCHMARK_INTEGRITY.md",
    ROOT / "research" / "BENCHMARK_WALL_FORENSICS.md",
    ROOT / "research" / "CLAIM_INTEGRITY_LEDGER.md",
]

REGISTRY = ROOT / "research_runs" / "journal_submission_readiness" / "candidate_registry.json"
EXTERNAL_READER_REPORT = (
    ROOT / "research_runs" / "external_reader_legitimacy" / "external_reader_legitimacy_report.json"
)
ARXIV_QUALITY_REPORT = ROOT / "research_runs" / "arxiv_quality_reset" / "arxiv_quality_gate_report.json"
APPROVED_PAPERS_REPORT = ROOT / "research_runs" / "approved_papers_goal" / "approval_status.json"
APPROVED_PAPERS_CURRENT = ROOT / "research_runs" / "approved_papers_goal" / "CURRENT.md"
CONTEXT_CONTAMINATION_REPORT = (
    ROOT / "research_runs" / "context_contamination" / "context_contamination_report.json"
)

READY_RE = re.compile(
    r"\bREADY_FOR_SUBMISSION\b|\bSUBMISSION_READY\b|\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|"
    r"\bIMPACT_JOURNAL_READY\b",
    flags=re.I,
)

REQUIRED_LEDGER_PHRASES = [
    "EXTERNAL_READER_LEGITIMACY_FAIL",
    "1 / 10",
    "TEN_CANDIDATE_GOAL_MET_HUMAN_SIGNOFF_BLOCKED",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict:
    return json.loads(read_text(path))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_required_docs(errors: list[str]) -> None:
    for path in REQUIRED_DOCS:
        if not path.exists():
            errors.append(f"missing benchmark integrity doc: {rel(path)}")

    ledger = ROOT / "research" / "CLAIM_INTEGRITY_LEDGER.md"
    if ledger.exists():
        ledger_text = read_text(ledger)
        for phrase in REQUIRED_LEDGER_PHRASES:
            if phrase not in ledger_text:
                errors.append(f"claim integrity ledger missing phrase: {phrase}")

    wall = ROOT / "research" / "BENCHMARK_WALL_FORENSICS.md"
    if wall.exists():
        wall_text = read_text(wall)
        for phrase in ("Failure Taxonomy", "External Reader Legitimacy", "Exact Next Evidence-Producing Action"):
            if phrase not in wall_text:
                errors.append(f"wall forensics missing section/phrase: {phrase}")


def validate_registry_against_external_reader(errors: list[str]) -> None:
    if not REGISTRY.exists():
        errors.append(f"missing registry: {rel(REGISTRY)}")
        return

    registry = read_json(REGISTRY)
    registry_status = str(registry.get("status", ""))
    external_status = str(registry.get("external_reader_legitimacy_status", ""))

    if external_status == "EXTERNAL_READER_LEGITIMACY_FAIL":
        if READY_RE.search(registry_status):
            errors.append("registry status cannot claim readiness while external-reader legitimacy fails")
        interpretation = str(registry.get("external_reader_legitimacy_interpretation", "")).lower()
        if "must not be represented as journal-ready" not in interpretation:
            errors.append("registry must explicitly block journal-ready interpretation on external-reader failure")

    candidates = registry.get("candidates", [])
    if not isinstance(candidates, list):
        errors.append("registry candidates must be a list")
        return

    for candidate in candidates:
        article_id = str(candidate.get("article_id", "<missing>"))
        status = str(candidate.get("status", ""))
        if READY_RE.search(status):
            errors.append(f"{article_id}: candidate status overclaims readiness")
        blockers = candidate.get("remaining_blockers", [])
        if not blockers:
            errors.append(f"{article_id}: candidate must retain human/sign-off blockers until public release ready")

    if EXTERNAL_READER_REPORT.exists():
        report = read_json(EXTERNAL_READER_REPORT)
        report_status = str(report.get("status", ""))
        passed = int(report.get("passed_count", -1))
        checked = int(report.get("checked_count", -1))
        if external_status and external_status != report_status:
            errors.append("registry external-reader status must match external-reader report status")
        if report_status == "EXTERNAL_READER_LEGITIMACY_FAIL":
            if passed >= checked:
                errors.append("external-reader failure cannot report all articles passed")
            if READY_RE.search(registry_status):
                errors.append("registry cannot claim ready status when external-reader report fails")
    elif external_status:
        errors.append(f"registry references external-reader status but report is missing: {rel(EXTERNAL_READER_REPORT)}")


def validate_arxiv_quality_status(errors: list[str]) -> None:
    if not ARXIV_QUALITY_REPORT.exists():
        return
    report = read_json(ARXIV_QUALITY_REPORT)
    status = str(report.get("status", ""))
    passed = int(report.get("passed_count", -1))
    checked = int(report.get("checked_count", -1))
    if status == "ARXIV_QUALITY_GATE_PASS" and passed != checked:
        errors.append("arXiv quality report cannot say PASS unless all checked articles pass")
    if status == "ARXIV_QUALITY_GATE_PARTIAL" and not (0 < passed < checked):
        errors.append("arXiv quality PARTIAL status requires some but not all checked articles to pass")
    if status == "ARXIV_QUALITY_GATE_FAIL" and passed != 0:
        errors.append("arXiv quality FAIL status cannot have passing articles")


def validate_approved_papers_current(errors: list[str]) -> None:
    if not APPROVED_PAPERS_REPORT.exists() or not APPROVED_PAPERS_CURRENT.exists():
        return
    report = read_json(APPROVED_PAPERS_REPORT)
    current = read_text(APPROVED_PAPERS_CURRENT)
    expected_status = f"Status: `{report.get('status')}`"
    expected_count = f"{report.get('approved_count')} / {report.get('target')}"
    if expected_status not in current:
        errors.append("approved-papers CURRENT.md status does not match approval_status.json")
    if expected_count not in current:
        errors.append("approved-papers CURRENT.md count does not match approval_status.json")
    if "External submission readiness: not claimed here" not in current:
        errors.append("approved-papers CURRENT.md must separate internal approval from external submission readiness")


def validate_context_contamination_status(errors: list[str]) -> None:
    if not CONTEXT_CONTAMINATION_REPORT.exists():
        return

    report = read_json(CONTEXT_CONTAMINATION_REPORT)
    status = str(report.get("status", ""))
    passed = int(report.get("passed_count", -1))
    checked = int(report.get("checked_count", -1))

    if status == "CONTEXT_CONTAMINATION_PASS" and passed != checked:
        errors.append("context-contamination report cannot say PASS unless all checked manuscripts pass")
    if status == "CONTEXT_CONTAMINATION_FAIL" and not (0 <= passed < checked):
        errors.append("context-contamination FAIL status requires fewer passing manuscripts than checked manuscripts")

    if not REGISTRY.exists():
        errors.append(f"context-contamination report exists but registry is missing: {rel(REGISTRY)}")
        return

    registry = read_json(REGISTRY)
    if registry.get("context_contamination_status") != status:
        errors.append("registry context-contamination status must match context-contamination report")
    if registry.get("context_contamination_pass_count") != passed:
        errors.append("registry context-contamination pass count must match context-contamination report")
    if registry.get("context_contamination_checked_count") != checked:
        errors.append("registry context-contamination checked count must match context-contamination report")

    if status == "CONTEXT_CONTAMINATION_FAIL":
        if registry.get("public_journal_candidate_count") != 0:
            errors.append("context-contaminated manuscript set cannot have public journal candidates")
        interpretation = str(registry.get("context_contamination_interpretation", "")).lower()
        if "must not" not in interpretation or "journal" not in interpretation:
            errors.append("registry must explicitly block journal interpretation on context-contamination failure")


def main() -> int:
    errors: list[str] = []
    validate_required_docs(errors)
    validate_registry_against_external_reader(errors)
    validate_arxiv_quality_status(errors)
    validate_approved_papers_current(errors)
    validate_context_contamination_status(errors)

    if errors:
        print("BENCHMARK_INTEGRITY_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("BENCHMARK_INTEGRITY_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
