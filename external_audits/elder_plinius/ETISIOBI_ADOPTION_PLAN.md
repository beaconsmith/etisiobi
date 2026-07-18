# Etisiobi Adoption Plan From elder-plinius Profile Audit

Date: 2026-06-21

Source profile: <https://github.com/elder-plinius>

## Audit Boundary

This audit cloned and inventoried the 46 public repositories listed on the
profile. It read public code, papers, READMEs, validation reports, experiment
folders, and result-file structure. It did not execute external code and does
not reproduce offensive implementation details.

## High-Value Pattern

The profile is not impressive only because of one paper. It is impressive
because the better projects use a repeatable public-output stack:

```text
named instrument
-> runnable artifact
-> public demo
-> raw result traces
-> validation report
-> paper/report
-> objections/corrections
```

Etisiobi has too often inverted this:

```text
paper/report first
-> internal scaffolding
-> weak experiment
-> PDF
```

That inversion is the main quality failure.

## Profile-Level Findings

From the local inventory:

- Repos audited: 46
- Public-demo pattern: 27 repos
- Agent/autonomous workflow pattern: 13 repos
- Symbolic-language/system pattern: 13 repos
- Research-report pattern: 8 repos
- Red-team/security pattern: 10 repos
- LLM parameter/search pattern: 5 repos

The strongest reusable lesson is not the offensive red-team content. It is the
artifact discipline: named tools, visible demos, experiments, raw outputs,
figures, and validation reports.

## What Etisiobi Should Copy

### 1. Create Named Instruments, Not Article Folders

Replace generic folders such as `006-unicode-readiness` with named instruments:

| Current weak form | Better instrument |
|---|---|
| Article 006 | `NwaguScriptReadiness` |
| Layer-promotion benchmark | `LPE-Bench` |
| 26x8 ledger | `NwaguLedger` |
| PAGC claim gate | `LayerSafe` |
| Visual research map | `Etisiobi Atlas` |

Every serious paper should be attached to one named instrument.

### 2. Make The First Table A Result, Not A Status Table

GLOSSOPETRAE's paper opens with a load-bearing experimental table. Etisiobi's
papers have used tables that look like internal project management:

```text
Experiment ID | Decision | Evidence score | IJRS
```

That is not a public research result. For Etisiobi, the first table should look
like:

```text
Condition | Agent family | Layer labels visible? | LPE rate | Human reviewer catch rate | CI
```

or:

```text
Representation | Human readability | Model task accuracy | Layer-confusion rate | Source/derived error rate
```

### 3. Add A Validation Report Before Any Paper Claim

GLOSSOPETRAE includes a validation report that documents confirmed defects,
fixes, regression tests, caveats, and remaining publication blockers. Etisiobi
needs this for every serious benchmark:

```text
VALIDATION.md
raw_results/
figures/
paper/
```

Required sections:

- Remediation status
- Validity table
- Defects found by adversarial review
- What was fixed
- What remains unmeasured
- Which claims may not be published yet

### 4. Use Sweep-Style Experiments

AutoTemp/HyperTune-style sweeps are useful for Etisiobi. For each research
agent/paper pipeline, test multiple prompt/layer configurations and keep only
the configuration that improves the score.

Etisiobi equivalent:

```text
baseline agent
vs source-label agent
vs source+derived-label agent
vs claim-gated agent
vs adversarially reviewed agent
```

Metric:

```text
Layer Promotion Error rate
```

### 5. Separate Engine Validity From Model Claims

GLOSSOPETRAE's validation report separates engine determinism from real-model
claims. Etisiobi must do the same:

```text
NwaguLedger validity != agent benchmark validity
agent benchmark validity != paper novelty
paper novelty != public release approval
```

Do not let a working local script imply a paper result.

### 6. Use Objections As Paper Structure

Every Etisiobi paper should include anticipated objections before submission:

- "Is this just a standards wrapper?"
- "Is 27/216 being smuggled in as source evidence?"
- "Is the benchmark circular because labels are constructed by the same agent?"
- "Does the result generalize outside Etisiobi?"
- "Is the cultural/source authority clear enough?"

If the paper cannot answer these cleanly, it is not ready.

## What Etisiobi Must Not Copy

- Do not copy covert-channel payload construction.
- Do not copy jailbreak or evasion instructions.
- Do not use edgy red-team posture as a substitute for scientific clarity.
- Do not overstate benchmarks from internal or synthetic labels.
- Do not let public demos expose restricted cultural material.

## Immediate Etisiobi Upgrade

Create one public-grade instrument:

```text
LPE-Bench: Layer Promotion Error Benchmark
```

Research question:

```text
Do AI research agents promote derived or speculative Nwagu/PAGC interpretations
into source-observed claims, and which controls reduce that error?
```

Minimum experiment:

```text
N = 360 cases
Conditions:
  1. no layer labels
  2. source/derived labels visible
  3. claim gate visible
  4. adversarial reviewer visible
Models/agents:
  at least 3 agent configurations
Review:
  independent human/domain annotation for the gold set
Metrics:
  precision, recall, F1, MCC, severity-weighted recall, confidence intervals
Outputs:
  raw JSON/CSV traces, figures, validation report, paper draft
```

This is the first Etisiobi paper that can plausibly reach impact-journal level:

```text
Layer Promotion Error: Measuring Source/Derived Claim Drift in AI Research Agents
```

## Adoption Checklist

Before Etisiobi writes another article package:

- [ ] Name the instrument.
- [ ] Define the benchmark task.
- [ ] Freeze the dataset/cases.
- [ ] Use independent labels.
- [ ] Run baselines.
- [ ] Emit raw result traces.
- [ ] Generate public-facing figures.
- [ ] Write `VALIDATION.md`.
- [ ] Write anticipated objections.
- [ ] Only then draft the paper.

