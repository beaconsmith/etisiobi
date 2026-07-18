# NWR-089 Portfolio Acceleration Dashboard Spec

Seed: `NWR-089`

Source question: What dashboard would show next proofs without rewarding easy outputs

Evidence layer: infrastructure

Claim ceiling: artifact_not_paper_candidate

## Bounded Artifact

This dashboard spec favors proof movement over output volume.

| Widget | Shows | Anti-gaming rule |
|---|---|---|
| Seed queue | 100 seed-only records by lane | Count does not imply maturity |
| Artifact progress | Selected seeds with bounded artifacts | Artifact needs claim ceiling |
| Blocker map | Source, rights, authority, review, and release blockers | Blockers cannot be hidden |
| Next proof | One concrete action per branch | Action must have failure condition |
| Overclaim watch | Risk phrases and forbidden promotions | Clear scan does not equal readiness |

## Evidence Layer

The artifact is infrastructure. It defines a dashboard, not a maturity score.

## Falsification Gate

The spec fails if it rewards easy output count more than evidence movement.

## Rights And Authority Guardrail

Dashboard visibility must not expose private review data or restricted source
material.

## What This Teaches Oroma

Operational dashboards should reward resolved uncertainty, not decorative
activity.

## Next Action

Implement a local dashboard only after metric review.
