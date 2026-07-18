# AUTORESEARCH SESSION FILE

## Paper Identity

**Paper slug:** community-os-pilot
**Working title:** Architecture and Design Rationale of a Community Coordination Operating System for Verifiable Local Governance
**Short title:** Community Coordination OS
**Target venue:** ICEGOV 2026
**Target track:** Track 12 — Experiments, Pilots, Prototypes and Case Studies
**Submission type:** Ongoing Research (4–6 pages)
**Priority tier:** B
**Current stage:** Reframe → Draft
**Promotion status:** Ready to draft — pending honest scope agreement
**Owner:** Human researcher
**Last updated:** 2026-04-27

---

## IMPORTANT REFRAME NOTE (2026-04-27)

This paper was previously framed as a "pilot study." That framing is rejected. There are no real users, no pilot deployment, and no user data. The paper is now reframed as:

> **A design science artifact paper describing the architecture, key design decisions, and evaluation plan of a community coordination operating system (Oroma) for verifiable local governance.**

This is honest. Track 12 accepts experiments, pilots, prototypes, and case studies. A prototype with documented architecture and design rationale is a legitimate Track 12 submission.

Do not: claim pilot results, user adoption data, or real-world impact. Those do not exist.
Do: document design decisions, architectural rationale, and an honest evaluation plan.

---

## 1. Mission

This paper contributes design knowledge from building Oroma — a community coordination OS. It documents:
- The problem the artifact addresses (governance coordination in low-trust informal communities)
- Key architectural design decisions and the rationale behind them
- What has been implemented and what remains
- An honest DSR-framed evaluation plan

---

## 2. Working Thesis

### Current thesis
Community governance in informal institutions — particularly in Southeast Nigeria — suffers from coordination failures caused by opaque decision-making, unverifiable financial actions, and the absence of tamper-evident records. This paper reports on the design and partial implementation of Oroma: a community coordination operating system that produces verifiable records as a byproduct of governance actions. Following Hevner's DSR framework, we describe (a) the problem environment, (b) key design principles, (c) implemented artifact components, and (d) an evaluation plan grounded in DSR validity criteria rather than premature impact claims.

### One-sentence contribution claim
This paper contributes a design theory for community coordination operating systems that produce verifiable governance records, evaluated through implementation logic and DSR validity criteria.

### Why this paper exists
Track 12 explicitly asks for experiments, pilots, and prototypes. Oroma is a real artifact with implemented backend services, smart contracts, and a frontend. Its design decisions (artifact-first records, hash-chained domain events, credential issuance, proposal-linked transactions) are documentable as design knowledge. The methodological contribution is applying DSR rigorously to community-layer governance technology in the Global South context.

---

## 3. Research Question Stack

### Primary research question
What design principles and architectural decisions should govern a community coordination OS that produces verifiable governance records?

### Secondary questions
1. What are the design requirements for verifiable records in community governance?
2. Which DSR evaluation methods are appropriate at pre-deployment maturity?
3. What implementation constraints shaped the artifact's design?

---

## 4. Oroma Artifact Evidence (from OROMA_BACKEND_ASSESSMENT.md, 2026-04-27)

### What Oroma has actually built

| Component | Implementation Status | Evidence |
|-----------|----------------------|----------|
| Workspace (community) creation | Implemented — WorkspaceRegistry.sol factory + DB | `contracts/WorkspaceRegistry.sol`, `packages/db/src/schema/workspaces.ts` |
| Role-based membership (soulbound NFT) | Implemented | `contracts/MembershipNFT.sol`, `packages/db/src/schema/members.ts` |
| Proposal/governance engine | Implemented (partial) | `contracts/ProposalEngine.sol`, `packages/services/src/proposal/` |
| Treasury (multi-sig) | Implemented (partial) | `contracts/Treasury.sol`, `packages/db/src/schema/transactions.ts` |
| Hash-chained domain event log | Implemented — SHA-256 event chain, genesis/non-genesis | `packages/services/src/core/event-writer.ts`, `packages/db/src/schema/domain_events.ts` |
| Tamper-evident records with provenance | Implemented | `packages/services/src/record/record-service.ts`, `packages/db/src/schema/records.ts` |
| First-class receipts | Implemented | `packages/db/src/schema/receipts.ts`, `packages/services/src/transaction/receipt-service.ts` |
| Credential issuance (Ichi) | Partially implemented | `packages/services/src/member/credential-service.ts`, `packages/db/src/schema/credentials.ts` |
| ICEGOV research indicators (DRL-01, CPS-01, TTI-01, FID-01) | Backend calculation implemented | `packages/services/src/indicator/indicator-service.ts`, `packages/db/src/schema/research_indicators.ts` |
| Dispute/case closure with authority | Implemented | `packages/services/src/case/case-service.ts` |
| Wallet challenge/signature binding | Implemented | `apps/agents-api/src/lib/wallet-auth.ts` |
| Smart contract tests (30+) | Passing | `test/WorkspaceRegistry.test.js`, `MembershipNFT.test.js`, `ProposalEngine.test.js`, etc. |

### Key design decisions to document in the paper

1. **Artifact-first records**: Every governance action produces a tamper-evident record. This aligns with ISO 15489's "duty to document" and Tyler's procedural justice — governance actions are verifiable.
2. **Hash-chained domain event log**: Domain events use SHA-256 hash chaining (previousHash / eventHash). This provides service-level tamper evidence without requiring blockchain for every event.
3. **Proposal-linked transactions**: Governed money actions (payouts, transfers, settlements) require an approved proposal. Treasury cannot disburse without prior authorization.
4. **First-class receipts**: Transaction settlement requires an issued receipt. Receipts link to confirmed contract events for chain-backed transparency.
5. **Soulbound membership NFT**: Membership is non-transferable. Role authority (admin, treasurer, member, observer) is derived from on-chain NFT state, not client claims.
6. **Backend-calculated ICEGOV indicators**: DRL-01, CPS-01, TTI-01, FID-01 are calculated server-side from database records, not from client-submitted values. Indicator service rejects caller-supplied scores.
7. **DB-primary, chain-legible architecture**: Canonical state lives in the database (for performance), while blockchain events provide settlement finality and tamper evidence for high-stakes actions.

### Honest maturity assessment
- Institutional-readiness score: **3/5** (service/API enforced; not yet DB/contract/indexer-hard)
- Direct DB mutation by privileged SQL is not yet prevented
- Indexer-to-contract-events pipeline not yet production-proven
- No real users; no pilot deployment

---

## 5. Track Fit

### Why this track is the best fit
Track 12 — Experiments, Pilots, Prototypes and Case Studies. Oroma is a real prototype with implemented components and documented design rationale. The contribution is design knowledge, not impact measurement.

### Track-fit risks
- Reviewer may expect user evaluation data
- Must explicitly frame as pre-deployment prototype with honest evaluation plan
- Must not overclaim: say "design validity" not "organizational impact"

---

## 6. Paper Type Fit

**Ongoing Research (4–6 pages)** — appropriate because:
- Real artifact exists with documented design decisions
- No deployment/user data available
- Evaluation plan is forward-looking and honest
- 4–6 pages matches scope and available evidence

---

## 7. Proposed Paper Structure (6 pages)

1. **Introduction** (0.5p): Community governance coordination problem in low-trust informal institutions. SE Nigeria context. Contribution claim.
2. **Related Work** (1p): DSR methodology (Hevner, Peffers). Community governance IT artifacts. Evaluation challenges in early-stage DSR (De Sordi 2020).
3. **Problem Environment and Requirements** (0.5p): What coordination failures community governance faces. Design requirements derived from problem analysis.
4. **Artifact Description** (2p): Architecture overview. Key design decisions with rationale (artifact-first records, hash-chained log, proposal-linked transactions, backend-calculated indicators). Honest maturity assessment.
5. **Evaluation Design** (1p): DSR evaluation criteria applied. What has been evaluated (design logic, implementation validity, expert review). What remains (deployment, user study). Claim boundary analysis.
6. **Conclusion and Future Work** (0.5p): Design knowledge contribution. Next steps.

---

## 8. Source Quotas

### Minimum source targets (for 4–6 page ongoing research)
- DSR methodology: 5 (Hevner 2004, Peffers 2008, Sein 2011, De Sordi 2020, artifact validity 2025)
- Community governance context: 2 (T11 sources — town union evidence, Ostrom polycentricity)
- Records/trust theory: 2 (Tyler 2006, ISO 15489 — shared with T1)
- Critique/limitation: 2 (De Sordi artificial evaluations, blockchain critique)
- Total target: ~12

### Current status
- DSR: 5 (Hevner 2004, Peffers 2008, Sein 2011, De Sordi 2020, ECIS generalization 2024)
- Community governance: 2 (can borrow from T11: Ostrom 1990, Eme & Onyishi 2011)
- Records/trust: 2 (Tyler 2006, ISO 15489 — shared with T1)
- Critique: 2 (De Sordi, ECIS)
- Total: ~10 (adequate for 4–6 page paper)

### Biggest source gaps
- **Africa civic tech evaluation studies** — no direct sources found; not fatal for 4-6 page format; acknowledge as limitation
- Regional Nigeria context — can borrow from T11 for problem framing

---

## 9. Blinding Risks

### Potential identity leaks
- Platform name "Oroma" — replace with "the prototype" or "a community coordination OS"
- Organization name "Beaconsmith Collective" — strip completely
- Location specifics — generalize to "Southeast Nigeria"
- GitHub URLs — remove or anonymize
- Specific community names — generalize

### Current blinding status
Must scrub before submission. All Oroma-specific names must be replaced.

---

## 10. Kill / Continue / Promote Decision

### Current disposition
continue — ready to draft

### Why
Oroma has real implemented components. The design decisions (hash-chained events, proposal-linked transactions, artifact-first records, backend-calculated indicators) are concrete and documentable. Track 12 is explicitly for prototypes. The paper can be written honestly.

### What would trigger kill
- User decides not to describe Oroma's implementation in an academic paper at all
- Cannot achieve double-blind anonymization while describing the system credibly

---

## 11. Next Best Actions

1. Write the paper directly — structure is clear, artifact is documented
2. Section 1: Write community governance coordination problem + SE Nigeria context + contribution claim
3. Section 4: Draft the artifact description — 7 key design decisions from OROMA_BACKEND_ASSESSMENT.md
4. Section 5: Write evaluation design — DSR validity criteria applied honestly
5. Compile into `writing/draft.tex` (ACM sigconf, ongoing research format)
6. Double-blind pass: replace all Oroma references with neutral terms

---

## 12. Session Resume Note

Fresh agent:
- This is a prototype design paper, NOT a pilot study
- Oroma implementation evidence is in `c:/Users/USER/code/oroma/OROMA_BACKEND_ASSESSMENT.md`
- Key design decisions are documented in the artifact evidence table above (Section 4)
- Do NOT claim user data or deployment results
- Write honestly: "pre-deployment prototype with implementation-logic evaluation"


---

## 1. Mission

This file is the control plane for this paper.

---

## 2. Working Thesis

### Current thesis
Design science research (DSR) in information systems demands rigorous artifact evaluation, yet studies show that 86% of DSR evaluations are artificial and unrealistic (De Sordi et al. 2020). This paper reports early evidence from the design and partial deployment of a community governance platform — a "community operating system" — that produces verifiable records of governance actions. Following Hevner's DSR framework and Peffers' process model, the paper reports on artifact design decisions, early feasibility indicators, and implementation constraints, explicitly scoping claims to design validity and initial utility rather than organizational impact.

### One-sentence contribution claim
This paper contributes a design theory for community-layer governance systems, evaluated through early-stage feasibility and design logic analysis, with honest scoping of what can and cannot be claimed from pre-deployment evidence.

### Why this paper exists
Track 12 wants experiments, pilots, prototypes. If the platform has any deployable evidence, this is where it belongs. The paper's contribution is methodological honesty: being explicit about what early evidence can claim.

### What would make this paper worth accepting
A reviewer should value this paper if it: (1) follows DSR conventions rigorously, (2) is honest about the maturity of evidence, (3) contributes design knowledge (not just an engineering report), and (4) addresses known DSR evaluation weaknesses explicitly.

---

## 3. Research Question Stack

### Primary research question
What design principles and early evidence emerge from building a community governance platform for verifiable local coordination?

### Secondary questions
1. What artifact evaluation methods are appropriate at pre-deployment maturity?
2. What design decisions were shaped by community governance requirements?
3. What can and cannot be claimed from early-stage evidence?

---

## 4. Track Fit

### Why this track is the best fit
Track 12 explicitly asks for "Experiments, Pilots, Prototypes and Case Studies." This is literally that.

### Track-fit risks
- Reviewer may expect deployed pilot with user data (which may not exist)
- Must frame honestly as "early evidence" not "pilot results"

---

## 5. Paper Type Fit

### Why this is Ongoing Research
No deployment data yet. Design decisions + feasibility analysis = ongoing research, not full research paper.

---

## 6. Scope

### In scope
- DSR methodology for community governance technology
- Artifact design decisions and rationale
- Early feasibility indicators
- Claim boundary analysis (what can be said vs. what requires further study)

### Out of scope
- Full user evaluation
- Impact measurement
- Community adoption studies
- Comparative analysis with other platforms

---

## 7. Source Quotas

### Minimum source targets
- foundational DSR sources: 5
- recent evaluation sources: 4
- Nigeria / SE Nigeria sources: 2 (at minimum)
- methods / evaluation sources: 5 (this is the methods paper)
- counterargument / critique sources: 3
- policy / standards / legal sources: 1

### Current status
- foundational DSR: 4 (Hevner 2004, Peffers 2008, Sein 2011 ADR, De Sordi 2020)
- recent: 3 (Artifact validity 2025, ECIS generalization 2024, Hevner keynote 2015)
- regional: 0
- methods: 5 (strong — DSR spine is solid)
- critique: 1 (De Sordi: 86% evaluations artificial)
- policy: 0
- total vetted: 7

### Biggest source gaps
- Zero Nigeria sources
- No civic tech pilot evaluation studies from Africa
- No community technology acceptance studies

---

## 8. Core Claims to Defend

### Claim 1
**Claim:** Early evidence can be rigorous without claiming final impact
**Current support level:** moderate (methodological argument strong)
**Risk level:** low if framed carefully

### Claim 2
**Claim:** Design science is appropriate for community governance technology
**Current support level:** strong
**Risk level:** low

### Claim 3
**Claim:** Most DSR evaluations are artificial and weak
**Current support level:** moderate (De Sordi single study)
**Risk level:** low — this motivates methodological care

---

## 9. Evidence Architecture

### Which cluster is strongest
DSR methodology — Hevner, Peffers, Sein are well-covered.

### Which cluster is weakest
Civic tech evaluation in Africa — no sources found.

---

## 10. Methods Position

### Current methods stance
DSR (Hevner 2004 / Peffers 2008) with potential ADR (Sein 2011) if organizational intervention occurs.

### Methodological anchors found
Strong: Hevner, Peffers, De Sordi, artifact validity paper.

---

## 11. Regional Grounding

### Strong local sources found
None.

### Weak or missing local grounding
No civic tech evaluations from Nigeria or SE Nigeria. No HCI/ICT4D studies in Igbo communities.

---

## 12. Reviewer Attack Surface

### Likely reviewer objection 1
**Objection:** "This is just a prototype — where is the impact evidence?"
**Defense:** DSR doesn't require mature impact data at early stage
**Risk level:** medium

### Likely reviewer objection 2
**Objection:** "Your evaluation is too small/short to mean anything."
**Defense:** Explicit claim scoping + generalization limits (ECIS 2024)
**Risk level:** medium

### Likely reviewer objection 3
**Objection:** "Why is this a paper and not an engineering report?"
**Defense:** Design theory contribution (Hevner)
**Risk level:** medium

---

## 16. Current Bottlenecks

### Primary bottleneck
**Depends on actual platform state.** If platform has no deployable evidence, this paper may need to be delayed or reframed as pure design theory.

### Secondary bottlenecks
- No regional sources
- Need actual artifact to describe

---

## 17. Kill / Continue / Promote Decision

### Current disposition
continue (conditional on pilot data materializing)

### Why
DSR methodology spine is solid. Track 12 is a natural fit. But the paper depends on having something to evaluate.

### What would trigger kill
- No deployable artifact or evidence before deadline
- Paper becomes pure speculation about a system that doesn't exist

### What would trigger promotion
- Platform has concrete design decisions to document
- Some early feasibility data exists
- DSR framing is honestly scoped

---

## 18. Next Best Actions

1. Assess current platform state — what artifact evidence exists?
2. Search for civic tech pilot evaluations in Africa
3. Search for ICT4D conference proceedings on prototype evaluation
4. Determine paper type: ongoing research (4-6 pages) or short paper (2-4 pages)
5. If no artifact exists, consider killing or delaying

---

## 20. Session Resume Note

Fresh agent: This paper depends on actual platform state. DSR methodology is strong. Check whether deployable evidence exists before investing more research time.
