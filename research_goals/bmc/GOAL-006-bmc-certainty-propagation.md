---
type: research_goal
goal_id: GOAL-006
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: false
paper_potential: high
risk: medium
readiness_status: completed_repo_local
score: 0.692
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-003"]
experiment_directory: experiments/EXP-BMC-006/
---

# GOAL-006: BMC Uncertainty and Certainty Propagation

## Research Question

How should uncertainty propagate from source transcription to BMC objects, grammar rules, count claims, and final manuscript claims?

## Novelty Hypothesis

The lab can define a rigorous certainty calculus for culturally grounded symbolic reconstruction.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- source quality records
- transcription confidence
- annotation confidence
- provenance integrity
- lineage integrity
- contradiction penalties
- review status

## Minimal Experiment

Propagate certainty from source artifact to annotation, BMC unit, count claim, grammar rule, theory claim, and paper claim.

## Success Criteria

- Claim confidence is computed from explicit factors.
- Blocked claims are traceable to weak factors.
- Contradiction penalties are visible.

## Failure Criteria

- Certainty records are too sparse for propagation.
- Confidence scores cannot be justified.
- High-level claims bypass low-confidence evidence.

## Falsification Condition

If certainty records are too sparse or inconsistent to support propagation, the lab must improve certainty instrumentation before high-level theory claims.

## Ultimate Conclusion

A certainty model that identifies which claims are safe, weak, contradicted, or blocked.

## Expected Paper Contribution

We provide a certainty propagation model for evidence-gated symbolic research pipelines.

## Experiment Directory

`experiments/EXP-BMC-006/`

## Human Review Needed

- certainty model review
- publication gate review

## Dependency On Other Goals

- GOAL-003

## Readiness Status

`pending_until_goal_003_claim_gate_seed`

## Next Action

Wait for GOAL-003 claim-gate seed, then propagate certainty factors.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `CERTAINTY_MODEL_COMPLETED_WITH_PUBLICATION_BLOCKERS`

Experiment: `experiments/EXP-BMC-006/`

Results: `experiments/EXP-BMC-006/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
