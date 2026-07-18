# LOOP-CHANGE-0001

## Problem

Claim and citation audits are currently partial and seeded from core files rather than extracted exhaustively from every paper draft.

## Proposed change

Add a parser that scans all `research/papers/*/evidence/claim_map.md`, `source_registry.md`, and `writing/draft.tex` files to build a unified claim-to-citation graph.

## Expected benefit

Lower unsupported-claim risk before submission.

## Risk

False positives from heterogeneous Markdown formats.

## Validation test

Run parser on all seven paper folders and manually inspect a sample of 20 claim-source edges.

## Rollback

Delete generated parser output; no source files are rewritten.

## Approval needed?

No for read-only parser generation. Yes if it rewrites paper files.
