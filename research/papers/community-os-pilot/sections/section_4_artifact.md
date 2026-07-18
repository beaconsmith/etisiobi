# Section 4: Artifact Description — The Oroma Coordination OS

This section describes the design and implementation of the Oroma Coordination OS, a design science artifact developed to address the coordination failures in informal community institutions. Following the "build-and-evaluate" loop (Hevner et al. 2004), the artifact embodies seven key design decisions derived from the problem environment of Southeast Nigerian town unions.

## 4.1 System Architecture: The "DB-Primary, Chain-Legible" Hybrid
The core architectural decision (DD-01) is a hybrid state management system. 
- **Off-chain database (PostgreSQL)** serves as the primary source of truth for high-velocity coordination (meeting minutes, member presence, proposal drafts).
- **On-chain registry (EVM-compatible)** acts as the immutable anchor for high-integrity state transitions (e.g., membership issuance, treasury disbursements).
This hybrid approach balances the need for low-latency user experience with the requirement for verifiable, non-repudiable institutional memory.

## 4.2 Modular Institutional Logic
Oroma utilizes a modular smart contract suite (DD-02) to replicate the polycentric nature of community governance:
1. **Registry Contract:** Manages identity and roles (e.g., *Ichi* credentials).
2. **Treasury Contract:** Enforces multi-signature approval for community funds.
3. **Program/Proposal Contracts:** Manage the lifecycle of community projects from deliberation to execution.

## 4.3 Service-Level Enforcement of Governance Norms
Rather than relying on social pressure alone, Oroma implements service-enforced logic (DD-03). For example, a treasury disbursement is technically impossible without the digital signatures of the required trustees as defined in the community's registry. This "code-as-constitution" approach (Lessig 2006) provides the "receipts" necessary to transition from recall-based to artifact-based trust.

## 4.4 Verifiable Credentials for Membership (Ichi)
Membership in the digital institution is anchored in verifiable credentials (DD-04), mapping the traditional *Ichi* status to a digital primitive. This ensures that only verified community members can participate in governance, mitigating the risk of elite capture or external interference.

## 4.5 The Artifact-First Data Schema
The data schema is designed to enforce the "artifact-first" principle (DD-05). Every transaction (e.g., a meeting record) must include specific metadata (TTI-01) such as a purpose statement (min 50 chars) and a reference to a parent proposal. This ensures that the system generates a structured, audit-ready evidence trail.

## 4.6 Deliberative State Machines
The lifecycle of community decisions is managed through formal state machines (DD-06). Proposals move through *Draft*, *Active*, *Finalizing*, and *Closed* states. This transition logic ensures that "dispute state machine closure" is a required terminal state, preventing the "zombie proposals" common in informal paper-based systems.

## 4.7 Multi-Modal Accessibility
Recognizing the digital divide, the artifact supports multi-modal interaction (DD-07), allowing officers with high-capability devices to anchor records while maintaining accessibility for members via lower-bandwidth interfaces.
