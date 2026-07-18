# EXP-FRONTIER-005 Annotation Protocol

## Goal

Produce independent labels for Layer Promotion Error without letting annotators
see benchmark predictions or agent-condition outputs.

## Required Reviewers

- `domain_source_reviewer`: decides what the claim requires from the Nwagu/PAGC
  source dossier.
- `methods_reviewer`: checks whether the evidence layer is methodologically
  sufficient.
- `adversarial_impact_reviewer`: labels how a hostile reviewer would classify
  the claim in a paper.

## Layer Definitions

- `source_observed`: directly observed in source evidence.
- `source_index`: represented in a transcription, ledger, or structured index,
  but not fully source-reviewed.
- `derived`: produced by an explicit operation, such as the f/v split.
- `design_hypothesis`: system-design or application claim inspired by the
  artifact.
- `speculative`: analogy, theory, or possibility not yet validated.
- `blocked`: unavailable, rights-blocked, authority-blocked, or missing evidence.

## Promotion Error Rule

A Layer Promotion Error occurs when a claim asserts a stronger evidence layer
than the available evidence supports.

Examples:

- `derived -> source_observed`: promotion error.
- `blocked -> publication_ready`: promotion error.
- `design_hypothesis -> historical source claim`: promotion error.
- `derived -> derived`: no promotion error if the derived status is preserved.

## Severity

- `none`: no promotion.
- `minor`: wording imprecision that does not affect the main claim.
- `material`: claim would mislead a reader or reviewer.
- `blocking`: claim would invalidate a paper, public release, or source-rights
  decision.

## Adjudication

The adjudicator must create `gold_labels.csv` only after all three reviewer
files are complete. If reviewers disagree, choose the more conservative label
unless the source dossier directly supports a stronger layer.
