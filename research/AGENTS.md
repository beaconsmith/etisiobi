# AGENTS.md

## Purpose

This repository is a research operating system for producing submission-grade academic papers under tight deadlines without sacrificing evidentiary rigor.

The system is source-first, evidence-first, resumable, and reviewer-aware.

Agents working in this repository must behave like members of a serious research lab, not generic writing assistants.

The primary goals are:

1. build defensible literature spines
2. extract and organize evidence
3. sharpen contribution claims
4. promote only sufficiently evidenced papers into drafting
5. reduce reviewer attack surface before submission
6. convert research findings into developer-actionable product and engineering feedback

This repository does **not** treat drafting as the first phase.
Drafting is downstream of source acquisition, evidence extraction, contradiction analysis, and scope control.

---

## Core Principles

### 1. Source-first
No paper should enter serious drafting before its literature base is sufficiently compiled, cleaned, clustered, and stress-tested.

### 2. Evidence over vibes
Do not write claims because they sound plausible.
Do not keep claims because they sound sophisticated.
Every non-trivial claim should be tied to evidence, method, or explicitly marked reasoning.

### 3. Resumability
A fresh agent should be able to enter any paper folder, read the current control files, and continue work with minimal ambiguity.

### 4. Human-legible state
Important state must live in Markdown and structured logs, not only in model context.
A human researcher must be able to inspect progress without reconstructing hidden reasoning.

### 5. Promotion gates
A paper advances from one stage to the next only after passing explicit gates.
Do not bypass gates because the deadline is close.

### 6. Portfolio realism
Not every candidate paper should survive.
Kill weak papers early.
Protect the strongest papers.

### 6a. Chief of Staff discipline
The lab must maintain an operating layer that makes recommendations, tracks blockers, turns research into product/engineering actions, and protects repo hygiene. See `CHIEF_OF_STAFF.md`.

### 7. Reviewer awareness
Build with a skeptical reviewer in mind from day one.
Every paper should maintain an active reviewer attack surface file.

### 7a. Research-team readiness gate
Before any paper can be called complete, submission-ready, or
`READY_FOR_HUMAN_ARXIV_REVIEW`, spawn or simulate a documented review team and
write `review_team_trace.jsonl` in the paper directory. The trace must include
at least a research lead, domain postdoc, methods reviewer, adversarial impact
journal reviewer, citation/evidence reviewer, and rights/authority reviewer.
Every role must pass with no blocking issues. If the trace is absent, the paper
is `NOT_READY_REVIEW_TEAM_BLOCKED`.

### 7b. A+ lab stage discipline
Before hardening any manuscript, check `A_PLUS_LAB_STANDARD.md` and
`LAB_STAGE_GATES.json`. A branch must not be rendered or described as a paper
candidate until it has an external-facing result, article-specific prior art,
source/rights status, reviewer attack surface, and decision trace. Ten research
branches are not ten papers. The default operating rule is at most two active
article-hardening branches at a time.

### 8. Double-blind discipline
Do not leak identifying information into drafts or notes intended for blinded submission.
Where necessary, use neutral placeholders and maintain blinding checks.

---

## Research Stages

All papers move through these stages:

### Stage 0 — Intake
Define the paper idea, track fit, thesis candidate, and kill criteria.

### Stage 1 — Source Acquisition
Gather, dedupe, validate, and rank relevant sources.
Build a usable literature spine.

### Stage 2 — Evidence Extraction
Extract claims, methods, regional context, contradictions, and reviewer risks.

### Stage 3 — Synthesis
Build cluster maps, claim maps, and a stable argument spine.
Do not draft full prose yet.

### Stage 4 — Promotion Review
Check whether the paper is strong enough to justify drafting.

### Stage 5 — Drafting
Draft outline and sections only after evidence gates pass.

### Stage 6 — Hardening
Run blinding, citation, track-fit, and overclaim checks before submission.

---

## Non-Negotiable Rules

### Rule 1 — Never draft from a thin source base
If the literature spine is weak, incomplete, generic, or overly global without local grounding, continue research instead of drafting.

### Rule 2 — Never invent citations
No fabricated references, no speculative page numbers, no false paraphrases, no fake local studies.

### Rule 3 — Never collapse disagreement
If relevant sources disagree, document the disagreement in `contradiction_map.md`.

### Rule 4 — Never confuse analogy with evidence
Conceptual similarity is not empirical support.

### Rule 5 — Never hide uncertainty
Mark uncertain claims explicitly and downgrade wording where necessary.

### Rule 6 — Never use a paper to hold unrelated ideas
If a concept belongs in another paper, move it there or mark it as excluded.

### Rule 7 — Never optimize for count over quality
Seven weak papers are worse than two strong ones.
Portfolio discipline matters.

### Rule 8 — Never skip the reviewer lens
Every paper must maintain `reviewer_attack_surface.md`.

### Rule 9 — Never let the manuscript outrun the evidence
If prose is more mature than the evidence file, the paper is in danger.

### Rule 10 — Never treat local context as optional
For papers about Nigeria, Southeast Nigeria, community institutions, or informal governance, local grounding is mandatory, not decorative.

---

## Standard Repository Layout

```text
research/
  AGENTS.md                     ← You are here
  RESEARCH_ORG.md
  QUALITY_BAR.md
  PORTFOLIO.md
  KILL_CRITERIA.md
  EVIDENCE_POLICY.md
  CITATION_POLICY.md
  SUBMISSION_RULES.md

  papers/
    <paper_slug>/
      autoresearch.md            ← Paper control plane
      paper_brief.md
      track_fit.md
      thesis.md
      questions.md
      scope.md
      exclusions.md
      source_quotas.md
      search_plan.md
      decision_log.md

      evidence/
        source_inbox.md
        source_registry.md
        source_gaps.md
        claim_map.md
        contradiction_map.md
        cluster_map.md
        methods_map.md
        quote_bank.md
        regional_context.md
        legal_policy_context.md
        reviewer_attack_surface.md

      writing/
        outline.md
        section_plan.md
        argument_spine.md
        related_work.md
        methods.md
        limitations.md
        blinding_check.md
        submission_checklist.md
        draft.tex

      runtime/
        autoresearch.jsonl
        run_manifest.yaml
        promote_gate.yaml
        metrics.json
        source_index.csv
        bib_status.csv
```

---

## Required File Semantics

### `autoresearch.md`
The paper control plane. A new agent must read this first.

### `paper_brief.md`
Fast orientation note explaining what the paper is, what it is not, and why it matters.

### `track_fit.md`
Explicit mapping from paper to conference track. Must include fit arguments and downgrade risks.

### `thesis.md`
Living record of thesis variants, contribution framing, and wording refinement.

### `scope.md`
Defines what is in and out of scope.

### `exclusions.md`
Captures tempting but excluded concepts, adjacent literatures, and spillover ideas.

### `source_quotas.md`
Declares what a sufficient literature base looks like.

### `decision_log.md`
Append-only human-readable record of major paper decisions.

### `source_registry.md`
Master vetted source ledger.

### `claim_map.md`
Maps claims to supports, contradictions, and risk levels.

### `contradiction_map.md`
Tracks real disagreement in the literature.

### `cluster_map.md`
Organizes the literature into debates and thematic groups.

### `methods_map.md`
Defines methods options, operationalization strategies, and methodological anchors.

### `reviewer_attack_surface.md`
Tracks probable reviewer objections and needed defenses.

### `argument_spine.md`
Short logical structure of the paper, not polished prose.

### `blinding_check.md`
Protects double-blind submission integrity.

### `submission_checklist.md`
Final pre-submission audit.

---

## Agent Roles

### 1. Portfolio Manager
Ranks candidate papers, assigns priority tiers, applies kill criteria, tracks bottlenecks.

### 2. Source Acquisition Agent
Search planning, source gathering, metadata normalization, duplication checks, initial relevance scoring.

### 3. Evidence Extraction Agent
Extracts claims, preserves useful quotes, updates claim maps, identifies missing support.

### 4. Contradiction Agent
Finds conflicting sources, detects definitional slippage, flags overclaim risk.

### 5. Methods Agent
Identifies methodological anchors, assesses measurability, improves operational definitions.

### 6. Regional Context Agent
Nigeria / Southeast Nigeria grounding, local institutional and historical context, region-specific support and critiques.

### 7. Reviewer Agent
Maintains reviewer attack surfaces, checks terminology, identifies oversold novelty, spots weak track fit.

### 8. Drafting Agent
Outline building, section writing, integrating literature into prose. Only after evidence gates pass.

---

## Standard Workflow for Any Agent

Before acting on a paper, an agent must:

1. read `autoresearch.md`
2. read `paper_brief.md`
3. read `track_fit.md`
4. inspect `decision_log.md`
5. inspect `source_gaps.md`
6. inspect `reviewer_attack_surface.md`
7. inspect current stage in `run_manifest.yaml`

If the paper is pre-promotion, the agent must avoid premature drafting.

---

## Promotion Gates

A paper should not be promoted to drafting until:

* thesis is clear
* track fit is credible
* source quotas are substantially met
* foundational sources exist
* recent sources exist
* counterarguments exist
* regional grounding exists where required
* methods anchor exists where required
* claim map is populated
* contradiction map is non-empty if disagreement exists
* reviewer attack surface has been initialized
* scope is stable enough to draft coherently

The lab-wide validator must also pass:

```bash
python scripts/validate_lab_standard.py
```

---

## Kill Criteria

Kill, freeze, or downgrade a paper if:

* contribution is not sufficiently distinct
* source base remains thin after serious search
* local / empirical grounding is too weak
* thesis depends on claims that cannot be evidenced in time
* methods story is not credible
* mostly rhetoric with no stable spine
* track fit is weak or opportunistic
* deadline pressure would force unacceptable sloppiness

Killing a paper is a quality decision, not a failure.

---

## Citation Standards

* Prefer primary sources where possible
* Use stable links and DOI where available
* Preserve page numbers for direct quotes
* Distinguish directly read sources from background mentions
* Do not cite sources that have not been actually reviewed
* Do not rely heavily on derivative summaries when primary sources are accessible

---

## Logging and State Discipline

### `decision_log.md`
Major human-readable decisions.

### `autoresearch.jsonl`
Machine-readable event logs. Each entry includes:
* timestamp, paper, stage, actor, action, files_touched, summary, confidence, blockers, next_action

---

## Definition of Done

A paper is done when:

* claims are supported
* scope is coherent
* track fit is defensible
* blinding check passes
* reviewer attack surface has been addressed
* `review_team_trace.jsonl` records passing reviews from the required research team
* citations are clean
* manuscript compiles
* abstract honestly matches the paper
* paper is strong enough to survive skeptical review
