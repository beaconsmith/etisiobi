# Etisiobi Knowledge Pipeline

> Version: 1.0
> Date: 2026-05-03
> Goal: Define how knowledge moves from raw sources to research output to product impact.

---

## Pipeline Stages

```text
Raw Sources
    ↓
Ingest & Catalog
    ↓
Extraction & Coding
    ↓
Synthesis & Claim Formation
    ↓
Falsification & Review
    ↓
Template / Paper / Feedback
    ↓
Product Handoff (Oroma + BeaconOS)
    ↓
Field Validation (Pilot)
    ↓
Update & Iterate
```

---

## Stage 1: Raw Sources

### Types
- Interview transcripts (recorded, transcribed, consented)
- Field notes (dated, geotagged, observer-named)
- Documents (constitutions, ledgers, meeting minutes)
- Academic papers (PDF, metadata, citation)
- Regulatory texts (NITDA, CAC, SEC guidelines)
- News and media (date, outlet, URL, archive link)

### Storage
- `library/papers/` — academic PDFs
- `research/[program]/sources/` — primary sources
- `data/` — structured datasets (CSV, JSON)
- `spine/` — extraction scripts

### Naming convention
```text
interview_[role]_[location]_[date].md
document_[type]_[institution]_[date].pdf
paper_[author]_[year]_[topic].pdf
```

---

## Stage 2: Ingest & Catalog

### Actions
1. Add source to `source_register.csv`.
2. Assign source ID.
3. Tag with: type, date, location, institution type, reliability.
4. Store original in `library/` or `research/[program]/sources/`.
5. Generate citation entry.

### Tools
- `library/research_pipeline/` — bulk downloaders
- Manual entry for primary sources

---

## Stage 3: Extraction & Coding

### Actions
1. Read source.
2. Extract factual claims (who, what, when, where, how).
3. Code claims by theme (governance, money, dispute, trust, digital).
4. Link claims to source ID.
5. Tag confidence (proven, supported, hypothesis, refuted).

### Tools
- Manual close reading
- `spine/extractor.py` for structured data from Oroma DB
- Spreadsheet or qualitative coding software

---

## Stage 4: Synthesis & Claim Formation

### Actions
1. Aggregate coded claims by theme.
2. Identify patterns across sources.
3. Form higher-level claims.
4. Check for contradictions.
5. Write synthesis memo.

### Output
- `research/[program]/syntheses/[theme].md`
- Must include: claims, evidence, limitations, contradictions

---

## Stage 5: Falsification & Review

### Actions
1. Pre-register hypotheses before testing.
2. Design empirical test (interview, survey, experiment, document review).
3. Run test.
4. Record result.
5. If refuted, archive claim with explanation.
6. If supported, advance to output stage.

### Review
- Peer review within Etisiobi team.
- External review for submission-grade papers.
- Claim gate (`pagc_claim_gate.py`) for language strength.

---

## Stage 6: Template / Paper / Feedback

### Institution Template Pack
- Assemble syntheses into standard template structure.
- Add source register.
- Mark confidence level for each section.

### Academic Paper
- Follow ICEGOV / venue format.
- Include method, data, analysis, limitations.
- Pass quality bar before submission.

### Product Feedback
- Translate findings into Oroma feature recommendations.
- Format: finding → evidence → recommendation → acceptance test.
- Store in `research/product_feedback/`.

---

## Stage 7: Product Handoff

### To Oroma
- `spine/research_feedback.py` generates structured report.
- Report includes: backend truth gaps, UI benchmarks, test gaps, feature recommendations.
- Oroma product lead reviews and prioritizes.

### To BeaconOS
- Research summaries copied to `beaconos/raw/research/`.
- Syntheses become claims in BeaconOS memory index.
- Contradictions become risks in BeaconOS risk registry.

---

## Stage 8: Field Validation

### Pilot feedback loop
- Oroma pilot generates real usage data.
- `spine/extractor.py` reads Oroma DB.
- Facts validate or refute template assumptions.
- Template updated.

### Continuous update
- Every pilot finding feeds back to Stage 1 as a new source.
- Templates are living documents, not static outputs.

---

## Metrics

| Metric | Target |
|--------|--------|
| Sources ingested per week | ≥5 |
| Claims extracted per source | ≥3 |
| Syntheses produced per month | ≥2 |
| Templates completed per quarter | ≥1 |
| Feedback reports to Oroma per month | ≥1 |
| Falsified claims archived (not deleted) | 100% |
| SourceRefs present on all outputs | 100% |

---

*Do not implement yet. Start by cataloging existing sources and filling gaps.*
