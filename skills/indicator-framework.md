# Skill: Indicator Framework Design
> Fat skill — design pattern for constructing governance indicator frameworks that survive peer review.

## What This Skill Does

Guides the design of a multi-dimension indicator framework from theoretical grounding through operationalization, Goodhart documentation, and composite scoring. Used for the OGI Framework and any future governance measurement work.

---

## When to Invoke

Say: **"Design indicator framework for [governance domain]"**

---

## The 5-Layer Design Pattern

Every robust indicator framework requires all five layers:

### Layer 1: Theoretical Grounding
Each dimension must be anchored to at least one of:
- **Institutional theory** (Ostrom design principles, Buterin legitimacy framework, polycentric governance)
- **Standards** (ISO 15489 records, NIST controls, W3C credentials)
- **Empirical evidence** (e-ROSCA experiments, CDD syntheses, ROSCA scoping reviews)
- **Sovereignty principles** (CARE Principles, data sovereignty frameworks)

Rule: if you can't cite the theoretical anchor for a dimension in one sentence, the dimension isn't ready.

### Layer 2: Precise Definition
Each dimension needs:
- A one-sentence definition of **what is being measured** (not how)
- A clear **unit of analysis** (community, workspace, governance cycle, member)
- A **measurement period** (90-day window, annual, per governance cycle)

### Layer 3: Computable Indicator
Each dimension needs at minimum:
- A **primary indicator** with a formula using observable inputs
- A **data source**: on-chain event, exported artifact, or community survey — never self-report as sole evidence
- A **benchmark** or threshold that distinguishes meaningful variation

For on-chain indicators, include query pseudocode:
```
indicator = count(events matching criteria) / count(total events) × 100
```

### Layer 4: Goodhart Documentation
Every indicator will be gamed if it matters. For each dimension document:
- **The attack**: how would a bad actor inflate this metric without improving governance?
- **The mitigation**: a design choice that makes gaming structurally harder

This section should be written *before* publishing the framework, not after someone games it.

### Layer 5: Dashboard + Sensitivity
- **Dashboard-first**: never publish only a single composite score. Always show dimension scores.
- **Optional composite**: if combining, use equal weights as default + sensitivity tests under 3 alternative schemes
- **Community calibration**: document which dimensions carry more weight in which community types
- **Sensitivity reference**: cite OECD/JRC Composite Indicators Handbook for methodology defense

---

## The Privacy Constraint

Any framework that measures community governance must pass the CARE test:

> Does this indicator require communities to expose records beyond the scope their governance protocols authorize?

If yes, the indicator design is wrong. The fix is usually:
- ZK proof instead of disclosed value (treasury balance → solvency proof)
- Aggregation instead of individual disclosure (participation count, not named participants)
- Community-controlled export (records accessible to members, not default-public)

Document the privacy approach for each indicator explicitly.

---

## The "Outcomes vs Forms" Rule

Indicators must measure **governance outcomes**, not **organizational forms**.

Wrong: "Is the community registered as a cooperative?" (organizational form)
Right: "What proportion of decisions have documented rationales?" (governance outcome)

Wrong: "Does the community use formal meeting minutes?" (form)
Right: "Can a decision made 12 months ago be reconstructed from archived records?" (outcome)

This rule prevents the framework from incentivizing bureaucratization of informal institutions.

---

## Reviewer Objection Pre-emption

Before finalizing any framework, map responses to these standard objections:

| Objection | Required response in paper |
|-----------|---------------------------|
| "Framework is too broad" | Show each dimension maps to a distinct theoretical anchor |
| "Single-score arbitrariness" | Dashboard-first design + sensitivity tests |
| "Weak causal attribution" | Explicit: framework measures process quality, not development outcomes |
| "Self-report bias" | Document that primary evidence is artifact-based, not self-report |
| "Privacy/surveillance risk" | CARE compliance section + ZK/minimal-disclosure design |
| "Over-bureaucratization" | Outcomes vs forms rule — cite explicitly |
| "Not generalizable" | Acknowledge primary context; specify transferability conditions |

---

## Reference Framework: OGI (7 Dimensions)

The OGI Framework for community-led digital governance is the reference implementation of this design pattern. See:
- `research/icegov/paper/OGI_PAPER_DRAFT_v2.md` — full framework
- `research/icegov/synthesis/AUTORESEARCH_SYNTHESIS.md` — theoretical grounding detail

The 7 OGI dimensions and their theoretical anchors:
1. Record Verifiability → ISO 15489 + RFC 6962
2. Decision Participation Rate → Ostrom P3 + Buterin legitimacy
3. Treasury Transparency Index → ISO 15489 + NIST + Buterin anti-collusion
4. Dispute Resolution Legitimacy → Ostrom P6 + Fox social accountability
5. Credential Portability Score → W3C VC + CARE P2 + Ostrom P1
6. Community Autonomy Score → CARE P2 + DPG Standard + Ostrom P7
7. Financial Inclusion Depth → e-ROSCA evidence + CARE P1 + Gugerty
