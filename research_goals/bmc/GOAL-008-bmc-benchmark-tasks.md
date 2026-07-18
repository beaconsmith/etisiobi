---
type: research_goal
goal_id: GOAL-008
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: false
paper_potential: medium
risk: low
readiness_status: completed_repo_local
score: 0.595
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-007"]
experiment_directory: experiments/EXP-BMC-008/
---

# GOAL-008: BMC Benchmark Tasks for Symbolic Reconstruction

## Research Question

Can the lab define benchmark tasks that evaluate reconstruction, annotation, count resolution, grammar induction, and claim gating?

## Novelty Hypothesis

The lab may produce benchmark tasks for future symbolic reconstruction systems rather than only one paper.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- row-label reconstruction labels
- vowel inventory labels
- cell-grid completion targets
- base/modifier classes
- contradiction labels
- claim evidence links
- certainty propagation outputs
- grammar induction outputs
- paper-claim validation outputs
- arXiv readiness outputs

## Minimal Experiment

Define tasks, metrics, scoring data requirements, and baseline outputs in the benchmark registry.

## Success Criteria

- Tasks are scoreable from repo-local artifacts.
- Metrics include accuracy, coverage, contradiction precision/recall, evidence-link completeness, certainty calibration, human-review agreement, and reproducibility.
- Benchmarks do not require hidden data for their seed version.

## Failure Criteria

- Tasks cannot be scored from existing artifacts.
- Benchmark labels are missing or circular.
- Metrics reward unsupported generation.

## Falsification Condition

If tasks cannot be scored from existing artifacts, the lab has infrastructure but not yet benchmark-grade data.

## Ultimate Conclusion

A benchmark registry that turns Etisiobi/PAGC research into repeatable evaluation tasks.

## Expected Paper Contribution

We define benchmark tasks for evidence-grounded symbolic reconstruction from heterogeneous scholarly artifacts.

## Experiment Directory

`experiments/EXP-BMC-008/`

## Human Review Needed

- benchmark review
- data release review

## Dependency On Other Goals

- GOAL-007

## Readiness Status

`pending_until_goal_007_graph_model`

## Next Action

Wait for GOAL-007 graph model, then define scoreable benchmark tasks.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `BENCHMARK_SEED_COMPLETED`

Experiment: `experiments/EXP-BMC-008/`

Results: `experiments/EXP-BMC-008/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
