# Oroma Product Tickets from PAGC Governance Grammar

Source experiment: `experiments/EXP-APP-002-governance-state-grammar/`

| Ticket | Indicator | Requirement | Acceptance test |
|---|---|---|---|
| GOV-TRANS-001 | DRL-01 | Block case closure unless evidence fields are populated. | Attempt to close a dispute without findings/resolution/evidence_refs fails. |
| GOV-TRANS-002 | TTI-01 | Enforce treasury metadata at service/contract level. | Treasury event with short purpose or missing proposalId/blockRef is rejected. |
| GOV-TRANS-003 | TTI-02 | Emit domain event on ZK solvency proof generation. | Verified solvency proof writes a treasury.solvency_proof_generated event with proofHash, verifiedOnChain, balanceThreshold, and txRef. |
| GOV-TRANS-004 | CPS-01 | Emit credential.exported event on Ichi credential export. | Credential export creates event with credentialType, evidenceEventCount, and exportTarget. |
| GOV-TRANS-005 | FID-01 | Add one-question onboarding survey and event at wallet creation. | Wallet creation can submit firstTimeParticipant and writes member.onboarding_survey_submitted. |

Next command:

`python scripts/run_pagc_governance_state_grammar.py`
