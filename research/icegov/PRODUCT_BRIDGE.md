# Oroma Product Bridge

> This file connects etisiobi (research) to oroma (product).
> All paths below are relative to `C:\Users\USER\code\oroma\`.
> Read these before making any claim about what OGI can compute.

---

## Why this exists

The OGI Framework's computability claims depend on what the Oroma platform actually implements. This bridge maps each OGI indicator to the specific Oroma artifacts that make it computable — or marks it as blocked if the required artifact doesn't exist yet.

---

## Canonical product sources (read before touching §5–6 of the paper)

| What you need to know | File in oroma |
|-----------------------|---------------|
| Platform architecture overview | `kb/03_ARCHITECTURE/overview.md` |
| Truth layer (receipts, proofs) | `kb/03_ARCHITECTURE/truthos.md` |
| All domain events (the evidence base for OGI) | `knowledge/events/` |
| All domain primitives (workspace, member, treasury, etc.) | `knowledge/domain/` |
| Canonical product decisions | `kb/09_DECISIONS/` |
| Agent architecture | `kb/05_AGENTS/` |
| Compliance layer | `kb/04_COMPLIANCE/` |

---

## OGI Indicator → Oroma Event Mapping

| OGI Indicator | Required Oroma Events | Status |
|---------------|----------------------|--------|
| RV-01 — Verifiable Action Coverage | `Event_ProposalApproved`, `Event_VoteCast`, `Event_TransactionSettled`, `Event_ProofVerified` | Defined |
| DPR-01 — Active Governance Participation | `Event_VoteCast`, `Event_ProposalSubmitted`, `Event_MemberActivated` | Defined |
| DPR-02 — Quorum Achievement | `Event_ProposalApproved` (with quorum metadata) | Defined |
| TTI-01 — Treasury Audit Completeness | `Event_TransactionInitiated`, `Event_TransactionSettled`, `Event_ContributionReceived` | Defined |
| TTI-02 — Solvency Provability | `Event_ProofRequired`, `Event_ProofSubmitted`, `Event_ProofVerified` | Defined |
| DRL-01 — Dispute Resolution Completeness | `Event_CaseOpened`, `Event_CaseResolved` | Defined |
| DRL-02 — Contestation Rate | `Event_CaseOpened` (reopened cases) | Defined |
| CPS-01 — Portable Identity Coverage | `Event_MemberActivated` + VC issuance (Ichi) | Check `kb/02_PRODUCT/` |
| CAS-01–03 — Community Autonomy | Export APIs + `Primitive_Record` | Check `kb/07_OPS/` |
| FID-01 — First-Time Participant | `Event_MemberActivated` + onboarding survey | Deployment-blocked |
| FID-02 — Gender Parity | Consent + membership metadata | Deployment-blocked |
| FID-03 — Diaspora Integration | Wallet geolocation + `Event_ContributionReceived` | Deployment-blocked |

---

## Domain Primitives (what the data model looks like)

| Primitive | File |
|-----------|------|
| Workspace | `knowledge/domain/Primitive_Workspace.md` |
| Member | `knowledge/domain/Primitive_Member.md` |
| Proposal | `knowledge/domain/Primitive_Proposal.md` |
| Treasury | `knowledge/domain/Primitive_Treasury.md` |
| Transaction | `knowledge/domain/Primitive_Transaction.md` |
| Record | `knowledge/domain/Primitive_Record.md` |
| Policy | `knowledge/domain/Primitive_Policy.md` |
| ProofRequirement | `knowledge/domain/Primitive_ProofRequirement.md` |
| Role | `knowledge/domain/Primitive_Role.md` |
| Program | `knowledge/domain/Primitive_Program.md` |

---

## Research Spine connection

The Research Spine architecture (referenced in paper §7.6) will read from:
```
oroma/domain_events (database) → OGI computation → etisiobi/research/icegov/spine/
```

Live computation blocked on: mainnet deployment + ethics clearance.

---

## Invariant

```
If an OGI indicator references an event that doesn't exist in
knowledge/events/ — it is not computable. Update the paper accordingly.
```
