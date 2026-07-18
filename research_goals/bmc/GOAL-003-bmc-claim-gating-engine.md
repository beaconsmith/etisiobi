---
type: research_goal
goal_id: GOAL-003
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: true
paper_potential: high
risk: medium
readiness_status: completed_repo_local
score: 0.719
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-001"]
experiment_directory: experiments/EXP-BMC-003/
---

# GOAL-003: BMC as a Claim-Gating Engine for Paper Generation

## Research Question

Can every manuscript claim be traced back to BMC objects, source evidence, certainty records, and experiment outputs?

## Novelty Hypothesis

A BMC-backed claim gate may be a publishable method for preventing unsupported symbolic, historical, or computational claims from entering a paper.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- paper claims
- claim IDs
- BMC objects
- source artifacts
- IIIF/TEI locators
- certainty scores
- provenance activities
- experiment results
- paper sections

## Minimal Experiment

Map paper claims to BMC objects, evidence locators, certainty scores, experiments, and action statuses.

## Success Criteria

- Major manuscript claims have source and BMC dependencies.
- Unsupported claims are marked NEEDS_SOURCE, NEEDS_EXPERIMENT, OVERCLAIMED, REWRITE_AS_LIMITATION, or REMOVE.
- Contradictions block positive paper contributions.
- Claim-gate output can regenerate a paper audit table.

## Failure Criteria

- Most claims cannot be linked to BMC or evidence objects.
- The gate cannot separate supported claims from speculative claims.
- Paper sections contain positive claims that the gate marks unsafe.

## Falsification Condition

If most claims cannot be linked to BMC/evidence objects, the lab is not ready for BMC-driven paper generation.

## Ultimate Conclusion

A manuscript whose major claims are evidence-gated and reproducible from repo-local artifacts, or a no-submission decision.

## Expected Paper Contribution

We present a claim-gated manuscript pipeline in which exact-count and symbolic-structure claims are accepted only when grounded in BMC-linked evidence.

## Experiment Directory

`experiments/EXP-BMC-003/`

## Human Review Needed

- publication gate review
- claim audit review
- authority review

## Dependency On Other Goals

- GOAL-001

## Readiness Status

`active_after_goal_001_seed`

## Next Action

Build a BMC claim-gate table from paper claims, corpus claims, BMC records, evidence, and experiments.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `CLAIM_GATE_COMPLETED_CORE_BMC_CLAIMS_SCOPED`

Experiment: `experiments/EXP-BMC-003/`

Results: `experiments/EXP-BMC-003/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
