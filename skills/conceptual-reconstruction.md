# Skill: Conceptual Reconstruction (Explore → Reconstruct → Verify)

Use this skill when Etisiobi must invent or rethink a *research model*, not when an ordinary source lookup or validator is enough. It complements, never replaces, `skills/autoresearch.md`, `research/AGENTS.md`, source and rights controls, and the lab-stage gates.

## 1. Explore: find the disputed assumption

Name the exact artifact and observed claim layer. State the current frame, a counterexample, and a genuinely different way of framing the problem. Check `research_lattice/`, claim ledgers, and previous negative results before creating a new branch. Do not treat analogy as evidence.

**Output:** one bounded question, at least one alternative hypothesis, and what would discriminate between them.

## 2. Reconstruct: propose a mechanism, not a metaphor

Specify inputs, transformations, outputs, invariants, and a failure case. Distinguish source-observed objects from derived representations. Make the smallest testable artifact; do not create a new parallel memory tree.

**Output:** an executable experiment or inspectable specification plus a falsifying test. Novelty is provisional until prior-art review; code execution does not constitute publication readiness.

## 3. Verify: give criticism veto power

Inspect local artifacts, external sources when available, rights constraints, baseline comparisons, and negative controls. Record what is *not* established. Preserve contrary results. If the model fails, keep its evidence but do not promote its claim.

**Output:** result, strongest surviving objection, conditional recommendation, decision trace, review trigger.

## 4. Connect decisions to their dependencies

Before building a new conceptual system, use `python scripts/decision_tripwire.py` to inspect the existing decision ledger. Supply `--changed path/to/artifact` (repeatable) or `--changed-file-list changed.txt` to identify decisions referencing changed evidence. The tripwire flags possible reevaluation; it never invalidates a claim or certifies rights/authority.

On changed evidence: review the cited material, question whether the former rationale still holds, and append a new authorized decision only if the evidence warrants one. Never silently rewrite historical ledger rows.

## Stop conditions

Stop when the next investigation is clear or expected information gain becomes low. Do not manufacture consensus, reviewer sign-offs, experiments, sources, or a claim of mathematical proof. Human authority controls sensitive material, product doctrine, release and publication.
