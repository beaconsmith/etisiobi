# Publication Gate

Generated: 2026-05-28

## Required Checks

1. Output type selected: paper, dataset, software, atlas, negative result, policy brief, standard, teaching module.
2. Every positive claim is C5 or higher.
3. Every C3/C4 background claim is labeled with limits.
4. Every CX claim is framed as rejected or negative result.
5. Citations exist and support the exact claim.
6. Figures/tables are generated from source data or clearly marked as conceptual.
7. Code and data commands are reproducible from a clean checkout.
8. Rights, consent, CARE/FAIR, and privacy checks pass.
9. A multi-role `review_team_trace.jsonl` exists and passes for any paper marked ready.
10. No external submission or upload occurs without explicit human approval.

## Blockers

- Missing primary source for central claim.
- Unverified citation in central claim.
- Unresolved contradiction in abstract/contribution.
- Private/community data without authority.
- Dependency install or paid/cloud compute required but not approved.
- LaTeX, dataset, software, or package preflight failure.
- Missing or incomplete research-team review trace for any ready-status paper.

## Research Team Required Before Readiness

Any paper marked `READY_FOR_HUMAN_ARXIV_REVIEW`, `READY_FOR_SUBMISSION`, or
equivalent must include a `review_team_trace.jsonl` file in its paper directory.
Required roles:

- `research_lead`
- `domain_postdoc`
- `methods_reviewer`
- `adversarial_impact_reviewer`
- `citation_evidence_reviewer`
- `rights_authority_reviewer`

Run `python scripts/validate_review_team_gate.py`. If it fails, the paper is
not ready regardless of PDF, citations, benchmark score, or author confidence.

## Current Output Channels

See `emitters/`.
