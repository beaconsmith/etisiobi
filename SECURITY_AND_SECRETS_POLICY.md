# Security and Secrets Policy

Generated: 2026-05-28

## Threat Model

- Prompt injection in repo documents and web sources.
- Secret leakage from environment, logs, datasets, PDFs, notebooks, or screenshots.
- Malicious dependencies and auto-install scripts.
- Private Oroma/product data exposure.
- Community-sensitive cultural artifact release.
- Hallucinated citations or fabricated results.

## Rules

1. Never print secrets.
2. Do not auto-install dependencies in experiments.
3. Use read-only product/database access for evidence extraction.
4. Do not upload data, submit papers, publish packages, or call paid/cloud APIs without human approval.
5. Redact logs before publication.
6. Keep generated artifacts separate from source artifacts.
7. Use source, claim, and rights registries before public release.
8. Treat cultural materials as governed artifacts, not free content.

## Human Approval Required

- External submission.
- Dependency installation.
- Paid/cloud compute.
- Production/private data access.
- Public release of scans, source images, datasets, fonts, or community-derived records.
- License changes.
