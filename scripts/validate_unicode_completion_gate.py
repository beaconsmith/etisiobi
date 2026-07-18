from __future__ import annotations

import json
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "research_runs" / "unicode_completion"
GATE = RUN_DIR / "unicode_completion_gate.json"
REQUIRED_DOCS = [
    RUN_DIR / "CURRENT.md",
    RUN_DIR / "nwagu_aneke_unicode_completion_dossier.md",
    RUN_DIR / "independent_submitter_pathway.md",
    RUN_DIR / "nwagu_aneke_preliminary_proposal_skeleton.md",
    RUN_DIR / "nwagu_aneke_working_repertoire_table.md",
    RUN_DIR / "nwagu_aneke_source_review_worksheet.md",
    RUN_DIR / "nwagu_aneke_character_glyph_matrix.md",
    RUN_DIR / "nwagu_aneke_properties_behavior_matrix.md",
    RUN_DIR / "nwagu_aneke_representative_evidence_plan.md",
    RUN_DIR / "nwagu_aneke_font_license_requirements.md",
    RUN_DIR / "sewg_packet_index.md",
    RUN_DIR / "related_igbo_scripts_triage.md",
]

READY_RE = re.compile(
    r"\bREADY_FOR_SUBMISSION\b|\bSUBMISSION_READY\b|\bREADY_FOR_HUMAN_ARXIV_REVIEW\b|"
    r"\bIMPACT_JOURNAL_READY\b|\bUNICODE_PROPOSAL_READY\b",
    flags=re.I,
)

REQUIRED_BLOCKERS = {
    "source_transcription_review",
    "stable_character_repertoire",
    "character_glyph_distinction_review",
    "representative_glyphs_rights_cleared",
    "usage_examples_rights_cleared",
    "submitter_user_community_relationship_record",
    "character_names",
    "unicode_properties",
    "implementation_font_licence",
    "cla_author_submitter_ip_endorsement",
    "proposal_pdf",
    "iso_iec_10646_summary_information",
    "human_final_package_signoff",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> int:
    errors: list[str] = []
    if not GATE.exists():
        errors.append(f"missing {rel(GATE)}")
    for path in REQUIRED_DOCS:
        if not path.exists():
            errors.append(f"missing {rel(path)}")
    if errors:
        print("UNICODE_COMPLETION_GATE_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    gate = json.loads(read_text(GATE))
    if gate.get("status") != "UNICODE_COMPLETION_BLOCKED_EVIDENCE_PACKAGE":
        errors.append("Unicode completion status must remain evidence-package blocked until proposal evidence exists")
    if gate.get("independent_submitter_path") != "OPEN_PACKAGE_INCOMPLETE":
        errors.append("independent submitter path must be open but package-incomplete")
    if gate.get("draft_allowed") is not True:
        errors.append("draft_allowed must be true for the independent submitter pathway")
    if gate.get("proposal_ready") is not False:
        errors.append("proposal_ready must be false")
    if gate.get("may_submit") is not False:
        errors.append("may_submit must be false")
    if gate.get("submit_decision") != "DO_NOT_SUBMIT":
        errors.append("submit_decision must be DO_NOT_SUBMIT")
    components = gate.get("package_components", {})
    for key in (
        "working_repertoire_table",
        "source_review_worksheet",
        "source_review_worksheet_summary",
        "character_glyph_matrix",
        "properties_behavior_matrix",
        "representative_evidence_plan",
        "font_license_requirements",
        "sewg_packet_index",
        "sewg_packet_index_json",
    ):
        path = ROOT / str(components.get(key, ""))
        if not path.exists():
            errors.append(f"package component {key} is missing or points to a missing file")

    blockers = set(gate.get("required_before_submission", []))
    missing = sorted(REQUIRED_BLOCKERS - blockers)
    if missing:
        errors.append("required_before_submission missing blockers: " + ", ".join(missing))

    related = {row.get("name"): row.get("status") for row in gate.get("related_scripts", [])}
    if related.get("Nwagugu") != "NO_SEPARATE_SCRIPT_EVIDENCE_FOUND":
        errors.append("Nwagugu must remain an unverified/no-separate-script lead")
    if related.get("Ndebe / Ńdébé") != "SEPARATE_CREATOR_AUTHORITY_REQUIRED":
        errors.append("Ndebe must require separate creator/authority participation")

    for path in REQUIRED_DOCS:
        text = read_text(path)
        if READY_RE.search(text):
            errors.append(f"{rel(path)} contains an unsupported readiness phrase")
        if path.name not in ("related_igbo_scripts_triage.md", "independent_submitter_pathway.md") and "Do not submit" not in text:
            errors.append(f"{rel(path)} must explicitly say Do not submit")
    repertoire = read_text(RUN_DIR / "nwagu_aneke_working_repertoire_table.md")
    for phrase in ("NA-ROW-026", "NA-VOWEL-008", "WORKING_REPERTOIRE_TABLE_NOT_PROPOSAL_REPERTOIRE"):
        if phrase not in repertoire:
            errors.append(f"working repertoire table missing phrase: {phrase}")
    glyph_matrix = read_text(RUN_DIR / "nwagu_aneke_character_glyph_matrix.md")
    if "DO_NOT_USE_AS_REPERTOIRE_PROPOSAL" not in glyph_matrix:
        errors.append("character-glyph matrix must block use as repertoire proposal")
    font_plan = read_text(RUN_DIR / "nwagu_aneke_font_license_requirements.md")
    if "NO_FONT_READY_FOR_SEWG" not in font_plan:
        errors.append("font/licence plan must record no SEWG-ready font")
    packet_index = json.loads(read_text(RUN_DIR / "sewg_packet_index.json"))
    if packet_index.get("may_submit") is not False:
        errors.append("SEWG packet index must keep may_submit=false")
    missing_before_submission = set(packet_index.get("missing_before_submission", []))
    for item in ("stable_proposed_repertoire", "representative_glyphs", "font", "proposal_pdf"):
        if item not in missing_before_submission:
            errors.append(f"SEWG packet index missing blocker: {item}")
    worksheet_path = RUN_DIR / "nwagu_aneke_source_review_worksheet.csv"
    with worksheet_path.open(encoding="utf-8", newline="") as handle:
        worksheet_rows = list(csv.DictReader(handle))
    if len(worksheet_rows) != 208:
        errors.append(f"source review worksheet must contain 208 rows, found {len(worksheet_rows)}")
    if any(row.get("review_decision") != "UNREVIEWED" for row in worksheet_rows):
        errors.append("source review worksheet must remain UNREVIEWED until human review is recorded")
    if any(row.get("rights_status") != "UNREVIEWED" for row in worksheet_rows):
        errors.append("source review worksheet rights_status must remain UNREVIEWED until human review is recorded")

    if errors:
        print("UNICODE_COMPLETION_GATE_INVALID")
        for error in errors[:200]:
            print(f"- {error}")
        return 1

    print("UNICODE_COMPLETION_GATE_VALID")
    print("primary_script=Nwagu Aneke")
    print("may_submit=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
