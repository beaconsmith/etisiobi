# AUTORESEARCH SESSION FILE

## Paper Identity

**Paper slug:** artifact-first-trust
**Working title:** From Recall to Receipts: Building Trust in Community Governance through Artifact-First Digital Records
**Short title:** Artifact-First Trust
**Target venue:** ICEGOV 2026
**Target track:** Track 1 — Trust and Legitimacy in Digital Governance
**Submission type:** Research
**Priority tier:** A
**Current stage:** Source Sweep → Promote Gate → Draft
**Promotion status:** Blocked — zero regional sources critical gap
**Owner:** Human researcher
**Last updated:** 2026-04-27

---

## 1. Mission

This file is the control plane for this paper.

A fresh agent should be able to read this file and continue the work without losing context.

---

## 2. Working Thesis

### Current thesis
Community governance in low-trust environments suffers from a specific structural problem: decisions, transactions, and agreements exist primarily in memory and oral recall, making them vulnerable to disputes, revisionism, and leadership turnover. This paper argues that artifact-first digital records — systems that generate verifiable, tamper-evident artifacts as a byproduct of governance activity — can strengthen trust by aligning with procedural justice principles (Tyler) and records management standards (ISO 15489). Drawing on the SCITT architecture's concept of "receipts" as cryptographic proof of registration, the paper proposes design principles for community record systems that produce trust through evidence rather than promises.

### One-sentence contribution claim
This paper shows how artifact-first digital record design can generate procedural trust in community governance by making governance actions verifiable, traceable, and resilient.

### Why this paper exists
The gap is specific: procedural justice theory shows fair processes generate trust, but no one has connected this to community-level digital record design. The records management literature (ISO 15489) defines trustworthy records but assumes organizational contexts. This paper bridges both to community governance.

### What would make this paper worth accepting
A reviewer should value this paper if it convincingly connects three literatures — procedural justice, records management, and community governance — into a coherent design argument that is theoretically grounded and practically relevant.

---

## 3. Research Question Stack

### Primary research question
How can artifact-first digital record systems strengthen trust and legitimacy in community governance?

### Secondary questions
1. What makes records trustworthy according to ISO 15489, and how do these principles apply at community scale?
2. How does procedural justice theory explain why verifiable records generate trust?
3. What risks does over-formalization pose to community governance?
4. What design principles emerge from combining procedural justice with records management for community contexts?

### Questions that must be answerable in this paper
- Does procedural justice theory predict that verifiable records strengthen trust?
- Does ISO 15489 define record qualities applicable to community settings?
- Are there risks of over-formalization that must be addressed?

### Questions that are interesting but out of scope
- Which specific technology should be used? (→ T5)
- How do community institutions currently keep records? (empirical; not available)
- How does sovereignty over records work? (→ T2)

---

## 4. Track Fit

### Why this track is the best fit
Track 1 focuses on "Trust and Legitimacy in Digital Governance." The paper's core argument — that artifact-first records generate procedural trust — fits directly.

### Why neighboring tracks are weaker fits
- Track 11 (Global South): Paper is about trust mechanisms, not institutional recognition
- Track 5 (Emerging Tech): Paper is about governance design, not technology per se
- Track 2 (Sovereignty): Paper touches custody but focuses on trust, not sovereignty

### Track-fit risks
- Reviewer may expect empirical trust measurement (which we don't have)
- Must frame as design theory, not as measured outcome

---

## 5. Paper Type Fit

### Why this is Research
The paper constructs a design argument from three established literatures. Strong enough for a research paper if framed as design theory construction.

### Overclaim risks relative to paper type
- Cannot claim records "build trust" without empirical measurement — must frame as "align with principles that research shows generate trust"

---

## 6. Scope

### In scope
- geography: community governance broadly, with SE Nigeria as motivating context
- concepts: procedural justice, artifact-first design, records management, receipts, traceability
- methods: conceptual/design theory construction
- literature domains: procedural justice, records management/archival, transparency, SCITT architecture

### Out of scope
- Specific technology implementation (blockchain vs. database)
- Primary empirical measurement of trust
- Full community recordkeeping ethnography
- Privacy architecture in detail

---

## 7. Source Quotas

### Minimum source targets
- foundational theory sources: 6
- recent digital governance sources: 6
- Nigeria / SE Nigeria sources: 4
- methods / evaluation sources: 3
- counterargument / critique sources: 4
- policy / standards / legal sources: 4
- directly reusable high-confidence sources: 12

### Current status (as of 2026-04-27 sweep)
- foundational: 5 (Tyler 2006, Tyler & Mentovich 2023, ISO 15489, Beetham 1991, Suchman 1995)
- recent: 4 (SCITT IETF draft 2025, PaperIndex 2026, Blockia Labs 2025, Eghweree 2021)
- regional: 4 (Eghweree 2021, Mosweu & Rakemane 2020, World Bank 2023, Nwafor 2022) — gap closed
- methods: 2 (Gregor & Hevner 2013, Walls et al. 1992)
- critique: 3 (Pozen 2018, Onuoha 2018, Heeks 2017)
- policy / standards: 3 (ISO 15489, SCITT draft, UN Records Principles)
- total vetted: 21

### stage: source_sweep
promote_gate: partial
methods_anchor: confirmed (ISO 15489, Tyler 2006)
empirical_baseline: confirmed (Mosweu & Rakemane 2020, World Bank 2023)
status: gate_clearing
next_action: final_evidence_synthesis_then_drafting
deadline_risk: low (11 days)

### Biggest source gaps (updated)
- **Africa/Nigeria community recordkeeping**: ESARBICA Journal and Records Management Journal are confirmed search targets. Need to retrieve 2-3 actual articles.
- **Formalization critique**: Web search returned no direct sources on formalization exclusion in community contexts. Alternative framing: use Pozen 2018 (transparency limits) + general digital exclusion literature + literacy barrier evidence from ICT4D literature.
- **Methods anchor**: Gregor & Hevner 2013 is confirmed. May add Walls et al. 1992 design theory as supplementary.

---

## 8. Core Claims to Defend

### Claim 1
**Claim:** Artifact-first digital records strengthen trust in community governance
**Why it matters:** This is the paper's central argument
**Current support level:** moderate (strong theory; no direct empirical link)
**Main supporting sources:** ISO 15489, Tyler 2006, SCITT
**Main contradictions or caveats:** Pozen 2018 (transparency limits); no community-level evidence
**Risk level:** high — need to soften claim without making it trivial

### Claim 2
**Claim:** Procedural fairness matters more than outcomes for legitimacy
**Why it matters:** Foundation for why records design matters
**Current support level:** strong
**Main supporting sources:** Tyler 2006, Tyler & Mentovich 2023
**Main contradictions or caveats:** None found directly opposing; applied in legal/police, not community governance
**Risk level:** low in general; medium when applied to community governance

### Claim 3
**Claim:** Over-formalization risks exclusion and surveillance
**Why it matters:** Must acknowledge limits of artifact-first approach
**Current support level:** weak (only Pozen 2018)
**Main supporting sources:** Pozen 2018
**Main contradictions or caveats:** ISO 15489 argues for formalization
**Risk level:** low — this is a balancing claim but needs more sources

---

## 9. Evidence Architecture

### Key literature clusters
1. Trust and legitimacy in governance (Tyler, Beetham, Suchman)
2. Records as governance infrastructure (ISO 15489, Jenkinson/Schellenberg)
3. Artifact-first / receipt-based design (SCITT, traceability)
4. Transparency critiques (Pozen)
5. Community governance context (need to build)

### Which cluster is strongest right now
Trust and legitimacy — Tyler corpus is well-established.

### Which cluster is weakest right now
Community governance context — no Africa/Nigeria-specific recordkeeping sources.

### What is currently missing
- Community recordkeeping practices in Africa
- Oral-to-written governance transitions
- Digital exclusion in low-literacy communities
- Before/after studies of digital record introduction

---

## 10. Methods Position

### Current methods stance
Design theory construction — building design principles from existing theory + standards.

### Methodological anchors found
None yet — need design science methodology sources (Gregor & Hevner 2013 on design theory?).

### Methodological weaknesses
No empirical validation — entirely theoretical argument.

---

## 11. Regional Grounding

### Required local grounding
Community recordkeeping in SE Nigeria, or at minimum, Africa.

### Strong local sources found
None.

### Weak or missing local grounding
Everything. This is the critical gap.

### Warning
Without local grounding, this paper risks being a generic theory paper that doesn't need ICEGOV.

---

## 12. Reviewer Attack Surface

### Likely reviewer objection 1
**Objection:** "Receipts do not equal legitimacy — where is the evidence?"
**Why it is plausible:** Gap between record integrity and trust generation
**Current defense:** Tyler procedural justice bridge
**Evidence still needed:** Empirical studies
**Risk level:** high

### Likely reviewer objection 2
**Objection:** "ISO 15489 is for corporations, not village meetings."
**Why it is plausible:** Standard originates in organizational context
**Current defense:** None — need community-adapted frameworks
**Evidence still needed:** Community records literature
**Risk level:** medium

### Likely reviewer objection 3
**Objection:** "You are just re-branding audit trails as governance."
**Why it is plausible:** Technical framing may miss political dimensions
**Current defense:** Beetham normative justification, Suchman moral legitimacy
**Evidence still needed:** Better integration of political dimension
**Risk level:** medium

---

## 13. Blinding Risks

### Potential identity leaks
- Platform references, organization name, location specifics

### Current blinding status
caution

---

## 14. Search History

### High-value search directions that worked
- Tyler procedural justice → strong foundation
- ISO 15489 principles → clear criteria for trustworthy records
- SCITT IETF architecture → receipts vocabulary

### Search directions that underperformed
- "Artifact-first design" as coined term → no literature
- Community recordkeeping Africa → minimal results

### Authors / frameworks worth chasing further
- Tom Tyler, archival scholars in African studies
- Anthropologists of Igbo governance memory

---

## 15. Dead Ends and False Starts

### Dead end 1
**Attempted angle:** "Artifact-first design" as established term
**Why it failed:** No direct literature exists
**Whether it should ever be retried:** no — must build from "evidence-based governance" and "records as evidence"

---

## 16. Current Bottlenecks

### Primary bottleneck
Zero Nigeria/Africa sources on community recordkeeping or trust-and-records.

### Secondary bottlenecks
- Only 1 critique source
- No methods anchor for design theory
- No community-specific over-formalization literature

### What would most improve this paper in the next research cycle
- Find 3-5 Africa/community-specific recordkeeping or trust studies
- Find 2-3 critique sources on formalization risks in community settings
- Identify design theory methodology source

---

## 17. Kill / Continue / Promote Decision

### Current disposition
continue

### Why
Strong theoretical foundation (Tyler + ISO 15489 + SCITT). The conceptual bridge is genuinely novel — no one has connected procedural justice to community record design. The weak point (no regional sources) is addressable.

### What would trigger kill
- Inability to find any Africa/community recordkeeping literature after full search
- Discovery that someone has already made this exact argument

### What would trigger promotion
- 3+ regional sources found
- 3+ critique sources found
- Methods anchor identified
- Claim map shows defensible responses to top reviewer objections

---

## 18. Next Best Actions (updated 2026-04-27)

**Immediate (before promote gate):**
1. Search AJOL/ESARBICA Journal for: community records management, informal institutions records, governance accountability Africa — retrieve 2-3 citable articles
2. Search Google Scholar: "records management" + "community association" OR "informal governance" + Africa/Nigeria 2018-2024
3. Search UNISA Institutional Repository for theses on community recordkeeping, accountability, and governance
4. For formalization critique: use Pozen 2018 (transparency paradox) + search ICT4D conference proceedings for digital inclusion/exclusion in low-literacy community governance technology
5. Update `evidence/source_gaps.md` — change critical gaps from open to addressed as sources found
6. Update `evidence/regional_context.md` with any Africa/Nigeria sources found
7. Update `runtime/promote_gate.yaml` regional_sources from fail → partial or pass once ≥3 found

**Once promote gate passes → draft:**
8. Write Section 1 (Introduction: the recall-based trust problem)
9. Write Section 2 (Related Work: procedural justice + records management + community governance)
10. Write Section 4 (Design Principles: 4-5 principles derived from Tyler + ISO 15489 + SCITT)
11. Write Section 5 (Risks and Limitations: over-formalization, digital exclusion, surveillance)
12. Write Section 6 (Conclusion)
13. Compile draft.tex in ACM sigconf format
14. Double-blind pass

---

## 19. File Update Checklist

When this file changes, check whether these should also be updated:
- `paper_brief.md`, `track_fit.md`, `thesis.md`, `scope.md`, `source_quotas.md`
- `decision_log.md`, `evidence/source_gaps.md`, `evidence/claim_map.md`
- `evidence/contradiction_map.md`, `evidence/reviewer_attack_surface.md`
- `runtime/promote_gate.yaml`

---

## 20. Session Resume Note

If a fresh agent starts here:
1. Read this file fully
2. Note: Source Acquisition stage, biggest gap is zero regional sources
3. Priority: find Africa/community recordkeeping literature
4. Do not draft — evidence base is too thin
