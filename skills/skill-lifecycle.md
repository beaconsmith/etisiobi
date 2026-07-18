# Skill: Skill Lifecycle Management
> Fat skill - MUSE-Autoskill style lifecycle for research skills.

## What This Skill Does

Turns repeated research workflow lessons into durable, evaluated skills. Use it when an agent discovers a reusable method while sweeping literature, running autoresearch, extracting evidence, writing papers, or maintaining research infrastructure.

The goal is not to make more notes. The goal is to keep a compact skill bank that accumulates experience without outrunning sources, citations, reviewer gates, or human approval.

---

## When to Invoke

Say: **"Apply skill lifecycle to [workflow/skill/failure]"**

Invoke whenever:
- a workflow succeeds after repeated trial and should be reused
- a skill fails or produces weak research output
- two skills overlap and should be merged
- a search/query/citation strategy saves time across more than one paper
- a reviewer, source, or experiment failure exposes a durable method gap

---

## MUSE Lifecycle

### 1. Creation

Create or revise a skill only when the reusable workflow is clear.

Minimum creation brief:
- task class
- inputs and outputs
- required source or evidence constraints
- failure modes the skill prevents
- validation command, rubric, or artifact check

Do not create a skill for a single paper-specific insight. Keep paper-specific decisions in that paper's `decision_log.md`.

### 2. Skill Memory

Each reusable skill may have a sibling memory file:

```text
skills/autoresearch.md
skills/autoresearch.memory.md
```

Append only compact dated notes:

```markdown
## 2026-05-28
- What was tried.
- What evidence proved it helped or failed.
- What to do differently next time.
```

Skill memory is experience, not authority. It cannot override source-first evidence, citation policy, human approval gates, or paper-specific control files.

### 3. Management

Before adding guidance:
1. Search existing skills with `rg`.
2. Update the closest existing skill when possible.
3. Merge overlapping skills instead of creating parallel doctrine.
4. Mark stale guidance as superseded before deleting it.
5. Keep the skill bank small enough that a new agent can choose correctly.

### 4. Evaluation

Do not register a skill change as reusable until it passes a check.

Allowed checks:
- autoresearch score improves under the frozen rubric
- literature sweep produces better coverage, freshness, or gap documentation
- paper section survives reviewer-attack-surface review
- citation/source check catches no fabricated or unsupported references
- script/test command passes for tooling skills
- human approval confirms publication-facing changes

### 5. Refinement

Patch one hypothesis at a time:
1. Name the failure.
2. Change one rule, query pattern, script, or rubric detail.
3. Rerun the evaluation.
4. Keep the change only if evidence improves.
5. Record discarded hypotheses briefly in the task report or memory file.

---

## Required Output

Report:
- skill created, updated, merged, pruned, or left unchanged
- skill memory note added or intentionally skipped
- evaluation used and result
- source, citation, and reviewer-risk boundaries preserved
- remaining risks and next refinement

---

## Non-Negotiables

- Never let skill memory become a citation.
- Never use skill memory to invent sources, page numbers, datasets, or reviewer claims.
- Never bypass paper promotion gates because a skill says the workflow is familiar.
- Never publish or submit automatically. User sovereignty remains final.
