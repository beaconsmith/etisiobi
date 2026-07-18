---
type: goal_backlog
id: "GOALS"
status: "active"
confidence: 0.8
created: "2026-05-28"
updated: "2026-05-28"
tags: [goal_backlog]
links: []
---

# Research Goal Backlog

Generated: 2026-05-28

| Goal | Status | Priority | Parent | Next test |
|---|---|---:|---|---|
| [[GOAL-0001]] PAGC base-inventory resolution | active | 0.862 | POSS-0001 | Audit Azuonye 1992 PDF and chart transcription line-by-line. |
| [[GOAL-0002]] ICEGOV evidence-gate reconciliation | active | 0.785 | POSS-0004 | Diff portfolio, runtime manifests, promote gates, source gaps, and submission rules. |
| [[GOAL-0003]] Scaled compression falsification for k=27 | active | 0.775 | POSS-0002 | Replicate BPE sweep on larger documented Igbo corpus and add MDL baselines. |
| [[GOAL-0004]] Research Spine computability dry run | proposed | 0.727 | POSS-0005 | Run extractor against synthetic read-only fixtures, not production data. |
| [[GOAL-0005]] Repo-level citation and claim auditor | proposed | 0.713 | POSS-0006 | Parse claim maps and source registries for missing links and citation metadata. |
| [[GOAL-0006]] Non-circular bounded-memory experiment | proposed | 0.705 | POSS-0003 | Design fixtures with non-aligned invariant structure and random-hash controls. |

<!-- BEGIN BMC_RESEARCH_PROGRAM -->
## Base Modifier Cache Research Program

    Novelty status: hypothesis pending prior-art review.

    | Goal | Status | Score | Dependency Gate | Next test |
    |---|---|---:|---|---|
    | [[BMC_Goals#GOAL-001 Base Modifier Cache Formal Reconstruction|GOAL-001]] Base Modifier Cache Formal Reconstruction | active | 0.718 | none | Create and validate corpus/base_modifier_cache.jsonl from local annotation, TEI, IIIF, certainty, lineage, provenance, and KG artifacts. |
| [[BMC_Goals#GOAL-002 BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims|GOAL-002]] BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims | active | 0.786 | GOAL-001 | Run a count reconciliation report across BMC, TEI, annotations, KG, claims, and paper artifacts. |
| [[BMC_Goals#GOAL-003 BMC as a Claim-Gating Engine for Paper Generation|GOAL-003]] BMC as a Claim-Gating Engine for Paper Generation | active | 0.719 | GOAL-001 | Build a BMC claim-gate table from paper claims, corpus claims, BMC records, evidence, and experiments. |
| [[BMC_Goals#GOAL-004 BMC Grammar Induction from Base/Modifier Relations|GOAL-004]] BMC Grammar Induction from Base/Modifier Relations | blocked | 0.608 | GOAL-002 | Wait for GOAL-002 count reconciliation before inducing rules. |
| [[BMC_Goals#GOAL-005 BMC Compression and Minimum Description Length Testing|GOAL-005]] BMC Compression and Minimum Description Length Testing | blocked | 0.605 | GOAL-004 | Wait for GOAL-004 grammar result before MDL testing. |
| [[BMC_Goals#GOAL-006 BMC Uncertainty and Certainty Propagation|GOAL-006]] BMC Uncertainty and Certainty Propagation | pending | 0.692 | GOAL-003 | Wait for GOAL-003 claim-gate seed, then propagate certainty factors. |
| [[BMC_Goals#GOAL-007 BMC Knowledge Graph Integration|GOAL-007]] BMC Knowledge Graph Integration | pending | 0.686 | GOAL-006 | Wait for GOAL-006 certainty model, then extend the KG. |
| [[BMC_Goals#GOAL-008 BMC Benchmark Tasks for Symbolic Reconstruction|GOAL-008]] BMC Benchmark Tasks for Symbolic Reconstruction | pending | 0.595 | GOAL-007 | Wait for GOAL-007 graph model, then define scoreable benchmark tasks. |
| [[BMC_Goals#GOAL-009 BMC Human-in-the-Loop and Authority-Aware Review|GOAL-009]] BMC Human-in-the-Loop and Authority-Aware Review | pending | 0.725 | GOAL-003 + GOAL-006 | Wait for GOAL-003 and GOAL-006, then connect review states to claim/release gates. |
| [[BMC_Goals#GOAL-010 BMC-to-Paper Recursive Research Hyperloop|GOAL-010]] BMC-to-Paper Recursive Research Hyperloop | blocked | 0.584 | GOAL-001 + GOAL-002 + GOAL-003 + GOAL-004 + GOAL-005 + GOAL-006 + GOAL-007 + GOAL-008 + GOAL-009 | Wait for GOAL-001 through GOAL-009 before recursive paper packaging. |
<!-- END BMC_RESEARCH_PROGRAM -->

<!-- BEGIN BMC_COMPLETION -->
## BMC Completion

All ten BMC goals are completed as repo-local studies. The BMC paper/hyperloop outcome is a no-submission decision until prior-art, transcription, rights, and authority review gates pass.
<!-- END BMC_COMPLETION -->
