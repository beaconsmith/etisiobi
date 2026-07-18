# Etisiobi Repo Alignment Audit

> Purpose: decide how to align Etisiobi with the LLM Wiki memory pattern
> (raw sources → wiki → schema) **before** changing anything.
> Date: 2026-06-09
> Method: full read-only inspection of the live repo on `research-hyperloop/bootstrap`.
> Status: AUDIT ONLY. No restructuring performed. Recommendation at the end.

---

## TL;DR

**Etisiobi already implements the LLM Wiki pattern — and more.** It has immutable
raw sources, LLM-maintained wikis, a procedural schema (AGENTS/skills/policies),
navigation indexes, episodic logs, claim memory, and a research→product bridge.

Therefore the proposed `raw/ wiki/ methods/ bridges/` target tree should **NOT**
be created as written. Imposing it would add a **fourth** parallel memory system
on top of three that already overlap (`research/*/`, `obsidian_vault/`, and the
top-level doctrine files). That is the exact "dumping ground / duplicate
structures" outcome the brief says to avoid.

**Recommendation: a thin overlay, not a new tree.** Adopt the LLM Wiki
*vocabulary and discipline*, map existing folders to memory types, and fill only
the genuine gaps: (1) entity memory, (2) one canonical navigation root, (3) the
**Oroma → Etisiobi signal-ingest** direction, (4) a maintained topic page that
synthesizes the memory pattern itself. Reconcile documented-vs-actual drift.

---

## 1. What already matches the LLM Wiki pattern

The pattern is `raw sources (immutable) → wiki (maintained) → schema (rules)`,
with index = navigation memory and log = episodic memory. Etisiobi covers every
layer today:

| LLM Wiki layer | Memory type | Where it already lives in Etisiobi |
|---|---|---|
| Raw sources (immutable) | Summary / evidence | `external_sources/source_notes/EXT-0001..0024` · `library/papers/` · `research/icegov/sources/cluster*` · `corpus/` · `obsidian_vault/Sources/SRC-*` · `data/igbo_corpus/` · `annotations/`, `artifacts/` (Nwagu Aneke) |
| Wiki (maintained) | Semantic | `research/icegov/WIKI.md` (explicitly *"LLM-maintained… do not edit manually"*) · `research/pagc/WIKI.md` · `obsidian_vault/` (Claims, Experiments, Goals, Possibilities, atlas notes) |
| Schema (rules) | Procedural | `AGENTS.md` · `CLAUDE.md` · `research/AGENTS.md` · `skills/*` · `EVIDENCE_POLICY.md` · `CLAIM_MATURITY_MODEL.md` · `HUMAN_APPROVAL_GATES.md` · `CITATION_POLICY.md` · `PUBLICATION_GATE.md` |
| Index (navigation) | Navigation | `obsidian_vault/00_Home.md`, `01_Repo_Atlas.md` · `repo_map.md` · `repo_index.json` · `research/icegov/INDEX.md`, `research/pagc/INDEX.md` |
| Log (episodic) | Episodic | `log.md` · `reflection_log.md` · `research_loop_changelog.md` · `research_system_status.md` · `research_runs/`, `autoresearch_runs/` |
| Claims | Claim memory | `obsidian_vault/Claims/CLAIM-*` · `CLAIM_MATURITY_MODEL.md` · `research/*/contradictions/` · `uncertainty/` (contradictions, hallucination_risks, replication_risks, weak_signals, unknowns, missing_evidence) |
| Product decisions / learnings | Decision / learning | `ETISIOBI_OROMA_FEED.md` · `research/icegov/PRODUCT_BRIDGE.md` · `research/icegov/OROMA_OGI_SCHEMA_MAP.md` · `research/product_feedback/` · `decisions/` · `self_improvement_proposals/` |

The research method is already the Karpathy autoresearch loop (the same
`EXT-0017-karpathy-autoresearch.md` source the brief wants us to apply) plus
"fat markdown skills" plus gstack ETHOS. **The memory philosophy the brief asks
for is already the house style.**

---

## 2. What is genuinely missing

These four are real gaps — not duplicates of anything that exists:

1. **Entity memory.** There is no canonical per-entity page concept. Knowledge
   about Oroma, Citrea, Miden, Flow-Research, IC3, LEMA Lab, etc. is scattered
   across program wikis and source notes. An `entities/` layer (one maintained
   page per actor/system/standard) is the cleanest non-duplicative addition.

2. **One canonical navigation root for the whole repo.** There are *several*
   competing entry points (`obsidian_vault/00_Home.md`, `repo_map.md`,
   `repo_index.json`, `research_repo_audit.md`, two READMEs). None is the single
   "start here" that an agent loads first across the entire repo. `AGENTS.md` is
   procedural, not navigational. A top-level `wiki index` / atlas that points to
   the existing structures (rather than replacing them) is missing.

3. **The Oroma → Etisiobi signal-ingest direction.** Today the bridge runs
   **one way**: research → product (`ETISIOBI_OROMA_FEED.md` is an evidence-backed
   *product feedback* queue). The brief's new requirement is the **reverse**:
   Oroma emits *signals* (QA failures, friction summaries, copy/role confusion,
   onboarding drop-offs, Ask-Oroma failure cases) that become Etisiobi research
   inputs. There is no spec for that inbound direction.

4. **A maintained topic page for the memory pattern itself.** `EXT-0017` (Karpathy
   autoresearch / LLM Wiki) exists as a raw source, but there is no *maintained*
   topic page that states how Etisiobi applies raw→wiki→schema and the memory-type
   taxonomy. Same for the Flow-style human-agent work-protocol lessons.

---

## 3. What should NOT be changed

Treat these as immutable or frozen working systems:

- **Raw sources** — `external_sources/source_notes/EXT-*`, `library/papers/`,
  `data/igbo_corpus/`, `annotations/`, `artifacts/`, `obsidian_vault/Sources/`.
  Never rewrite. New evidence = new file.
- **Frozen submission artifacts** — `research/icegov/paper/*` (canonical/blinded
  drafts), `papers/SELECTED_PAPER/*`, reviewer packets, claim/novelty gates.
- **Working procedural memory** — `AGENTS.md`, `research/AGENTS.md`, `skills/*`,
  `EVIDENCE_POLICY.md`, `CLAIM_MATURITY_MODEL.md`, `HUMAN_APPROVAL_GATES.md`,
  `PUBLICATION_GATE.md`. These already encode the rules; extend, don't replace.
- **The Obsidian vault** — it is a live, internally-linked wiki with templates and
  canvases. Do not migrate it into a new `wiki/` tree.
- **The autoresearch harness** — `research_runs/`, `autoresearch_runs/`,
  `experiment_tracking/`, `spine/`.

---

## 4. What should be renamed or consolidated (carefully, later)

These are drift/clutter problems, not pattern problems. Flagged here; **none should
be touched in this pass** without explicit sign-off:

- **Documented-vs-actual drift.** `README.md` and `CLAUDE.md` describe a clean
  `research/{icegov,pagc}` + library + spine + skills tree. The live repo has ~40
  top-level entries (`obsidian_vault/`, `external_sources/`, `authority/`,
  `benchmarks/`, `certainty/`, `decisions/`, `emitters/`, `lineage/`,
  `observability/`, `NS modifier/`, etc.). The maps are stale.
- **Conflicting facts across roots.** Root `AGENTS.md` says ICEGOV deadline
  **May 8** and canonical = `OGI_PAPER_SUBMISSION_CANONICAL.md`; `CLAUDE.md`/`README`
  say **April 24** and `OGI_PAPER_DRAFT_v2.md`. One is stale. (Episodic memory
  should resolve this, not three docs disagreeing.)
- **Multiple navigation roots** (see gap #2) — consolidate references under one
  atlas rather than deleting any.
- **`NS modifier/`** — a full Next.js app (Arkiv ModifierVault) living inside the
  research repo. Out of scope for memory alignment; note it exists so it is not
  mistaken for research memory.

Consolidation is a **separate, sign-off-gated task.** Do not fold it into the
memory-alignment pass.

---

## 5. Where each layer should live (adapted, not the proposed tree)

| Brief's proposed path | Adapted decision (use what exists) |
|---|---|
| `raw/sources/...` | **Already exists.** Keep `external_sources/`, `library/`, program `sources/`, `obsidian_vault/Sources/`. Do not create `raw/`. |
| `wiki/topics/*` | **Already exists** as program WIKIs + obsidian notes. Add new cross-program topic pages **under the existing wiki home**, not a new `wiki/` root. |
| `wiki/entities/*` | **NEW (gap #1).** Create a single `entities/` home and populate `oroma.md`, `etisiobi.md` first. |
| `wiki/index.md` | **NEW (gap #2)** — but as a top-level atlas that *links to* `obsidian_vault/00_Home.md`, `repo_map.md`, program INDEXes. One root, not a replacement. |
| `wiki/log.md` | **Already exists** as `log.md`. Append, don't fork. |
| `methods/*` | **Already exists** as `skills/*`. Don't duplicate. |
| `bridges/oroma-research-bridge.md` | **Partly exists** (`ETISIOBI_OROMA_FEED.md` = outbound). Add the **inbound** `oroma-signal-ingest` spec (gap #3). |
| `scripts/check-wiki.mjs` | **Defer.** Structure is not yet stable; a linter now would ossify the wrong shape. |

---

## 6. How Oroma should send research signals into Etisiobi

Direction matters. Two distinct pipes:

- **Outbound (exists):** Etisiobi research → Oroma product. Lives in
  `ETISIOBI_OROMA_FEED.md` (Finding → Evidence → Recommendation → Acceptance Test)
  and `research/icegov/PRODUCT_BRIDGE.md` (OGI indicator → Oroma event).
- **Inbound (missing):** Oroma signals → Etisiobi research questions. Proposed
  spec: Oroma emits **anonymized, privacy-safe** signals only — QA report
  failures, friction summaries, onboarding drop-offs, copy/role confusion,
  Ask-Oroma thin-data/failure cases, report-preview failures, redaction
  incidents. **No raw records, amounts, contacts, receipts, or member data.**
  Each signal becomes a candidate `ResearchSession`, reviewed before it earns a
  claim. Routing today is via the sibling `../beaconos` dashboard (per README)
  and `research/product_feedback/`.

This inbound spec is the one new bridge file worth adding (gap #3).

---

## 7. Memory-type map (for AGENTS.md, once approved)

| Memory type | Canonical home in Etisiobi |
|---|---|
| Semantic | `research/*/WIKI.md` + new cross-program topic pages |
| Entity | **new** `entities/*` |
| Episodic | `log.md`, `reflection_log.md`, `research_runs/`, `research-sessions` notes |
| Summary | `external_sources/source_notes/*`, program `sources/*` (linked back to raw) |
| Procedural | `AGENTS.md`, `research/AGENTS.md`, `skills/*`, policies |
| Claim | `obsidian_vault/Claims/*`, `CLAIM_MATURITY_MODEL.md`, `uncertainty/*` |
| Product decision | `ETISIOBI_OROMA_FEED.md`, `research/icegov/PRODUCT_BRIDGE.md`, `decisions/` |
| Learning | `self_improvement_proposals/`, `research_loop_changelog.md` |
| Navigation | **new** single atlas → existing indexes |

---

## 8. Recommended deliverables for the first pass (adapted)

Minimal, non-duplicative, reversible. In priority order:

1. **This audit** (done).
2. **`entities/oroma.md`** and **`entities/etisiobi.md`** — entity memory, gap #1.
3. **`entities/README.md`** — defines what an entity page is and its update rules.
4. **`bridges/oroma-signal-ingest.md`** — the inbound signal spec, gap #3
   (complements the existing outbound `ETISIOBI_OROMA_FEED.md`).
5. **One topic page** synthesizing the memory pattern (`ai-agent-memory`) and,
   if useful, `human-agent-work-protocols` — placed under the existing wiki, gap #4.
6. **AGENTS.md update** — add the §7 memory-type map + the 12 maintenance rules
   from the brief, *adapted* to the real folder names (not the proposed tree).
7. **One `log.md` entry** recording that alignment started.

**Explicitly deferred (needs sign-off):** the full `raw/wiki/methods/scripts`
tree, any folder migration, the README/repo_map drift fix, and `check-wiki.mjs`.

---

## 9. Definition of done for alignment (revised)

- [x] Repo inspected; memory layers mapped to the LLM Wiki pattern.
- [x] Confirmed the pattern already exists; proposed tree rejected with reasons.
- [ ] Entity memory introduced (`entities/`).
- [ ] Inbound Oroma→Etisiobi signal spec added.
- [ ] Memory-type map + maintenance rules folded into `AGENTS.md`.
- [ ] Drift (README/repo_map, deadline/canonical conflict) flagged for a separate pass.
- [ ] No raw source modified. No working system migrated. No parallel `wiki/` root created.

---

*Gate satisfied: this audit is written, so targeted additions may proceed. Blind
restructuring remains prohibited until the §4/§8-deferred items are signed off.*
