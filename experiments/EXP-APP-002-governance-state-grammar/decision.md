# EXP-APP-002 Decision

Decision: `KEEP_AS_PRODUCT_RESEARCH_BRANCH`

Keep this as the first product-connected application branch.

What it discovered:

The PAGC count-layer grammar can act as a product-research compiler: it turns OGI computability gaps into explicit state transitions, guards, and acceptance tests.

| Transition | Base | Move | Indicator | Product requirement |
|---|---|---|---|---|
| GOV-TRANS-001 | DisputeCase | Created -> Closed | DRL-01 | Block case closure unless evidence fields are populated. |
| GOV-TRANS-002 | TreasuryMovement | Created -> ProvenanceAnchored | TTI-01 | Enforce treasury metadata at service/contract level. |
| GOV-TRANS-003 | TreasuryMovement | EvidenceAttached -> Closed | TTI-02 | Emit domain event on ZK solvency proof generation. |
| GOV-TRANS-004 | IchiCredential | AuthorityChecked -> Exported | CPS-01 | Emit credential.exported event on Ichi credential export. |
| GOV-TRANS-005 | ParticipantOnboarding | Created -> EvidenceAttached | FID-01 | Add one-question onboarding survey and event at wallet creation. |
| GOV-TRANS-006 | DisputeCase | Closed -> Contested | DRL-02 | Emit case.reopened event with reason and actor authority. |
| GOV-TRANS-007 | ParticipantOnboarding | EvidenceAttached -> ReleaseBlocked | FID-02/FID-03 | Route demographic fields through policy/community consent before schema implementation. |

What it does not prove:

- It does not prove Oroma already implements these transitions.
- It does not prove empirical governance improvement.
- It does not prove the Nwagu Aneke source layer encodes governance semantics.

Next best action:

Implement or file tickets for the first five transition guards, then run the OGI extractor to see which indicators become computable.
