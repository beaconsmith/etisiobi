# Etisiobi Wiki — Cross-Program Atlas

> **Start here.** This is the single navigation root for the whole repo.
> It is a thin *atlas*: it links to the memory that already exists, and it is the
> home for **cross-program** memory (entities and shared topics) that does not
> belong to any single research program.
>
> It does **not** replace the per-program wikis (`research/*/WIKI.md`) or the
> Obsidian vault (`obsidian_vault/`). It points to them.
> See `ETISIOBI_REPO_ALIGNMENT_AUDIT.md` for why this layer exists.

---

## Memory model (LLM Wiki pattern)

`raw sources (immutable) → wiki (maintained) → schema (rules)`

| Memory type | Where it lives |
|---|---|
| Navigation | **this file**, plus `obsidian_vault/00_Home.md`, `repo_map.md` |
| Semantic (wiki) | `research/icegov/WIKI.md`, `research/pagc/WIKI.md`, `wiki/topics/*` |
| Entity | `wiki/entities/*` |
| Episodic (log) | `log.md`, `reflection_log.md`, `research_loop_changelog.md` |
| Summary (sources) | `external_sources/source_notes/EXT-*`, `library/`, program `sources/` |
| Procedural (schema) | `AGENTS.md`, `research/AGENTS.md`, `skills/*`, `EVIDENCE_POLICY.md` |
| Claim | `obsidian_vault/Claims/*`, `CLAIM_MATURITY_MODEL.md`, `uncertainty/*` |
| Product decision | `ETISIOBI_OROMA_FEED.md`, `research/icegov/PRODUCT_BRIDGE.md`, `decisions/` |
| Learning | `self_improvement_proposals/`, `research_loop_changelog.md` |

---

## Start here

- **What this studio is:** `README.md`
- **How agents must work / rules:** `AGENTS.md`, `research/AGENTS.md`
- **Active programs:** ICEGOV/OGI (`research/icegov/`), PAGC (`research/pagc/`)
- **Nwagu frontier status:** `research/frontier/nwagu_aneke/FRONTIER_LAB_STATUS.md`
- **Latest activity:** `log.md` (tail)

## Entities (cross-program)

- [Oroma](entities/oroma.md) — the product Etisiobi studies
- [Etisiobi](entities/etisiobi.md) — this research studio
- _(stubs to add as needed: citrea, miden, flow-research, ic3, lema-lab)_
- Rules for entity pages: [entities/README.md](entities/README.md)

## Topics (cross-program)

- [AI Agent Memory](topics/ai-agent-memory.md) — the LLM Wiki pattern, applied here
- [Human-Agent Work Protocols](topics/human-agent-work-protocols.md) — Flow-style lessons
- [Derived Hypothesis Charter](../research/pagc/DERIVED_HYPOTHESIS_CHARTER.md) — separates strict source claims from testable formal hypotheses
- [DH-001 Derived Completion](../research/pagc/hypotheses/DH-001-derived-27x8-completion.md) — parked by global benchmark gate; source-safe but label-dependent
- [DH-003 Layer-Promotion Error Benchmark](../research/pagc/hypotheses/DH-003-layer-promotion-error-benchmark.md) — significant internal knowledge breakthrough; ten bounded benchmark-design knowledge units

## Program wikis (canonical, do not duplicate here)

- ICEGOV / OGI: `research/icegov/WIKI.md` · `research/icegov/INDEX.md`
- PAGC: `research/pagc/WIKI.md` · `research/pagc/INDEX.md`

## Oroma bridges (both directions)

- Outbound (research → product): `ETISIOBI_OROMA_FEED.md`, `research/icegov/PRODUCT_BRIDGE.md`
- Inbound (product signals → research): [bridges/oroma-signal-ingest.md](../bridges/oroma-signal-ingest.md)

## Current cross-program research questions

1. How should Oroma explain "what members can see" so elders trust it?
2. Which Oroma signals are worth turning into research sessions vs. noise?
3. Does verifiable-record framing actually raise community trust (OGI thesis)?
4. Can Layer Promotion Error benchmarks prevent research agents from turning derived, blocked, or rights-uncleared claims into source or publication claims?

## Known drift to resolve (separate, sign-off-gated pass)

- Legacy provider-specific session-harness diagrams are stale vs. the live tree.
- ICEGOV deadline + canonical-paper filename disagree across root docs.
- Multiple navigation roots exist; this atlas is the intended single entry.
