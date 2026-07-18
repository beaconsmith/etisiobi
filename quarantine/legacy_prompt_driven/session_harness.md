# etisiobi — Research Studio Harness
> *signals from the tree* | The Beaconsmith Collective Research Archive

## What This Repo Is

etisiobi is the research infrastructure for The Beaconsmith Collective — a creative-technology studio based in Enugu, Southeast Nigeria. It houses active research programs, literature wikis, experiment logs, and paper drafts.

**Current active research programs:**
1. **ICegov / OGI** — Oroma Governance Indicator Framework for community-led digital governance in Southeast Nigeria. Paper submitted/submitting to ICEGOV 2026 (Track 6, deadline April 24, 2026).
2. **PAGC** — Principle of Ancestral Generative Compression. Cross-disciplinary study of the 27-base × 8-modifier matrix originating from the Nwagu Aneke Igbo syllabary.

**The studio's research method:** Karpathy autoresearch loop (metric-driven iteration) + Orchestra Research Skills (fat markdown skills) + gstack ETHOS (boil the lake, search before building, user sovereignty).

---

## Repo Structure

```
etisiobi/
├── CLAUDE.md                   ← You are here. Loaded every session.
├── README.md                   ← Public-facing studio overview
├── log.md                      ← Append-only studio research log
│
├── research/
│   ├── icegov/                 ← OGI Framework / community governance
│   │   ├── WIKI.md             ← Compiled knowledge wiki (LLM-maintained)
│   │   ├── INDEX.md            ← Source catalog with one-line summaries
│   │   ├── sources/            ← Raw + compiled sources by cluster
│   │   │   ├── cluster1_6_frameworks/
│   │   │   ├── cluster2_3_nigeria_isusu/
│   │   │   ├── cluster4_5_records_blockchain/
│   │   │   ├── cluster7_crosscutting/
│   │   │   └── synthesis/
│   │   └── paper/              ← Draft versions + autoresearch evals
│   │       ├── OGI_PAPER_DRAFT_v2.md   ← CURRENT SUBMISSION DRAFT
│   │       └── AUTORESEARCH_EVAL_v2.md
│   │
│   └── pagc/                   ← PAGC research (existing work)
│       ├── WIKI.md             ← (to be compiled)
│       ├── INDEX.md            ← existing INDEX.md
│       ├── disciplines/        ← existing discipline analyses
│       ├── sources/            ← existing pagc_library/ + downloaded papers
│       └── paper/              ← existing autoreason drafts
│
├── experiments/                ← Active empirical experiments
│   ├── 01_bpe_igbo_k27/        ← BPE sweep for Igbo k=27
│   └── 05_sovereign_memory_rl/ ← Sovereign Memory RL simulation
│
└── skills/                     ← Reusable research methodology skills
    ├── autoresearch.md         ← Karpathy loop applied to research papers
    ├── literature-sweep.md     ← 7-cluster sweep methodology
    ├── indicator-framework.md  ← OGI framework design pattern
    └── paper-writing.md        ← ICEGOV Track 6 paper structure
```

---

## Active Research: ICegov OGI Framework

**Status:** Draft v2 complete. Score: 4.70/5. Ready for EDAS submission.
**Deadline:** April 24, 2026.
**Track:** ICEGOV 2026 Track 6 — New Metrics and Approaches for Measuring Digital Governance Success.
**Key file:** `research/icegov/paper/OGI_PAPER_DRAFT_v2.md`

**Before submission checklist:**
- [ ] Confirm Workspace A data is real on-chain evidence OR relabel as "illustrative case"
- [ ] Convert to ACM two-column format
- [ ] Double-blind check: grep for "Oroma", "Beaconsmith", "Citrea", "Enugu" — anonymize
- [ ] EDAS account + abstract paste (231 words)
- [ ] Page limit check (8-10 pages ACM format)

**Product-research sync requirements (Oroma must build before pilot):**
1. Dispute state machine closure state → enables DRL-01
2. Ichi credential issuance contract enforcement (3 events minimum) → enables CPS-01
3. TTI-01 metadata enforcement at contract level (purpose ≥50 chars, proposalId ref)
4. Onboarding survey question at wallet creation → enables FID-01

---

## Active Research: PAGC

**Status:** Cross-disciplinary literature sweep complete (~120 sources). BPE experiments running. Sovereign Memory RL simulation complete.
**Current focus:** Mathematical falsification tests — E₆ symmetry claim, universal compression claim.
**Key file:** `research/pagc/INDEX.md` (currently at repo root as `INDEX.md`)

---

## How to Work in This Repo

### Starting a new session
Say: "I'm continuing work on [icegov/pagc/experiments]. What's the current state?"
Claude will read the relevant WIKI.md and recent log entries to resume context.

### Adding a source
1. Drop raw content into `research/[program]/sources/`
2. Say: "Ingest this source into the [program] wiki"
3. Claude updates WIKI.md, INDEX.md, and log.md

### Running an autoresearch iteration
Say: "Run autoresearch loop on [paper/section/experiment]"
Claude applies: draft → evaluate against metric → identify revisions → apply → re-score

### Running a literature sweep
Say: "Sweep [topic] for [program]"
Claude uses the `skills/literature-sweep.md` methodology

---

## Studio Principles (from gstack ETHOS)

1. **Boil the Lake** — Write the complete thing. Completeness is cheap with AI.
2. **Search Before Building** — Prize first-principles observations that zig while others zag.
3. **User Sovereignty** — Claude generates and recommends. You decide what gets published.
4. **Artifact-First** — Research claims must be backed by verifiable artifacts, not just assertions.
5. **Community Sovereignty** — Research about communities must serve those communities (CARE Principles).
