# Vendor Neutrality Audit

generated_at: `2026-06-21T03:11:19+01:00`
status: `VENDOR_NEUTRALITY_PASS`
blocking_hits: `0`
nonblocking_hits: `22`

Operational vendor terms are not allowed in public or operational surfaces unless explicitly quarantined as historical provenance.

## Filename Hits

None.

## Content Hits

| path | line | match | scope | blocking | context |
|---|---:|---|---|---|---|
| `corpus/repo_artifacts.jsonl` | 1 | `claude` | `generated-projection` | `false` | {"path": ".claude/scheduled_tasks.lock", "category": "unknown", "extension": ".lock", "bytes": 91} |
| `data/igbo_corpus/merged.txt` | 14348 | `Claude` | `historical-or-source` | `false` | Claude Ake |
| `data/igbo_corpus/test.txt` | 1251 | `Claude` | `historical-or-source` | `false` | Claude Kelly |
| `data/igbo_corpus/train.txt` | 2117 | `anthropic` | `historical-or-source` | `false` | Ụkpụrụ nke anthropic |
| `data/igbo_corpus/val.txt` | 853 | `Claude` | `historical-or-source` | `false` | Claude Morel |
| `ETISIOBI_REPO_ALIGNMENT_AUDIT.md` | 41 | `CLAUDE` | `historical-or-source` | `false` | \| Schema (rules) \| Procedural \| `AGENTS.md` · `CLAUDE.md` · `research/AGENTS.md` · `skills/*` · `EVIDENCE_POLICY.md` · `CLAIM_MATURITY_MODEL.md` · `HUMAN_APPROVAL_GATES.md` · `CITATION_POLICY.md` · `PUBLICATION_GATE.md`  |
| `library/download_manifest.jsonl` | 1771 | `Anthropic` | `historical-or-source` | `false` | {"title": "On the Anti-Anthropic Principle (AAP): If there is an Anthropic Principle Exists, There Must be an Anti-Anthropic Principle (AAP) Exists Too", "discipline": "thermodynamics of computation   landauer principle" |
| `library/full_missing_sources_list.md` | 1719 | `Anthropic` | `historical-or-source` | `false` | \| On the Anti-Anthropic Principle (AAP): If there is an Anthropic Principle Exists, There Must be an Anti-Anthropic Principle (AAP) Exists Too \| `https://doi.org/10.21275/art20164235` \| failed \| |
| `library/missing_report_metadata.json` | 16123 | `Anthropic` | `historical-or-source` | `false` | "title": "On the Anti-Anthropic Principle (AAP): If there is an Anthropic Principle Exists, There Must be an Anti-Anthropic Principle (AAP) Exists Too", |
| `log.md` | 37 | `CLAUDE` | `historical-or-source` | `false` | New layout: `research/icegov/`, `research/pagc/`, `skills/`, `CLAUDE.md`. |
| `obsidian_vault/01_Repo_Atlas.md` | 20 | `claude` | `generated-projection` | `false` | \| `.claude` \| dir \| |
| `papers/SELECTED_PAPER/freeze_manifest.json` | 6 | `claude` | `generated-projection` | `false` | "M .claude/settings.local.json", |
| `quarantine/legacy_prompt_driven/run_autoreason.py` | 86 | `Anthropic` | `historical-or-source` | `false` | "for Anthropic and the global scientific community. You write at the level of a Nature/Science feature " |
| `quarantine/legacy_prompt_driven/session_harness.md` | 20 | `CLAUDE` | `historical-or-source` | `false` | ├── CLAUDE.md                   ← You are here. Loaded every session. |
| `repo_index.json` | 6 | `claude` | `generated-projection` | `false` | "status_short_branch": "## research-hyperloop/bootstrap\n M .claude/settings.local.json\n M .gitignore\n M .obsidian/graph.json\n M .obsidian/workspace.json\n D \"216, k, d.md\"\n M README.md\n D RESEARCH_SPINE.md\n M lo |
| `repo_map.md` | 9 | `claude` | `generated-projection` | `false` | \| `.claude` \| dir \| |
| `research/pagc/sources/pagc_library/cognitive_science_(chunking___working_memory).md` | 3 | `Claude` | `historical-or-source` | `false` | Alzheimer's disease\n- **Authors:** Jonathan Huntley, Daniel Bor, Adam Hampshire, Adrian Owen, Robert Howard\n- **Year:** 2011\n- **Citations:** 38\n- **URL:** https://doi.org/10.1192/bjp.bp.110.083857\n- PAGC Mapping: T |
| `research/pagc/sources/pagc_library/thermodynamics_of_computation___landauer_principle.md` | 1 | `Anthropic` | `historical-or-source` | `false` | # Thermodynamics of Computation / Landauer Principle\n\n**Category Relevance Summary:** Exploring how PAGC limits and hypotheses apply to this frontier.\n\n## [1] Information erasure: Landauer's principle\n- **Authors:** |
| `research_repo_audit.md` | 13 | `claude` | `generated-projection` | `false` | M .claude/settings.local.json |
| `research_reset_audit.md` | 19 | `claude` | `historical-or-source` | `false` | D .claude/scheduled_tasks.lock |
| `scripts/vendor_neutrality_audit.py` | 44 | `claude` | `scanner-self` | `false` | "claude", |
| `vendor_neutrality_audit.md` | 18 | `claude` | `historical-or-source` | `false` | \| `corpus/repo_artifacts.jsonl` \| 1 \| `claude` \| `generated-projection` \| `false` \| {"path": ".claude/scheduled_tasks.lock", "category": "unknown", "extension": ".lock", "bytes": 91} \| |

## Policy

Use provider-neutral capability names in operational docs: `planner`, `retriever`, `scientist`, `coder`, `critic`, `reviewer`, `embedding`, `vision`.
Historical vendor traces should either be quarantined with metadata or deliberately preserved under an explicit provenance policy.
