---
id: CONT-004
program: icegov
indicator: FID-01
type: missing_instrumentation
severity: major
status: open
opened: 2026-04-16
---

# CONT-004: Onboarding survey not collected at wallet creation

**Description:** FID-01 (First-Time Formal Participant Rate) requires a single survey question at wallet creation: "Has your savings group or community fund ever used a tool other than WhatsApp, cash, or mobile money transfers to make and record decisions?" No onboarding survey is collected. No `member.onboarding_survey_submitted` event exists.

**Unblock condition:** Add single-question survey at wallet creation (via Privy onboarding flow). Write `member.onboarding_survey_submitted` event with `payload: { firstTimeParticipant: boolean }`.

**Product backlog item:** "Add onboarding survey at wallet creation" — one question, one domain event.

**Paper impact:** FID-01 remains `blocked`. Paper v3 must note this is pending product instrumentation.

**Resolution:** ~
