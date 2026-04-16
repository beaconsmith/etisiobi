---
id: CONT-003
program: icegov
indicator: CPS-01
type: missing_instrumentation
severity: major
status: open
opened: 2026-04-16
---

# CONT-003: credential.exported event missing from domain_events

**Description:** CPS-01 (Portable Identity Coverage) requires tracking when members export their Ichi credentials as W3C Verifiable Credentials to platform-independent storage. No `credential.exported` event exists in `domain_events`. Currently, credential issuance is tracked but export (the portability step) is not.

**Unblock condition:** When a member exports a credential, emit `credential.exported` domain event with `payload: { credentialType, evidenceEventCount, exportTarget: 'ipfs' | 'local' | 'wallet' }`.

**Product backlog item:** "Track credential export events in domain_events" — wire into Ichi module export flow.

**Paper impact:** CPS-01 remains `blocked`. Paper v3 should frame credential portability as a design principle with pending instrumentation.

**Resolution:** ~
