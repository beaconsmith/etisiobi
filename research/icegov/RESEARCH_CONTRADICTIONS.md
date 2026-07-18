# OGI Contradiction Tracker

> Active contradictions, tensions, and open design questions.
> Resolved contradictions move to the bottom. Never deleted.
> Feed this into each autoresearch session.

---

## CURRENT TRACKER

### CONT-001 — RESOLVED (v6-iter1)
**Was:** WIKI listed Buterin (2021/2020) as legitimacy theory sources.
**Correct:** Beetham (1991), Tyler (2006), Suchman (1995).
**Resolution:** Fixed in WIKI.md.

---

### CONT-002 — OPEN
**Tension:** DPR-01 participation weighting (stake-in-outcome = ≥1 treasury contribution)
may exclude legitimately active members: new joiners in first 90-day window, diaspora
members who contribute annually not monthly, members contributing in-kind.
**Risk:** Framework inadvertently measures financial participation, not governance participation.
**Proposed mitigation:** Add a grace-period clause: new members (≤30 days) are counted
without the treasury requirement for their first measurement window.
**Status:** Open — needs Delphi validation in Stage 5.

---

### CONT-003 — OPEN
**Tension:** TTI-01 "≥50 char purpose metadata" is enforced at the platform contract level.
This means TTI-01 measures platform compliance (does the contract enforce the rule?),
not governance intent (did the community actually document its reasons?).
A platform that enforces the rule but allows copy-pasted boilerplate achieves TTI-01 = 100%
with no genuine accountability improvement.
**Risk:** Indicator conflates platform design quality with community governance quality.
**Proposed mitigation (already integrated in the canonical submission draft):** Require proposalId reference in purpose field —
links metadata to a specific governance decision. But this is still platform-enforced,
not semantically validated.
**Status:** Open — mitigation reduces risk but does not eliminate it. Flag in journal version.

---

### CONT-004 — OPEN
**Tension:** CPS-01 "≥3 on-chain governance events" threshold for credential issuance
has no empirical grounding. Why 3? Not 2, not 5?
**Risk:** Arbitrary threshold makes CPS-01 platform-specific and non-transferable.
**Proposed resolution:** Tie to Ostrom Principle 1 (clearly defined membership):
minimum evidence of governance participation across at least one full governance cycle
(proposal + vote + outcome). 3 events is a plausible minimum for a full cycle.
**Status:** Open — add to journal Delphi validation targets.

---

### CONT-005 — OPEN
**Tension:** FID-02 (Gender Parity Index) requires "community consent and ethics clearance."
But FID-01 uses an onboarding survey without separate consent beyond platform ToS.
Are these ethically consistent? FID-01 asks about prior financial history — potentially
sensitive in contexts where financial history carries social stigma.
**Risk:** Inconsistent ethics treatment across FID sub-indicators.
**Proposed resolution:** Extend ethics clearance requirement to FID-01 survey question
in any deployment context where financial history is socially sensitive.
**Status:** Open — governance policy decision, not framework design decision.

---

### CONT-006 — RESOLVED (canonical submission draft)
**Tension:** CAS-03 (State Dependency Ratio) measures governance decisions "requiring
formal government approval." But in Southeast Nigeria, many community decisions are
technically illegal under formal law (e.g. informal dispute resolution that substitutes
for courts). A community with low CAS-03 score may be non-compliant with formal law,
not genuinely autonomous.
**Risk:** Framework could inadvertently reward legal non-compliance as "autonomy."
**Proposed resolution:** CAS-03 should measure *chosen* state dependency (decisions
the community routes through government because it prefers to) vs *imposed* dependency
(decisions legally required to go through government). Requires legal context mapping
per deployment jurisdiction.
**Status:** Resolved for the canonical submission draft. CAS-03 is now defined as **imposed**
state dependency only, explicitly excluding chosen state engagement. Journal version still
needs jurisdiction-specific legal mapping guidance.

---

### CONT-007 — RESOLVED (canonical submission draft)
**Tension:** The core claim is that verifiable records are a necessary condition for
governance accountability. But Ostrom's most durable CPR institutions (Swiss alpine
meadows, Japanese irrigation systems, Maine lobster fisheries) operated for centuries
without any digital records and with minimal written records at all.
**Risk:** The framework may be measuring a *sufficient* path to accountability in digital
contexts, not a *necessary* condition universally.
**Proposed resolution:** Scope the claim explicitly: "verifiable records are a necessary
condition for accountability in *digital-native* community governance contexts where
members are geographically dispersed and cannot rely on social witnessing alone."
This is already partially true of the paper's framing (diaspora cooperatives, WhatsApp
governance failures) but not stated as an explicit scope condition.
**Status:** Resolved for the canonical submission draft. The paper now scopes the claim to
digitally mediated, geographically dispersed community governance contexts where shared
social witnessing is insufficient.

---

## RESOLVED

- CONT-001: WIKI Buterin error → corrected to Beetham/Tyler/Suchman (v6-iter1)
- CONT-006: CAS-03 reframed as imposed vs chosen state dependency in canonical submission draft
- CONT-007: Necessary-condition claim narrowed in canonical submission draft
