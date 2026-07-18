from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.validate_external_reader_legitimacy import build_report, write_report

REGISTRY = ROOT / "research_runs" / "journal_submission_readiness" / "candidate_registry.json"
OUT_DIR = ROOT / "research_runs" / "public_release_triage"
OUT_JSON = OUT_DIR / "independent_public_output_audit.json"
OUT_MD = OUT_DIR / "independent_public_output_audit.md"

PUBLIC_JOURNAL = "PUBLIC_JOURNAL_MANUSCRIPT_CANDIDATE"
PUBLIC_PREPRINT = "PUBLIC_PREPRINT_CANDIDATE"
PUBLIC_TECHNICAL = "PUBLIC_TECHNICAL_REPORT"
PUBLIC_DATASET = "PUBLIC_DATASET_OR_NOTE"
MERGE = "MERGE_INTO_STRONGER_MANUSCRIPT"
INTERNAL = "INTERNAL_ONLY"
PARK = "KILL_OR_PARK"

RELEASE_CLASSES = {
    PUBLIC_JOURNAL,
    PUBLIC_PREPRINT,
    PUBLIC_TECHNICAL,
    PUBLIC_DATASET,
    MERGE,
    INTERNAL,
    PARK,
}

TRIAGE_OVERRIDES = {
    "ARTICLE-NA-012": {
        "release_class": INTERNAL,
        "rationale": "The layer-promotion-error topic is valuable as a lab-quality benchmark, but the current manuscript still reads as internal process infrastructure rather than an independently evidenced research paper.",
        "required_work": [
            "Replace lab-process framing with a public benchmark definition and external task examples.",
            "Add independently reproducible benchmark instances beyond the Nwagu Aneke article program.",
            "Only reconsider as a paper after external-reader legitimacy passes.",
        ],
    },
    "ARTICLE-NA-002": {
        "release_class": MERGE,
        "rationale": "The count-layer audit is the strongest next scholarly nucleus, but the current text still carries private project framing and should absorb the f/v hinge material instead of spawning parallel weak papers.",
        "required_work": [
            "Rewrite as a source-critical article addressed to digital humanities readers.",
            "Move ARTICLE-NA-003 into a subsection unless new source evidence makes it independent.",
            "Keep 26 by 8 source-observed and 27/216 derived-layer language explicit in every result.",
        ],
    },
    "ARTICLE-NA-010": {
        "release_class": INTERNAL,
        "rationale": "The non-promotion invariant is useful infrastructure, but the current manuscript depends on lab-internal framing and lacks enough external comparative evidence for a cultural-heritage journal paper.",
        "required_work": [
            "Turn the invariant into a reusable method with non-Nwagu examples.",
            "Add ablations or counterexamples showing what the invariant prevents.",
            "Park as internal method work until the empirical base is broader.",
        ],
    },
    "ARTICLE-NA-001": {
        "release_class": MERGE,
        "rationale": "The reconstruction ledger is important, but it overlaps heavily with the count-layer audit and currently reads as package inventory rather than a distinct field contribution.",
        "required_work": [
            "Merge the ledger's strongest source-discipline material into ARTICLE-NA-002.",
            "Retain standalone release only if it gains a separate source-dossier result.",
        ],
    },
    "ARTICLE-NA-003": {
        "release_class": MERGE,
        "rationale": "The f/v hinge is a derived-layer rule, not currently enough for an independent paper; it should strengthen the count-layer audit.",
        "required_work": [
            "Integrate as a derived-layer case study in ARTICLE-NA-002.",
            "Do not release independently unless new primary evidence or comparative orthographic analysis is added.",
        ],
    },
    "ARTICLE-NA-004": {
        "release_class": PARK,
        "rationale": "The logograph lead set may be useful later, but rights, source-image, and cultural-authority constraints make the current paper too thin for public release.",
        "required_work": [
            "Obtain rights/authority clearance for public examples before any paper claim.",
            "Rebuild as a dataset note only if the lead-set evidence can be inspected by reviewers.",
        ],
    },
    "ARTICLE-NA-005": {
        "release_class": INTERNAL,
        "rationale": "The TEI/IIIF/Web Annotation bridge is currently a standards workflow note. Without coordinate evidence or released selector examples, it is not an independent research manuscript.",
        "required_work": [
            "Produce inspectable selector records tied to cleared source examples.",
            "Release as a technical report before considering a journal article.",
        ],
    },
    "ARTICLE-NA-008": {
        "release_class": PARK,
        "rationale": "The comparative standardization idea needs fresh comparative source work. The current version still advertises a package rather than delivering a mature cross-script result.",
        "required_work": [
            "Rebuild the comparison from external standards documentation and peer-reviewed sources.",
            "Separate Nwagu Aneke positioning from any Unicode-readiness implication.",
        ],
    },
    "ARTICLE-NA-009": {
        "release_class": PARK,
        "rationale": "The tokenizer baseline is not yet a language-resource paper because data rights, corpus scope, and downstream evaluation are too limited.",
        "required_work": [
            "Clarify corpus licensing and sampling.",
            "Add a stronger baseline/evaluation protocol before public language-resource claims.",
        ],
    },
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def plain_word_count(tex: str) -> int:
    stripped = re.sub(r"\\cite\{[^}]+\}", " citation ", tex)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?", " ", stripped)
    stripped = re.sub(r"[{}\\_$]", " ", stripped)
    return len(re.findall(r"[A-Za-z][A-Za-z0-9/-]+", stripped))


def citation_count(tex: str) -> int:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in group.split(",") if key.strip())
    return len(keys)


def candidate_tex_path(candidate: dict) -> Path:
    trace = ROOT / str(candidate["review_team_trace"])
    return trace.parent / "main.tex"


def structural_profile(candidate: dict) -> dict[str, object]:
    tex_path = candidate_tex_path(candidate)
    tex = read_text(tex_path) if tex_path.exists() else ""
    required_sections = [
        r"\section{Introduction}",
        r"\section{Related Work}",
        r"\section{Materials and Evidence}",
        r"\section{Method}",
        r"\section{Results}",
        r"\section{Discussion}",
        r"\section{Limitations}",
        r"\section{Reproducibility}",
        r"\section{Conclusion}",
    ]
    return {
        "tex_path": tex_path.relative_to(ROOT).as_posix(),
        "word_count": plain_word_count(tex),
        "citation_count": citation_count(tex),
        "scientific_section_count": sum(1 for section in required_sections if section in tex),
        "has_result_table": bool(re.search(r"\\begin\{table\*?\}", tex)),
    }


def classify_candidate(candidate: dict, external_row: dict) -> dict[str, object]:
    article_id = str(candidate["article_id"])
    profile = structural_profile(candidate)
    external_pass = bool(external_row.get("external_reader_legitimacy_pass"))
    remaining_blockers = list(candidate.get("remaining_blockers", []))
    override = TRIAGE_OVERRIDES.get(article_id, {})

    if external_pass:
        release_class = PUBLIC_PREPRINT
        rationale = (
            "This manuscript reads as a field-facing paper rather than a lab package. "
            "It remains below public journal-candidate status because source, rights, venue, disclosure, "
            "and final author sign-offs are still unresolved."
        )
        required_work = [
            "Obtain human source and rights/authority sign-off.",
            "Decide whether the appropriate output is a short methods paper, standards note, or technical report.",
            "Do not call it an impact-journal candidate until a target-venue review accepts its contribution scale.",
        ]
    else:
        release_class = str(override.get("release_class", INTERNAL))
        rationale = str(override.get("rationale", "The manuscript fails external-reader legitimacy and must remain internal."))
        required_work = list(override.get("required_work", ["Remove private lab/process framing and add substantive public evidence."]))

    if release_class == PUBLIC_JOURNAL and (not external_pass or remaining_blockers):
        release_class = PUBLIC_PREPRINT if external_pass else INTERNAL

    return {
        "article_id": article_id,
        "title": candidate.get("title", ""),
        "target_venue": candidate.get("target_venue", ""),
        "release_class": release_class,
        "external_reader_legitimacy_pass": external_pass,
        "external_reader_blockers": external_row.get("blockers", []),
        "registry_status": candidate.get("status", ""),
        "remaining_human_signoff_blockers": remaining_blockers,
        "structural_profile": profile,
        "rationale": rationale,
        "required_work": required_work,
    }


def build_audit() -> dict[str, object]:
    registry = read_json(REGISTRY)
    external_report = build_report()
    write_report(external_report)
    external_by_id = {row["article_id"]: row for row in external_report["articles"]}  # type: ignore[index]
    outputs = [
        classify_candidate(candidate, external_by_id[str(candidate["article_id"])])
        for candidate in registry.get("candidates", [])
    ]
    public_journal_count = sum(1 for row in outputs if row["release_class"] == PUBLIC_JOURNAL)
    public_preprint_count = sum(1 for row in outputs if row["release_class"] == PUBLIC_PREPRINT)
    public_technical_count = sum(1 for row in outputs if row["release_class"] == PUBLIC_TECHNICAL)
    blocked_or_internal_count = len(outputs) - public_journal_count - public_preprint_count - public_technical_count
    preprint_phrase = (
        f"{public_preprint_count} public-facing preprint candidates"
        if public_preprint_count != 1
        else "one public-facing preprint candidate"
    )
    blocked_phrase = (
        f"{blocked_or_internal_count} outputs that must be merged, parked, or kept internal"
        if blocked_or_internal_count != 1
        else "one output that must be merged, parked, or kept internal"
    )
    return {
        "status": "PUBLIC_RELEASE_TRIAGE_BLOCKED",
        "checked_count": len(outputs),
        "external_reader_pass_count": external_report["passed_count"],
        "public_journal_candidate_count": public_journal_count,
        "public_preprint_candidate_count": public_preprint_count,
        "public_technical_report_count": public_technical_count,
        "interpretation": (
            "The previous ten-candidate registry is structurally useful but not a public-release claim. "
            f"At the current evidence stage there are zero public journal-manuscript candidates, {preprint_phrase}, "
            f"and {blocked_phrase} before release."
        ),
        "exact_next_action": (
            "Prepare the smallest human source/rights review packets for ARTICLE-NA-002, ARTICLE-NA-006, "
            "and ARTICLE-NA-010; do not advance any to public journal-manuscript candidate status until "
            "human source, rights, venue, disclosure, licence, and final package sign-offs are recorded."
        ),
        "allowed_release_classes": sorted(RELEASE_CLASSES),
        "outputs": outputs,
    }


def write_audit(report: dict[str, object]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Independent Public Output Audit",
        "",
        f"Status: `{report['status']}`",
        f"Checked: {report['checked_count']}",
        f"External-reader pass count: {report['external_reader_pass_count']}",
        f"Public journal-manuscript candidates: {report['public_journal_candidate_count']}",
        f"Public preprint candidates: {report['public_preprint_candidate_count']}",
        "",
        str(report["interpretation"]),
        "",
        f"Exact next action: {report['exact_next_action']}",
        "",
        "## Triage",
        "",
    ]
    for row in report["outputs"]:  # type: ignore[index]
        lines.extend(
            [
                f"### {row['article_id']}: {row['release_class']}",  # type: ignore[index]
                f"Title: {row['title']}",  # type: ignore[index]
                f"External-reader legitimacy: {'PASS' if row['external_reader_legitimacy_pass'] else 'FAIL'}",  # type: ignore[index]
                "",
                str(row["rationale"]),  # type: ignore[index]
                "",
                "Required work:",
            ]
        )
        for item in row["required_work"]:  # type: ignore[index]
            lines.append(f"- {item}")
        blockers = row.get("external_reader_blockers", [])  # type: ignore[assignment]
        if blockers:
            lines.append("")
            lines.append("Current legitimacy blockers:")
            for blocker in blockers[:4]:
                lines.append(f"- {blocker}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    report = build_audit()
    write_audit(report)
    print(report["status"])
    print(f"checked={report['checked_count']}")
    print(f"public_journal_candidates={report['public_journal_candidate_count']}")
    print(f"public_preprint_candidates={report['public_preprint_candidate_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
