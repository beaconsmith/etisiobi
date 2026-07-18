---
type: research_goal
goal_id: GOAL-009
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: false
paper_potential: high
risk: medium
readiness_status: completed_repo_local
score: 0.725
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-003", "GOAL-006"]
experiment_directory: experiments/EXP-BMC-009/
---

# GOAL-009: BMC Human-in-the-Loop and Authority-Aware Review

## Research Question

How should expert, cultural, legal, and research authority decisions enter the BMC without erasing uncertainty or overclaiming?

## Novelty Hypothesis

The lab authority register can become an explicit part of symbolic reconstruction, not an afterthought.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- authority approval records
- decision trace records
- certainty records
- BMC records
- paper claims
- release metadata
- review states

## Minimal Experiment

Link review states to authority/approval_register.jsonl, decisions/decision_log.jsonl, certainty records, BMC records, paper claims, and release metadata.

## Success Criteria

- Review states distinguish machine_seeded, human_review_needed, expert_reviewed, authority_approved, disputed, restricted, withdrawn, publication_allowed, and publication_blocked.
- Authority decisions can block release and manuscript claims.
- Uncertainty is preserved across review.

## Failure Criteria

- Authority decisions cannot be connected to release and manuscript claims.
- Review status overwrites uncertainty.
- Publication-facing claims bypass authority state.

## Falsification Condition

If authority decisions cannot be connected to release and manuscript claims, public-facing research claims must be blocked.

## Ultimate Conclusion

A review protocol showing how culturally meaningful symbolic artifacts move from annotation to publication safely.

## Expected Paper Contribution

We integrate authority and consent records directly into a symbolic reconstruction pipeline.

## Experiment Directory

`experiments/EXP-BMC-009/`

## Human Review Needed

- cultural authority review
- legal review
- publication release review

## Dependency On Other Goals

- GOAL-003
- GOAL-006

## Readiness Status

`pending_until_goal_003_and_goal_006`

## Next Action

Wait for GOAL-003 and GOAL-006, then connect review states to claim/release gates.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `AUTHORITY_REVIEW_PROTOCOL_COMPLETED_INTERNAL_ONLY`

Experiment: `experiments/EXP-BMC-009/`

Results: `experiments/EXP-BMC-009/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
