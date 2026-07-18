# Claim Integrity Ledger

This ledger records research-status corrections, benchmark contamination risks,
gate changes, and readiness retractions. It is append-only in spirit: add new
entries instead of erasing old mistakes.

## 2026-07-06 - Ten-Candidate Readiness Downgrade Held

Affected surfaces:

- `research_runs/journal_submission_readiness/candidate_registry.json`
- `research_runs/external_reader_legitimacy/external_reader_legitimacy_report.md`
- `research/BENCHMARK_WALL_FORENSICS.md`

Correction:

The ten Nwagu Aneke candidate packets may be counted as packet-complete
submission-review candidates, but they must not be described as journal-ready,
impact-journal-ready, or ready for external submission while the
external-reader legitimacy gate reports `EXTERNAL_READER_LEGITIMACY_FAIL`.

Reason:

The external-reader gate reports `1 / 10` passing manuscripts after rerun. The
failure mode remains substantive: most manuscripts still read like private lab
packets or process notes, not independent scientific papers.

Allowed status:

```text
TEN_CANDIDATE_GOAL_MET_HUMAN_SIGNOFF_BLOCKED
```

Forbidden status until the gates change:

```text
READY_FOR_SUBMISSION
SUBMISSION_READY
READY_FOR_HUMAN_ARXIV_REVIEW
IMPACT_JOURNAL_READY
```

Next evidence that can change this entry:

One candidate must gain a result-first manuscript, field-specific evidence,
prior-art review, external-reader legitimacy pass, lab-standard pass,
review-team pass, rights/authority review, and human submission sign-off.

## 2026-07-06 - Approved-Papers Goal Downgraded From Stale 10/10 To Live 9/10

Affected surfaces:

- `research_runs/approved_papers_goal/CURRENT.md`
- `research_runs/approved_papers_goal/approval_status.md`
- `research_runs/approved_papers_goal/approval_status.json`
- `scripts/validate_approved_papers_goal.py`
- `scripts/validate_benchmark_integrity.py`

Correction:

The approved-papers control plane had split-brain state: `CURRENT.md` reported
`2 / 10`, while `approval_status.md` and `approval_status.json` reported
`10 / 10`. A live rerun of the validator reports `9 / 10`.

Reason:

`ARTICLE-NA-006` is currently below the approved-paper word-depth threshold. It
may be a useful Unicode-readiness manuscript and may pass some external-reader
prose checks, but it should not count as an approved internal research paper
until it satisfies the approval validator without special pleading.

Allowed status:

```text
APPROVED_PAPERS_GOAL_NOT_MET
approved=9/10
```

Forbidden status until the validator changes:

```text
APPROVED_PAPERS_GOAL_MET
approved=10/10
```

Structural fix:

`scripts/validate_approved_papers_goal.py` now rewrites `CURRENT.md` from the
same report used for `approval_status.md/json`, and
`scripts/validate_benchmark_integrity.py` checks that those surfaces agree.

## 2026-07-06 - arXiv Quality Gate Reclassified Partial

Affected surfaces:

- `scripts/validate_arxiv_quality_gate.py`
- `research_runs/arxiv_quality_reset/arxiv_quality_gate_report.md`
- `research_runs/arxiv_quality_reset/arxiv_quality_gate_report.json`

Correction:

The arXiv-quality gate previously returned `ARXIV_QUALITY_GATE_PASS` when any
article passed. That made `9 / 20` look like a gate pass. It now reports:

```text
ARXIV_QUALITY_GATE_PARTIAL
passed=9/20
```

Reason:

A quality gate should only report `PASS` when every checked article passes. A
partial pass is valuable triage information, but it must block readiness claims.

Structural fix:

`scripts/validate_benchmark_integrity.py` now rejects arXiv-quality reports that
say `PASS` unless `passed_count == checked_count`.

## 2026-07-07 - ARTICLE-NA-006 Hardened, Approved Goal Restored, Public Release Still Blocked

Affected surfaces:

- `papers/nwagu_aneke_articles/006-unicode-readiness/main.tex`
- `research_runs/approved_papers_goal/CURRENT.md`
- `research_runs/approved_papers_goal/approval_status.md`
- `research_runs/approved_papers_goal/approval_status.json`
- `research_runs/arxiv_quality_reset/arxiv_quality_gate_report.md`
- `research_runs/arxiv_quality_reset/arxiv_quality_gate_report.json`

Correction:

`ARTICLE-NA-006` was expanded into a substantive Unicode-readiness paper
candidate. A live approval rerun now reports `APPROVED_PAPERS_GOAL_MET`,
`approved=10/10`. This restores internal approved-paper count only. It does not
make the manuscript set public-journal-ready, arXiv-ready, impact-ready, or
externally submission-ready.

Reason:

The wider gate stack still blocks public readiness. The arXiv-quality gate is
partial at `passed=10/20`, external-reader legitimacy remains
`EXTERNAL_READER_LEGITIMACY_FAIL`, and public-release triage still reports zero
public journal-manuscript candidates.

Allowed status:

```text
APPROVED_PAPERS_GOAL_MET
PUBLIC_RELEASE_TRIAGE_BLOCKED
```

Forbidden status until the gates change:

```text
READY_FOR_SUBMISSION
SUBMISSION_READY
READY_FOR_HUMAN_ARXIV_REVIEW
IMPACT_JOURNAL_READY
```

## 2026-07-07 - Context Contamination Gate Added

Affected surfaces:

- `scripts/validate_context_contamination.py`
- `tests/research/test_context_contamination_gate.py`
- `research_runs/context_contamination/context_contamination_report.md`
- `research_runs/context_contamination/context_contamination_report.json`
- `research_runs/journal_submission_readiness/candidate_registry.json`
- `scripts/validate_benchmark_integrity.py`
- `scripts/validate_lab_standard.py`

Correction:

Manuscripts can pass structure, packet completeness, and even some depth checks
while still carrying hidden evaluation/status-frame residue: lab names, article
IDs, validator/gate language, packet prose, and benchmark-shaped wording. The
new context-contamination report currently records:

```text
CONTEXT_CONTAMINATION_FAIL
passed=1/20
```

Only `ARTICLE-NA-006` currently passes this gate.

Reason:

Global-workspace-style evidence suggests task context can shape model behavior
without appearing as ordinary output content. In this repo the visible symptom
is manuscript prose that still sounds like an internal benchmark or readiness
packet instead of an independent scientific paper.

Allowed status:

```text
PUBLIC_RELEASE_TRIAGE_BLOCKED
public_journal_candidate_count=0
```

Forbidden status until the context gate changes:

```text
JOURNAL_READY
ARXIV_READY
IMPACT_JOURNAL_READY
READY_FOR_SUBMISSION
```

Next evidence that can change this entry:

Rewrite one candidate from field result, method, evidence, limitations, and
prior art; remove private lab/status context from the manuscript; then rerun
context-contamination, external-reader, public-release, benchmark-integrity, and
lab-standard gates.

## 2026-07-07 - ARTICLE-NA-002 Promoted to Public-Facing Preprint Candidate

Affected surfaces:

- `papers/nwagu_aneke_articles/002-count-layer-drift/main.tex`
- `research_runs/context_contamination/context_contamination_report.md`
- `research_runs/context_contamination/context_contamination_report.json`
- `research_runs/external_reader_legitimacy/external_reader_legitimacy_report.md`
- `research_runs/external_reader_legitimacy/external_reader_legitimacy_report.json`
- `research_runs/public_release_triage/independent_public_output_audit.md`
- `research_runs/public_release_triage/independent_public_output_audit.json`
- `research_runs/journal_submission_readiness/candidate_registry.json`

Correction:

`ARTICLE-NA-002` has been rewritten as a field-facing count-layer audit rather
than a lab-status packet. It now passes the context-contamination and
external-reader legitimacy gates. The current public-facing preprint candidate
set is:

```text
ARTICLE-NA-002
ARTICLE-NA-006
ARTICLE-NA-010
```

Current gate state after rerun:

```text
EXTERNAL_READER_LEGITIMACY_FAIL
passed=3/10

CONTEXT_CONTAMINATION_FAIL
passed=3/20

PUBLIC_RELEASE_TRIAGE_BLOCKED
public_journal_candidate_count=0
public_preprint_candidate_count=3
```

Reason:

The manuscript-level improvement is real, but it does not satisfy the full
ten-candidate goal. Seven registry candidates still fail external-reader
legitimacy or remain merge, park, or internal-only outputs. The three cleaner
manuscripts still retain human source, rights, venue, disclosure, licence, and
final-package sign-off blockers.

Allowed status:

```text
PUBLIC_PREPRINT_CANDIDATE
PUBLIC_RELEASE_TRIAGE_BLOCKED
```

Forbidden status until the gates change:

```text
PUBLIC_JOURNAL_MANUSCRIPT_CANDIDATE
READY_FOR_SUBMISSION
SUBMISSION_READY
READY_FOR_HUMAN_ARXIV_REVIEW
IMPACT_JOURNAL_READY
```

Exact next action:

Prepare the smallest human source and rights review packets for
`ARTICLE-NA-002`, `ARTICLE-NA-006`, and `ARTICLE-NA-010`, or harden the next
independent manuscript only if it can become field-facing without duplicating
one of those three papers.

## 2026-07-07 - Unicode Completion Prioritized, Submission Still Blocked

Affected surfaces:

- `research_runs/unicode_completion/CURRENT.md`
- `research_runs/unicode_completion/nwagu_aneke_unicode_completion_dossier.md`
- `research_runs/unicode_completion/related_igbo_scripts_triage.md`
- `research_runs/unicode_completion/unicode_completion_gate.json`
- `scripts/validate_unicode_completion_gate.py`

Correction:

The active priority is now Nwagu Aneke Unicode-completion work. Completion does
not mean submitting the current manuscript or readiness matrix. It means
building the standards-facing evidence needed for a possible future SEWG
submission: reviewed repertoire, character-glyph distinction, representative
glyph evidence, usage/stability/interchange evidence, source and authority
review, character names, properties, behavior, font/licence, CLA/IP decisions,
proposal PDF, and ISO/IEC 10646 summary information.

Current gate state:

```text
UNICODE_COMPLETION_GATE_VALID
may_submit=false
submit_decision=DO_NOT_SUBMIT
```

2026-07-07 clarification:

An independent submitter path is open for Nwagu Aneke. The blocker is not a
universal requirement for community permission before anyone can draft or
submit. The blockers are the evidence and process requirements for a credible
SEWG proposal: stable repertoire, character-glyph distinction, rights-cleared
examples, usage/stability/interchange evidence, properties and behavior, font
or font plan, CLA/IP/author/submitter decisions, proposal PDF, and ISO/IEC
10646 summary information.

Related-script decision:

`Nwagugu` currently has no separate script evidence in the checked sources and
must not be spun into a proposal branch without a source. `Ndebe / Ńdébé` is a
separate modern Igbo script project and requires creator or authorized
representative participation before any representation, bundling, or submission
work.

Allowed status:

```text
UNICODE_COMPLETION_BLOCKED_SOURCE_RIGHTS_AUTHORITY
```

Forbidden status until the Unicode gate changes:

```text
UNICODE_PROPOSAL_READY
READY_FOR_SUBMISSION
SUBMISSION_READY
READY_FOR_HUMAN_ARXIV_REVIEW
IMPACT_JOURNAL_READY
```

Exact next action:

Use the independent-submitter pathway: fill the preliminary proposal skeleton
with reviewed source evidence, then reduce blockers in order: source
transcription review, repertoire stabilization, character-glyph review,
rights-cleared representative examples, user/source relationship record,
character names/properties and behavior draft, font/licence plan, then human
CLA/IP/submission decisions.
