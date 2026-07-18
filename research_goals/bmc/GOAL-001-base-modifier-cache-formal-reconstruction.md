---
type: research_goal
goal_id: GOAL-001
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: true
paper_potential: high
risk: medium
readiness_status: completed_repo_local
score: 0.718
created: "2026-05-28"
updated: "2026-05-28"
dependencies: []
experiment_directory: experiments/EXP-BMC-001/
---

# GOAL-001: Base Modifier Cache Formal Reconstruction

## Research Question

Can the lab reconstruct every observed symbolic unit as a base-plus-modifier object with explicit provenance, certainty, source location, and claim dependency?

## Novelty Hypothesis

The Base Modifier Cache may be a novel evidence-gated symbolic substrate that links annotation, TEI, IIIF, certainty, provenance, knowledge graph, and publication claims.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- glyph annotation records
- cell-grid records
- TEI row and vowel inventory
- IIIF canvas and source locators
- certainty records
- provenance graph
- lineage records
- knowledge graph records
- authority approval records

## Minimal Experiment

Generate corpus/base_modifier_cache.jsonl and verify that every BMC object links to source, certainty, provenance, lineage, and claim dependencies.

## Success Criteria

- Every verified BMC object has a source locator.
- Every verified BMC object has a certainty score.
- Every exact-count claim can be traced to BMC records.
- Ambiguous records are preserved rather than forced.
- Contradictions are surfaced.

## Failure Criteria

- BMC objects cannot be grounded in source evidence.
- Exact counts disagree without an abstraction-layer explanation.
- Certainty records are missing or unusable.
- Authority constraints block publication use.

## Falsification Condition

If source artifacts cannot support stable base/modifier decomposition, BMC must be downgraded from formal substrate to working annotation index.

## Ultimate Conclusion

A reproducible BMC dataset, claim gate, and paper-ready method section, or a clear negative result showing why BMC cannot yet support theory claims.

## Expected Paper Contribution

We introduce a provenance-backed Base Modifier Cache that converts source-localized glyph annotations into auditable symbolic units.

## Experiment Directory

`experiments/EXP-BMC-001/`

## Human Review Needed

- authority/cultural review
- exact-count review
- source transcription review

## Dependency On Other Goals

- none

## Readiness Status

`active`

## Next Action

Create and validate corpus/base_modifier_cache.jsonl from local annotation, TEI, IIIF, certainty, lineage, provenance, and KG artifacts.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `COMPLETED_AS_WORKING_ANNOTATION_INDEX`

Experiment: `experiments/EXP-BMC-001/`

Results: `experiments/EXP-BMC-001/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
