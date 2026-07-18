---
type: research_goal
goal_id: GOAL-002
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: true
paper_potential: high
risk: medium
readiness_status: completed_repo_local
score: 0.786
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-001"]
experiment_directory: experiments/EXP-BMC-002/
---

# GOAL-002: BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims

## Research Question

Does the BMC support a stable 26-row by 8-vowel, 208-cell structure, and how does that interact with 26/27/28 PAGC base or foundation claims?

## Novelty Hypothesis

The BMC may function as a count-audit engine that prevents symbolic theory claims from depending on unstable inventory counts.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- TEI row inventory
- TEI vowel inventory
- glyph annotation row labels
- cell grid records
- knowledge graph nodes
- certainty records
- release manifest
- PAGC foundation/base claims
- paper claims

## Minimal Experiment

Compare TEI rows, TEI vowels, glyph annotations, cell grid records, KG units, certainty records, and PAGC count claims.

## Success Criteria

- Rows, vowels, and cells reconcile at a declared abstraction layer.
- The 26/27/28 distinction is represented as layer-specific rather than flattened.
- Unsupported exact-count claims are downgraded or blocked.
- A count-resolution decision is recorded.

## Failure Criteria

- BMC counts disagree with source inventories without explanation.
- PAGC claims depend on 27 bases without a separate abstraction layer.
- The audit cannot locate count-bearing evidence.

## Falsification Condition

If BMC supports 26 rows and 208 cells while PAGC theory depends on 27 bases without a separately defined abstraction layer, the 27-base claim must be marked unstable or overclaimed.

## Ultimate Conclusion

A count-resolution decision: RESOLVED_26, RESOLVED_27, RESOLVED_28, MULTI_LAYER_COUNT_VALID, UNRESOLVED_SOURCE_CONFLICT, INVALID_TRANSCRIPTION, or INSUFFICIENT_EVIDENCE.

## Expected Paper Contribution

We show that exact-count claims in symbolic research archives require layer-specific inventory reconciliation before theory claims can be trusted.

## Experiment Directory

`experiments/EXP-BMC-002/`

## Human Review Needed

- exact-count review
- source transcription review
- PAGC theory review

## Dependency On Other Goals

- GOAL-001

## Readiness Status

`active_after_goal_001_seed`

## Next Action

Run a count reconciliation report across BMC, TEI, annotations, KG, claims, and paper artifacts.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `MULTI_LAYER_COUNT_VALID`

Experiment: `experiments/EXP-BMC-002/`

Results: `experiments/EXP-BMC-002/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
