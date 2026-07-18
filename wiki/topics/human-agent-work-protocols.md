# Topic: Human-Agent Work Protocols (Flow-style lessons)
> status: maintained | updated: 2026-06-09
> sources: Flow-Research (Jarvis, Workstream, Harnessy, knowledge-base), IC3 crypto×AI survey

## The core lesson
Serious work should not live only in chat. It should become a **durable record**
with: a purpose, the records/sources used, evidence, human review, a decision, a
next step, history, and (optionally) a learning. The primitive is not
`User → Agent → Answer`; it is a reviewable, evidence-backed work session.

## What applies to Etisiobi
- A research run is a **ResearchSession**, not a chat: question → sources →
  claims → review → product implication → learning. Etisiobi already models this
  (autoresearch harness, claims, evidence/publication gates).
- **Policy before autonomy.** Manual-first; add automation only after the review
  loop is proven. Etisiobi's human-approval gates already encode this.
- **Evidence before acceptance.** A claim is not "supported" until it cites raw
  sources. Mirrors `EVIDENCE_POLICY.md` / `CLAIM_MATURITY_MODEL.md`.

## What applies to Oroma
- Every question, payment, receipt, approval, report, meeting leaves a record,
  evidence, review, and next step. (This is the Community Work Protocol — built.)
- Agents may draft, find, summarise, compare, suggest. Agents may **not** approve,
  pay, publish, change roles, or expose private data without human review.

## What not to copy
- Flow's labor-market / reputation-score / token framing — out of scope for
  community finance and for research integrity.
- Agent-first product language. Internally sophisticated; externally simple.
- "Transparent = trustworthy." IC3 is explicit: recording provenance on-chain does
  not prove a model (or a record) behaved correctly.

## What this teaches Oroma
Build the **memory, evidence, review, and learning rails** first. Agents become
safe and useful only on top of those rails — not before them.
