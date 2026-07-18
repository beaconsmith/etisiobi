---
type: scoring_guide
program: nwagu_aneke_frontier
status: guide_ready_no_human_results
created: "2026-06-22"
goal: GOAL-FRONTIER-001
claim_ceiling: human_comprehension_signal_not_source_evidence
---

# Count-Layer Response Scoring Guide

## Score Values

Use only these values in the `correct` column:

- `correct`
- `partial`
- `incorrect`

`partial` does not count toward the 80% threshold. It is useful for diagnosis,
not for passing the run.

## Correct

Mark `correct` when the answer names the expected layer and avoids claim
promotion.

Examples:

- `26/208` is source-observed Appendix I chart display, not complete inventory.
- `27/216` is derived from f/v splitting and not source-observed.
- Appendix II is unrecovered in this package, not disproved.
- Computational evaluation tests agent behavior, not Nwagu source facts.

## Partial

Mark `partial` when the answer notices uncertainty or a blocker but misses the
specific layer.

Examples:

- Says `27/216` is "uncertain" but does not say derived.
- Says Appendix II is "missing" but also says another archive route may resolve
  it.
- Says PAGC is "unproven" but does not name speculative/exploratory status.

## Incorrect

Mark `incorrect` when the answer promotes, collapses, or reverses a layer.

Examples:

- Treats `27/216` as source-observed.
- Treats Appendix II unrecovered status as proof Appendix II does not exist.
- Treats PAGC as a source fact.
- Treats computational evaluation as source evidence.
- Treats applied design output as historical meaning.

## Confusion Types

Use the `confusion_type` column only when the answer is `partial` or
`incorrect`.

Allowed values:

- `source_derived_collapse`
- `absence_claim_error`
- `speculation_promoted`
- `application_promoted`
- `computation_promoted`
- `count_type_collapse`
- `dropped_branch_revived`
- `other`

## Scorer Rules

The scorer requires:

- 3-5 readers;
- every reader answers every question;
- no duplicate question responses per reader;
- at least 80% overall correct;
- at least 80% correct on the direct `27/216` derived-status question.

Any hard-stop confusion requires label revision before rerunning the protocol.
