# Research Registry
> Single source of truth for all research programs, indicators, evidence classes, and promotion rules.
> Everything else in this repo derives from this document.
> Do not let scripts, papers, or wikis define their own standards — point them here.

---

## Programs

| ID | Name | Status | Paper venue | Key file |
|----|------|--------|-------------|----------|
| `icegov` | OGI Framework — Community-Led Digital Governance | Active | ICEGOV 2026 Track 6, deadline Apr 24 2026 | `research/icegov/paper/OGI_PAPER_DRAFT_v2.md` |
| `pagc` | Principle of Ancestral Generative Compression | Active | TBD | `research/pagc/INDEX.md` |
| `oroma-os` | Oroma Architecture Research | Seed | TBD | — |
| `pilots` | Community Pilot Studies | Pending ethics clearance | TBD | — |
| `agents` | Agent Behavior Research | Future | TBD | — |
| `trust-repair` | How Communities Recover | Future | TBD | — |

---

## Evidence Classes

Every piece of evidence in this repo must be classified. Nothing enters a paper or memo without a declared class.

| Class | Definition | Can be automated? | Requires human review? |
|-------|-----------|-------------------|----------------------|
| `RAW_FACT` | Direct output of a DB query or on-chain read. No interpretation. | Yes | No |
| `STRUCTURED_FACT` | Normalized research event derived from raw facts, with schema version pinned. | Yes | No |
| `DRAFT_INSIGHT` | Agent-generated interpretation of structured facts. Not a claim. | Yes | **Yes — before sharing** |
| `PUBLISHABLE_CLAIM` | A statement intended for a paper, memo, or public artifact. | **Never** | **Yes — always** |
| `ILLUSTRATIVE` | A hypothetical value or scenario used to demonstrate computability. Must be explicitly labelled. | Yes | No |
| `HUMAN_JUDGMENT` | A qualitative statement from a named human with direct knowledge. | No | Implicit |

**Rule:** Nothing in a paper or public document may be `RAW_FACT` or `STRUCTURED_FACT` alone. It must be promoted through human review to `PUBLISHABLE_CLAIM`, or explicitly labelled `ILLUSTRATIVE`.

---

## OGI Indicator Registry (Program: icegov)

| Indicator | Name | Status | Evidence source | Blocked by |
|-----------|------|--------|----------------|-----------|
| RV-01 | Verifiable Action Coverage Rate | `partial` | `domain_events.provenance.blockRef` | Needs testnet activity |
| DPR-01 | Active Governance Participation Rate | `partial` | `domain_events`, `members` | Needs testnet activity |
| DPR-02 | Quorum Achievement Rate | `partial` | `proposals` | Needs testnet activity |
| TTI-01 | Treasury Audit Completeness Rate | `partial` | `domain_events` treasury events | Purpose enforcement not at contract level |
| TTI-02 | Solvency Provability Score | `blocked` | `domain_events` | `treasury.solvency_proof_generated` event missing |
| DRL-01 | Dispute Resolution Completeness | `partial` | `cases` | `cases.findings` not always populated |
| DRL-02 | Outcome Contestation Rate | `blocked` | `domain_events` | `case.reopened` event missing |
| DRL-03 | Resolution Speed | `partial` | `cases.closed_at - cases.created_at` | Needs resolved cases |
| CPS-01 | Portable Identity Coverage | `blocked` | `domain_events` | `credential.exported` event missing |
| CAS-01 | Record Exportability Rate | `partial` | `records.verification_state` | Needs verified records |
| FID-01 | First-Time Formal Participant Rate | `blocked` | `domain_events` | `member.onboarding_survey_submitted` event missing |
| FID-02 | Gender Participation Parity | `blocked` | `members` | Gender field not in schema — **governance-sensitive** |
| FID-03 | Diaspora Integration Rate | `blocked` | `members`, `domain_events` | Diaspora flag not in schema — **governance-sensitive** |

**OGI-Core** = RV-01 + DPR-01 + TTI-01 + DRL-01 (equally weighted). Computable once testnet has governance activity.

### Indicator statuses
- `computable` — can be computed from current DB state with real data
- `partial` — formula exists, blocked only by absence of testnet activity
- `blocked` — formula exists but a required DB field or event type is missing
- `deprecated` — no longer in current framework version

---

## Contradiction Schema

Every contradiction must have these fields. Managed in `research/<program>/contradictions/`.

```yaml
id: CONT-001
program: icegov
indicator: DRL-01
type: missing_instrumentation | sensitive_identity | incoherent_ratio | unverifiable_provenance | paper_claim_unsupported
severity: blocker | major | minor
description: "cases.findings is NULL for all resolved cases — DRL-01 uncomputable"
unblock_condition: "Product must enforce findings field on case.status = resolved transition"
product_backlog_item: "Add DRL-01 evidence enforcement to case closure flow"
paper_impact: "Section 6 DRL-01 must remain illustrative until resolved"
status: open | resolved
opened: 2026-04-16
resolved: ~
```

### Contradiction types
- `missing_instrumentation` — a required event type or field is absent from schema (normal product gap, engineering backlog)
- `sensitive_identity` — a required attribute involves personal/demographic data requiring governance approval before collection (separate backlog, requires policy decision)
- `incoherent_ratio` — computed indicator value is outside expected range, suggesting a data problem
- `unverifiable_provenance` — event exists but blockRef or txRef is null, making ISO 15489 compliance fail
- `paper_claim_unsupported` — a sentence in the paper cannot be traced to any evidence class

---

## Output Promotion Rules

```
RAW_FACT
  └─ extractor.py writes automatically
  └─ stored in research/<program>/facts/

STRUCTURED_FACT
  └─ indicator registry interprets automatically
  └─ stored in research/<program>/facts/ (same files, separate fields)

DRAFT_INSIGHT
  └─ agent-generated synthesis
  └─ stored in research/<program>/drafts/
  └─ REQUIRES: human reads and marks "reviewed by [name] on [date]"

PUBLISHABLE_CLAIM
  └─ REQUIRES: claim ledger entry
  └─ REQUIRES: evidence reference (facts file + indicator version)
  └─ REQUIRES: named human reviewer
  └─ stored in research/<program>/claims/
```

---

## Sovereignty Rules (Workspace Consent)

Before any workspace data contributes to a paper or public artifact:

```yaml
workspace_id: ws_xxx
research_consent:
  allow_aggregation: false       # may workspace metrics appear in aggregate stats?
  allow_publication: false       # may findings appear in publications?
  anonymization_level: strict    # strict | partial | none
  approved_by: actorRef          # who in the workspace approved this
  approved_at: ~
  retention_days: 365
  deletion_on_exit: true
```

**Default**: all fields false / strict until explicitly set.

**Separation rule**: "missing instrumentation" contradictions go to product engineering backlog. "sensitive identity" contradictions (FID-02 gender, FID-03 diaspora) go to a governance policy decision track — different approvers, different timelines, different consent requirements.

---

## Validator Invariants (for daily extraction)

Before any facts file is written, these checks must pass:

1. No metric published without `provenance.blockRef` for on-chain claims
2. No cohort metric from a group smaller than 5 workspaces
3. No indicator promoted if underlying SQL changed without version bump
4. No export from a workspace lacking `research_consent.allow_aggregation = true`
5. No `PUBLISHABLE_CLAIM` without a claim ledger entry
6. No indicator status changed without updating this Registry

---

## Schema + Extractor Versioning

Every facts file must record:
- `schema_version` — date of last schema change in Oroma DB
- `extractor_version` — version of `spine/extractor.py`
- `registry_version` — version of this file (use date: YYYY-MM-DD)

If any of these change, all downstream `DRAFT_INSIGHT` and `PUBLISHABLE_CLAIM` artifacts must be re-reviewed.

**Current versions:**
- schema_version: `2026-04-16`
- extractor_version: `0.1.0`
- registry_version: `2026-04-16`
