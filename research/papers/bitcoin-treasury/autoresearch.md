# AUTORESEARCH SESSION FILE

## Paper Identity

**Paper slug:** bitcoin-treasury
**Working title:** Verifiable Community Treasury Operations on Bitcoin Rails: A Design Framework for Transparent Collective Finance
**Short title:** Bitcoin Community Treasury
**Target venue:** ICEGOV 2026
**Target track:** Track 5 — Digital Governance and Emerging Technologies
**Submission type:** Ongoing Research
**Priority tier:** B
**Current stage:** Evidence Population
**Promotion status:** Scaffolded
**Owner:** Human researcher
**Last updated:** 2026-04-24

---

## 1. Mission

This file is the control plane for this paper.

---

## 2. Working Thesis

### Current thesis
Community financial coordination — from town union levies to ROSCA contributions to diaspora remittances — currently relies on opaque, trust-dependent processes where a treasurer or small committee holds funds with limited verifiability. This creates recurring governance crises: embezzlement allegations, disputed balances, leadership turnover risks. This paper proposes a design framework for verifiable community treasury operations using Bitcoin settlement infrastructure, drawing lessons from DAO governance failures, public financial management transparency tools, and blockchain governance critique to avoid the known failure modes of both centralized and decentralized treasury management.

### One-sentence contribution claim
This paper proposes design principles for community treasury systems that achieve verifiability and accountability without repeating the governance failures documented in DAOs and centralized financial management.

### Why this paper exists
The gap: community financial coordination is a massive governance activity in SE Nigeria and across the Global South, but digital governance literature treats it as either informal/invisible or as a fintech problem rather than a governance problem. No existing framework addresses the specific design requirements of community treasuries where trust is earned through transparency, not assumed through institutional authority.

### What would make this paper worth accepting
A reviewer should value this paper if it: (1) takes DAO/blockchain governance critique seriously instead of being crypto-promotional, (2) identifies specific design requirements for community treasuries distinct from corporate/government finance, and (3) proposes principles grounded in both governance theory and practical failure analysis.

---

## 3. Research Question Stack

### Primary research question
What design principles should govern verifiable community treasury systems built on Bitcoin settlement infrastructure?

### Secondary questions
1. What governance failures from DAOs and centralized financial management must community treasuries avoid?
2. Does blockchain/distributed ledger technology provide materially better tamper resistance than centralized alternatives for community-scale finance?
3. What exclusion risks does blockchain-based finance pose in low-resource, low-literacy settings?
4. How do existing community financial coordination practices (ROSCAs, levies, diaspora remittances) inform design requirements?

### Questions that must be answerable in this paper
- What are the known governance failure modes in DAOs? (Yes — Ferreira 2026, The DAO case)
- Does distributed architecture provide stronger tamper resistance? (Partially — T5-I vs T5-H)
- What are the exclusion risks? (Yes — T5-G)

### Questions that are interesting but out of scope
- Should Bitcoin specifically be used vs. other chains? (technical choice, not governance question)
- How do communities currently manage finances? (empirical; not available)
- Platform operator governance (→ T10)

---

## 4. Track Fit

### Why this track is the best fit
Track 5 focuses on "Digital Governance and Emerging Technologies." Bitcoin/blockchain as emerging technology for governance directly fits. The design framework approach aligns with the track's interest in how emerging tech shapes governance.

### Why neighboring tracks are weaker fits
- Track 10 (Policy): That track is about platform operator governance, not design principles
- Track 7 (DPI): Treasury is one function, not full DPI

### Track-fit risks
- Reviewer may see this as crypto promotion → must lead with governance critique
- "Bitcoin Rails" in title may trigger bias → consider softening to "blockchain settlement infrastructure"

---

## 5. Paper Type Fit

### Why this is Ongoing Research (not full Research)
No pilot data, no empirical evaluation. The paper proposes a design framework informed by existing literature and failure analysis. This is honest — claiming "research" would require evaluation evidence we don't have.

### Overclaim risks
- Cannot claim the framework "works" — only that it addresses known failure modes
- Cannot claim Bitcoin is superior — only that certain properties (settlement finality, censorship resistance) are relevant

---

## 6. Scope

### In scope
- Design principles for community treasury verifiability
- DAO governance failure lessons
- Blockchain vs. centralized ledger tradeoffs for community scale
- Exclusion and accessibility risks
- Community financial coordination practices as design context

### Out of scope
- Specific implementation code or architecture
- Bitcoin price/investment/speculation
- Full platform governance (→ T10)
- Community DPI (→ T7)
- Environmental impact of Bitcoin mining (acknowledge, don't deep-dive)

---

## 7. Source Quotas

### Minimum source targets
- foundational theory sources: 4
- recent digital governance sources: 6
- Nigeria / SE Nigeria sources: 4
- methods / evaluation sources: 3
- counterargument / critique sources: 5
- policy / standards / legal sources: 3

### Current status
- foundational: 2 (Hevner 2004 general DSR; Ostrom 1990 commons)
- recent: 5 (Ferreira 2026, World Bank 2025, Smart Africa 2020, Springer 2025, Trends Research 2025)
- regional: 1 (Smart Africa 2020 mentions Nigeria)
- methods: 0
- critique: 3 (Ferreira 2026, T5-G exclusion, T5-H centralized alternative)
- policy / standards: 1 (Smart Africa 2020)
- total vetted: 9

### Biggest source gaps
- **No community treasury/finance studies from Nigeria** — critical
- No ROSCA governance literature
- No cooperative finance + technology studies
- Missing: CBN regulatory context, cooperative society governance

---

## 8. Core Claims to Defend

### Claim 1
**Claim:** Blockchain-backed infrastructure can improve community treasury transparency
**Current support level:** moderate (technical potential strong; community evidence weak)
**Main supporting sources:** World Bank 2025, Smart Africa 2020, T5-I
**Main contradictions:** Ferreira 2026 (governance challenges persist), T5-G (exclusion)
**Risk level:** high — must specify "can" not "will"

### Claim 2
**Claim:** DAO failures offer lessons for community governance
**Current support level:** moderate
**Main supporting sources:** The DAO case, Ferreira 2026
**Risk level:** medium — DAOs are investor-driven; communities have different logic

### Claim 3
**Claim:** Distributed ledgers provide stronger tamper resistance than centralized
**Current support level:** moderate
**Main supporting sources:** T5-I
**Main contradictions:** T5-H (centralized alternatives adequate)
**Risk level:** medium — must justify why community needs distributed specifically

---

## 9. Evidence Architecture

### Key literature clusters
1. Blockchain governance critique (Ferreira, The DAO)
2. Treasury transparency and PFM (World Bank)
3. Africa blockchain context (Smart Africa, Springer)
4. Centralized vs. decentralized ledgers (LedgerDB vs. distributed)
5. Exclusion and accessibility in blockchain (Trends Research)
6. Community finance practices (ROSCA, cooperative — MISSING)

### Which cluster is strongest
Blockchain governance critique — Ferreira 2026 is excellent.

### Which cluster is weakest
Community finance practices — nearly absent.

---

## 10. Methods Position

### Current methods stance
Design framework construction — not DSR evaluation (that would be T12).

### Methodological weaknesses
No empirical validation. Framework is derived from literature + failure analysis.

---

## 11. Regional Grounding

### Strong local sources found
Smart Africa 2020 mentions Nigeria; Springer 2025 notes Nigeria as "proactive" on blockchain regulation.

### Weak or missing local grounding
No Nigeria-specific community treasury studies, cooperative finance studies, or blockchain deployment cases.

---

## 12. Reviewer Attack Surface

### Likely reviewer objection 1
**Objection:** "This is crypto evangelism dressed up as governance research."
**Defense:** Ferreira 2026, T5-G, The DAO provide critical balance
**Risk level:** high

### Likely reviewer objection 2
**Objection:** "Where is the evidence from actual community treasuries?"
**Defense:** Design science framing — framework, not evaluation
**Risk level:** high

### Likely reviewer objection 3
**Objection:** "Why Bitcoin specifically? A centralized database would be cheaper."
**Defense:** T5-I distributed tamper resistance + community sovereignty argument
**Risk level:** high

### Likely reviewer objection 4
**Objection:** "Where is the privacy protection?"
**Defense:** Need privacy-preserving design literature
**Risk level:** medium

---

## 13. Blinding Risks

### Potential identity leaks
- Platform name, organization, specific community references

### Current blinding status
caution

---

## 14. Search History

### High-value directions that worked
- DAO governance critique → Ferreira 2026
- World Bank blockchain + PFM → practical transparency framework
- Africa blockchain landscape → Smart Africa, Springer

### Directions that underperformed
- "Bitcoin rails" → no academic literature
- "Design science blockchain" → few governance results

---

## 15. Dead Ends and False Starts

### Dead end 1
**Attempted angle:** "Bitcoin rails" as terminology
**Why it failed:** No academic literature uses this term
**Whether to retry:** no — frame as "Bitcoin-aligned infrastructure" or "blockchain settlement"

---

## 16. Current Bottlenecks

### Primary bottleneck
No community treasury/finance empirical studies from Nigeria or Africa.

### Secondary bottlenecks
- No ROSCA governance literature
- No methods anchor for design framework
- Title may trigger anti-crypto reviewer bias

### What would most improve this paper
- Find 3-5 ROSCA / cooperative / community finance studies
- Find Nigeria-specific fintech or cooperative governance sources
- Identify design framework methodology anchor

---

## 17. Kill / Continue / Promote Decision

### Current disposition
continue (conditional)

### Why
Strong critique spine (Ferreira is excellent). The design framework approach is viable as ongoing research. But promotion depends on finding community finance sources.

### What would trigger kill
- Cannot find any community finance governance literature after full search
- The paper becomes indistinguishable from T10 or T7

### What would trigger promotion
- 3+ community finance/ROSCA sources
- Clear differentiation from T10
- Design principles are concrete enough to evaluate

---

## 18. Next Best Actions

1. Search for ROSCA governance studies in Africa/Nigeria
2. Search for cooperative finance + digital technology in Nigeria
3. Find CBN regulatory documents on digital financial services
4. Search for "village savings" or "community savings" + blockchain/digital
5. Consider renaming to avoid "Bitcoin" in title if no Bitcoin-specific governance argument materializes

---

## 20. Session Resume Note

Fresh agent: Stage is Source Acquisition. Biggest gap is zero community finance empirical sources. Do not draft. Priority: ROSCA and cooperative governance literature.
