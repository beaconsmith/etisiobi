# Skill: Autoresearch Loop
> Fat skill — loaded by reference. Based on Karpathy autoresearch + Orchestra Research two-loop architecture.

## What This Skill Does

Applies metric-driven iterative improvement to any research artifact — paper drafts, indicator frameworks, literature wikis, experiment results. The agent modifies the artifact, evaluates it against a frozen metric, keeps or reverts, and repeats.

**Core loop:**
```
draft artifact → evaluate against metric → identify weakest dimension
→ apply targeted revision → re-score → keep if improved, revert if not
→ repeat until metric target reached or diminishing returns
```

---

## When to Invoke

Say: **"Run autoresearch loop on [paper/section/framework/experiment]"**

The agent will:
1. Read the current artifact
2. Define or recall the evaluation metric for that artifact type
3. Score the current state across all metric dimensions
4. Identify the lowest-scoring dimension
5. Apply a focused revision (one dimension at a time)
6. Re-score the revised artifact
7. Report: score change, what was revised, what remains

---

## Metric Definitions by Artifact Type

### Academic Paper (ICEGOV Track 6)
Score 1–5 across:
- **Novelty** — does it propose something not in prior ICEGOV/EGOV papers?
- **Measurement rigor** — are indicators defined, operationalized, bounded, with abuse cases?
- **Contextual grounding** — real institutions, real statistics, real geographic context?
- **Track fit** — measurement methodology paper, not platform pitch or case study?
- **Reviewer-resistance** — preempts the known objections with cited evidence?
- **Global South perspective** — explicit about what Global South contexts require differently?

Target: all dimensions ≥ 4/5. Composite ≥ 4.5/5 = submittable.

### Indicator Framework
Score 1–5 across:
- **Coverage** — all Ostrom principles mapped to at least one indicator?
- **Computability** — each indicator has formula + data source + query logic?
- **Goodhart documentation** — each indicator has a named abuse case + mitigation?
- **Privacy compliance** — CARE principles satisfied? ZK or minimal-disclosure path documented?
- **Sensitivity** — weighting choices tested under alternative schemes?

### Literature Wiki (WIKI.md)
Score 1–5 across:
- **Coverage** — all 7 clusters represented with ≥15 sources each?
- **Synthesis quality** — cross-cluster connections documented?
- **Freshness** — sources from last 3 years present in each cluster?
- **Gap documentation** — missing areas explicitly named?
- **Reviewability** — can a reader find the 10 most important sources in under 2 minutes?

---

## Execution Protocol

```
1. STATE: "Running autoresearch loop on [artifact]. Current score: [X/5]."
2. IDENTIFY: "Lowest-scoring dimension: [name] at [score]."
3. REVISE: Apply targeted edit. State what was changed and why.
4. RE-SCORE: "New score: [Y/5]. Delta: [+/-Z]."
5. DECIDE: Keep if Y > X. Revert and try next-lowest dimension if Y ≤ X.
6. REPEAT until target reached or 3 consecutive non-improvements.
7. FINAL REPORT: Composite score, each dimension, remaining revision list.
```

---

## Important Constraints

- **One dimension per iteration.** Don't revise multiple dimensions simultaneously — you lose signal on what worked.
- **Freeze the metric before the first iteration.** Changing the evaluation criteria mid-loop is the most common failure mode.
- **Document every iteration.** Write AUTORESEARCH_EVAL_vN.md for each loop cycle. This is the audit trail.
- **User sovereignty.** Present the revised artifact and score. The user decides whether to keep it. The agent never auto-publishes.

---

## Skill Lifecycle Trigger

If an autoresearch loop discovers a reusable workflow, failure mode, scoring shortcut, source strategy, or reviewer defense pattern, invoke `skills/skill-lifecycle.md`.

Use the MUSE lifecycle:
1. Search existing skills first.
2. Patch one reusable rule at a time.
3. Re-run the frozen metric or reviewer check.
4. Record only evidence-backed lessons in the skill or its sibling `.memory.md`.
5. Keep paper-specific decisions in the paper folder, not in global skills.

Do not register a skill lesson if the score did not improve, the evidence base stayed thin, citations became weaker, or reviewer risk increased.

---

## Reference: Karpathy Autoresearch Design Principles
- Fixed time budget per experiment (we use: fixed scope per revision — one dimension)
- Single measurable metric (val_bpb for ML; composite reviewer score for papers)
- Immutable evaluation harness (prepare.py equivalent: the metric definition never changes mid-loop)
- Agent edits only one file (train.py equivalent: the artifact under revision)
- program.md equivalent: this SKILL.md + the evaluation rubric above
