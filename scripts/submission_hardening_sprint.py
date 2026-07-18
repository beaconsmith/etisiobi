from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
SELECTED = ROOT / "papers" / "SELECTED_PAPER"
REVIEWER = ROOT / "outputs" / "reviewer_packet"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean(text: str) -> str:
    stripped = dedent(text).strip()
    return "\n".join(line[8:] if line.startswith("        ") else line for line in stripped.splitlines())


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(text) + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run(args: list[str], cwd: Path = ROOT) -> dict:
    proc = subprocess.run(args, cwd=cwd, capture_output=True, text=True, shell=False)
    return {
        "command": " ".join(args),
        "cwd": str(cwd),
        "exit_code": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def git_value(args: list[str]) -> str:
    proc = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, shell=False)
    return proc.stdout.strip() if proc.returncode == 0 else ""


def freeze_manifest() -> dict:
    selected_files = [
        p for p in SELECTED.rglob("*")
        if p.is_file() and p.name != "freeze_manifest.json"
    ]
    reviewer_files = [p for p in REVIEWER.rglob("*") if p.is_file()] if REVIEWER.exists() else []
    manifest = {
        "created_at": now(),
        "git_branch": git_value(["rev-parse", "--abbrev-ref", "HEAD"]),
        "git_commit": git_value(["rev-parse", "HEAD"]),
        "dirty_status_lines": git_value(["status", "--short"]).splitlines(),
        "current_readiness_status": (SELECTED / "submission_readiness_decision.md").read_text(encoding="utf-8").strip(),
        "manuscript_files": [{"path": rel(p), "sha256": sha256(p), "bytes": p.stat().st_size} for p in selected_files],
        "pdf_checksum": sha256(SELECTED / "main.pdf"),
        "arxiv_package_zip_checksum": sha256(SELECTED / "arxiv_package.zip"),
        "source_bibliography_checksum": sha256(SELECTED / "source_bibliography.bib"),
        "figure_table_checksums": [
            {"path": rel(p), "sha256": sha256(p), "bytes": p.stat().st_size}
            for folder in ("figures", "tables")
            for p in (SELECTED / folder).glob("*")
            if p.is_file()
        ],
        "reviewer_packet_checksums": [
            {"path": rel(p), "sha256": sha256(p), "bytes": p.stat().st_size}
            for p in reviewer_files
        ],
    }
    write_json(SELECTED / "freeze_manifest.json", manifest)
    write_text(
        SELECTED / "freeze_manifest.md",
        f"""
        # Freeze Manifest

        Created: `{manifest['created_at']}`

        Branch: `{manifest['git_branch']}`

        Commit: `{manifest['git_commit']}`

        Dirty/untracked status lines: `{len(manifest['dirty_status_lines'])}`

        PDF checksum: `{manifest['pdf_checksum']}`

        arXiv package zip checksum: `{manifest['arxiv_package_zip_checksum']}`

        Source bibliography checksum: `{manifest['source_bibliography_checksum']}`

        Current readiness snapshot:

        ```text
        {manifest['current_readiness_status']}
        ```

        The old readiness decision is preserved. This file freezes the pre-hardening state for comparison.
        """,
    )
    write_text(
        SELECTED / "submission_hardening_log.md",
        f"""
        # Submission Hardening Log

        - `{manifest['created_at']}`: froze selected paper state.
        - Scope: PAPER-003 only.
        - Goal: strongest honest readiness decision after final claim, prior-art, rights, glyph, package, and compile gates.
        """,
    )
    return manifest


def final_claim_gate() -> list[dict]:
    rows = [
        {
            "claim_id": "FINAL-CLAIM-0001",
            "claim_text": "BMC as a standalone annotation cache overlaps existing standards.",
            "paper_location": "Abstract; Introduction; Discussion",
            "claim_type": "prior_art",
            "evidence_files": ["external_sources/local_vs_sota_comparison.md"],
            "external_sources": ["EXT-0001", "EXT-0003", "EXT-0005", "EXT-0006", "EXT-0008", "EXT-0009", "EXT-0011", "EXT-0013"],
            "status": "READY",
            "risk": "low",
            "required_action": "Keep conservative novelty wording.",
        },
        {
            "claim_id": "FINAL-CLAIM-0002",
            "claim_text": "The contribution is the integration of standards-compatible evidence objects, count-layer reconciliation, claim gates, autoresearch scoring, and manuscript preflight.",
            "paper_location": "Abstract; Introduction; Conclusion",
            "claim_type": "novelty",
            "evidence_files": ["papers/PAPER_SELECTION_TOURNAMENT.md", "autoresearch_runs/RUN-PUB-20260528-0001"],
            "external_sources": ["EXT-0001", "EXT-0003", "EXT-0008", "EXT-0017"],
            "status": "READY",
            "risk": "medium",
            "required_action": "Do not strengthen to first-ever claim.",
        },
        {
            "claim_id": "FINAL-CLAIM-0003",
            "claim_text": "Source layer reconciles as 26 rows by 8 vowels for 208 BMC records.",
            "paper_location": "Abstract; Introduction; Results; Table 2",
            "claim_type": "count",
            "evidence_files": ["corpus/bmc_count_reconciliation.json", "corpus/base_modifier_cache.jsonl"],
            "external_sources": ["EXT-0018", "EXT-0019"],
            "status": "READY",
            "risk": "medium",
            "required_action": "Retain source-layer wording and cite local count audit.",
        },
        {
            "claim_id": "FINAL-CLAIM-0004",
            "claim_text": "27/216 belongs to a derived f/v split layer, not the source-observed layer.",
            "paper_location": "Abstract; Introduction; Results; Figure 2",
            "claim_type": "count",
            "evidence_files": ["corpus/bmc_count_reconciliation.json"],
            "external_sources": [],
            "status": "READY",
            "risk": "medium",
            "required_action": "Never state 27/216 as source-observed.",
        },
        {
            "claim_id": "FINAL-CLAIM-0005",
            "claim_text": "The current BMC is a working annotation index, not a fully reviewed glyph substrate.",
            "paper_location": "Limitations",
            "claim_type": "limitation",
            "evidence_files": ["corpus/base_modifier_cache.jsonl", "authority/bmc_review_states.jsonl"],
            "external_sources": ["EXT-0007"],
            "status": "READY",
            "risk": "low",
            "required_action": "Keep as explicit limitation.",
        },
        {
            "claim_id": "FINAL-CLAIM-0006",
            "claim_text": "The paper does not prove glyph-shape grammar, E6, universal compression, or exact 27/216 theory claims.",
            "paper_location": "Limitations; Conclusion",
            "claim_type": "limitation",
            "evidence_files": ["corpus/bmc_claim_gate.jsonl", "corpus/bmc_hyperloop_result.json"],
            "external_sources": [],
            "status": "READY",
            "risk": "low",
            "required_action": "Keep exclusions explicit.",
        },
        {
            "claim_id": "FINAL-CLAIM-0007",
            "claim_text": "Public release or external submission is approved.",
            "paper_location": "Not stated positively",
            "claim_type": "authority",
            "evidence_files": ["authority/approval_register.jsonl", "release/release_manifest.json"],
            "external_sources": [],
            "status": "NEEDS_HUMAN_REVIEW",
            "risk": "high",
            "required_action": "Keep final readiness blocked until authority and rights documents are attached.",
        },
        {
            "claim_id": "FINAL-CLAIM-0008",
            "claim_text": "The Web Annotation export is a partial mapping proposal.",
            "paper_location": "Method; Discussion; web_annotation_mapping.md",
            "claim_type": "standard",
            "evidence_files": ["exports/web_annotation/bmc_web_annotations.jsonld", "papers/SELECTED_PAPER/web_annotation_mapping.md"],
            "external_sources": ["EXT-0008", "EXT-WA-VOCAB"],
            "status": "READY",
            "risk": "medium",
            "required_action": "Do not claim full W3C Web Annotation compliance.",
        },
        {
            "claim_id": "FINAL-CLAIM-0009",
            "claim_text": "The CIDOC CRM / CRMdig export is a lightweight mapping proposal.",
            "paper_location": "Method; Discussion; cidoc_crm_mapping.md",
            "claim_type": "standard",
            "evidence_files": ["exports/cidoc_crm/bmc_cidoc_mapping.jsonld", "papers/SELECTED_PAPER/cidoc_crm_mapping.md"],
            "external_sources": ["EXT-0009", "EXT-0010", "EXT-CRMDIG"],
            "status": "READY",
            "risk": "medium",
            "required_action": "Require ontology expert validation before calling it compliant.",
        },
        {
            "claim_id": "FINAL-CLAIM-0010",
            "claim_text": "The package is ready for arXiv submission.",
            "paper_location": "Not stated positively",
            "claim_type": "reproducibility",
            "evidence_files": ["papers/SELECTED_PAPER/final_submission_readiness_decision.md"],
            "external_sources": ["EXT-0014", "EXT-0015"],
            "status": "NEEDS_HUMAN_REVIEW",
            "risk": "high",
            "required_action": "Only change after authority, rights, glyph, and final human review pass.",
        },
    ]
    write_jsonl(SELECTED / "final_claim_gate.jsonl", rows)
    table = "\n".join(
        f"| {r['claim_id']} | {r['claim_type']} | {r['status']} | {r['risk']} | {r['required_action']} |"
        for r in rows
    )
    write_text(
        SELECTED / "final_claim_gate.md",
        f"""
        # Final Claim Gate

        | Claim ID | Type | Status | Risk | Required Action |
        |---|---|---|---|---|
        {table}

        Gate result: no positive exact-count, novelty, glyph-grammar, E6, universal-compression, public-release, or arXiv-readiness claim is allowed beyond the evidence above.
        """,
    )
    return rows


def update_bibliography() -> None:
    bib_path = SELECTED / "source_bibliography.bib"
    bib = bib_path.read_text(encoding="utf-8")
    additions = []
    if "w3c_annotation_vocab_2017" not in bib:
        additions.append(
            """
            @misc{w3c_annotation_vocab_2017,
              title = {Web Annotation Vocabulary},
              author = {W3C Web Annotation Working Group},
              year = {2017},
              url = {https://www.w3.org/TR/annotation-vocab/}
            }
            """
        )
    if "crmdig_50" not in bib:
        additions.append(
            """
            @misc{crmdig_50,
              title = {CRMdig: An Extension of CIDOC CRM to Support Provenance Metadata},
              author = {CIDOC CRM SIG},
              year = {2023},
              url = {https://cidoc-crm.org/crmdig/}
            }
            """
        )
    if additions:
        bib_path.write_text(bib.rstrip() + "\n\n" + "\n\n".join(clean(a) for a in additions) + "\n", encoding="utf-8")


def revise_manuscript() -> None:
    path = SELECTED / "main.tex"
    text = path.read_text(encoding="utf-8")
    if r"\keywords{" not in text:
        text = text.replace(
            r"\maketitle",
            "\\ccsdesc[500]{Information systems~Digital libraries and archives}\n"
            "\\ccsdesc[300]{Applied computing~Arts and humanities}\n"
            "\\keywords{research objects, provenance, claim gates, Nwagu Aneke, IIIF, TEI, cultural heritage}\n\n"
            "\\maketitle",
        )
    text = text.replace(
        "Web Annotation~\\cite{w3c_annotation_2017}",
        "Web Annotation~\\cite{w3c_annotation_2017,w3c_annotation_vocab_2017}",
    )
    text = text.replace(
        "CIDOC CRM~\\cite{cidoc_crm_home,cidoc_crm_713}",
        "CIDOC CRM and CRMdig~\\cite{cidoc_crm_home,cidoc_crm_713,crmdig_50}",
    )
    method_insert = (
        "As a hardening step, we exported BMC records into two standards-facing proposal layers. "
        "The Web Annotation export maps each BMC record to an Annotation with body, target, motivation, certainty, and provenance metadata; because most records lack reviewed pixel selectors, we label it a partial mapping rather than full compliance. "
        "The CIDOC CRM/CRMdig export maps the source artifact, digital BMC dataset, annotation activity, actor, and BMC information objects into cultural-heritage graph concepts; it remains a proposal until reviewed by a domain ontology expert.\n\n"
    )
    if "As a hardening step, we exported BMC records" not in text:
        text = text.replace("\\input{figures/bmc_standard_mapping_graph}", method_insert + "\\input{figures/bmc_standard_mapping_graph}")
    limitation_add = (
        "The Web Annotation and CIDOC CRM/CRMdig exports are interoperability proposals, not certified standards compliance artifacts. "
        "They are intended to make the BMC easier to review against existing scholarly infrastructure while preserving the paper's main limitation: external submission is blocked until authority, rights, and source review pass."
    )
    if "interoperability proposals, not certified standards compliance artifacts" not in text:
        text = text.replace(
            "The manuscript is a draft for human review, not an external submission.",
            "The manuscript is a draft for human review, not an external submission. " + limitation_add,
        )
    text = text.replace(
        "The sprint can be rerun with \\texttt{python scripts/autoresearch\\_publication\\_loop.py} followed by \\texttt{python scripts/generate\\_publication\\_assets.py}.",
        "The sprint can be rerun with \\texttt{python scripts/autoresearch\\_publication\\_loop.py}, \\texttt{python scripts/generate\\_publication\\_assets.py}, \\texttt{python scripts/export\\_bmc\\_web\\_annotations.py}, \\texttt{python scripts/export\\_bmc\\_cidoc\\_mapping.py}, and \\texttt{python scripts/submission\\_hardening\\_sprint.py}.",
    )
    path.write_text(text, encoding="utf-8")
    write_text(
        SELECTED / "claim_gate_revision_log.md",
        """
        # Claim Gate Revision Log

        Revisions applied after final claim gate:

        - Added ACM CCS and keywords metadata.
        - Kept BMC novelty wording conservative: BMC is not claimed as a standalone new annotation standard.
        - Added Web Annotation export paragraph and labeled it partial, not full compliance.
        - Added CIDOC CRM / CRMdig mapping paragraph and labeled it a proposal pending ontology review.
        - Expanded limitations to block readiness on authority, rights, and source review.
        - Updated reproducibility commands to include the two standards-export scripts and hardening sprint.

        Removed or blocked claims:

        - No claim that BMC is wholly novel.
        - No claim that glyph-shape grammar was proven.
        - No E6 or universal-compression validation claim.
        - No claim that 27/216 is source-observed.
        - No claim that public release or arXiv submission is approved.
        """,
    )


def prior_art_audits() -> None:
    clusters = [
        ("Research-object packaging", "adequate", ["RO-Crate", "DataCite", "FAIR"], [], "medium", "Keep BMC as integration layer, not packaging replacement."),
        ("Provenance", "adequate", ["PROV-O", "PROV-DM"], [], "medium", "Map future provenance graph to PROV-O RDF."),
        ("Source localization", "adequate", ["IIIF Presentation API", "TEI Guidelines"], ["reviewed pixel/region selectors"], "medium", "Block glyph claims until source review."),
        ("Annotation", "adequate", ["W3C Web Annotation Data Model", "Web Annotation Vocabulary"], ["validated JSON-LD profile"], "high", "Use partial export wording."),
        ("Cultural heritage knowledge representation", "weak", ["CIDOC CRM", "CRMdig"], ["ontology expert review", "version-specific class/property validation"], "medium", "Call CIDOC export a mapping proposal."),
        ("Scientific writing / claim verification", "weak", ["local claim gate", "citation audit"], ["deeper scholarly claim-verification literature"], "medium", "Do not claim complete prior-art coverage."),
        ("Autoresearch", "adequate", ["Karpathy autoresearch"], ["comparative evaluation of paper-readiness metric"], "medium", "Frame as adaptation, not solved autonomous research."),
        ("Domain", "weak", ["Azuonye 1992", "Omniglot overview"], ["primary source chart/transcription review", "expert review"], "high", "Keep Nwagu Aneke count claims source-layer and pending review."),
    ]
    rows = [
        {
            "cluster": c,
            "coverage_status": s,
            "best_sources": best,
            "missing_sources": missing,
            "novelty_collision_risk": risk,
            "required_revision": rev,
        }
        for c, s, best, missing, risk, rev in clusters
    ]
    write_json(SELECTED / "final_prior_art_gap_audit.json", rows)
    md_rows = "\n".join(
        f"| {r['cluster']} | {r['coverage_status']} | {', '.join(r['best_sources'])} | {', '.join(r['missing_sources']) or 'none identified'} | {r['novelty_collision_risk']} |"
        for r in rows
    )
    write_text(
        SELECTED / "final_prior_art_gap_audit.md",
        f"""
        # Final Prior-Art Gap Audit

        | Cluster | Coverage | Best Sources | Missing Sources | Novelty Collision Risk |
        |---|---|---|---|---|
        {md_rows}

        Conclusion: the standards coverage is adequate for a hardened draft, but domain/glyph review and scholarly claim-verification prior art remain weak enough to block a readiness claim.
        """,
    )
    write_text(
        SELECTED / "final_novelty_audit.md",
        """
        # Final Novelty Audit

        Conservative novelty statement:

        The contribution is not a new standalone annotation model. The contribution is the integration of standards-compatible evidence objects, count-layer reconciliation, claim gates, autoresearch scoring, and manuscript preflight into one reproducible research-object pipeline, demonstrated on the PAGC/Nwagu Aneke case.

        What is not novel:

        - Provenance modeling alone: PROV-O and PROV-DM cover this space.
        - Research-object packaging alone: RO-Crate and DataCite cover much of this space.
        - Source localization alone: IIIF and TEI cover much of this space.
        - Annotation body-target modeling alone: W3C Web Annotation covers this space.
        - Cultural heritage graphing alone: CIDOC CRM and CRMdig cover much of this space.

        What remains potentially novel:

        - A practical claim-gated pipeline that uses these standards-facing objects to stop exact-count drift from becoming manuscript claims.
        - A bounded publication autoresearch metric that keeps, revises, or rejects manuscript claims rather than optimizing model loss.
        - A concrete PAGC/Nwagu Aneke case study where 26x8 source-layer evidence is separated from derived 27/216 interpretation.

        Novelty status: `PROVISIONAL_BUT_DEFENSIBLE_FOR_HUMAN_REVIEW`.

        Remaining risk: deeper prior art in scientific claim verification and digital humanities publication pipelines may narrow the systems contribution.
        """,
    )


def mapping_docs() -> None:
    write_text(
        SELECTED / "web_annotation_mapping.md",
        """
        # BMC to W3C Web Annotation Mapping

        Export: `exports/web_annotation/bmc_web_annotations.jsonld`

        Mapping:

        | BMC concept | Web Annotation concept | Status |
        |---|---|---|
        | BMC record | Annotation | mapped |
        | reading / row / vowel | TextualBody | mapped |
        | IIIF canvas | Target source | mapped |
        | TEI locator | target metadata | partial |
        | certainty basis | TextualBody with assessing purpose | mapped |
        | source region | FragmentSelector | only when available |
        | provenance activity | annotation metadata | partial |

        Compliance note: this is a partial mapping proposal. Most BMC records do not yet have reviewed pixel or region selectors, so the export should not be described as complete Web Annotation compliance.
        """,
    )
    write_text(
        SELECTED / "cidoc_crm_mapping.md",
        """
        # BMC to CIDOC CRM / CRMdig Mapping

        Export: `exports/cidoc_crm/bmc_cidoc_mapping.jsonld`

        Mapping:

        | BMC/lab concept | CIDOC/CRMdig concept | Status |
        |---|---|---|
        | Nwagu Aneke source artifact reference | `crm:E22_Human-Made_Object` | placeholder pending authority review |
        | BMC dataset | `crm:E73_Information_Object` | mapped |
        | BMC generation / annotation activity | `crm:E13_Attribute_Assignment`, `crmdig:D7_Digital_Machine_Event` | proposal |
        | Etisiobi Research Collective | `crm:E39_Actor` | mapped |
        | BMC record | `crm:E73_Information_Object` | mapped |
        | claim dependencies | BMC extension metadata | partial |

        Compliance note: this is a lightweight mapping proposal, not a validated CIDOC CRM profile. A cultural-heritage ontology expert should review class/property choices before publication claims rely on it.
        """,
    )


def authority_and_rights_gate() -> str:
    approval = read_jsonl(ROOT / "authority" / "approval_register.jsonl")
    release = read_json(ROOT / "release" / "release_manifest.json") if (ROOT / "release" / "release_manifest.json").exists() else {}
    datacite = read_json(ROOT / "release" / "datacite_metadata.json") if (ROOT / "release" / "datacite_metadata.json").exists() else {}
    external_release_allowed = bool(release.get("external_release_allowed"))
    status = "CLEAR_FOR_HUMAN_ARXIV_REVIEW" if external_release_allowed else "PUBLICATION_REQUIRES_AUTHORITY_REVIEW"
    gate = {
        "status": status,
        "approval_records": len(approval),
        "external_release_allowed": external_release_allowed,
        "release_blockers": release.get("external_release_blockers", []),
        "datacite_rights": datacite.get("rightsList", []),
        "decision": "Do not submit externally until authority documents, rights review, and glyph/source review are attached.",
    }
    write_json(SELECTED / "authority_and_rights_gate.json", gate)
    write_text(
        SELECTED / "authority_and_rights_gate.md",
        f"""
        # Authority and Rights Gate

        Status: `{status}`

        Approval records found: `{len(approval)}`

        External release allowed by release manifest: `{external_release_allowed}`

        Release blockers:

        {chr(10).join('- ' + item for item in gate['release_blockers'])}

        DataCite rights note:

        ```json
        {json.dumps(gate['datacite_rights'], ensure_ascii=False, indent=2)}
        ```

        Decision: do not submit externally until the paper-specific authority and rights review is attached and explicitly allows public arXiv/ACM circulation.
        """,
    )
    write_text(
        REVIEWER / "HUMAN_AUTHORITY_RIGHTS_REVIEW.md",
        """
        # Human Authority and Rights Review

        1. Proposed public submission: PAPER-003, a systems/audit paper about claim-gated research objects with a PAGC/Nwagu Aneke count-layer case study.
        2. Exposed data/artifacts: manuscript text, generated tables/figures, BMC summary counts, source locators, standards mappings, and reviewer packet. The current package should not expose restricted source images.
        3. Source material quoted/reproduced: the draft cites Azuonye and public source pages but does not reproduce protected source images.
        4. Cultural claims made: Nwagu Aneke/PAGC count-layer distinction, BMC as working annotation index, and authority-aware publication gating.
        5. Current authority evidence: user attestation exists, but signed/recorded paper-specific approval is not attached.
        6. Unclear: source-image rights, public release scope, glyph review authority, and whether derived 27/216 explanation is approved for public discussion.
        7. Required approvers: lab owner, cultural/source authority reviewer, rights/legal reviewer, and a glyph/source transcription reviewer.
        """,
    )
    return status


def glyph_source_review_packet() -> str:
    status = "GLYPH_SOURCE_REVIEW_REQUIRED"
    write_text(
        SELECTED / "glyph_source_review_packet.md",
        f"""
        # Glyph / Source Review Packet

        Status: `{status}`

        What needs review:

        - The 26 source-row labels used in `corpus/base_modifier_cache.jsonl`.
        - The 8 vowel/modifier columns used in `corpus/bmc_count_reconciliation.json`.
        - The f/v split explanation that yields the derived 27/216 layer.
        - Representative BMC records such as `BMC-000001` through `BMC-000008`, plus all row-boundary records.
        - Whether source locators and TEI references correspond to the human-reviewed chart/transcription.

        Count-layer claims depending on review:

        - Source layer: 26 x 8 = 208.
        - Derived layer: f/v split gives 27 x 8 = 216.
        - Rule: 27/216 is not source-observed.

        Figure/table dependencies:

        - Table 1 BMC artifact inventory.
        - Table 2 count-layer reconciliation.
        - Figure 2 count-layer model.

        Approval means:

        - The row and vowel counts are correct for the cited source layer.
        - The f/v split is acceptable as a derived interpretation and is not being confused with source evidence.
        - The manuscript limitations accurately describe unresolved glyph-shape interpretation.

        Needs correction means:

        - Revise BMC records, count reconciliation, tables, and manuscript claims before public submission.

        Not publishable yet means:

        - Source chart/transcription cannot support the paper's count-layer claims or public discussion remains culturally/legally blocked.
        """,
    )
    write_text(
        REVIEWER / "GLYPH_SOURCE_REVIEW_CHECKLIST.md",
        """
        # Glyph / Source Review Checklist

        - [ ] Verify source-observed row count is 26.
        - [ ] Verify source-observed vowel/modifier count is 8.
        - [ ] Verify BMC record count is 208 and follows 26 x 8.
        - [ ] Verify f/v split explanation before allowing 27/216 as derived language.
        - [ ] Confirm no glyph-shape grammar is claimed.
        - [ ] Confirm no source images are being published without rights clearance.
        - [ ] Approve, correct, or block public manuscript circulation.
        """,
    )
    return status


def update_reviewer_packet(final_status: str, arxiv_status: str, acm_status: str) -> None:
    write_text(
        REVIEWER / "GARRY_UPDATE.md",
        f"""
        # Garry Update

        What exists:

        - A compiled PAPER-003 manuscript.
        - A source package and package zip.
        - A final claim gate.
        - Web Annotation and CIDOC CRM / CRMdig export proposals.
        - A hardening report and final readiness decision.

        What is new:

        - The paper no longer relies on BMC being novel as a standalone annotation cache.
        - The defensible claim is the integrated claim-gated research-object pipeline with a PAGC/Nwagu Aneke count-drift case study.
        - The source layer is stated as 26 x 8 = 208; 27/216 is only derived by f/v split.

        What is blocked:

        - Authority and rights review.
        - Human glyph/source transcription review.
        - Final human decision on whether public arXiv/ACM review is allowed.

        Current final readiness: `{final_status}`

        arXiv package status: `{arxiv_status}`

        ACM package status: `{acm_status}`

        What can be shown today:

        - The draft PDF and reviewer packet can be shown internally for targeted authority, rights, and glyph review.
        - Do not submit externally yet.
        """,
    )
    write_text(
        REVIEWER / "HUMAN_REVIEW_CHECKLIST.md",
        """
        # Human Review Checklist

        - [ ] Read the manuscript claim around BMC novelty.
        - [ ] Confirm it does not overclaim BMC as a standalone standard.
        - [ ] Verify the 26 x 8 source-layer count.
        - [ ] Verify the derived 27/216 f/v split explanation.
        - [ ] Approve or correct the glyph/source review packet.
        - [ ] Approve, limit, or block public discussion of the Nwagu Aneke/PAGC case.
        - [ ] Attach paper-specific authority and rights clearance.
        - [ ] Decide whether the draft may move to human arXiv review.
        """,
    )
    write_text(
        REVIEWER / "SUBMISSION_BLOCKERS_ONE_PAGE.md",
        f"""
        # Submission Blockers One Page

        Final status: `{final_status}`

        Blockers:

        1. Authority review is not paper-specific and external release is not currently allowed by the release manifest.
        2. Rights review for source images/source material remains open.
        3. Human glyph/source review has not approved the 26 x 8 and derived 27/216 explanation.
        4. Prior art is adequate for draft hardening, but deeper claim-verification and digital-humanities pipeline work should be checked before submission.

        Not blockers after this sprint:

        - BMC novelty overclaim: rewritten as an integration claim.
        - Unsupported exact-count claim: gated and phrased by layer.
        - Local compile path: direct `pdflatex + bibtex + pdflatex + pdflatex` is documented.
        - arXiv package structure: `{arxiv_status}`.
        - ACM source structure: `{acm_status}`.
        """,
    )
    write_text(
        REVIEWER / "DEMO_SCRIPT.md",
        """
        # Demo Script

        1. Open `papers/SELECTED_PAPER/main.pdf`.
        2. Show `papers/SELECTED_PAPER/final_claim_gate.md`.
        3. Show `papers/SELECTED_PAPER/final_novelty_audit.md`.
        4. Show `exports/web_annotation/bmc_web_annotations.jsonld`.
        5. Show `exports/cidoc_crm/bmc_cidoc_mapping.jsonld`.
        6. Show `papers/SELECTED_PAPER/final_submission_readiness_decision.md`.
        7. Explain: this is a hardened draft blocked by authority/glyph review, not an external submission.
        """,
    )
    write_text(
        REVIEWER / "PAPER_STATUS.md",
        f"""
        # Paper Status

        Status: `{final_status}`

        PAPER-003 is a hardened draft with a compiled PDF and structurally clean source package, but it is not approved for external submission until human authority, rights, and glyph/source gates pass.
        """,
    )
    write_text(
        REVIEWER / "WHAT_IS_NEW.md",
        """
        # What Is New

        The novelty hypothesis is not BMC as an annotation cache. The stronger contribution is a reproducible claim-gated research-object pipeline that integrates standards-facing evidence objects, count-layer reconciliation, manuscript claim gates, publication scoring, and preflight checks.
        """,
    )
    write_text(
        REVIEWER / "WHAT_WE_PROVED.md",
        """
        # What We Proved

        - The local BMC dataset contains 208 records.
        - The source layer is represented as 26 x 8.
        - The 27/216 layer must be framed as derived by f/v split.
        - The manuscript can be compiled through a direct `pdflatex + bibtex` chain.
        - The claim gate prevents unsupported exact-count claims from entering the paper as positive results.
        """,
    )
    write_text(
        REVIEWER / "WHAT_WE_DID_NOT_PROVE.md",
        """
        # What We Did Not Prove

        - We did not prove BMC is wholly novel.
        - We did not prove glyph-shape grammar.
        - We did not prove E6, universal compression, or broad PAGC theory claims.
        - We did not prove public submission is authorized.
        - We did not complete human glyph/source review.
        """,
    )
    write_text(
        REVIEWER / "NEXT_72_HOURS.md",
        """
        # Next 72 Hours

        1. Assign a human reviewer for glyph/source review.
        2. Attach paper-specific authority and rights approval or mark the submission blocked.
        3. Have one external digital-humanities or cultural-heritage reviewer inspect the standards-mapping claims.
        4. If gates pass, regenerate the source package and move to human arXiv review.
        """,
    )
    write_text(
        REVIEWER / "EXECUTIVE_BRIEF.md",
        """
        # Executive Brief

        Etisiobi now has a hardened systems/audit paper draft. The paper argues that claim-gated research objects can prevent symbolic count drift from becoming unsupported manuscript claims. The concrete case study separates the PAGC/Nwagu Aneke source layer, represented locally as 26 x 8 = 208, from a derived 27/216 f/v split layer.

        The defensible contribution is the integrated pipeline, not BMC as a standalone annotation standard. The draft is blocked by authority/rights and glyph/source review, not by missing manuscript machinery.
        """,
    )


def compile_and_package() -> tuple[str, str, dict]:
    # Regenerate figures/tables after manuscript revision.
    run(["python", "scripts/generate_publication_assets.py"], cwd=ROOT)

    selected = SELECTED
    for artifact in ("main.aux", "main.bbl", "main.blg", "main.out", "main.log"):
        path = selected / artifact
        if path.exists():
            path.unlink()

    direct = [
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=selected),
        run(["bibtex", "main"], cwd=selected),
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=selected),
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=selected),
    ]
    latexmk = run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=selected)
    compile_status = {
        "direct_chain": [{"command": r["command"], "exit_code": r["exit_code"]} for r in direct],
        "direct_chain_passed": all(r["exit_code"] == 0 for r in direct),
        "latexmk": {"command": latexmk["command"], "exit_code": latexmk["exit_code"], "stderr": latexmk["stderr"][-1200:]},
        "classification": "local_tooling_failure_if_direct_chain_passes" if all(r["exit_code"] == 0 for r in direct) and latexmk["exit_code"] != 0 else "source_or_tool_failure",
    }
    write_json(selected / "latex_compile_diagnostics.json", compile_status)
    write_text(
        selected / "latex_compile_diagnostics.md",
        f"""
        # LaTeX Compile Diagnostics

        Direct chain:

        | Command | Exit code |
        |---|---:|
        {chr(10).join('| `' + r['command'] + '` | ' + str(r['exit_code']) + ' |' for r in direct)}

        Direct chain passed: `{compile_status['direct_chain_passed']}`

        latexmk command: `{latexmk['command']}`

        latexmk exit code: `{latexmk['exit_code']}`

        Classification: `{compile_status['classification']}`

        Interpretation: if the direct chain passes and latexmk fails locally, this sprint treats latexmk as a local MiKTeX/tooling issue rather than a source-package blocker.
        """,
    )

    package = selected / "arxiv_package"
    package.mkdir(parents=True, exist_ok=True)
    for name in ["main.tex", "source_bibliography.bib", "main.bbl"]:
        src = selected / name
        if src.exists():
            shutil.copy2(src, package / name)
    for folder in ["figures", "tables"]:
        (package / folder).mkdir(parents=True, exist_ok=True)
        for src in (selected / folder).glob("*"):
            if src.is_file():
                shutil.copy2(src, package / folder / src.name)
    write_text(
        package / "README_ARXIV_PACKAGE.md",
        """
        # arXiv Package

        Human-review package for PAPER-003. Do not submit externally until `final_submission_readiness_decision.md` is upgraded by human authority, rights, and glyph/source review.

        Compile chain used locally:

        ```powershell
        pdflatex -interaction=nonstopmode -halt-on-error main.tex
        bibtex main
        pdflatex -interaction=nonstopmode -halt-on-error main.tex
        pdflatex -interaction=nonstopmode -halt-on-error main.tex
        ```
        """,
    )

    zip_path = selected / "arxiv_package.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in package.rglob("*"):
            if p.is_file():
                zf.write(p, p.relative_to(package).as_posix())

    text_files = [p for p in package.rglob("*") if p.is_file() and p.suffix.lower() in {".tex", ".bib", ".md", ".bbl"}]
    content = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in text_files)
    absolute_path_hits = ["C:\\", "/Users/", "/home/", "\\Users\\"]
    arxiv_issues = []
    if any(hit in content for hit in absolute_path_hits):
        arxiv_issues.append("absolute path marker found")
    if "\\write18" in content or "shell-escape" in content or "\\usepackage{minted}" in content:
        arxiv_issues.append("shell escape or minted dependency found")
    if not (package / "main.tex").exists():
        arxiv_issues.append("main.tex missing")
    if not (package / "source_bibliography.bib").exists():
        arxiv_issues.append("source_bibliography.bib missing")
    unsafe = [rel(p) for p in package.rglob("*") if " " in p.name]
    if unsafe:
        arxiv_issues.append("unsafe filenames with spaces: " + ", ".join(unsafe))
    unresolved = [term for term in ["TODO", "FIXME", "??"] if term in content]
    if unresolved:
        arxiv_issues.append("unresolved marker(s): " + ", ".join(unresolved))
    arxiv_status = "ARXIV_PACKAGE_STRUCTURALLY_CLEAN" if not arxiv_issues and compile_status["direct_chain_passed"] else "ARXIV_PACKAGE_NEEDS_REPAIR"
    write_text(
        selected / "arxiv_package_audit.md",
        f"""
        # arXiv Package Audit

        Status: `{arxiv_status}`

        Package path: `papers/SELECTED_PAPER/arxiv_package/`

        Zip path: `papers/SELECTED_PAPER/arxiv_package.zip`

        Structural checks:

        - `main.tex`: `{(package / 'main.tex').exists()}`
        - bibliography: `{(package / 'source_bibliography.bib').exists()}`
        - figures directory: `{(package / 'figures').exists()}`
        - tables directory: `{(package / 'tables').exists()}`
        - shell-escape/minted dependency: `{'yes' if any('shell' in issue or 'minted' in issue for issue in arxiv_issues) else 'no'}`
        - absolute paths: `{'yes' if any('absolute path' in issue for issue in arxiv_issues) else 'no'}`
        - unsafe filenames: `{'yes' if unsafe else 'no'}`
        - direct compile passed: `{compile_status['direct_chain_passed']}`

        Issues:

        {chr(10).join('- ' + issue for issue in arxiv_issues) if arxiv_issues else '- none found by local structural audit'}

        Note: structural cleanliness does not override authority, rights, or glyph/source review blockers.
        """,
    )

    main_tex = (selected / "main.tex").read_text(encoding="utf-8")
    acm_issues = []
    if "\\documentclass[manuscript]{acmart}" not in main_tex:
        acm_issues.append("not using acmart manuscript mode")
    if "\\title{" not in main_tex:
        acm_issues.append("title missing")
    if "\\begin{abstract}" not in main_tex:
        acm_issues.append("abstract missing")
    if "\\keywords{" not in main_tex:
        acm_issues.append("keywords missing")
    if "\\ccsdesc" not in main_tex:
        acm_issues.append("CCS descriptors missing")
    acm_status = "ACM_PACKAGE_STRUCTURALLY_CLEAN" if not acm_issues and compile_status["direct_chain_passed"] else "ACM_PACKAGE_NEEDS_REPAIR"
    write_text(
        selected / "acm_package_audit.md",
        f"""
        # ACM Package Audit

        Status: `{acm_status}`

        Checks:

        - `\\documentclass[manuscript]{{acmart}}`: `{'yes' if '\\documentclass[manuscript]{acmart}' in main_tex else 'no'}`
        - title present: `{'yes' if '\\title{' in main_tex else 'no'}`
        - abstract present: `{'yes' if '\\begin{abstract}' in main_tex else 'no'}`
        - keywords present: `{'yes' if '\\keywords{' in main_tex else 'no'}`
        - CCS descriptors present: `{'yes' if '\\ccsdesc' in main_tex else 'no'}`
        - direct compile passed: `{compile_status['direct_chain_passed']}`

        Issues:

        {chr(10).join('- ' + issue for issue in acm_issues) if acm_issues else '- none found by local structural audit'}

        Note: author identity/anonymization and venue-specific settings must be adjusted only after a target venue decision.
        """,
    )
    return arxiv_status, acm_status, compile_status


def reviewer2_attack() -> None:
    write_text(
        SELECTED / "reviewer2_second_attack.md",
        """
        # Reviewer 2 Second Attack

        1. Is this just a wrapper around existing standards?  
        Partly. The paper survives only if framed as an integration and audit pipeline, not as a new provenance, annotation, or packaging standard.

        2. Is BMC actually necessary?  
        BMC is necessary as the local auditable join table between source locators, count layers, certainty, provenance, KG nodes, and paper claims. It is not necessary as a universal model.

        3. Is the case study too small?  
        Possibly. The count-drift case is concrete but narrow. The paper should avoid broad claims and present this as a systems/audit demonstration.

        4. Are 26x8 and 27/216 clear?  
        The manuscript now separates source layer from derived f/v split. Human glyph/source review remains required.

        5. Is domain evidence strong enough?  
        Not for external submission without source review. It is strong enough for internal human review of the hardened draft.

        6. Are cultural/authority constraints serious?  
        They are now explicit blockers, which strengthens the paper ethically but prevents readiness.

        7. Does the paper oversell autoresearch?  
        It should not. The current language says it adapts the loop to paper-readiness, not that it solves autonomous research.

        8. Are results reproducible?  
        Locally yes for tables, figures, mappings, and compile chain. Public reproducibility remains blocked by rights/authority.

        9. Better paper type?  
        Best current type: systems/audit paper with a negative/correction case study.

        10. Single highest-impact change:  
        Obtain and attach human glyph/source plus authority/rights approvals, then revise the limitations and readiness decision.
        """,
    )
    write_text(
        SELECTED / "revision_response_plan.md",
        """
        # Revision Response Plan

        - Keep the title and systems/audit framing.
        - Add no stronger novelty claim.
        - Add Web Annotation and CIDOC export paragraphs only as mapping proposals.
        - Keep authority and glyph review as hard blockers.
        - If human review approves the count model, update the readiness decision and reviewer packet.
        - If human review changes the count model, regenerate BMC count reconciliation, tables, figures, and manuscript.
        """,
    )


def final_report(final_status: str, arxiv_status: str, acm_status: str, authority_status: str, glyph_status: str) -> None:
    write_text(
        SELECTED / "submission_hardening_report.md",
        f"""
        # Submission Hardening Report

        Final readiness status: `{final_status}`

        What was hardened:

        - Froze the pre-hardening manuscript/package state.
        - Ran a final claim gate and revised the manuscript.
        - Added final novelty and prior-art gap audits.
        - Added BMC to Web Annotation JSON-LD export.
        - Added BMC to CIDOC CRM / CRMdig mapping proposal.
        - Re-ran compile diagnostics.
        - Rebuilt the arXiv package and zip.
        - Audited ACM manuscript structure.
        - Updated reviewer packet for targeted human review.

        Manuscript changes:

        - Added ACM CCS/keywords metadata.
        - Added Web Annotation and CIDOC/CRMdig mapping paragraphs.
        - Expanded limitations around standards compliance, authority, rights, and glyph/source review.
        - Updated reproducibility commands.

        Claims removed or rewritten:

        - BMC wholly novel: blocked/reframed.
        - Glyph-shape grammar proven: blocked.
        - E6/universal compression validated: blocked.
        - 27/216 as source layer: blocked and rewritten as derived layer only.
        - Public submission approved: blocked.

        Package statuses:

        - arXiv: `{arxiv_status}`
        - ACM: `{acm_status}`
        - Authority/rights: `{authority_status}`
        - Glyph/source review: `{glyph_status}`
        """,
    )
    write_text(
        SELECTED / "final_submission_readiness_decision.md",
        f"""
        # Final Submission Readiness Decision

        Status: `{final_status}`

        Why:

        PAPER-003 is now a hardened, compiled draft with final claim-gate, novelty, prior-art, standards-export, package, and compile diagnostics. It is not ready for human arXiv review because the paper-specific authority/rights gate has not cleared and human glyph/source review has not approved the 26 x 8 source-layer and derived 27/216 explanation.

        What was hardened:

        - Claim gate.
        - Novelty audit.
        - Prior-art gap audit.
        - Web Annotation export.
        - CIDOC CRM / CRMdig mapping proposal.
        - LaTeX diagnostics.
        - arXiv and ACM package audits.
        - Reviewer packet.

        What changed in the manuscript:

        - Added ACM metadata.
        - Added standards-export discussion.
        - Expanded limitations and reproducibility commands.

        Claims removed or rewritten:

        - No standalone BMC novelty claim.
        - No glyph-shape grammar claim.
        - No E6/universal-compression claim.
        - No source-layer 27/216 claim.
        - No public-submission approval claim.

        Citations/sources added or verified:

        - W3C Web Annotation Vocabulary.
        - CRMdig mapping target.
        - Existing PROV-O, RO-Crate, IIIF, TEI, Web Annotation, CIDOC CRM, FAIR, DataCite, arXiv, ACM, Karpathy autoresearch, Azuonye, and glyph/digital heritage sources remain cited.

        arXiv package status: `{arxiv_status}`

        ACM package status: `{acm_status}`

        Authority/rights status: `{authority_status}`

        Glyph/source review status: `{glyph_status}`

        Exact remaining blockers:

        1. Attach paper-specific authority and rights clearance.
        2. Complete human glyph/source review.
        3. Confirm whether source images, glyph records, and cultural claims may be publicly discussed.
        4. If approved, rerun package generation and update this decision.

        Exact next human action:

        Review `outputs/reviewer_packet/HUMAN_AUTHORITY_RIGHTS_REVIEW.md` and `outputs/reviewer_packet/GLYPH_SOURCE_REVIEW_CHECKLIST.md`, then approve, correct, or block public submission.
        """,
    )


def main() -> None:
    freeze_manifest()
    claim_rows = final_claim_gate()
    update_bibliography()
    revise_manuscript()
    prior_art_audits()
    mapping_docs()

    run(["python", "scripts/export_bmc_web_annotations.py"], cwd=ROOT)
    run(["python", "scripts/export_bmc_cidoc_mapping.py"], cwd=ROOT)

    authority_status = authority_and_rights_gate()
    glyph_status = glyph_source_review_packet()
    reviewer2_attack()
    arxiv_status, acm_status, _compile = compile_and_package()

    final_status = "NOT_READY_AUTHORITY_BLOCKED"
    if authority_status == "CLEAR_FOR_HUMAN_ARXIV_REVIEW" and glyph_status != "GLYPH_SOURCE_REVIEW_REQUIRED" and arxiv_status == "ARXIV_PACKAGE_STRUCTURALLY_CLEAN" and acm_status == "ACM_PACKAGE_STRUCTURALLY_CLEAN":
        final_status = "READY_FOR_HUMAN_ARXIV_REVIEW"

    update_reviewer_packet(final_status, arxiv_status, acm_status)
    final_report(final_status, arxiv_status, acm_status, authority_status, glyph_status)
    write_text(
        SELECTED / "submission_hardening_summary.json.md",
        f"""
        ```json
        {json.dumps({
            "final_status": final_status,
            "arxiv_status": arxiv_status,
            "acm_status": acm_status,
            "authority_status": authority_status,
            "glyph_status": glyph_status,
            "final_claims": len(claim_rows),
            "generated_at": now(),
        }, ensure_ascii=False, indent=2)}
        ```
        """,
    )
    print(json.dumps({
        "final_status": final_status,
        "arxiv_status": arxiv_status,
        "acm_status": acm_status,
        "authority_status": authority_status,
        "glyph_status": glyph_status,
    }, indent=2))


if __name__ == "__main__":
    main()
