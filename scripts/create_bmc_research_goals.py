from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now(timezone.utc).date().isoformat()
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()


GOALS = [
    {
        "id": "GOAL-001",
        "slug": "base-modifier-cache-formal-reconstruction",
        "title": "Base Modifier Cache Formal Reconstruction",
        "status": "active",
        "readiness": "active",
        "risk": "medium",
        "paper_potential": "high",
        "question": "Can the lab reconstruct every observed symbolic unit as a base-plus-modifier object with explicit provenance, certainty, source location, and claim dependency?",
        "novelty": "The Base Modifier Cache may be a novel evidence-gated symbolic substrate that links annotation, TEI, IIIF, certainty, provenance, knowledge graph, and publication claims.",
        "required_evidence": [
            "glyph annotation records",
            "cell-grid records",
            "TEI row and vowel inventory",
            "IIIF canvas and source locators",
            "certainty records",
            "provenance graph",
            "lineage records",
            "knowledge graph records",
            "authority approval records",
        ],
        "minimal_experiment": "Generate corpus/base_modifier_cache.jsonl and verify that every BMC object links to source, certainty, provenance, lineage, and claim dependencies.",
        "success": [
            "Every verified BMC object has a source locator.",
            "Every verified BMC object has a certainty score.",
            "Every exact-count claim can be traced to BMC records.",
            "Ambiguous records are preserved rather than forced.",
            "Contradictions are surfaced.",
        ],
        "failure": [
            "BMC objects cannot be grounded in source evidence.",
            "Exact counts disagree without an abstraction-layer explanation.",
            "Certainty records are missing or unusable.",
            "Authority constraints block publication use.",
        ],
        "falsification": "If source artifacts cannot support stable base/modifier decomposition, BMC must be downgraded from formal substrate to working annotation index.",
        "ultimate": "A reproducible BMC dataset, claim gate, and paper-ready method section, or a clear negative result showing why BMC cannot yet support theory claims.",
        "contribution": "We introduce a provenance-backed Base Modifier Cache that converts source-localized glyph annotations into auditable symbolic units.",
        "experiment": "experiments/EXP-BMC-001/",
        "human_review": ["authority/cultural review", "exact-count review", "source transcription review"],
        "dependencies": [],
        "next_action": "Create and validate corpus/base_modifier_cache.jsonl from local annotation, TEI, IIIF, certainty, lineage, provenance, and KG artifacts.",
        "scores": {
            "evidence_strength": 0.72,
            "novelty_potential": 0.78,
            "falsifiability": 0.80,
            "reproducibility": 0.85,
            "cultural_source_integrity": 0.80,
            "paper_fit": 0.82,
            "safety": 0.85,
            "unresolved_contradiction_risk": 0.35,
        },
    },
    {
        "id": "GOAL-002",
        "slug": "bmc-count-reconciliation",
        "title": "BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims",
        "status": "active",
        "readiness": "active_after_goal_001_seed",
        "risk": "medium",
        "paper_potential": "high",
        "question": "Does the BMC support a stable 26-row by 8-vowel, 208-cell structure, and how does that interact with 26/27/28 PAGC base or foundation claims?",
        "novelty": "The BMC may function as a count-audit engine that prevents symbolic theory claims from depending on unstable inventory counts.",
        "required_evidence": [
            "TEI row inventory",
            "TEI vowel inventory",
            "glyph annotation row labels",
            "cell grid records",
            "knowledge graph nodes",
            "certainty records",
            "release manifest",
            "PAGC foundation/base claims",
            "paper claims",
        ],
        "minimal_experiment": "Compare TEI rows, TEI vowels, glyph annotations, cell grid records, KG units, certainty records, and PAGC count claims.",
        "success": [
            "Rows, vowels, and cells reconcile at a declared abstraction layer.",
            "The 26/27/28 distinction is represented as layer-specific rather than flattened.",
            "Unsupported exact-count claims are downgraded or blocked.",
            "A count-resolution decision is recorded.",
        ],
        "failure": [
            "BMC counts disagree with source inventories without explanation.",
            "PAGC claims depend on 27 bases without a separate abstraction layer.",
            "The audit cannot locate count-bearing evidence.",
        ],
        "falsification": "If BMC supports 26 rows and 208 cells while PAGC theory depends on 27 bases without a separately defined abstraction layer, the 27-base claim must be marked unstable or overclaimed.",
        "ultimate": "A count-resolution decision: RESOLVED_26, RESOLVED_27, RESOLVED_28, MULTI_LAYER_COUNT_VALID, UNRESOLVED_SOURCE_CONFLICT, INVALID_TRANSCRIPTION, or INSUFFICIENT_EVIDENCE.",
        "contribution": "We show that exact-count claims in symbolic research archives require layer-specific inventory reconciliation before theory claims can be trusted.",
        "experiment": "experiments/EXP-BMC-002/",
        "human_review": ["exact-count review", "source transcription review", "PAGC theory review"],
        "dependencies": ["GOAL-001"],
        "next_action": "Run a count reconciliation report across BMC, TEI, annotations, KG, claims, and paper artifacts.",
        "scores": {
            "evidence_strength": 0.82,
            "novelty_potential": 0.74,
            "falsifiability": 0.90,
            "reproducibility": 0.90,
            "cultural_source_integrity": 0.82,
            "paper_fit": 0.86,
            "safety": 0.90,
            "unresolved_contradiction_risk": 0.25,
        },
    },
    {
        "id": "GOAL-003",
        "slug": "bmc-claim-gating-engine",
        "title": "BMC as a Claim-Gating Engine for Paper Generation",
        "status": "active",
        "readiness": "active_after_goal_001_seed",
        "risk": "medium",
        "paper_potential": "high",
        "question": "Can every manuscript claim be traced back to BMC objects, source evidence, certainty records, and experiment outputs?",
        "novelty": "A BMC-backed claim gate may be a publishable method for preventing unsupported symbolic, historical, or computational claims from entering a paper.",
        "required_evidence": [
            "paper claims",
            "claim IDs",
            "BMC objects",
            "source artifacts",
            "IIIF/TEI locators",
            "certainty scores",
            "provenance activities",
            "experiment results",
            "paper sections",
        ],
        "minimal_experiment": "Map paper claims to BMC objects, evidence locators, certainty scores, experiments, and action statuses.",
        "success": [
            "Major manuscript claims have source and BMC dependencies.",
            "Unsupported claims are marked NEEDS_SOURCE, NEEDS_EXPERIMENT, OVERCLAIMED, REWRITE_AS_LIMITATION, or REMOVE.",
            "Contradictions block positive paper contributions.",
            "Claim-gate output can regenerate a paper audit table.",
        ],
        "failure": [
            "Most claims cannot be linked to BMC or evidence objects.",
            "The gate cannot separate supported claims from speculative claims.",
            "Paper sections contain positive claims that the gate marks unsafe.",
        ],
        "falsification": "If most claims cannot be linked to BMC/evidence objects, the lab is not ready for BMC-driven paper generation.",
        "ultimate": "A manuscript whose major claims are evidence-gated and reproducible from repo-local artifacts, or a no-submission decision.",
        "contribution": "We present a claim-gated manuscript pipeline in which exact-count and symbolic-structure claims are accepted only when grounded in BMC-linked evidence.",
        "experiment": "experiments/EXP-BMC-003/",
        "human_review": ["publication gate review", "claim audit review", "authority review"],
        "dependencies": ["GOAL-001"],
        "next_action": "Build a BMC claim-gate table from paper claims, corpus claims, BMC records, evidence, and experiments.",
        "scores": {
            "evidence_strength": 0.70,
            "novelty_potential": 0.76,
            "falsifiability": 0.82,
            "reproducibility": 0.80,
            "cultural_source_integrity": 0.78,
            "paper_fit": 0.88,
            "safety": 0.86,
            "unresolved_contradiction_risk": 0.30,
        },
    },
    {
        "id": "GOAL-004",
        "slug": "bmc-grammar-induction",
        "title": "BMC Grammar Induction from Base/Modifier Relations",
        "status": "blocked",
        "readiness": "blocked_until_goal_002_count_stability",
        "risk": "medium",
        "paper_potential": "medium",
        "question": "Can BMC entries reveal a compact grammar that explains the observed symbolic inventory?",
        "novelty": "If base/modifier combinations are systematic, the BMC may support a generative grammar rather than a flat annotation table.",
        "required_evidence": [
            "verified BMC records",
            "count reconciliation result",
            "row class evidence",
            "modifier class evidence",
            "exception and ambiguity records",
        ],
        "minimal_experiment": "Infer candidate production rules and test coverage, exception rate, false-generation rate, ambiguity rate, and human-review burden.",
        "success": [
            "A candidate grammar covers verified entries.",
            "Exceptions and unsupported generations are measurable.",
            "Ambiguous cells remain flagged.",
        ],
        "failure": [
            "The grammar fails to cover many verified entries.",
            "The grammar generates many unsupported objects.",
            "The rules depend on unstable counts.",
        ],
        "falsification": "If a grammar fails coverage or generates unsupported entries, BMC remains an index rather than a generative grammar.",
        "ultimate": "A formal grammar, or a negative result showing that the observed inventory resists compact generative modeling.",
        "contribution": "We test whether the BMC supports grammar induction and report the boundary between observed symbolic structure and speculative generation.",
        "experiment": "experiments/EXP-BMC-004/",
        "human_review": ["grammar review", "source transcription review"],
        "dependencies": ["GOAL-002"],
        "next_action": "Wait for GOAL-002 count reconciliation before inducing rules.",
        "scores": {
            "evidence_strength": 0.55,
            "novelty_potential": 0.78,
            "falsifiability": 0.75,
            "reproducibility": 0.70,
            "cultural_source_integrity": 0.72,
            "paper_fit": 0.75,
            "safety": 0.80,
            "unresolved_contradiction_risk": 0.45,
        },
    },
    {
        "id": "GOAL-005",
        "slug": "bmc-compression-mdl",
        "title": "BMC Compression and Minimum Description Length Testing",
        "status": "blocked",
        "readiness": "blocked_until_goal_004_grammar_result",
        "risk": "medium",
        "paper_potential": "medium",
        "question": "Does the BMC produce a measurable compression advantage over a flat enumeration of glyph or cell records?",
        "novelty": "If the symbolic system has real generative structure, base/modifier representation should compress the inventory while preserving reconstructability.",
        "required_evidence": [
            "flat cell list",
            "row-vowel table",
            "BMC records",
            "candidate grammar",
            "knowledge graph representation",
            "uncertainty records",
        ],
        "minimal_experiment": "Compare description length, primitives, rules, reconstruction accuracy, exception count, uncertainty-weighted compression, and interpretability across representations.",
        "success": [
            "BMC or grammar representation compresses while preserving reconstruction.",
            "Exceptions and uncertainty costs are included.",
            "Flat-table baselines are explicit.",
        ],
        "failure": [
            "BMC does not compress better than a flat table.",
            "Compression requires dropping uncertainty or exceptions.",
            "The comparison depends on an unstable grammar.",
        ],
        "falsification": "If BMC does not compress better than a flat table, compression-based PAGC claims are unsupported.",
        "ultimate": "A formal result showing either real symbolic compression or a negative result against compression/theory claims.",
        "contribution": "We introduce uncertainty-aware compression as a falsification test for symbolic-structure claims.",
        "experiment": "experiments/EXP-BMC-005/",
        "human_review": ["method review", "PAGC theory review"],
        "dependencies": ["GOAL-004"],
        "next_action": "Wait for GOAL-004 grammar result before MDL testing.",
        "scores": {
            "evidence_strength": 0.50,
            "novelty_potential": 0.76,
            "falsifiability": 0.85,
            "reproducibility": 0.75,
            "cultural_source_integrity": 0.70,
            "paper_fit": 0.77,
            "safety": 0.82,
            "unresolved_contradiction_risk": 0.50,
        },
    },
    {
        "id": "GOAL-006",
        "slug": "bmc-certainty-propagation",
        "title": "BMC Uncertainty and Certainty Propagation",
        "status": "pending",
        "readiness": "pending_until_goal_003_claim_gate_seed",
        "risk": "medium",
        "paper_potential": "high",
        "question": "How should uncertainty propagate from source transcription to BMC objects, grammar rules, count claims, and final manuscript claims?",
        "novelty": "The lab can define a rigorous certainty calculus for culturally grounded symbolic reconstruction.",
        "required_evidence": [
            "source quality records",
            "transcription confidence",
            "annotation confidence",
            "provenance integrity",
            "lineage integrity",
            "contradiction penalties",
            "review status",
        ],
        "minimal_experiment": "Propagate certainty from source artifact to annotation, BMC unit, count claim, grammar rule, theory claim, and paper claim.",
        "success": [
            "Claim confidence is computed from explicit factors.",
            "Blocked claims are traceable to weak factors.",
            "Contradiction penalties are visible.",
        ],
        "failure": [
            "Certainty records are too sparse for propagation.",
            "Confidence scores cannot be justified.",
            "High-level claims bypass low-confidence evidence.",
        ],
        "falsification": "If certainty records are too sparse or inconsistent to support propagation, the lab must improve certainty instrumentation before high-level theory claims.",
        "ultimate": "A certainty model that identifies which claims are safe, weak, contradicted, or blocked.",
        "contribution": "We provide a certainty propagation model for evidence-gated symbolic research pipelines.",
        "experiment": "experiments/EXP-BMC-006/",
        "human_review": ["certainty model review", "publication gate review"],
        "dependencies": ["GOAL-003"],
        "next_action": "Wait for GOAL-003 claim-gate seed, then propagate certainty factors.",
        "scores": {
            "evidence_strength": 0.65,
            "novelty_potential": 0.74,
            "falsifiability": 0.82,
            "reproducibility": 0.78,
            "cultural_source_integrity": 0.82,
            "paper_fit": 0.80,
            "safety": 0.88,
            "unresolved_contradiction_risk": 0.32,
        },
    },
    {
        "id": "GOAL-007",
        "slug": "bmc-knowledge-graph-integration",
        "title": "BMC Knowledge Graph Integration",
        "status": "pending",
        "readiness": "pending_until_goal_006_certainty_model",
        "risk": "low",
        "paper_potential": "medium",
        "question": "Can every BMC object be represented as a graph node linked to source evidence, provenance, certainty, claims, and experiments?",
        "novelty": "The BMC-KG integration may become a reusable architecture for symbolic archive research.",
        "required_evidence": [
            "BMC object records",
            "source artifacts",
            "IIIF canvases",
            "TEI locators",
            "certainty records",
            "provenance activities",
            "claims",
            "experiments",
            "paper sections",
            "authority records",
        ],
        "minimal_experiment": "Extend knowledge_graph/etisiobi_kg.jsonld with Base, Modifier, Cell, GlyphObservation, TEILocator, IIIFCanvas, CertaintyRecord, ProvenanceActivity, Claim, Experiment, PaperSection, and AuthorityRecord nodes.",
        "success": [
            "BMC objects can be queried through graph relations.",
            "Claims and paper sections link to evidence nodes.",
            "Authority records are part of the graph.",
        ],
        "failure": [
            "The KG cannot represent dependencies without ambiguity.",
            "Important BMC objects remain detached.",
            "Claims cannot be queried through evidence paths.",
        ],
        "falsification": "If the KG cannot represent claim/evidence dependencies without ambiguity, the model needs ontology repair.",
        "ultimate": "A graph-native research object that can be queried before paper writing.",
        "contribution": "We show how BMC objects can be embedded in a provenance-aware scholarly knowledge graph.",
        "experiment": "experiments/EXP-BMC-007/",
        "human_review": ["ontology review", "authority review"],
        "dependencies": ["GOAL-006"],
        "next_action": "Wait for GOAL-006 certainty model, then extend the KG.",
        "scores": {
            "evidence_strength": 0.68,
            "novelty_potential": 0.72,
            "falsifiability": 0.72,
            "reproducibility": 0.82,
            "cultural_source_integrity": 0.78,
            "paper_fit": 0.76,
            "safety": 0.86,
            "unresolved_contradiction_risk": 0.28,
        },
    },
    {
        "id": "GOAL-008",
        "slug": "bmc-benchmark-tasks",
        "title": "BMC Benchmark Tasks for Symbolic Reconstruction",
        "status": "pending",
        "readiness": "pending_until_goal_007_graph_model",
        "risk": "low",
        "paper_potential": "medium",
        "question": "Can the lab define benchmark tasks that evaluate reconstruction, annotation, count resolution, grammar induction, and claim gating?",
        "novelty": "The lab may produce benchmark tasks for future symbolic reconstruction systems rather than only one paper.",
        "required_evidence": [
            "row-label reconstruction labels",
            "vowel inventory labels",
            "cell-grid completion targets",
            "base/modifier classes",
            "contradiction labels",
            "claim evidence links",
            "certainty propagation outputs",
            "grammar induction outputs",
            "paper-claim validation outputs",
            "arXiv readiness outputs",
        ],
        "minimal_experiment": "Define tasks, metrics, scoring data requirements, and baseline outputs in the benchmark registry.",
        "success": [
            "Tasks are scoreable from repo-local artifacts.",
            "Metrics include accuracy, coverage, contradiction precision/recall, evidence-link completeness, certainty calibration, human-review agreement, and reproducibility.",
            "Benchmarks do not require hidden data for their seed version.",
        ],
        "failure": [
            "Tasks cannot be scored from existing artifacts.",
            "Benchmark labels are missing or circular.",
            "Metrics reward unsupported generation.",
        ],
        "falsification": "If tasks cannot be scored from existing artifacts, the lab has infrastructure but not yet benchmark-grade data.",
        "ultimate": "A benchmark registry that turns Etisiobi/PAGC research into repeatable evaluation tasks.",
        "contribution": "We define benchmark tasks for evidence-grounded symbolic reconstruction from heterogeneous scholarly artifacts.",
        "experiment": "experiments/EXP-BMC-008/",
        "human_review": ["benchmark review", "data release review"],
        "dependencies": ["GOAL-007"],
        "next_action": "Wait for GOAL-007 graph model, then define scoreable benchmark tasks.",
        "scores": {
            "evidence_strength": 0.50,
            "novelty_potential": 0.70,
            "falsifiability": 0.78,
            "reproducibility": 0.72,
            "cultural_source_integrity": 0.72,
            "paper_fit": 0.68,
            "safety": 0.90,
            "unresolved_contradiction_risk": 0.40,
        },
    },
    {
        "id": "GOAL-009",
        "slug": "bmc-authority-aware-review",
        "title": "BMC Human-in-the-Loop and Authority-Aware Review",
        "status": "pending",
        "readiness": "pending_until_goal_003_and_goal_006",
        "risk": "medium",
        "paper_potential": "high",
        "question": "How should expert, cultural, legal, and research authority decisions enter the BMC without erasing uncertainty or overclaiming?",
        "novelty": "The lab authority register can become an explicit part of symbolic reconstruction, not an afterthought.",
        "required_evidence": [
            "authority approval records",
            "decision trace records",
            "certainty records",
            "BMC records",
            "paper claims",
            "release metadata",
            "review states",
        ],
        "minimal_experiment": "Link review states to authority/approval_register.jsonl, decisions/decision_log.jsonl, certainty records, BMC records, paper claims, and release metadata.",
        "success": [
            "Review states distinguish machine_seeded, human_review_needed, expert_reviewed, authority_approved, disputed, restricted, withdrawn, publication_allowed, and publication_blocked.",
            "Authority decisions can block release and manuscript claims.",
            "Uncertainty is preserved across review.",
        ],
        "failure": [
            "Authority decisions cannot be connected to release and manuscript claims.",
            "Review status overwrites uncertainty.",
            "Publication-facing claims bypass authority state.",
        ],
        "falsification": "If authority decisions cannot be connected to release and manuscript claims, public-facing research claims must be blocked.",
        "ultimate": "A review protocol showing how culturally meaningful symbolic artifacts move from annotation to publication safely.",
        "contribution": "We integrate authority and consent records directly into a symbolic reconstruction pipeline.",
        "experiment": "experiments/EXP-BMC-009/",
        "human_review": ["cultural authority review", "legal review", "publication release review"],
        "dependencies": ["GOAL-003", "GOAL-006"],
        "next_action": "Wait for GOAL-003 and GOAL-006, then connect review states to claim/release gates.",
        "scores": {
            "evidence_strength": 0.76,
            "novelty_potential": 0.72,
            "falsifiability": 0.70,
            "reproducibility": 0.75,
            "cultural_source_integrity": 0.95,
            "paper_fit": 0.78,
            "safety": 0.90,
            "unresolved_contradiction_risk": 0.22,
        },
    },
    {
        "id": "GOAL-010",
        "slug": "bmc-to-paper-hyperloop",
        "title": "BMC-to-Paper Recursive Research Hyperloop",
        "status": "blocked",
        "readiness": "blocked_until_goal_001_through_goal_009",
        "risk": "high",
        "paper_potential": "high",
        "question": "Can the lab recursively generate, test, revise, and package research papers without claim drift?",
        "novelty": "The strongest systems-level contribution may be the full recursive loop from BMC to claim extraction, count audit, contradiction detection, experiment selection, certainty propagation, paper generation, self-review, and arXiv preflight.",
        "required_evidence": [
            "BMC records",
            "claim extraction outputs",
            "count audit",
            "contradiction detection",
            "experiment selection logs",
            "certainty propagation",
            "paper generation outputs",
            "self-review",
            "arXiv preflight",
        ],
        "minimal_experiment": "Run the research hyperloop over the BMC and measure claims generated, claims blocked, contradictions found, supported paper claims, unsupported claims removed, reproducible tables/figures, and time to readiness decision.",
        "success": [
            "Recursive generation reduces unsupported claims.",
            "Contradictions remain visible.",
            "The loop ends in READY_FOR_HUMAN_ARXIV_REVIEW or a precise no-submission decision.",
        ],
        "failure": [
            "Recursive generation increases unsupported claims.",
            "Contradictions are hidden.",
            "Readiness status cannot be reproduced from artifacts.",
        ],
        "falsification": "If recursive generation increases unsupported claims or hides contradictions, the hyperloop is unsafe for publication-oriented research.",
        "ultimate": "READY_FOR_HUMAN_ARXIV_REVIEW or a precise no-submission decision with blockers.",
        "contribution": "We demonstrate a recursive, evidence-gated research loop that converts a BMC-backed archive into a claim-audited manuscript or a principled no-submission decision.",
        "experiment": "experiments/EXP-BMC-010/",
        "human_review": ["full publication gate review", "authority review", "legal review"],
        "dependencies": ["GOAL-001", "GOAL-002", "GOAL-003", "GOAL-004", "GOAL-005", "GOAL-006", "GOAL-007", "GOAL-008", "GOAL-009"],
        "next_action": "Wait for GOAL-001 through GOAL-009 before recursive paper packaging.",
        "scores": {
            "evidence_strength": 0.45,
            "novelty_potential": 0.80,
            "falsifiability": 0.78,
            "reproducibility": 0.70,
            "cultural_source_integrity": 0.76,
            "paper_fit": 0.84,
            "safety": 0.78,
            "unresolved_contradiction_risk": 0.55,
        },
    },
]


DEPENDENCIES = [
    ("GOAL-001", "GOAL-002"),
    ("GOAL-002", "GOAL-003"),
    ("GOAL-002", "GOAL-004"),
    ("GOAL-004", "GOAL-005"),
    ("GOAL-003", "GOAL-006"),
    ("GOAL-006", "GOAL-007"),
    ("GOAL-007", "GOAL-008"),
    ("GOAL-003", "GOAL-009"),
    ("GOAL-006", "GOAL-009"),
]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean_text(text) + "\n", encoding="utf-8")


def clean_text(text: str) -> str:
    cleaned = dedent(text).strip()
    lines = []
    for line in cleaned.splitlines():
        lines.append(line[8:] if line.startswith("        ") else line)
    return "\n".join(lines)


def score(goal: dict) -> float:
    s = goal["scores"]
    value = (
        0.25 * s["evidence_strength"]
        + 0.20 * s["novelty_potential"]
        + 0.15 * s["falsifiability"]
        + 0.15 * s["reproducibility"]
        + 0.10 * s["cultural_source_integrity"]
        + 0.10 * s["paper_fit"]
        + 0.05 * s["safety"]
        - 0.20 * s["unresolved_contradiction_risk"]
    )
    return round(value, 3)


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_goal_files() -> None:
    out_dir = ROOT / "research_goals" / "bmc"
    for goal in GOALS:
        deps = goal["dependencies"] or ["none"]
        text = f"""
        ---
        type: research_goal
        goal_id: {goal['id']}
        status: {goal['status']}
        theme: Base Modifier Cache
        novelty_status: hypothesis
        requires_prior_art_check: true
        requires_authority_check: true
        requires_count_audit: {'true' if goal['id'] in {'GOAL-001', 'GOAL-002', 'GOAL-003', 'GOAL-004', 'GOAL-005'} else 'false'}
        paper_potential: {goal['paper_potential']}
        risk: {goal['risk']}
        readiness_status: {goal['readiness']}
        score: {score(goal)}
        created: "{TODAY}"
        updated: "{TODAY}"
        dependencies: {json.dumps(goal['dependencies'])}
        experiment_directory: {goal['experiment']}
        ---

        # {goal['id']}: {goal['title']}

        ## Research Question

        {goal['question']}

        ## Novelty Hypothesis

        {goal['novelty']}

        This is not a proven novelty claim. It remains pending systematic prior-art review.

        ## Required Evidence

        {bullet(goal['required_evidence'])}

        ## Minimal Experiment

        {goal['minimal_experiment']}

        ## Success Criteria

        {bullet(goal['success'])}

        ## Failure Criteria

        {bullet(goal['failure'])}

        ## Falsification Condition

        {goal['falsification']}

        ## Ultimate Conclusion

        {goal['ultimate']}

        ## Expected Paper Contribution

        {goal['contribution']}

        ## Experiment Directory

        `{goal['experiment']}`

        ## Human Review Needed

        {bullet(goal['human_review'])}

        ## Dependency On Other Goals

        {bullet(deps)}

        ## Readiness Status

        `{goal['readiness']}`

        ## Next Action

        {goal['next_action']}
        """
        write_text(out_dir / f"{goal['id']}-{goal['slug']}.md", text)


def write_index_files() -> None:
    out_dir = ROOT / "research_goals" / "bmc"
    table = "\n".join(
        f"| [{g['id']}: {g['title']}]({g['id']}-{g['slug']}.md) | {g['status']} | {score(g):.3f} | {g['readiness']} |"
        for g in GOALS
    )
    write_text(
        out_dir / "README.md",
        f"""
        # Base Modifier Cache Research Program

        Generated: {TODAY}

        The Base Modifier Cache (BMC) program treats BMC as a lab-internal novelty hypothesis until systematic prior-art review verifies otherwise.

        Working definition:

        ```text
        base unit
        + modifier
        + source locator
        + row / vowel / cell coordinate
        + glyph evidence
        + certainty score
        + provenance record
        + knowledge-graph node
        + claim dependency
        + experiment trace
        = auditable symbolic object
        ```

        ## Active Goals

        - GOAL-001: Base Modifier Cache formal reconstruction.
        - GOAL-002: BMC count reconciliation.
        - GOAL-003: BMC claim-gating engine.

        ## Pending / Blocked Goals

        GOAL-004 through GOAL-010 stay pending or blocked until their dependency gates pass. This preserves the research frontier without promoting grammar, compression, or paper-hyperloop claims ahead of evidence.

        ## Goal Table

        | Goal | Status | Score | Readiness |
        |---|---|---:|---|
        {table}
        """,
    )
    write_text(
        out_dir / "goal_dependency_graph.md",
        """
        # BMC Goal Dependency Graph

        ```mermaid
        graph LR
          G001["GOAL-001 BMC formal reconstruction"] --> G002["GOAL-002 count reconciliation"]
          G002 --> G003["GOAL-003 claim gate"]
          G002 --> G004["GOAL-004 grammar induction"]
          G004 --> G005["GOAL-005 compression / MDL"]
          G003 --> G006["GOAL-006 certainty propagation"]
          G006 --> G007["GOAL-007 knowledge graph"]
          G007 --> G008["GOAL-008 benchmarks"]
          G003 --> G009["GOAL-009 authority-aware review"]
          G006 --> G009
          G001 --> G010["GOAL-010 BMC-to-paper hyperloop"]
          G002 --> G010
          G003 --> G010
          G004 --> G010
          G005 --> G010
          G006 --> G010
          G007 --> G010
          G008 --> G010
          G009 --> G010
        ```

        ## Activation Rule

        Activate only GOAL-001, GOAL-002, and GOAL-003 now. Do not activate GOAL-004 or GOAL-005 until GOAL-002 confirms stable count layers. Do not activate GOAL-010 until the claim gate has approved or blocked core claims.
        """,
    )
    scored = []
    for goal in GOALS:
        row = {
            "goal_id": goal["id"],
            "title": goal["title"],
            "status": goal["status"],
            "readiness_status": goal["readiness"],
            "score": score(goal),
            "scores": goal["scores"],
            "dependencies": goal["dependencies"],
            "active_selected": goal["id"] in {"GOAL-001", "GOAL-002", "GOAL-003"},
        }
        scored.append(row)
    (out_dir / "goal_scores.json").write_text(
        json.dumps(
            {
                "generated_at": NOW,
                "formula": "0.25*evidence_strength + 0.20*novelty_potential + 0.15*falsifiability + 0.15*reproducibility + 0.10*cultural_source_integrity + 0.10*paper_fit + 0.05*safety - 0.20*unresolved_contradiction_risk",
                "novelty_status": "hypotheses_pending_prior_art_review",
                "goals": scored,
            },
            indent=2,
            ensure_ascii=True,
        )
        + "\n",
        encoding="utf-8",
    )
    write_text(
        out_dir / "active_goal_selection.md",
        """
        # BMC Active Goal Selection

        ## Selected Active Goals

        | Goal | Reason | Dependency State |
        |---|---|---|
        | GOAL-001 | Creates the BMC substrate all other goals depend on. | No prior BMC dependency. |
        | GOAL-002 | Resolves row/vowel/cell/foundation-count drift before grammar or compression work. | Depends on GOAL-001 seed. |
        | GOAL-003 | Turns the BMC into a paper-claim gate before manuscript generation. | Depends on GOAL-001 seed. |

        ## Blocked or Pending

        - GOAL-004 is blocked until GOAL-002 stabilizes count layers.
        - GOAL-005 is blocked until GOAL-004 yields a grammar or negative grammar result.
        - GOAL-006 is pending until GOAL-003 creates claim-gate records.
        - GOAL-007 is pending until GOAL-006 produces a certainty model.
        - GOAL-008 is pending until GOAL-007 produces graph-queryable BMC objects.
        - GOAL-009 is pending until GOAL-003 and GOAL-006 link claims and certainty to authority.
        - GOAL-010 is blocked until GOAL-001 through GOAL-009 pass or produce explicit negative results.

        ## Next Experiment

        `experiments/EXP-BMC-001/`: generate and validate `corpus/base_modifier_cache.jsonl` from repo-local artifacts.

        ## Next Human Review Needed

        Source transcription and exact-count review for GOAL-001/GOAL-002, followed by authority/cultural review before public release use.
        """,
    )


def replace_block(path: Path, marker: str, content: str) -> None:
    start = f"<!-- BEGIN {marker} -->"
    end = f"<!-- END {marker} -->"
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    block = f"{start}\n{clean_text(content)}\n{end}\n"
    if start in old and end in old:
        prefix = old.split(start, 1)[0]
        suffix = old.split(end, 1)[1]
        path.write_text(prefix.rstrip() + "\n\n" + block + suffix.lstrip(), encoding="utf-8")
    else:
        path.write_text(old.rstrip() + "\n\n" + block, encoding="utf-8")


def update_yaml_state() -> None:
    path = ROOT / "research_state.yaml"
    old = path.read_text(encoding="utf-8") if path.exists() else ""
    start = "# BEGIN BMC_RESEARCH_PROGRAM"
    end = "# END BMC_RESEARCH_PROGRAM"
    content = f"""
{start}
bmc_research_program:
  generated_at: {TODAY}
  theme: Base Modifier Cache as reproducible generative and evidentiary substrate
  novelty_status: hypotheses_pending_prior_art_review
  active_goals:
    - GOAL-001: Base Modifier Cache formal reconstruction
    - GOAL-002: BMC count reconciliation
    - GOAL-003: BMC claim-gating engine
  pending_or_blocked_goals:
    - GOAL-004: blocked until GOAL-002 count stability
    - GOAL-005: blocked until GOAL-004 grammar result
    - GOAL-006: pending until GOAL-003 claim gate seed
    - GOAL-007: pending until GOAL-006 certainty model
    - GOAL-008: pending until GOAL-007 graph model
    - GOAL-009: pending until GOAL-003 and GOAL-006
    - GOAL-010: blocked until GOAL-001 through GOAL-009
  next_experiment: experiments/EXP-BMC-001/
  next_artifact: corpus/base_modifier_cache.jsonl
  next_human_review: source transcription and exact-count review
  files:
    index: research_goals/bmc/README.md
    scores: research_goals/bmc/goal_scores.json
    dependency_graph: research_goals/bmc/goal_dependency_graph.md
    active_selection: research_goals/bmc/active_goal_selection.md
{end}
"""
    if start in old and end in old:
        prefix = old.split(start, 1)[0]
        suffix = old.split(end, 1)[1]
        path.write_text(prefix.rstrip() + "\n\n" + content.strip() + "\n" + suffix.lstrip(), encoding="utf-8")
    else:
        path.write_text(old.rstrip() + "\n\n" + content.strip() + "\n", encoding="utf-8")


def update_backlogs() -> None:
    rows = "\n".join(
        [
            f"| [[BMC_Goals#{g['id']} {g['title']}|{g['id']}]] {g['title']} | {g['status']} | {score(g):.3f} | "
            f"{'none' if not g['dependencies'] else ' + '.join(g['dependencies'])} | {g['next_action']} |"
            for g in GOALS
        ]
    )
    section = """
    ## Base Modifier Cache Research Program

    Novelty status: hypothesis pending prior-art review.

    | Goal | Status | Score | Dependency Gate | Next test |
    |---|---|---:|---|---|
    {rows}
    """.format(rows=rows)
    for path in [ROOT / "research_goals" / "backlog.md", ROOT / "obsidian_vault" / "04_Goal_Backlog.md"]:
        if path.exists():
            replace_block(path, "BMC_RESEARCH_PROGRAM", section)


def update_obsidian() -> None:
    links = "\n".join(
        f"- [[BMC_Goals#{g['id']} {g['title']}|{g['id']}: {g['title']}]] - {g['status']}"
        for g in GOALS
    )
    goal_sections = "\n\n".join(
        f"""## {g['id']} {g['title']}

Status: `{g['status']}`

Readiness: `{g['readiness']}`

Score: `{score(g):.3f}`

Repo file: [research_goals/bmc/{g['id']}-{g['slug']}.md](../../research_goals/bmc/{g['id']}-{g['slug']}.md)

Next action: {g['next_action']}"""
        for g in GOALS
    )
    write_text(
        ROOT / "obsidian_vault" / "Goals" / "BMC_Goals.md",
        f"""
        ---
        type: goal_index
        id: BMC_GOALS
        status: active
        confidence: 0.74
        created: "{TODAY}"
        updated: "{TODAY}"
        tags: [bmc, pagc, nwagu-aneke, claim-gate]
        links: [04_Goal_Backlog]
        ---

        # BMC Goals

        Base Modifier Cache is treated as a novelty hypothesis pending prior-art review.

        ## Active

        - [[BMC_Goals#GOAL-001 Base Modifier Cache Formal Reconstruction|GOAL-001]]
        - [[BMC_Goals#GOAL-002 BMC Count Reconciliation Across Rows, Vowels, Cells, and PAGC Foundation Claims|GOAL-002]]
        - [[BMC_Goals#GOAL-003 BMC as a Claim-Gating Engine for Paper Generation|GOAL-003]]

        ## All Goals

        {links}

        ## Goal Details

        {goal_sections}

        ## Dependency Map

        [BMC goal dependency graph](../../research_goals/bmc/goal_dependency_graph.md)

        ## Next Experiment

        `experiments/EXP-BMC-001/` should generate `corpus/base_modifier_cache.jsonl` from repo-local artifacts.
        """,
    )
    current_run = ROOT / "obsidian_vault" / "10_Current_Research_Run.md"
    if current_run.exists():
        replace_block(
            current_run,
            "BMC_RESEARCH_PROGRAM",
            """
            ## BMC Current Research Run

            Active goals: GOAL-001, GOAL-002, GOAL-003.

            Next experiment: `experiments/EXP-BMC-001/`.

            Blocked goals: GOAL-004 through GOAL-010 remain dependency-gated.
            """,
        )


def update_canvas() -> None:
    path = ROOT / "obsidian_vault" / "Canvases" / "Research Atlas.canvas"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    nodes = data.setdefault("nodes", [])
    edges = data.setdefault("edges", [])
    if not any(node.get("id") == "bmc-goals" for node in nodes):
        nodes.append(
            {
                "id": "bmc-goals",
                "type": "file",
                "file": "Goals/BMC_Goals.md",
                "x": 1040,
                "y": 240,
                "width": 300,
                "height": 170,
            }
        )
    if not any(node.get("id") == "bmc-cache" for node in nodes):
        nodes.append(
            {
                "id": "bmc-cache",
                "type": "text",
                "text": "Base Modifier Cache\\ninventory -> structure -> claims -> grammar -> compression -> certainty -> graph -> benchmark -> authority -> paper",
                "x": 1040,
                "y": 20,
                "width": 320,
                "height": 160,
            }
        )
    for edge in [
        {"id": "e-bmc-cache-goals", "fromNode": "bmc-cache", "toNode": "bmc-goals"},
        {"id": "e-goals-bmc-goals", "fromNode": "goals", "toNode": "bmc-goals"},
        {"id": "e-bmc-claims", "fromNode": "bmc-goals", "toNode": "claims"},
    ]:
        if not any(existing.get("id") == edge["id"] for existing in edges):
            edges.append(edge)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def update_research_runs() -> None:
    runs_dir = ROOT / "research_runs"
    if not runs_dir.exists():
        return
    section = """
    ## Base Modifier Cache Goals

    Active:

    - GOAL-001 Base Modifier Cache formal reconstruction.
    - GOAL-002 BMC count reconciliation.
    - GOAL-003 BMC claim-gating engine.

    Next experiment: `experiments/EXP-BMC-001/`.
    """
    for path in runs_dir.rglob("active_goals.md"):
        replace_block(path, "BMC_RESEARCH_PROGRAM", section)


def main() -> None:
    write_goal_files()
    write_index_files()
    update_yaml_state()
    update_backlogs()
    update_obsidian()
    update_canvas()
    update_research_runs()
    print("BMC research goals generated: 10 goals; active GOAL-001, GOAL-002, GOAL-003")


if __name__ == "__main__":
    main()
