---
type: research_goal
goal_id: GOAL-005
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: true
paper_potential: medium
risk: medium
readiness_status: completed_repo_local
score: 0.605
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-004"]
experiment_directory: experiments/EXP-BMC-005/
---

# GOAL-005: BMC Compression and Minimum Description Length Testing

## Research Question

Does the BMC produce a measurable compression advantage over a flat enumeration of glyph or cell records?

## Novelty Hypothesis

If the symbolic system has real generative structure, base/modifier representation should compress the inventory while preserving reconstructability.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- flat cell list
- row-vowel table
- BMC records
- candidate grammar
- knowledge graph representation
- uncertainty records

## Minimal Experiment

Compare description length, primitives, rules, reconstruction accuracy, exception count, uncertainty-weighted compression, and interpretability across representations.

## Success Criteria

- BMC or grammar representation compresses while preserving reconstruction.
- Exceptions and uncertainty costs are included.
- Flat-table baselines are explicit.

## Failure Criteria

- BMC does not compress better than a flat table.
- Compression requires dropping uncertainty or exceptions.
- The comparison depends on an unstable grammar.

## Falsification Condition

If BMC does not compress better than a flat table, compression-based PAGC claims are unsupported.

## Ultimate Conclusion

A formal result showing either real symbolic compression or a negative result against compression/theory claims.

## Expected Paper Contribution

We introduce uncertainty-aware compression as a falsification test for symbolic-structure claims.

## Experiment Directory

`experiments/EXP-BMC-005/`

## Human Review Needed

- method review
- PAGC theory review

## Dependency On Other Goals

- GOAL-004

## Readiness Status

`blocked_until_goal_004_grammar_result`

## Next Action

Wait for GOAL-004 grammar result before MDL testing.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `COMPRESSION_POSITIVE_FOR_ROW_VOWEL_INDEX_ONLY`

Experiment: `experiments/EXP-BMC-005/`

Results: `experiments/EXP-BMC-005/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
