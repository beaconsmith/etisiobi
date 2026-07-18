# Etisiobi Lab Operating System

Generated: 2026-05-28

## Core Pipeline

```text
artifact/source/event -> observation -> extracted claim -> maturity label -> evidence gate -> experiment or source audit -> output emitter
```

## Daily Loop

1. Scan changed files and new sources.
2. Register artifacts and sources.
3. Extract claims into `corpus/claims.jsonl`.
4. Assign C0-C7/CX maturity.
5. Update contradictions.
6. Refresh visual dashboards.

## Weekly Loop

1. Review active programs.
2. Promote or demote claims.
3. Move weak mappings to `research_lattice/rejected_mappings/`.
4. Move testable mappings to `research_goals/`.
5. Produce one emitter artifact: note, dataset, figure, policy brief, teaching module, negative result, or paper section.

## Publication Loop

1. Select output type.
2. Freeze scope.
3. Run source existence checks.
4. Run claim maturity gate.
5. Run citation and rights review.
6. Run reproducibility/preflight.
7. Write limitations before abstract.
8. Require human approval for release.

## Program Rule

Each research program must expose:

- canonical artifact or event source,
- claim ledger,
- contradiction ledger,
- experiment or audit directory,
- output emitters,
- human approval gates.

## Current Operating Priorities

1. Complete the Nwagu Aneke artifact dossier.
2. Harden claim maturity and evidence gates.
3. Generalize the Research Spine.
4. Compile PAGC wiki with risk labels.
5. Clean BPE experiment reproducibility.
6. Publish visual dashboards for internal navigation.
7. Reconcile OGI paper evidence.
8. Preserve the omnidomain lattice without overclaiming.
