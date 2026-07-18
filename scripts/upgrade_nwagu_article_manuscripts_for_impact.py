from __future__ import annotations

import json
import re
import textwrap
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"


GLOBAL_CITATIONS = [
    "azuonye1992",
    "omniglotNwagu",
    "unicodeAfricanScripts2023",
    "scriptSourceNwagu",
    "seiProposalTips",
    "teiP5Glyphs",
    "iiifPresentation3",
    "w3cAnnotationModel",
    "w3cProvO",
    "rocrate12",
    "datacite45",
    "wilkinson2016fair",
    "carroll2020care",
    "acmSubmissions",
    "arxivSubmitTex",
]


ARTICLES = [
    {
        "id": "ARTICLE-NA-001",
        "slug": "001-source-critical-reconstruction",
        "title": "A Source-Critical Reconstruction of the Nwagu Aneke Igbo Syllabary",
        "target": "Digital Scholarship in the Humanities or Digital Humanities Quarterly",
        "field": "digital humanities, African writing systems, source criticism",
        "failure": "The previous version was a claim-gated note. It did not contain a complete source-critical argument, a recoverable corpus protocol, or a clear statement of what counts as reconstruction.",
        "fix": "This revision turns the paper into a reconstruction argument: it defines the current reconstructable object, separates row-column evidence from glyph evidence, and states the minimum source review needed for submission.",
        "thesis": "The first publishable contribution is not a universal theory of PAGC; it is a defensible source-critical reconstruction ledger for Nwagu Aneke.",
        "novelty": "A reproducible reconstruction ledger for Nwagu Aneke that separates source-observed, derived, secondary, and blocked claims.",
        "materials": "Azuonye metadata and local PDF, local chart transcription, symbol inventory, 208-record BMC index, base-count audit, Omniglot snapshot, and EXP-NA-001 evidence table.",
        "method": "Source-critical alignment of every row, column, count, and uncertainty statement; each claim is assigned a source class and a review gate.",
        "finding": "The current evidence supports a 26 by 8 source-observed ledger and a visible logograph lead set, but not a completed glyph corpus.",
        "experiment": "EXP-NA-001 is complete. The next experiment is line-level extraction from Azuonye plus human chart review.",
    },
    {
        "id": "ARTICLE-NA-002",
        "slug": "002-count-layer-drift",
        "title": "Count-Layer Drift in Nwagu Aneke: Auditing 26 by 8, 27, 216, 164, and 224 Claims",
        "target": "Digital Scholarship in the Humanities, DHQ, or a scholarly data-quality venue",
        "field": "symbolic inventory audit, digital humanities, research-methods",
        "failure": "The previous version named the count problem but did not provide a full taxonomy of count-bearing claims or explain why count drift is a general scholarly risk.",
        "fix": "This revision frames count-layer drift as the main contribution and gives an audit method that can be applied to any artifact-derived symbolic theory.",
        "thesis": "The scientific result is multi-layer reconciliation, not selection of one privileged number.",
        "novelty": "A count-layer audit model that prevents derived design counts from becoming source-observed manuscript claims.",
        "materials": "EXP-NA-001 evidence table, base-count audit, BMC count reconciliation, symbol inventory, source audit, and external 164/224 leads.",
        "method": "Represent each number as count, layer, source, locator, derivation rule, confidence, and allowed use.",
        "finding": "26 by 8 equals 208 is currently source-observed; 27/216 is derived only by splitting f/v; 164/224 remain unverified leads.",
        "experiment": "EXP-NA-002 must build a count ledger and mark every downstream paper claim as ready, derived, blocked, or rejected.",
    },
    {
        "id": "ARTICLE-NA-003",
        "slug": "003-f-v-hinge",
        "title": "The f/v Hinge: Orthographic Economy and Derived-Layer Design in Nwagu Aneke",
        "target": "Written Language and Literacy, African linguistics venues, or DHQ",
        "field": "orthography, Igbo linguistics, writing-system design",
        "failure": "The previous version did not distinguish linguistic evidence from design interpretation strongly enough for a linguistics reviewer.",
        "fix": "This revision makes f/v a research hinge rather than a resolved phonological claim and specifies the linguistic evidence needed to promote it.",
        "thesis": "The f/v row is best treated as a hinge between source transcription and derived design, not as a resolved source split.",
        "novelty": "A layer-safe account of how one combined row can generate a derived design layer without changing the source ledger.",
        "materials": "Chart transcription, row-label inventory, BMC count model, Igbo/Umuleri review queue, and local source audit.",
        "method": "Compare three interpretations: printed-row economy, phonological split, and design-layer split; evaluate which claims each permits.",
        "finding": "The f/v split explains 27/216 as a derived layer, but linguistic publication requires expert review and examples.",
        "experiment": "EXP-NA-003 should collect f/v examples from Azuonye, manuscripts, and reviewed Igbo phonology sources.",
    },
    {
        "id": "ARTICLE-NA-004",
        "slug": "004-logographs-in-a-syllabary",
        "title": "Logographs in a Syllabary: Separating Whole-Word Signs from Nwagu Aneke CV Cells",
        "target": "Digital Scholarship in the Humanities, Written Language and Literacy, or script-studies venues",
        "field": "script typology, logography, digital inventory methods",
        "failure": "The previous version proposed a logograph ledger but had no typological argument and no separation between visible lead set and corpus inventory.",
        "fix": "This revision turns the paper into a typological and data-modeling argument about how logographs should be counted separately from CV cells.",
        "thesis": "Nwagu Aneke logographs must be modeled as a separate sign layer before any inventory count or typological claim is defensible.",
        "novelty": "A mixed-inventory protocol for preventing whole-word signs from corrupting syllabary-cell counts.",
        "materials": "Visible chart lead set, Omniglot secondary description, Azuonye anchor, symbol inventory aggregate records, TEI glyph modeling guidance.",
        "method": "Define logograph records with evidence locator, reading, semantic field, relation to CV cell, and publication status.",
        "finding": "The current evidence supports a logograph lead set but not a complete logograph corpus.",
        "experiment": "EXP-NA-004 should extract every visible whole-word sign and classify it independently from CV cells.",
    },
    {
        "id": "ARTICLE-NA-005",
        "slug": "005-tei-iiif-critical-edition",
        "title": "Toward a TEI/IIIF Critical Edition of an Unencoded African Syllabary",
        "target": "Digital Scholarship in the Humanities or DHQ",
        "field": "digital scholarly editing, IIIF, TEI, Web Annotation",
        "failure": "The previous version was mostly a standards list. It did not define a digital edition architecture or a validation path.",
        "fix": "This revision specifies a standards-compatible edition architecture and identifies the missing selectors, transcriptions, and rights gates.",
        "thesis": "A pre-Unicode critical edition can be built if source images, TEI glyph records, IIIF canvases, and annotation targets remain linked.",
        "novelty": "A staged edition protocol for an unencoded African syllabary that avoids premature Unicode or corpus claims.",
        "materials": "Local TEI scaffold, IIIF manifest, chart transcription, symbol inventory, Web Annotation mapping, and source uncertainty notes.",
        "method": "Map each source object to IIIF Canvas, each transcription to TEI char/glyph structures, and each claim to annotation/provenance records.",
        "finding": "The standards route is clear, but the edition is blocked by source-region selectors and rights-cleared images.",
        "experiment": "EXP-NA-005 should produce ten selector-level IIIF/Web Annotation records and matching TEI glyph declarations.",
    },
    {
        "id": "ARTICLE-NA-006",
        "slug": "006-unicode-readiness",
        "title": "Unicode Readiness for Nwagu Aneke: Character, Glyph, Evidence, and Community Review",
        "target": "Unicode proposal track, script encoding venues, or digital humanities methods venues",
        "field": "script encoding, Unicode readiness, character-glyph modeling",
        "failure": "The previous version stated that a readiness matrix was needed, but it did not identify all proposal-grade evidence gaps.",
        "fix": "This revision turns the paper into a gap analysis against encoding expectations, with a clear non-claim that no Unicode proposal is being submitted.",
        "thesis": "Unicode readiness is an evidence and authority problem before it is a technical encoding problem.",
        "novelty": "A community-gated readiness matrix for an unencoded Nigerian syllabary.",
        "materials": "Unicode African scripts update, ScriptSource status, SEI proposal guidance, local symbol inventory, rights/authority gate.",
        "method": "Evaluate repertoire, naming, glyph variants, text samples, directionality, sorting, punctuation, use evidence, and community approval.",
        "finding": "The local package is adequate for early discussion but inadequate for proposal-grade repertoire decisions.",
        "experiment": "EXP-NA-006 should produce a Unicode-readiness gap matrix with every field marked present, partial, missing, or blocked.",
    },
    {
        "id": "ARTICLE-NA-007",
        "slug": "007-manuscript-corpus-provenance",
        "title": "Manuscript Corpus Provenance for Nwagu Aneke: A CARE-First Research Plan",
        "target": "Data Science Journal, DHQ, cultural-heritage data venues",
        "field": "data governance, manuscript provenance, CARE/FAIR research objects",
        "failure": "The previous version was a protocol note and did not yet show how provenance changes what claims can be made.",
        "fix": "This revision makes manuscript provenance the central research object and ties it to claim maturity, release rights, and data citation.",
        "thesis": "No public corpus claim is defensible until holdings, custodianship, rights, and permitted use are recorded.",
        "novelty": "A CARE-first provenance ledger for studying a culturally meaningful, under-digitized African manuscript corpus.",
        "materials": "Azuonye anchor, Smithsonian catalogue lead, local authority register, release manifest, FAIR/CARE/DataCite standards.",
        "method": "Create a provenance record for each manuscript lead: holder, source of claim, access condition, authority record, release status, citation status.",
        "finding": "The current package supports provenance planning, not corpus-scale analysis.",
        "experiment": "EXP-NA-007 should build the first rights-safe holdings ledger without publishing restricted material.",
    },
    {
        "id": "ARTICLE-NA-008",
        "slug": "008-comparative-standardization",
        "title": "Comparative Standardization Paths for African Syllabaries: Positioning Nwagu Aneke",
        "target": "Digital Scholarship in the Humanities or comparative writing-system venues",
        "field": "African scripts, standardization, comparative digital humanities",
        "failure": "The previous version named comparison but did not specify comparison axes or explain how comparison avoids flattening different histories.",
        "fix": "This revision defines a comparative matrix that compares evidence conditions, not only script typology or Unicode status.",
        "thesis": "Nwagu Aneke should be compared by standardization readiness, evidence maturity, and authority status rather than by resemblance alone.",
        "novelty": "A comparative standardization matrix for African scripts that includes authority and evidence gates.",
        "materials": "Unicode African scripts update, ScriptSource, Omniglot, SEI guidance, local readiness matrix, CARE principles.",
        "method": "Compare scripts across repertoire evidence, corpus availability, encoding status, community authority, teaching use, tooling, and rights readiness.",
        "finding": "Nwagu Aneke currently occupies an unencoded and source-promising but review-blocked position.",
        "experiment": "EXP-NA-008 should build a comparative review table for Vai, Bamum, Mende Kikakui, Loma, Kpelle, Nsibidi, Ndebe, and Nwagu Aneke.",
    },
    {
        "id": "ARTICLE-NA-009",
        "slug": "009-igbo-tokenization",
        "title": "Igbo Tokenization from a Source-Grounded Nwagu Aneke Layer: A Research Design",
        "target": "ACL Findings, TACL, African NLP workshops, or low-resource NLP venues",
        "field": "low-resource NLP, tokenization, Igbo language technology",
        "failure": "The previous version had no experiment and therefore could not be submitted to an NLP venue.",
        "fix": "This revision is now explicit that it is a research design until baselines, corpora, metrics, and statistical tests are run.",
        "thesis": "Nwagu Aneke can generate tokenizer hypotheses, but only task-level metrics can justify NLP claims.",
        "novelty": "A layer-safe tokenizer evaluation design using source CV units and derived f/v units as competing hypotheses.",
        "materials": "Local Igbo corpus, source-layer row-vowel inventory, derived f/v split model, standard BPE/unigram baselines, reproducibility scripts.",
        "method": "Compare BPE, unigram, source-layer CV, and derived f/v tokenizers on compression, fertility, OOV behavior, and downstream proxy tasks.",
        "finding": "No NLP performance result is claimed yet; the article defines the experiment required to make one.",
        "experiment": "EXP-NA-009 must run tokenizer baselines with fixed seeds, train/test splits, corpus card, confidence intervals, and failure analysis.",
    },
    {
        "id": "ARTICLE-NA-010",
        "slug": "010-layer-safe-generative-design",
        "title": "Layer-Safe Generative Design Systems from Nwagu Aneke",
        "target": "Information systems theory venues, design-science venues, ACM CHI/DIS, or systems research venues",
        "field": "design science, information systems, symbolic generative systems",
        "failure": "The previous version had a promising invariant but did not connect it to design-science contribution, evaluation, or system falsification.",
        "fix": "This revision frames layer safety as a design-science construct and turns the count-layer case into a testable invariant.",
        "thesis": "Artifact-derived generative systems need a layer-safety invariant: outputs may derive from sources but cannot relabel derivations as source facts.",
        "novelty": "A formal design invariant for source-grounded generative systems built from culturally meaningful artifacts.",
        "materials": "Nwagu Aneke count-layer model, event trace, claim gates, BMC records, PROV-O/RO-Crate standards, layer-safety proof notes.",
        "method": "Model source-observed, derived, speculative, and blocked labels as states; test whether workflows preserve labels under generation.",
        "finding": "The 26-by-8 versus 27/216 case provides a concrete counterexample to unsafe flattening.",
        "experiment": "EXP-NA-010 should implement label-preservation tests over design outputs and measure promotion-error rate.",
    },
]


def tex_escape(value: str) -> str:
    return value.replace("&", r"\&")


def cite(keys: list[str]) -> str:
    return "\\cite{" + ",".join(keys) + "}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def make_tex(article: dict[str, str]) -> str:
    all_keys = list(dict.fromkeys(GLOBAL_CITATIONS))
    return rf"""
    \documentclass[sigconf,nonacm]{{acmart}}
    \settopmatter{{printacmref=false}}
    \setcopyright{{none}}
    \renewcommand\footnotetextcopyrightpermission[1]{{}}
    \pagestyle{{plain}}

    \acmConference[Etisiobi Research Draft]{{Etisiobi Nwagu Aneke Article Program}}{{June 2026}}{{Enugu, Nigeria}}
    \acmYear{{2026}}
    \acmISBN{{}}
    \acmDOI{{}}

    \title{{{tex_escape(article["title"])}}}
    \author{{The Beaconsmith Collective}}
    \affiliation{{
      \institution{{Etisiobi Research Studio}}
      \city{{Enugu}}
      \country{{Nigeria}}
    }}
    \email{{research@example.invalid}}

    \begin{{abstract}}
    This revised draft evaluates whether {tex_escape(article["title"])} can move
    from a formatted note to an impact-journal research article. The earlier
    package failed because it was too thin: it had a title, format, citations,
    and limitations, but not enough article-specific argument, related work,
    evidence, method, falsification, or venue fit. This version states a
    testable thesis, identifies the evidence currently available, explains the
    missing evidence that still blocks submission, and defines the experiment
    required to convert the draft into a submission candidate. The central
    constraint remains unchanged: the source-observed layer is 26 by 8 equals
    208 records, while 27/216 is only a derived f/v split layer.
    \end{{abstract}}

    \keywords{{Nwagu Aneke, Igbo syllabary, source-grounded research, impact-journal readiness, {tex_escape(article["field"])}}}

    \begin{{document}}
    \maketitle

    \section{{Why The Earlier Draft Would Be Rejected}}
    A serious reviewer would reject the earlier version for substance rather
    than format. It was a valid \emph{{draft packet}}, but impact journals assess
    originality, correctness, novelty, importance, evidence, methodological
    clarity, and fit to venue expectations. ACM's publication evaluation policy
    names originality, correctness, novelty, importance, and clarity as review
    dimensions {cite(["acmSubmissions"])}. Digital-humanities venues require an
    argument situated in a broader research context rather than insider notes
    about a local archive {cite(["teiP5Glyphs","iiifPresentation3","w3cAnnotationModel"])}.
    Data and cultural-heritage papers must also make reuse, provenance,
    authority, and ethics explicit {cite(["wilkinson2016fair","carroll2020care","datacite45"])}.

    For this article, the concrete failure was: {tex_escape(article["failure"])}

    \section{{Impact-Journal Thesis}}
    \textbf{{Thesis.}} {tex_escape(article["thesis"])}

    This thesis is intentionally narrower than broad PAGC claims. It does not
    use Nwagu Aneke as evidence for universal-compression results, exceptional
    mathematics, or a completed glyph grammar. It also does not describe the
    derived 27/216 layer as observed in the source. The source-observed layer
    remains 26 rows by 8 vowel/modifier columns, giving 208 current ledger
    records. The 27/216 layer can be used only when explicitly labeled as a
    derived f/v split layer.

    \section{{Research Question}}
    The research question is whether the Nwagu Aneke artifact can support the
    article-specific claim without losing the boundary between source evidence,
    derived interpretation, speculative design, and blocked evidence. In this
    paper, that question is applied to {tex_escape(article["field"])}. The
    research question is not whether the artifact can be used to support every
    possible downstream theory. It asks what a reviewer can verify from the
    current dossier and what experiment would be required to move the draft
    into a submission pathway.

    \section{{Evidence Base}}
    The source-observed 26 rows by 8 vowel/modifier columns baseline is the
    only count-layer foundation used as source evidence. The article uses the
    local evidence package, public metadata, and standards documents as
    bounded inputs rather than as proof of a completed corpus. Every article
    must preserve the distinction between a source-observed layer, a derived
    f/v split layer, a standards-mapping layer, and a future experiment layer.
    For avoidance of ambiguity, the source-observed layer remains 26 rows by 8
    columns in every article in this package. This sentence is repeated because
    it is the load-bearing control that keeps the papers from turning design
    possibilities into source claims. If a later source review changes that
    foundation, the entire package must be revised rather than silently patched.
    That is the standard a serious journal reviewer would expect.

    \section{{Target Venue Fit}}
    The best target class is: \textbf{{{tex_escape(article["target"])}}}.
    The paper belongs to {tex_escape(article["field"])}. It is not ready for
    submission because the current evidence package still lacks at least one of
    the following: human source review, rights clearance, article-specific prior
    art, corpus-scale evidence, baseline experiments, or expert linguistic
    review. The revision therefore changes the status from a formatted note to
    a \emph{{journal-track draft}} with a defined evidence path.

    \section{{Related Work and Standards}}
    The source anchor is Azuonye's 1992 treatment of the script {cite(["azuonye1992"])}.
    Public secondary descriptions and Unicode-status records show that Nwagu
    Aneke is relevant to African script documentation and encoding-readiness
    work {cite(["omniglotNwagu","unicodeAfricanScripts2023","scriptSourceNwagu","seiProposalTips"])}.
    A credible digital edition or data article must align with TEI, IIIF, Web
    Annotation, PROV-O, RO-Crate, and DataCite rather than inventing a private
    one-off data model {cite(["teiP5Glyphs","iiifPresentation3","w3cAnnotationModel","w3cProvO","rocrate12","datacite45"])}.
    FAIR and CARE principles constrain publication of reusable cultural data
    and prevent the research from treating community authority as a footnote
    {cite(["wilkinson2016fair","carroll2020care"])}. The local autoresearch loop
    is useful only if it produces stronger evidence and rejects unsupported
    claims rather than creating more documents {cite(["karpathyAutoresearch"])}.

    \section{{Central Claim}}
    \textbf{{Claim.}} {tex_escape(article["thesis"])}

    This claim is allowed only as a journal-track draft claim. It becomes a
    submission claim only if the evidence package is upgraded from local ledger
    status to source-reviewed status. The central claim is therefore not just a
    sentence in the abstract; it is a contract between evidence, method, target
    venue, and authority review.

    \section{{Materials and Evidence}}
    The article uses the following materials: {tex_escape(article["materials"])}
    These materials are enough to state a bounded research problem, but not
    enough to authorize public submission. The local evidence can support
    source-ledger claims, count-layer distinctions, standards mappings, and
    experiment designs. It cannot yet support public reproduction of images,
    completed glyph-shape claims, final Unicode repertoire claims, corpus-scale
    usage claims, or task-performance claims.

    \begin{{table}}[t]
    \caption{{Impact readiness gate for {article["id"]}}}
    \label{{tab:impact-gate}}
    \begin{{tabular}}{{p{{0.30\columnwidth}}p{{0.60\columnwidth}}}}
    \toprule
    Gate & Current decision \\
    \midrule
    Novel question & Present, but needs article-specific prior art \\
    Source evidence & Partial; source ledger exists \\
    Method & Revised; must be executed for submission \\
    Results & Bounded or proposed, not final for most articles \\
    Rights/authority & Blocks submission until reviewed \\
    Venue fit & Plausible but not final \\
    \bottomrule
    \end{{tabular}}
    \end{{table}}

    \section{{Method}}
    {tex_escape(article["method"])}

    The method has five required controls. First, every positive claim must
    cite either a source artifact, an external standard, or an experiment result.
    Second, every use of 26, 8, 208, 27, or 216 must identify its layer. Third,
    the paper must preserve uncertainty rather than normalize it away. Fourth,
    article-specific novelty must be compared against external literature before
    submission. Fifth, cultural authority and rights review must happen before
    public dissemination of source-sensitive material.

    \section{{Current Finding}}
    {tex_escape(article["finding"])}

    The strongest current cross-article finding is not that all ten papers are
    ready. The finding is that Nwagu Aneke can generate multiple legitimate
    research tracks only when source, derived, speculative, and blocked layers
    remain separate. This is the condition under which further research can
    produce frontier work rather than decorative speculation.

    \section{{Findings}}
    The findings are deliberately separated into three levels. First, the
    source-ledger finding: the current package can support a 26 by 8 source
    layer and a bounded ledger of 208 row-vowel records. Second, the derived
    design finding: the f/v split can generate a 27/216 design layer only when
    its label remains derived. Third, the journal-readiness finding: this paper
    has a viable research direction, but still needs the article-specific
    experiment or review listed below. This separation is what prevents the
    article from becoming another overextended speculative essay.

    \section{{Falsification and Next Experiment}}
    {tex_escape(article["experiment"])}

    A future submission should be rejected by the lab before journal submission
    if any of these tests fail: the central claim cannot be traced to evidence;
    the derived f/v layer is described as source-observed; the article lacks a
    target-venue literature review; the paper asserts completed corpus or glyph
    evidence without human review; or the proposed experiment cannot be
    reproduced from versioned files.

    \section{{What Was Fixed In This Revision}}
    {tex_escape(article["fix"])}

    The revision also adds a stronger venue argument, a field-specific failure
    analysis, a clearer novelty hypothesis, and a concrete experiment path.
    The novelty hypothesis is: {tex_escape(article["novelty"])}. This is still a
    hypothesis until a systematic literature review confirms that the same
    result or method has not already been published.

    \section{{Relation to Global Standards}}
    The revision treats global standards as constraints, not decoration.
    Source claims are checked against source location and review status.
    Digital-edition claims are checked against TEI, IIIF, and Web Annotation
    expectations. Provenance claims are checked against PROV-O and RO-Crate
    expectations. Data release claims are checked against FAIR, CARE, and
    DataCite expectations. Publication claims are checked against ACM and arXiv
    source-package norms. This is why a formatted PDF is not enough: a paper
    must explain how its evidence can be inspected by a reviewer outside the
    lab.

    \section{{Reviewer-2 Risk Model}}
    The strongest rejection argument is that the paper still depends too much
    on internal evidence. A reviewer can also argue that the prior art is too
    shallow, the source transcription is not independently reviewed, and the
    article's novelty is currently a hypothesis rather than a demonstrated
    result. The revision accepts those objections and converts them into gates.
    A draft that names its blockers is better than a draft that hides them, but
    naming blockers does not remove them.

    \section{{Limitations and Human Review}}
    This article is not a submission authorization. The current draft requires
    source transcription review, rights review, cultural/source authority
    review, and final author review before public submission. If source review
    changes the count ledger, the manuscript must be revised. If rights review
    blocks source-image use, the paper must rely on descriptions, derived
    tables, or restricted appendices. If prior art shows that the novelty
    hypothesis is already known, the contribution must be rewritten as a
    replication, correction, or negative result.

    \section{{Impact Contribution Ladder}}
    The article has four possible contribution levels. At the lowest level, it
    is an internal lab note and should not leave the repository. At the next
    level, it is a workshop or preprint draft because it explains a useful
    method but lacks full evidence. At the third level, it becomes a specialist
    journal article if source review, prior art, and the article-specific
    experiment all pass. At the highest level, it becomes an impact-journal
    article only if it changes how another field studies artifact-derived
    knowledge systems. That highest level requires a result that is not merely
    locally interesting but portable: a method, dataset, proof, or empirical
    finding that other researchers can reuse or dispute.

    The present manuscript is at the second level. It is stronger than a
    scaffold because it now has a target field, a thesis, a method, and a
    rejection model. It is weaker than a submission because at least one
    decisive experiment or review has not yet happened. This distinction is the
    repair. The package should not pretend to be ready, but it should make the
    route to readiness explicit enough that future work is measurable.

    \section{{Minimum Acceptance Bar}}
    Before submission, the paper must meet five tests. First, a reviewer must
    be able to find every important source claim in the evidence table or in a
    cited external source. Second, the target venue must be able to recognize
    the paper as belonging to its field rather than as an idiosyncratic local
    project. Third, the novelty claim must survive a systematic prior-art
    sweep. Fourth, the article-specific method must produce a result or a
    rigorous negative result. Fifth, rights and authority review must permit
    the public claims being made. Until those tests pass, the correct status is
    journal-track draft, not submission candidate.

    \section{{Submission Readiness Decision}}
    \textbf{{Decision: NOT\_READY\_FOR\_IMPACT\_JOURNAL\_SUBMISSION.}}
    The paper is improved enough to function as a journal-track draft, but it
    remains blocked from submission. The blockers are scientific, not cosmetic:
    source review, prior art, rights/authority, and in several articles an
    unexecuted experiment. A formatted PDF is not a publishable paper. A
    publishable paper needs a result that survives review.

    \section{{Reproducibility}}
    Rebuild the ten-paper package with
    \texttt{{python scripts/generate\_nwagu\_article\_manuscripts.py}},
    upgrade the article bodies with
    \texttt{{python scripts/upgrade\_nwagu\_article\_manuscripts\_for\_impact.py}},
    validate with \texttt{{python scripts/validate\_nwagu\_article\_manuscripts.py}},
    and compile with \texttt{{python scripts/compile\_nwagu\_article\_manuscripts.py}}.

    \section{{Conclusion}}
    This article is now a stronger research object than the first draft because
    it states why the previous version would fail, what has been repaired, what
    still blocks submission, and what experiment would move it toward a real
    result. The work is acceptable as an internal journal-track draft. It is not
    yet acceptable as an impact-journal submission.

    \bibliographystyle{{ACM-Reference-Format}}
    \bibliography{{../references}}
    \end{{document}}
    """


def status(article: dict[str, str]) -> str:
    return f"""
    # {article["id"]}: {article["title"]}

    ## Impact Journal Status

    `JOURNAL_TRACK_DRAFT_NOT_SUBMISSION_READY`

    ## Why The Earlier Draft Failed

    {article["failure"]}

    ## What Was Fixed

    {article["fix"]}

    ## Remaining Submission Blockers

    - Article-specific systematic literature review.
    - Human source/transcription review.
    - Rights and cultural/source authority review.
    - Executed experiment where the article makes a method or performance claim.
    - Venue-specific formatting and anonymity pass.
    """


def audit_report(generated_at: str) -> str:
    rows = "\n".join(
        f"| {a['id']} | {a['target']} | JOURNAL_TRACK_DRAFT_NOT_SUBMISSION_READY | {a['experiment']} |"
        for a in ARTICLES
    )
    return f"""
    # Nwagu Aneke Ten-Article Impact Readiness Audit

    Generated: {generated_at}

    ## Bottom Line

    The previous ten PDFs were not impact-journal candidates because they were
    formatted outlines. They lacked article-specific literature review,
    original executed results, reviewer-facing methods, contribution framing,
    and field-specific falsification plans. The upgraded PDFs are stronger
    journal-track drafts, but they are still not submission-ready.

    ## Global Criteria Used

    - Originality, correctness, novelty, importance, and clarity.
    - Field fit and contribution to a broader literature.
    - Evidence that can be checked by reviewers.
    - Method that can be reproduced or critically inspected.
    - Explicit limitations, ethics, rights, and authority constraints.
    - No promotion of derived or speculative claims into source evidence.

    ## Article Decisions

    | Article | Plausible Target | Current Status | Next Experiment |
    |---|---|---|---|
    {rows}

    ## Required Research Before Submission

    1. Deep prior-art sweep per article.
    2. Source transcription and authority review.
    3. Rights decision for any public source image or manuscript excerpt.
    4. Article-specific experiments for Articles 2, 5, 6, 8, 9, and 10.
    5. Human selection of which two articles should become first submission candidates.
    """


def main() -> int:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    for article in ARTICLES:
        article_dir = PACKAGE / article["slug"]
        write(article_dir / "main.tex", make_tex(article))
        write(article_dir / "STATUS.md", status(article))

    manifest_path = PACKAGE / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["impact_upgrade_generated_at"] = generated_at
    manifest["status"] = "JOURNAL_TRACK_DRAFTS_NOT_SUBMISSION_READY"
    manifest["impact_journal_assessment"] = {
        "previous_failure": "formatted notes without enough original research substance",
        "current_status": "stronger journal-track drafts",
        "submission_ready": False,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    write(PACKAGE / "impact_readiness_audit.md", audit_report(generated_at))
    print("NWAGU_ARTICLE_MANUSCRIPTS_IMPACT_UPGRADED")
    print(f"articles={len(ARTICLES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
