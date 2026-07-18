# Research Organization

> Agent roles and coordination model for the ICEGOV 2026 research sprint.

---

## Operating Model

This lab uses a **source-first, stage-gated, portfolio-managed** research process.

The key insight from the autoresearch pattern (Karpathy → pi-autoresearch → larger orchestration systems) is:

1. **The loop discipline**: small bounded actions, fixed evaluation, keep-or-revert
2. **The session scaffolding**: resumable from files alone, append-only logs
3. **The promotion gates**: no drafting before evidence maturity
4. **The portfolio triage**: kill weak papers, protect strong ones

---

## Agent Roles

All work in this repo falls into one of these conceptual roles. A single human or AI agent may perform multiple roles, but the roles are distinct.

### Chief of Staff
- Owns operating cadence across research, product, and engineering feedback
- Maintains weekly priority stack and blockers
- Converts research findings into developer-actionable recommendations
- Runs or reviews `spine/research_feedback.py` and `spine/pagc_claim_gate.py`
- Enforces source integrity, repo hygiene, and decision memory
- See `CHIEF_OF_STAFF.md`

### Portfolio Manager
- Maintains `PORTFOLIO.md`
- Applies `KILL_CRITERIA.md`
- Assigns priority tiers
- Resolves cross-paper overlap
- Decides resource allocation

### Source Acquisition Agent
- Executes `search_plan.md` for each paper
- Populates `source_inbox.md`
- Promotes vetted sources to `source_registry.md`
- Updates `source_gaps.md`
- Logs events to `autoresearch.jsonl`

### Evidence Extraction Agent
- Builds `claim_map.md` from vetted sources
- Populates `quote_bank.md`
- Updates `contradiction_map.md`
- Builds `cluster_map.md`
- Assesses evidence confidence levels per `EVIDENCE_POLICY.md`

### Contradiction Agent
- Finds conflicting sources
- Detects definitional slippage across papers
- Flags overclaim risk in `reviewer_attack_surface.md`
- Updates `contradiction_map.md`

### Methods Agent
- Identifies methodological anchors
- Updates `methods_map.md`
- Assesses whether claims are measurable
- Ensures paper type matches available evidence

### Regional Context Agent
- Nigeria / Southeast Nigeria grounding
- Updates `regional_context.md`
- Locates local institutional and historical context
- Flags when generic citations substitute for specific grounding

### Reviewer Agent
- Maintains `reviewer_attack_surface.md`
- Checks track fit
- Identifies oversold novelty
- Tests blinding compliance

### Adversarial Impact Reviewer
- Attacks the paper as an impact-journal reviewer, not a friendly lab reader
- Checks whether the manuscript has a real thesis, evidence, method, result,
  falsification path, venue fit, and public readability
- Rejects papers that expose internal benchmark IDs, repo paths, machine status
  strings, or lab-control-plane prose as public argument
- Must sign `review_team_trace.jsonl` before any ready status is allowed

### Domain Postdoc
- Reviews domain-specific prior art, methods expectations, terminology, and
  whether the paper would be legible to researchers outside Etisiobi
- Must sign `review_team_trace.jsonl` before any ready status is allowed

### Drafting Agent
- Creates `outline.md` and `argument_spine.md` **only after promotion gate passes**
- Writes sections from evidence, not from imagination
- Integrates quotes and citations from `quote_bank.md` and `source_registry.md`

---

## Coordination Rules

### Chief of Staff authority
The Chief of Staff may recommend killing, downgrading, pausing, or promoting work without waiting for the human researcher to name the concern first. Recommendations must cite evidence, affected files or programs, and the next concrete action.

### State handoff
All agent work must be recorded in durable files. When an agent session ends, another agent must be able to continue from files alone without needing the previous agent's context window.

### Conflict resolution
If two agents disagree about a claim, thesis direction, or paper decision, the disagreement is recorded in `decision_log.md` and escalated to the human researcher.

### Cross-paper sharing
Sources used in multiple papers maintain a single entry in `library/papers/` and are cross-referenced in each paper's `source_registry.md` by BibTeX key.

---

## Standard Loop

A single "run" in this system is one bounded research action:

1. Acquire 10 candidate sources → populate `source_inbox.md`
2. Deduplicate and validate metadata → promote to `source_registry.md`
3. Extract claims from 5 high-value sources → update `claim_map.md`
4. Verify 1 disputed claim → update `contradiction_map.md`
5. Cluster 20 notes into themes → update `cluster_map.md`
6. Test source coverage against `source_quotas.md`
7. Run reviewer attack surface check → update `reviewer_attack_surface.md`
8. Log the run → append to `autoresearch.jsonl`

No run may end by declaring a paper ready unless the required research team has
recorded passing rows in `review_team_trace.jsonl` and
`python scripts/validate_review_team_gate.py` passes.

Each run should be completable in one agent session.

---

## Escalation Triggers

Stop and escalate to human researcher when:

- A paper may need to be killed
- Source disagreement materially affects the thesis
- Blinding is threatened
- Evidence is too thin for safe drafting
- Deadline pressure encourages a bad shortcut
- Two papers are converging to the same argument
