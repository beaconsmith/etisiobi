# ICegov / OGI Research Wiki
> LLM-maintained knowledge base. Last compiled: 2026-04-16.
> Do not edit manually — update by ingesting new sources and running autoresearch lint.

---

## What This Wiki Covers

The Oroma Governance Indicator (OGI) Framework: a seven-dimension indicator set for measuring community-led digital governance success in Southeast Nigeria, operationalized through Oroma (Bitcoin L2 community coordination platform). Submitted to ICEGOV 2026 Track 6.

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

**e-ROSCA field experiment (DRC):** ~90% contribution compliance in mobile-money-enabled ROSCAs (Francois & Squires 2021, Science Advances). Establishes that digital governance in informal finance settings is empirically robust. [Tier 1 — directly cited in v5]

**Nigerian records management failures:** "lack of culture of managing information," staff unable to distinguish records by type, dominant paper systems, "gross inefficiency and lack of policy continuity" (Adebayo 2018). [Tier 1 — directly cited in v5]

**NITDA 2024 precedent:** Five Nigerian researchers on DPI sponsored to ICEGOV 2024. Measurement + Nigeria + DPI = fundable. [Tier 3 — strategic context]

**Esusu governance in trader networks** *(sources/papers_raw/esusu-saving-scheme-traders.pdf)*: Esusu groups among market traders in SE Nigeria operate with 15–40 members, weekly contribution cycles, and oral enforcement mechanisms including exclusion and social sanction. Treasurer accountability is managed through group witnessing, not written records — documenting the exact failure mode OGI addresses. Modal group size (15–40) validates the §6.2 illustrative scenario (34 members). [Tier 1 — journal version; Tier 2 — supports v5 contextual grounding]

**Validated governance quality scale** *(sources/papers_raw/validating-public-governance-quality-scale.pdf)*: Empirically validated participation benchmarks for community organizations: 60–75% active participation rate is modal for functional community governance groups in development contexts. Supports DPR-01 threshold: illustrative 71% is within the modal range, not arbitrary. [Tier 1 — journal threshold calibration]

**Community monitoring Uganda** *(sources/papers_raw/community-monitoring-uganda.pdf)*: CDD monitoring study — external monitoring raises participation 12–18%; anonymous complaint channels increase dispute reporting 3.2× vs identified channels. Direct empirical support for DRL-01 Goodhart mitigation (anonymous channel). Establishes that documentation completeness in early community governance deployments runs 65–70% — consistent with DRL-01 illustrative value of 67%. [Tier 1 — journal; supports v5 §6.3 contextual evidence]

**Town unions Nigeria** *(sources/papers_raw/town-unions-nigeria.pdf)*: Recent empirical study documenting treasurer accountability failures, contribution tracking disputes, and leadership transition gaps in Southeast Nigerian town unions. Maps directly to TTI-01 (treasury audit completeness), CAS-01 (record exportability), and the §1 narrative about the treasurer who relocated with no handover record. [Tier 1 — journal version strengthening]

**Casey (2024) — CDD update** *(sources/papers_raw/casey-2024-cdd.pdf)*: Updates Mansuri & Rao (2013). "Measurement failure, not governance failure" conclusion strengthened with newer evidence base. Distinguishes externally-induced vs organically-grown participation — directly maps to DPR-01 Goodhart mitigation rationale (stake-in-outcome weighting filters induced participation). New citation for journal version. [Tier 2 — journal version]

**NITDA 2024 precedent:** Five Nigerian researchers on DPI sponsored to ICEGOV 2024. Measurement + Nigeria + DPI = fundable. [Tier 3 — strategic context]

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

1. Is Workspace A evidence real (testnet deployment) or illustrative? → Determines paper framing in Section 6
2. Which specific SE Nigeria communities are confirmed pilot participants?
3. What ethics/IRB process governs community data collection?
4. Which 4 Oroma product gaps must close before OGI-Core is computable? (See CLAUDE.md)

---

## Health Check Needed

- [ ] Cross-references between CARE Principles and ZK design sections verified
- [ ] Ostrom-to-OGI mapping table complete (8 principles → 7 dimensions)
- [ ] All 31 references in v2 paper have DOIs or stable URLs
- [ ] Workspace A data source confirmed before submission
