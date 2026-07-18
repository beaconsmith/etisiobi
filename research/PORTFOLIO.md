# ICEGOV 2026 Portfolio

> **Venue:** 18th International Conference on Theory and Practice of Electronic Governance (ICEGOV 2026)
> **Deadline:** May 8, 2026 (11 days)
> **Status:** 3-paper focused execution. T5 and T7 killed 2026-04-27. Active papers: T11 (Tier A, main), T1 (Tier A, secondary), T12 (Tier B, ongoing research).

---

## Portfolio Summary

| Slug | Track | Working Title | Tier | Stage | Decision | Disposition |
|------|-------|---------------|------|-------|----------|-------------|
| `community-governance` | 11 — Global South | Beyond State-Centric E-Government: Community Institutions as Engines of Digital Transformation in Southeast Nigeria | **A** | Full Draft | **ACTIVE — Main** | Full draft complete 2026-04-27. Ready for refinement and LaTeX migration. |
| `artifact-first-trust` | 1 — Trust | From Recall to Receipts: Building Trust in Community Governance through Artifact-First Digital Records | **A** | Full Draft | **ACTIVE — Secondary** | Full draft complete 2026-04-27. Ready for refinement and LaTeX migration. |
| `community-os-pilot` | 12 — Experiments | Architecture, Implementation, and Early Evaluation Plan of a Community Coordination OS | **B** | Full Draft | **ACTIVE — Ongoing Research** | Full draft complete 2026-04-27. Ready for refinement and LaTeX migration. |
| `bitcoin-treasury` | 5 — Emerging Tech | Verifiable Community Treasury Operations on Bitcoin Rails: A Design Framework for Transparent Collective Finance | **B** | Killed | **KILLED 2026-04-27** | Source-hungry. No ROSCA empirics found. 11 days insufficient. Park for future cycle. |
| `community-dpi` | 7 — DPI | Community-Led Digital Public Infrastructure for Low-Trust Environments: Payments, Records, and Coordination Beyond the State | **B** | Killed | **KILLED 2026-04-27** | Conceptually too risky. Category confusion risk too high for 11 days. Park for T11 follow-up. |
| `digital-sovereignty` | 2 — Sovereignty | — | **C** | Killed | **KILLED 2026-04-24** | Ideas merged to T1. |
| `platform-governance` | 10 — Policy | — | **C** | Killed | **KILLED 2026-04-24** | Sources fed to T5. |

---

## Tier Definitions

| Tier | Meaning | Resource Allocation |
|------|---------|---------------------|
| **A** | Enough evidence foundation to definitely finish. Priority for source acquisition and drafting resources. | Full effort |
| **B** | Viable only if source thresholds are met in next acquisition loop. Monitor closely. | Conditional effort |
| **C** | Exploratory shells. Kill quickly if source base doesn't improve after one full loop. | Minimal effort; kill-ready |

---

## Cross-Paper Dependencies

- **Shared sources**: Tyler 2006, Beetham 1991, Suchman 1995, Ostrom 1990, Aguerre et al. 2024 appear across multiple papers. Maintain in shared `library/` and cross-reference.
- **Conceptual overlap risk**: `community-governance` (T11) and `community-dpi` (T7) both argue community institutions can host governance functions. Must differentiate: T11 is descriptive/analytical, T7 is prescriptive/design.
- **Methods overlap**: `community-os-pilot` (T12) depends on `bitcoin-treasury` (T5) and `artifact-first-trust` (T1) for the artifact being evaluated. If T5 or T1 are killed, T12 loses its referent.
- **Kill cascade**: `platform-governance` (T10) killed, its best sources (Ferreira 2026, World Bank 2025) fed to T5. `digital-sovereignty` (T2) killed, ideas moved to T1.

---

## Next Portfolio Review

**Trigger:** After next source acquisition loop completes for all papers.
**Decision:** Which papers promote to Tier A, which stay B, which get killed.
**Owner:** Human researcher.

---

## Active Bottlenecks

1. **T11 promote gate** — Methods anchor, contradiction coverage, reviewer defense need strengthening before drafting clears.
2. **T1 Africa/Nigeria sources** — Zero regional recordkeeping sources is the critical gap blocking promotion. ESARBICA journal is the priority search target.
3. **T12 Oroma reframe** — Must be honest design science: describe implemented architecture, key design decisions, evaluation plan. Do NOT frame as pilot results.

## Parked Papers

| Slug | Why Parked | When to Revisit |
|------|-----------|------------------|
| `bitcoin-treasury` | No ROSCA empirics; 11 days insufficient | After T11/T1 accepted; use as basis for next cycle |
| `community-dpi` | Category confusion risk; too thin for 11 days | After T11 accepted; strong conceptual extension of T11 |

## Harness Integrity Notes

- `run_manifest.yaml` is the local canonical stage for each paper.
- `promote_gate.yaml` must contain reasoned pass/fail values, not blanket placeholders.
- Writing files may contain planning scaffolds, but a paper is not in drafting until `promote_gate.yaml` passes and `run_manifest.yaml` advances.
- Raw `research/icegov_2026/` folders are archival ingestion logs; active paper state lives under `research/papers/`.
