# Product Feedback Harness

This folder stores research-to-product reports generated from the Oroma repo.

The harness is intentionally practical: each finding should help a developer build faster tomorrow. Reports must include claim, evidence, affected surface, severity, proposed fix, and acceptance test.

Run from the Etisiobi root:

```bash
python spine/research_feedback.py --oroma ../oroma-product
```

Generated report set:

- `product_recommendation.md`
- `engineering_risks.md`
- `ui_benchmark_findings.md`
- `backend_truth_findings.md`
- `test_gap_report.md`

The harness does not replace human review. It creates a first pass that research, product, design, and engineering can argue with.

## Source authenticity and freshness boundary

The default target is the current `beaconsmith/oroma-product` checkout, not the archived `beaconsmith/oroma` repository. The harness requires a supported product layout (backend routes, schema, frontend surfaces, and repo control files) **before creating any output**; a missing checkout fails rather than producing a plausible-looking empty-source report.

The current Vite frontend lives under `apps/oroma-experience/src/surfaces` and `apps/oroma-refined/src/surfaces`. Historical Next.js checkouts under `frontend/app` remain supported when passed explicitly.

This is a **lightweight file inventory and recommendation generator**, not a code test, a freshness-certified assessment, a security audit, or a product-readiness verdict. Where current assessment files are absent, findings must say the status is unverified rather than recycling an old readiness score or CRITICAL claim. A valid checkout does not by itself establish that any defect still exists.

Regression check: `python -m unittest discover -s tests/research -p 'test_research_feedback_source_guard.py' -v`.
