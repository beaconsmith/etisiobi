# Section 3: Problem Environment — The Coordination Paradox

The design of the Oroma Coordination OS is motivated by the "Coordination Paradox" observed in informal community institutions: these entities possess high social capital and moral legitimacy but suffer from low administrative durability and "procedural drift." In the context of Southeast Nigerian town unions, this paradox manifests in three specific failure modes.

## 3.1 The Recall-Trust Gap
Governance in these institutions is traditionally "oral-first." Decisions made in village assemblies or town union meetings are stored in the collective memory of the participants rather than in accessible, immutable records. This reliance on social recall creates a "Trust Gap" whenever a decision is contested months later. Without a verifiable artifact, the dispute often devolves into personality conflicts or leadership crises, undermining the institution's legitimacy.

## 3.2 The "Zombie Proposal" Phenomenon
Proposals for community development (e.g., road maintenance, security funding) frequently enter a state of perpetual limbo. Because there is no formal deliberative state machine, a project may be "approved in principle" but never move to execution because the specific conditions, multi-signature requirements, or milestone tracking were never formalized. These "Zombie Proposals" drain community energy and discourage future collective action.

## 3.3 Information Asymmetry and Elite Capture
The opacity of paper-based or oral records allows for information asymmetry between the executive committee (the "elite") and the general membership. This asymmetry is the primary driver of elite capture, where community resources are diverted to projects that benefit a few rather than the many. The lack of a "legible" ledger of decisions and treasury state transitions prevents the broader community from exercising effective oversight.

## 3.4 Requirements for a Coordination OS
To address these failures, the problem environment requires an artifact that satisfies four core requirements:
1. **Durability:** Records must persist beyond the memory of current officers.
2. **Verifiability:** State transitions must be provable to any community member.
3. **Norm Enforcement:** Governance rules must be embedded in the coordination tool itself.
4. **Legibility:** Internal community state must be understandable to external partners (e.g., NGOs, State Government).
