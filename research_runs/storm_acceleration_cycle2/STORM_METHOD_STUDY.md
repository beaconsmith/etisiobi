# STORM Method Study for Etisiobi Cycle 2

## Observed STORM Pattern

Stanford STORM is a long-form knowledge-curation system focused on the pre-writing stage. The NAACL 2024 paper defines STORM as Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking. The public project describes two stages: pre-writing, where the system collects references and generates an outline, and writing, where the outline and references are used to generate a cited article.

The transferable mechanisms are:

- Perspective-guided question asking.
- Simulated conversations with source-grounded expert answers.
- Outline curation before drafting.
- Evaluation of outline breadth and organization.
- Human expert feedback.
- Error analysis for red herrings and source-bias transfer.
- Co-STORM-style collaborative discourse with a moderator and dynamic mind map.

## Etisiobi Transfer

Etisiobi must not copy STORM as a paper generator. The useful transfer is a pre-writing and review protocol. For Nwagu Aneke work, the perspectives are source critic, standards engineer, NLP methods reviewer, cultural authority reviewer, systems designer, and adversarial impact reviewer. The source expert is replaced by evidence files and source gates. The generated outline is not accepted until it passes layer-promotion checks.

## Non-Transferable Parts

STORM is designed for Wikipedia-like articles, not impact-journal research papers. Its own README states that the system cannot produce publication-ready articles without significant edits. Etisiobi therefore uses STORM for question discovery and outline discipline, not as evidence of submission readiness.

## Sources

- Stanford STORM paper: https://arxiv.org/abs/2402.14207
- Stanford STORM project page: https://storm-project.stanford.edu/research/storm/
- Stanford OVAL STORM repository: https://github.com/stanford-oval/storm
- Co-STORM paper: https://arxiv.org/abs/2408.15232
