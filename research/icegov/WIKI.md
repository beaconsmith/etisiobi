# ICegov / OGI Research Wiki
> LLM-maintained knowledge base. Last compiled: 2026-04-20.
> Do not edit manually — update by ingesting new sources and running autoresearch lint.

---

## What This Wiki Covers

The OGI Framework: a seven-dimension indicator set for measuring community-led digital governance success in Southeast Nigeria. A canonical blinded submission draft is frozen for ICEGOV 2026 Track 6 at `research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md`.

---

## Current Submission State

- Canonical paper file: `research/icegov/paper/OGI_PAPER_SUBMISSION_CANONICAL.md`
- Review mode: double-blind
- Draft posture: Stage 4 design-science demonstration, not empirical validation
- Abstract length: 246 words
- Main remaining tasks: ACM formatting, final page check, EDAS upload

---

## Core Claim

Existing digital governance indices (EGDI, OECD DGI, GTMI) measure what states do. They structurally cannot capture the governance quality of the community institutions — town unions, esusu circles, diaspora cooperatives — that constitute de-facto governance infrastructure for the majority of Nigerians. The OGI Framework closes this gap using verifiable on-chain records as the primary evidence base.

---

## Key Concepts

### The Measurement Gap
- **EGDI** = equally weighted composite of OSI + TII + HCI (all national-level, state-sourced)
- **Africa EGDI average** = 0.4247 (significantly below global mean)
- **WJP Rule of Law** explicitly recognizes "Informal Justice" but excludes it from aggregated scores
- **Pattern**: all major indices measure what states do, using data states produce

### Community Governance in Southeast Nigeria
- *Igbo enwe eze* ("Igbo have no king") — historically stateless, polycentric governance
- **Town unions** = de-facto fourth tier of government: self-finance roads, schools, markets; manage community funds; adjudicate disputes; coordinate diaspora
- **Esusu/isusu/ajo** = rotating savings credit association (ROSCA); operates on "oath of allegiance and mutual trust"; 17% of Nigerian adults participate
- **COVID-19 evidence**: town unions had superior distribution capacity; only 4.9% of Nigerian households received federal palliatives
- **Current record infrastructure**: WhatsApp screenshots — no audit trail, no verifiability

### The OGI Framework (7 Dimensions)

| Dim | Name | Key Indicator | Data Source |
|-----|------|---------------|-------------|
| RV | Record Verifiability | RV-01: Verifiable Action Coverage Rate | On-chain receipt index |
| DPR | Decision Participation Rate | DPR-01: Active Governance Participation Rate | Governance module event logs |
| TTI | Treasury Transparency Index | TTI-01: Treasury Audit Completeness Rate | Akpa Oroma on-chain ledger |
| DRL | Dispute Resolution Legitimacy | DRL-01: Dispute Resolution Completeness | Truth Layer dispute desk |
| CPS | Credential Portability Score | CPS-01: Portable Identity Coverage | Ichi reputation module |
| CAS | Community Autonomy Score | CAS-01: Record Exportability Rate | Platform export audit |
| FID | Financial Inclusion Depth | FID-01: First-Time Formal Participant Rate | Onboarding survey |

### Theoretical Anchors

| Theory | Source | Applied to |
|--------|--------|-----------|
| 8 design principles for collective governance | Ostrom (1990) | All 7 OGI dimensions |
| Collective action and elite capture risk | Olson (1965) | DPR monitoring design, TTI multi-sig |
| Three foundations of legitimate power (rule-governed, justifiable, consented) | Beetham (1991) | Cross-cutting legitimacy criteria |
| Procedural fairness → compliance (not outcome favourability) | Tyler (2006) | DPR, DRL dimensions |
| Pragmatic / moral / cognitive legitimacy types | Suchman (1995) | CPS, CAS dimensions |
| Records as authoritative evidence (authenticity, reliability, integrity, usability) | ISO 15489-1:2016 | RV, TTI dimensions |
| Digital continuity = information usable across transitions | National Archives (2017) | CAS dimension |
| Collective Benefit, Authority to Control, Responsibility, Ethics | CARE Principles (Carroll et al. 2020) | CAS, FID, privacy design |
| Append-only logs with consistency proofs | RFC 6962 | RV technical implementation |
| Verifiable credentials | W3C VC v2.0 | CPS dimension |
| Composite indicator construction, sensitivity | OECD/JRC Nardo et al. (2008) | Composite scoring design |
| DSR stages: problem → objective → design → demonstration → evaluation → communication | Hevner et al. (2004); Peffers et al. (2007) | Framework as Stage 4 artifact |

### Oroma as Community DPI Stack

| DPI Layer | Oroma Module | OGI Dimensions Enabled |
|-----------|-------------|------------------------|
| Digital Identity | Ichi (W3C VC credentials) | CPS-01, CPS-02, DPR-01 |
| Digital Payments | Akpa Oroma (Bitcoin L2 treasury) | TTI-01, TTI-02, FID-01–03 |
| Verifiable Data Exchange | Truth Layer (ZK proofs, dispute desk) | RV-01, DRL-01–03, CAS-01–03 |

### Key Evidence

**e-ROSCA field experiment (DRC):** ~90% contribution compliance in mobile-money-enabled ROSCAs (Francois & Squires 2021, Science Advances). Establishes that digital governance in informal finance settings is empirically robust. [Cited in canonical submission draft]

**Nigerian records management failures:** "lack of culture of managing information," staff unable to distinguish records by type, dominant paper systems, "gross inefficiency and lack of policy continuity" (Adebayo 2018). [Cited in canonical submission draft]

**NITDA 2024 precedent:** Five Nigerian researchers on DPI sponsored to ICEGOV 2024. Measurement + Nigeria + DPI = fundable. [Tier 3 — strategic context]

**Esusu governance in trader networks** *(sources/papers_raw/esusu-saving-scheme-traders.pdf)*: Esusu groups among market traders in SE Nigeria operate with 15–40 members, weekly contribution cycles, and oral enforcement mechanisms including exclusion and social sanction. Treasurer accountability is managed through group witnessing, not written records — documenting the exact failure mode OGI addresses. [Context source retained for post-submission empirical versions]

**Validated governance quality scale** *(sources/papers_raw/validating-public-governance-quality-scale.pdf)*: Empirically validated participation benchmarks for community organizations: 60–75% active participation rate is modal for functional community governance groups in development contexts. [Supporting calibration source; not required in canonical submission draft]

**Community monitoring Uganda** *(sources/papers_raw/community-monitoring-uganda.pdf)*: CDD monitoring study — external monitoring raises participation and strengthens complaint visibility. Direct empirical support for DRL-oriented documentation and anonymity design. [Cited in canonical submission draft via Bjorkman & Svensson 2009]

**Town unions Nigeria** *(sources/papers_raw/town-unions-nigeria.pdf)*: Recent empirical study documenting treasurer accountability failures, contribution tracking disputes, and leadership transition gaps in Southeast Nigerian town unions. Maps directly to TTI-01 and CAS-01 style governance-record failures. [Cited in canonical submission draft via Nwangwu 2024]

**Casey (2024) — CDD update** *(sources/papers_raw/casey-2024-cdd.pdf)*: Updates Mansuri & Rao (2013). Strengthens the interpretation that weak measured governance effects can partly reflect weak measurement, not only weak community capacity. [Cited in canonical submission draft]

**NITDA 2024 precedent:** Five Nigerian researchers on DPI sponsored to ICEGOV 2024. Measurement + Nigeria + DPI = fundable. [Tier 3 — strategic context]

---

## Threshold Calibration Evidence

Empirical grounding for OGI provisional thresholds (for journal version Delphi validation):

| Indicator | Provisional Threshold | Empirical Support | Source |
|-----------|----------------------|-------------------|--------|
| RV-01 ≥80% "digitally governed" | ≥80% | Undigitized community records run <40% completeness (Adebayo 2018); ISO 15489 "complete and unaltered" principle; blockchain audit trail systems target ≥95% (ISACA 2024) | Multiple |
| DPR-01 modal participation | 60–75% active | Validated governance quality scale: functional community groups show 60–75% active participation | sources/papers_raw/validating-public-governance-quality-scale.pdf |
| DPR-01 illustrative 71% | Within modal range | Modal range 60–75%; illustrative value is representatively plausible | Ibid |
| DRL-01 illustrative 67% | Within early-deployment range | Community monitoring (Uganda): 65–70% documentation completeness in early deployments | sources/papers_raw/community-monitoring-uganda.pdf |
| FID-01 group size (34 members) | Modal esusu range | 15–40 members is modal for functional SE Nigeria esusu groups | sources/papers_raw/esusu-saving-scheme-traders.pdf |
| FID-01 3 cycles minimum | Enforcement observable | Besley et al. (1993): 3–4 cycles minimum for enforcement mechanisms to operate | Besley et al. 1993 |

---

## Post-Submission Backlog

Priority work after ICEGOV submission:

| Task | Why needed | Priority |
|------|------------|----------|
| Delphi validation of thresholds and weights | Converts provisional thresholds into reviewed measurement design | HIGH |
| First ethics-governed pilot data | Moves paper from illustrative computability to evaluated evidence | HIGH |
| Cross-substrate comparison (ledger vs simpler append-only logs) | Tests whether the framework depends on a single implementation style | MEDIUM |
| Large-group calibration | Tests how DPR and related indicators behave beyond small and medium groups | MEDIUM |

---

## Source Clusters (124 total)

| Cluster | Sources | File |
|---------|---------|------|
| C1&6: E-Governance Frameworks + Indicator Methodology | 30 | `sources/cluster1_6_frameworks/MANIFEST.md` |
| C2&3: SE Nigeria Governance + Isusu/ROSCA Finance | 30 | `sources/cluster2_3_nigeria_isusu/MANIFEST.md` |
| C4&5: Records Management + Blockchain Civic Governance | 30 | `sources/cluster4_5_records_blockchain/MANIFEST.md` |
| C7+: Data Sovereignty + DPI + ICegov Papers | 34 | `sources/cluster7_crosscutting/MANIFEST.md` |

---

## Open Questions

1. Which communities should be first pilot candidates after submission?
2. What ethics/IRB path will govern onboarding-survey and inclusion data?
3. Which four product gaps should close first for post-submission OGI evidence extraction?
4. When should the Research Spine start producing daily facts files?

---

## Health Check Needed

- [x] Canonical blinded submission draft frozen
- [ ] ACM PDF page check completed
- [ ] DOI/URL spot-check completed on canonical bibliography
- [ ] First facts file generated once DB connection is available
