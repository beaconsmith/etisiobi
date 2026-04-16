---
id: CONT-002
program: icegov
indicator: TTI-02
type: missing_instrumentation
severity: blocker
status: open
opened: 2026-04-16
---

# CONT-002: treasury.solvency_proof_generated event missing from schema

**Description:** TTI-02 requires a `treasury.solvency_proof_generated` event in `domain_events` to confirm a ZK solvency proof was generated and verified on-chain. This event type does not exist. The ZK circuit itself (Circom + SnarkJS) is in development but the corresponding audit event is not wired into the domain event log.

**Unblock condition:** When a ZK solvency proof is generated, a `treasury.solvency_proof_generated` domain event must be written with `payload: { proofHash, verifiedOnChain: boolean, balanceThreshold }` and `provenance.txRef` pointing to the on-chain verification transaction.

**Product backlog item:** "Emit domain event on ZK solvency proof generation" — wire into Akpa Oroma module.

**Paper impact:** TTI-02 remains `blocked` in the indicator registry. Paper v3 must note this as future work.

**Resolution:** ~
