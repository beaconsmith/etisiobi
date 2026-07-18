---
type: goal_index
id: BMC_GOALS
status: active
confidence: 0.74
created: "2026-05-28"
updated: "2026-05-28"
tags: [bmc, pagc, nwagu-aneke, claim-gate]
links: [04_Goal_Backlog]
---

# BMC Goals

Base Modifier Cache is treated as a novelty hypothesis pending prior-art review.

## Active

- [[BMC_Goals#GOAL-001 Base Modifier Cache Formal Reconstruction|GOAL-001]]
- [[BMC_Goals#GOAL-002 BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims|GOAL-002]]
- [[BMC_Goals#GOAL-003 BMC as a Claim-Gating Engine for Paper Generation|GOAL-003]]

## All Goals

- [[BMC_Goals#GOAL-001 Base Modifier Cache Formal Reconstruction|GOAL-001: Base Modifier Cache Formal Reconstruction]] - active
- [[BMC_Goals#GOAL-002 BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims|GOAL-002: BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims]] - active
- [[BMC_Goals#GOAL-003 BMC as a Claim-Gating Engine for Paper Generation|GOAL-003: BMC as a Claim-Gating Engine for Paper Generation]] - active
- [[BMC_Goals#GOAL-004 BMC Grammar Induction from Base/Modifier Relations|GOAL-004: BMC Grammar Induction from Base/Modifier Relations]] - blocked
- [[BMC_Goals#GOAL-005 BMC Compression and Minimum Description Length Testing|GOAL-005: BMC Compression and Minimum Description Length Testing]] - blocked
- [[BMC_Goals#GOAL-006 BMC Uncertainty and Certainty Propagation|GOAL-006: BMC Uncertainty and Certainty Propagation]] - pending
- [[BMC_Goals#GOAL-007 BMC Knowledge Graph Integration|GOAL-007: BMC Knowledge Graph Integration]] - pending
- [[BMC_Goals#GOAL-008 BMC Benchmark Tasks for Symbolic Reconstruction|GOAL-008: BMC Benchmark Tasks for Symbolic Reconstruction]] - pending
- [[BMC_Goals#GOAL-009 BMC Human-in-the-Loop and Authority-Aware Review|GOAL-009: BMC Human-in-the-Loop and Authority-Aware Review]] - pending
- [[BMC_Goals#GOAL-010 BMC-to-Paper Recursive Research Hyperloop|GOAL-010: BMC-to-Paper Recursive Research Hyperloop]] - blocked

## Goal Details

## GOAL-001 Base Modifier Cache Formal Reconstruction

Status: `active`

Readiness: `active`

Score: `0.718`

Repo file: [research_goals/bmc/GOAL-001-base-modifier-cache-formal-reconstruction.md](../../research_goals/bmc/GOAL-001-base-modifier-cache-formal-reconstruction.md)

Next action: Create and validate corpus/base_modifier_cache.jsonl from local annotation, TEI, IIIF, certainty, lineage, provenance, and KG artifacts.

## GOAL-002 BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims

Status: `active`

Readiness: `active_after_goal_001_seed`

Score: `0.786`

Repo file: [research_goals/bmc/GOAL-002-bmc-count-reconciliation.md](../../research_goals/bmc/GOAL-002-bmc-count-reconciliation.md)

Next action: Run a count reconciliation report across BMC, TEI, annotations, KG, claims, and paper artifacts.

## GOAL-003 BMC as a Claim-Gating Engine for Paper Generation

Status: `active`

Readiness: `active_after_goal_001_seed`

Score: `0.719`

Repo file: [research_goals/bmc/GOAL-003-bmc-claim-gating-engine.md](../../research_goals/bmc/GOAL-003-bmc-claim-gating-engine.md)

Next action: Build a BMC claim-gate table from paper claims, corpus claims, BMC records, evidence, and experiments.

## GOAL-004 BMC Grammar Induction from Base/Modifier Relations

Status: `blocked`

Readiness: `blocked_until_goal_002_count_stability`

Score: `0.608`

Repo file: [research_goals/bmc/GOAL-004-bmc-grammar-induction.md](../../research_goals/bmc/GOAL-004-bmc-grammar-induction.md)

Next action: Wait for GOAL-002 count reconciliation before inducing rules.

## GOAL-005 BMC Compression and Minimum Description Length Testing

Status: `blocked`

Readiness: `blocked_until_goal_004_grammar_result`

Score: `0.605`

Repo file: [research_goals/bmc/GOAL-005-bmc-compression-mdl.md](../../research_goals/bmc/GOAL-005-bmc-compression-mdl.md)

Next action: Wait for GOAL-004 grammar result before MDL testing.

## GOAL-006 BMC Uncertainty and Certainty Propagation

Status: `pending`

Readiness: `pending_until_goal_003_claim_gate_seed`

Score: `0.692`

Repo file: [research_goals/bmc/GOAL-006-bmc-certainty-propagation.md](../../research_goals/bmc/GOAL-006-bmc-certainty-propagation.md)

Next action: Wait for GOAL-003 claim-gate seed, then propagate certainty factors.

## GOAL-007 BMC Knowledge Graph Integration

Status: `pending`

Readiness: `pending_until_goal_006_certainty_model`

Score: `0.686`

Repo file: [research_goals/bmc/GOAL-007-bmc-knowledge-graph-integration.md](../../research_goals/bmc/GOAL-007-bmc-knowledge-graph-integration.md)

Next action: Wait for GOAL-006 certainty model, then extend the KG.

## GOAL-008 BMC Benchmark Tasks for Symbolic Reconstruction

Status: `pending`

Readiness: `pending_until_goal_007_graph_model`

Score: `0.595`

Repo file: [research_goals/bmc/GOAL-008-bmc-benchmark-tasks.md](../../research_goals/bmc/GOAL-008-bmc-benchmark-tasks.md)

Next action: Wait for GOAL-007 graph model, then define scoreable benchmark tasks.

## GOAL-009 BMC Human-in-the-Loop and Authority-Aware Review

Status: `pending`

Readiness: `pending_until_goal_003_and_goal_006`

Score: `0.725`

Repo file: [research_goals/bmc/GOAL-009-bmc-authority-aware-review.md](../../research_goals/bmc/GOAL-009-bmc-authority-aware-review.md)

Next action: Wait for GOAL-003 and GOAL-006, then connect review states to claim/release gates.

## GOAL-010 BMC-to-Paper Recursive Research Hyperloop

Status: `blocked`

Readiness: `blocked_until_goal_001_through_goal_009`

Score: `0.584`

Repo file: [research_goals/bmc/GOAL-010-bmc-to-paper-hyperloop.md](../../research_goals/bmc/GOAL-010-bmc-to-paper-hyperloop.md)

Next action: Wait for GOAL-001 through GOAL-009 before recursive paper packaging.

## Dependency Map

[BMC goal dependency graph](../../research_goals/bmc/goal_dependency_graph.md)

## Next Experiment

`experiments/EXP-BMC-001/` should generate `corpus/base_modifier_cache.jsonl` from repo-local artifacts.

<!-- BEGIN BMC_COMPLETION -->
## Completion Status

| Goal | Status | Decision |
|---|---|---|
| GOAL-001 | completed | `COMPLETED_AS_WORKING_ANNOTATION_INDEX` |
| GOAL-002 | completed | `MULTI_LAYER_COUNT_VALID` |
| GOAL-003 | completed | `CLAIM_GATE_COMPLETED_CORE_BMC_CLAIMS_SCOPED` |
| GOAL-004 | completed | `PARTIAL_STRUCTURAL_GRAMMAR_NOT_GLYPH_GRAMMAR` |
| GOAL-005 | completed | `COMPRESSION_POSITIVE_FOR_ROW_VOWEL_INDEX_ONLY` |
| GOAL-006 | completed | `CERTAINTY_MODEL_COMPLETED_WITH_PUBLICATION_BLOCKERS` |
| GOAL-007 | completed | `KG_INTEGRATION_COMPLETED` |
| GOAL-008 | completed | `BENCHMARK_SEED_COMPLETED` |
| GOAL-009 | completed | `AUTHORITY_REVIEW_PROTOCOL_COMPLETED_INTERNAL_ONLY` |
| GOAL-010 | completed | `NO_BMC_ARXIV_SUBMISSION_YET` |

Next experiment: independent human review of EXP-BMC-001 and EXP-BMC-002.
<!-- END BMC_COMPLETION -->
