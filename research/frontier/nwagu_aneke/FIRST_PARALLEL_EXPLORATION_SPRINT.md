---
type: frontier_sprint
program: nwagu_aneke_frontier
status: first_artifacts_complete_internal_not_ready
created: "2026-06-22"
updated: "2026-06-22T18:34:57+01:00"
goal: GOAL-FRONTIER-001
---

# First Parallel Exploration Sprint

## Sprint Rule

Do not select only one path. Launch three orthogonal, bounded branches that
increase the number of informed possibilities while preserving evidence,
rights, and claim-layer integrity.

This sprint does not create public-release, paper-ready, or frontier-ready
claims.

## Track A: Source and Reconstruction

Question:

```text
Does Azuonye 1992 confirm, revise, or weaken the current 26/208 source-observed
and 27/216 derived count-layer audit?
```

Evidential layer:

- source-facing;
- currently partial;
- rights and quotation status unknown.

Method:

1. Verify bibliographic and source metadata for Azuonye 1992.
2. Extract count-relevant evidence about rows, columns, f/v, and logographs.
3. Classify the matrix as observed structure, editorial display, or unresolved.
4. Record rights/quotation limits.
5. Update the count-layer dossier only if the source evidence supports it.

Expected learning:

- whether the current count-layer audit is strengthened, revised, or weakened;
- which exact questions remain for human/domain review.

Failure condition:

- source cannot be accessed or does not contain count-relevant evidence; record
  as a blocked or negative result, not as confirmation.

Artifact output:

`research/frontier/nwagu_aneke/results/EXP-NA-002-source-note-azuonye-1992.md`

Status:

- First artifact produced.
- Azuonye 1992 Appendix I strengthens the current 26 x 8 source-display count
  and combined `f/v` row finding.
- Appendix II content recovery remains blocked/unresolved in the local PDF
  extraction/render trail.
- Dedicated recovery audit added at
  `research/frontier/nwagu_aneke/source_reviews/azuonye_1992_appendix_ii_recovery.md`.
- Source-acquisition lead table and unsent ScholarWorks request draft added
  under `research/frontier/nwagu_aneke/source_reviews/`.

Rights implications:

- no reproduction of restricted figures or long extracts;
- citation and short paraphrase only until rights review.

Next-branch options:

- source comparison dossier;
- human transcription review packet;
- count-layer audit revision.

## Track B: Computation and Representation

Question:

```text
Can a machine-readable claim-layer schema preserve source-observed, derived,
speculative, computational, applied, contested, and restricted records across
experiments?
```

Evidential layer:

- method infrastructure;
- applies across source, derived, computational, and applied records.

Method:

1. Use `CLAIM_LAYER_SCHEMA.md` as the draft vocabulary.
2. Encode a small fixture set covering:
   - 26x8 source-observed count;
   - 27/216 derived f/v split;
   - manuscript corpus restricted status;
   - PAGC speculative claims;
   - layer-safe design application.
3. Validate whether each fixture has source refs, uncertainty, rights status,
   contradiction refs, and collapse conditions.

Expected learning:

- whether the schema can drive future validators, visualizers, and LPE fixtures.

Failure condition:

- schema cannot represent contested or applied records without flattening them;
  revise schema instead of forcing data to fit.

Artifact output:

`research/frontier/nwagu_aneke/claim_layer_fixtures.jsonl`

Status:

- First artifact produced.
- Fixture review added at
  `research/frontier/nwagu_aneke/claim_layer_fixture_review.md`.
- Fixtures cover source-observed, derived, restricted, speculative,
  computationally-generated, applied, contested, and dropped records.
- Fixture validator added at `scripts/validate_claim_layer_fixtures.py`.
- Interface outline, static prototype, and usability packet now use these
  fixtures; remaining Track B branches are JSON Schema hardening or LPE fixture
  generation.

Rights implications:

- use non-sensitive metadata only.

Next-branch options:

- JSON Schema validator;
- layer-aware visualization;
- LPE fixture generator.

## Track C: Interface, Preservation, or Application

Question:

```text
Can a simple layer-view artifact make observation, derivation, speculation, and
application distinguishable to a reader without turning the visual into proof?
```

Evidential layer:

- applied/interface;
- must show lineage back to source and derived records.

Method:

1. Create a static outline for a layered count-model view.
2. Separate source-observed, derived, speculative, and applied panels.
3. Include visible "not source-observed" markers for 27/216.
4. Avoid source-image reproduction until rights review.
5. Identify how the view could become interactive later.

Expected learning:

- whether public legibility can improve without weakening claim discipline.

Failure condition:

- the interface makes derived or speculative layers look more authoritative than
  source-observed records.

Artifact output:

`research/frontier/nwagu_aneke/interfaces/count_layer_view_outline.md`

Status:

- First artifact produced.
- Interface index added at
  `research/frontier/nwagu_aneke/interfaces/README.md`.
- Data-to-view map added at
  `research/frontier/nwagu_aneke/interfaces/count_layer_data_to_view_map.jsonl`.
- View-map validator added at `scripts/validate_count_layer_view_map.py`.
- Rights-safe static prototype added at
  `research/frontier/nwagu_aneke/interfaces/count_layer_static_prototype.html`.
- Static prototype validator added at
  `scripts/validate_count_layer_static_prototype.py`.
- Comprehension-test packet added under
  `research/frontier/nwagu_aneke/interfaces/usability/`.
- Usability packet validator added at
  `scripts/validate_count_layer_usability_packet.py`.
- Scorer added at `scripts/score_count_layer_comprehension_results.py`, with
  dependency-free tests at
  `tests/research/test_count_layer_comprehension_scoring.py`.
- Next branch is a 3-5 reader run with scored results to test whether
  `27/216` remains visibly derived and `26/208` remains visibly
  source-observed.

Rights implications:

- no source images;
- text and abstract tables only.

Next-branch options:

- static HTML prototype;
- visual atlas;
- usability/contact test instrument.

## Sprint Completion Criteria

The sprint has made progress when all three tracks have produced their first
artifact and each artifact states:

- question;
- layer;
- method;
- expected learning;
- failure condition;
- rights implication;
- next-branch options.

Status: first artifacts complete. The sprint remains internal and not ready for
publication, public release, or paper-promotion language.
