# Human Approval Gates

The research loop must stop and ask for approval before:

- Installing dependencies or running unknown package scripts.
- Running paid APIs or cloud compute.
- Uploading data, results, PDFs, or source packages externally.
- Accessing production databases or private pilot/community data.
- Running expensive experiments.
- Submitting to EDAS, arXiv, ACM, or any venue.
- Deleting, moving, or rewriting user files.
- Changing licenses.
- Publishing generated papers or archives.
- Expanding the loop's permissions, autonomy, or data access.

Default allowed actions:

- Read-only scans.
- Path-only secret-risk scans that do not print values.
- Generating local Markdown/JSON/YAML/LaTeX scaffolds.
- Dry-run validation.
