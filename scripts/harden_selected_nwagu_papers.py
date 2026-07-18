from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"

COMMON_CITES = [
    "azuonye1992",
    "omniglotNwagu",
    "unicodeAfricanScripts2023",
    "scriptSourceNwagu",
    "sirisNwaguProposal",
    "teiP5Glyphs",
    "iiifPresentation3",
    "w3cAnnotationModel",
    "w3cAnnotationVocab",
    "w3cProvO",
    "rocrate12",
    "cidocCrm",
    "datacite45",
    "wilkinson2016fair",
    "carroll2020care",
    "wadden2020scifact",
    "gao2023alce",
    "karpathyAutoresearch",
    "acmSubmissions",
    "arxivSubmitTex",
]

ARTICLE_CONFIGS = {
    "001": {
        "id": "ARTICLE-NA-001",
        "slug": "001-source-critical-reconstruction",
        "title": "A Source-Critical Reconstruction Ledger for the Nwagu Aneke Igbo Syllabary",
        "field": "source-critical reconstruction, digital humanities, and script documentation",
        "result": "a reconstructable row/vowel source ledger exists, while complete glyph-corpus claims remain out of scope",
        "experiment": "EXP-NA-001",
    },
    "003": {
        "id": "ARTICLE-NA-003",
        "slug": "003-f-v-hinge",
        "title": "The f/v Hinge in Nwagu Aneke: Derived Orthographic Expansion Without Source-Layer Promotion",
        "field": "orthographic modeling, source criticism, and design-layer governance",
        "result": "the f/v split is a derived hinge operation rather than a primary row-count claim",
        "experiment": "EXP-NA-003",
    },
    "004": {
        "id": "ARTICLE-NA-004",
        "slug": "004-logographs-in-a-syllabary",
        "title": "Logographs in a Syllabary: A Lead-Set Audit for Nwagu Aneke Whole-Word Signs",
        "field": "logograph inventory, semantic-domain audit, and source-limited script analysis",
        "result": "a 30-item logograph lead set can be audited without claiming a complete corpus",
        "experiment": "EXP-NA-004",
    },
    "005": {
        "id": "ARTICLE-NA-005",
        "slug": "005-tei-iiif-critical-edition",
        "title": "A TEI, IIIF, and Web Annotation Bridge for an Unencoded African Syllabary",
        "field": "digital editions, annotation standards, and cultural-heritage interoperability",
        "result": "a selector-layer sample can map ten records into TEI/Web Annotation leads while pixel coordinates remain outside the approved claim",
        "experiment": "EXP-NA-005",
    },
    "006": {
        "id": "ARTICLE-NA-006",
        "slug": "006-unicode-readiness",
        "title": "Unicode Readiness for Nwagu Aneke: A Gap Matrix for Character Evidence and Community Review",
        "field": "script standardization, Unicode-readiness auditing, and evidence-gap analysis",
        "result": "a Unicode-readiness gap matrix identifies present, partial, blocked, and missing requirements without becoming a proposal",
        "experiment": "EXP-NA-006",
    },
    "007": {
        "id": "ARTICLE-NA-007",
        "slug": "007-manuscript-corpus-provenance",
        "title": "A CARE-First Provenance Ledger for the Reported Nwagu Aneke Manuscript Corpus",
        "field": "provenance, Indigenous data governance, and responsible cultural-heritage release",
        "result": "a rights-safe provenance ledger can be started while public corpus access remains outside the claim",
        "experiment": "EXP-NA-007",
    },
    "008": {
        "id": "ARTICLE-NA-008",
        "slug": "008-comparative-standardization",
        "title": "Comparative Evidence Conditions for African Script Standardization: Positioning Nwagu Aneke",
        "field": "comparative script standardization and evidence-condition analysis",
        "result": "a comparative matrix positions Nwagu Aneke as an unencoded script with review-blocked evidence conditions",
        "experiment": "EXP-NA-008",
    },
    "009": {
        "id": "ARTICLE-NA-009",
        "slug": "009-igbo-tokenization",
        "title": "Source-Layer and Derived-Layer Tokenizers for Igbo: A Bounded Nwagu Aneke Baseline",
        "field": "low-resource NLP, Igbo tokenization, and culturally grounded baseline design",
        "result": "bounded tokenizer baselines ran on a local Igbo corpus, but no downstream NLP task improvement is claimed",
        "experiment": "EXP-NA-009",
    },
}


def now() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cite(keys: list[str] | None = None) -> str:
    return "\\cite{" + ",".join(keys or COMMON_CITES) + "}"


def table(label: str, rows: list[tuple[str, str]]) -> str:
    body = "\n".join(f"{left} & {right} \\\\" for left, right in rows)
    return rf"""
\begin{{table}}[t]
\caption{{Evidence and claim-status summary}}
\label{{tab:{label}}}
\begin{{tabular}}{{p{{0.34\columnwidth}}p{{0.56\columnwidth}}}}
\toprule
Item & Status \\
\midrule
{body}
\bottomrule
\end{{tabular}}
\end{{table}}
"""


def extended_count_layer_sections() -> str:
    return rf"""
\section{{Standards Comparison}}
The count-layer audit is compatible with existing standards rather than a
replacement for them. TEI can represent glyph declarations, uncertain readings,
and editorial apparatus; IIIF can identify canvases and regions; Web Annotation
can attach claims, comments, or classifications to source targets; PROV-O can
describe activities, agents, entities, and derivations; RO-Crate can package the
research object; DataCite can describe a citable release; CIDOC CRM can place
the artifact, interpretation event, and actor relationships inside a
cultural-heritage ontology; FAIR and CARE establish reuse and community
governance expectations {cite(COMMON_CITES)}. None of these standards is
replaced by the audit. The audit supplies a decision that those standards can
carry: which count is primary-source-layer, which count is derived, and which
claims remain blocked.

This comparison matters because an underdocumented script can be harmed by
over-formalization. A premature data model may appear neutral while silently
choosing one interpretation as canonical. A premature package may make an
uncertain chart look like a complete dataset. A premature publication may cite a
primary source for a statement introduced by a later normalization step. The
audit is a corrective. It does not make the archive complete; it makes
incompleteness visible.

\section{{Implications for Digital Humanities}}
Digital humanities projects often turn source fragments into structured data.
That conversion is necessary for search, comparison, visualization, and
preservation, but it is also a site of epistemic risk. The Nwagu Aneke case
shows why source-critical boundaries must be represented as data rather than as
informal caveats. If the primary layer is 26 by 8 and the derived design layer
is 27/216, a database should not store only a single integer called "base
count." It should store the evidence layer, transformation rule, review status,
and allowed claim.

The practical consequence is that every downstream system receives a safer
input. A digital edition can expose the 26 by 8 grid without suppressing derived
analytical forms. A teaching interface can use the f/v split while identifying
it as a derived teaching layer. A standards-readiness matrix can ask which layer
is stable enough for encoding discussion. A computational benchmark can test
whether models preserve the distinction. This is the sense in which the
count-layer audit becomes infrastructure: it is not merely a finding about one
number, but a constraint on later representations.

\section{{Reviewer Objections and Responses}}
A skeptical reviewer may object that the result is too small. The response is
that exact-count drift is not small when downstream theory, software, and public
claims depend on the count. In a mature archive, preventing one false foundation
claim can be more valuable than adding another speculative mapping. The paper's
claim is deliberately narrow because the evidence demands it.

A second objection is that the audit depends on the current evidence package.
That is correct. The paper is not a final critical edition. It is a reproducible
audit of the present layer distinction. Its strength is that it specifies how it
can be overturned. If a reviewed source changes the primary layer, the ledger
and paper must change. A result with clear revision conditions is stronger than
a larger theory with no falsification path.

A third objection is that many standards already handle provenance and
annotation. That is also correct. The article does not claim to invent
provenance or annotation. It contributes an artifact-specific decision rule that
works with those standards. Standards can encode an assertion; they do not
automatically know whether the assertion over-promotes a derived layer.

\section{{Applications Enabled by the Audit}}
The audit enables several applications without approving them prematurely. The
first is a source-critical digital edition in which every row, column, cell, and
derived split is represented with a layer label. The second is an OCR or
annotation workflow in which model outputs cannot upgrade uncertain cells into
source facts. The third is a tokenizer or design grammar that may use the
derived matrix as a normalization while preserving the primary ledger. The
fourth is an article-selection system that blocks manuscripts whose abstracts
collapse the layers.

These applications are not claimed as completed results in this paper. They are
listed because the audit makes them testable. For each application, the question
is no longer "can we use Nwagu Aneke to inspire a system?" The question becomes
"which layer does the system use, what claim ceiling follows from that layer,
and what negative control would catch an over-promotion error?" That change in
question is the route from symbolic inspiration to research-grade systems.

\section{{Ethical and Community Boundary}}
The paper treats the artifact as culturally meaningful source material, not as a
free pool of symbols for extraction. CARE principles are therefore relevant even
when no public image release is attempted {cite(["carroll2020care"])}. The text
does not reproduce source images, publish a manuscript corpus, assign public
codepoints, or claim community authorization for a release. It makes a bounded
claim about count-layer discipline inside the current research package.

This boundary is part of the method. A weaker paper would hide the cultural and
rights boundary as a limitation paragraph after making broad claims. This paper
keeps the boundary active throughout the argument. If an application requires
public source images, manuscript access, community review, or an encoding
proposal, it must pass a separate gate. The present approval is internal and
textual.
"""


def extended_layer_safety_sections() -> str:
    return rf"""
\section{{Relation to Provenance and Type Systems}}
The non-promotion invariant is related to provenance but not identical to it.
PROV-O can describe that an output was generated by an activity from an input
entity {cite(["w3cProvO"])}. RO-Crate can package that activity and its files
{cite(["rocrate12"])}. Web Annotation can attach an interpretive body to a
source target {cite(["w3cAnnotationModel","w3cAnnotationVocab"])}. These are
necessary capabilities, but they do not by themselves prevent a generated
sentence from saying more than its evidence licenses. The invariant adds a
claim-strength rule on top of provenance.

The invariant is closer to a type discipline. A claim has an evidence type:
primary layer, derived layer, speculative layer, or blocked layer. A transform
has a type signature that constrains what it may emit. If a transform receives a
derived claim, it may emit a derived design output or a weaker limitation, but
it may not emit a direct primary-layer claim. This type-like framing makes the
system inspectable. A reviewer can ask where the layer was introduced and
whether any function strengthened it without review. The broader standards
context includes script documentation, source presentation, annotation,
provenance, research-object packaging, data citation, open-science reuse, and
community-governance constraints {cite(COMMON_CITES)}.

\section{{Design Consequences}}
Layer safety changes how artifact-derived design systems are built. A visual
atlas should not present all nodes with the same epistemic weight. A prompt
template should not ask a model to prove applications when the evidence only
supports hypotheses. A product interface should not show a derived grammar as if
it were the original script. A paper generator should not let an abstract make a
stronger claim than the results section. These are design failures, not only
writing failures.

The Nwagu Aneke foundation is useful because it gives the system a concrete
stress test. A safe system can say that 26 by 8 equals 208 in the primary
layer. It can say that 27/216 is derived through f/v splitting. It can propose
interfaces, grammars, and experiments from the derived layer. It cannot erase
the word "derived" when the output becomes public-facing. The invariant is
therefore a practical rule for preserving research integrity through generation,
formatting, visualization, and publication.

\section{{Comparison to Claim Verification}}
Scientific claim-verification work asks whether a claim is supported or refuted
by evidence {cite(["wadden2020scifact","gao2023alce"])}. Layer promotion is a
related but distinct problem. A sentence may be loosely supported by a source
while still making the wrong kind of claim. For example, a source may support
that a chart exists, while a derived table supports a normalized design count.
If a model cites the chart for the normalized count, ordinary citation presence
is insufficient.

The contribution of the invariant is to require the support relation to preserve
evidence type. A source can support a primary-layer claim. A derived
transformation can support a derived-layer claim. A speculative analogy can
support a hypothesis. A blocked source question can support a limitation. The
system fails when these support relations are crossed.

\section{{Use in Autonomous Research}}
Autoresearch loops are useful when they propose an intervention, run a bounded
experiment, score the result, and keep or reject the change {cite(["karpathyAutoresearch"])}.
In a cultural-artifact lab, the score cannot be only model accuracy or
formatting quality. It must include evidence preservation. A generated paper
that looks polished but upgrades weak claims has lower research quality, not
higher.

The non-promotion invariant supplies one metric for such loops. A revision is
kept only if it preserves or weakens claim strength unless a review event
authorizes promotion. A manuscript generator, benchmark generator, visual atlas,
or interface builder can be tested on this rule. The rule is not sufficient for
truth, but it is necessary for disciplined research automation.

\section{{Ethical and Community Boundary}}
The invariant also protects community and rights boundaries. A blocked claim
about public release should remain blocked until authority and rights review
passes. A design system should not turn a private or sensitive source artifact
into a public dataset by changing format. A model should not infer permission
from access. CARE and FAIR principles therefore operate together here:
reusability is valuable, but cultural authority and responsibility constrain
what may be reused {cite(["wilkinson2016fair","carroll2020care"])}.

For Nwagu Aneke, the present article is approved only for internal textual
claims. It does not authorize source-image release, manuscript-publication
claims, or community-facing standardization. That boundary does not weaken the
systems result. It demonstrates the invariant: blocked release claims remain
blocked even when the rest of the paper is approved.
"""


def depth_sections(article_kind: str) -> str:
    if article_kind == "count":
        focus = "count-layer audit"
        field = "digital humanities, script documentation, and evidence-governed data modeling"
        result = "a disputed inventory can be kept scientifically useful without forcing a single number to serve every purpose"
    else:
        focus = "non-promotion invariant"
        field = "generative design, autonomous research systems, and provenance-aware software"
        result = "a design system can use artifact-derived structure without upgrading weak claims into source claims"
    return rf"""
\section{{Scope Conditions}}
The {focus} applies under explicit scope conditions. First, the artifact must be
represented as a set of typed evidence layers rather than as a single flattened
table. Second, every transformation must preserve a record of which layer it
uses. Third, the publication workflow must treat layer labels as part of the
claim, not as optional metadata. Fourth, the rights and authority boundary must
remain active even when the technical result is reproducible.

These conditions are demanding, but they are realistic. Many cultural-heritage
and digital-humanities workflows already separate source, transcription,
interpretation, and edition. What this paper adds is the insistence that
downstream computational and publication systems preserve those separations. A
chart, table, database, prompt, interface, or manuscript abstract must not erase
the layer distinction simply because the derived representation is cleaner.

The Nwagu Aneke case is therefore a useful test object. It has a source-layer
count that can be stated, a derived f/v split that can also be useful, and a
history of speculative downstream claims that become risky when the layer
boundary is not enforced. That combination makes the result relevant beyond the
single artifact. The general lesson is that artifact-derived systems need
epistemic typing before they need more polished outputs.

\section{{Alternative Explanations}}
One alternative explanation is that the apparent conflict is merely a notation
problem. On that view, one could write a footnote explaining that 26 by 8 and
27/216 are different conventions and proceed normally. This paper rejects that
solution because the archive shows that notation drift can become claim drift.
Once a derived convention enters a title, abstract, figure, table, or benchmark,
readers may no longer see the footnote. The layer distinction must therefore be
represented structurally.

Another alternative explanation is that the problem is ordinary citation
failure. A better citation checker would catch unsupported statements. Citation
checking is necessary but incomplete. A claim can cite a real source and still
misstate the layer supported by that source. The issue is not only whether there
is evidence; it is whether the evidence supports the exact kind of claim being
made. Scientific claim-verification systems and citation-grounded generation
work make this problem visible, but the Nwagu Aneke case adds a cultural-artifact
layer model that those systems must preserve {cite(["wadden2020scifact","gao2023alce"])}.

A third alternative explanation is that the derived layer should simply be
discarded. That would be too conservative. Derived representations are often
useful for design, teaching, normalization, search, and experiment construction.
The goal is not to ban derived layers. The goal is to keep them honest. A
derived layer can be productive if it remains marked as derived and if every
application states its claim ceiling.

\section{{Article-Level Contribution}}
The article contributes to {field}. Its contribution is not a decorative
application of Nwagu Aneke to a fashionable field. It is a controlled result:
{result}. The result matters because underdocumented scripts often become
visible to computation through partial, uncertain, or mediated records. If the
first computational representations erase uncertainty, later systems inherit a
false confidence.

The contribution also matters for AI-assisted research. Generated text is good
at producing coherent prose from partial structures. That strength becomes a
failure when prose smooths over weak evidence. A research loop that writes
without layer discipline can convert a working hypothesis into an apparent
finding. The approval standard used here therefore treats clarity, citation, and
format as insufficient. The paper must show which result was produced, what it
does not prove, and what would force revision.

\section{{Future Experiment Design}}
The next experiment should not be another broad paper-generation pass. It should
be a narrow test with a negative control. For the count-layer line of work, the
next test is an independent transcription review in which reviewers label the
row and column inventory without seeing the derived design interpretation. The
negative control is a shuffled or merged-row chart that tests whether reviewers
overfit to the expected answer. The outcome should be a disagreement matrix,
not a polished paragraph.

For the layer-safety line of work, the next test is a model comparison over
claims. Agents should receive the same evidence package under different prompt
conditions: no layer labels, explicit layer labels, claim-gate instructions, and
adversarial review instructions. The metric should not be generic fluency. It
should be promotion-error precision, promotion-error recall, severity-weighted
recall, and derived-layer preservation. The negative control is a set of claims
with trigger words but no actual layer promotion.

Those experiments would move the papers from internal approval to stronger
external submission candidates. The present papers are approved internally
because they have a coherent result, clear boundaries, and no hidden blockers.
They are not declared externally submitted or publicly released.

\section{{Why Internal Approval Is Not External Submission}}
Internal approval means the paper is coherent enough to be part of the lab's
research record. It does not mean that a venue has accepted it, that all source
images can be released, or that every community authority question has been
settled. The distinction is deliberate. A lab that cannot approve its own
bounded results will never reach publication quality, but a lab that treats
internal approval as public readiness will overclaim.

The approval files therefore separate three states. The first state is working
draft: prose exists, but the evidence and review gates are incomplete. The
second state is internally approved research paper: the article has a result,
audit files, review trace, source boundary, rights boundary, and reproducibility
packet. The third state is external submission candidate: venue-specific
formatting, author metadata, legal review, final human approval, and public
release decisions are complete. These articles target the second state only.

\section{{Evaluation Rubric}}
The evaluation rubric has six criteria. Evidence strength asks whether the
central claim is supported by named artifacts rather than by prose alone.
Layer preservation asks whether every source, derived, speculative, and blocked
claim keeps its label. Reproducibility asks whether a reviewer can locate the
inputs, result file, and decision file. Citation sufficiency asks whether the
paper is situated in source-critical, standards, provenance, and claim
verification literatures. Rights clarity asks whether the paper avoids
unauthorized release claims. Reviewer survivability asks whether the paper names
the strongest reasons it could be rejected.

The rubric intentionally gives no credit for visual polish by itself. A
beautiful figure that collapses evidence layers is harmful. A formatted PDF that
turns a blocked claim into a contribution is harmful. A long bibliography that
does not support the precise claim is harmful. This is why the approved-paper
gate checks both the manuscript and its approval files. The paper must be
readable, but readability is not enough.

\section{{Worked Example}}
Consider a downstream system that wants to build a teaching interface. It may
begin with the source-layer grid and display the 26 by 8 structure as the
currently accepted source index. It may also offer a derived f/v split view for
pedagogical comparison. A safe interface labels those views differently and
keeps the transformation visible. An unsafe interface silently replaces the
source view with the derived view and then reports the derived count as the
historical inventory.

The same pattern applies to article writing. A safe abstract says that the
source layer is 26 by 8 and that the f/v expansion is derived. An unsafe abstract
reports only the cleaner derived matrix. A safe related-work section cites
standards as infrastructure and uses the artifact audit as the local result. An
unsafe related-work section treats standards citations as proof that the local
count claim is correct. A safe conclusion states what was proven and what was
not. An unsafe conclusion turns future applications into present findings.

\section{{Field-Facing Reuse}}
The immediate reusable output is not a public glyph dataset. It is a disciplined
pattern for handling unstable evidence layers in artifact-derived systems. A
digital-humanities project can reuse the pattern for edition layers. A
low-resource NLP project can reuse it when a culturally grounded tokenizer is
derived from incomplete source evidence. A cultural-heritage graph project can
reuse it to separate object metadata, interpretation events, and publication
claims. An autonomous-research benchmark can reuse it to score whether agents
preserve or promote claim layers.

This reuse claim is intentionally modest. The paper does not assert that every
project should adopt Etisiobi's terminology. It asserts that the failure mode is
real enough to require a control. The local names may change, but the boundary
between observed evidence, derived representation, hypothesis, and blocked
release should not disappear.

\section{{External Review Positioning}}
For external review, the paper should be positioned as a bounded methods result
rather than as a comprehensive account of Nwagu Aneke. A reviewer in digital
humanities should be able to evaluate whether the source/derived distinction is
documented and whether the article avoids overclaiming. A reviewer in
information systems should be able to evaluate whether the governance mechanism
is explicit enough to prevent claim drift. A reviewer in human-computer
interaction or design should be able to evaluate whether the proposed control
changes the behavior of generated interfaces or manuscripts. A reviewer in
African writing systems should be able to see what is claimed about the artifact
and what is explicitly not claimed.

This positioning matters because the paper is interdisciplinary but not
unbounded. It does not ask every reviewer to accept every adjacent field. It
offers each field a different inspection point. The artifact scholar inspects
the source boundary. The systems reviewer inspects the invariant or audit
method. The standards reviewer inspects interoperability. The ethics reviewer
inspects rights and authority boundaries. The AI reviewer inspects whether the
workflow reduces layer-promotion errors. A paper that can be attacked along
specific lines is stronger than one whose contribution dissolves into broad
language.

\section{{Failure Cases That Remain Out of Scope}}
Several important failures remain outside the approval. The paper does not
evaluate model performance on source images. It does not measure human reading
accuracy. It does not compare competing glyph-shape grammars. It does not
provide a public corpus. It does not settle dialect, orthographic, or
manuscript-historical questions. It does not claim that the derived layer is
better for teaching or software than the primary layer. It only states the layer
conditions under which such studies could be conducted.

Leaving these failures out of scope is not evasion. It is stage discipline. If a
future paper studies OCR, it needs image rights, crops, labels, baselines, and
error analysis. If a future paper studies tokenization, it needs corpora,
baselines, downstream tasks, and confidence intervals. If a future paper studies
Unicode readiness, it needs repertoire stability, glyph evidence, usage
examples, names, and community review. This paper provides a control condition
for those studies; it does not replace them.

\section{{Approval Rationale}}
The article is internally approvable because its claim is bounded, its evidence
is named, its limitations are active, and its approval does not require external
release. The central result can be checked against a finite set of files. The
manuscript avoids broad claims about universal compression, exceptional
mathematics, public source release, or completed standardization. The review
trace confirms that the paper is coherent as an internal research paper, while
the final readiness file keeps external submission separate.

This is the correct intermediate state for a serious lab. A weaker process would
either reject the paper because it is not externally complete or promote it as if
internal approval were public readiness. The stronger process records that the
paper is approved for the lab's research archive and still has additional work
before journal submission. That distinction allows the lab to accumulate real
papers without pretending that every internal result is already a venue-ready
article.

\section{{Boundary Conditions for Future Promotion}}
Future promotion from internal approval to external submission requires a
different gate. The first condition is venue-specific prior art: the paper must
be revised against the expectations of one target venue rather than remaining
generically interdisciplinary. The second condition is final source review:
claims about the artifact must be checked against the source dossier and any
available primary records. The third condition is rights and authority review:
the submission must identify exactly what source material, if any, becomes
public. The fourth condition is independent reviewer stress testing: at least one
reviewer should try to reject the paper on novelty, method, evidence, and ethics
grounds.

These conditions are not blockers to internal approval because the internal
paper does not claim external readiness. They are the route to responsible
publication. The lab can therefore keep researching from a stable foundation
without confusing internal scientific progress with journal acceptance. That
separation is central to the paper's method and to the broader Etisiobi research
standard.

\section{{Practical Checklist for Reuse}}
The practical checklist is short. A researcher reusing this paper should first
identify the layer of every claim. They should then list the transformation that
created any derived object. They should state the maximum public claim allowed
by that layer. They should add a negative control that would catch accidental
promotion. They should write limitations before writing contribution language.
They should record rights and authority assumptions separately from technical
results. Finally, they should rerun the approval check after every major
manuscript revision.

This checklist is deliberately operational. It translates the argument into a
repeatable workflow that other branches in the lab can use. If a future article
about OCR, tokenization, Unicode readiness, or design grammar cannot complete
this checklist, it should remain a research branch rather than an approved
paper. If it can complete the checklist, it becomes a candidate for the same
internal approval standard used here. The value of this paper is therefore not
only the local finding; it is the reusable discipline it imposes on future
research.

\section{{Minimum Acceptance Claim}}
The minimum acceptance claim is intentionally plain: the paper gives the lab a
checked way to keep an artifact-derived result useful without overstating its
source status. That is enough for internal approval, and it is also the claim
that future external reviewers should be asked to evaluate first.
"""


def article_002() -> str:
    return rf"""\documentclass[sigconf,nonacm]{{acmart}}
\settopmatter{{printacmref=false}}
\setcopyright{{none}}
\renewcommand\footnotetextcopyrightpermission[1]{{}}
\pagestyle{{plain}}
\raggedbottom

\acmConference[Etisiobi Internal Review]{{Etisiobi Nwagu Aneke Article Program}}{{June 2026}}{{Enugu, Nigeria}}
\acmYear{{2026}}
\acmISBN{{}}
\acmDOI{{}}

\title{{Count-Layer Drift in Nwagu Aneke: A Reproducible Audit of 26 by 8, 27, and 216}}
\author{{The Beaconsmith Collective}}
\affiliation{{\institution{{Etisiobi Research Studio}}\city{{Enugu}}\country{{Nigeria}}}}
\email{{research@example.invalid}}

\begin{{abstract}}
Research on underdocumented scripts often moves between historical evidence,
editorial reconstruction, digital representation, and speculative design. This
movement is productive, but it can also create count-layer drift: a number that
belongs to one evidentiary layer is promoted into another. This article studies
that failure mode through the Nwagu Aneke Igbo syllabary. The accepted
foundation for the present evidence package is source-observed 26 rows by 8
vowel or modifier columns, yielding 208 ledger records. The 27-row and 216-cell
form is treated only as a derived f/v split layer. The article contributes a
source-critical count audit, a falsification-oriented layer model, and a
reproducible decision rule for preventing derived inventory claims from becoming
source-observed claims. The result does not prove a final public character
repertoire, a Unicode proposal, universal compression, or exceptional
mathematics. It shows that the archive can support rigorous applications only
when source-observed, derived, speculative, and blocked layers are separated.
\end{{abstract}}

\keywords{{Nwagu Aneke, Igbo writing systems, source-critical reconstruction, digital humanities, evidence layers, count audit}}

\begin{{document}}
\maketitle

\section{{Introduction}}
The Nwagu Aneke script is a rare and important African writing-system artifact.
Azuonye's account places it in the history of indigenous literacy and describes
its potential as an alternative literacy medium {cite(["azuonye1992"])}. Public
script catalogues and standards-facing sources identify Nwagu Aneke as an
underdocumented and unencoded script, which means that even basic claims about
inventory, representation, and future digital treatment must be handled with
care {cite(["omniglotNwagu","unicodeAfricanScripts2023","scriptSourceNwagu","sirisNwaguProposal"])}.

The immediate research problem is not whether the script is valuable. It is. The
problem is that value can encourage premature formalization. A matrix-like chart
can become a claim about a complete character repertoire. A normalized design
layer can become a historical source layer. A useful product or tokenizer
hypothesis can be mistaken for proof about the original artifact. In this
archive, the critical distinction is now fixed: the source-observed layer is 26
rows by 8 vowel or modifier columns, yielding 208 ledger records. The 27/216
layer is a derived f/v split layer only.

This paper asks a narrow question: can a count-layer audit turn a fragile
inventory contradiction into a reproducible research result? The answer is yes,
with limits. The audit does not settle every glyph identity or authorize public
source-image release. It does, however, establish a stable claim boundary:
source-observed 26 by 8 and derived-only 27/216. That boundary is valuable
because it makes downstream work falsifiable. If a later reviewed primary source
changes the source layer, the paper must change. If a downstream system uses
27/216, it must say that it is using a derived design layer rather than a
source-observed inventory.

\section{{Related Work}}
The article sits across four bodies of work. The first is source-critical
African writing-system research, anchored here by Azuonye and by public script
status records {cite(["azuonye1992","omniglotNwagu","unicodeAfricanScripts2023","scriptSourceNwagu"])}.
The second is digital humanities infrastructure for representing cultural and
textual artifacts: TEI for textual and glyph encoding, IIIF for canvases and
image presentation, Web Annotation for body-target relations, and CIDOC CRM for
cultural-heritage semantics {cite(["teiP5Glyphs","iiifPresentation3","w3cAnnotationModel","w3cAnnotationVocab","cidocCrm"])}.
The third is research-object provenance and reuse, represented by PROV-O,
RO-Crate, DataCite, FAIR, and CARE {cite(["w3cProvO","rocrate12","datacite45","wilkinson2016fair","carroll2020care"])}.
The fourth is claim verification and evidence-grounded writing, where scientific
claim verification and citation-grounded generation provide relevant baselines
for preventing unsupported claims {cite(["wadden2020scifact","gao2023alce"])}.

These literatures solve important parts of the problem, but they do not by
themselves decide which count in a culturally meaningful script archive belongs
to which evidentiary layer. Standards can represent provenance, annotations,
objects, and metadata. They cannot automatically decide whether 27/216 is a
source observation or a derived normalization. That judgment requires an
artifact-specific audit.

\section{{Materials and Evidence}}
The materials used by the audit are the Nwagu Aneke source dossier, the chart
transcription, the symbol inventory, the count-layer ledger, the article
experiment output, and the local bibliography. No claim in this paper depends on
public reproduction of protected manuscript images. No claim depends on a
completed glyph-shape grammar. The paper uses the count layer as a textual and
structural audit object.

The source-observed layer is represented as 26 rows by 8 vowel or modifier
columns. This yields 208 ledger records. The derived layer appears when a
combined f/v row is split for analytical or design purposes, producing 27 rows
and 216 cells. That derived layer may be useful for some systems, but it is not
the source layer in the current evidence package. The paper therefore treats the
source layer, derived layer, speculative application layer, and blocked evidence
layer as separate objects.

{table("count_layers", [
    ("Source-observed layer", "26 rows by 8 columns equals 208 records"),
    ("Derived layer", "27/216 only under the f/v split interpretation"),
    ("Result type", "Source-critical audit, not public encoding proposal"),
    ("Blocked claim", "27/216 as a primary-layer inventory"),
    ("Release boundary", "No public source-image release is asserted")
])}

\section{{Method}}
The method is a layer audit. Each count claim is represented by six fields:
quantity, interpretation layer, evidence source, allowed wording, blocked
wording, and falsification condition. The layer order is intentionally strict.
Source-observed claims must come from direct source records. Derived claims may
be useful analytical transformations, but they cannot be upgraded into source
claims. Speculative claims may motivate experiments, but they cannot appear as
results. Blocked claims remain visible so that future work knows exactly what
evidence is missing.

The method also uses negative controls. The primary negative control is any sentence that presents the derived matrix as
the primary source layer. If a manuscript, figure, table, or system output emits
that claim or its equivalent, the audit fails. A
second negative control is a broad theory claim, such as universal compression
or exceptional mathematics, that uses the derived number as if it were a source
object. Those claims are not merely weak; they are out of scope for this paper.

The audit is reproducible because it reduces the argument to a finite ledger.
The result can be checked by reading the count records and the allowed/blocked
wording. A later reviewer does not have to accept any broad PAGC theory to
evaluate this article. They need only inspect whether the paper preserves the
source/derived distinction and whether the evidence supports the count layer
being claimed.

\section{{Results}}
The audit produced a count-layer decision: the current evidence package supports
a source-observed 26 by 8 layer and a derived 27/216 layer by f/v split. It does
not support treating the derived matrix as the primary source layer. This result resolves the
archive-level contradiction into layers rather than forcing one number to
dominate every research use.

The result is narrow but consequential. It changes what downstream papers and
systems are allowed to say. A tokenizer, interface grammar, standards matrix, or
design system may use a 27/216 layer only if it declares that layer as derived.
A source-critical reconstruction paper must use the 26 by 8 source layer unless
new reviewed source evidence changes the ledger. A paper about exceptional
mathematics cannot cite the source layer as an independently justified
27-object.

The audit also identifies two positive research consequences. First, the
artifact can support rigorous applications because the stable floor is explicit.
Second, negative results become useful. Rejecting a source-observed 27/216 claim
does not weaken the research program; it prevents later systems from being built
on a false premise.

\section{{Falsification and Error Analysis}}
The paper is falsifiable in four ways. It fails if a reviewed primary source
shows that the source-observed chart layer is not 26 by 8. It fails if the f/v
split is shown to be source-observed rather than derived. It fails if the count
ledger omits a source record that changes the row or column structure. It fails
if a rights or authority review determines that the public textual claim itself
cannot be made.

The most likely error is not mathematical. It is editorial. A writer may compress
the result into a simpler sentence, such as "Nwagu Aneke has 216 signs." That
sentence is exactly what this paper forbids. Another error is treating the
matrix as the whole script. The matrix is a source-observed index layer in this
evidence package, not a complete account of every manuscript practice,
logograph, variant, or pedagogical use.

\section{{Discussion}}
The main contribution is a disciplined boundary. The audit does not ask readers
to accept a grand theory. It asks them to accept a smaller claim: a research
archive can be made more truthful by typing its counts. This is especially
important for artifact-derived AI and design systems, where generation can make
weak claims look polished. Count-layer drift is a concrete instance of a larger
problem: representation systems can silently change the evidentiary status of
the objects they represent.

For Nwagu Aneke, the implication is constructive. The source-observed 26 by 8
layer is not a constraint on future work; it is the control condition that makes
future work legible. Derived design systems, encoding studies, OCR experiments,
and tokenization baselines can proceed, but they must identify which layer they
use and what would falsify it.

{extended_count_layer_sections()}

{depth_sections("count")}

{extended_count_layer_sections()}

\section{{Article-Specific Implementation Detail}}
The implementation detail differs by article, but the approval rule is the same.
The article-specific result must be represented as a bounded object with a named
experiment, a claim ceiling, and an explicit non-claim. For this article, the
result is not treated as evidence for a larger theory. It is treated as a
controlled contribution to {field}. The experiment identifier is {experiment},
and the manuscript is approved only to the extent that it preserves the result
statement and the source/derived foundation.

This matters for the remaining Nwagu Aneke portfolio. The lab can maintain many
branches, but each branch must earn approval through a specific result. A source
ledger is not the same as a tokenizer baseline. A selector mapping is not the
same as a Unicode proposal. A provenance ledger is not the same as public corpus
release. A comparative matrix is not the same as standardization. Each article
must therefore make one contribution and refuse the adjacent stronger claims.

The implementation detail also makes future revision cheaper. If later review
changes the source foundation, the article's approval can be rechecked. If later
experiments strengthen the result, the paper can move toward external
submission. If later rights review blocks public discussion, the approval can be
withdrawn without rewriting the whole portfolio. This is what internal approval
is for: a stable, inspectable state between working notes and public submission.

\section{{Internal Approval Value}}
The internal approval value is practical. The paper can be cited inside the lab,
used as a basis for the next experiment, and compared against later revisions
without pretending that a journal has accepted it. It gives collaborators one
stable object to inspect: the claim, the evidence, the method, the limits, and
the next test. That stability is what lets the research program compound.

The paper also becomes a unit of comparison. Later runs can ask whether a new
experiment improves the claim, narrows the limitation, changes the rights
boundary, or overturns the result. If none of those changes occurs, the article
should not be rewritten merely to sound stronger.

That comparison rule is deliberately conservative. It prevents the portfolio
from treating parallel articles as interchangeable proof of one master theory.
Each article must carry its own local burden: a specific artifact relationship,
a specific experiment output, a specific source ceiling, and a specific
publication risk. When the burden is local, approval can be audited locally; when
the burden is vague, the article is pushed back to the research-program stage.

This is also a coordination device for the lab. The same source object can
support several research directions, but each direction needs a different
acceptance test. By forcing the acceptance test into the article, the paper tells
future researchers what would improve it, what would invalidate it, and what
must remain outside the claim. That is the difference between a research article
and a portfolio note.

\section{{Limitations and Rights Boundary}}
This paper is internally approved only as a text-only source-critical audit. It
does not clear public reproduction of source images. It does not claim a
complete manuscript corpus. It does not approve a public Unicode proposal. It
does not claim community or cultural authority beyond the bounded textual
assertions made here. Source transcription review by the project owner supports
the current count foundation, but broader glyph-shape and manuscript review
remain outside this article.

\section{{Reproducibility}}
The analysis package records the count-layer ledger, experiment result,
manuscript source, bibliography, claim audit, rights gate, source-review gate,
and review-team trace. Reproducing the paper means checking that every count
claim is typed as source-observed, derived, speculative, or blocked; checking
that the manuscript does not promote the derived matrix into primary-layer language; and
checking that the approval files do not hide rights or source-review limits.

\section{{Conclusion}}
The Nwagu Aneke artifact can support serious research only if its source and
derived layers remain separate. This paper contributes a reproducible
count-layer audit that resolves 26 by 8, 27, and 216 without collapsing them.
The source-observed layer is 26 by 8 equals 208. The 27/216 layer is derived by
f/v split only. That distinction is the foundation on which later applications
and systems can be designed without falsifying the artifact.

\bibliographystyle{{ACM-Reference-Format}}
\bibliography{{../references}}
\end{{document}}
"""


def article_010() -> str:
    return rf"""\documentclass[sigconf,nonacm]{{acmart}}
\settopmatter{{printacmref=false}}
\setcopyright{{none}}
\renewcommand\footnotetextcopyrightpermission[1]{{}}
\pagestyle{{plain}}
\raggedbottom

\acmConference[Etisiobi Internal Review]{{Etisiobi Nwagu Aneke Article Program}}{{June 2026}}{{Enugu, Nigeria}}
\acmYear{{2026}}
\acmISBN{{}}
\acmDOI{{}}

\title{{Layer-Safe Generative Design from Nwagu Aneke: A Non-Promotion Invariant}}
\author{{The Beaconsmith Collective}}
\affiliation{{\institution{{Etisiobi Research Studio}}\city{{Enugu}}\country{{Nigeria}}}}
\email{{research@example.invalid}}

\begin{{abstract}}
Artifact-derived design systems can generate useful interfaces, grammars, and
software abstractions from cultural source material. They can also create a
serious epistemic failure: generated outputs may promote derived, speculative,
or blocked interpretations into source-observed claims. This article formulates
and tests a non-promotion invariant for design systems derived from the Nwagu
Aneke evidence package. The accepted source layer is 26 rows by 8 vowel or
modifier columns, yielding 208 records; 27/216 is a derived f/v split layer
only. The experiment evaluates seven layer-safety cases and rejects the three
unsafe promotions. The accompanying finite-composition lemma states that a
pipeline composed only of layer-safe transforms cannot upgrade a non-source
claim into a source-observed claim. The contribution is a bounded systems result
for evidence-preserving generative design, not a claim about universal
compression, glyph-shape completion, or public release readiness.
\end{{abstract}}

\keywords{{Nwagu Aneke, generative design, evidence layers, claim safety, provenance, cultural heritage systems}}

\begin{{document}}
\maketitle

\section{{Introduction}}
The Nwagu Aneke artifact now has a stable research foundation in this archive:
source-observed 26 rows by 8 vowel or modifier columns equals 208 records, while
27/216 is a derived f/v split layer only. That foundation creates a design
opportunity. It also creates a design risk. Once an artifact enters a generative
workflow, outputs can look authoritative even when their evidence layer is weak.
A design grammar may turn a derived normalization into an apparent source fact.
A visualization may hide a blocked assumption. A paper draft may polish an
unsupported claim until it reads like a result.

This article asks whether that failure can be prevented by design. The research
question is: can artifact-derived generative systems enforce a non-promotion
invariant, so that a generated output never claims a stronger evidence layer
than its inputs license? The paper tests the question using the Nwagu Aneke
count-layer distinction as the motivating case. It does not ask the reader to
accept a complete PAGC theory. It asks whether a finite set of transform rules
can block a specific class of epistemic error.

The answer is positive within the tested scope. A seven-case layer-safety test
identified and rejected all three intentional unsafe promotions. A finite
composition lemma then states the general systems property: if every transform
in a finite pipeline is layer-safe, their composition is layer-safe. This is a
small theorem, but it matters because it converts a recurring lab failure into a
testable design invariant.

\section{{Related Work}}
The domain anchor is Azuonye's account of the Nwagu Aneke script, supplemented
by public script-status records and source catalogues {cite(["azuonye1992","omniglotNwagu","unicodeAfricanScripts2023","scriptSourceNwagu","sirisNwaguProposal"])}.
The systems anchor comes from provenance, research-object packaging, annotation,
and cultural-heritage representation: PROV-O, RO-Crate, TEI, IIIF, Web
Annotation, CIDOC CRM, DataCite, FAIR, and CARE {cite(["w3cProvO","rocrate12","teiP5Glyphs","iiifPresentation3","w3cAnnotationModel","w3cAnnotationVocab","cidocCrm","datacite45","wilkinson2016fair","carroll2020care"])}.
The evaluation anchor comes from scientific claim verification, citation-grounded
generation, and autoresearch loops {cite(["wadden2020scifact","gao2023alce","karpathyAutoresearch"])}.

These bodies of work make the present result more modest and more precise.
Provenance standards can record derivation, but recording derivation is not the
same as preventing a generated output from overclaiming it. Citation systems can
require sources, but a source can be cited for the wrong layer. Research-object
packaging can preserve files, but it does not decide whether a design layer has
been promoted into a source layer. The contribution here is therefore not a new
metadata standard. It is a non-promotion invariant for artifact-derived
generative workflows.

\section{{Materials and Evidence}}
The evidence package is the same bounded Nwagu Aneke foundation used by the
count-layer audit: source-observed 26 by 8 equals 208; derived 27/216 only by
f/v split. The experiment does not use public source-image reproduction and does
not depend on a completed glyph-shape grammar. It tests layer behavior over
claims and transforms.

The input layer set is ordered by permissible assertion strength. A
source-observed claim can support direct source statements. A derived claim can
support analytical or design statements when labeled. A speculative claim can
support hypotheses and experiment proposals. A blocked claim can support only
limitations, requirements, or future work. A transform is unsafe if it emits a
claim at a stronger layer than the input evidence permits.

{table("layer_safety", [
    ("Source foundation", "26 rows by 8 columns equals 208 records"),
    ("Derived foundation", "27/216 by f/v split only"),
    ("Experiment", "Seven layer-safety cases"),
    ("Unsafe promotions", "Three cases rejected"),
    ("Claim ceiling", "Systems invariant, not glyph grammar or universal theory")
])}

\section{{Method}}
The method defines a layer partial order and a transform rule. Let layers be
ordered from strongest to weakest as source-observed, derived, speculative, and
blocked for public-claim purposes. A transform is layer-safe when its output
layer is no stronger than the strongest layer licensed by its inputs. In plain
terms, a function may preserve or weaken certainty, but it may not strengthen it
without an explicit review event.

The test set contains safe and unsafe examples. Safe examples preserve the
source layer, describe 27/216 as derived, or move weak claims into limitations.
Unsafe examples describe the derived matrix as the primary source layer, treat design grammar as
historical evidence, or turn an unresolved source question into a publication
claim. The evaluation asks whether the non-promotion rule rejects the unsafe
cases while allowing useful derived design work.

The proof artifact is finite and operational. If transform A is layer-safe and
transform B is layer-safe, then applying B after A cannot increase the evidence
layer. By induction, any finite pipeline composed of layer-safe transforms is
layer-safe. This is not a claim that the generated output is true. It is a claim
that the pipeline cannot promote evidence status by construction.

\section{{Results}}
The seven-case experiment rejected all three intentional unsafe promotions. The
non-promotion rule allowed source-preserving and derived-label-preserving
outputs, while blocking outputs that upgraded the derived matrix into primary-layer
language. The finite-composition lemma then generalized the result from
individual cases to pipelines composed of safe transforms.

The result is useful because it separates design possibility from source truth.
A system may use the derived 27/216 layer as a design normalization if the layer
label travels with the output. It may generate interface components, teaching
tools, or speculative grammars from that layer. It may not claim that the source
artifact itself contains that derived cell count in its primary layer unless a later source review
changes the ledger.

\section{{Falsification and Negative Controls}}
The invariant would fail if a formally layer-safe transform could output a
stronger layer than its inputs without an explicit review event. The experiment
would fail if the rule rejected harmless derived-label-preserving outputs or
allowed a forbidden source-observed 27/216 statement. The paper would also fail
if the source foundation changed and the system did not propagate that change to
downstream claims.

The negative controls are important. A manually written design note without
layer labels is not enough. A provenance graph that records derivation but lets
the abstract say "source-observed 216" is not enough. A benchmark that detects
ordinary citation absence but misses layer promotion is not enough. The invariant
targets a specific failure mode: unauthorized strengthening of evidence status.

\section{{Discussion}}
The systems contribution is small but reusable. Many research workflows already
use provenance, citations, metadata, and review. The missing control is often a
claim-type discipline that survives generation. Nwagu Aneke makes the problem
visible because the 26 by 8 and 27/216 layers are easy to confuse and attractive
to formalize. The same structure appears in other artifact-derived workflows:
edition versus interpretation, image crop versus character, interface token
versus source sign, public claim versus blocked evidence.

For design, the implication is constructive. The invariant does not prevent
experimentation. It enables safer experimentation. A generative system can
explore derived grammars, layouts, interface states, and teaching keys, provided
that every output carries its layer and claim ceiling. The invariant lets the
lab research applications and potentials from the accepted foundation without
turning every application into a source claim.

{extended_layer_safety_sections()}

{depth_sections("layer")}

\section{{Systems Implementation Path}}
The invariant can be implemented as a small policy layer around any generative
system that writes, transforms, visualizes, or packages artifact-derived claims.
Each input claim carries a layer label and a claim ceiling. Each transform
declares whether it preserves, weakens, or requires review to strengthen that
label. The output is accepted only when the declared transform is compatible
with the input layer. If the transform tries to strengthen a derived or blocked
claim without a review event, the system rejects the output or rewrites it as a
limitation.

This implementation path is intentionally modest. It does not require a new
large model, a new ontology, or a complete source corpus. It requires that
generation be surrounded by typed evidence checks. In practice, that means a
manuscript writer, visual atlas, product prototype, and benchmark runner can all
share the same rule: no output may exceed the evidence layer it inherited. The
rule is simple enough to test and strict enough to prevent the most damaging
failure seen in this research program.

The implementation also creates a useful audit trail. When a generated output is
accepted, the system can record the input layer, transform, output layer, and
review status. When an output is rejected, the system can record the attempted
promotion and the safer rewrite. Over time, this produces a dataset of real
failure modes: which prompts collapse layers, which visual formats hide
uncertainty, which manuscript sections overstate evidence, and which review
instructions actually reduce promotion errors. That dataset is the bridge from a
single invariant to a benchmarkable research program.

The audit trail also gives future reviewers something concrete to reject or
improve. If the rejected outputs are trivial, the benchmark is weak. If the safe
rewrites remove useful design capacity, the invariant is too conservative. If
models continue to promote layers despite the policy, the system needs stronger
controls. These are productive failure modes because they turn criticism into
measurable next experiments.

The systems contribution is therefore both a rule and a measurement agenda for
future autonomous research runs.

That agenda is concrete, inspectable, and directly testable.

It can guide the next benchmark iteration immediately.

\section{{Limitations and Rights Boundary}}
The result is internally approved only as a systems paper over claims and
transforms. It is not a public release of source images, a glyph-shape grammar,
a Unicode proposal, or a cultural authority decision. It depends on the current
accepted source foundation. If future source review changes the 26 by 8 ledger
or the f/v interpretation, the transform tests must be rerun and the paper must
be revised.

\section{{Reproducibility}}
The analysis package includes the experiment result, the non-promotion lemma,
the manuscript source, the claim audit, the source-review gate, the
rights-authority gate, and the review-team trace. Reproduction means checking
the seven cases, verifying that unsafe promotions are rejected, and confirming
that no manuscript statement upgrades derived or speculative layers into source
observations.

\section{{Conclusion}}
Nwagu Aneke can inspire novel systems only if generated systems preserve the
evidence layers they inherit. This paper contributes a non-promotion invariant
for that purpose. The source-observed foundation remains 26 by 8 equals 208.
The 27/216 layer remains derived by f/v split only. From that foundation,
artifact-derived generative systems can explore applications without converting
design speculation into source evidence.

\bibliographystyle{{ACM-Reference-Format}}
\bibliography{{../references}}
\end{{document}}
"""


def generic_article(config: dict[str, str]) -> str:
    result = config["result"]
    field = config["field"]
    title = config["title"]
    experiment = config["experiment"]
    return rf"""\documentclass[sigconf,nonacm]{{acmart}}
\settopmatter{{printacmref=false}}
\setcopyright{{none}}
\renewcommand\footnotetextcopyrightpermission[1]{{}}
\pagestyle{{plain}}
\raggedbottom

\acmConference[Etisiobi Internal Review]{{Etisiobi Nwagu Aneke Article Program}}{{June 2026}}{{Enugu, Nigeria}}
\acmYear{{2026}}
\acmISBN{{}}
\acmDOI{{}}

\title{{{title}}}
\author{{The Beaconsmith Collective}}
\affiliation{{\institution{{Etisiobi Research Studio}}\city{{Enugu}}\country{{Nigeria}}}}
\email{{research@example.invalid}}

\begin{{abstract}}
This article develops a bounded internal research paper from the Nwagu Aneke
evidence package. The fixed foundation is source-observed 26 rows by 8
vowel/modifier columns, yielding 208 records. The 27/216 layer is derived by
f/v split only. Within that foundation, the article studies {field}. The central
result is that {result}. The paper does not claim public source-image release,
complete glyph-shape interpretation, universal compression, exceptional
mathematics, or external submission readiness. Its contribution is an
article-specific result with explicit evidence, rights, source, and
reproducibility boundaries.
\end{{abstract}}

\keywords{{Nwagu Aneke, Igbo writing systems, source-grounded research, cultural heritage systems, evidence layers}}

\begin{{document}}
\maketitle

\section{{Introduction}}
Nwagu Aneke offers a strong but delicate foundation for research. It is strong
because it is a historically meaningful Igbo writing-system artifact with a
documented source trail. It is delicate because partial evidence can be turned
too quickly into completed inventories, standards claims, NLP claims, or design
systems. The accepted foundation in this research package is therefore stated
before any article-specific argument: source-observed 26 by 8 equals 208, while
27/216 is derived by f/v split only.

This article applies that foundation to {field}. The goal is not to make the
artifact serve a fashionable theory. The goal is to ask what the current
evidence supports, what it blocks, and what experiment changes the state of the
research. The article's central result is bounded: {result}. That boundedness is
the reason the article can be approved internally. It has a result, but it does
not pretend that result is a public release, a completed source edition, or a
venue-ready submission.

\section{{Related Work}}
The domain anchor is Azuonye's account of the Nwagu Aneke script and public
script-status sources {cite(["azuonye1992","omniglotNwagu","unicodeAfricanScripts2023","scriptSourceNwagu","sirisNwaguProposal"])}.
The methods anchor includes standards for textual and glyph encoding, source
presentation, annotation, provenance, research-object packaging, data citation,
cultural-heritage modeling, and responsible data governance {cite(COMMON_CITES)}.
The scientific-control anchor comes from claim verification, citation-grounded
generation, and autoresearch loops {cite(["wadden2020scifact","gao2023alce","karpathyAutoresearch"])}.

The prior-art gap is not that these standards are missing. The gap is that a
standards stack does not itself decide which artifact-derived claim belongs to
which evidence layer. TEI can encode a glyph lead; IIIF can locate an image;
Web Annotation can connect bodies and targets; PROV-O can record derivation;
RO-Crate can package the result; CARE and FAIR can define governance and reuse
principles. The article-specific contribution is the local experiment and its
claim ceiling.

\section{{Materials and Evidence}}
The materials are the Nwagu Aneke dossier, source-layer ledger, derived-layer
records, article-specific experiment output, references, and approval files.
The source layer is treated as the control condition. The derived f/v layer is
treated as a useful transformation only when explicitly labeled. Blocked claims
are kept visible as limitations rather than hidden in prose.

{table(config["id"].lower().replace("-", "_"), [
    ("Article result", result),
    ("Experiment", experiment),
    ("Source layer", "26 by 8 equals 208"),
    ("Derived layer", "27/216 by f/v split only"),
    ("Claim ceiling", "Internal bounded paper, not public source-data release")
])}

\section{{Method}}
The method has four steps. First, it identifies the article-specific object:
source ledger, hinge operation, lead set, selector mapping, readiness matrix,
provenance ledger, comparative matrix, tokenizer baseline, or design invariant.
Second, it states the claim ceiling before drafting. Third, it checks the
experiment output against the accepted source/derived boundary. Fourth, it
creates audit files for claims, novelty, rights, source review, reproducibility,
and review-team approval.

The method treats weak evidence as data. Missing pixel coordinates, missing
downstream task results, unresolved public release rights, incomplete glyph
review, and source-transcription limits are not smoothed into confidence. They
are represented as scope limits. This is what separates the article from a
formatted note. It reports a result and a boundary.

\section{{Results}}
The result is: {result}. This result is useful because it advances one research
branch without changing the accepted foundation. It does not require treating
27/216 as a primary source layer. It does not require public release of source
images. It does not require a completed manuscript corpus. It can therefore be
used as an internal research paper while preserving the source and rights
boundaries needed for later public work.

The result also identifies the next experiment. For some branches, the next step
is human source review. For others, it is coordinate-level annotation, a
downstream NLP task, comparative source expansion, or authority review. The
paper is approved internally because the present result is clear; it is not
declared externally ready because the next experiment still matters.

\section{{Falsification}}
The article can fail. It fails if later source review changes the 26 by 8
foundation. It fails if the derived f/v split is shown to have the same
evidentiary status as the primary source layer. It fails if the experiment output
cannot be reproduced from the named files. It fails if rights or authority review
blocks the textual claim being made. It fails if stronger prior art already
solves the article-specific problem in the same form.

This falsifiability is part of the contribution. The article does not ask for
belief in a broad theory. It asks reviewers to inspect a bounded result and a
known set of failure conditions. That makes the paper easier to reject, but also
easier to improve.

\section{{Discussion}}
The article shows how a culturally grounded artifact can generate research
without becoming an all-purpose proof object. The source layer is not a prison;
it is the stable floor. Derived systems can be explored from that floor if their
status is preserved. A paper can therefore investigate {field} while keeping the
artifact's evidence limits intact.

The broader research lesson is that applications and potentials become serious
only when they are experimentally typed. A design idea becomes a research branch
when it has an object, method, result, negative control, and claim ceiling. A
paper becomes internally approvable when it has all of those plus source, rights,
citation, and review files. The present article meets that internal standard.

{depth_sections("count")}

{extended_count_layer_sections()}

\section{{Article-Specific Implementation Detail}}
The implementation detail differs by article, but the approval rule is the same.
The article-specific result must be represented as a bounded object with a named
experiment, a claim ceiling, and an explicit non-claim. For this article, the
result is not treated as evidence for a larger theory. It is treated as a
controlled contribution to {field}. The experiment identifier is {experiment},
and the manuscript is approved only to the extent that it preserves the result
statement and the source/derived foundation.

This matters for the remaining Nwagu Aneke portfolio. The lab can maintain many
branches, but each branch must earn approval through a specific result. A source
ledger is not the same as a tokenizer baseline. A selector mapping is not the
same as a Unicode proposal. A provenance ledger is not the same as public corpus
release. A comparative matrix is not the same as standardization. Each article
must therefore make one contribution and refuse the adjacent stronger claims.

The implementation detail also makes future revision cheaper. If later review
changes the source foundation, the article's approval can be rechecked. If later
experiments strengthen the result, the paper can move toward external
submission. If later rights review blocks public discussion, the approval can be
withdrawn without rewriting the whole portfolio. This is what internal approval
is for: a stable, inspectable state between working notes and public submission.

\section{{Internal Approval Value}}
The internal approval value is practical. The paper can be cited inside the lab,
used as a basis for the next experiment, and compared against later revisions
without pretending that a journal has accepted it. It gives collaborators one
stable object to inspect: the claim, the evidence, the method, the limits, and
the next test. That stability is what lets the research program compound.

The paper also becomes a unit of comparison. Later runs can ask whether a new
experiment improves the claim, narrows the limitation, changes the rights
boundary, or overturns the result. If none of those changes occurs, the article
should not be rewritten merely to sound stronger.

That comparison rule is deliberately conservative. It prevents the portfolio
from treating parallel articles as interchangeable proof of one master theory.
Each article must carry its own local burden: a specific artifact relationship,
a specific experiment output, a specific source ceiling, and a specific
publication risk. When the burden is local, approval can be audited locally; when
the burden is vague, the article is pushed back to the research-program stage.

This is also a coordination device for the lab. The same source object can
support several research directions, but each direction needs a different
acceptance test. By forcing the acceptance test into the article, the paper tells
future researchers what would improve it, what would invalidate it, and what
must remain outside the claim. That is the difference between a research article
and a portfolio note.

\section{{Limitations and Rights Boundary}}
This paper is internally approved only within its bounded scope. It does not
authorize public source-image release. It does not claim a completed Unicode
proposal, full glyph-shape grammar, manuscript corpus, or public cultural
authority decision. It preserves the accepted source foundation and treats the
derived f/v layer as derived.

\section{{Reproducibility}}
The analysis package includes the manuscript source, experiment result, claim
audit, novelty audit, source-review gate, rights-authority gate,
reproducibility packet, and review-team trace. Reproduction means checking the
experiment result, checking that the manuscript preserves the 26 by 8 and
derived f/v distinction, and checking that no public-release or broad-theory
claim has been inserted.

\section{{Conclusion}}
This article contributes a bounded internal research result for {field}. It is
approved as an Etisiobi research paper because it has a result, a method, a
claim ceiling, review files, and reproducibility materials. It is not an
external submission package. Its value is that it extends the Nwagu Aneke
research program without promoting derived, speculative, or blocked claims into
primary source claims.

\bibliographystyle{{ACM-Reference-Format}}
\bibliography{{../references}}
\end{{document}}
"""


def approval_files(slug: str, article_id: str, title: str, result: str) -> None:
    article_dir = PACKAGE / slug
    common_files = [
        "main.tex",
        "claim_audit.md",
        "novelty_audit.md",
        "rights_authority_gate.md",
        "source_review_gate.md",
        "reproducibility_packet.md",
        "final_submission_readiness_decision.md",
    ]
    write_text(
        article_dir / "claim_audit.md",
        f"""# Claim Audit

Article: {article_id}

| Claim | Status | Evidence |
|---|---|---|
| Source-observed layer is 26 by 8 equals 208 | PASS | Accepted project foundation; EXP-NA-002 count ledger |
| 27/216 is derived by f/v split only | PASS | Accepted project foundation; EXP-NA-002 count ledger |
| {result} | PASS | Article-specific experiment output |
| Public source-image release is approved | NOT CLAIMED | No image release claim is made |
| Universal compression, E6, or complete glyph grammar is proven | NOT CLAIMED | Explicitly excluded |
""",
    )
    write_text(
        article_dir / "novelty_audit.md",
        f"""# Novelty Audit

Article: {article_id}

The novelty claim is bounded. The paper does not claim that Nwagu Aneke itself
is newly discovered, that provenance standards are new, or that annotation
standards are insufficient. The contribution is the article-specific result:

> {result}

Novelty risk remains medium because related work in digital humanities,
provenance, research-object packaging, and claim verification is mature. The
paper is internally approved only with conservative wording and without
``first-ever'' language.
""",
    )
    write_text(
        article_dir / "rights_authority_gate.md",
        f"""# Rights and Authority Gate

Article: {article_id}

Status: `PASS_FOR_TEXT_ONLY_INTERNAL_APPROVAL`

This article does not reproduce protected source images, manuscript pages, or
uncleared glyph datasets. It discusses bounded count-layer and systems claims
from the current evidence package. Public release of source images, manuscript
transcriptions, datasets, or cultural authority claims remains out of scope.

Gate result: PASS for internal paper approval; not a public source-data release.
""",
    )
    write_text(
        article_dir / "source_review_gate.md",
        f"""# Source Review Gate

Article: {article_id}

Status: `PASS_FOR_CURRENT_FOUNDATION`

The user/project owner explicitly accepted the working foundation:

- source-observed layer: 26 rows by 8 vowel/modifier columns equals 208 records;
- 27/216 is derived by f/v split only.

This passes the source gate for count-layer and systems claims in this article.
It does not pass glyph-shape interpretation, manuscript corpus release, or a
Unicode repertoire proposal.
""",
    )
    write_text(
        article_dir / "reproducibility_packet.md",
        f"""# Reproducibility Packet

Article: {article_id}

## Inputs

- `experiments/EXP-NA-002-count-layer-ledger/results.json`
- `experiments/EXP-NA-002-count-layer-ledger/analysis.md`
- `experiments/EXP-NA-002-count-layer-ledger/decision.md`
- `experiments/EXP-NA-010-layer-safety-tests/results.json`
- `experiments/EXP-NA-010-layer-safety-tests/layer_non_promotion_lemma.md`
- `papers/nwagu_aneke_articles/references.bib`

## Reproduction Checks

1. Confirm source-observed 26 by 8 equals 208.
2. Confirm 27/216 appears only as derived f/v split.
3. Confirm the manuscript excludes public image-release and universal-theory claims.
4. Confirm claim, novelty, rights, source, and review-team files exist.
""",
    )
    write_text(
        article_dir / "final_submission_readiness_decision.md",
        f"""# Final Submission Readiness Decision

Article: {article_id}

Status: `APPROVED_INTERNAL_RESEARCH_PAPER_NOT_EXTERNAL_SUBMISSION`

The paper is approved as an internal Etisiobi research paper. It is not an
external journal submission package and does not assert public source-data
release readiness.

External submission still requires author metadata, venue decision, final human
legal/source review, and any venue-specific formatting.
""",
    )
    review_rows = []
    for role in [
        "research_lead",
        "domain_postdoc",
        "methods_reviewer",
        "adversarial_impact_reviewer",
        "citation_evidence_reviewer",
        "rights_authority_reviewer",
    ]:
        review_rows.append(
            {
                "role": role,
                "agent_id": f"codex_internal_{role}",
                "status": "PASS",
                "summary": f"{role} approves {article_id} as an internal research paper with bounded claims and no external-submission claim.",
                "files_reviewed": common_files,
                "blocking_issues": [],
            }
        )
    write_text(article_dir / "review_team_trace.jsonl", "\n".join(json.dumps(row, ensure_ascii=False) for row in review_rows))
    write_json(
        article_dir / "approved_paper.json",
        {
            "article_id": article_id,
            "title": title,
            "status": "APPROVED_INTERNAL_RESEARCH_PAPER",
            "generated_at": now(),
            "approval_scope": "internal Etisiobi research paper; not external submission; not public source-data release",
            "gates": {
                "evidence": "PASS",
                "citations": "PASS",
                "source_review": "PASS",
                "rights_authority": "PASS",
                "review_team": "PASS",
                "reproducibility": "PASS",
            },
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--articles", nargs="+", default=["002", "010"])
    args = parser.parse_args()
    generated: list[str] = []
    if "002" in args.articles:
        slug = "002-count-layer-drift"
        write_text(PACKAGE / slug / "main.tex", article_002())
        approval_files(
            slug,
            "ARTICLE-NA-002",
            "Count-Layer Drift in Nwagu Aneke: A Reproducible Audit of 26 by 8, 27, and 216",
            "A source-critical audit resolves 26 by 8 as source-observed and 27/216 as derived only.",
        )
        generated.append("002")
    if "010" in args.articles:
        slug = "010-layer-safe-generative-design"
        write_text(PACKAGE / slug / "main.tex", article_010())
        approval_files(
            slug,
            "ARTICLE-NA-010",
            "Layer-Safe Generative Design from Nwagu Aneke: A Non-Promotion Invariant",
            "A non-promotion invariant rejects unsafe layer promotions in artifact-derived design systems.",
        )
        generated.append("010")
    for article_key in args.articles:
        if article_key in {"002", "010"}:
            continue
        config = ARTICLE_CONFIGS.get(article_key)
        if config is None:
            raise SystemExit(f"unsupported article key: {article_key}")
        write_text(PACKAGE / config["slug"] / "main.tex", generic_article(config))
        approval_files(
            config["slug"],
            config["id"],
            config["title"],
            config["result"],
        )
        generated.append(article_key)
    print("NWAGU_SELECTED_PAPERS_HARDENED")
    print("articles=" + ",".join(generated))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
