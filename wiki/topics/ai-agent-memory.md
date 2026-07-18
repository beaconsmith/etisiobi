# Topic: AI Agent Memory (the LLM Wiki pattern)
> status: maintained | updated: 2026-06-09
> primary source: `external_sources/source_notes/EXT-0017-karpathy-autoresearch.md`

## The pattern
`raw sources (immutable) → wiki (maintained) → schema (rules)`

- **Raw sources** are immutable evidence. You never rewrite them; new evidence is
  a new file. They are the ground truth a claim can be traced back to.
- **The wiki** is maintained memory. Agents connect, summarise, merge, and update
  it. It is the working belief state — not a transcript.
- **The schema** is the procedure for maintaining memory: where things go, how
  claims are marked, what must never be touched. It lives in `AGENTS.md` + skills.
- **Search/embeddings** may help *navigate* memory later. They do not *define* it.
  The maintained markdown is the memory; search is an index over it.

## Memory types (and where they live here)
- **Semantic** — general knowledge: `research/*/WIKI.md`, `wiki/topics/*`.
- **Entity** — knowledge about specific actors/systems: `wiki/entities/*`.
- **Episodic** — what happened and when: `log.md`, `reflection_log.md`, runs.
- **Summary** — condensed sources linked back to raw: `external_sources/source_notes/*`.
- **Procedural** — how to operate: `AGENTS.md`, `skills/*`, policies.
- **Claim** — discrete assertions with status: `obsidian_vault/Claims/*`, `uncertainty/*`.

## Why this matters to Etisiobi
Etisiobi already runs this pattern (the Karpathy autoresearch loop is the same
lineage). The risk is not "we lack a memory model" — it is **memory sprawl**:
several overlapping wikis and indexes. The discipline to take from the pattern is:
*update canonical pages; don't fork new ones; keep one navigation root; keep raw
immutable.* See `ETISIOBI_REPO_ALIGNMENT_AUDIT.md`.

## What not to copy blindly
- Do not bolt on a vector DB and call it "memory." The markdown is the memory.
- Do not auto-generate wiki pages without review — generated clutter is worse than
  a gap. Human sovereignty over what gets promoted stays.
- Do not let "memory" ingest private product data (see the inbound-signal rules).

## What this teaches Oroma
The same separation Oroma already uses: *Recorded ≠ Reviewed ≠ Complete ≠
Preserved.* A stored record (or a hash) is not proof the underlying event was
true. Transparency ≠ trustworthiness.
