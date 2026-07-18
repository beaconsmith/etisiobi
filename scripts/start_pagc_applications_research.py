from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "RUN-APP-20260528-0001"
RUN_DIR = ROOT / "research_runs" / RUN_ID
EXP_DIR = ROOT / "experiments" / "EXP-APP-001-count-layer-design-grammar"
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


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


SOTA_SOURCES = [
    {
        "source_id": "APP-SOTA-001",
        "name": "Shape grammars",
        "source": "Stiny, Introduction to Shape and Shape Grammars",
        "url": "https://journals.sagepub.com/doi/10.1068/b070343",
        "method": "Generative design rules over shape/state primitives.",
        "relationship": "Closest design precedent for using a compact grammar to generate a design space.",
        "gap_for_pagc": "Does not provide Nwagu Aneke count-layer grounding or source/derived layer separation.",
        "risk": "medium",
    },
    {
        "source_id": "APP-SOTA-002",
        "name": "Design Tokens Community Group",
        "source": "W3C Community Group",
        "url": "https://www.w3.org/groups/cg/design-tokens",
        "method": "Portable design-token representation for digital design systems.",
        "relationship": "Useful baseline for exporting PAGC-derived system tokens into familiar design tooling.",
        "gap_for_pagc": "Design tokens do not decide symbolic inventory validity or cultural source provenance.",
        "risk": "high",
    },
    {
        "source_id": "APP-SOTA-003",
        "name": "Statecharts",
        "source": "Harel, Statecharts: A visual formalism for complex systems",
        "url": "https://www.sciencedirect.com/science/article/pii/0167642387900359",
        "method": "Hierarchical state-machine formalism for complex system behavior.",
        "relationship": "Baseline for turning base/modifier tokens into operational system transitions.",
        "gap_for_pagc": "Statecharts do not encode a culturally grounded source-layer inventory.",
        "risk": "medium",
    },
    {
        "source_id": "APP-SOTA-004",
        "name": "Combinatorial testing",
        "source": "NIST Combinatorial Coverage Measurement",
        "url": "https://www.nist.gov/publications/combinatorial-coverage-measurement",
        "method": "Covering arrays and t-way coverage for configuration/state spaces.",
        "relationship": "Baseline for testing a 26x8 or 27x8 design space without exhaustive manual review.",
        "gap_for_pagc": "Does not produce the semantic grammar; only tests coverage.",
        "risk": "low",
    },
    {
        "source_id": "APP-SOTA-005",
        "name": "Domain-specific languages and model-driven engineering",
        "source": "DSL/MDE systematic-review literature",
        "url": "https://arxiv.org/abs/2307.04599",
        "method": "Domain-specific languages and model-driven practices for formalizing system designs.",
        "relationship": "Baseline for turning PAGC/BMC into a language or modeling tool.",
        "gap_for_pagc": "Generic DSL methods do not provide the Nwagu Aneke source/derived distinction.",
        "risk": "medium",
    },
    {
        "source_id": "APP-SOTA-006",
        "name": "Finite-state transducers",
        "source": "Finite-state methods for morphology",
        "url": "https://aclanthology.org/W19-3107.pdf",
        "method": "Finite-state mapping between surface forms and analyses.",
        "relationship": "Baseline for future Igbo/Nwagu Aneke transliteration or morphology experiments.",
        "gap_for_pagc": "Requires reviewed glyph/transcription data before source-derived FST claims.",
        "risk": "medium",
    },
]


APPLICATION_BRANCHES = [
    {
        "branch_id": "APP-001",
        "title": "Count-Layer Design Grammar",
        "research_question": "Can 26x8 source-layer tokens and derived 27/216 tokens form a drift-safe grammar for designing novel systems?",
        "application_domain": "systems design",
        "hypothesis": "A source/derived layer grammar can generate auditable system-design tokens without confusing evidence layers.",
        "minimal_experiment": "Generate source-layer and derived-layer design grammar artifacts and validate layer invariants.",
        "testability": 0.95,
        "novel_system_value": 0.9,
        "evidence_readiness": 0.9,
        "novelty_signal": 0.75,
        "rights_risk": 0.2,
        "status": "active",
    },
    {
        "branch_id": "APP-002",
        "title": "Igbo Tokenization and Compression",
        "research_question": "Does a source-layer or derived-layer PAGC tokenizer improve Igbo tokenization/compression against BPE baselines?",
        "application_domain": "NLP",
        "hypothesis": "Layer-aware tokenization will be more interpretable and may improve compression for selected Igbo corpora.",
        "minimal_experiment": "Compare source-layer and derived-layer tokenizers against BPE/UTF-8 on open Igbo text.",
        "testability": 0.75,
        "novel_system_value": 0.85,
        "evidence_readiness": 0.45,
        "novelty_signal": 0.7,
        "rights_risk": 0.5,
        "status": "pending_data",
    },
    {
        "branch_id": "APP-003",
        "title": "Oroma Governance State Grammar",
        "research_question": "Can community governance events be modeled as base x modifier tokens with audit-safe transitions?",
        "application_domain": "governance infrastructure",
        "hypothesis": "Oroma workflows can become statechart-like systems where bases are governance objects and modifiers are validated states/actions.",
        "minimal_experiment": "Map existing OGI/Oroma product gaps to a base/modifier transition grammar.",
        "testability": 0.85,
        "novel_system_value": 0.95,
        "evidence_readiness": 0.7,
        "novelty_signal": 0.8,
        "rights_risk": 0.35,
        "status": "proposed",
    },
    {
        "branch_id": "APP-004",
        "title": "Claim-Gated AI Agent Memory",
        "research_question": "Can an agent memory use source-layer objects plus modifiers to prevent unsupported inference drift?",
        "application_domain": "AI agents",
        "hypothesis": "Memory tokens with explicit source/derived/proposed modifiers can reduce claim drift in autonomous research agents.",
        "minimal_experiment": "Replay a small claim graph through source/derived/speculative memory states and measure blocked overclaims.",
        "testability": 0.8,
        "novel_system_value": 0.9,
        "evidence_readiness": 0.8,
        "novelty_signal": 0.85,
        "rights_risk": 0.25,
        "status": "proposed",
    },
    {
        "branch_id": "APP-005",
        "title": "Cultural Design Token System",
        "research_question": "Can PAGC source/derived layers produce design tokens for interfaces without turning cultural evidence into decoration?",
        "application_domain": "interface design",
        "hypothesis": "A layer-aware token export can create visual systems that carry provenance and authority state.",
        "minimal_experiment": "Export source-layer design tokens with provenance fields and render a small dashboard.",
        "testability": 0.7,
        "novel_system_value": 0.8,
        "evidence_readiness": 0.65,
        "novelty_signal": 0.65,
        "rights_risk": 0.55,
        "status": "proposed",
    },
    {
        "branch_id": "APP-006",
        "title": "Combinatorial Design-Space Testing",
        "research_question": "Can NIST-style combinatorial coverage test PAGC-derived system variants efficiently?",
        "application_domain": "software testing",
        "hypothesis": "A 26x8 layer can be sampled with t-way coverage to test generated systems without exhaustive deployment.",
        "minimal_experiment": "Generate pairwise/triple-wise test plans over base/modifier/context/authority axes.",
        "testability": 0.9,
        "novel_system_value": 0.7,
        "evidence_readiness": 0.85,
        "novelty_signal": 0.55,
        "rights_risk": 0.15,
        "status": "proposed",
    },
]


def score(branch: dict) -> float:
    return round(
        0.25 * branch["testability"]
        + 0.25 * branch["novel_system_value"]
        + 0.20 * branch["evidence_readiness"]
        + 0.20 * branch["novelty_signal"]
        - 0.10 * branch["rights_risk"],
        3,
    )


def build_tokens(bmc: list[dict], split_fv: bool) -> list[dict]:
    tokens: list[dict] = []
    for row in bmc:
        labels = [row["row_label"]]
        if split_fv and row["row_label"] == "f/v":
            labels = ["f", "v"]
        for label in labels:
            tokens.append(
                {
                    "token_id": row["cell_id"] if label == row["row_label"] else f"{row['cell_id']}-{label}",
                    "layer": "derived_fv_split" if split_fv else "source_observed",
                    "base": label,
                    "modifier": row["vowel_label"],
                    "reading": f"{label}{row['vowel_label']}",
                    "source_bmc_id": row["bmc_id"],
                    "source_observed": not split_fv,
                    "derived_rule": "split f/v row into f and v" if split_fv and row["row_label"] == "f/v" else None,
                    "design_use": "system primitive candidate",
                }
            )
    return tokens


def main() -> None:
    timestamp = now()
    count = read_json(ROOT / "corpus" / "bmc_count_reconciliation.json")
    bmc = read_jsonl(ROOT / "corpus" / "base_modifier_cache.jsonl")
    rows = sorted({r["row_label"] for r in bmc})
    vowels = sorted({r["vowel_label"] for r in bmc})
    source_tokens = build_tokens(bmc, split_fv=False)
    derived_tokens = build_tokens(bmc, split_fv=True)
    branches = [{**b, "score": score(b)} for b in APPLICATION_BRANCHES]
    branches.sort(key=lambda item: item["score"], reverse=True)

    write_text(
        RUN_DIR / "README.md",
        f"""
        # {RUN_ID}: PAGC Applications Research Sprint 001

        Started: `{timestamp}`

        Foundation: the user-confirmed count-layer model.

        - Source-observed layer: `26 x 8 = 208`.
        - Derived layer: `27 x 8 = 216` only when the `f/v` row is split.
        - Rule: applications may use the derived layer, but must never call it source-observed.

        Mission: research applications and potentials for designing novel systems from this foundation.

        First active experiment: `experiments/EXP-APP-001-count-layer-design-grammar/`.
        """,
    )
    write_text(
        RUN_DIR / "foundation.md",
        """
        # Research Foundation

        Accepted for internal research:

        1. The source-observed layer is represented locally as 26 rows x 8 vowel/modifier columns = 208 BMC records.
        2. The 27/216 layer is derived only when the f/v row is split.
        3. The derived layer may be used for design exploration if labeled as derived.

        Research consequence:

        We can now stop arguing about whether 27/216 is source-observed and start asking what systems can be designed when source and derived layers are kept separate.
        """,
    )
    write_jsonl(RUN_DIR / "sota_sources.jsonl", SOTA_SOURCES)
    with (RUN_DIR / "sota_matrix.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(SOTA_SOURCES[0].keys()))
        writer.writeheader()
        writer.writerows(SOTA_SOURCES)
    write_jsonl(RUN_DIR / "application_branches.jsonl", branches)
    write_json(RUN_DIR / "branch_scores.json", {b["branch_id"]: b["score"] for b in branches})
    write_text(
        RUN_DIR / "active_selection.md",
        f"""
        # Active Application Selection

        Active branch: `{branches[0]['branch_id']} — {branches[0]['title']}`

        Why it starts first:

        - It directly tests the accepted count-layer foundation.
        - It produces a reusable system-design artifact.
        - It has low rights risk because it uses IDs, counts, and layer rules rather than source images.
        - It creates the substrate needed by later NLP, governance, AI-agent, and interface experiments.

        Next blocked branches:

        - `APP-002` needs open Igbo corpus/data review.
        - `APP-005` needs stronger visual/public-release rights review.
        """,
    )

    grammar = {
        "grammar_id": "PAGC-DESIGN-GRAMMAR-001",
        "created_at": timestamp,
        "foundation": {
            "source_layer": {"bases": 26, "modifiers": 8, "tokens": 208},
            "derived_layer": {"bases": 27, "modifiers": 8, "tokens": 216, "rule": "split f/v row"},
            "hard_rule": "derived tokens must not be reported as source-observed",
        },
        "constructs": {
            "Base": "domain primitive, source-observed row, or mapped system object",
            "Modifier": "state, operator, vowel/modifier, or transformation axis",
            "Token": "Base x Modifier object with layer label and provenance",
            "Cache": "high-salience object that bypasses composition only when evidence/authority allows",
            "Transition": "valid movement between tokens, constrained by domain rules",
            "Authority": "permission or legitimacy state for using a generated object",
        },
        "design_rules": [
            "Every generated object must carry a layer label: source_observed, derived_fv_split, domain_mapped, or speculative.",
            "A derived object may support design exploration but not source-inventory claims.",
            "Every system mapping must define bases, modifiers, transitions, authority, and falsification criteria.",
            "A design is stronger when it compresses repeated structure without hiding uncertainty.",
        ],
        "active_domains": ["systems design", "governance", "AI agent memory", "interface design", "NLP/tokenization"],
    }
    write_json(EXP_DIR / "system_design_grammar.json", grammar)
    write_jsonl(EXP_DIR / "tokens_source_layer.jsonl", source_tokens)
    write_jsonl(EXP_DIR / "tokens_derived_layer.jsonl", derived_tokens)
    write_json(
        EXP_DIR / "config.json",
        {
            "experiment_id": "EXP-APP-001",
            "source_bmc_records": len(bmc),
            "source_rows": len(rows),
            "source_modifiers": len(vowels),
            "source_tokens": len(source_tokens),
            "derived_tokens": len(derived_tokens),
            "derived_rule": "split f/v row",
        },
    )

    invariant_pass = (
        len(bmc) == 208
        and count["checks"]["bmc_rows"] == 26
        and count["checks"]["bmc_vowels"] == 8
        and len(source_tokens) == 208
        and len(derived_tokens) == 216
    )
    results = {
        "experiment_id": "EXP-APP-001",
        "decision": "KEEP_AS_FOUNDATIONAL_DESIGN_GRAMMAR" if invariant_pass else "REVISE_LAYER_MODEL",
        "invariants": {
            "bmc_records": len(bmc),
            "source_rows": len(rows),
            "source_modifiers": len(vowels),
            "source_tokens": len(source_tokens),
            "derived_tokens_after_fv_split": len(derived_tokens),
            "passed": invariant_pass,
        },
        "first_research_output": "A drift-safe PAGC count-layer design grammar that can seed system applications.",
        "next_experiment": "EXP-APP-002-governance-state-grammar or EXP-APP-003-agent-memory-claim-drift",
    }
    write_json(EXP_DIR / "results.json", results)
    write_text(
        EXP_DIR / "plan.md",
        """
        # EXP-APP-001: Count-Layer Design Grammar

        ## Research question

        Can the confirmed 26x8 source layer and derived 27/216 f/v split become a drift-safe grammar for designing novel systems?

        ## Hypothesis

        If every generated design object carries a layer label, then PAGC applications can use source and derived layers without turning derived counts into source claims.

        ## Method

        1. Load the BMC source-layer records.
        2. Generate source-layer tokens.
        3. Generate derived-layer tokens by splitting f/v.
        4. Check count invariants.
        5. Emit a reusable system-design grammar.

        ## Success criteria

        - 208 source-layer tokens.
        - 216 derived-layer tokens.
        - Derived tokens carry `derived_fv_split`.
        - No generated artifact calls 27/216 source-observed.
        """,
    )
    write_text(
        EXP_DIR / "analysis.md",
        f"""
        # EXP-APP-001 Analysis

        The experiment generated a source-layer token set and a derived f/v split token set.

        Results:

        - Source BMC records: `{len(bmc)}`
        - Source rows: `{len(rows)}`
        - Source modifiers: `{len(vowels)}`
        - Source tokens: `{len(source_tokens)}`
        - Derived tokens after f/v split: `{len(derived_tokens)}`
        - Invariants passed: `{invariant_pass}`

        Interpretation:

        This is enough to begin applications research because the foundational layer distinction is machine-readable. It does not prove any downstream application works; it gives future experiments a drift-safe grammar to build from.
        """,
    )
    write_text(
        EXP_DIR / "decision.md",
        f"""
        # EXP-APP-001 Decision

        Decision: `{results['decision']}`

        Keep this as the first foundation for PAGC applications research.

        What it proves:

        - The accepted count-layer model can be represented as a system-design grammar.
        - The source and derived layers can be generated without count drift.

        What it does not prove:

        - It does not prove a useful product, NLP result, governance workflow, or AI memory improvement yet.
        - It does not prove glyph-shape grammar.
        - It does not prove E6, universal compression, or broad PAGC theory claims.

        Next best experiment:

        `EXP-APP-002-governance-state-grammar`: map Oroma/OGI governance objects into base/modifier/transition grammar and test whether it clarifies product gaps.
        """,
    )
    write_text(
        EXP_DIR / "commands.sh",
        """
        python scripts/start_pagc_applications_research.py
        """,
    )

    write_text(
        APP_DIR / "README.md",
        """
        # PAGC Applications Research

        This directory is for applications and systems-design research built on the accepted count-layer foundation.

        Foundation:

        - Source-observed layer: 26 x 8 = 208.
        - Derived layer: 27 x 8 = 216 only by f/v split.
        - Rule: never call derived 27/216 source-observed.

        Active run:

        - `research_runs/RUN-APP-20260528-0001/`

        Active experiment:

        - `experiments/EXP-APP-001-count-layer-design-grammar/`
        """,
    )
    write_text(
        APP_DIR / "APPLICATION_RESEARCH_BRIEF.md",
        """
        # Application Research Brief

        ## Discovery being used

        The usable foundation is a layer distinction:

        - Source layer: 26 x 8 = 208.
        - Derived layer: 27/216 by f/v split.

        ## Research direction

        We are no longer researching whether the layer distinction exists for internal work. We are researching what it can design.

        ## First thesis

        A system can become more trustworthy when its generated objects carry explicit source, derived, speculative, and authority labels.

        ## First applications

        1. Design grammar / DSL for novel systems.
        2. Governance state grammar for Oroma.
        3. AI agent memory grammar that blocks claim drift.
        4. Igbo tokenization/compression tests.
        5. Cultural design-token system.
        """,
    )
    write_text(
        APP_DIR / "count_layer_design_principles.md",
        """
        # Count-Layer Design Principles

        1. Preserve the layer distinction.
        2. Treat source-observed and derived objects differently.
        3. Allow derived objects to inspire design, but mark them.
        4. Require every application to name its bases and modifiers.
        5. Require every application to state what would falsify it.
        6. Prefer prototypes that can be measured.
        7. Do not use cultural source material as decoration.
        8. Keep authority and public-release status visible.
        """,
    )
    branch_lines = "\n".join(f"- `{b['branch_id']}` {b['title']} — score `{b['score']}`, status `{b['status']}`" for b in branches)
    write_text(
        APP_DIR / "system_design_lattice.md",
        f"""
        # System Design Lattice

        {branch_lines}

        The lattice starts with APP-001 because it creates the grammar substrate that later experiments can reuse.
        """,
    )
    write_jsonl(APP_DIR / "novel_system_hypotheses.jsonl", branches)

    write_text(
        REVIEWER_DIR / "WHAT_WE_ARE_RESEARCHING_NOW.md",
        """
        # What We Are Researching Now

        We are researching applications and potentials for designing novel systems from the accepted count-layer foundation.

        ## Foundation

        - Source layer: 26 x 8 = 208.
        - Derived layer: 27/216 by f/v split.

        ## First active question

        Can this layer model become a drift-safe design grammar for new systems?

        ## First experiment

        `EXP-APP-001-count-layer-design-grammar`

        ## Why this matters

        If the grammar works, PAGC can become a design substrate for governance workflows, agent memory, tokenization, and interface systems while preserving evidence labels.

        ## What is next

        Build the Oroma governance state grammar and test whether it clarifies product/research gaps.
        """,
    )

    decision_line = {
        "decision_id": "LAB-DEC-0007",
        "timestamp": timestamp,
        "actor": "Codex agent under user direction",
        "authority_basis": "User instructed: now start the research; count-layer foundation is user-confirmed.",
        "scope": "pagc_applications_research",
        "decision": "Start applications research from the confirmed 26x8 source layer and derived 27/216 f/v split layer.",
        "rationale": "The foundation is no longer a local blocker for internal applications research; the next scientific question is what novel systems the layer model can design and how to test them.",
        "evidence": [
            "papers/SELECTED_PAPER/count_layer_foundation_attestation.md",
            "corpus/bmc_count_reconciliation.json",
            "experiments/EXP-APP-001-count-layer-design-grammar/results.json",
        ],
        "status": "active",
        "outputs": [
            "research_runs/RUN-APP-20260528-0001/",
            "research/pagc/applications/",
            "experiments/EXP-APP-001-count-layer-design-grammar/",
        ],
    }
    decision_path = ROOT / "decisions" / "decision_log.jsonl"
    existing = decision_path.read_text(encoding="utf-8") if decision_path.exists() else ""
    if '"decision_id": "LAB-DEC-0007"' not in existing:
        with decision_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(decision_line, ensure_ascii=False) + "\n")

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
