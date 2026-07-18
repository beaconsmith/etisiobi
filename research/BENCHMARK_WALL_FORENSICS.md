# Benchmark Wall Forensics

Date: 2026-07-06

## Purpose

This file records where the research harness hits a wall. The point is to stop
the lab from treating every failure as a manuscript polish problem.

## Current Wall: External Reader Legitimacy

Observed state:

- Registry surface: `research_runs/journal_submission_readiness/candidate_registry.json`
- Gate surface: `research_runs/external_reader_legitimacy/external_reader_legitimacy_report.md`
- Current gate status: `EXTERNAL_READER_LEGITIMACY_FAIL`
- Current pass count: `1 / 10`

Diagnosis:

The ten candidate packets have files, review traces, and sign-off blockers. One
candidate currently passes the string-based external-reader check, but the
package still fails as a whole because nine manuscripts retain private lab
framing, package/process prose, and self-describing article language. That is a
manuscript legitimacy failure, not a PDF, compile, or registry-count failure.

## Failure Taxonomy

| Failure class | Symptom | What not to do | Evidence-producing response |
|---|---|---|---|
| Structural completeness mistaken for quality | Candidate registry reaches 10 files/packets | Claim journal readiness | Keep status human-signoff-blocked and require external-reader pass |
| Process prose in manuscript | Text says claim ceiling, review packet, gate checks, reproducibility packet | Replace strings mechanically | Rewrite around field result, method, evidence, limitations, and prior art |
| Private lab framing | Manuscript asks readers to care about Etisiobi, Beaconsmith, article IDs, or internal stages | Add apologetic caveats | Remove internal framing from public manuscript and move process notes to appendices or repo docs |
| Self-describing contribution | Conclusion says the article has a result or extends the research program | Add more abstract praise | State the actual result and what it changes for the field |
| Anti-fitting risk | Rewrite only avoids validator regexes | Celebrate gate pass | Add fresh reader checks and evidence review before promotion |

## Current Decision

Do not mark the ten-candidate registry as journal-ready. The honest status is:

```text
PACKET_COMPLETE + STRUCTURAL_GATE_PASS + EXTERNAL_READER_LEGITIMACY_FAIL
```

That means the package is useful for selecting hardening work, but not for
external submission.

## Additional Wall: Split-Brain Status Surfaces

Observed state:

- `research_runs/approved_papers_goal/CURRENT.md` was stale relative to
  `approval_status.md/json`.
- A live validator rerun now reports `APPROVED_PAPERS_GOAL_NOT_MET`, `9 / 10`.
- `ARTICLE-NA-006` is the current blocker because it is below the internal
  approved-paper word-depth threshold.

Diagnosis:

The lab had multiple status files that could be updated by different loops.
That allowed a celebration surface to persist after the live validator no
longer supported it.

Evidence-producing response:

Make validators regenerate their own current status surfaces and make benchmark
integrity checks compare summary Markdown against machine-readable JSON.

## Additional Wall: Partial Gate Named As Pass

Observed state:

- The arXiv-quality gate reported `ARXIV_QUALITY_GATE_PASS` while only `9 / 20`
  checked articles passed.

Diagnosis:

The gate name described the existence of passing articles, not the status of the
whole checked set. That is useful for triage but unsafe as a readiness gate.

Evidence-producing response:

Use `ARXIV_QUALITY_GATE_PARTIAL` whenever some but not all checked articles
pass, and return a failing exit code until all checked articles pass.

## Additional Wall: Context Contamination and Hidden Evaluation Frame

Observed state:

- Gate surface:
  `research_runs/context_contamination/context_contamination_report.md`
- Current gate status: `CONTEXT_CONTAMINATION_FAIL`
- Current pass count: `3 / 20`
- Current passing manuscripts: `ARTICLE-NA-002`, `ARTICLE-NA-006`, and
  `ARTICLE-NA-010`

Diagnosis:

The Anthropic global-workspace result is a useful warning for this lab: hidden
task context can shape behavior even when the final text looks superficially
on-task. In the Etisiobi manuscripts the visible residue is not mysterious. It
appears as lab/status vocabulary, article IDs, gate language, review-packet
language, and benchmark-shaped wording inside the manuscript itself. That prose
can pass structural checks while still failing as public scientific writing.

Evidence-producing response:

Run `python scripts/validate_context_contamination.py` after every manuscript
hardening step. A manuscript must be rewritten from field result, method,
evidence, limitations, and prior art, not merely scrubbed until regexes stop
matching. Public status must remain blocked while this gate reports failure.

## Current Wall: Human Source and Rights Review Packets

Observed state:

- External-reader legitimacy: `EXTERNAL_READER_LEGITIMACY_FAIL`, `3 / 10`
- Public release triage: `PUBLIC_RELEASE_TRIAGE_BLOCKED`
- Public journal-manuscript candidates: `0`
- Public preprint candidates: `3`
- Current preprint candidates: `ARTICLE-NA-002`, `ARTICLE-NA-006`,
  `ARTICLE-NA-010`

Diagnosis:

The lab now has three manuscripts that read as field-facing papers rather than
private process packets. The wall has moved from prose legitimacy to release
authority. None of the three should be promoted to public journal-manuscript
candidate status until source wording, rights/authority, venue fit, disclosure,
licence, and final package sign-offs are recorded by humans.

Evidence-producing response:

Create small review packets for each of the three cleaner manuscripts. Each
packet should isolate the public claims, source basis, unreleased materials,
rights assumptions, target-venue fit, and exact human decisions still needed.
Do not broaden the paper count by reviving overlapping manuscripts unless the
candidate has an independent result that survives the same context and
external-reader gates.

## Exact Next Evidence-Producing Action

Prepare the smallest human source and rights review packets for
`ARTICLE-NA-002`, `ARTICLE-NA-006`, and `ARTICLE-NA-010`, while keeping all
three below public journal-manuscript status:

1. Extract each paper's public claim, strongest evidence, and explicit
   non-claims.
2. List exact source files or source records a human must inspect.
3. List any public-image, glyph, example, corpus, or authority assumption.
4. Record venue/disclosure/licence decisions that remain human-only.
5. Rerun `python scripts/validate_context_contamination.py`.
6. Rerun `python scripts/validate_external_reader_legitimacy.py`.
7. Rerun `python scripts/audit_independent_public_output.py`.
8. Rerun `python scripts/validate_benchmark_integrity.py`.
9. Rerun `python scripts/validate_lab_standard.py`.

Do not broaden to ten manuscripts by packet count. Broaden only when the next
candidate has an independent result and survives the same gates.
