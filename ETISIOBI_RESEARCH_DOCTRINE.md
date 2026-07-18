# Etisiobi Research Doctrine

> Version: 1.0
> Date: 2026-05-03
> Derived from: `BEACONSMITH_PRODUCT_DOCTRINE.md`

---

## What Etisiobi Is

Etisiobi is the **research and intelligence engine** for Beaconsmith.

It researches:
- Cultural governance (how Nigerian communities actually govern themselves)
- Institutions (hometown associations, faith welfare funds, cooperatives, market unions)
- Markets (diaspora finance, informal savings, regulatory landscape)
- Social coordination (trust, dispute resolution, authority, legitimacy)

It produces:
- **Institution Template Research Packs** — reusable templates for Oroma
- **Indicator frameworks** — measurable governance quality signals
- **Product feedback** — evidence-backed recommendations for Oroma engineering
- **Strategic insight** — market maps, competitor analysis, policy briefs for BeaconOS

---

## Research Modes

### Mode A: Applied Governance (ICEGOV / OGI)
- **Goal:** Produce rigorous, evidence-based governance frameworks for Nigerian community institutions.
- **Output:** Academic papers, indicator catalogs, policy bridges, institution templates.
- **Standard:** Submission-grade. Source-first. Falsifiable.
- **Current status:** Track 6 submitted. 3-track portfolio active (T11, T1, T12).

### Mode B: Foundational / Cultural Intelligence (PAGC)
- **Goal:** Investigate whether indigenous knowledge systems encode generative principles.
- **Output:** Concept papers, primary source archives, experimental results.
- **Standard:** Source-first. Hypothesis must survive falsification.
- **Current status:** Hard reset. Core claim (k=27) refuted. Under re-evaluation.

### Rule: Applied mode takes priority.
PAGC does not block ICEGOV. If PAGC cannot produce falsifiable results, it stays in the archive.

---

## Source-First Discipline

Every claim must trace to a source.

### Source hierarchy
1. **Primary:** Interviews, field observations, original documents, artifacts
2. **Secondary:** Academic papers, government reports, NGO studies
3. **Tertiary:** News articles, blog posts, social media

### Claim strength
- **Proven:** Multiple independent primary sources agree.
- **Supported:** One primary source or multiple secondary sources.
- **Hypothesis:** Pre-registered, awaiting test.
- **Refuted:** Evidence contradicts claim. Claim is archived, not deleted.

### Falsification is a feature
- A refuted claim is valuable. It tells us what is NOT true.
- Experiments with negative results are published internally.
- Kill criteria are enforced. If a paper cannot reach the quality bar, it is killed.

---

## Institution Template Research Packs

### Standard structure

```text
Template Pack: [Institution Type]

1. Identity
   - Name variants
   - Geographic distribution
   - Typical size (members, capital)

2. Governance
   - Roles (names, responsibilities, selection method)
   - Decision-making rules (quorum, voting, consensus)
   - Rotation / zoning practices
   - Term limits

3. Money Flows
   - Contribution types (dues, levies, donations, fines)
   - Collection methods
   - Disbursement rules
   - Record-keeping practices

4. Dispute Resolution
   - Common disputes
   - Resolution rituals
   - Appeal paths
   - Enforcement mechanisms

5. Trust Patterns
   - Why members trust the system
   - How trust is repaired after breach
   - External legitimacy signals

6. Digital Opportunities
   - Current tools (Excel, WhatsApp, paper)
   - Pain points
   - Feature fit for Oroma

7. Sources
   - Interview transcripts
   - Documents
   - Photos (with consent)
   - Academic references
```

### Target packs (90 days)
1. Hometown Association Template Pack
2. Faith-Based Welfare Fund Template Pack
3. Cooperative Society Template Pack
4. Market Union / Trader Association Template Pack

---

## Anti-patterns

- Do not research for research’s sake. Every project must answer: "What product decision does this inform?"
- Do not publish generic institution assumptions. Research the specific roles and rituals.
- Do not let PAGC block applied work.
- Do not treat chat transcripts as primary sources without verification.
- Do not release claims to Oroma or BeaconOS without sourceRefs.

---

## Success Criteria (60 Days)

1. One complete Institution Template Research Pack (Hometown Association).
2. `spine/extractor.py` connects to Oroma DB and generates daily facts.
3. One research feedback report delivered to Oroma with ≥5 evidence-backed recommendations.
4. PAGC claim gate resolved (all risky lines qualified or sourced).
5. Git working tree is clean.

---

*This doctrine governs all Etisiobi research. If a project contradicts it, the project is killed or corrected.*
