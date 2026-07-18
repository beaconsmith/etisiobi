# Measuring Community-Layer Digital Governance: An Indicator Framework for Southeast Nigeria

## Abstract

The dominant digital governance indices measure what states do. They do not capture the governance quality of the community institutions - town unions, rotating savings circles, and diaspora associations - that organize collective life for many Nigerians outside the state's everyday record systems. This paper introduces the OGI Framework, a seven-dimension indicator set for measuring community-layer digital governance in Southeast Nigeria. The framework is designed for ongoing research in Track 6 terms: it proposes a new measurement instrument, grounds it theoretically, and demonstrates that its core indicators are computationally tractable in a prototype digital governance environment. The framework is built on four commitments: artifact-first evidence rather than self-reported perception alone; records-quality criteria drawn from ISO 15489; legitimacy and collective-action theory from Ostrom, Beetham, Tyler, and Suchman; and CARE-style community data sovereignty. Each dimension is paired with a formula, an evidence source, and an explicit Goodhart-risk mitigation. We distinguish a four-indicator OGI-Core, which is intended to be computable from verifiable event records, from secondary dimensions that require credential export, consent workflows, or inclusion metadata. A Stage 4 design-science demonstration using an illustrative cooperative scenario shows that the framework can surface different classes of governance weakness - for example missing receipt anchors, weak dispute documentation, or low credential portability - rather than collapsing governance into a single state-centered service metric. The contribution is a measurement framework for a governance layer that existing indices structurally omit: community-led, digitally mediated, privacy-sensitive, and accountable through community evidence rather than state self-report.

**Keywords:** digital governance indicators, community-led development, verifiable records, digital public infrastructure, Southeast Nigeria, informal institutions

---

## 1. Introduction

In much of Southeast Nigeria, governance does not begin at the state. Town unions mobilize funds for roads and schools. Rotating savings groups coordinate credit and obligation. Diaspora associations pool contributions for projects back home. These institutions govern collectively, but their decisions are often documented through fragile media: notebooks, chat threads, oral witnessing, or treasurer memory. When disputes arise or leadership changes, the problem is frequently not the absence of governance, but the absence of durable and auditable records.

That mismatch matters for measurement. The most widely used digital-governance benchmarks - the UN E-Government Development Index (EGDI), the OECD Digital Government Index (DGI), and the World Bank GovTech Maturity Index (GTMI) - provide the authoritative language for "digital governance success," yet none is designed to evaluate whether a community treasury is reconstructable, whether a dispute process is documented, or whether community records remain under member control [UN DESA 2024; OECD 2024; World Bank 2025a]. In contexts where collective action is organized through non-state institutions, this leaves a large part of governance analytically invisible.

This paper argues that a distinct measurement layer is needed for digitally mediated community governance. The claim is deliberately scoped. We do not argue that verifiable records are a universal condition for all governance across all history. We argue that in digitally mediated community governance contexts - especially where members are geographically dispersed and cannot rely on co-presence or shared witnessing alone - verifiable records are a necessary condition for measurable accountability.

The paper makes three contributions.

1. It documents a measurement gap: existing benchmark families and adjacent accountability tools do not measure community-internal governance quality.
2. It proposes the OGI Framework, a seven-dimension indicator set grounded in collective-action theory, legitimacy theory, records management, and data sovereignty.
3. It demonstrates, in design-science terms, that the framework's core indicators are computationally tractable in a prototype community-governance environment, while naming the dimensions that remain deployment-blocked.

The remainder of the paper situates the gap, presents the framework, shows how the indicator logic maps to a prototype measurement substrate, and closes with validity threats and next-step evaluation requirements.

---

## 2. Background and Related Work

### 2.1 State-centered digital governance benchmarks

The dominant benchmark families are state-centered by design. EGDI combines online services, telecommunications infrastructure, and human-capital measures at national level [UN DESA 2024]. OECD's DGI measures public-sector digital-government maturity across a set of institutional dimensions [OECD 2024]. GTMI assesses government digital capacity across 198 economies, relying partly on government-reported information [World Bank 2025a]. IIAG synthesizes African governance indicators from multiple sources, while the WJP Rule of Law Index explicitly recognizes informal justice but excludes it from headline scoring [Mo Ibrahim Foundation 2024; WJP 2025].

The common pattern is structural, not accidental: these instruments measure what states do, using data states produce, administer, or authorize. They are valuable for their intended layer. They are poorly suited to questions such as whether community decisions are independently verifiable, whether records survive leadership transition, or whether treasury history can be reconstructed without relying on a single trusted intermediary.

**Table 1** summarizes the difference.

| Measurement property | EGDI | OECD DGI | GTMI | OGI |
|----------------------|------|----------|------|-----|
| Community decisions independently verifiable | No | No | No | Yes |
| Records survive leadership transition | No | No | Partial | Yes |
| Treasury history reconstructable | No | No | Partial | Yes |
| Dispute process auditable | No | No | No | Yes |
| Community controls its own records | No | No | No | Yes |
| Evidence source | State and official datasets | Government systems and surveys | Government systems and surveys | Community-produced artifacts |

This gap aligns with Heeks' early critique that e-government benchmarking privileges what is legible to formal institutions [Heeks 2006]. The unresolved question is whether community-produced digital artifacts can provide a credible evidentiary base for a different kind of benchmark.

### 2.2 Adjacent measurement traditions

Community-driven development research shows that communities can organize collective action effectively, but that governance effects are difficult to evaluate with blunt or externally imposed measures [Mansuri and Rao 2013; Casey 2024]. That finding is often read as weak community governance. It can also be read as weak community-governance measurement.

Two adjacent traditions are important comparators. Community Scorecard methods assess citizen satisfaction with service delivery through facilitated dialogue [Singh and Shah 2003]. Social Audit methods inspect whether delegated state resources were used as intended [Gaventa and McGee 2013]. Both are powerful accountability tools, but both assume that the primary accountable actor is external to the community. The OGI Framework addresses a different unit of analysis: the community institution itself as record producer, treasury operator, and decision-making body.

Recent ICEGOV work on local online service provision and e-participation remains concentrated on municipal portals and state-facing digital service layers rather than community-governance records [Guimaraes et al. 2025; Kabanov 2025]. A bibliometric review of Nigerian digital-governance research similarly identifies gaps around indigenous technology development and marginalized community contexts [Ishola et al. 2025]. The present paper sits in that opening.

### 2.3 Southeast Nigeria as primary context

Southeast Nigeria provides a strong grounding case because community institutions are not peripheral to governance there. The idiom *Igbo enwe eze* signals a long tradition of distributed authority rather than a single centralized sovereign [Okafor 2019]. Town unions, age grades, and hometown associations have long served as durable collective institutions, including for development finance and project coordination [Harneit-Sievers 2006; Ottenberg 1955; Uduku 2002].

Rotating savings and credit associations are especially important for thinking about digitally mediated governance because they depend on contribution tracking, sequence legitimacy, and dispute handling. The classic ROSCA literature emphasizes repeated interaction, reputational enforcement, and social sanction rather than formal documentation [Ardener 1964; Besley, Coate, and Loury 1993; Bouman 1995]. Gendered participation structures matter too, which is why inclusion measures in this framework remain consent-dependent rather than being folded uncritically into the core score [Ardener and Burman 1995; Gugerty 2007].

At the same time, Nigerian records-management studies document recurring failures of continuity, filing discipline, and institutional memory [Adebayo 2018]. Recent work on town unions in Southeast Nigeria points to accountability and coordination pressures that become sharper, not weaker, when collective finance scales across distance [Nwangwu 2024]. This is precisely the setting in which digitally mediated, verifiable community records become analytically important.

---

## 3. Theoretical Foundation

The OGI Framework draws on four bodies of work, each of which does specific design work.

First, Ostrom's design principles provide the collective-action backbone [Ostrom 1990]. Clearly defined membership, monitoring, conflict resolution, and rights to organize can all be translated into observable record properties or governance events. Olson's collective-action logic sharpens the capture problem: participation and monitoring indicators must be designed against free riding and organized subgroup domination [Olson 1965].

Second, legitimacy theory provides the outcome logic for why these process measures matter. Beetham emphasizes rule-boundedness, justifiability, and consent [Beetham 1991]. Tyler shows the empirical force of procedural fairness [Tyler 2006]. Suchman distinguishes pragmatic, moral, and cognitive legitimacy [Suchman 1995]. Taken together, these perspectives justify indicators that ask whether decisions were documented, contestable, and participatory rather than merely whether they produced favorable short-term outcomes.

Third, records management turns governance actions into evidence questions. ISO 15489 defines records through authenticity, reliability, integrity, and usability [ISO 15489-1 2016]. The National Archives' digital continuity work adds the temporal requirement that records remain usable across transitions [National Archives UK 2017]. In a digitally mediated governance setting, those properties are not ancillary; they are part of accountability itself.

Fourth, the CARE Principles constrain the framework normatively [Carroll et al. 2020]. More legibility is not always better governance. A framework that improves auditability by making community records broadly exposed to outsiders can create a different failure: surveillance instead of sovereignty. For that reason, privacy-preserving verification and community control are built into the indicator logic rather than treated as afterthoughts.

---

## 4. The OGI Framework

### 4.1 Design commitments

The framework is built around four commitments.

1. **Artifact-first evidence.** Primary evidence should come from community-produced artifacts - event records, receipts, exportable logs, or verifiable credentials - not from self-report alone.
2. **Process-quality measurement.** The framework measures accountable process conditions, not whether a community's decisions are normatively correct.
3. **Community sovereignty.** Record export, platform independence, and privacy-preserving verification are part of governance quality.
4. **Explicit anti-Goodhart design.** Every dimension names the behavior it might incentivize badly and pairs that risk with a structural mitigation.

The OGI Framework does not replace EGDI, DGI, or GTMI. It complements them by adding a layer they do not observe.

### 4.2 Indicator set

**Table 2** summarizes the seven dimensions.

| Dim. | What it asks | Core indicator(s) | Primary evidence | Main Goodhart risk and mitigation |
|------|--------------|------------------|------------------|-----------------------------------|
| RV | Are governance actions externally verifiable? | `RV-01` Verifiable Action Coverage | Anchored event receipts | Anchored but not independently reproducible records; require cycle-level export/proof checks |
| DPR | Are eligible members participating in decisions? | `DPR-01` Active Participation, `DPR-02` Quorum Achievement | Proposal and vote events; membership registry | Manufactured participation; require stake-in-outcome with grace-period exceptions |
| TTI | Can treasury history be reconstructed? | `TTI-01` Audit Completeness, `TTI-02` Solvency Provability | Treasury events and metadata | Boilerplate purpose fields; require proposal linkage and audit review |
| DRL | Are disputes documented, contestable, and resolved? | `DRL-01` Documentation Completeness, `DRL-02` Contestation, `DRL-03` Resolution Speed | Case records and resolution events | Suppressed disputes; include anonymous submission channel |
| CPS | Can members carry governance standing across platforms? | `CPS-01` Portable Identity Coverage, `CPS-02` Interoperability | Exported verifiable credentials | Vanity credentials; tie issuance to governance-event evidence |
| CAS | Can the community retain records and governance capacity independent of operator or state? | `CAS-01` Exportability, `CAS-02` Platform Independence, `CAS-03` Imposed State Dependency | Export audits, open formats, registry checks | Technically complete but unreadable exports; require periodic readability testing |
| FID | Does digitization include first-time or historically excluded participants? | `FID-01` First-time Formal Participation, `FID-02` Gender Parity, `FID-03` Diaspora Integration | Onboarding survey and consented metadata | Counting onboarding without sustained participation; require post-onboarding activity threshold |

### 4.3 Indicator definitions

The framework uses the following core formulas.

**RV-01 - Verifiable Action Coverage**

```text
RV-01 = actions with verifiable anchored receipts / total governance actions
```

This dimension operationalizes records authenticity, integrity, and usability. Its main thresholding problem is calibration rather than principle: the framework treats any cutoff as provisional until empirical calibration and Delphi review are complete.

**DPR-01 - Active Governance Participation**

```text
DPR-01 = unique members who vote or propose in window / eligible members in window
```

**DPR-02 - Quorum Achievement**

```text
DPR-02 = proposals reaching quorum / proposals initiated
```

Participation is not counted as raw click volume. The design assumes a stake-in-outcome screen, but explicitly allows grace-period exceptions for new members and contribution cadences that are annual or otherwise non-monthly. This keeps the measure from collapsing into a crude wealth proxy.

**TTI-01 - Treasury Audit Completeness**

```text
TTI-01 = treasury movements with complete metadata / total treasury movements
```

Required metadata include amount, timestamp, counterparties or role-authorized signatories, and stated purpose linked to an authorizing decision. `TTI-02` is binary and asks whether a treasury-balance proof can be generated without exposing individual contributions.

**DRL-01 - Dispute Documentation Completeness**

```text
DRL-01 = disputes with claim, evidence, decision, and reasoning / total disputes
```

`DRL-02` captures reopened or appealed cases, and `DRL-03` records median resolution time. Together they ask whether conflict resolution is visible, contestable, and timely.

**CPS-01 - Portable Identity Coverage**

```text
CPS-01 = members with an exported verifiable credential backed by governance evidence / active members
```

The evidence threshold for credential issuance remains provisional. The current design treats three governance events as a plausible minimum for a complete participation cycle, but this is a known item for later Delphi validation rather than a settled universal standard.

**CAS-01 - Record Exportability**

```text
CAS-01 = governance records exportable in open machine-readable form / total governance records
```

`CAS-02` is a categorical independence score from no export to export plus independent verification. `CAS-03` measures *imposed* state dependency only: decisions legally required to pass through state approval. It does not penalize communities for *chosen* state engagement.

**FID-01 - First-time Formal Participation**

```text
FID-01 = new members whose first documented governance participation occurs here / newly onboarded members
```

`FID-02` and `FID-03` require consent-governed metadata and are therefore explicitly deployment-blocked. Inclusion is part of the framework, but not every inclusion indicator is ethically collectible at design stage.

### 4.4 OGI-Core and composite use

The framework is dashboard-first. It is designed to be read dimension by dimension before being collapsed into any composite score. For cross-case comparison, a provisional **OGI-Core** can be computed as the equally weighted average of `RV-01`, `DPR-01`, `TTI-01`, and `DRL-01`. These four were selected because they are the least dependent on surveys or identity metadata and the most clearly tied to governance record quality.

Sensitivity to weighting remains a known limitation of all composite governance indices [Nardo et al. 2008; Oman 2006]. To avoid false precision, the framework proposes community-calibrated weighting through a later Delphi exercise rather than fixing a universal weight vector at submission stage.

**Table 3** gives two illustrative weight profiles.

| Dimension | Diaspora fund | Village infrastructure committee |
|-----------|---------------|----------------------------------|
| RV | 0.15 | 0.15 |
| DPR | 0.10 | 0.20 |
| TTI | 0.20 | 0.25 |
| DRL | 0.10 | 0.20 |
| CPS | 0.20 | 0.05 |
| CAS | 0.10 | 0.10 |
| FID | 0.15 | 0.05 |

The point is not that these are correct weights. The point is that community type changes what "good governance" should emphasize, and the measurement design should make that visible.

### 4.5 Known design tensions

Three tensions are important enough to name now. First, participation screens based on contribution risk excluding legitimate members with irregular or in-kind participation. Second, treasury-completeness rules can measure structural compliance better than semantic intent. Third, credential thresholds remain provisional. Naming these tensions improves the framework; it does not weaken it.

---

## 5. Measurement Substrate and Computational Tractability

### 5.1 Prototype architecture

The OGI Framework requires a substrate capable of producing append-only governance events, treasury metadata, dispute records, exportable artifacts, and privacy-preserving proofs. For the design-science demonstration, we map the framework to a prototype community-coordination environment under development for Southeast Nigerian use cases. To preserve review blinding, the paper treats that system generically rather than as a named platform.

The prototype has three measurement-relevant layers.

| Layer | Function | OGI dimensions primarily enabled |
|-------|----------|----------------------------------|
| Identity layer | Membership and credential issuance | CPS, part of DPR |
| Treasury layer | Contributions, disbursements, approval metadata | TTI, part of FID |
| Verifiable record layer | Anchored receipts, case records, export workflows | RV, DRL, CAS |

### 5.2 Query logic

Two examples illustrate tractability.

For `RV-01`:

```text
1. Query governance events in measurement window.
2. Check whether each event has a verifiable anchored receipt.
3. Compute verified events / total events.
```

For `TTI-01`:

```text
1. Query treasury movement events.
2. Check for required metadata and authorizing-decision linkage.
3. Compute complete movements / total movements.
```

The key design choice is that these queries should be reproducible from artifacts without relying on a cooperative platform operator at scoring time.

### 5.3 Why a ledger-backed substrate?

The framework does not require a particular chain or vendor. It requires three properties: independent verifiability, non-tampering of governance records, and support for privacy-preserving treasury proof workflows. Simpler append-only logs can satisfy some of these conditions, but often only by reintroducing a trusted operator or monitor. A ledger-backed substrate is therefore treated here as one implementation path, not as the theoretical contribution.

### 5.4 Current implementation boundary

The prototype supports a strong tractability claim for the OGI-Core and a weaker one for the full seven-dimension framework. Core event models make `RV-01`, `DPR-01`, `DPR-02`, and parts of `TTI-01` and `DRL-01` structurally queryable. By contrast, `TTI-02`, `DRL-02`, `CPS-01`, and `FID-01` through `FID-03` depend on workflows that are only partially implemented or not yet ethically deployable. This distinction matters. The submission claims architectural feasibility for the full framework and partial computability for the prototype, not empirical validation of all indicators.

### 5.5 Privacy and residual trust

Privacy is not an add-on. In savings-group settings, raw transparency can expose members to pressure, stigma, or retaliation. For that reason, the framework treats solvency proof and disclosure minimization as part of treasury governance quality rather than as external compliance constraints.

Residual trust also remains. Any practical substrate can still face censorship, collusion among signatories, weak key custody, or operator influence over onboarding and export flows. The contribution is therefore not "trustlessness." It is a clearer and more measurable disclosure of where trust remains.

---

## 6. Illustrative Design-Science Demonstration

This paper is positioned as a Stage 4 design-science contribution: a framework plus a demonstration that the framework can be instantiated meaningfully before live evaluation [Hevner et al. 2004; Peffers et al. 2007; Gregor and Hevner 2013]. The values below are illustrative. They are not results from live community deployment.

The scenario is a 34-member diaspora-facing cooperative spanning Southeast Nigeria and the United Kingdom over three completed governance cycles. That size and cadence are plausible for savings-group and hometown-association style collective action [Besley, Coate, and Loury 1993; Gugerty 2007].

| Indicator | Illustrative value | Diagnostic meaning |
|-----------|--------------------|--------------------|
| RV-01 | 94% | Most governance actions are verifiable, but anchoring gaps remain |
| DPR-01 | 71% | Participation is substantial but not universal |
| DPR-02 | 82% | Quorum failure is visible rather than hidden |
| TTI-01 | 100% | Treasury completeness rules are being enforced structurally |
| DRL-01 | 67% | Dispute documentation is the weak point in the core score |
| CPS-01 | 47% | Credential portability is an adoption bottleneck |
| CAS-02 | 2/3 | Records are exportable, but full independence is incomplete |
| FID-01 | 58% | The system appears capable of formalizing first-time participation |

The illustrative **OGI-Core** is 83%. That number is less important than the profile. The framework does not merely announce "good" or "bad" governance. It localizes weakness: missing receipt anchors, incomplete dispute documentation, or low credential portability imply different governance and design interventions.

The demonstration is also plausible in context. Studies of Nigerian records management and town-union coordination document the underlying continuity problem [Adebayo 2018; Harneit-Sievers 2006; Nwangwu 2024]. Digitized ROSCA evidence from the DRC suggests that sustained contribution behavior can survive digitization under the right incentive structure [Francois and Squires 2021]. Community-monitoring evidence from Uganda supports the importance of documented grievance channels and anonymity-preserving complaint design [Bjorkman and Svensson 2009].

---

## 7. Discussion, Validity, and Next Steps

### 7.1 A missing layer in the measurement stack

The OGI Framework is best understood as a missing layer rather than a rival index. National and municipal benchmark systems remain useful for service delivery, administrative capacity, and formal public-sector digital maturity. What they do not capture is whether community institutions can document, verify, transfer, and contest their own governance records. That omission is especially consequential in settings where collective action is distributed across town unions, savings groups, and diaspora infrastructures.

### 7.2 Privacy, sovereignty, and organizational form

The framework treats privacy and sovereignty as constitutive of governance quality. Community records that are perfectly auditable but only because they are broadly exposed to outsiders do not represent a success condition here. The same is true of organizational form. A community can remain socially informal while becoming evidentially stronger. The framework therefore asks whether a decision is documented and contestable, not whether the institution has become formally state-like.

### 7.3 Relationship to blockchain-governance criticism

Critical work on blockchain governance warns against rhetorical decentralization, underestimation of the state, and confusion between code and legitimate authority [Atzori 2017; Schneider 2019; De Filippi and Wright 2018]. The OGI Framework is compatible with those critiques. It does not assume that a distributed ledger yields good governance. It asks whether community autonomy, record quality, and independent verification can be measured under conditions where technical infrastructure might otherwise obscure continuing concentrations of power.

### 7.4 Threats to validity

Several validity threats remain explicit.

- **Construct validity.** The framework measures governance-record quality, not full governance quality. It is strongest when the research question is about measurable accountability conditions.
- **Internal validity.** Platform design choices affect scores. A system that enforces metadata fields can raise `TTI-01` without guaranteeing semantic honesty.
- **External validity.** The framework is grounded in Southeast Nigerian institutions and should travel cautiously to other contexts.
- **Scale validity.** Participation norms vary sharply by group size; thresholds for small cooperatives may not transfer cleanly to large plenary associations.
- **Selection effects.** Communities willing to adopt digitally mediated governance are likely to differ from communities that do not.

These are reasons to evaluate carefully, not reasons to avoid framework design.

### 7.5 Future work

The post-submission research agenda is clear.

1. Run Delphi validation on dimension definitions, thresholds, and weights [Quyen 2014].
2. Complete the missing prototype workflows for export, credential, dispute-reopen, and onboarding events.
3. Conduct ethics-governed pilot deployments with consenting communities.
4. Compare ledger-backed and non-ledger append-only implementations against the same indicator logic.

That sequencing follows design-science method: demonstration first, situated evaluation next [Hevner et al. 2004; Gregor and Hevner 2013].

---

## 8. Conclusion

Digital-governance measurement currently sees the state far more clearly than it sees the community. In Southeast Nigeria, that leaves a substantial share of real governance outside the field of measurement.

This paper contributes a response tailored to that gap. The OGI Framework proposes seven dimensions for measuring community-layer digital governance; grounds them in collective-action theory, legitimacy theory, records management, and data sovereignty; and demonstrates that the core of the framework is computationally tractable in a prototype environment even before live deployment.

The paper does not claim empirical validation. It claims that a neglected governance layer can now be measured in a principled way, using community-produced digital evidence rather than state self-report. If later evaluation shows that some indicators fail, that too will be a useful research result. The central point remains: community-led digital governance deserves instruments built for its own evidence, risks, and forms of accountability.

---

## References

1. Adebayo, O. (2018). Public records and management of information materials in Nigerian local government: A transformative route. *Global Journal of Human Social Science*, 18(3).
1. Aligica, P.D., and Tarko, V. (2012). Polycentricity: From Polanyi to Ostrom and beyond. *Governance*, 25(2), 237-262.
1. Ardener, S. (1964). The comparative study of rotating credit associations. *Journal of the Royal Anthropological Institute of Great Britain and Ireland*, 94(2), 201-229.
1. Ardener, S., and Burman, S. (Eds.). (1995). *Money-go-rounds: The importance of rotating savings and credit associations for women*. Berg Publishers.
1. Atzori, M. (2017). Blockchain technology and decentralized governance: Is the state still necessary? *Journal of Governance and Regulation*, 6(1), 45-62.
1. Beetham, D. (1991). *The Legitimation of Power*. Palgrave Macmillan.
1. Besley, T., Coate, S., and Loury, G. (1993). The economics of rotating savings and credit associations. *American Economic Review*, 83(4), 792-810.
1. Bjorkman, M., and Svensson, J. (2009). Power to the people: Evidence from a randomized field experiment on community-based monitoring in Uganda. *Quarterly Journal of Economics*, 124(2), 735-769.
1. Bouman, F.J.A. (1995). Rotating and accumulating savings credit associations: A development perspective. *World Development*, 23(3), 371-384.
1. Carroll, S.R., et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 19, 43. https://doi.org/10.5334/dsj-2020-043
1. Casey, K. (2024). Long-term effects of community-driven development. Working paper.
1. De Filippi, P., and Wright, A. (2018). *Blockchain and the Law: The Rule of Code*. Harvard University Press.
1. Francois, P., and Squires, M. (2021). Linking mobile money networks to "e-ROSCAs": An experimental study. *Science Advances*, 7(1). https://doi.org/10.1126/sciadv.abc5831
1. Gaventa, J., and McGee, R. (2013). The impact of transparency and accountability initiatives. *Development Policy Review*, 31(s1), s3-s28.
1. Gregor, S., and Hevner, A.R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly*, 37(2), 337-355.
1. Gugerty, M.K. (2007). You can't save alone: Testing theories of rotating savings and credit associations. *Economic Development and Cultural Change*, 55(2), 251-282.
1. Guimaraes, R., Figueiredo, T., Sartori, L., Cogo, G., and Cunha, M.A. (2025). The local in LOSI: A discussion on small municipalities' online portals in Brazil. In *Proceedings of ICEGOV 2025*.
1. Harneit-Sievers, A. (2006). Institutionalizing community I: Town unions. In *A place in the world: New local historiographies from Africa and South Asia*. Brill.
1. Heeks, R. (2006). *Benchmarking e-government*. IDPM, University of Manchester.
1. Hevner, A.R., March, S.T., Park, J., and Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75-105.
1. International Organization for Standardization. (2016). *ISO 15489-1:2016 - Information and documentation - Records management*.
1. Ishola, A.A., Maramura, T.C., and Gumbo, T. (2025). Charting digital governance: A bibliometric analysis of ICT research in Nigeria's public administration. *Frontiers in Sustainable Cities*. https://doi.org/10.3389/frsc.2025.1605736
1. Kabanov, Y. (2025). Decentralization and local e-services development: A pilot cross-national study with the LOSI data. In *Proceedings of ICEGOV 2025*.
1. Mansuri, G., and Rao, V. (2013). *Localizing development: Does participation work?* World Bank.
1. Mo Ibrahim Foundation. (2024). *Ibrahim Index of African Governance: Methodology and sources 2024*. https://mo.ibrahim.foundation/iiag
1. Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A., and Giovannini, E. (2008). *Handbook on constructing composite indicators*. OECD/JRC. https://doi.org/10.1787/9789264043466-en
1. National Archives UK. (2017). *Understanding digital continuity*. The National Archives.
1. Nwangwu, B.C. (2024). Repositioning town unions as the fourth-tier of government in South East Nigeria. *International Journal of Research and Innovation in Social Science*, 8(11). https://doi.org/10.47772/IJRISS.2024.8110251
1. OECD. (2024). *2023 OECD Digital Government Index: Results and key findings*. https://doi.org/10.1787/1a89ed5e-en
1. Okafor, E.E. (2019). The dictum, Igbo Enwe Eze. *Sociology and Philosophy*, 9(1). https://doi.org/10.4236/sm.2019.91005
1. Olson, M. (1965). *The Logic of Collective Action*. Harvard University Press.
1. Oman, C.P. (2006). *Uses and abuses of governance indicators*. OECD Development Centre.
1. Ostrom, E. (1990). *Governing the Commons*. Cambridge University Press.
1. Ottenberg, S. (1955). Improvement associations among the Afikpo Ibo. *Africa*, 25(1), 1-22.
1. Peffers, K., Tuunanen, T., Rothenberger, M.A., and Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45-77.
1. Quyen, D.T.N. (2014). Developing university governance indicators using a modified Delphi method. *Procedia - Social and Behavioral Sciences*, 141, 828-833.
1. Schneider, N. (2019). Decentralization: An incomplete ambition. *Journal of Cultural Economy*, 12(4), 265-285.
1. Singh, J., and Shah, P. (2003). Community scorecard process: A short note on the general methodology for implementation. *World Bank Social Development Notes*.
1. Suchman, M.C. (1995). Managing legitimacy: Strategic and institutional approaches. *Academy of Management Review*, 20(3), 571-610.
1. Tyler, T.R. (2006). *Why People Obey the Law*. Princeton University Press.
1. Uduku, O. (2002). The socio-economic basis of a diaspora community: *Igbo bu ike*. *African Affairs*, 101(404), 339-355.
1. United Nations DESA. (2024). *UN E-Government Survey 2024*. United Nations.
1. World Bank. (2025a). *GovTech Maturity Index 2025 update*.
1. World Justice Project. (2025). *WJP Rule of Law Index 2025: Methodology and sources*.
