---
type: lpe_label_quality_gate
experiment_id: EXP-FRONTIER-017
status: LPE_LABEL_QUALITY_GATE_PILOT_INTERNAL_NOT_FRONTIER_RESULT
claim_ceiling: quality_gate_pilot_not_paper_result
---

# LPE Label Quality Gate

This branch-specific experiment promotes `NWR-049` from a bounded artifact into
an internal quality-gate pilot for Layer Promotion Error labels.

The pilot asks whether an LPE label can be routed by four checks before it is
used as evidence in agent evaluation: evidence anchor, layer contrast,
disagreement state, and adjudication need. It uses local EXP-FRONTIER-005 label
and score artifacts only. It does not run models, install dependencies, submit
externally, or create a public benchmark result.

Claim ceiling: `quality_gate_pilot_not_paper_result`.

## Full-Gate Extension

The full local label table has now been routed without changing the pilot
claim ceiling.

- Full table: `full_quality_gate.csv`
- Results: `full_quality_gate_results.json`
- Score comparison: `score_gate_alignment.json`
- Human/domain packet: `human_domain_review_packet.csv`
- Routed cases: `360`
- Review-ready internal rows: `290`
- Needs adjudication rows: `28`
- Public-release-blocked rows: `42`

Full-gate claim ceiling: `full_quality_gate_internal_not_paper_result`.

## Pilot Inputs

- Source bounded artifact: `NWR-049`.
- Source label table: 360 local EXP-FRONTIER-005 gold-label rows.
- Pilot sample: 24 rows.
- Prior score context: EXP-FRONTIER-005 score file remains not validated for a
  frontier claim.

## What This Teaches Oroma

Oroma should not treat a label as governance-ready just because it exists.
Labels need provenance, layer contrast, disagreement handling, and an explicit
adjudication route before they guide decisions.

## Next Action

Route the 70 adjudication or public-release-blocked rows into independent
human/domain review before any paper-candidate or journal-submission decision.
