# Etisiobi
> status: maintained | updated: 2026-06-09

## What it is
Etisiobi ("the tree from my heart"; named for Late Prof. Etisiobi Ndiokwelu) is
The Beaconsmith Collective's **research studio and research memory** — the twin of
the product, Oroma. It houses active research programs, literature wikis,
experiment logs, claims, and paper drafts, built from and for communities in
Enugu / Southeast Nigeria (CARE principles).

## Current state / stage
- Two active programs: **ICEGOV / OGI** (community-governance indicator framework,
  ICEGOV 2026 submission) and **PAGC** (Nwagụ Aneke syllabary compression study).
- Mature research operating system already in place: autoresearch harness,
  evidence/claim/publication gates, Obsidian vault, per-program wikis, skills.

## How it works (raw → wiki → schema)
- **Raw (immutable):** `external_sources/source_notes/`, `library/`, program
  `sources/`, `obsidian_vault/Sources/`. Never rewritten — new evidence = new file.
- **Wiki (maintained):** `research/*/WIKI.md`, `obsidian_vault/`, and cross-program
  pages under `wiki/` (this layer).
- **Schema (rules):** `AGENTS.md`, `research/AGENTS.md`, `skills/*`,
  `EVIDENCE_POLICY.md`, `CLAIM_MATURITY_MODEL.md`, `HUMAN_APPROVAL_GATES.md`.
- **Index:** `wiki/index.md` (atlas), `obsidian_vault/00_Home.md`.
- **Log:** `log.md`, `reflection_log.md`.

## How research becomes product decisions
1. Oroma signal or field observation → 2. research question / session →
3. sources + evidence → 4. claim (with status) → 5. review →
6. product implication → 7. `ETISIOBI_OROMA_FEED.md` item → 8. Oroma ticket →
9. UX/test/screenshot confirms → 10. learning recorded.

## What is not allowed
- Modifying raw sources.
- Treating an unreviewed claim as product truth.
- Writing Oroma product doctrine from research without human review.
- Ingesting private Oroma data (names, amounts, contacts, receipts).

## What Etisiobi must watch
- Drift between documented and actual repo structure.
- Memory sprawl: prefer updating canonical pages over creating new ones.

## Sources
- `README.md`, `AGENTS.md`, `ETISIOBI_RESEARCH_DOCTRINE.md`,
  `ETISIOBI_KNOWLEDGE_PIPELINE.md`, `ETISIOBI_REPO_ALIGNMENT_AUDIT.md`
