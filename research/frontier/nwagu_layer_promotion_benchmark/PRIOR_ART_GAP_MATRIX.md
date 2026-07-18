# Prior-Art Gap Matrix

## Current Novelty Hypothesis

Layer Promotion Error is not ordinary factuality. It is evidentiary-status
laundering: a generated or edited output rewrites a derived, speculative,
design, or blocked claim as if it were source-observed.

## Required Prior-Art Clusters

| Cluster | Why it matters | Current status | Risk |
|---|---|---|---|
| FEVER / SciFact / AVeriTeC claim verification | Strongest collision with evidence-supported claim checking. | Seed anchors added: FEVER and SciFact. AVeriTeC still missing. | High |
| LLM factuality and attribution | May already evaluate unsupported or citation-faithful generation. | Missing. | High |
| PROV constraints and workflow provenance | May already express evidence dependencies. | Partial. | Medium |
| SHACL / ShEx / OWL validation | May already validate evidence-layer constraints over graphs. | SHACL anchor added; ShEx/OWL still missing. | High |
| Information-flow type systems | Label lattices and noninterference resemble evidence-layer monotonicity. | Denning-style lattice/information-flow anchor added; modern IFC still missing. | High |
| Digital humanities source criticism | Scholarly editing already handles source/intervention uncertainty. | Missing. | High |
| Cultural heritage uncertainty models | CIDOC CRM extensions may model contested identification and inference. | Missing. | Medium |
| CARE / Local Contexts / Indigenous data governance | Needed for rights and authority gates. | Partial. | High |
| Benchmark validity for hallucination/provenance | Needed to avoid synthetic benchmark overclaim. | Missing. | High |
| Inspect-style evaluation harnesses | Needed to avoid inventing a private evaluation shape when a public eval framework exists. | ATLAS-0049 primary-source relevance verified; bounded no-install port plan created at `experiments/EXP-FRONTIER-007-inspect-ai-lpe-port/`. | Medium |

## Decision

Keep the sprint, but block paper promotion until this matrix is filled with
verified sources and a novelty-collision decision.

## Seed Sources Added

- FEVER: https://aclanthology.org/N18-1074/
- SciFact: https://aclanthology.org/2020.emnlp-main.609/
- SHACL: https://www.w3.org/TR/shacl/
- Denning lattice model of secure information flow: https://www.cs.nmt.edu/~doshin/t/s06/cs589/pub/7.Denning-LMIF.pdf
- Inspect AI documentation: https://inspect.aisi.org.uk/
- Inspect AI repository: https://github.com/UKGovernmentBEIS/inspect_ai
