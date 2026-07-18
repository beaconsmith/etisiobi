# Oroma
> status: maintained | updated: 2026-06-09

## What it is
Oroma ("orange" in Igbo — a fruit-bearing tree) is The Beaconsmith Collective's
product: a **community operating system** for town unions, associations,
cooperatives, churches, and diaspora branches in Southeast Nigeria. Every serious
action (a payment, receipt, approval, meeting, report, question) is meant to leave
a clear record, evidence, review, visibility decision, next step, and history.

Oroma is **not** a dashboard, a chatbot, or a blockchain app. User-facing language
stays simple (Record, Receipt, Meeting, Decision, Approval, Report, "what members
can see"). Blockchain/agent terms are internal only.

## Current state / stage
- Pre-pilot. **Fixture-backed**, no real community users yet.
- Active frontend: `apps/component-lab` (despite "backend-only" doctrine).
- Local repos observed: `C:\Users\USER\code\Orange` (the *oroma-backend-core*
  extraction — contracts/db/services/agents-api/sdk + component-lab) and
  `C:\Users\USER\code\oroma` (the `kb/`+`knowledge/` tree that
  `research/icegov/PRODUCT_BRIDGE.md` points at). `needs-review`: which is
  canonical product truth today is ambiguous and should be confirmed.
- Doctrine lives in `Orange/docs/current/*` (~38 docs) governed by `AGENTS.md`.

## What we believe (claim status + sources)
- The **Community Work Protocol + local Proof Fabric** is built and passing —
  protocol primitives (WorkItem, EvidenceBundle, ReviewDecision, VisibilityDecision,
  PolicyVersion, PreservationEnvelope), deterministic hashing, private-field
  exclusion, and a chain-free preservation slice on the Reports page.
  `supported` (verified 2026-06-09: typecheck/build/37 proof checks/5 screenshots).
- Citrea sits behind an adapter; the app works without a chain. `supported`.
- The OGI indicators Oroma must support (RV/DPR/TTI/DRL/CPS) depend on Oroma
  emitting specific domain events; several are still `blocked`/`needs-review`
  per `research/icegov/PRODUCT_BRIDGE.md` and `ETISIOBI_OROMA_FEED.md` blockers.

## Open questions
- Do members understand "what members can see" / "not complete yet"? (untested)
- Which institution types need distinct templates?
- What raises trust: verifiable records, or simply clear records?

## What Etisiobi must watch
- Onboarding drop-offs, role confusion, copy confusion, Ask-Oroma failure cases,
  report-preview failures, redaction incidents — **anonymized signals only**
  (see `bridges/oroma-signal-ingest.md`).
- Whether the proof/preservation layer adds trust or just confuses users.

## What this teaches Oroma
- Keep the surface simple; keep the protocol sophisticated underneath.
- Do not ship proof as a feature until research shows it raises trust.
- Reverse the over-documentation reflex: validate with one real community next.

## Sources
- `Orange/docs/current/OROMA_COMMUNITY_WORK_PROTOCOL.md` and siblings
- `research/icegov/PRODUCT_BRIDGE.md`, `research/icegov/OROMA_OGI_SCHEMA_MAP.md`
- `ETISIOBI_OROMA_FEED.md`
