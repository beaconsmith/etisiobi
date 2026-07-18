# etisiobi — Research Studio Harness
> *signals from the tree* | The Beaconsmith Collective Research Archive

## What This Repo Is

etisiobi is the research infrastructure for The Beaconsmith Collective — a creative-technology studio based in Enugu, Southeast Nigeria. It houses active research programs, literature wikis, experiment logs, and paper drafts.

**Current active research programs:**
1. **ICegov / OGI** — Oroma Governance Indicator Framework for community-led digital governance in Southeast Nigeria. Paper submitted/submitting to ICEGOV 2026 (Track 6, deadline May 8, 2026).
2. **PAGC** — Principle of Ancestral Generative Compression. Artifact-first study of the Nwagu Aneke source layer and its system-design applications. Current working foundation: source-observed 26 rows × 8 vowel/modifier columns = 208 records; 27 / 216 is a derived f/v split layer, not source-observed in the current evidence package.

**The studio's research method:** Karpathy autoresearch loop (metric-driven iteration) + Orchestra Research Skills (fat markdown skills) + gstack ETHOS (boil the lake, search before building, user sovereignty).

---

## Repo Structure

```
etisiobi/
├── AGENTS.md                   ← You are here. Loaded every session.
├── README.md                   ← Public-facing studio overview
├── CONTRIBUTING.md             ← Research workflow and folder standards
├── log.md                      ← Append-only studio research log
│
├── research/
│   ├── AGENTS.md               ← Research Operating System (autoresearch harness)
│   ├── PORTFOLIO.md            ← Portfolio triage and paper status
│   ├── QUALITY_BAR.md          ← What "submission-ready" means
│   ├── KILL_CRITERIA.md        ← When to stop working on a paper
│   ├── CHIEF_OF_STAFF.md       ← Operating cadence and research-to-product owner
│   ├── RESEARCH_ORG.md         ← Agent roles and coordination
│   ├── EVIDENCE_POLICY.md      ← Evidence handling rules
│   ├── CITATION_POLICY.md      ← Citation standards
│   ├── SUBMISSION_RULES.md     ← ICEGOV 2026 submission requirements
│   │
│   ├── papers/                 ← Per-paper autoresearch harness (7 papers)
│   │   ├── community-governance/    ← Track 11 [Tier A]
│   │   ├── artifact-first-trust/    ← Track 1  [Tier A]
│   │   ├── bitcoin-treasury/        ← Track 5  [Tier B]
│   │   ├── community-dpi/           ← Track 7  [Tier B]
│   │   ├── community-os-pilot/      ← Track 12 [Tier B]
│   │   ├── digital-sovereignty/     ← Track 2  [Tier C — kill candidate]
│   │   └── platform-governance/     ← Track 10 [Tier C — kill candidate]
│   │
│   ├── icegov/                 ← OGI Framework (Submitted — Track 6)
│   │   ├── WIKI.md
│   │   ├── INDEX.md
│   │   ├── facts/
│   │   ├── contradictions/
│   │   └── paper/
│   │
│   ├── icegov_2026/            ← Raw Research Logs (ingested → papers/)
│   │   ├── track_11_global_south/
│   │   ├── track_1_trust/
│   │   ├── track_5_emerging_tech/
│   │   ├── track_7_dpi/
│   │   ├── track_2_sovereignty/
│   │   ├── track_12_experiments/
│   │   └── track_10_policy/
│   │
│   └── pagc/                   ← PAGC research (Long-term)
│       ├── WIKI.md
│       ├── INDEX.md
│       ├── facts/
│       ├── contradictions/
│       └── paper/
│
├── experiments/                ← Active empirical experiments
├── library/                    ← Global Research Library (formerly sources)
│   ├── papers/                 ← Academic PDF collection
│   └── research_pipeline/      ← Global metadata and logs
├── spine/                      ← Research Infrastructure (The Spine)
│   ├── ARCHITECTURE.md         ← Spine design specification
│   └── extractor.py            ← Evidence extraction engine
└── skills/                     ← Reusable research methodology skills
```


---

## Active Research: ICegov OGI Framework

**Status:** Canonical blinded submission draft frozen on 2026-04-20. Compressed for ACM 8-10 page target; final PDF page check still pending.
**Deadline:** May 8, 2026.
**Track:** ICEGOV 2026 Track 6 — New Metrics and Approaches for Measuring Digital Governance Success.
**Key file:** `research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md`

**Before submission checklist:**
- [x] Workspace A / prototype evidence relabeled as illustrative design-science demonstration
- [x] Convert to ACM two-column format
- [x] Double-blind submission draft prepared — direct identifiers stripped
- [x] EDAS account + abstract paste (246 words)
- [x] Page limit check (8-10 pages ACM format) (Note: PDF compiles to 7 pages)

**Product-research sync requirements (Oroma must build before pilot):**
1. Dispute state machine closure state → enables DRL-01
2. Ichi credential issuance contract enforcement (3 events minimum) → enables CPS-01
3. TTI-01 metadata enforcement at contract level (purpose ≥50 chars, proposalId ref)
4. Onboarding survey question at wallet creation → enables FID-01

---

## Active Research: PAGC

**Status:** Reset under source/derived-layer discipline. Cross-disciplinary material remains historically useful, but current work must start from source-grounded Nwagu Aneke reconstruction and explicit claim gates.
**Current focus:** Applications and systems that preserve the confirmed source/derived distinction. Exceptional-math, universal-compression, and exact-27 theory branches remain speculative or rejected-for-now unless a later event promotes them with evidence.
**Key files:** `research/pagc/PAGC_RESET.md`, `research/pagc/primary_sources/nwagu_aneke/README.md`, and `spine/events/current_state.md`.

---

## How to Work in This Repo

### Starting a new session
Say: "I'm continuing work on [icegov/pagc/experiments]. What's the current state?"
Codex will read the relevant WIKI.md and recent log entries to resume context.

### Adding a source
1. Drop raw content into `research/[program]/sources/`
2. Say: "Ingest this source into the [program] wiki"
3. Codex updates WIKI.md, INDEX.md, and log.md

### Running an autoresearch iteration
Say: "Run autoresearch loop on [paper/section/experiment]"
Codex applies: draft → evaluate against metric → identify revisions → apply → re-score

### Running a literature sweep
Say: "Sweep [topic] for [program]"
Codex uses the `skills/literature-sweep.md` methodology

---

## Studio Principles (from gstack ETHOS)

1. **Boil the Lake** — Write the complete thing. Completeness is cheap with AI.
2. **Search Before Building** — Prize first-principles observations that zig while others zag.
3. **User Sovereignty** — Codex generates and recommends. You decide what gets published.
4. **Artifact-First** — Research claims must be backed by verifiable artifacts, not just assertions.
5. **Community Sovereignty** — Research about communities must serve those communities (CARE Principles).

---

## Paper Readiness Requires a Research Team Trace

No agent may declare any research paper "complete", "submission-ready", or
`READY_FOR_HUMAN_ARXIV_REVIEW` unless the paper directory contains a
`review_team_trace.jsonl` file with passing reviews from at least these roles:

1. `research_lead`
2. `domain_postdoc`
3. `methods_reviewer`
4. `adversarial_impact_reviewer`
5. `citation_evidence_reviewer`
6. `rights_authority_reviewer`

Each row must record `role`, `agent_id`, `status`, `summary`, `files_reviewed`,
and `blocking_issues`. A ready paper requires `status: "PASS"` for every role
and no blocking issues. If this trace is missing or incomplete, the strongest
allowed status is `NOT_READY_REVIEW_TEAM_BLOCKED`.

Run `python scripts/validate_review_team_gate.py` before any readiness claim.

## A+ Lab Standard Gate

The lab must not manufacture quality by patching individual PDFs after review
comments. It must enforce stage discipline before outputs are promoted.

Read `research/A_PLUS_LAB_STANDARD.md` and `research/LAB_STANDARD_AUDIT.md`
before promoting any research branch toward article hardening.

No branch may look more mature than its evidence stage. A compiled PDF, a
working benchmark, or a formatted manuscript does not make a paper. The canonical
stage sequence is defined in `research/LAB_STAGE_GATES.json`:

1. `RESEARCH_PROGRAM`
2. `SOURCE_DOSSIER`
3. `CLAIM_MODEL`
4. `EXPERIMENTAL_RESULT`
5. `PAPER_CANDIDATE`
6. `SUBMISSION_CANDIDATE`
7. `PUBLIC_RELEASE_READY`

Run `python scripts/validate_lab_standard.py` before any readiness claim or
article-package regeneration.

---

## Memory Maintenance (LLM Wiki alignment)

> Added 2026-06-09. See `ETISIOBI_REPO_ALIGNMENT_AUDIT.md`. Start every session at
> `wiki/index.md` (the cross-program atlas). The memory model is
> `raw sources (immutable) → wiki (maintained) → schema (rules)`.

**Memory-type map**

| Type | Home |
|---|---|
| Navigation | `wiki/index.md`, `obsidian_vault/00_Home.md`, `repo_map.md` |
| Semantic | `research/*/WIKI.md`, `wiki/topics/*` |
| Entity | `wiki/entities/*` |
| Episodic | `log.md`, `reflection_log.md`, `research_loop_changelog.md`, runs |
| Summary | `external_sources/source_notes/*`, `library/`, program `sources/` |
| Procedural | `AGENTS.md`, `research/AGENTS.md`, `skills/*`, `EVIDENCE_POLICY.md` |
| Claim | `obsidian_vault/Claims/*`, `CLAIM_MATURITY_MODEL.md`, `uncertainty/*` |
| Product decision | `ETISIOBI_OROMA_FEED.md`, `research/icegov/PRODUCT_BRIDGE.md`, `decisions/` |
| Learning | `self_improvement_proposals/`, `research_loop_changelog.md` |

**Rules**

1. Never modify raw sources. New evidence is a new file.
2. Every wiki claim must point to source records where possible.
3. Do not create duplicate topic/entity pages — update the canonical one.
4. Update canonical pages instead of creating clutter.
5. If evidence contradicts an existing claim, add the contradiction; don't overwrite.
6. Keep `wiki/index.md` current.
7. Log meaningful ingests, merges, and decisions in `log.md`.
8. Mark claim status: `draft` / `supported` / `weak` / `contradicted` / `rejected` / `needs-review`.
9. Separate observation from interpretation.
10. Every research output should say what it teaches Oroma.
11. Do not let an agent write Oroma product doctrine without evidence and review.
12. Do not promote research-only ideas into Oroma product work without review.

**Bridges:** outbound research→product is `ETISIOBI_OROMA_FEED.md`; inbound
product→research (anonymized signals only) is `bridges/oroma-signal-ingest.md`.

**Do not** create a parallel `raw/` tree or migrate the Obsidian vault. The wiki
layer is a thin cross-program atlas, not a replacement for `research/*/WIKI.md`.
