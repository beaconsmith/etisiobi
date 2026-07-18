# Derived Hypothesis Charter

Date: 2026-06-27

## Purpose

This charter fixes a failure mode in the PAGC research system: the lab has been
strong at blocking false source claims, but too weak at growing formal
hypotheses.

The correction is simple:

```text
source truth stays strict;
derived hypotheses become testable;
experiments decide what survives;
papers claim only what their evidence type supports.
```

This charter does not weaken `PAGC_RESET.md`. It adds a positive lane for modern
formalization work that is explicitly not historical proof.

## Non-Negotiable Boundary

The current Nwagụ Aneke source-observed foundation remains:

```text
26 rows x 8 vowel/modifier columns = 208 records
```

The `27 x 8 = 216` layer remains a derived f/v split or completion hypothesis
unless later source evidence promotes it. It must never be described as
source-observed, historically proven, culturally authorized, or public-release
ready.

Clean wording:

> This work begins from the Nwagụ Aneke script tradition but does not claim that
> the modern formal model was historically explicit in that tradition. The model
> is a derived research construction inspired by observed structural features.

## Four Research Lanes

### Lane 1: Source Lane

Purpose: protect historical truth.

Questions:

- What does the source actually show?
- What did Nwagụ Aneke write?
- Which rows, signs, manuscripts, and variants are observed?

Allowed outputs:

- source inventory
- manuscript census
- sign catalogue
- historical or linguistic paper

Evidence standard: strict source, provenance, rights, and expert review.

### Lane 2: Formalization Lane

Purpose: turn observed structures into mathematical or computational objects.

Questions:

- What happens if the chart is modeled as a table?
- Which gaps, transformations, symmetries, and invariants appear?
- What does the source-observed 26 x 8 layer do?
- What does a derived 27 x 8 completion add?
- Is the completion arbitrary, useful, or falsifiable?

Allowed outputs:

- formal note
- toy model
- symbolic grammar
- matrix model
- generative rule set
- counterexample

Evidence standard: definitions, invariants, examples, and counterexamples. This
lane requires logical coherence, not historical proof.

### Lane 3: Experimental Lane

Purpose: test whether a formal model does anything.

Questions:

- Does the model compress, recover, classify, generate, or explain better than
  baselines?
- Does it improve memory, analogy, tokenization, or design-space search?
- Does an ablation remove the effect?

Allowed outputs:

- benchmark
- simulation
- ablation
- human study design
- empirical report
- negative result

Evidence standard: measurable performance against trivial and relevant
baselines.

### Lane 4: Transfer Lane

Purpose: explore whether a structure travels across disciplines without turning
analogy into evidence.

Questions:

- Does the structure resemble role binding, semantic memory, graph grammars,
  ontology engineering, chemical valence, codons, or design-space search?
- Does the mapping produce a non-trivial prediction?
- What would falsify the analogy?

Allowed outputs:

- cross-domain map
- theory note
- article candidate
- negative transfer result

Evidence standard: structural mapping plus a testable consequence.

## Claim Types and Proof Standards

| Claim type | Allowed wording | Needed proof |
|---|---|---|
| Historical claim | "the source shows..." | source, manuscript, provenance, rights status |
| Linguistic claim | "the corpus supports..." | corpus, transliteration, expert analysis |
| Formal claim | "define a model where..." | definitions, invariants, examples, counterexamples |
| Computational claim | "the model improves..." | benchmark, baseline, ablation |
| Cognitive claim | "participants remember..." | human experiment and analysis |
| Cross-domain claim | "this maps to..." | structural mapping plus non-trivial prediction |
| Philosophical claim | "this clarifies..." | conceptual clarity and explanatory power |

No claim type may borrow proof from another lane. A formal model can be
interesting without being historically proven. A historical source can be real
without proving a modern formal model.

## Derived Hypothesis Rules

1. Source-observed claims remain strict.
2. Derived hypotheses are allowed.
3. Derived hypotheses must never be presented as historical facts.
4. Every derived structure must define its rules.
5. Every derived structure must name its input layer.
6. Every derived structure must state what it invents.
7. Every derived structure must face baselines or counterexamples.
8. Every derived structure must produce a test, a kill condition, or be parked.
9. Transfer claims must name the structural mapping and the prediction it makes.
10. Publication language must state the evidence lane before stating the claim.

## Hypothesis Record Template

Every derived hypothesis should use this compact record before it becomes a
paper branch.

```text
id:
title:
lane:
source inputs:
invented/derived step:
formal object:
research question:
hypothesis:
baseline:
test:
kill condition:
allowed wording:
forbidden wording:
stage:
next action:
```

## Initial Quarantined Hypotheses

These are not findings. They are starter specimens for formal and experimental
work.

Current formal records:

- [`DH-001: Derived 27 x 8 Completion`](hypotheses/DH-001-derived-27x8-completion.md)
  is now `PARKED_BY_GLOBAL_BENCHMARK_GATE`, with the source/derived boundary
  intact and the current positive result rejected as label-dependent.
- [`DH-003: Layer-Promotion Error Benchmark`](hypotheses/DH-003-layer-promotion-error-benchmark.md)
  is now `INTERNAL_KNOWLEDGE_BREAKTHROUGH`, with ten bounded benchmark-design
  knowledge units and no paper/public/global-readiness promotion.

### DH-001: Derived 27 x 8 Completion

Lane: Formalization.

Hypothesis: splitting the f/v row into two formal roles creates a 27 x 8 matrix
whose usefulness can be tested without claiming that 27 rows are source-observed.

Baseline: source-observed 26 x 8 layer; shuffled or random completion.

Test: compare whether the derived completion improves recovery, consistency,
analogy generation, or error detection over the 26 x 8 and shuffled baselines.

Kill condition: no measurable gain, or any result that depends on calling 27 x 8
source-observed.

### DH-002: Base/Modifier Generative Grammar

Lane: Formalization -> Experimental.

Hypothesis: a base plus vowel/modifier grammar can generate useful constrained
variation from the observed chart structure.

Baseline: flat sign inventory; ordinary syllable table; random base/modifier
assignment.

Test: define generation rules, then measure compression, reconstruction error,
or invalid-form rejection against baselines.

Kill condition: the grammar only restates the table and does not improve any
measured task.

### DH-003: Layer-Promotion Error Benchmark

Lane: Experimental.

Hypothesis: autonomous research agents can be evaluated on whether they promote
derived, speculative, or blocked claims into source-observed or publication-ready
claims.

Baseline: no layer labels; citation-only prompting; source/derived labels
without a claim gate.

Test: score promotion-error recall, false positives, and derived-layer
preservation on held-out claims.

Kill condition: the benchmark catches only obvious wording and fails on table,
caption, metadata, or interface-label promotions.

Current state: selected as the next active branch after
`EXP-DH-003-layer-promotion-knowledge-benchmark` produced ten traceable internal
knowledge units from existing LPE evidence. The next action is full label
quality routing and blind review, not paper promotion.

### DH-004: Concept-Indexing and Memory Structure

Lane: Transfer.

Hypothesis: the source/derived layer structure may function as a useful
concept-indexing or memory constraint when translated into a modern formal
system.

Baseline: unstructured memory list; ordinary vector retrieval; flat concept
taxonomy.

Test: compare retrieval precision, update stability, or explanation quality
under fixed memory budgets.

Kill condition: no improvement over ordinary retrieval or taxonomy baselines.

## Promotion Path

A derived hypothesis moves through these states:

```text
QUARANTINED_HYPOTHESIS
DEFINED_FORMAL_OBJECT
TOY_MODEL_BUILT
BASELINE_TESTED
EXPERIMENTAL_RESULT
PAPER_CANDIDATE
```

`PAPER_CANDIDATE` still requires the lab-wide A+ gate. A derived hypothesis may
be exciting and still not be a paper.

## What This Changes

Before this charter, the failure pattern was:

```text
Is 27 x 8 source-observed?
No.
Stop.
```

After this charter, the research logic is:

```text
Is 27 x 8 source-observed?
No.

Is it a legitimate derived formal hypothesis?
Maybe.

Does it explain source irregularities?
Test.

Does it outperform 26 x 8 or trivial baselines?
Test.

Does it transfer beyond the artifact with a prediction?
Test.

If it survives, publish as modern formalization, not historical claim.
```

That is the lane where frontier work is allowed to mature without lying.
