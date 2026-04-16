# Measuring What States Miss: An Indicator Framework for Community-Led Digital Governance in Southeast Nigeria

**Track 6: New Metrics and Approaches for Measuring Digital Governance Success**
**Category: Ongoing Research Paper (8–10 pages)**
**ICEGOV 2026 — Riyadh, Saudi Arabia**

> *[Author information removed for double-blind review]*

---

## Abstract

The dominant digital governance indices — EGDI, OECD DGI, GTMI — share a structural blind spot: they measure what states do, using state-generated data. They cannot capture the governance quality of the community institutions — town unions, rotating savings circles (esusu/ajo), diaspora cooperatives — that constitute de-facto governance infrastructure for the majority of Nigerians and hundreds of millions across Sub-Saharan Africa. This measurement gap is not incidental; it is a consequence of design. No existing benchmark operationalizes whether community decisions are verifiable, whether treasury records survive leadership transitions, or whether dispute resolutions are documented and legitimate. This paper introduces the **Oroma Governance Indicator (OGI) Framework**: seven dimensions for measuring community-led digital governance success, grounded in ISO 15489 records management standards, Ostrom's collective action design principles, governance legitimacy theory, and CARE data sovereignty principles. Each dimension specifies a measurable indicator, an observable artifact or on-chain event as data source, and a documented Goodhart risk with mitigation. The framework is operationalized through a Bitcoin Layer 2 community coordination platform under active development in Southeast Nigeria. Following a design science research approach, we demonstrate the framework's computational tractability using the platform's data model. We argue that community-layer digital governance requires its own measurement language — and that this language is now theoretically grounded and technically feasible.

**Keywords:** digital governance indicators, community-led development, Southeast Nigeria, verifiable records, DPI, informal governance, ROSCA, composite indicators

---

## 1. Introduction

The phrase *Igbo enwe eze* — "Igbo have no king" — describes a political tradition in Southeast Nigeria that is not an absence of governance but a different architecture of it [Okafor 2019]. Governance in Igboland has always been distributed: through town unions that self-finance roads and schools, through esusu circles that capitalize enterprise without banks, through age grades and diaspora networks that sustain home communities across distance [Harneit-Sievers 2006; Ottenberg 1955]. When Nigeria's federal government distributed COVID-19 relief palliatives in 2020, only 4.9% of Nigerian households received any assistance, while warehouse looting by politically-connected actors was documented across multiple states [Nwangwu 2024]. Town unions had the community knowledge and trust networks to distribute more effectively. What they lacked was a verifiable record system — decisions made on WhatsApp disappeared, funds moved on social trust alone, and no audit trail existed when disputes arose.

This paper's core argument is not that community governance is broken. It is that the *measurement* of community governance is broken — and that this measurement failure has consequences for how digital governance success is defined, funded, and evaluated across Africa.

The UN E-Government Development Index (EGDI), the OECD Digital Government Index (DGI), and the World Bank GovTech Maturity Index (GTMI) together constitute the authoritative vocabulary for "digital governance success." None was designed to measure governance quality below the state level. Africa's average EGDI score is 0.4247 [UN EGov 2024] — a number that tells us nothing about whether the town union treasurer in Afikpo can be held accountable, whether the diaspora community fund in Enugu can produce an auditable receipt, or whether the esusu circle that financed a member's business can prove the loan terms were honoured.

Polycentric governance theory holds that self-organizing community institutions — operating alongside and independently of state structures — constitute legitimate governance actors in their own right, capable of managing collective resources through their own rules, monitoring, and sanctions [Ostrom 1990; Aligica & Tarko 2012]. Making this proposition measurable in the digital domain is the contribution of this paper.

We propose the **Oroma Governance Indicator (OGI) Framework**: a seven-dimension indicator set with three contributions:

1. **A documented measurement gap** — demonstrating, from the construction logic of existing indices, what they structurally cannot capture about community-led governance.

2. **A theoretical foundation** — synthesizing Ostrom's collective action design principles, ISO 15489 records management standards, governance legitimacy theory [Beetham 1991; Tyler 2006; Suchman 1995], and CARE data sovereignty principles into a coherent measurement ontology.

3. **An operationalized and computable indicator set** — seven dimensions, each with a definition, computable formula, on-chain or artifact-based data source, and documented Goodhart risk, demonstrated as tractable using a Bitcoin L2 community coordination platform's data architecture.

---

## 2. Background and Related Work

### 2.1 The Structural Limits of Existing Indices

The UN EGDI is computed as an equally weighted composite of the Online Services Index (OSI), Telecommunications Infrastructure Index (TII), and Human Capital Index (HCI) [UN EGov Survey 2024 Technical Appendix]. The OSI assesses national government portal feature presence; TII draws on ITU infrastructure penetration data; HCI draws on UNESCO education statistics. All three components are national-level, state-sourced, and capture service *availability* — not whether governance decisions within communities are recorded, verifiable, or durable.

The OECD DGI measures six dimensions of digital government maturity — Digital by design, Data-driven public sector, Government as a platform, Open by default, User-driven, Proactiveness [OECD DGI 2023] — across 38 countries, all OECD members or accession candidates. The World Bank GTMI covers 198 economies across four components (CGSI, PSDI, DCEI, GTEI), relying substantially on government self-reported survey responses [GTMI 2025]. The Worldwide Governance Indicators aggregate perceptions-based expert and business surveys [WGI 2025]. The Mo Ibrahim IIAG synthesizes 96 indicators from 49 external sources [IIAG 2024].

The pattern is consistent across all major frameworks: the WJP Rule of Law Index explicitly recognizes "Informal Justice" as a conceptual domain but *excludes it from aggregated scores* [WJP 2025]. Recognized, acknowledged, excluded. This is not carelessness — it is the design constraint that all major indices measure what states do, using data states produce. Community governance institutions are structurally invisible.

Heeks [2006] identified this as a "ranking obsession" that privileges legible state-layer governance over the informal institutions that constitute governance reality for much of the Global South. The observation is two decades old. The measurement gap remains.

### 2.2 Community-Led Development and Its Measurement Problem

A 3ie evidence synthesis of community-driven development (CDD) programs finds consistent gains in small-scale infrastructure but "little or no impact on social cohesion and governance" [3ie 2018]. Mansuri and Rao [2013] attribute this not to the absence of community capacity but to the absence of monitoring and evaluation systems capable of capturing governance quality: "induced participation is deeply shaped by context and political economy, and most projects fail for weak M&E systems that limit learning." The measurement failure precedes and produces the apparent governance failure.

The contribution of this paper to this literature: the measurement gap is now closeable. Blockchain-based community coordination platforms generate verifiable artifacts — on-chain receipts, cryptographic proofs of participation, immutable decision logs — that can serve as the evidentiary basis for governance indicators that do not rely on state self-reporting or expert perception surveys.

### 2.3 Southeast Nigeria as the Primary Context

Seventeen percent of Nigerian adults save in informal savings groups (adashi/esusu/ajo), according to World Bank General Household Survey Panel data. Rotating savings credit associations (ROSCAs) — in which members contribute fixed amounts at regular intervals, with each member receiving the pooled sum in rotation — operate on "an oath of allegiance and mutual trust" with no formal legal mechanism [Global Informality Project 2020; Besley, Coate & Loury 1993]. In some African nations, ROSCA membership among adults exceeds 95%.

In Southeast Nigeria, these financial governance mechanisms are embedded in a broader institutional ecology: town unions that self-finance public infrastructure and govern community affairs, age grade associations that execute development projects, diaspora networks that sustain home communities across geographic distance [Harneit-Sievers 2006; Honey & Okafor 1998; Uduku 2002]. Empirical studies of Nigerian local government records management document systematic failures of institutional memory — misplaced files, unwritten decisions, transitions that begin without any handover documentation [Adebayo 2018]. The governance challenge is not institutional capacity; it is institutional *legibility*. WhatsApp screenshots are the current record infrastructure. When a treasurer relocates, when a diaspora contributor demands accountability, when a dispute emerges over a prior decision, there is no verifiable audit trail.

---

## 3. Theoretical Framework

### 3.1 Ostrom's Design Principles as Measurement Anchors

Ostrom's eight design principles for robust common-pool resource governance [Ostrom 1990] identify the properties that distinguish durable community governance from fragile arrangements: clearly defined membership boundaries, rules matched to local conditions, collective-choice arrangements, monitoring of conditions and behavior, graduated sanctions, conflict-resolution mechanisms, recognition of rights to organize, and nested enterprises. We treat each principle as a measurement anchor: if a governance system exhibits the property, it should be detectable in records and artifacts. Where no artifact exists, the property is absent or unmeasured — both constitute governance failures of different kinds.

The literature on collective action adds a structural challenge that any community governance framework must address: institutions designed to serve all members can be captured by organized subgroups at the expense of the broader membership [Olson 1965]. Ostrom's Principles 4 (monitoring) and 5 (graduated sanctions) are specifically designed to make such capture harder. The OGI Framework measures not only participation rates but whether governance design imposes structural barriers against elite capture — through quorum requirements, multi-signature approvals, anonymous dispute channels, and privacy-preserving treasury verification that makes unilateral fund movement impossible.

### 3.2 Governance Legitimacy as the Outcome Variable

Political legitimacy theory provides the conceptual basis for what the OGI Framework is measuring. Beetham [1991] identifies three foundations of legitimate power: rule-governed exercise of power, justifiability of those rules by shared beliefs, and expressed consent by the governed. Tyler [2006] demonstrates empirically that compliance with institutional decisions depends primarily on perceived procedural fairness, not outcome favourability — a finding with direct implications for digital governance design. Suchman [1995] distinguishes pragmatic legitimacy (does it benefit members?), moral legitimacy (does it reflect community values?), and cognitive legitimacy (is it accepted as the natural way things work?) — distinctions that map onto the OGI Framework's measurable dimensions.

From this literature, five measurable conditions of governance legitimacy emerge: **continuity** (prior acceptance predicts future acceptance, which requires records of prior decisions); **fairness** (outcomes satisfy procedural justice norms, which requires transparent process documentation); **process** (legitimate procedures produce auditable outputs); **performance** (successful execution generates institutional confidence); and **participation** (members accept outcomes they helped shape, which requires verifiable participation records). These five conditions become the cross-cutting quality criteria applied across all seven OGI dimensions.

A governance system that processes transactions but cannot produce evidence of continuity, fairness, process, performance, or participation has not achieved legitimacy in any of these senses — regardless of how efficiently it moves funds.

### 3.3 Records as Governance Infrastructure

ISO 15489-1:2016 defines authoritative records as evidence when they possess: **authenticity** (the record is what it claims to be), **reliability** (it accurately represents the activity), **integrity** (it is complete and unaltered), and **usability** (it can be retrieved and interpreted) [ISO 15489 2016]. The National Archives' digital continuity framework [2017] adds the temporal dimension: continuity means information remains complete, available, and usable across transitions — leadership turnover, system migrations, funding gaps.

These four properties are necessary conditions for governance quality at the community layer. A governance system that makes decisions but cannot produce ISO 15489-quality evidence of those decisions is, in any measurable sense, not governing in a way that can be held accountable.

### 3.4 CARE Principles: Sovereignty Over Surveillance

The CARE Principles for Indigenous Data Governance [Carroll et al. 2020] — Collective Benefit, Authority to Control, Responsibility, Ethics — establish that community governance records must serve community purposes, that communities must control their own data governance protocols, and that data stewardship must embed community values. These principles resolve a tension the technical literature frequently obscures: more verifiability is not always better governance. An indicator framework that makes community records more legible to external auditors at the cost of member privacy or community autonomy produces a different kind of governance failure. The CARE Principles are incorporated into the OGI Framework as a constraint, not a value: indicators must be computable *without* requiring communities to expose records beyond the scope their own governance protocols authorize.

---

## 4. The Oroma Governance Indicator (OGI) Framework

### 4.1 Framework Design Logic

The OGI Framework operationalizes community governance success as the production of *governance records that are verifiable, continuous, participatory, auditable, sovereign, repairable, and inclusive*. These seven properties map to seven indicator dimensions. Each dimension specifies:

- A theoretical grounding in Ostrom, ISO 15489, legitimacy theory, or CARE
- A definition of what is being measured
- A primary indicator with a computation formula
- A data source: an on-chain event, an exported artifact, or a platform log — never a self-reported survey as primary evidence
- A known Goodhart risk with documented mitigation

The framework is artifact-first by design. Following the DPI Map methodology [World Bank 2023], variables are coded on the basis of publicly or community-verifiable sources, not self-report. This is the core methodological departure from perception-based governance indices.

### 4.2 Seven Indicator Dimensions

---

**Dimension 1 — Record Verifiability (RV)**

*Grounding*: ISO 15489 (authenticity, reliability, integrity, usability); RFC 6962 (append-only logs with consistency proofs); W3C Verifiable Credentials v2.0

*Definition*: The proportion of community governance actions for which a cryptographically verifiable, externally reproducible record exists.

*RV-01 — Verifiable Action Coverage Rate*:

```
RV-01 = (Governance actions with anchored on-chain receipt) /
         (Total governance actions logged on platform) × 100
```

*Data source*: Block explorer query against the community's workspace contract address; Truth Layer canonical receipt index. Computable by any member with the workspace address, without platform API access.

*Benchmark*: ≥80% = "digitally governed"; 40–79% = "transitional"; <40% = "WhatsApp-equivalent baseline"

*Goodhart risk*: Records that are technically on-chain but not independently reproducible — e.g., platform controls the only indexer. *Mitigation*: Require at least one IPFS-pinned or community-archived proof export per governance cycle before the cycle counts as closed.

---

**Dimension 2 — Decision Participation Rate (DPR)**

*Grounding*: Ostrom Principle 3 (collective-choice arrangements); Tyler [2006] (procedural fairness → legitimacy); Mansuri & Rao [2013] (induced vs. organic participation)

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

*Goodhart risk*: Manufactured participation — automated or coerced votes inflating DPR-01. *Mitigation*: Weight participation by stake-in-outcome: only members who made at least one treasury contribution in the 90-day window count toward the denominator.

---

**Dimension 3 — Treasury Transparency Index (TTI)**

*Grounding*: ISO 15489 (reliability); NIST SP 800-53 (auditability controls); Ostrom Principles 4 and 5 (monitoring and sanctioning); collective action theory [Olson 1965] (anti-capture design)

*Definition*: The proportion of treasury movements for which an on-chain record with sufficient metadata exists to reconstruct the complete financial history of the workspace.

*TTI-01 — Treasury Audit Completeness Rate*:

```
TTI-01 = (Treasury movements with complete on-chain metadata:
           amount, sender, recipient, stated purpose, timestamp,
           approving signatory addresses) /
          (Total treasury movements) × 100
```

*TTI-02 — Solvency Provability Score*: Binary (1/0) — whether the workspace can generate a zero-knowledge proof of current treasury balance ≥ stated obligations without revealing individual member contribution amounts.

*Data source*: Akpa Oroma on-chain ledger (queryable directly from block explorer); Policy Locks enforcement records.

*Goodhart risk*: Inflated purpose metadata — strings that formally satisfy length requirements but carry no information. *Mitigation*: Require purpose strings ≥50 characters with at least one reference to a prior proposal ID, enforced at the contract level.

---

**Dimension 4 — Dispute Resolution Legitimacy (DRL)**

*Grounding*: Ostrom Principle 6 (conflict-resolution mechanisms); Beetham [1991] (legitimacy through process); Fox [2015] (social accountability conditions for institutional response)

*Definition*: A composite measure of dispute resolution quality: documentation completeness, outcome contestation rate, and resolution speed.

*DRL-01 — Dispute Resolution Completeness*:

```
DRL-01 = (Disputes with full documented record:
           claim, evidence submitted, decision, reasoning) /
          (Total disputes initiated) × 100
```

*DRL-02 — Outcome Contestation Rate* (inverse-scored — lower is better):

```
DRL-02 = (Disputes reopened or formally appealed within 30 days) /
          (Total disputes resolved) × 100
```

*DRL-03 — Resolution Speed*: Median calendar days from dispute initiation to community-accepted resolution.

*Data source*: Truth Layer dispute desk records; on-chain vote records for resolution acceptance.

*Goodhart risk*: Suppressed dispute rates — social pressure preventing legitimate grievances from being raised. *Mitigation*: Require an anonymous on-chain dispute channel (ZK-anonymized submission); track ratio of anonymous to identified disputes as a signal of suppression.

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

*CPS-02 — Credential Interoperability Rate*: Binary per credential type (1/0) — readable by at least one external verifier without platform API dependency.

*Data source*: Ichi reputation module export logs; W3C VC DID document registry.

*Goodhart risk*: Vanity credentials issued without meaningful governance participation. *Mitigation*: Enforce the three-event evidence requirement at the credential issuance contract.

---

**Dimension 6 — Community Autonomy Score (CAS)**

*Grounding*: CARE Principle 2 (Authority to Control); Digital Public Goods Standard (platform independence); Ostrom Principle 7 (recognition of rights to organize); ISO 14721 / OAIS (long-term preservation and community-controlled access)

*Definition*: The degree to which governance records and operational capacity remain under community control, independent of the platform operator, any single technology provider, or the state.

*CAS-01 — Record Exportability Rate*:

```
CAS-01 = (Governance records exportable in machine-readable
           open-standard format by a member without
           platform operator assistance) /
          (Total governance records) × 100
```

*CAS-02 — Platform Independence Score*: Categorical 0–3: 0 = no export; 1 = export to platform-controlled storage only; 2 = export to community-controlled storage (IPFS/Arweave); 3 = export + independent verification without any platform API call.

*CAS-03 — State Dependency Ratio* (lower is better): (Governance decisions requiring formal government approval or registration to be valid) / (Total governance decisions).

*Data source*: Platform export audit; block explorer verification; community self-attestation for CAS-03.

*Goodhart risk*: Export archives that are technically complete but practically unreadable by non-technical members. *Mitigation*: Annual community-conducted readability audit — at least one member without a technical background must successfully reconstruct a governance decision from the export archive.

---

**Dimension 7 — Financial Inclusion Depth (FID)**

*Grounding*: Francois & Squires [2021] (e-ROSCA ~90% compliance); World Bank GHS Panel (17% informal savings participation); CARE Principle 1 (Collective Benefit); Gugerty [2007] (ROSCA dynamics and participation)

*Definition*: The depth to which the digitized governance system reaches across the community's membership distribution — specifically whether it includes members historically excluded from formally documented financial governance.

*FID-01 — First-Time Formal Participant Rate*:

```
FID-01 = (New members for whom this is their first formally
           documented financial governance experience) /
          (Total new members onboarded in measurement period) × 100
```

Measured by onboarding survey (single question: "Has your savings group or community fund ever used a tool other than WhatsApp, cash, or mobile money transfers to make and record decisions?")

*FID-02 — Gender Participation Parity Index*: (Female active governance participants) / (Total active governance participants), benchmarked at 0.50 equity baseline. *Note: collection requires community consent and ethics clearance — see Section 7.5.*

*FID-03 — Diaspora Integration Rate*: (Members contributing from outside Nigeria with ≥1 verifiable governance action) / (Total diaspora-flagged members). *Note: diaspora flag collection requires community consent — see Section 7.5.*

*Data source*: Onboarding survey; membership metadata; geographic distribution of wallet addresses cross-referenced against contribution records.

*Goodhart risk*: Optimizing for onboarding counts without sustained participation. *Mitigation*: FID-01 requires ≥3 governance interactions post-onboarding to count.

---

### 4.3 Composite Scoring, Dashboard Design, and Sensitivity

Following OECD/JRC Composite Indicator guidance [Nardo et al. 2008], we adopt a **dashboard-first design**. The seven dimensions carry different weights across community types: a diaspora fund weights FID-03 and CPS heavily; a village infrastructure committee weights TTI and DRL. Communities calibrate weights through a Delphi process among recognized members [Quyên 2014].

For cross-community benchmarking, we define a **minimum viable composite — the OGI-Core Score** = equally weighted average of RV-01, DPR-01, TTI-01, and DRL-01. These four are computable entirely from on-chain data, requiring no community survey.

Sensitivity to weighting choices is a known vulnerability of composite governance indices [Nardo et al. 2008; Oman 2006]. Supplementary material (available on request) reports sensitivity tests following the OECD/JRC handbook protocol: OGI-Core scores under five alternative weighting schemes, confirming rank stability for clearly high- and low-performing workspaces while flagging middle-band instability as a limitation requiring Delphi validation before policy deployment.

---

## 5. Platform Architecture as Measurement Infrastructure

### 5.1 Community-Layer DPI Mapping

The World Bank, UNDP, and Carnegie Endowment converge on a three-layer definition of Digital Public Infrastructure: digital identity, digital payments, and verifiable data exchange [World Bank DPI 2025; UNDP 2024; Carnegie 2025]. A community coordination platform that implements all three layers at community scale constitutes community-layer DPI.

| DPI Layer | Platform Module | OGI Dimensions Enabled |
|-----------|----------------|------------------------|
| Digital Identity | **Ichi** — portable W3C VC credentials, community-controlled | CPS-01, CPS-02, DPR-01 |
| Digital Payments | **Akpa Oroma** — community treasury on Bitcoin L2 | TTI-01, TTI-02, FID-01–03 |
| Verifiable Data Exchange | **Truth Layer** — canonical receipts, ZK proofs, dispute desk | RV-01, DRL-01–03, CAS-01–03 |

Supporting modules — **Policy Locks** (enforcement without custody) and **Governance** (dual-chamber proposals, quorum-gated batch payouts) — implement Ostrom Principles 5 and 6 in smart contract form.

The OGI Framework's core indicators are computable from this architecture without platform operator cooperation: any member with the workspace contract address can query block explorer data to compute RV-01, TTI-01, DPR-01, and DPR-02 directly.

### 5.2 Measurement Query Logic

For RV-01, the computation from on-chain data:

```
1. Query workspace contract events: ProposalCreated, VoteCast,
   TreasuryMovement, DisputeOpened, DisputeResolved
2. For each event: check for corresponding TruthLayer receipt
   (anchored hash + IPFS CID stored in receipt mapping)
3. RV-01 = count(events with receipt) / count(total events) × 100
```

For TTI-01:

```
1. Query TreasuryMovement events for workspace address
2. For each movement: check metadata fields (purpose string,
   proposalId reference, signatoryAddresses array, timestamp)
3. Completeness check: purpose.length >= 50 AND proposalId != 0
   AND signatoryAddresses.length >= workspace.quorumThreshold
4. TTI-01 = count(complete movements) / count(total movements) × 100
```

These queries run against a public block explorer or a local node with the contract ABI — no platform login, no API key. This artifact-first measurement approach directly addresses the self-report bias documented in GTMI [2025] and satisfies the "publicly verifiable source" requirement of the DPI Map methodology [World Bank 2023].

### 5.3 Privacy-Preserving Verifiability

The privacy-verifiability tradeoff is the central governance design challenge for community finance. Members need confidence in treasury solvency without individual contribution amounts being exposed — especially in ROSCAs, where members in early-payout or default positions are vulnerable to social pressure. Transparency without privacy controls is not good governance; it is a different kind of surveillance risk.

The platform addresses this through zero-knowledge circuits (Circom + SnarkJS, Groth16) on a Bitcoin L2 zkEVM. The Treasury Solvency Proof (TTI-02) allows any member to verify that workspace treasury balance ≥ *X* without learning the balance of any individual contributor. The proof is generated client-side and verifiable on-chain — implementing the CARE framework's Authority to Control principle through a cryptographic mechanism rather than a policy statement.

---

## 6. Framework Computability Demonstration

### 6.1 Design Science Approach

This paper follows the design science research (DSR) tradition in information systems [Hevner et al. 2004; Peffers et al. 2007]. DSR produces design knowledge: evidence that a proposed artifact — framework, system, model — can address a class of organizational problems. The OGI Framework is the artifact. The contribution is demonstrating its conceptual soundness, theoretical grounding, and computational tractability.

Section 6.2 presents a computability demonstration, not an empirical evaluation. All indicator values are derived from the platform's data model and event schema to show what the OGI Framework would produce when applied to a real community workspace. **These values are ILLUSTRATIVE. They are not sourced from a live deployment and cannot be interpreted as evidence of any real community's governance quality.** They verify that each indicator is computable from the platform's event architecture, produces meaningful variation, and surfaces actionable governance insights.

Full empirical evaluation requires: (1) mainnet deployment with consenting community workspaces; (2) ethics clearance for community data collection (see Section 7.5); (3) Delphi validation of indicator weights and definitions across practitioner groups. This constitutes the future work programme.

### 6.2 Illustrative Computability Case

The following values are derived by applying OGI indicator formulas to a hypothetical community workspace matching the platform's data model: a diaspora-facing cooperative with 34 members distributed across Southeast Nigeria and the United Kingdom, with an active treasury and three completed governance cycles. All values are examples of what the framework would produce, not measurements of an actual workspace.

| OGI Indicator | Illustrative Value | What it demonstrates |
|---------------|-------------------|----------------------|
| RV-01 | 94% | 32 of 34 hypothetical governance actions would have anchored receipts; 2 failed IPFS pin would surface as a gap requiring re-anchoring |
| DPR-01 | 71% | 24 of 34 members would meet the participation threshold; the framework surfaces the 26% non-participating as a governance quality signal |
| DPR-02 | 82% | 9 of 11 hypothetical proposals would reach quorum; 2 expired-without-quorum events would be documented, not silently dropped |
| TTI-01 | 100% | All 18 hypothetical treasury movements with complete metadata; the formula is directly queryable from the treasury event log |
| TTI-02 | 1 | Binary: ZK solvency proof would be generated and verifiable on-chain |
| DRL-01 | 67% | 2 of 3 hypothetical disputes with full documentation; 1 pending would be flagged as incomplete |
| CPS-01 | 47% | 16 of 34 hypothetical members with exported portable credentials; adoption gap identified for intervention |
| CAS-02 | 2 | Records exported to IPFS; full platform-independent verification pathway available |
| FID-01 | 58% | 7 of 12 hypothetical new members reporting first formal governance experience |

*Illustrative OGI-Core Score* (RV-01 + DPR-01 + TTI-01 + DRL-01, equally weighted): **83%** — demonstrating that the composite is computable and produces a meaningful summary.

The framework's diagnostic value is visible even in illustrative form: CPS-01 at 47% would identify credential portability as an adoption gap; DRL-01 at 67% would surface incomplete dispute documentation as a governance quality concern requiring product-level enforcement.

### 6.3 Contextual Evidence from the Literature

The structural problem the OGI Framework addresses is empirically documented. Records management studies in Nigerian local government councils report: absence of records management culture, staff unable to distinguish records by type or purpose, dominant paper-based systems, insufficient storage, and "gross inefficiency and lack of policy continuity" [Adebayo 2018; Public Records Management Nigeria 2018]. These studies document the failure mode the OGI Framework is designed to make measurable and preventable.

The e-ROSCA field experiment by Francois and Squires [2021] in DRC found approximately 90% contribution compliance in mobile-money-enabled rotating savings groups — demonstrating that digital governance mechanisms in informal finance contexts are empirically feasible under appropriate incentive design. This is the strongest available evidence that the underlying assumption of the OGI Framework — that community members will engage with digitized governance if the design is appropriate — holds in practice.

---

## 7. Discussion

### 7.1 Three Measurement Layers, Not One

The OGI Framework does not compete with EGDI, DGI, or GTMI. It occupies the measurement layer those indices leave structurally empty. A complete digital governance measurement stack for Nigeria requires:

- **Layer 1** — National e-government benchmarks (EGDI, GTMI, DGI as-is)
- **Layer 2** — Subnational digital governance indicators (LOSI extensions; state-level assessments)
- **Layer 3** — Community-layer governance indicators (OGI Framework)

Only Layer 3 captures the governance accountability that most Nigerians experience directly. A country that scores well on EGDI while its town union treasuries are unauditable and its esusu circles cannot produce verified records has not achieved digital governance success. Its digital governance measurement has simply failed to look where governance actually happens.

### 7.2 The Transparency-Privacy Tension

Greater verifiability is not always better governance. An indicator framework that makes community records more legible to external auditors at the cost of member privacy or community autonomy produces a different kind of governance failure. This tension is concrete in the ROSCA context: publishing individual contribution records in the name of "transparency" exposes members in default positions to social stigma, debt collectors, or family pressure — directly violating the CARE Principle of Authority to Control.

The OGI Framework addresses this through two design choices. First, TTI-02 uses ZK proofs specifically to separate solvency verification (which the community needs) from contribution disclosure (which members have a right to control). Second, CAS-03 tracks state dependency — the ratio of governance decisions requiring formal government involvement — as a metric to minimize, not maximize. A governance framework that achieves verifiability by routing all records through state registries has not improved community governance; it has subordinated it to state oversight without community consent.

### 7.3 Measuring Outcomes vs. Organizational Forms

A common objection to digitizing informal institutions is that it forces bureaucratization — that formal record-keeping requirements destroy the adaptive social fabric that makes informal systems work. This objection deserves a direct answer.

The OGI Framework measures governance *outcomes* — can a decision be verified? can a dispute be audited? does a record survive leadership transition? — not organizational *forms*. A WhatsApp group that generates a ZK solvency proof is still a WhatsApp group. An esusu circle that anchors its contribution records on-chain retains its social character while adding an evidentiary layer. The indicator asks "is this governance action verifiable?" not "does this institution look like a registered cooperative?"

The distinction matters because the literature documents that the most durable informal institutions succeed precisely because they adapt their forms while maintaining their functions [Ostrom 1990; Ardener & Burman 1995; Gugerty 2007]. An indicator framework that creates pressure to formalize organizational structure in exchange for a better score would damage what it is trying to measure. All seven OGI dimensions are process-quality indicators, not organizational compliance indicators.

### 7.4 DPI Policy Implications for Nigeria

NITDA's statutory remit covers planning, research, standardisation, and monitoring/evaluation of IT practices in Nigeria. The OGI Framework provides a measurable specification for community-layer DPI outcomes — analogous to how State of Instant and Inclusive Payment Systems (SIIPS) assessments measure national payment system maturity. The seven OGI dimensions are directly translatable into monitoring criteria for community digital governance programmes across Nigeria's 36 states and 774 local government areas.

Community-layer DPI — digital identity (portable credentials), digital payments (community treasury), and verifiable data exchange (canonical records with dispute resolution) — complements but is not substitutable for national-layer DPI. The OGI Framework makes community-layer DPI investment outcomes measurable for the first time, enabling NITDA and development partners to evaluate whether community digital governance programmes are producing the institutional quality their funding intends.

### 7.5 Limitations and Future Work

**Empirical validation**: The OGI Framework has been demonstrated as computationally tractable but not empirically validated. Future work will conduct a Delphi consensus process [Quyên 2014] across five stakeholder groups: (1) community governance practitioners (town union leaders, esusu coordinators), (2) digital governance measurement specialists, (3) DPI policy actors, (4) blockchain governance researchers, and (5) community members of active deployments. Target: Q3 2026.

**Ethics and consent**: Collection of any demographic data (FID-02, FID-03) requires community consent protocols and ethics clearance aligned with relevant national research ethics frameworks. Consent state must be machine-readable and attached to each workspace before data collection begins. This is a policy requirement, not an instrumentation question.

**Attribution**: Following Fox [2015] and Mansuri & Rao [2013], no causal claim is made that verifiable digital records produce improved community outcomes. The OGI Framework measures governance process quality. The causal pathway from verifiable records to reduced elite capture to improved development outcomes requires a separate longitudinal evaluation design — one the Research Spine architecture (described in the companion technical specification) is designed to support.

**Deployment scale**: Demonstrating cross-context validity requires deployment across multiple community types — market cooperatives, town unions, diaspora funds, student associations — in multiple locations. The framework's seven dimensions are designed to be transferable, but contextual calibration will be needed for each deployment context.

---

## 8. Conclusion

Every major digital governance benchmark currently in use was designed to measure what states do. This is not a criticism — it is a description of the design constraints under which those indices were built, and those constraints were reasonable for their purpose. The problem is that in Southeast Nigeria, as in much of Sub-Saharan Africa, states are not where most governance happens. Town unions build the roads. Esusu circles finance the enterprises. Diaspora networks sustain communities across distance. None of this is measurable by any instrument that currently counts as "digital governance measurement."

The OGI Framework is a first attempt to close that gap — seven dimensions grounded in Ostrom's design principles, ISO 15489 records standards, governance legitimacy theory [Beetham 1991; Tyler 2006; Suchman 1995], and CARE data sovereignty principles. Each indicator computable from verifiable on-chain artifacts, not self-reported surveys. Each dimension accompanied by a documented Goodhart risk and structural mitigation. A dashboard-first design that communities calibrate to their own governance contexts.

The contribution to Track 6 is precise: new metrics and a new measurement methodology for the governance layer that existing approaches structurally omit. The contribution to Nigerian digital governance policy is direct: a NITDA-aligned, artifact-based indicator set for community-layer DPI outcomes, ready for Delphi validation and field deployment.

The town union treasurer who carried the ledger to London when he relocated, leaving no record of three years of community contributions. The esusu circle whose rotating payout went disputed because the organiser's notebook was the only record of who had already received their share. The diaspora levy committee that dissolved — not because members stopped caring, but because no one could prove which projects the contributions had funded. These are not exotic governance failures. They are the normal operating condition of collective finance and governance for millions of Nigerians. The OGI Framework is designed for that context: not an adaptation of a Western measurement instrument, but a first attempt to build measurement appropriate to what these institutions are already doing, on their own terms, with their own evidence.

---

## References

1. Adebayo, O. (2018). Public records and management of information materials in Nigerian local government: A transformative route. *Global Journal of Human Social Science*, 18(3).
2. Aligica, P.D., & Tarko, V. (2012). Polycentricity: From Polanyi to Ostrom and beyond. *Governance*, 25(2), 237–262.
3. Ardener, S., & Burman, S. (Eds.). (1995). *Money-go-rounds: The importance of rotating savings and credit associations for women*. Berg Publishers.
4. Beetham, D. (1991). *The Legitimation of Power*. Palgrave Macmillan.
5. Besley, T., Coate, S., & Loury, G. (1993). The economics of rotating savings and credit associations. *American Economic Review*, 83(4), 792–810.
6. Carnegie Endowment for International Peace. (2025, February). *Digital public infrastructure: A practical approach for Africa*. Sang, D., Munga, J., & Sambuli, N.
7. Carroll, S.R., et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 19, 43. https://doi.org/10.5334/dsj-2020-043
8. Fox, J. (2015). Social accountability: What does the evidence really say? *World Development*, 72, 346–361.
9. Francois, P., & Squires, M. (2021). Linking mobile money networks to "e-ROSCAs": An experimental study. *Science Advances*, 7(1). https://doi.org/10.1126/sciadv.abc5831
10. Global Informality Project. (2020). *Esusu (Nigeria)*. https://www.in-formality.com/wiki/index.php?title=Esusu_(Nigeria)
11. Gugerty, M.K. (2007). You can't save alone: Testing theories of rotating savings and credit associations. *Economic Development and Cultural Change*, 55(2), 251–282.
12. Harneit-Sievers, A. (2006). Institutionalizing community I: Town unions. In *A place in the world: New local historiographies from Africa and South Asia*. Brill.
13. Heeks, R. (2006). *Benchmarking e-government: Improving the national and international measurement, evaluation and comparison of e-government*. IDPM, University of Manchester.
14. Hevner, A.R., March, S.T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105.
15. Honey, R., & Okafor, S.I. (Eds.). (1998). *Hometown associations: Indigenous knowledge and development in Nigeria*. Intermediate Technology Publications.
16. International Organization for Standardization. (2016). *ISO 15489-1:2016 — Information and documentation — Records management — Part 1: Concepts and principles*.
17. Ishola, A.A., Maramura, T.C., & Gumbo, T. (2025). Charting digital governance: A bibliometric analysis of ICT research in Nigeria's public administration. *Frontiers in Sustainable Cities*. https://doi.org/10.3389/frsc.2025.1605736
18. Mansuri, G., & Rao, V. (2013). *Localizing development: Does participation work?* World Bank Policy Research Report.
19. Mo Ibrahim Foundation. (2024). *Ibrahim Index of African Governance: Methodology and sources 2024*. https://mo.ibrahim.foundation/iiag
20. Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A., & Giovannini, E. (2008). *Handbook on constructing composite indicators: Methodology and user guide*. OECD/JRC. https://doi.org/10.1787/9789264043466-en
21. National Archives UK. (2017). *Understanding digital continuity*. The National Archives.
22. Nwangwu, B.C. (2024). Repositioning town unions as the fourth-tier of government in South East Nigeria: Lessons from Covid-19. *International Journal of Research and Innovation in Social Science*, 8(11). https://doi.org/10.47772/IJRISS.2024.8110251
23. OECD. (2024). *2023 OECD Digital Government Index: Results and key findings*. OECD Public Governance Policy Papers. https://doi.org/10.1787/1a89ed5e-en
24. Okafor, E.E. (2019). The dictum, Igbo Enwe Eze: Socio-cultural underpinnings for understanding the current Igbo peoples' political dilemma. *Sociology and Philosophy*, 9(1). https://doi.org/10.4236/sm.2019.91005
25. Olson, M. (1965). *The Logic of Collective Action: Public Goods and the Theory of Groups*. Harvard University Press.
26. Oman, C.P. (2006). *Uses and abuses of governance indicators*. OECD Development Centre.
27. Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
28. Ottenberg, S. (1955). Improvement associations among the Afikpo Ibo. *Africa: Journal of the International African Institute*, 25(1), 1–22.
29. Peffers, K., Tuunanen, T., Rothenberger, M.A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77.
30. Public Records Management in Nigerian Local Government. (2018). *Public records and management of information materials in Nigerian local government: A transformative route*. *Global Journal of Human Social Science*.
31. Quyên, Đ.T.N. (2014). Developing university governance indicators and their weighting system using a modified Delphi method. *Procedia — Social and Behavioral Sciences*, 141, 828–833.
32. Shava, E., & Mhlanga, D. (2023). Mitigating bureaucratic inefficiencies through blockchain technology in Africa. *Frontiers in Blockchain*, 6. https://doi.org/10.3389/fbloc.2023.1053555
33. Suchman, M.C. (1995). Managing legitimacy: Strategic and institutional approaches. *Academy of Management Review*, 20(3), 571–610.
34. Tyler, T.R. (2006). *Why People Obey the Law*. Princeton University Press.
35. Uduku, O. (2002). The socio-economic basis of a diaspora community: *Igbo bu ike*. *African Affairs*, 101(404), 339–355.
36. United Nations DESA. (2024). *UN E-Government Survey 2024: Accelerating digital transformation for sustainable development*. United Nations.
37. UNDP. (2024). *Digital public infrastructure (DPI)*. https://www.undp.org/digital/digital-public-infrastructure
38. World Bank. (2025). *GovTech Maturity Index 2025 update: Tracking public sector digital transformation worldwide*.
39. World Bank. (2025). *Digital public infrastructure and development: A World Bank Group approach*. https://openknowledge.worldbank.org/entities/publication/cca2963e-27bf-4dbb-aa5a-24a0ffc92ed9
40. World Justice Project. (2025). *WJP Rule of Law Index 2025: Methodology and sources*.
41. Zambrano, A.F., et al. (2023). Rotating savings and credit associations: A scoping review. *World Development Sustainability*, 3. https://doi.org/10.1016/j.wds.2023.100093

---

*[End of manuscript — Draft v3. Approximately 8,800 words excluding references. Category: Ongoing Research, 8–10 pages. Abstract: 226 words. Keywords: 8. Double-blind compliant.]*
