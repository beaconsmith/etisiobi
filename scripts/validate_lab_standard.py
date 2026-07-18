from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

READY_RE = re.compile(r"\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|\bREADY_FOR_SUBMISSION\b|\bSUBMISSION_READY\b")

REQUIRED_DOCS = [
    ROOT / "research" / "A_PLUS_LAB_STANDARD.md",
    ROOT / "research" / "BENCHMARK_INTEGRITY.md",
    ROOT / "research" / "BENCHMARK_WALL_FORENSICS.md",
    ROOT / "research" / "CLAIM_INTEGRITY_LEDGER.md",
    ROOT / "research" / "LAB_STAGE_GATES.json",
    ROOT / "research" / "LAB_STANDARD_AUDIT.md",
]

STALE_READY_SURFACES = [
    ROOT / "obsidian_vault" / "08_Arxiv_Readiness.md",
    ROOT / "obsidian_vault" / "06_Paper_Map.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_json(path: Path) -> dict:
    return json.loads(read_text(path))


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_DOCS:
        if not path.exists():
            errors.append(f"missing required lab standard doc: {path.relative_to(ROOT).as_posix()}")

    gates_path = ROOT / "research" / "LAB_STAGE_GATES.json"
    if gates_path.exists():
        gates = load_json(gates_path)
        stage_names = [stage.get("stage") for stage in gates.get("stages", [])]
        expected = [
            "RESEARCH_PROGRAM",
            "SOURCE_DOSSIER",
            "CLAIM_MODEL",
            "EXPERIMENTAL_RESULT",
            "PAPER_CANDIDATE",
            "SUBMISSION_CANDIDATE",
            "PUBLIC_RELEASE_READY",
        ]
        if stage_names != expected:
            errors.append("LAB_STAGE_GATES.json must define the canonical seven-stage sequence")
        limits = gates.get("portfolio_limits", {})
        if limits.get("max_active_article_hardening_branches") != 2:
            errors.append("portfolio limit must cap active article hardening branches at 2")

    for path in STALE_READY_SURFACES:
        if path.exists() and READY_RE.search(read_text(path)):
            errors.append(f"stale ready claim in {path.relative_to(ROOT).as_posix()}")

    registry_path = ROOT / "research_runs" / "journal_submission_readiness" / "candidate_registry.json"
    external_reader_path = (
        ROOT / "research_runs" / "external_reader_legitimacy" / "external_reader_legitimacy_report.json"
    )
    public_release_triage_path = (
        ROOT / "research_runs" / "public_release_triage" / "independent_public_output_audit.json"
    )
    context_contamination_path = (
        ROOT / "research_runs" / "context_contamination" / "context_contamination_report.json"
    )
    if registry_path.exists():
        registry = load_json(registry_path)
        registry_status = str(registry.get("status", ""))
        external_status = str(registry.get("external_reader_legitimacy_status", ""))
        if external_status == "EXTERNAL_READER_LEGITIMACY_FAIL" and READY_RE.search(registry_status):
            errors.append("journal registry cannot claim readiness while external-reader legitimacy fails")
        if external_status == "EXTERNAL_READER_LEGITIMACY_FAIL":
            interpretation = str(registry.get("external_reader_legitimacy_interpretation", "")).lower()
            if "must not be represented as journal-ready" not in interpretation:
                errors.append("journal registry must explicitly block journal-ready interpretation on external-reader failure")
        triage_status = str(registry.get("public_release_triage_status", ""))
        if triage_status == "PUBLIC_RELEASE_TRIAGE_BLOCKED":
            if registry.get("public_journal_candidate_count") != 0:
                errors.append("public release triage cannot be blocked while public journal candidates are nonzero")
            triage_interpretation = str(registry.get("public_release_triage_interpretation", "")).lower()
            if "zero public journal-manuscript candidates" not in triage_interpretation:
                errors.append("journal registry must explicitly record zero public journal candidates when triage is blocked")
        context_status = str(registry.get("context_contamination_status", ""))
        if context_status == "CONTEXT_CONTAMINATION_FAIL":
            if registry.get("public_journal_candidate_count") != 0:
                errors.append("context-contamination failure cannot coexist with public journal candidates")
            context_interpretation = str(registry.get("context_contamination_interpretation", "")).lower()
            if "must not" not in context_interpretation or "journal" not in context_interpretation:
                errors.append("journal registry must explicitly block journal-ready interpretation on context contamination")
    if registry_path.exists() and external_reader_path.exists():
        registry = load_json(registry_path)
        external_reader = load_json(external_reader_path)
        if registry.get("external_reader_legitimacy_status") != external_reader.get("status"):
            errors.append("journal registry external-reader status must match external-reader report")
    if registry_path.exists() and public_release_triage_path.exists():
        registry = load_json(registry_path)
        triage = load_json(public_release_triage_path)
        if registry.get("public_release_triage_status") != triage.get("status"):
            errors.append("journal registry public-release triage status must match triage report")
        if registry.get("public_journal_candidate_count") != triage.get("public_journal_candidate_count"):
            errors.append("journal registry public-journal count must match triage report")
    if registry_path.exists() and context_contamination_path.exists():
        registry = load_json(registry_path)
        context = load_json(context_contamination_path)
        if registry.get("context_contamination_status") != context.get("status"):
            errors.append("journal registry context-contamination status must match context-contamination report")
        if registry.get("context_contamination_pass_count") != context.get("passed_count"):
            errors.append("journal registry context-contamination pass count must match context-contamination report")
        if registry.get("context_contamination_checked_count") != context.get("checked_count"):
            errors.append("journal registry context-contamination checked count must match context-contamination report")

    scoreboard_path = ROOT / "benchmarks" / "nwagu_article_research" / "scoreboard.json"
    if scoreboard_path.exists():
        scoreboard = load_json(scoreboard_path)
        ijrs = float(scoreboard.get("impact_journal_readiness_score", 0))
        status = scoreboard.get("status")
        if ijrs < 65 and status != "WORKING_PAPER_SET_NOT_IMPACT_READY":
            errors.append("sub-65 IJRS must be WORKING_PAPER_SET_NOT_IMPACT_READY")
        if ijrs >= 65 and status == "WORKING_PAPER_SET_NOT_IMPACT_READY":
            errors.append("working-paper status cannot carry impact-level IJRS")

    manifest_path = ROOT / "papers" / "nwagu_aneke_articles" / "manifest.json"
    if manifest_path.exists():
        manifest = load_json(manifest_path)
        status = str(manifest.get("status", ""))
        if status != "TARGETED_HUMAN_REVIEW_DRAFTS_NOT_SUBMISSION_READY":
            errors.append("Nwagu article manifest must remain not-submission-ready until stage gates pass")
        assessment = manifest.get("impact_journal_assessment", {})
        if assessment.get("submission_ready") is True:
            errors.append("Nwagu article manifest cannot mark submission_ready true")
        current_status = str(assessment.get("current_status", "")).lower()
        if "journal-track" in current_status or "impact" in current_status:
            errors.append("Nwagu article manifest must not describe current package as journal-track or impact")
        triage = manifest.get("portfolio_triage", {})
        if triage.get("active_hardening") != ["ARTICLE-NA-002", "ARTICLE-NA-010"]:
            errors.append("Nwagu portfolio triage must harden only ARTICLE-NA-002 and ARTICLE-NA-010")
        if len(triage.get("parked", [])) != 8:
            errors.append("Nwagu portfolio triage must park the other eight article branches")

    if errors:
        print("LAB_STANDARD_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("LAB_STANDARD_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
