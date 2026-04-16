# The Beaconsmith Research Spine
> Architecture specification for the living research system connecting Oroma (product) to etisiobi (research archive).
> Status: Design document — Stage 1 buildable now.

---

## The Core Idea

Oroma is a community coordination OS. Etisiobi is its research twin.

Every consequential Oroma action already produces a `domain_event` — append-only, with provenance, authority, intent, and causal chain. That event log is already research-grade by design. The Research Spine routes it into structured research memory.

**The flow:**
```
Oroma product activity
    → domain_events (DB)
    → evidence extractor (Python script)
    → normalized research facts (JSON + MD)
    → etisiobi research programs (wikis, logs, indicators)
    → autoresearch loop (Claude agent)
    → updated paper, open questions, contradiction tracker
```

No hallucination. Every research claim traceable to a source event. Research stops pretending certainty where evidence is absent.

---

## The Five Loops

### Loop 1: Evidence Extraction (daily)
**Runs:** Daily cron, triggered on workspace activity, or manually
**Does:**
- Queries Oroma DB for new domain_events, proposals, cases, records
- Computes OGI indicator values for each active workspace
- Writes `research/icegov/facts/YYYY-MM-DD.json` + `.md`
- Flags uncomputable indicators with reason

**Output example (`research/icegov/facts/2026-04-20.json`):**
```json
{
  "date": "2026-04-20",
  "workspaces": [
    {
      "id": "ws_abc123",
      "alias": "workspace_alpha",
      "measurement_period": "2026-01-20 to 2026-04-20",
      "indicators": {
        "RV-01": { "value": null, "status": "no_testnet_activity", "note": "0 events with blockRef" },
        "DPR-01": { "value": null, "status": "no_testnet_activity" },
        "TTI-01": { "value": null, "status": "no_treasury_movements" },
        "DRL-01": { "value": null, "status": "no_disputes_opened" }
      },
      "OGI_core": null,
      "raw_counts": {
        "total_domain_events": 0,
        "proposals_initiated": 0,
        "treasury_movements": 0,
        "cases_opened": 0
      }
    }
  ],
  "contradictions": [
    "TTI-01 uncomputable: purpose field enforcement not at contract level",
    "FID-01 uncomputable: onboarding survey event missing from schema",
    "CPS-01 uncomputable: credential.exported event not in domain_events"
  ],
  "product_gaps": [
    "ZK solvency proof event (TTI-02): not in schema",
    "member.onboarding_survey_submitted: not in schema",
    "credential.exported with evidenceEventCount: not in schema",
    "case.reopened event: not in schema"
  ],
  "schema_version": "2026-04-16",
  "extractor_version": "0.1.0"
}
```

### Loop 2: Research Synthesis (weekly)
**Runs:** Weekly, after evidence extraction
**Does:**
- Reads last 7 days of facts files
- Updates `research/icegov/WIKI.md` with new observations
- Updates `log.md` with weekly summary
- Identifies trends across workspaces
- Flags paper claims that are now stale or unsupported

### Loop 3: Contradiction Tracking (continuous)
**Runs:** Every evidence extraction cycle
**Does:**
- Checks each OGI indicator: is it computable from current DB state?
- Checks paper claims: does current evidence support them?
- Writes to `research/icegov/contradictions/`
- Generates a "research debt" list: what the product must build for research to compute

**Example contradiction:**
```
CONTRADICTION: paper claims DRL-01 measurable from Truth Layer dispute desk records.
DB state: cases.findings is NULL for 3 of 4 resolved cases in workspace_alpha.
Status: uncomputable — paper claim not yet verifiable.
Action required: Product must enforce findings field on case closure.
```

### Loop 4: Method Refinement (manual, triggered)
**Runs:** When a skill produces bad output or a new research program starts
**Does:**
- Updates skills/ based on what worked/failed
- Improves extraction queries based on new schema
- Refines paper writing templates for new venues

### Loop 5: Publication Gate (human-triggered)
**Runs:** Only when human says "prepare this for publication"
**Does:**
- Checks evidence support for every paper claim
- Flags claims with insufficient evidence
- Generates evidence citation table mapping paper sections to facts files
- Creates a publication readiness report
- Does NOT auto-publish anything

---

## Stage 1: Minimal Viable Spine (build now)

### What to build

**File: `spine/extractor.py`**
```python
# Connects to Oroma DB (read-only connection string from .env)
# Queries domain_events, proposals, cases, records
# Computes OGI-Core indicators
# Writes facts JSON + MD
# Updates contradictions tracker
```

**File: `spine/synthesize.py`**
```python
# Reads last N days of facts
# Updates WIKI.md evidence section
# Appends to log.md
# Outputs weekly summary
```

**File: `spine/.env.example`**
```
OROMA_DB_URL=postgresql://readonly_user:...@localhost:5432/oroma
RESEARCH_REPO_PATH=/path/to/etisiobi
WORKSPACE_IDS=ws_abc123,ws_def456
```

**CI: `.github/workflows/daily_extraction.yml`**
```yaml
on:
  schedule:
    - cron: '0 6 * * *'  # 6am daily
  workflow_dispatch:
jobs:
  extract:
    steps:
      - uses: actions/checkout@v3
        with:
          repository: beaconsmith/etisiobi
      - run: python spine/extractor.py
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: "spine: daily evidence extraction [automated]"
```

### What this unlocks

Once running:
- Every day, etisiobi has a new facts file showing exactly what's computable
- Contradictions surface automatically — product can see what research needs
- Paper Section 6 gets real evidence instead of mock data
- The "ongoing research" framing becomes genuinely ongoing

---

## Stage 2: Product/Research Sync (after April 24)

Build bidirectional signal:

**Research → Product:**
- Contradiction tracker generates `RESEARCH_PRODUCT_REQUIREMENTS.md`
- Each OGI gap maps to a specific product task:
  - "Add `member.onboarding_survey_submitted` event" → FID-01
  - "Enforce `cases.findings` on closure" → DRL-01
  - "Add `credential.exported` event with evidenceEventCount" → CPS-01
  - "Add `treasury.solvency_proof_generated` event" → TTI-02

**Product → Research:**
- When a new feature ships, the extractor automatically detects new event types
- Logs: "TTI-02 is now computable — first solvency proof event detected"
- Updates paper evidence table automatically

---

## Stage 3: Persistent Research Maintainer (Hermes-compatible)

A long-running agent with memory across sessions:
- Knows which workspaces are active pilots
- Tracks indicator trends over time
- Flags when a workspace's score drops (governance quality signal)
- Runs literature health checks: are there new papers in the OGI space?
- Maintains the PAGC wiki in parallel

The Hermes agent architecture (NousResearch) is the right substrate for this — persistent memory, skill accumulation, scheduled runs.

---

## Stage 4: Multi-Program Research Archive

As Oroma adds more community types, research programs branch:

```
research/
├── icegov/          ← OGI indicators (current)
├── pagc/            ← PAGC theory (current)
├── oroma-os/        ← Architecture and coordination design research
├── pilots/          ← Pilot community case studies (consented, anonymized)
├── agents/          ← When agents run in Oroma, study their behavior
└── trust-repair/    ← How communities recover from treasurer failure, fraud, disputes
```

Each program has: WIKI.md, INDEX.md, facts/, contradictions/, log.md, paper/

---

## What This Is Not

- Not automatic publishing (human gate required)
- Not a replacement for IRB/ethics (policy layer needed before pilot data)
- Not a hallucination printer (every claim traced to source event or marked as hypothetical)
- Not "AI writing research" — AI organizes evidence, humans decide what it means

---

## The Deepest Opportunity

Etisiobi becomes the research twin of Oroma.

Product changes → research evidence.
Research contradictions → product backlog.
Paper claims → machine-checkable against current DB state.
Pilot activity → live evidence trail.

Almost no product-research pair has this. The ones that do produce the best longitudinal research on their own systems.

---

## Immediate Next Steps

1. **Fix paper v3** — remove mock data, replace Buterin with Beetham/Tyler/Suchman, fix AI-sounding language
2. **Build `spine/extractor.py`** — connects to Oroma DB, outputs first facts file (even if all values are null, that's honest evidence of current state)
3. **Add 4 missing events to Oroma** — the ones blocking OGI-Core computability
4. **Set up daily GitHub Action** — automated evidence extraction to etisiobi
5. **Submit paper on April 24** — with Section 6 honestly framed as "framework with illustrative computability demonstration"
