---
id: CONT-001
program: icegov
indicator: DRL-01
type: missing_instrumentation
severity: major
status: open
opened: 2026-04-16
---

# CONT-001: cases.findings not enforced on resolution

**Description:** `cases.findings`, `cases.resolution`, and `cases.evidence_refs` are nullable in the schema. Resolved cases can close without populating them. DRL-01 (Dispute Resolution Completeness) requires all three to be non-null for a case to count as "documented." Currently unenforceable.

**Unblock condition:** Product enforces non-null `findings`, `resolution`, and at least one `evidence_refs` entry before `status` can transition to `resolved` or `dismissed`. This must be a contract-level or service-layer constraint, not just a UI suggestion.

**Product backlog item:** "Enforce DRL-01 evidence fields on case closure" — add validation in case service before status update.

**Paper impact:** `research/icegov/paper/OGI_PAPER_DRAFT_v2.md` Section 6 DRL-01 must remain `ILLUSTRATIVE` until resolved.

**Resolution:** ~
