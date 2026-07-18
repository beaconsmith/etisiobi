# Research Lab Dashboard

> SOTA harness control surface for the etisiobi research folder.
> Last updated: 2026-04-24.

## Canonical State Sources

| Layer | Canonical file(s) | Purpose |
|---|---|---|
| Portfolio | `research/PORTFOLIO.md` | Paper ranking, kill/continue decisions, bottlenecks |
| Lab quality | `research/QUALITY_BAR.md`, `research/EVIDENCE_POLICY.md`, `research/CITATION_POLICY.md` | Promotion and evidence standards |
| Paper state | `research/papers/<slug>/runtime/run_manifest.yaml` | Current stage, owner, checkpoint |
| Promotion | `research/papers/<slug>/runtime/promote_gate.yaml` | Gate status with blocking reasons |
| Evidence | `research/papers/<slug>/evidence/*.md` | Claims, contradictions, sources, regional grounding, reviewer risks |
| Submission | `research/SUBMISSION_RULES.md` | Venue, format, blinding, page limits |

## Current Portfolio Health

| Paper | Status | Lab decision |
|---|---|---|
| `community-governance` | Promotion candidate, evidence normalization | Highest priority; populate methods/policy/critical SE Nigeria gaps before drafting |
| `artifact-first-trust` | Evidence population | Continue, but local grounding and critique sources block promotion |
| `bitcoin-treasury` | Conditional evidence population | Continue only if ROSCA/cooperative finance sources are found |
| `community-dpi` | Concept-risk evidence population | Continue cautiously; avoid claiming DPI equivalence |
| `community-os-pilot` | Conditional on artifact evidence | Pause major drafting until platform evidence is audited |
| `digital-sovereignty` | Killed | Preserve reusable records-resilience ideas for T1 |
| `platform-governance` | Killed | Preserve platform/operator sources for T5 |

## SOTA Harness Requirements

- Every active paper must have a non-empty `source_gaps.md`, `claim_map.md`, `contradiction_map.md`, `regional_context.md`, and `reviewer_attack_surface.md`.
- Every promotion decision must be reasoned in `promote_gate.yaml`.
- Every source registry should be mirrored into `runtime/source_index.csv` for machine checks.
- Every paper should maintain `runtime/metrics.json` with counts and blockers.
- Drafting starts only after gates pass. Planning files are allowed; manuscript prose must not outrun evidence.
- Killed papers stay in the tree but their manifests must say `stage: killed`.

## Next Lab Moves

1. Finish evidence maps for `community-governance` and rerun its promotion gate.
2. Run a targeted regional/source sweep for `artifact-first-trust`.
3. Decide whether `bitcoin-treasury` and `community-dpi` are ongoing-research papers or short papers.
4. Audit actual platform evidence before investing in `community-os-pilot`.
5. Compile PAGC `WIKI.md` and create a falsification tracker.
