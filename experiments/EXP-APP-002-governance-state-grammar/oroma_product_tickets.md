# Oroma Product Tickets from PAGC Governance Grammar

These are the first implementation tickets implied by EXP-APP-002. They are research-derived product requirements, not proof that the product already satisfies them.

| Ticket | Indicator | Requirement | Acceptance test |
|---|---|---|---|
| GOV-TRANS-001 | DRL-01 | Block case closure unless evidence fields are populated. | Attempt to close a dispute without findings/resolution/evidence_refs fails. |
| GOV-TRANS-002 | TTI-01 | Enforce treasury metadata at service/contract level. | Treasury event with short purpose or missing proposalId/blockRef is rejected. |
| GOV-TRANS-003 | TTI-02 | Emit domain event on ZK solvency proof generation. | Verified solvency proof writes a treasury.solvency_proof_generated event with proofHash, verifiedOnChain, balanceThreshold, and txRef. |
| GOV-TRANS-004 | CPS-01 | Emit credential.exported event on Ichi credential export. | Credential export creates event with credentialType, evidenceEventCount, and exportTarget. |
| GOV-TRANS-005 | FID-01 | Add one-question onboarding survey and event at wallet creation. | Wallet creation can submit firstTimeParticipant and writes member.onboarding_survey_submitted. |

## Priority

1. `GOV-TRANS-001` because DRL-01 is closest to a concrete state-machine closure invariant.
2. `GOV-TRANS-002` because TTI-01 is structurally computable once metadata is enforced.
3. `GOV-TRANS-004` because CPS-01 requires a clear export event.
4. `GOV-TRANS-005` because FID-01 needs one consented onboarding event.
5. `GOV-TRANS-003` because TTI-02 depends on a heavier ZK solvency-proof workflow.
