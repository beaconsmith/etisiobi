---
type: research_goal
goal_id: GOAL-007
status: completed
theme: Base Modifier Cache
novelty_status: hypothesis
requires_prior_art_check: true
requires_authority_check: true
requires_count_audit: false
paper_potential: medium
risk: low
readiness_status: completed_repo_local
score: 0.686
created: "2026-05-28"
updated: "2026-05-28"
dependencies: ["GOAL-006"]
experiment_directory: experiments/EXP-BMC-007/
---

# GOAL-007: BMC Knowledge Graph Integration

## Research Question

Can every BMC object be represented as a graph node linked to source evidence, provenance, certainty, claims, and experiments?

## Novelty Hypothesis

The BMC-KG integration may become a reusable architecture for symbolic archive research.

This is not a proven novelty claim. It remains pending systematic prior-art review.

## Required Evidence

- BMC object records
- source artifacts
- IIIF canvases
- TEI locators
- certainty records
- provenance activities
- claims
- experiments
- paper sections
- authority records

## Minimal Experiment

Extend knowledge_graph/etisiobi_kg.jsonld with Base, Modifier, Cell, GlyphObservation, TEILocator, IIIFCanvas, CertaintyRecord, ProvenanceActivity, Claim, Experiment, PaperSection, and AuthorityRecord nodes.

## Success Criteria

- BMC objects can be queried through graph relations.
- Claims and paper sections link to evidence nodes.
- Authority records are part of the graph.

## Failure Criteria

- The KG cannot represent dependencies without ambiguity.
- Important BMC objects remain detached.
- Claims cannot be queried through evidence paths.

## Falsification Condition

If the KG cannot represent claim/evidence dependencies without ambiguity, the model needs ontology repair.

## Ultimate Conclusion

A graph-native research object that can be queried before paper writing.

## Expected Paper Contribution

We show how BMC objects can be embedded in a provenance-aware scholarly knowledge graph.

## Experiment Directory

`experiments/EXP-BMC-007/`

## Human Review Needed

- ontology review
- authority review

## Dependency On Other Goals

- GOAL-006

## Readiness Status

`pending_until_goal_006_certainty_model`

## Next Action

Wait for GOAL-006 certainty model, then extend the KG.

<!-- BEGIN BMC_COMPLETION -->
## Completion Evidence

Status: `completed`

Decision: `KG_INTEGRATION_COMPLETED`

Experiment: `experiments/EXP-BMC-007/`

Results: `experiments/EXP-BMC-007/results.json`

Verified by: `scripts/validate_bmc_goals.py`
<!-- END BMC_COMPLETION -->
