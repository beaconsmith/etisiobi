# Etisiobi Epistemic Tripwire

**Purpose:** Convert the existing append-only `decisions/decision_log.jsonl` from a retrospective record into an *inspectable dependency watchlist* without inventing an autonomous agent or changing any decision.

```bash
python scripts/decision_tripwire.py
python scripts/decision_tripwire.py --changed corpus/bmc_count_reconciliation.json
# Optional: git diff --name-only main...HEAD > changed.txt
python scripts/decision_tripwire.py --changed-file-list changed.txt
python -m unittest discover -s tests/research -p 'test_decision_tripwire.py' -v
```

The output is JSON. `review_required=true` means a listed changed path intersects the decision's cited repository artifact or cited directory; **it does not prove the decision is false**. Reviewers should check the actual diff and decide whether to append a superseding decision. The tool does not inspect Git history or external URLs, validate legal authority, interpret natural-language reversal conditions, or alter existing artifacts.

Warnings are separate from dependency matches: `missing_reversal_condition`, `missing_risk`, `missing_local_evidence`, and `unverifiable_reference`. A conversation statement is not a durable evidence artifact. Neither a local file's existence nor a source citation establishes that the contents are correct.

## Read-only repo inspection, 2026-11-22

At the inspected `main` snapshot, the ledger contained **9** decision records. `LAB-DEC-0007`, `0008`, `0009` lack a recorded risk and reversal condition. `LAB-DEC-0005` and `0006` each contain a conversation-dependent evidence reference. These are documentation gaps, **not findings that the underlying decisions are invalid**. Source rights and authorization continue to require human review.

Example: marking `corpus/bmc_count_reconciliation.json` as changed should surface `LAB-DEC-0006` and `LAB-DEC-0007` for review. Nothing is automatically revoked or promoted.

## Why this exists

Etisiobi's conceptual reconstruction workflow needs a correction channel: a research result may undermine a *premise* shared by several downstream decisions. The tripwire identifies those decisions so the researcher can reconsider them rather than allowing an old accepted conclusion to become invisible doctrine.

Known limit: the dependency graph is incomplete because it uses only explicit `evidence` references. Transitive assumptions, informal citations, and semantic contradictions still need a human research review. Future iterations could use explicit decision-to-claim IDs, but should earn that complexity with a real test case first.
