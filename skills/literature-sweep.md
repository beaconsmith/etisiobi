# Skill: Literature Sweep
> Fat skill — 7-cluster sweep methodology for research papers targeting Global South governance, technology, and indigenous knowledge domains.

## What This Skill Does

Systematically sweeps academic and grey literature across 7 pre-defined clusters relevant to the research question, targeting ≥100 sources with full metadata. Outputs cluster MANIFEST.md files and a MASTER_INDEX.md.

---

## When to Invoke

Say: **"Sweep [topic] for [program]"**

Example: "Sweep community governance indicators for icegov"

---

## The 7 Standard Clusters

These map to the ICegov OGI research. Adapt cluster names for other programs.

| # | Cluster | Target Sources | Key Databases |
|---|---------|----------------|---------------|
| 1 | **Measurement Frameworks** — existing indices, benchmarks, methodology | 25+ | UN, OECD, World Bank, EGOV proceedings |
| 2 | **Regional Context** — local governance, political economy, institutions | 25+ | ResearchGate, AJOL, African Studies journals |
| 3 | **Informal Finance / Coordination** — ROSCAs, cooperatives, savings groups | 20+ | JSTOR, economic journals, dev finance |
| 4 | **Records & Accountability** — records management, archival standards, audit | 20+ | ISO, NIST, archival science journals |
| 5 | **Technology Stack** — blockchain, DPI, ZK proofs, verifiable credentials | 20+ | arXiv, ACM DL, W3C, World Bank |
| 6 | **Indicator Design Methodology** — composite indicators, Delphi, validation | 15+ | OECD/JRC, UNDP, statistical methods |
| 7 | **Data Sovereignty & Ethics** — CARE principles, community data, epistemic justice | 15+ | Data Science Journal, indigenous studies |

---

## Execution Protocol

```
For each cluster:
1. WebSearch with 3-5 targeted queries (see query templates below)
2. WebFetch priority URLs (those flagged in synthesis or prior sweeps)
3. curl/wget PDF where available; WebFetch HTML full-text where not
4. Save: [slug].txt (full text) + [slug].json (metadata: title, authors, year, doi, abstract, relevance_note)
5. Write MANIFEST.md: table of all sources with relevance column
```

### Query Templates by Cluster

**Cluster 1 (Measurement):**
- "[topic] measurement framework indicator [year range]"
- "[topic] composite index methodology [region]"
- "EGDI GTMI [topic] measurement gap"

**Cluster 2 (Regional):**
- "[institution type] [region] governance accountability academic"
- "[country] community-led development governance records"
- "[ethnic group / political tradition] governance structure"

**Cluster 3 (Informal Finance):**
- "ROSCA rotating savings [region] governance trust academic"
- "[local name: esusu/ajo/susu] digitization accountability"
- "informal finance formalization governance [region]"

**Cluster 4 (Records):**
- "records management [region] local government accountability"
- "ISO 15489 records governance [context]"
- "digital continuity governance [institution type]"

**Cluster 5 (Technology):**
- "blockchain [governance type] [region] verifiable records"
- "DPI digital public infrastructure [region] community"
- "zero-knowledge proof community governance accountability"

**Cluster 6 (Indicator Methodology):**
- "composite indicator Delphi validation governance"
- "OECD JRC composite indicator handbook methodology"
- "governance indicator construction weighting sensitivity"

**Cluster 7 (Sovereignty):**
- "CARE principles indigenous data governance community"
- "community data sovereignty [region]"
- "epistemic justice data governance [context]"

---

## Output Structure

```
research/[program]/sources/
├── cluster1_[name]/
│   ├── MANIFEST.md
│   ├── [source_slug].txt      ← full text where available
│   └── [source_slug].json     ← metadata
├── cluster2_[name]/
│   └── ...
└── MASTER_INDEX.md            ← 100+ source master table with citation clusters by paper section
```

---

## Quality Gates

Before declaring sweep complete:
- [ ] ≥100 sources total across all clusters
- [ ] Each cluster has ≥15 sources
- [ ] At least 3 sources from current year (year of sweep)
- [ ] At least 1 peer-reviewed empirical study per cluster (not just frameworks/reports)
- [ ] Gap documentation: list what was searched for but not found
- [ ] MASTER_INDEX.md maps sources to paper sections

---

## Skill Lifecycle Trigger

If a sweep reveals a repeatable query pattern, source database, paywall workaround, dedupe rule, OCR failure mode, metadata cleanup script, or cluster taxonomy improvement, invoke `skills/skill-lifecycle.md`.

Before updating a skill:
1. Record the baseline problem: missing source type, bad query, duplicate pattern, stale source cluster, or extraction failure.
2. Change one query/rule/script at a time.
3. Re-run a focused sweep or source check.
4. Keep the lesson only if coverage, freshness, metadata quality, or gap documentation improves.
5. Add a compact note to the relevant skill or sibling `.memory.md`; keep paper-specific source decisions in the paper's logs.

Never treat a successful query as evidence for a claim. It only improves the acquisition method; claims still need source extraction and citation checks.

---

## Artifact-First Rule

For every source, the data source must be an observable artifact:
- Full text (HTML or PDF)
- Abstract + DOI (minimum viable)
- Never: "I know this paper exists from memory"

If a paper is behind a paywall and no open-access version exists, record: title, authors, year, DOI, and note "paywall — abstract only." This is a real source with incomplete coverage, not a fabricated citation.
