---
type: research_goal
goal_id: GOAL-004
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: true
paper_potential: medium
risk: medium
readiness_status: completed_repo_local
score: 0.608
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-002"]
experiment_directory: experiments/EXP-BMC-004/
---

# GOAL-004: BMC Grammar Induction from Base/Modifier Relations

## Research Question

Can BMC entries reveal a compact grammar that explains the observed symbolic inventory?

## Novelty Hypothesis

If base/modifier combinations are systematic, the BMC may support a generative grammar rather than a flat annotation table.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- verified BMC records
- count reconciliation result
- row class evidence
- modifier class evidence
- exception and ambiguity records

## Minimal Experiment

Infer candidate production rules and test coverage, exception rate, false-generation rate, ambiguity rate, and human-review burden.

## Success Criteria

- A candidate grammar covers verified entries.
- Exceptions and unsupported generations are measurable.
- Ambiguous cells remain flagged.

## Failure Criteria

- The grammar fails to cover many verified entries.
- The grammar generates many unsupported objects.
- The rules depend on unstable counts.

## Falsification Condition

If a grammar fails coverage or generates unsupported entries, BMC remains an index rather than a generative grammar.

## Ultimate Conclusion

A formal grammar, or a negative result showing that the observed inventory resists compact generative modeling.

## Expected Paper Contribution

We test whether the BMC supports grammar induction and report the boundary between observed symbolic structure and speculative generation.

## Experiment Directory

`experiments/EXP-BMC-004/`

## Human Review Needed

- grammar review
- source transcription review

## Dependency On Other Goals

- GOAL-002

## Readiness Status

`blocked_until_goal_002_count_stability`

## Next Action

Wait for GOAL-002 count reconciliation before inducing rules.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `PARTIAL_STRUCTURAL_GRAMMAR_NOT_GLYPH_GRAMMAR`

Experiment: `experiments/EXP-BMC-004/`

Results: `experiments/EXP-BMC-004/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
