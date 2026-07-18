# Product Feedback Harness

This folder stores research-to-product reports generated from the Oroma repo.

The harness is intentionally practical: each finding should help a developer build faster tomorrow. Reports must include claim, evidence, affected surface, severity, proposed fix, and acceptance test.

Run from the Etisiobi root:

```bash
python spine/research_feedback.py --oroma ../oroma
```

Generated report set:

- `product_recommendation.md`
- `engineering_risks.md`
- `ui_benchmark_findings.md`
- `backend_truth_findings.md`
- `test_gap_report.md`

The harness does not replace human review. It creates a first pass that research, product, design, and engineering can argue with.
