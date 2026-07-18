from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
EXP_DIR = ROOT / "experiments" / "EXP-APP-002-governance-state-grammar"
APP_DIR = ROOT / "research" / "pagc" / "applications"
REVIEWER_DIR = ROOT / "outputs" / "reviewer_packet"


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def clean(text: str) -> str:
    stripped = dedent(text).strip()
    return "\n".join(line[8:] if line.startswith("        ") else line for line in stripped.splitlines())


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(text) + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


GOVERNANCE_BASES = [
    {
        "base_id": "GOV-BASE-001",
        "base": "Proposal",
        "source": "research/papers/community-os-pilot sections; OGI proposal indicators",
        "meaning": "A community decision candidate that must move through deliberation and closure states.",
    },
    {
        "base_id": "GOV-BASE-002",
        "base": "TreasuryMovement",
        "source": "TTI-01/TTI-02 indicator definitions",
        "meaning": "A contribution, disbursement, hold, or solvency proof event tied to authorizing evidence.",
    },
    {
        "base_id": "GOV-BASE-003",
        "base": "DisputeCase",
        "source": "DRL-01/DRL-02/DRL-03 indicator definitions",
        "meaning": "A conflict or adjudication object requiring claims, evidence, findings, resolution, and closure.",
    },
    {
        "base_id": "GOV-BASE-004",
        "base": "IchiCredential",
        "source": "CPS-01 indicator and community-os-pilot paper",
        "meaning": "A portable membership/standing credential backed by governance-event evidence.",
    },
    {
        "base_id": "GOV-BASE-005",
        "base": "ParticipantOnboarding",
        "source": "FID-01 indicator definition",
        "meaning": "A wallet/member creation event with consented first-time-participation signal.",
    },
    {
        "base_id": "GOV-BASE-006",
        "base": "Record",
        "source": "CAS-01 and RV-01 evidence classes",
        "meaning": "A verifiable community record with export/provenance status.",
    },
]


GOVERNANCE_MODIFIERS = [
    {
        "modifier_id": "GOV-MOD-001",
        "modifier": "Created",
        "semantics": "object exists but is not yet evidence-complete",
        "pagc_layer_analogy": "source-layer token: base + initial state",
    },
    {
        "modifier_id": "GOV-MOD-002",
        "modifier": "EvidenceAttached",
        "semantics": "minimum source/evidence fields are attached",
        "pagc_layer_analogy": "modifier marks observable support",
    },
    {
        "modifier_id": "GOV-MOD-003",
        "modifier": "AuthorityChecked",
        "semantics": "actor/role/community authority check passed",
        "pagc_layer_analogy": "authority modifier",
    },
    {
        "modifier_id": "GOV-MOD-004",
        "modifier": "ProvenanceAnchored",
        "semantics": "blockRef/txRef/hash lineage is present",
        "pagc_layer_analogy": "source locator modifier",
    },
    {
        "modifier_id": "GOV-MOD-005",
        "modifier": "Closed",
        "semantics": "terminal state reached with required closure evidence",
        "pagc_layer_analogy": "state-stabilization modifier",
    },
    {
        "modifier_id": "GOV-MOD-006",
        "modifier": "Exported",
        "semantics": "object is portable outside the platform",
        "pagc_layer_analogy": "routing modifier",
    },
    {
        "modifier_id": "GOV-MOD-007",
        "modifier": "Contested",
        "semantics": "outcome challenged or case reopened",
        "pagc_layer_analogy": "revision/uncertainty modifier",
    },
    {
        "modifier_id": "GOV-MOD-008",
        "modifier": "ReleaseBlocked",
        "semantics": "sensitive data, consent, or authority blocker prevents publication/export",
        "pagc_layer_analogy": "gate modifier",
    },
]


REQUIRED_TRANSITIONS = [
    {
        "transition_id": "GOV-TRANS-001",
        "base": "DisputeCase",
        "from": "Created",
        "to": "Closed",
        "guard": "findings != null AND resolution != null AND evidence_refs count >= 1",
        "ogi_indicator": "DRL-01",
        "current_gap": "cases.findings/resolution/evidence_refs not enforced on closure",
        "contradiction": "CONT-001",
        "product_requirement": "Block case closure unless evidence fields are populated.",
        "acceptance_test": "Attempt to close a dispute without findings/resolution/evidence_refs fails.",
    },
    {
        "transition_id": "GOV-TRANS-002",
        "base": "TreasuryMovement",
        "from": "Created",
        "to": "ProvenanceAnchored",
        "guard": "purpose length >= 50 AND proposalId != null AND provenance.blockRef != null",
        "ogi_indicator": "TTI-01",
        "current_gap": "purpose/proposal linkage enforcement is partial",
        "contradiction": "research/REGISTRY.md TTI-01 blocker",
        "product_requirement": "Enforce treasury metadata at service/contract level.",
        "acceptance_test": "Treasury event with short purpose or missing proposalId/blockRef is rejected.",
    },
    {
        "transition_id": "GOV-TRANS-003",
        "base": "TreasuryMovement",
        "from": "EvidenceAttached",
        "to": "Closed",
        "guard": "domain_event == treasury.solvency_proof_generated AND verifiedOnChain == true",
        "ogi_indicator": "TTI-02",
        "current_gap": "treasury.solvency_proof_generated event missing",
        "contradiction": "CONT-002",
        "product_requirement": "Emit domain event on ZK solvency proof generation.",
        "acceptance_test": "Verified solvency proof writes a treasury.solvency_proof_generated event with proofHash, verifiedOnChain, balanceThreshold, and txRef.",
    },
    {
        "transition_id": "GOV-TRANS-004",
        "base": "IchiCredential",
        "from": "AuthorityChecked",
        "to": "Exported",
        "guard": "domain_event == credential.exported AND evidenceEventCount >= minimum threshold",
        "ogi_indicator": "CPS-01",
        "current_gap": "credential.exported event missing",
        "contradiction": "CONT-003",
        "product_requirement": "Emit credential.exported event on Ichi credential export.",
        "acceptance_test": "Credential export creates event with credentialType, evidenceEventCount, and exportTarget.",
    },
    {
        "transition_id": "GOV-TRANS-005",
        "base": "ParticipantOnboarding",
        "from": "Created",
        "to": "EvidenceAttached",
        "guard": "domain_event == member.onboarding_survey_submitted AND firstTimeParticipant is boolean",
        "ogi_indicator": "FID-01",
        "current_gap": "onboarding survey event missing",
        "contradiction": "CONT-004",
        "product_requirement": "Add one-question onboarding survey and event at wallet creation.",
        "acceptance_test": "Wallet creation can submit firstTimeParticipant and writes member.onboarding_survey_submitted.",
    },
    {
        "transition_id": "GOV-TRANS-006",
        "base": "DisputeCase",
        "from": "Closed",
        "to": "Contested",
        "guard": "domain_event == case.reopened AND reopeningReason != null",
        "ogi_indicator": "DRL-02",
        "current_gap": "case.reopened event missing",
        "contradiction": "extractor KNOWN_PRODUCT_GAPS",
        "product_requirement": "Emit case.reopened event with reason and actor authority.",
        "acceptance_test": "Reopened case writes event and links to original closed case.",
    },
    {
        "transition_id": "GOV-TRANS-007",
        "base": "ParticipantOnboarding",
        "from": "EvidenceAttached",
        "to": "ReleaseBlocked",
        "guard": "demographic data requested without workspace consent / ethics clearance",
        "ogi_indicator": "FID-02/FID-03",
        "current_gap": "gender/diaspora fields require governance policy decision",
        "contradiction": "CONT-005",
        "product_requirement": "Route demographic fields through policy/community consent before schema implementation.",
        "acceptance_test": "System blocks demographic collection until policy and workspace consent records exist.",
    },
]


def build_state_tokens() -> list[dict]:
    rows = []
    for base in GOVERNANCE_BASES:
        for modifier in GOVERNANCE_MODIFIERS:
            rows.append(
                {
                    "token_id": f"{base['base_id']}:{modifier['modifier_id']}",
                    "base": base["base"],
                    "modifier": modifier["modifier"],
                    "meaning": f"{base['base']} / {modifier['modifier']}",
                    "source": base["source"],
                    "semantics": modifier["semantics"],
                    "layer": "domain_mapped_from_pagc_count_layer",
                    "evidence_status": "derived_design_hypothesis",
                }
            )
    return rows


def main() -> None:
    timestamp = now()
    state_tokens = build_state_tokens()
    blocked = [row for row in REQUIRED_TRANSITIONS if row["current_gap"]]
    result = {
        "experiment_id": "EXP-APP-002",
        "created_at": timestamp,
        "decision": "KEEP_AS_PRODUCT_RESEARCH_BRANCH",
        "bases": len(GOVERNANCE_BASES),
        "modifiers": len(GOVERNANCE_MODIFIERS),
        "state_tokens": len(state_tokens),
        "required_transitions": len(REQUIRED_TRANSITIONS),
        "blocked_or_partial_transitions": len(blocked),
        "finding": "The PAGC-derived governance grammar exposes OGI computability gaps as missing state transitions and guards.",
        "next_action": "Turn GOV-TRANS-001 through GOV-TRANS-005 into product tickets and negative tests in Oroma.",
    }

    write_jsonl(EXP_DIR / "governance_bases.jsonl", GOVERNANCE_BASES)
    write_jsonl(EXP_DIR / "governance_modifiers.jsonl", GOVERNANCE_MODIFIERS)
    write_jsonl(EXP_DIR / "governance_state_tokens.jsonl", state_tokens)
    write_jsonl(EXP_DIR / "required_transitions.jsonl", REQUIRED_TRANSITIONS)
    write_json(EXP_DIR / "results.json", result)
    write_text(
        EXP_DIR / "plan.md",
        """
        # EXP-APP-002: Governance State Grammar

        ## Research question

        Can the accepted PAGC count-layer grammar clarify Oroma/OGI product gaps by representing governance evidence as base x modifier x transition objects?

        ## Hypothesis

        If OGI indicators are mapped into base/modifier transition grammar, missing research evidence will appear as missing product guards, events, or terminal states.

        ## Method

        1. Define governance bases from OGI/Oroma research objects.
        2. Define eight governance modifiers as evidence/authority/provenance/state operators.
        3. Generate governance state tokens.
        4. Map known OGI contradictions to required transitions and guards.
        5. Record product requirements and acceptance tests.
        """,
    )
    write_text(
        EXP_DIR / "analysis.md",
        f"""
        # EXP-APP-002 Analysis

        Generated governance grammar:

        - Bases: `{len(GOVERNANCE_BASES)}`
        - Modifiers: `{len(GOVERNANCE_MODIFIERS)}`
        - State tokens: `{len(state_tokens)}`
        - Required transitions: `{len(REQUIRED_TRANSITIONS)}`
        - Blocked or partial transitions: `{len(blocked)}`

        Main finding:

        The PAGC-derived grammar is useful when it turns a vague product gap into a missing transition guard. Example: DRL-01 is no longer just "dispute documentation incomplete"; it becomes:

        `DisputeCase.Created -> DisputeCase.Closed` requires `findings`, `resolution`, and `evidence_refs`.

        That is an implementable acceptance test.

        Research value:

        The grammar creates a bridge between cultural/source-layer formalization and product evidence design without claiming that the source layer itself directly encodes governance.
        """,
    )
    transition_rows = "\n".join(
        f"| {row['transition_id']} | {row['base']} | {row['from']} -> {row['to']} | {row['ogi_indicator']} | {row['product_requirement']} |"
        for row in REQUIRED_TRANSITIONS
    )
    write_text(
        EXP_DIR / "decision.md",
        f"""
        # EXP-APP-002 Decision

        Decision: `{result['decision']}`

        Keep this as the first product-connected application branch.

        What it discovered:

        The PAGC count-layer grammar can act as a product-research compiler: it turns OGI computability gaps into explicit state transitions, guards, and acceptance tests.

        | Transition | Base | Move | Indicator | Product requirement |
        |---|---|---|---|---|
        {transition_rows}

        What it does not prove:

        - It does not prove Oroma already implements these transitions.
        - It does not prove empirical governance improvement.
        - It does not prove the Nwagu Aneke source layer encodes governance semantics.

        Next best action:

        Implement or file tickets for the first five transition guards, then run the OGI extractor to see which indicators become computable.
        """,
    )
    write_text(
        EXP_DIR / "commands.sh",
        """
        python scripts/run_pagc_governance_state_grammar.py
        """,
    )

    write_text(
        APP_DIR / "governance_state_grammar.md",
        f"""
        # PAGC-Inspired Governance State Grammar

        Status: `ACTIVE_PRODUCT_RESEARCH_BRANCH`

        This grammar maps Oroma/OGI governance evidence into base x modifier state tokens. It is inspired by the accepted PAGC count-layer foundation but does not claim that Nwagu Aneke directly encodes governance semantics.

        ## Core Discovery

        OGI computability gaps can be represented as missing transitions:

        - DRL-01 needs `DisputeCase.Created -> DisputeCase.Closed` guarded by findings, resolution, and evidence references.
        - TTI-01 needs `TreasuryMovement.Created -> TreasuryMovement.ProvenanceAnchored` guarded by purpose, proposalId, and blockRef.
        - TTI-02 needs `TreasuryMovement.EvidenceAttached -> TreasuryMovement.Closed` guarded by a solvency-proof event.
        - CPS-01 needs `IchiCredential.AuthorityChecked -> IchiCredential.Exported`.
        - FID-01 needs `ParticipantOnboarding.Created -> ParticipantOnboarding.EvidenceAttached`.

        ## Result

        See `experiments/EXP-APP-002-governance-state-grammar/results.json`.
        """,
    )
    write_json(APP_DIR / "governance_state_grammar.json", {
        "bases": GOVERNANCE_BASES,
        "modifiers": GOVERNANCE_MODIFIERS,
        "transitions": REQUIRED_TRANSITIONS,
        "result": result,
    })
    write_text(
        REVIEWER_DIR / "PAGC_APPLICATION_DISCOVERY_001.md",
        """
        # PAGC Application Discovery 001

        ## New discovery

        The accepted PAGC count-layer model is useful as a product-research grammar for Oroma/OGI. It turns abstract research blockers into explicit missing product transitions.

        ## Why it matters

        OGI indicators become computable only when the product enforces the right event, field, and authority transitions. The grammar makes those transitions visible and testable.

        ## Example

        DRL-01 becomes:

        `DisputeCase.Created -> DisputeCase.Closed`

        Guard:

        `findings != null AND resolution != null AND evidence_refs count >= 1`

        Acceptance test:

        Closing a dispute without those fields must fail.

        ## What to build next

        Turn GOV-TRANS-001 through GOV-TRANS-005 into Oroma product tickets and negative tests.
        """,
    )
    ticket_rows = "\n".join(
        f"| {row['transition_id']} | {row['ogi_indicator']} | {row['product_requirement']} | {row['acceptance_test']} |"
        for row in REQUIRED_TRANSITIONS[:5]
    )
    write_text(
        EXP_DIR / "oroma_product_tickets.md",
        f"""
        # Oroma Product Tickets from PAGC Governance Grammar

        These are the first implementation tickets implied by EXP-APP-002. They are research-derived product requirements, not proof that the product already satisfies them.

        | Ticket | Indicator | Requirement | Acceptance test |
        |---|---|---|---|
        {ticket_rows}

        ## Priority

        1. `GOV-TRANS-001` because DRL-01 is closest to a concrete state-machine closure invariant.
        2. `GOV-TRANS-002` because TTI-01 is structurally computable once metadata is enforced.
        3. `GOV-TRANS-004` because CPS-01 requires a clear export event.
        4. `GOV-TRANS-005` because FID-01 needs one consented onboarding event.
        5. `GOV-TRANS-003` because TTI-02 depends on a heavier ZK solvency-proof workflow.
        """,
    )
    write_text(
        APP_DIR / "oroma_product_tickets.md",
        f"""
        # Oroma Product Tickets from PAGC Governance Grammar

        Source experiment: `experiments/EXP-APP-002-governance-state-grammar/`

        | Ticket | Indicator | Requirement | Acceptance test |
        |---|---|---|---|
        {ticket_rows}

        Next command:

        `python scripts/run_pagc_governance_state_grammar.py`
        """,
    )

    decision_line = {
        "decision_id": "LAB-DEC-0008",
        "timestamp": timestamp,
        "actor": "Codex agent under user direction",
        "authority_basis": "User instructed to proceed with applications research.",
        "scope": "pagc_governance_state_grammar",
        "decision": "Keep EXP-APP-002 as the first product-connected PAGC applications branch.",
        "rationale": "The grammar translates OGI computability gaps into product state transitions, guards, and acceptance tests.",
        "evidence": [
            "experiments/EXP-APP-002-governance-state-grammar/results.json",
            "research/pagc/applications/governance_state_grammar.md",
            "research/icegov/contradictions/",
        ],
        "status": "active",
        "outputs": [
            "experiments/EXP-APP-002-governance-state-grammar/",
            "research/pagc/applications/governance_state_grammar.md",
            "outputs/reviewer_packet/PAGC_APPLICATION_DISCOVERY_001.md",
        ],
    }
    decision_path = ROOT / "decisions" / "decision_log.jsonl"
    existing = decision_path.read_text(encoding="utf-8") if decision_path.exists() else ""
    if '"decision_id": "LAB-DEC-0008"' not in existing:
        with decision_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(decision_line, ensure_ascii=False) + "\n")

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
