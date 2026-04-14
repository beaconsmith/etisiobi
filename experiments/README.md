# PAGC Experiments

> **Karpathy standard:** Every claim must be falsifiable with a single command.
> No numbers = no paper.

## Structure

```
experiments/
  01_bpe_igbo_k27/          # Does k=27 emerge as natural vocabulary optimum?
  02_mdl_comparison/        # Is PAGC 27×8 compressive vs flat alphabets?
  03_cross_lingual_k/       # Does the optimal k differ across tone languages?
  04_e6_mapping/            # Can Aneke bases map to 27-dim E6 representation?
```

---

## Experiment 01 — BPE k=27 Sweep (THE core test)

**Hypothesis:** k=27 is the natural optimal BPE vocabulary size for Igbo text.

**Method:** Train BPE tokenizers at k=15..50 on Igbo corpus. Measure fertility,
coverage, compression. Find the inflection (knee of the fertility curve).

**Falsification:** If inflection is not at k=27 (±2), the specific PAGC
vocabulary-size claim is refuted.

```bash
# Step 1: Download Igbo corpus
python experiments/01_bpe_igbo_k27/fetch_corpus.py

# Step 2: Run sweep (takes ~5 mins)
python experiments/01_bpe_igbo_k27/train_bpe_sweep.py

# Results in: experiments/01_bpe_igbo_k27/results/
```

**Output files:**
- `results/bpe_sweep_metrics.json` — raw numbers
- `results/bpe_sweep_combined.png` — 2x2 figure (fertility, coverage, compression, marginal gain)
- `results/report.md` — auto-generated verdict

---

## Experiment 02 — MDL Comparison (planned)

**Hypothesis:** PAGC's 27×8=216 generative matrix achieves a shorter description
length for Igbo cultural texts than flat Unicode or standard BPE.

**Method:** Compute Minimum Description Length for a standardized Igbo text
encoded under: (a) UTF-8, (b) BPE k=27, (c) PAGC 216-token matrix.

```bash
python experiments/02_mdl_comparison/mdl_calc.py
```

---

## Experiment 03 — Cross-Lingual k Optimum (planned)

**Hypothesis:** The optimal BPE fertility knee varies by language family.
Tone languages (Igbo, Yoruba, Ewe) converge near k=27.

**Method:** Run Experiment 01 sweep on: English, Swahili, Yoruba, Hausa, Igbo.
Compare inflection k across languages.

```bash
python experiments/03_cross_lingual_k/sweep_multilingual.py
```

---

## Experiment 04 — E6 Algebraic Mapping (planned)

**Hypothesis:** The 27 Aneke bases can be non-trivially mapped to the 27
fundamental representations of the Lie group E₆.

**Method:** Compute the character table of the 27-dim representation of E₆.
Attempt a bijection with Aneke bases. Measure structural overlap.

```bash
python experiments/04_e6_mapping/e6_aneke_map.py
```

---

## Status

| Experiment | Status | Result |
|------------|--------|--------|
| 01 — BPE k=27 sweep | `READY TO RUN` | Pending |
| 02 — MDL comparison | Planned | — |
| 03 — Cross-lingual k | Planned | — |
| 04 — E6 mapping | Planned | — |

---

## Running Everything

```bash
# Full pipeline
python experiments/01_bpe_igbo_k27/fetch_corpus.py
python experiments/01_bpe_igbo_k27/train_bpe_sweep.py
```

**First result in ~10 minutes.**
