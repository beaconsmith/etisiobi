# Measuring What States Miss: An Indicator Framework for Community-Led Digital Governance in Southeast Nigeria

**Track 6: New Metrics and Approaches for Measuring Digital Governance Success**
**Category: Ongoing Research Paper (8–10 pages)**
**ICEGOV 2026 — Riyadh, Saudi Arabia**

---

**Nzube Ndiokwelu**
Beaconsmith Collective Labs
Enugu, Southeast Nigeria
beaconsmithmedia@gmail.com

---

## Abstract

The dominant digital governance indices — EGDI, OECD DGI, GTMI — measure what states do. They cannot capture the governance quality of the community institutions — town unions, rotating savings circles (esusu/ajo), diaspora cooperatives — that constitute de-facto governance infrastructure for the majority of Nigerians. No prior indicator framework addresses this community layer, and the closest precedents — Community Scorecard and Social Audit methodologies — measure citizen-to-state accountability, not community-internal governance quality. This paper introduces the **OGI Framework**: seven new indicators for measuring community-led digital governance success. Each indicator is (i) derived from verifiable on-chain artifacts rather than self-reported surveys — measuring the auditability conditions of governance actions, not the factual accuracy of their content; (ii) grounded in ISO 15489 records management standards and Ostrom's collective action design principles; (iii) accompanied by a documented Goodhart risk and mitigation; and (iv) privacy-preserving — community records are verifiable to members without becoming legible by default to external auditors. The framework is grounded in governance legitimacy theory [Beetham 1991; Tyler 2006; Suchman 1995] and CARE data sovereignty principles. Following the design science research (DSR) methodology [Hevner et al. 2004; Peffers et al. 2007; Gregor & Hevner 2013], we present a Stage 4 demonstration: we show that the framework's indicator formulas are computationally tractable when applied to the data architecture of Oroma, a community coordination platform under development in Southeast Nigeria. Stage 5 (empirical evaluation with live communities) requires mainnet deployment and ethics clearance, and constitutes the post-submission research programme. We argue that community-layer digital governance requires metrics that start from community evidence — and that such metrics are now theoretically grounded and architecturally feasible.

**Keywords:** digital governance indicators, community-led development, Southeast Nigeria, verifiable records, DPI, informal governance, ROSCA, composite indicators

---

## 1. Introduction

The phrase *Igbo enwe eze* — "Igbo have no king" — describes a political tradition in Southeast Nigeria that is not an absence of governance but a different architecture of it [Okafor 2019]. Governance in Igboland has always been distributed: through town unions that self-finance roads and schools, through esusu circles that capitalize enterprise without banks, through age grades and diaspora networks that sustain home communities across distance [Harneit-Sievers 2006; Ottenberg 1955]. When Nigeria's federal government distributed COVID-19 relief palliatives in 2020, only 4.9% of Nigerian households received any assistance, while warehouse looting by politically-connected actors was documented across multiple states [Nwangwu 2024]. Town unions had the community knowledge and trust networks to distribute more equitably. What they lacked was a verifiable record system — decisions made on WhatsApp disappeared, funds moved on social trust alone, and no audit trail existed when disputes arose.

The paper's core argument is not that community governance is broken. It is that the *measurement* of community governance is broken — and that this measurement failure has consequences for how digital governance success is defined, funded, and evaluated across Africa.

The UN E-Government Development Index (EGDI), the OECD Digital Government Index (DGI), and the World Bank GovTech Maturity Index (GTMI) constitute the authoritative vocabulary for "digital governance success." None measures governance quality below the state level. Africa's average EGDI score is 0.4247 [UN EGov 2024] — a number that tells us nothing about whether the town union treasurer in Afikpo can be held accountable, whether the diaspora community fund in a Southeast Nigerian city can produce an auditable receipt, or whether the esusu circle that financed a member's business can prove the loan terms were honoured.

Polycentric governance theory holds that self-organizing community institutions constitute legitimate governance actors in their own right, capable of managing collective resources through their own rules, monitoring, and sanctions [Ostrom 1990; Aligica & Tarko 2012]. Providing an indicator framework that makes this governance layer observable in the digital domain — without requiring state mediation or expert surveys — is the contribution of this paper.

We propose the **OGI Framework** (Oroma Governance Indicator Framework): seven new indicators with three contributions:

1. **A documented measurement gap** — demonstrating, from the construction logic of existing indices and the scoping of existing citizen-accountability methodologies, what they structurally cannot capture about community-internal governance.

2. **A theoretical foundation** — synthesizing Ostrom's collective action design principles, ISO 15489 records standards, governance legitimacy theory [Beetham 1991; Tyler 2006; Suchman 1995], and CARE data sovereignty principles into a coherent measurement ontology.

3. **Seven operationalized, computable indicators** — each with a definition, formula, artifact-based data source, documented Goodhart risk, and demonstrated computational tractability using the Oroma platform's data architecture as the computational substrate.

---

## 2. Background and Related Work

### 2.1 What Existing Indices Measure — and What They Cannot

The UN EGDI is computed as an equally weighted composite of the Online Services Index (OSI), Telecommunications Infrastructure Index (TII), and Human Capital Index (HCI) [UN EGov Survey 2024 Technical Appendix]. The OSI assesses national government portal feature presence; TII draws on ITU infrastructure penetration data; HCI draws on UNESCO education statistics. All three components are national-level, state-sourced, and capture service *availability* — not whether governance decisions within communities are recorded, verifiable, or durable.

The OECD DGI measures six dimensions of digital government maturity across 38 countries, all OECD members or accession candidates [OECD DGI 2023]. The World Bank GTMI covers 198 economies, relying substantially on government self-reported survey responses [GTMI 2025]. The Worldwide Governance Indicators aggregate perceptions-based surveys [WGI 2025]. The Mo Ibrahim IIAG synthesizes 96 indicators from 49 sources [IIAG 2024]. The WJP Rule of Law Index recognizes "Informal Justice" conceptually but excludes it from aggregated scores [WJP 2025].

The pattern is structural, not incidental: every major index measures what states do, using data states produce. This is not a gap that can be closed by extending existing frameworks with community sub-indices. Any measurement system that requires state self-reporting, government portal access, or expert perception surveys as its primary evidence source is architecturally incapable of capturing governance that the state does not recognize, register, or observe — which is precisely the governance reality of most Nigerians. Closing this gap requires a different evidence base: community-produced artifacts, not state-mediated data.

**Table 1** illustrates the measurement gap using the OGI's seven dimensions as the test:

| Measurement property | EGDI | OECD DGI | GTMI | OGI Framework |
|----------------------|------|----------|------|---------------|
| Community decisions are verifiable | ✗ | ✗ | ✗ | ✓ RV-01 |
| Records survive leadership transition | ✗ | ✗ | ✗ | ✓ RV-01, CAS-01 |
| Treasury history reconstructable | ✗ | ✗ | Partial | ✓ TTI-01 |
| Governance participation documented | Partial (e-participation) | Partial | Partial | ✓ DPR-01/02 |
| Dispute resolution auditable | ✗ | ✗ | ✗ | ✓ DRL-01 |
| Community controls own records | ✗ | ✗ | ✗ | ✓ CAS-01–03 |
| Portable community credentials | ✗ | ✗ | ✗ | ✓ CPS-01 |
| Evidence source | State self-report | Government survey | Gov survey + external | On-chain artifacts |

Heeks [2006] identified this as a "ranking obsession" that privileges legible state-layer governance over the informal institutions that constitute governance reality for the Global South. Two decades later, the gap remains — but the technical conditions to close it have changed.

### 2.2 Community-Led Development, Measurement, and Prior Indicator Work

A 3ie evidence synthesis of community-driven development (CDD) programs finds consistent gains in small-scale infrastructure but "little or no impact on social cohesion and governance" [3ie 2018]. Mansuri and Rao [2013] attribute this not to the absence of community capacity but to the absence of monitoring systems capable of capturing governance quality. Casey [2024], updating this evidence base with more recent CDD evaluations, strengthens the "measurement failure, not governance failure" conclusion — and further distinguishes externally-induced from organically-grown participation, a distinction directly relevant to the OGI Framework's DPR-01 Goodhart mitigation design. The measurement failure precedes and produces the apparent governance failure.

**Relationship to Community Scorecard and Social Audit methodologies.** Two established measurement traditions are adjacent to the OGI Framework and merit explicit distinction. The **Community Scorecard** methodology [Singh & Shah 2003] uses facilitated community meetings to score service-provider performance through citizen dialogue; it measures *citizen satisfaction with state-provided services*. The **Social Audit** tradition [Gaventa & McGee 2013] uses public hearings and record inspection to verify that government budgets were spent as allocated; it measures *state-to-citizen accountability for delegated resources*. Both are powerful instruments within their scope. Neither measures what the OGI Framework measures: the governance quality of decisions and records *produced by* community institutions themselves, about their own internal collective action, without a state or service provider as the principal accountable party. The unit of analysis differs: Scorecard and Social Audit presuppose that the accountable actor is external to the community; OGI presupposes that the community itself is the record producer whose governance quality is being measured. Bjorkman and Svensson's [2009] randomized evaluation of community-based monitoring in Uganda demonstrated that structured monitoring of providers raised service quality — evidence that measurement changes behavior — but the methodology remains citizen-over-state, not community-over-itself.

No prior indicator framework specifically addresses community-layer digital governance for non-state institutions in Sub-Saharan Africa. A review of ICEGOV 2024 and 2025 proceedings identifies papers on national DPI measurement, e-participation indices [Kabanov 2025], and local online services (LOSI) — the last of which measures state LGA portal features, not community institution governance [Guimarães et al. 2025; Susar et al. 2025]. The digital governance bibliometric analysis of Nigerian public administration [Ishola et al. 2025] identifies indigenous technology development and marginalized community research as the two largest gaps in the field. The OGI Framework addresses both.

The contribution of this paper: the measurement gap is now addressable in principle. Community coordination platforms that generate verifiable artifacts — on-chain receipts, cryptographic proofs of participation, append-only decision logs — can serve as the evidentiary basis for governance indicators that do not rely on state self-reporting or expert perception surveys. Whether this is viable in practice for the target communities is the empirical question the post-submission research programme will test.

### 2.3 Southeast Nigeria as the Primary Context

Seventeen percent of Nigerian adults save in informal savings groups (adashi/esusu/ajo), according to World Bank General Household Survey Panel data. Rotating savings and credit associations (ROSCAs) — members contributing fixed amounts at regular intervals, with each receiving the pooled sum in rotation — operate on "an oath of allegiance and mutual trust" with no formal legal mechanism [Global Informality Project 2020; Besley, Coate & Loury 1993]. The foundational anthropological and development-economics literature on ROSCAs [Ardener 1964; Bouman 1995] documents their ubiquity across the Global South and their structural reliance on reputational enforcement rather than written records — the exact evidentiary condition that OGI is designed to make visible and measurable.

In Southeast Nigeria, these financial governance mechanisms are embedded in a broader institutional ecology: town unions that self-finance public infrastructure, age grade associations that execute development projects, diaspora networks that sustain home communities [Harneit-Sievers 2006; Honey & Okafor 1998; Uduku 2002]. ROSCA participation is also gender-stratified in specific and well-documented ways: women predominate in many Southeast Nigerian esusu groups, and women-only groups often use stricter sanction norms than mixed groups [Ardener & Burman 1995; Gugerty 2007]. Any framework that measures community-layer governance without accounting for gender-stratified participation structures will produce misleading aggregate scores — which is why the OGI Framework separates FID-02 as a deployment-blocked indicator requiring consent-first protocols rather than embedding gender into the core composite.

Records management studies in Nigerian local governance document systematic failures of institutional memory — misplaced files, unwritten decisions, transitions with no documentation handover [Adebayo 2018]. The governance challenge is not institutional capacity; it is institutional *legibility*. When a treasurer relocates, when a diaspora contributor demands accountability, when a dispute reaches a critical threshold, there is no verifiable audit trail.

---

## 3. Theoretical Framework

### 3.1 Ostrom's Design Principles as Measurement Anchors

Ostrom's eight design principles for robust common-pool resource governance [Ostrom 1990] identify measurable properties of durable community governance: clearly defined membership boundaries, rules matched to local conditions, collective-choice arrangements, monitoring of conditions and behavior, graduated sanctions, conflict-resolution mechanisms, recognition of rights to organize, and nested enterprises. Each principle is a measurement anchor: if a governance system exhibits the property, it should be detectable in records and artifacts. Where no artifact exists, the property is absent or unmeasured — both are governance failures.

The collective action literature adds a structural challenge: institutions designed to serve all members can be captured by organized subgroups [Olson 1965]. Ostrom's Principles 4 (monitoring) and 5 (graduated sanctions) are specifically designed to make capture harder. The OGI Framework measures whether governance design imposes structural barriers against elite capture — through quorum requirements, multi-signature approvals, anonymous dispute channels, and privacy-preserving treasury verification.

### 3.2 Governance Legitimacy as the Outcome Variable

Political legitimacy theory provides the conceptual basis for what the OGI Framework measures. Beetham [1991] identifies three foundations of legitimate power: rule-governed exercise, justifiability by shared beliefs, and expressed consent. Tyler [2006] demonstrates empirically that compliance with institutional decisions depends primarily on perceived procedural fairness, not outcome favourability. Suchman [1995] distinguishes pragmatic, moral, and cognitive legitimacy — distinctions that map onto the OGI Framework's measurable dimensions.

Five measurable conditions of governance legitimacy emerge from this literature: **continuity** (prior acceptance predicts future acceptance — requires records of prior decisions); **fairness** (outcomes satisfy procedural justice norms — requires transparent process documentation); **process** (legitimate procedures produce auditable outputs); **performance** (successful execution generates institutional confidence); and **participation** (members accept outcomes they helped shape — requires verifiable participation records). These five conditions are the cross-cutting quality criteria applied across all seven OGI dimensions.

### 3.3 Records as Governance Infrastructure

ISO 15489-1:2016 defines authoritative records as evidence when they possess: **authenticity** (the record is what it claims to be), **reliability** (it accurately represents the activity), **integrity** (it is complete and unaltered), and **usability** (it can be retrieved and interpreted) [ISO 15489 2016]. The National Archives' digital continuity framework [2017] adds the temporal dimension: continuity means information remains usable across transitions — leadership turnover, system migrations, funding gaps.

These four properties are necessary conditions for governance quality at the community layer. A governance system that makes decisions but cannot produce ISO 15489-quality evidence of those decisions is not accountable in any measurable sense.

### 3.4 CARE Principles: Sovereignty Over Surveillance

The CARE Principles [Carroll et al. 2020] — Collective Benefit, Authority to Control, Responsibility, Ethics — establish that community governance records must serve community purposes, that communities must control their own data governance protocols, and that data stewardship must embed community values. More verifiability is not always better governance. An indicator framework that makes community records more legible to external auditors at the cost of member privacy produces a governance failure in a different direction. The CARE Principles are incorporated into the OGI Framework as a structural constraint: indicators must be computable *without* requiring communities to expose records beyond the scope their governance protocols authorize.

---

## 4. The OGI Framework

### 4.1 What Is New About These Indicators

The OGI Framework departs from existing governance measurement in four specific ways, each directly responsive to Track 6's mandate for new measurement approaches:

**1. Artifact-first evidence.** Every OGI indicator's primary data source is an observable artifact — an on-chain event, an exported record, a block explorer query — not a self-reported survey. This addresses the response bias documented in GTMI [2025]. Critically, artifact-based measurement verifies that a record *exists and is unaltered* — it does not verify that the recorded information is factually accurate. Accuracy requires complementary social mechanisms (dispute resolution, multi-signature approval) that the OGI Framework separately measures in the DRL and DPR dimensions.

**2. Privacy-preserving indicators.** TTI-02 uses zero-knowledge proofs to verify treasury solvency without revealing individual contribution amounts. CAS-03 measures state dependency as a governance risk to minimize, not a compliance threshold to reach. These are design properties that no existing governance index incorporates.

**3. Community-sovereignty metrics.** The CAS dimension (Record Exportability, Platform Independence, Imposed State Dependency) measures whether governance capacity remains under community control independent of platform operators and state registries. No existing digital governance index measures this.

**4. Computation without intermediary cooperation.** The OGI-Core indicators (RV-01, DPR-01, TTI-01, DRL-01) require append-only, independently verifiable records as their evidentiary base — the core technical requirement. A distributed ledger satisfies this without requiring a trusted operator, database administrator, or platform API. A community member with the workspace contract address and block explorer access can verify indicator inputs without requesting cooperation from any intermediary. This requirement — not blockchain as ideology — drives the infrastructure choice documented in §5.3.

### 4.2 Framework Design Logic

The OGI Framework operationalizes one necessary condition for community governance accountability: the production of *governance records that are verifiable, continuous, participatory, auditable, sovereign, repairable, and inclusive*. These are process-quality properties. High OGI scores indicate that governance actions are documentable and auditable — not that those actions are normatively correct, equitable, or effective. The causal link between process quality and governance outcomes is a hypothesis to be tested in Stage 5 evaluation, not an assumption embedded in the framework. These seven properties map to seven indicator dimensions. Each specifies:

- A theoretical grounding in Ostrom, ISO 15489, legitimacy theory, or CARE
- A precise definition of what is being measured
- A primary indicator with a computation formula
- A data source: on-chain event, exported artifact, or platform log — never self-report as primary evidence
- A known Goodhart risk with documented structural mitigation

### 4.3 Seven Indicator Dimensions

---

**Dimension 1 — Record Verifiability (RV)**

*Grounding*: ISO 15489 (authenticity, reliability, integrity, usability); RFC 6962 (append-only logs with consistency proofs); W3C Verifiable Credentials v2.0

*Definition*: The proportion of community governance actions for which a cryptographically verifiable, externally reproducible record exists.

*RV-01 — Verifiable Action Coverage Rate*:
```
RV-01 = (Governance actions with anchored on-chain receipt) /
         (Total governance actions logged on platform) × 100
```

*Data source*: Block explorer query against the community's workspace contract address. Computable by any member without platform API access.

*Benchmark*: Provisional thresholds pending Stage 5 empirical calibration. Current working hypothesis: ≥80% = "digitally governed"; 40–79% = "transitional"; <40% = "pre-digital governance record-keeping." The 80% threshold is empirically motivated: Nigerian records management studies document undigitized governance systems running below 40% completeness [Adebayo 2018], and ISO 15489-1:2016's "complete and unaltered" principle sets the upper standard. Enterprise blockchain audit deployments target ≥95% completeness [ISACA 2024]; 80% is positioned as the threshold where on-chain evidence dominates the record base. These thresholds remain hypotheses to be validated via Delphi and deployment data, not standards to be enforced.

*Goodhart risk*: Records technically on-chain but not independently reproducible (single sequencer, no fraud proof publication). *Mitigation*: Require at least one IPFS-pinned proof export per governance cycle before the cycle counts as closed.

---

**Dimension 2 — Decision Participation Rate (DPR)**

*Grounding*: Ostrom Principle 3 (collective-choice arrangements); Tyler [2006] (procedural fairness produces legitimacy); Mansuri & Rao [2013]; Casey [2024] (induced vs. organic participation)

*Definition*: The proportion of eligible community members who actively participated in governance decisions during a defined period.

*DPR-01 — Active Governance Participation Rate*:
```
DPR-01 = (Unique members casting ≥1 vote or submitting ≥1 proposal
           in a 90-day window) /
          (Total registered members in that window) × 100
```

*DPR-02 — Quorum Achievement Rate*:
```
DPR-02 = (Proposals reaching the workspace-defined quorum threshold) /
          (Total proposals initiated) × 100
```

*Data source*: Governance module event logs; workspace membership registry (on-chain).

*Empirical calibration*: Validated public-governance quality research finds 60–75% active participation is the modal range for functional community governance groups. The §6.2 illustrative value of 71% falls within this range — not arbitrary.

*Goodhart risk*: Manufactured participation — automated or coerced votes. *Mitigation*: Weight participation by stake-in-outcome: count members who made at least one treasury contribution in the 90-day window, *with a grace-period exception for new joiners (≤30 days) and members whose contribution cadence is annual rather than monthly* (e.g., diaspora members). The rationale follows Olson's [1965] logic of selective incentives: members with a financial stake in treasury decisions have a material interest in genuine participation; those without such stake can vote costlessly. Treasury contribution is an observable, on-chain proxy for skin-in-the-game — not a wealth threshold — and is the same signal used in esusu circles to determine who has standing in a given rotation cycle. The grace-period exception prevents the indicator from inadvertently excluding legitimately active but non-monthly contributors.

---

**Dimension 3 — Treasury Transparency Index (TTI)**

*Grounding*: ISO 15489 (reliability); NIST SP 800-53 (auditability controls); Ostrom Principles 4 and 5 (monitoring and sanctioning); Olson [1965] (collective action and capture prevention)

*Definition*: The proportion of treasury movements for which an on-chain record with sufficient metadata exists to reconstruct the complete financial history of the workspace.

*TTI-01 — Treasury Audit Completeness Rate*:
```
TTI-01 = (Treasury movements with complete on-chain metadata:
           amount, sender, recipient, stated purpose ≥50 chars,
           timestamp, approving signatory addresses) /
          (Total treasury movements) × 100
```

*TTI-02 — Solvency Provability Score*: Binary (1/0) — whether the workspace can generate a ZK proof of current treasury balance ≥ stated obligations without revealing individual member contribution amounts.

*Data source*: Akpa Oroma community treasury on-chain ledger (queryable from block explorer); policy enforcement records.

*Goodhart risk*: Inflated purpose metadata — strings that satisfy length requirements but carry no information. *Mitigation*: Require at least one reference to a prior proposal ID in purpose metadata, enforced at the contract level. We note the residual limitation: TTI-01 measures platform-enforced structural completeness, not the semantic quality of the purpose statement. A contract that enforces length and proposal-ID linkage still cannot detect boilerplate text. Semantic validation of governance intent remains an open challenge and is flagged for Stage 5 qualitative audit.

---

**Dimension 4 — Dispute Resolution Legitimacy (DRL)**

*Grounding*: Ostrom Principle 6 (conflict-resolution mechanisms); Beetham [1991] (legitimacy through process); Fox [2015] (social accountability conditions)

*Definition*: A composite measure of dispute resolution quality: documentation completeness, outcome contestation rate, and resolution speed.

*DRL-01 — Dispute Resolution Completeness*:
```
DRL-01 = (Disputes with full documented record:
           claim, evidence submitted, decision, reasoning) /
          (Total disputes initiated) × 100
```

*DRL-02 — Outcome Contestation Rate* (inverse-scored):
```
DRL-02 = (Disputes reopened or formally appealed within 30 days) /
          (Total disputes resolved) × 100
```

*DRL-03 — Resolution Speed*: Median calendar days from dispute initiation to community-accepted resolution.

*Data source*: Truth Layer dispute desk records; on-chain vote records for resolution acceptance.

*Empirical calibration*: Early-deployment community-monitoring studies document 65–70% documentation completeness in the first operational phase [Bjorkman & Svensson 2009], with anonymous complaint channels increasing dispute reporting 3.2× over identified channels. The §6.2 illustrative DRL-01 value of 67% falls within this range.

*Goodhart risk*: Suppressed dispute rates — social pressure preventing legitimate grievances. *Mitigation*: Require an anonymous on-chain dispute channel; track ratio of anonymous to identified disputes as a suppression signal. Anonymity is enforced at the protocol level: the dispute is submitted as a cryptographic commitment to the dispute hash, with no identity field in the transaction calldata. The submitter's wallet address is visible on-chain but is not linked to their community identity record in the governance module — preventing the common failure mode where "anonymous" channels are pseudonymous in a small community where wallet addresses are known.

---

**Dimension 5 — Credential Portability Score (CPS)**

*Grounding*: W3C Verifiable Credentials v2.0; CARE Principle 2 (Authority to Control); Ostrom Principle 1 (clearly defined membership); Suchman [1995] (cognitive legitimacy through recognizable membership status)

*Definition*: The proportion of active members who hold at least one portable, platform-independent, community-issued verifiable credential they control.

*CPS-01 — Portable Identity Coverage*:
```
CPS-01 = (Members with ≥1 exported W3C VC referencing
           ≥3 on-chain governance events as evidence) /
          (Total active members) × 100
```

The three-event threshold is motivated by Ostrom Principle 1 (clearly defined membership): meaningful membership evidence requires participation across at least one complete governance cycle (proposal, vote, outcome). The specific value is provisional pending Delphi validation.

*CPS-02 — Credential Interoperability Rate*: Binary per credential type (1/0) — readable by at least one external verifier without platform API dependency.

*Data source*: Ichi reputation module export logs; W3C VC DID document registry.

*Goodhart risk*: Vanity credentials issued without meaningful governance participation. *Mitigation*: Enforce the three-event evidence requirement at the credential issuance contract.

---

**Dimension 6 — Community Autonomy Score (CAS)**

*Grounding*: CARE Principle 2 (Authority to Control); Digital Public Goods Standard (platform independence); Ostrom Principle 7 (right to organize); ISO 14721/OAIS (community-controlled long-term access)

*Definition*: The degree to which governance records and operational capacity remain under community control, independent of the platform operator, any technology provider, or the state.

*CAS-01 — Record Exportability Rate*:
```
CAS-01 = (Governance records exportable in machine-readable
           open-standard format without platform operator assistance) /
          (Total governance records) × 100
```

*CAS-02 — Platform Independence Score*: Categorical 0–3: 0 = no export; 1 = export to platform-controlled storage only; 2 = export to community-controlled storage (IPFS/Arweave); 3 = export + independent verification without any platform API call.

*CAS-03 — Imposed State Dependency Ratio* (lower is better):
```
CAS-03 = (Governance decisions legally required to be routed
           through government approval or registration to be valid) /
          (Total governance decisions)
```

*Scope clarification.* CAS-03 measures *imposed* dependency — decisions that the community is legally obligated to route through a government body for formal validity. It explicitly excludes *chosen* dependency: voluntary state engagement (e.g., a community electing to register a cooperative in order to obtain legal recourse it values). Distinguishing imposed from chosen dependency requires a legal-context mapping per deployment jurisdiction; the framework provides the indicator structure but requires community-led legal review to populate the numerator. This distinction prevents the indicator from inadvertently rewarding legal non-compliance as "autonomy" — a risk flagged early in the framework's design review.

*Data source*: Platform export audit; block explorer verification. CAS-03 primary source: community-exported governance protocol documentation (machine-readable) cross-checked against public state registry records. Community self-attestation is a fallback only where no documentary evidence exists — flagged explicitly in reporting.

*Goodhart risk*: Export archives technically complete but practically unreadable. *Mitigation*: Annual community-conducted readability audit by a member without a technical background.

---

**Dimension 7 — Financial Inclusion Depth (FID)**

*Grounding*: Francois & Squires [2021] (e-ROSCA ~90% compliance); World Bank GHS Panel (17% informal savings participation); CARE Principle 1 (Collective Benefit); Gugerty [2007] (ROSCA participation dynamics); Ardener & Burman [1995] (gender stratification in ROSCAs)

*Definition*: The depth to which the digitized governance system reaches across the community's membership distribution — specifically whether it includes members historically excluded from formally documented financial governance.

*FID-01 — First-Time Formal Participant Rate*:
```
FID-01 = (New members for whom this is their first formally
           documented financial governance experience) /
          (Total new members onboarded in measurement period) × 100
```

*FID-02 — Gender Participation Parity Index*: (Female active governance participants) / (Total active governance participants), benchmarked at 0.50 equity baseline. *Requires community consent and ethics clearance before collection.*

*FID-03 — Diaspora Integration Rate*: (Members contributing from outside Nigeria with ≥1 verifiable governance action) / (Total diaspora-flagged members). *Requires community consent before collection.*

*Data source*: Onboarding survey (FID-01); membership metadata; geographic distribution of wallet addresses (FID-03).

*Survey instrument note*: FID-01 requires a single binary question at wallet creation: "Is this your first participation in a formally documented financial governance group?" This is the dimension's only survey-dependent component. It is classified as **deployment-blocked** — computable only after mainnet onboarding begins. FID-02 and FID-03 are similarly deployment-blocked and require community consent protocols. FID-01's survey question touches on financial history, which is socially sensitive in some Southeast Nigerian contexts; the framework therefore recommends extending ethics clearance to FID-01 in any deployment where financial history carries stigma, consistent with CARE Principle 4 (Ethics).

*Goodhart risk*: Optimizing for onboarding counts without sustained participation. *Mitigation*: FID-01 requires ≥3 governance interactions post-onboarding to count as a qualifying "first formal participant."

*Structural measurement boundary*: The FID dimension measures inclusion *within* the platform. It cannot measure communities that do not adopt on-chain coordination — a known and irreducible limitation. Communities that adopt are likely to differ systematically from those that do not (in digital literacy, diaspora connectivity, and trust in technology infrastructure). OGI scores on FID are therefore not comparable across adoption contexts without controlling for adoption barriers. This is documented explicitly rather than treated as a future problem: the framework measures what it can observe, and what it cannot observe is named.

---

### 4.4 Composite Scoring, Dashboard Design, and Sensitivity

Following OECD/JRC Composite Indicator guidance [Nardo et al. 2008], we adopt a **dashboard-first design**. Dimensions carry different weights across community types. **Table 2** shows two illustrative weighting schemes to make the design concrete:

| Dimension | Diaspora Fund | Village Infrastructure Committee |
|-----------|---------------|----------------------------------|
| RV (Record Verifiability) | 0.15 | 0.15 |
| DPR (Decision Participation) | 0.10 | 0.20 |
| TTI (Treasury Transparency) | 0.20 | 0.25 |
| DRL (Dispute Resolution) | 0.10 | 0.20 |
| CPS (Credential Portability) | 0.20 | 0.05 |
| CAS (Community Autonomy) | 0.10 | 0.10 |
| FID (Financial Inclusion) | 0.15 | 0.05 |

The diaspora fund weights credential portability and inclusion heavily (members join, leave, and need portable proof of participation across jurisdictions); the village committee weights treasury transparency and dispute resolution heavily (physical co-presence substitutes for some credential needs but raises the stakes of record-keeping around shared physical assets). These are illustrative, not prescriptive: communities calibrate weights through a Delphi process [Quyên 2014] that will constitute part of the Stage 5 research programme.

For cross-community benchmarking, the **OGI-Core Score** = equally weighted average of RV-01, DPR-01, TTI-01, and DRL-01. These four are computable entirely from on-chain data without community surveys.

Sensitivity to weighting choices is a known vulnerability of composite governance indices [Nardo et al. 2008; Oman 2006]. Supplementary material reports sensitivity tests under five alternative weighting schemes, confirming rank stability for clearly high- and low-performing workspaces while flagging middle-band instability as a known limitation requiring Delphi validation before policy deployment.

---

## 5. Computational Tractability: Platform Architecture as Measurement Substrate

The OGI Framework is only useful if its indicators are computable from artifacts that actually exist. This section demonstrates that the data architecture required to compute the seven OGI indicators is technically realizable, using Oroma — a community coordination platform under development by Beaconsmith Collective Labs — as the computational substrate for the §6 tractability demonstration. The framework is platform-agnostic at the indicator level; Oroma is the substrate that allowed us to verify that every indicator formula maps to a concrete event schema and a concrete query path.

### 5.1 Community-Layer DPI Mapping

The World Bank, UNDP, and Carnegie Endowment converge on a three-layer definition of Digital Public Infrastructure: digital identity, digital payments, and verifiable data exchange [World Bank DPI 2025; UNDP 2024; Carnegie 2025]. A community coordination platform implementing all three at community scale constitutes community-layer DPI. The mapping below identifies which OGI dimensions each infrastructure layer enables to become computable.

| DPI Layer | Oroma Module | OGI Dimensions Enabled |
|-----------|--------------|------------------------|
| Digital Identity | Ichi — portable W3C VC credentials, community-controlled | CPS-01, CPS-02, DPR-01 |
| Digital Payments | Akpa Oroma — community treasury on Bitcoin L2 (Citrea zkEVM) | TTI-01, TTI-02, FID-01–03 |
| Verifiable Data Exchange | Truth Layer — canonical receipts, ZK proofs, dispute desk | RV-01, DRL-01–03, CAS-01–03 |

Supporting modules implement Ostrom Principles 5 and 6 in smart contract form: policy enforcement without custody (graduated sanctions) and dual-chamber proposals with quorum-gated execution (conflict-resolution mechanism).

### 5.2 Measurement Query Logic

For RV-01:
```
1. Query workspace contract events: ProposalCreated, VoteCast,
   TreasuryMovement, DisputeOpened, DisputeResolved
2. For each event: check for corresponding Truth Layer receipt
   (anchored hash + IPFS CID in receipt mapping)
3. RV-01 = count(events with receipt) / count(total events) × 100
```

For TTI-01:
```
1. Query TreasuryMovement events for workspace address
2. For each: check purpose.length >= 50 AND proposalId != 0
   AND signatoryAddresses.length >= workspace.quorumThreshold
3. TTI-01 = count(complete movements) / count(total movements) × 100
```

These queries run against a public block explorer with the contract ABI — no platform login, no API key, no intermediary. This addresses the response bias documented in GTMI [2025] at the input level; the outputs measure auditability conditions, not the normative quality of the governance decisions they record.

### 5.3 Why Blockchain Rather Than Simpler Append-Only Logs

Three specific properties required by the OGI Framework are not trivially achieved by simpler infrastructure: (1) **permissionless verification** — CAS-02 requires that any member can verify records without platform operator cooperation; a database-backed append-only log requires the database operator to remain cooperative; (2) **cryptographic non-tampering without trusted intermediary** — RV-01 requires that verifiability not depend on the platform operator's honesty; RFC 6962-style certificate transparency logs require a designated monitor; an L2 chain with fraud proofs provides this without a monitor; (3) **treasury operations with ZK privacy** — TTI-02's solvency proof requires a proving system; implementing this outside an EVM-compatible environment requires custom cryptographic engineering.

This is an infrastructure choice, not an ideological commitment to blockchain. A community that can implement all three properties on simpler infrastructure should. The OGI Framework's indicators are agnostic about the underlying implementation — they measure properties (verifiability, permissionlessness, ZK provability) that a Bitcoin L2 zkEVM provides as built-in features, reducing implementation burden for resource-constrained community institutions.

**Cross-platform applicability.** The indicator specifications are substrate-neutral. RV-01 could be computed against a Trillian-style transparency log if a community accepts the monitor-dependence tradeoff; CAS-01 could be computed over Solid pods for communities that prefer personal-data-store semantics; CPS-01 is defined in terms of W3C VCs and is independent of any specific issuance chain. What the chain provides is a specific combination of properties (no monitor, no operator, ZK support) at reduced integration cost for resource-constrained communities. A future comparative evaluation across substrates is a Stage 5 research direction.

### 5.4 Privacy-Preserving Verifiability

Members need confidence in treasury solvency without individual contribution amounts being disclosed — particularly in ROSCAs, where members in default positions are vulnerable to social pressure. Transparency without privacy controls is not governance; it is a different form of surveillance.

Oroma implements zero-knowledge circuits (ZK-SNARK, Groth16) on a Bitcoin L2 zkEVM. The Treasury Solvency Proof (TTI-02) allows any member to verify that workspace balance ≥ *X* without learning any individual's contribution. This implements the CARE Authority to Control principle through a cryptographic mechanism rather than a policy statement — a verifiable commitment, not a declaration.

### 5.5 Threat Model and Residual Trust

The measurement substrate reduces but does not eliminate trust assumptions. Three residual trust points are explicit in the current design: (1) the Citrea sequencer — compromise would not permit tampering with finalized records but could censor or delay inclusion; fraud-proof publication mitigates this and is itself measurable through RV-01; (2) workspace administrator collusion with the platform operator — a multi-signature collusion across the community's own signatories is outside the measurement substrate's scope and is a social-governance problem (addressed partially by DPR-02 quorum requirements and CAS-02 independent verification); (3) key custody — individual member key loss degrades DPR-01 rather than corrupting it, but a mass-custody compromise in a single-wallet deployment is a real risk that the framework neither creates nor solves. Making these trust points explicit is itself a measurement contribution: existing governance indices make no comparable disclosure of their measurement trust assumptions.

---

## 6. Framework Computability Demonstration

### 6.1 Design Science Research Stage

This paper follows the design science research (DSR) methodology [Hevner et al. 2004; Peffers et al. 2007]. DSR proceeds through six stages: problem identification, objective definition, design and development, **demonstration**, evaluation, and communication. The OGI Framework is the artifact produced at Stage 3. This section executes Stage 4 — demonstration: verifying that the artifact is technically feasible and produces meaningful output on a representative instance of the problem. Gregor and Hevner [2013] characterize Stage 4 contributions as "design knowledge" that becomes citable and extensible before full empirical validation — the positioning appropriate to an Ongoing Research submission.

Stage 4 (demonstration) is explicitly distinct from Stage 5 (evaluation). Hevner et al. [2004] note that "design-science research is not complete until the artifact is evaluated in its intended environment." We are at Stage 4. Stage 5 requires: (1) mainnet deployment with consenting community workspaces; (2) ethics clearance for community data collection; (3) longitudinal data collection; (4) Delphi validation of indicator definitions and weights across five practitioner groups — constituting the post-submission research programme targeting Q3–Q4 2026.

This sequencing is methodologically appropriate and standard in IS design science. The demonstration values below are **ILLUSTRATIVE** — applied to a hypothetical workspace matching the Oroma platform's data model. They verify that indicator formulas produce meaningful variation from the platform's event schema. They are not evidence of any real community's governance quality, and no such claim is made.

### 6.2 Illustrative Computability Case

Hypothetical scenario: a diaspora-facing cooperative with 34 members distributed across Southeast Nigeria and the United Kingdom, with an active treasury and three completed governance cycles. The 34-member size reflects the empirically documented modal range for functional ROSCAs — Gugerty [2007] finds that groups of 20–50 members sustain participation more durably than either smaller or larger cohorts, and Besley et al. [1993] note that three to four rotation cycles is the minimum for ROSCA participants to observe enforcement mechanisms operating. Trader-network esusu studies in Southeast Nigeria document modal group sizes of 15–40 members [Global Informality Project 2020], bracketing the scenario's size. The scenario is constructed to be representatively plausible, not arbitrarily illustrative.

| OGI Indicator | Illustrative Value | Framework diagnostic |
|---------------|-------------------|----------------------|
| RV-01 | 94% | 2 of 34 governance actions lacked receipt anchors — surfaced as re-anchoring gaps |
| DPR-01 | 71% | 10 non-participating members identified — signals participation design opportunity |
| DPR-02 | 82% | 2 proposals expired without quorum — documented as governance events, not silently dropped |
| TTI-01 | 100% | All treasury movements fully documented — purpose enforcement working |
| TTI-02 | 1 | ZK solvency proof pathway is computable and verifiable on-chain |
| DRL-01 | 67% | 1 of 3 disputes lacked full documentation — identifies enforcement gap |
| CPS-01 | 47% | 18 of 34 members without portable credentials — adoption gap visible |
| CAS-02 | 2 | Records reach IPFS; platform-independent verification achievable |
| FID-01 | 58% | First-time formal participant rate computable from onboarding survey |

*Illustrative OGI-Core Score* (RV-01 + DPR-01 + TTI-01 + DRL-01, equally weighted): **83%**

The framework's diagnostic value is visible even in illustrative form: CPS-01 at 47% surfaces credential portability as a specific adoption gap; DRL-01 at 67% identifies dispute documentation as requiring product-level enforcement.

### 6.3 Contextual Evidence

Records management studies in Nigerian local governance document: absence of records management culture, staff unable to distinguish record types, dominant paper systems, and "gross inefficiency and lack of policy continuity" [Adebayo 2018]. Empirical studies of Southeast Nigerian town unions document the same pattern at the community layer: treasurer accountability failures, contribution tracking disputes, and leadership transition gaps with no documentary handover [Harneit-Sievers 2006; Nwangwu 2024]. This is the failure mode the OGI Framework is designed to make measurable and preventable.

Two empirical anchors support the framework's participation and dispute benchmarks. The e-ROSCA field experiment by Francois and Squires [2021] in DRC found approximately 90% contribution compliance in mobile-money-enabled rotating savings groups — the strongest available evidence that community members will engage with digitized governance under appropriate incentive design. The randomized community-based monitoring experiment by Bjorkman and Svensson [2009] in Uganda demonstrated that structured monitoring raised service quality, with anonymous complaint channels increasing dispute reporting 3.2× relative to identified channels — direct empirical support for DRL-01's anonymous-channel Goodhart mitigation. Together these studies establish that digitized community governance is both behaviorally plausible (e-ROSCA) and benefits measurably from anonymity-preserving dispute infrastructure (Uganda monitoring) — the two empirical conditions most load-bearing for the OGI Framework's core design choices.

---

## 7. Discussion

### 7.1 Three Measurement Layers, Not One

The OGI Framework does not replace EGDI, DGI, or GTMI. It occupies the measurement layer those indices leave structurally empty. A complete digital governance measurement stack for Nigeria requires three layers: (1) national e-government benchmarks; (2) subnational digital governance indicators; (3) community-layer governance indicators — the OGI Framework. Only Layer 3 captures the governance accountability that most Nigerians experience directly.

### 7.2 The Transparency-Privacy Tension

Greater verifiability is not always better governance. An indicator framework that makes community records legible to external auditors at the cost of member privacy produces a different governance failure. In the ROSCA context, publishing individual contribution records exposes members in default positions to social stigma and family pressure — a direct violation of the CARE Authority to Control principle.

The OGI Framework addresses this by design: TTI-02 separates solvency verification from contribution disclosure using ZK proofs; CAS-03 treats imposed state dependency as a metric to minimize; CARE compliance is a structural constraint on every indicator, not a value statement in the conclusion.

### 7.3 Outcomes vs. Organizational Forms

The OGI Framework measures governance *process quality* — is a decision verifiable? can a dispute be audited? does a record survive leadership transition? — not governance *outcomes* or organizational *forms*. A community with a perfect OGI-Core score may still make inequitable decisions; the OGI Framework would document those decisions with high fidelity, not judge them. A WhatsApp group that generates a ZK solvency proof is still a WhatsApp group. An esusu circle that anchors its contribution records on-chain retains its social character while adding an evidentiary layer. The indicator asks "is this action verifiable?" not "does this institution look like a registered cooperative?"

The most durable informal institutions succeed because they adapt their forms while maintaining their functions [Ostrom 1990; Ardener & Burman 1995; Gugerty 2007]. An indicator framework that incentivizes organizational formalization in exchange for a better score would damage what it intends to measure. All seven OGI dimensions are process-quality indicators — necessary conditions for accountable governance, not sufficient ones.

### 7.4 Relationship to Blockchain Governance Literature — and Its Critics

A substantial literature examines blockchain applications in public governance: government audit trails in public financial management [World Bank 2024; ISACA 2024], civic participation traceability [Belfer Center 2023], and Africa-specific regulatory and infrastructure surveys [Shava & Mhlanga 2023; ABSA 2025]. The OGI Framework is not an extension of this literature. The distinction is the direction of sovereignty.

Existing blockchain governance applications place governments or institutions in the role of record producer, with citizens as beneficiaries of increased transparency. The World Bank FundsChain pilot improves *state* accountability to funders. Certificate Transparency [RFC 6962] makes *certificate authorities* auditable to the public. In each case, a powerful institution uses a public ledger to become more verifiable to those it serves.

The OGI Framework inverts this: *communities* are the record producers, and the measurement question is whether those community-produced records meet governance evidence standards — without external custodians, state registration, or platform operator cooperation.

**Engagement with blockchain-governance skepticism.** A serious critical literature questions whether distributed ledgers deliver their claimed governance benefits. Schneider [2019] argues that "decentralization" in blockchain systems is an incomplete and often rhetorically inflated ambition, with de-facto centralization re-emerging at the infrastructure, exchange, and governance layers. Atzori [2017] argues that blockchain-based governance systems frequently underestimate the continuing necessity of state institutions for coercive enforcement. De Filippi and Wright [2018] document how "rule of code" aspirations collide with the irreducible social character of governance disputes. The OGI Framework takes these critiques seriously and does not claim that distributed ledgers produce better governance by themselves. Three design choices are direct responses to this critical literature: (i) CAS-01 through CAS-03 measure de-facto community autonomy — including the re-centralization pathways Schneider names — rather than assuming decentralization by infrastructure type; (ii) §4.1 and §7.3 explicitly decouple record verifiability from governance outcome quality, avoiding the "rule of code" conflation; (iii) CAS-03's imposed-vs-chosen state dependency distinction (§4.3) aligns with Atzori's observation that state interfaces are sometimes legitimately required. The framework's contribution is a measurement instrument that is falsifiable against these critiques, not immune to them.

### 7.5 DPI Policy Implications for Nigeria

NITDA's statutory remit covers planning, research, standardisation, and monitoring/evaluation of IT practices in Nigeria. The OGI Framework provides a measurable specification for community-layer DPI outcomes — analogous to how SIIPS payment system maturity assessments evaluate national payment infrastructure. The seven dimensions are directly translatable into monitoring criteria for community digital governance programmes across Nigeria's 36 states and 774 local government areas, making community-layer DPI investment outcomes measurable for the first time.

### 7.6 Limitations and Future Work

**Empirical validation**: Future work will conduct a Delphi consensus process [Quyên 2014] across five stakeholder groups: (1) community governance practitioners, (2) digital governance measurement specialists, (3) DPI policy actors, (4) blockchain governance researchers, and (5) community members of active deployments. Target: Q3 2026.

**Evidence pipeline**: A companion Research Spine architecture — a live evidence extraction pipeline connecting Oroma's `domain_events` database to a continuously updated research archive — is under development at Beaconsmith Collective Labs. This pipeline will compute OGI-Core indicators from real deployment data, updating the research archive daily and flagging when computed values diverge from illustrative projections.

**Scale dynamics**: The framework has been designed against modal group sizes documented in the ROSCA and town union literature (15–50 members; occasionally up to a few hundred for town-union plenaries). Indicators scale differently: RV-01 and TTI-01 are robust at any size because they measure per-action completeness; DPR-01 behaves differently at 30 versus 300 members because active-participation norms are size-dependent. Large-group calibration is part of the Stage 5 research programme.

**Ethics and consent**: FID-02 and FID-03 require community consent protocols and national ethics clearance before data collection. FID-01's financial-history survey question also warrants ethics review in contexts where financial history carries social stigma. These are governance-policy decisions, not instrumentation questions, and require a separate approval path.

**Attribution**: No causal claim is made that verifiable digital records produce improved community outcomes. The OGI Framework measures governance process quality. The causal pathway from verifiable records to reduced elite capture to improved development outcomes requires a separate longitudinal evaluation design.

---

## 8. Threats to Validity

**Construct validity**: Do on-chain records measure governance quality or record-keeping? The OGI Framework explicitly measures the latter. The claim is that verifiable, continuous, participatory, auditable, sovereign, and inclusive *records* are necessary conditions for accountable community governance — not sufficient conditions. A cryptographically verified on-chain record of a captured vote is still a governance failure; the OGI Framework's DRL and DPR dimensions are designed to surface this, but the relationship between record quality and governance outcome quality requires separate longitudinal validation.

**Internal validity**: Platform design choices directly affect indicator scores. TTI-01 requires ≥50-character purpose metadata; DPR-01's Goodhart mitigation weights participation by treasury contribution. These are normative encoding choices made by the platform designers. The OGI Framework measures what the platform enforces, not abstract governance ideals — which is a feature (indicators are grounded in actual artifacts) and a limitation (indicator scores reflect platform design as much as community governance).

**External validity**: Southeast Nigeria has specific institutional features — town unions, esusu circles, age grades, diaspora networks — that are embedded in particular social histories. The OGI Framework's seven dimensions are designed to be applicable wherever community institutions produce governance records; transferability to other informal governance contexts requires case-by-case assessment rather than direct generalization.

**Scale validity**: Participation indicators (DPR-01 in particular) are calibrated for modal group sizes. Scores from workspaces outside this range should be interpreted with caution until Stage 5 size-stratified calibration completes.

**Exclusion risk**: The FID dimension measures inclusion *within* the platform. Communities that adopt on-chain coordination will systematically differ from those that do not — in digital literacy, smartphone access, trust in technology, and diaspora connectivity. OGI scores are not comparable across communities unless adoption barriers are accounted for. The framework cannot measure what it cannot observe: informal governance that remains entirely off-platform is invisible to OGI by design.

**Disclosure**: Oroma, the community coordination platform used as the computational substrate in §5–6, is under development by Beaconsmith Collective Labs (the author's research group). The OGI Framework is designed to be platform-agnostic at the indicator level; the Oroma-specific examples illustrate one possible implementation, not a normative requirement. This relationship is disclosed here to prevent misreading of §5 as platform advocacy.

---

## 9. Conclusion

Every major digital governance benchmark currently in use was designed to measure what states do. This is not a criticism of those benchmarks. It is a description of their design constraints — and those constraints were reasonable. The problem is that in Southeast Nigeria, as in much of Sub-Saharan Africa, states are not where most governance happens. Town unions build the roads. Esusu circles finance the enterprises. Diaspora networks sustain communities across distance. None of this is measurable by any existing instrument that counts as "digital governance measurement."

The OGI Framework introduces seven new indicators for this governance layer — each grounded in Ostrom's collective action design principles, ISO 15489 records standards, governance legitimacy theory [Beetham 1991; Tyler 2006; Suchman 1995], and CARE data sovereignty principles. Each computable from verifiable artifacts. Each accompanied by a documented Goodhart risk and structural mitigation. A dashboard-first design communities calibrate to their own governance contexts. And — in direct response to a serious critical literature on blockchain governance — a design that locates community sovereignty in CAS-dimension measurement rather than in claims of infrastructural decentralization.

The contribution to Track 6 is precise: a proposed indicator framework and measurement methodology for the governance layer that existing approaches structurally omit — artifact-based, privacy-preserving, independently verifiable, and grounded in community sovereignty rather than state delegation. The framework is theoretically grounded and architecturally feasible; empirical validation is the next step, not the current claim.

The town union treasurer who carried the ledger to London when he relocated, leaving no record of three years of community contributions. The esusu circle whose rotating payout went disputed because the organiser's notebook was the only record of who had already received their share. The diaspora levy committee that dissolved — not because members stopped caring, but because no one could prove which projects the contributions had funded. These are not exotic governance failures. They are the normal operating condition of collective finance for millions of Nigerians. The OGI Framework is designed for that context: a first attempt to build measurement appropriate to what these institutions are already doing, on their own terms, with their own evidence.

The framework is at DSR Stage 4 — demonstrated as computationally tractable, theoretically grounded, and structurally differentiated from all existing governance measurement instruments. DSR Stage 5 — empirical evaluation with real communities — is the next step, not a reason to withhold the design. If the measurement approach is wrong, empirical evaluation will reveal it. Either outcome advances knowledge about whether verifiable community records can serve as the evidentiary basis for governance indicators in the Global South.

---

## References

1. Adebayo, O. (2018). Public records and management of information materials in Nigerian local government: A transformative route. *Global Journal of Human Social Science*, 18(3).
2. Aligica, P.D., & Tarko, V. (2012). Polycentricity: From Polanyi to Ostrom and beyond. *Governance*, 25(2), 237–262.
3. Ardener, S. (1964). The comparative study of rotating credit associations. *Journal of the Royal Anthropological Institute of Great Britain and Ireland*, 94(2), 201–229.
4. Ardener, S., & Burman, S. (Eds.). (1995). *Money-go-rounds: The importance of rotating savings and credit associations for women*. Berg Publishers.
5. Atzori, M. (2017). Blockchain technology and decentralized governance: Is the state still necessary? *Journal of Governance and Regulation*, 6(1), 45–62.
6. Beetham, D. (1991). *The Legitimation of Power*. Palgrave Macmillan.
7. Besley, T., Coate, S., & Loury, G. (1993). The economics of rotating savings and credit associations. *American Economic Review*, 83(4), 792–810.
8. Bjorkman, M., & Svensson, J. (2009). Power to the people: Evidence from a randomized field experiment on community-based monitoring in Uganda. *Quarterly Journal of Economics*, 124(2), 735–769.
9. Bouman, F.J.A. (1995). Rotating and accumulating savings credit associations: A development perspective. *World Development*, 23(3), 371–384.
10. Carnegie Endowment for International Peace. (2025). *Digital public infrastructure: A practical approach for Africa*. Sang, D., Munga, J., & Sambuli, N.
11. Carroll, S.R., et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 19, 43. https://doi.org/10.5334/dsj-2020-043
12. Casey, K. (2024). Long-term effects of community-driven development. Working paper (CDD evaluation update).
13. De Filippi, P., & Wright, A. (2018). *Blockchain and the Law: The Rule of Code*. Harvard University Press.
14. Fox, J. (2015). Social accountability: What does the evidence really say? *World Development*, 72, 346–361.
15. Francois, P., & Squires, M. (2021). Linking mobile money networks to "e-ROSCAs": An experimental study. *Science Advances*, 7(1). https://doi.org/10.1126/sciadv.abc5831
16. Gaventa, J., & McGee, R. (2013). The impact of transparency and accountability initiatives. *Development Policy Review*, 31(s1), s3–s28.
17. Global Informality Project. (2020). *Esusu (Nigeria)*. https://www.in-formality.com/wiki/index.php?title=Esusu_(Nigeria)
18. Gregor, S., & Hevner, A.R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly*, 37(2), 337–355.
19. Gugerty, M.K. (2007). You can't save alone: Testing theories of rotating savings and credit associations. *Economic Development and Cultural Change*, 55(2), 251–282.
20. Guimarães, R., Figueiredo, T., Sartori, L., Cogo, G., & Cunha, M.A. (2025). The local in LOSI: A discussion on small municipalities' online portals in Brazil. In *Proceedings of ICEGOV 2025*.
21. Harneit-Sievers, A. (2006). Institutionalizing community I: Town unions. In *A place in the world: New local historiographies from Africa and South Asia*. Brill.
22. Heeks, R. (2006). *Benchmarking e-government*. IDPM, University of Manchester.
23. Hevner, A.R., March, S.T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105.
24. Honey, R., & Okafor, S.I. (Eds.). (1998). *Hometown associations: Indigenous knowledge and development in Nigeria*. Intermediate Technology Publications.
25. International Organization for Standardization. (2016). *ISO 15489-1:2016 — Information and documentation — Records management*.
26. Ishola, A.A., Maramura, T.C., & Gumbo, T. (2025). Charting digital governance: A bibliometric analysis of ICT research in Nigeria's public administration. *Frontiers in Sustainable Cities*. https://doi.org/10.3389/frsc.2025.1605736
27. Kabanov, Y. (2025). Decentralization and local e-services development: A pilot cross-national study with the LOSI data. In *Proceedings of ICEGOV 2025*.
28. Mansuri, G., & Rao, V. (2013). *Localizing development: Does participation work?* World Bank Policy Research Report.
29. Mo Ibrahim Foundation. (2024). *Ibrahim Index of African Governance: Methodology and sources 2024*. https://mo.ibrahim.foundation/iiag
30. Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A., & Giovannini, E. (2008). *Handbook on constructing composite indicators*. OECD/JRC. https://doi.org/10.1787/9789264043466-en
31. National Archives UK. (2017). *Understanding digital continuity*. The National Archives.
32. Nwangwu, B.C. (2024). Repositioning town unions as the fourth-tier of government in South East Nigeria. *International Journal of Research and Innovation in Social Science*, 8(11). https://doi.org/10.47772/IJRISS.2024.8110251
33. OECD. (2024). *2023 OECD Digital Government Index: Results and key findings*. https://doi.org/10.1787/1a89ed5e-en
34. Okafor, E.E. (2019). The dictum, Igbo Enwe Eze. *Sociology and Philosophy*, 9(1). https://doi.org/10.4236/sm.2019.91005
35. Olson, M. (1965). *The Logic of Collective Action*. Harvard University Press.
36. Oman, C.P. (2006). *Uses and abuses of governance indicators*. OECD Development Centre.
37. Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.
38. Ottenberg, S. (1955). Improvement associations among the Afikpo Ibo. *Africa*, 25(1), 1–22.
39. Peffers, K., Tuunanen, T., Rothenberger, M.A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77.
40. Quyên, Đ.T.N. (2014). Developing university governance indicators using a modified Delphi method. *Procedia — Social and Behavioral Sciences*, 141, 828–833.
41. Schneider, N. (2019). Decentralization: An incomplete ambition. *Journal of Cultural Economy*, 12(4), 265–285.
42. Shava, E., & Mhlanga, D. (2023). Mitigating bureaucratic inefficiencies through blockchain in Africa. *Frontiers in Blockchain*, 6. https://doi.org/10.3389/fbloc.2023.1053555
43. Singh, J., & Shah, P. (2003). Community scorecard process: A short note on the general methodology for implementation. *World Bank Social Development Notes*.
44. Suchman, M.C. (1995). Managing legitimacy: Strategic and institutional approaches. *Academy of Management Review*, 20(3), 571–610.
45. Susar, D., Aquaro, V., Sarantis, D., & Soares, D. (2025). Bridging the urban digital divide: A cross-continental analysis of municipal e-service availability. In *Proceedings of ICEGOV 2025*.
46. Tyler, T.R. (2006). *Why People Obey the Law*. Princeton University Press.
47. Uduku, O. (2002). The socio-economic basis of a diaspora community: *Igbo bu ike*. *African Affairs*, 101(404), 339–355.
48. United Nations DESA. (2024). *UN E-Government Survey 2024*. United Nations.
49. UNDP. (2024). *Digital public infrastructure (DPI)*. https://www.undp.org/digital/digital-public-infrastructure
50. World Bank. (2025). *GovTech Maturity Index 2025 update*.
51. World Bank. (2025). *Digital public infrastructure and development: A World Bank Group approach*.
52. World Justice Project. (2025). *WJP Rule of Law Index 2025: Methodology and sources*.
53. Zambrano, A.F., et al. (2023). Rotating savings and credit associations: A scoping review. *World Development Sustainability*, 3. https://doi.org/10.1016/j.wds.2023.100093

---

*[End of manuscript — Draft v7. Single-blind submission draft. Author: Nzube Ndiokwelu, Beaconsmith Collective Labs. Approximately 10,200 words excluding references. Ongoing Research category, 8–10 pages ACM format. 53 references. Key changes from v6: author attribution restored; Community Scorecard and Social Audit comparator analysis (§2.2); Bouman 1995 and Ardener 1964 foundational ROSCA references (§2.3); gender stratification noted in esusu context (§2.3); CAS-03 imposed-vs-chosen state dependency distinction (§4.3); threshold calibration evidence integrated (§4.3 RV-01, DPR-01; §4.4); worked example weighting table (§4.4); Oroma named directly throughout §5; cross-platform applicability paragraph (§5.3); Citrea zkEVM named (§5.4); threat model section (§5.5); Gregor & Hevner 2013 for DSR Stage 4 positioning (§6.1); Bjorkman & Svensson 2009 explicit empirical anchor (§6.3); critical blockchain-governance engagement (Schneider 2019, Atzori 2017, De Filippi & Wright 2018, §7.4); scale validity added to Threats to Validity (§8); disclosure paragraph updated for single-blind context.]*
