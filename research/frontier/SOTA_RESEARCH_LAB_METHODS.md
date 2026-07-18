# SOTA Research Lab Methods

Date: 2026-06-21

## Purpose

This file anchors Etisiobi's lab design against current external research
automation methods. It is not a literature review for a paper. It is the
operating standard for making the lab competitive with current autonomous
research systems.

## External Methods Reviewed

| Method | What it contributes | What Etisiobi must learn | Gap Etisiobi can own |
|---|---|---|---|
| Stanford STORM / Co-STORM | Pre-writing knowledge curation through retrieval, outline generation, and multi-perspective question asking. | Use retrieval before writing and separate knowledge curation from paper claims. | STORM does not decide artifact evidence layers or cultural authority gates. |
| MLAgentBench | Benchmark tasks with clear goals, code execution, logs, and automatic evaluation for ML experimentation agents. | Every autonomous research loop needs fixed tasks, metrics, baselines, and keep/reject decisions. | Etisiobi needs equivalent benchmarks for source-critical and cultural-artifact research, not only ML accuracy. |
| The AI Scientist / AI Scientist-v2 | End-to-end ideation, experiments, figures, writing, and simulated review; v2 adds agentic tree search and workshop-level peer-review evaluation. | Research automation must produce experiments and reviewer-facing results, not notes. | Etisiobi must add rights, source authority, layer safety, and artifact-specific review to the AI Scientist loop. |
| Google AI Co-Scientist | Multi-agent hypothesis generation, debate, ranking, review, and scientist-guided validation. | A serious lab uses adversarial teams and hypothesis tournaments before claiming novelty. | Etisiobi can specialize this pattern for African knowledge systems and artifact-grounded systems design. |
| GLOSSOPETRAE | Procedural xenolinguistics engine with deterministic language generation, model tasks, raw result traces, and tokenizer/monitor blind-spot experiments. | Symbolic systems become serious research when they produce deterministic artifacts, controlled tasks, raw data, and safety audits. | Etisiobi can safely adapt the method for source-layer visibility, layer safety, tokenizer audit, and defensive publication hygiene. |
| elder-plinius profile audit | Portfolio-level pattern across 46 public repos: named instruments, demos, validation reports, raw traces, research papers, and adversarial correction logs. | Etisiobi must stop leading with article folders and instead build named instruments with visible demos and benchmark-grade outputs. | Etisiobi can own artifact-grounded source/derived claim-drift benchmarks for cultural-symbolic research. |
| PROV-O / RO-Crate / IIIF / TEI / Web Annotation / CIDOC CRM | Standards for provenance, research packaging, source localization, text encoding, annotation, and cultural heritage graphs. | Standards compatibility is table stakes. | Standards do not by themselves prevent count-layer promotion or speculative design claims. |

## Design Implication

Etisiobi should not compete by generating more papers. It should compete by
making a new class of benchmarked research possible:

```text
artifact source -> evidence layer -> claim layer -> design layer -> publication layer
```

The frontier contribution is the prevention, detection, and measurement of
**layer-promotion errors**: cases where derived, speculative, blocked, or
design-layer claims are rewritten as source-observed facts.

## Sources

- Stanford STORM project: https://storm-project.stanford.edu/research/storm/
- Stanford OVAL STORM repository: https://github.com/stanford-oval/storm
- MLAgentBench: https://arxiv.org/abs/2310.03302
- Sakana AI Scientist: https://arxiv.org/abs/2408.06292
- AI Scientist-v2: https://arxiv.org/abs/2504.08066
- Google AI Co-Scientist: https://arxiv.org/abs/2502.18864
- GLOSSOPETRAE: https://github.com/elder-plinius/GLOSSOPETRAE
- elder-plinius public profile: https://github.com/elder-plinius
- PROV-O: https://www.w3.org/TR/prov-o/
- RO-Crate: https://www.researchobject.org/ro-crate/
- IIIF Presentation API: https://iiif.io/api/presentation/
- TEI Guidelines: https://tei-c.org/guidelines/
- W3C Web Annotation: https://www.w3.org/TR/annotation-model/
- CIDOC CRM: https://www.cidoc-crm.org/
