# Skill: Academic Paper Writing (ICEGOV Track 6)
> Fat skill — structure, tone, and submission protocol for ICEGOV Track 6 Ongoing Research papers.

## When to Invoke

Say: **"Write paper draft for [topic] targeting [venue/track]"**

---

## ICEGOV 2026 Track 6 — Submission Specs

| Parameter | Value |
|-----------|-------|
| Track | Track 6: New Metrics and Approaches for Measuring Digital Governance Success |
| Category | Ongoing Research: 8–10 pages |
| Submission | EDAS only (edas.info) |
| Format | ACM two-column, US Letter |
| Blind | Double-blind — no author names, affiliations, acknowledgements |
| Abstract | 150–300 words |
| Keywords | 3–8 |
| Acceptance rate | ~41% |
| Deadline 2026 | April 24, 2026 |

---

## Structure: Ongoing Research Paper

```
1. Introduction (1 page)
   - Open with the concrete problem (not "in this paper we propose")
   - State what existing approaches cannot do (the gap)
   - Three contributions in numbered list
   - Road map paragraph

2. Background and Related Work (1.5 pages)
   - 2.1 What existing approaches measure and why they fail for this domain
   - 2.2 The specific measurement/conceptual gap
   - 2.3 The primary context (region/institution type/community)

3. Theoretical Framework (1 page)
   - Each theory cited must do work — it must anchor at least one indicator or design choice
   - Required for ICEGOV: institutional theory + at least one empirical anchor
   - Do not cite theory for decoration

4. The Framework / Contribution (2–2.5 pages)
   - Framework overview: 1 paragraph + visual summary table
   - Each dimension: grounding, definition, formula, data source, Goodhart risk
   - Composite scoring and sensitivity discussion

5. Platform/System as Evidence Base (0.75 pages)
   - Map system architecture to framework dimensions
   - Include query logic or pseudocode for key indicators
   - Keep this as "measurement infrastructure" not "product pitch"

6. Early Empirical Signals (0.5–0.75 pages)
   - ONE illustrative case with real or clearly-labelled hypothetical values
   - Contextual evidence from literature
   - Explicit statement: "These are [preliminary signals / illustrative cases], not validation evidence"

7. Discussion (0.75–1 page)
   - 7.1 Positioning vs existing benchmarks (do not compete — complement)
   - 7.2 Privacy/sovereignty tension (required for community data)
   - 7.3 Outcomes vs organizational forms (required for informal institution research)
   - 7.4 Policy implications for [relevant national agency]
   - 7.5 Limitations and Future Work

8. Conclusion (0.25 pages)
   - Restate the gap (one sentence)
   - Restate the contribution (one sentence per contribution)
   - Close with normative vision, not just summary
```

---

## Tone and Framing Rules

**Track 6 is a measurement paper track, not a blockchain track, not a country case study track.**

Every section should answer: "What does this tell us about *measuring* digital governance success?"

- Lead with the measurement gap, not the technology
- The platform/system is evidence infrastructure, not the contribution
- Community context is the grounding, not the novelty
- Indicators are the contribution

**Opening sentence test:** If your abstract's first sentence mentions a specific technology (blockchain, Bitcoin, ZK proofs) before it mentions the measurement gap — rewrite it.

---

## Double-Blind Protocol

Before uploading to EDAS, run this grep check:
```bash
grep -i "oroma\|beaconsmith\|enugu\|citrea\|[author names]" paper.pdf
```

Replace with:
- Platform name → "the platform" or "a Bitcoin L2 community coordination platform"
- Studio name → "a creative-technology studio in Southeast Nigeria"  
- City → remove or generalize to "Southeast Nigeria"
- Author self-citations → "[ANONYMIZED]"

Note: Citrea is acceptable — it's a public technology, not uniquely identifying.

---

## EDAS Submission Checklist

- [ ] EDAS account created at edas.info
- [ ] Correct track selected (Track 6)
- [ ] Category selected (Ongoing Research = 8-10 pages)
- [ ] PDF exported from ACM template (US Letter, two-column)
- [ ] Page count verified (8–10 pages including references)
- [ ] Abstract pasted into EDAS abstract field (150–300 words)
- [ ] Keywords entered (3–8)
- [ ] Double-blind check completed (grep for identifiers)
- [ ] Paper is not under review elsewhere (ICEGOV requires exclusivity)
- [ ] Co-authors confirmed as available to present at conference

---

## Post-Acceptance (Camera-Ready)

- Reveal author information
- Convert anonymized references back to real platform names
- Add acknowledgements section (NITDA sponsorship, community participants, ethics approval)
- Add data availability statement
- Verify DOIs for all references
- Upload to EDAS by author registration deadline (August 13, 2026)
