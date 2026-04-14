"""
train_bpe_sweep.py — The Core PAGC Experiment
==============================================

HYPOTHESIS: k=27 is the natural optimal vocabulary size for Igbo text.
If PAGC is valid, a BPE sweep from k=15 to k=50 should show a natural
inflection point (knee of the curve) at or near k=27.

WHAT WE MEASURE per vocabulary size k:
  1. Fertility rate    — avg tokens per word (lower = more efficient)
  2. Coverage          — % of test words fully reproduced (higher = better)
  3. Compression ratio — original chars / tokenized chars
  4. Type-token ratio  — vocabulary richness vs redundancy

FALSIFICATION CONDITION:
  If the fertility curve is monotonically decreasing with no inflection near
  k=27, or the inflection appears at a different k (e.g. 22 or 35), the
  specific PAGC k=27 claim is refuted. The broader compression argument
  (that Igbo has a natural optimal vocabulary) may still hold.

Requirements:
    pip install tokenizers matplotlib numpy scipy

Run:
    python experiments/01_bpe_igbo_k27/train_bpe_sweep.py
    
Output:
    experiments/01_bpe_igbo_k27/results/
      bpe_sweep_metrics.json    — all metrics
      bpe_sweep_fertility.png   — fertility curve with annotations
      bpe_sweep_compression.png — compression ratio curve
      bpe_sweep_combined.png    — 2x2 panel (Karpathy-style)
      report.md                 — auto-generated results summary
"""

import json
import sys
import os
import time
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────
REPO_ROOT    = Path(__file__).resolve().parents[2]
DATA_DIR     = REPO_ROOT / "data" / "igbo_corpus"
RESULTS_DIR  = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ── Install dependencies ────────────────────────────────────────
def ensure_deps():
    deps = ["tokenizers", "matplotlib", "numpy", "scipy"]
    for dep in deps:
        try:
            __import__(dep)
        except ImportError:
            print(f"Installing {dep}...")
            os.system(f"{sys.executable} -m pip install {dep} -q")

ensure_deps()

import numpy as np
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# ── Sweep config ───────────────────────────────────────────────
# k = vocabulary size to test
# Range: 15–50, centered on k=27 with fine resolution around it
K_VALUES = list(range(15, 51))   # 15, 16, 17, ... 50

# Minimum corpus requirement
MIN_SENTENCES = 50


def load_corpus() -> tuple[list[str], list[str]]:
    """Load train and test split."""
    train_path = DATA_DIR / "train.txt"
    test_path  = DATA_DIR / "test.txt"

    if not train_path.exists():
        raise FileNotFoundError(
            f"Corpus not found at {DATA_DIR}\n"
            f"Run: python experiments/01_bpe_igbo_k27/fetch_corpus.py first"
        )

    train = [l.strip() for l in train_path.read_text("utf-8").splitlines() if l.strip()]
    test  = [l.strip() for l in test_path.read_text("utf-8").splitlines() if l.strip()]

    print(f"Corpus loaded: {len(train):,} train / {len(test):,} test sentences")
    if len(train) < MIN_SENTENCES:
        print(f"[WARN] Very small corpus ({len(train)} sentences). Results may not be reliable.")
        print("       Add more Igbo text to data/igbo_corpus/train.txt for robust results.")

    return train, test


def train_bpe(k: int, train_sentences: list[str]) -> Tokenizer:
    """Train a BPE tokenizer with vocabulary size k."""
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Whitespace()
    trainer = BpeTrainer(
        vocab_size=k,
        special_tokens=["[UNK]", "[PAD]"],
        min_frequency=1,
        show_progress=False,
    )
    tokenizer.train_from_iterator(train_sentences, trainer)
    return tokenizer


def compute_metrics(tokenizer: Tokenizer, test_sentences: list[str], k: int) -> dict:
    """Compute all metrics for a tokenizer on test sentences."""
    total_tokens  = 0
    total_words   = 0
    total_chars   = 0
    covered_words = 0
    token_lengths = []

    for sentence in test_sentences:
        words = sentence.split()
        if not words:
            continue
        total_words += len(words)
        total_chars += len(sentence.replace(" ", ""))

        encoding = tokenizer.encode(sentence)
        tokens   = encoding.tokens
        total_tokens += len(tokens)

        # Coverage: word is "covered" if it doesn't produce [UNK]
        for word in words:
            enc_word = tokenizer.encode(word)
            if "[UNK]" not in enc_word.tokens:
                covered_words += 1

        token_lengths.extend([len(t) for t in tokens if t not in ("[UNK]", "[PAD]")])

    fertility      = total_tokens / max(total_words, 1)
    coverage       = covered_words / max(total_words, 1)
    # Compression: original char count / tokenized token count (chars represented per token)
    chars_per_tok  = total_chars / max(total_tokens, 1)
    # Average token length
    avg_tok_len    = np.mean(token_lengths) if token_lengths else 0

    return {
        "k":              k,
        "fertility":      round(fertility, 4),
        "coverage":       round(coverage, 4),
        "chars_per_tok":  round(chars_per_tok, 4),
        "avg_tok_len":    round(float(avg_tok_len), 4),
        "total_tokens":   total_tokens,
        "total_words":    total_words,
        "total_chars":    total_chars,
    }


def find_inflection(ks: list[int], values: list[float]) -> int:
    """Find the knee of the curve using second derivative method."""
    from scipy.signal import savgol_filter
    if len(values) < 5:
        return ks[np.argmin(np.gradient(np.gradient(values)))]
    
    smoothed = savgol_filter(values, window_length=min(7, len(values)//2*2+1), polyorder=2)
    d2 = np.gradient(np.gradient(smoothed))
    # Knee = where second derivative is maximally negative (rate of decrease slows)
    knee_idx = np.argmax(np.abs(d2))
    return ks[int(knee_idx)]


def run_sweep() -> list[dict]:
    """Run the full BPE sweep."""
    print("\n" + "=" * 60)
    print("BPE Sweep: Testing vocabulary sizes k=15..50 on Igbo")
    print("HYPOTHESIS: k=27 is the natural optimal point")
    print("=" * 60 + "\n")

    train, test = load_corpus()
    results = []

    for k in K_VALUES:
        t0 = time.time()
        tokenizer = train_bpe(k, train)
        metrics   = compute_metrics(tokenizer, test, k)
        elapsed   = time.time() - t0

        marker = " <-- PAGC prediction" if k == 27 else ""
        print(
            f"  k={k:3d} | fertility={metrics['fertility']:.3f} | "
            f"coverage={metrics['coverage']:.3f} | "
            f"chars/tok={metrics['chars_per_tok']:.2f} | "
            f"{elapsed:.1f}s{marker}"
        )
        results.append(metrics)

    return results


def save_results(results: list[dict]):
    """Save raw metrics JSON."""
    out = RESULTS_DIR / "bpe_sweep_metrics.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n[*] Metrics saved: {out}")
    return out


def plot_results(results: list[dict]):
    """Generate publication-quality 2x2 figure."""
    import matplotlib
    matplotlib.use("Agg")  # headless
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from scipy.signal import savgol_filter

    ks         = [r["k"]             for r in results]
    fertility  = [r["fertility"]      for r in results]
    coverage   = [r["coverage"]       for r in results]
    chars_tok  = [r["chars_per_tok"]  for r in results]
    avg_len    = [r["avg_tok_len"]    for r in results]

    # Find actual inflection in fertility
    try:
        infl_k = find_inflection(ks, fertility)
    except Exception:
        infl_k = None

    # ── Style ──────────────────────────────────────────────
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "figure.facecolor": "#fafafa",
    })

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "BPE Vocabulary Sweep on Igbo Corpus\nPAGC Hypothesis: k=27 is the Natural Optimal Vocabulary Size",
        fontsize=14, fontweight="bold", y=0.98
    )

    PAGC_COLOR  = "#e05a2b"   # warm orange for k=27 marker
    INFL_COLOR  = "#2b8ae0"   # blue for detected inflection
    LINE_COLOR  = "#333"

    def add_k27_line(ax):
        ax.axvline(27, color=PAGC_COLOR, linestyle="--", alpha=0.7, lw=1.5, label="k=27 (PAGC)")
        ax.text(27.3, ax.get_ylim()[1] * 0.97, "PAGC\nprediction",
                color=PAGC_COLOR, fontsize=8, va="top")

    def add_infl_line(ax, k):
        if k and k != 27:
            ax.axvline(k, color=INFL_COLOR, linestyle=":", alpha=0.7, lw=1.5, label=f"Detected knee (k={k})")

    # ── Plot 1: Fertility (main result) ────────────────────
    ax = axes[0, 0]
    ax.plot(ks, fertility, "o-", color=LINE_COLOR, ms=4, lw=2)
    # Smooth trendline
    if len(fertility) >= 5:
        smooth = savgol_filter(fertility, 5, 2)
        ax.plot(ks, smooth, "--", color="gray", lw=1, alpha=0.5, label="Smoothed")
    add_k27_line(ax)
    if infl_k:
        add_infl_line(ax, infl_k)
    ax.set_xlabel("Vocabulary size k")
    ax.set_ylabel("Fertility (tokens per word)")
    ax.set_title("Fertility Rate\n(lower = more efficient)")
    ax.legend(fontsize=8)
    # Annotate the k=27 value
    idx27 = ks.index(27) if 27 in ks else None
    if idx27 is not None:
        ax.annotate(
            f"k=27: {fertility[idx27]:.3f}",
            xy=(27, fertility[idx27]),
            xytext=(29, fertility[idx27] + 0.05),
            arrowprops=dict(arrowstyle="->", color=PAGC_COLOR),
            color=PAGC_COLOR, fontsize=9
        )

    # ── Plot 2: Coverage ────────────────────────────────────
    ax = axes[0, 1]
    ax.plot(ks, [c * 100 for c in coverage], "s-", color="#2b8ae0", ms=4, lw=2)
    add_k27_line(ax)
    ax.set_xlabel("Vocabulary size k")
    ax.set_ylabel("Coverage (%)")
    ax.set_title("Word Coverage\n(higher = better)")

    # ── Plot 3: Chars per token (compression proxy) ─────────
    ax = axes[1, 0]
    ax.plot(ks, chars_tok, "^-", color="#6a2be0", ms=4, lw=2)
    add_k27_line(ax)
    ax.set_xlabel("Vocabulary size k")
    ax.set_ylabel("Chars per token")
    ax.set_title("Compression Efficiency\n(chars represented per token)")

    # ── Plot 4: Marginal gain (delta fertility) ─────────────
    ax = axes[1, 1]
    delta = [abs(fertility[i] - fertility[i-1]) for i in range(1, len(fertility))]
    ax.bar(ks[1:], delta, color=[
        PAGC_COLOR if k == 27 else "#aaa" for k in ks[1:]
    ], alpha=0.8)
    ax.set_xlabel("Vocabulary size k")
    ax.set_ylabel("|ΔFertility|")
    ax.set_title("Marginal Fertility Gain per k\n(diminishing returns = inflection)")
    ax.axvline(27, color=PAGC_COLOR, linestyle="--", alpha=0.7, lw=1.5, label="k=27")
    ax.legend(fontsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out = RESULTS_DIR / "bpe_sweep_combined.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[*] Figure saved: {out}")
    return out


def generate_report(results: list[dict], infl_k: int) -> str:
    """Auto-generate a Markdown results report."""
    ks        = [r["k"]        for r in results]
    fertility = [r["fertility"] for r in results]
    coverage  = [r["coverage"]  for r in results]

    idx27 = ks.index(27) if 27 in ks else None

    verdict = "INCONCLUSIVE"
    if idx27 is not None:
        f27 = fertility[idx27]
        if infl_k:
            if abs(infl_k - 27) <= 2:
                verdict = "SUPPORTS PAGC"
            elif abs(infl_k - 27) <= 5:
                verdict = "WEAK SUPPORT"
            else:
                verdict = f"REFUTED (inflection at k={infl_k}, not k=27)"

    f27_val  = fertility[idx27] if idx27 is not None else "N/A"
    c27_val  = coverage[idx27]  if idx27 is not None else "N/A"
    best_k   = ks[int(np.argmin(fertility))]

    report = f"""# BPE Sweep Results — PAGC k=27 Hypothesis

**Date:** {time.strftime("%Y-%m-%d %H:%M")}
**Corpus:** Igbo text ({results[0]['total_words']:,} test words)
**Sweep range:** k=15 to k=50
**Method:** BPE (Byte Pair Encoding) via HuggingFace `tokenizers`

## Verdict: {verdict}

| Metric                  | Value |
|-------------------------|-------|
| Detected inflection k   | {infl_k} |
| k=27 fertility          | {f27_val} |
| k=27 coverage           | {c27_val} |
| Best k by fertility     | {best_k} |

## Hypothesis
PAGC claims that 27 base symbols is the natural optimal vocabulary for Igbo.
If valid: the fertility curve (tokens per word) should show a **knee at k≈27**,
where diminishing returns set in — more vocabulary above 27 yields minimal gain.

## Falsification Condition
If the knee appears at k != 27 (±2), the specific PAGC k=27 claim is **refuted**
for this corpus. The broader compression argument may still hold at whatever k
the knee appears.

## Full Metrics Table

| k | Fertility | Coverage | Chars/Tok |
|---|-----------|----------|-----------|
"""
    for r in results:
        marker = " **<-- PAGC**" if r["k"] == 27 else ""
        infl_marker = " *(inflection)*" if r["k"] == infl_k else ""
        report += f"| {r['k']} | {r['fertility']} | {r['coverage']:.3f} | {r['chars_per_tok']:.2f} |{marker}{infl_marker}\n"

    report += """
## What Next
1. If SUPPORTS: run at scale with CC-100 Igbo corpus (~15MB)
2. If REFUTED: investigate whether the detected inflection k is meaningful
   for other tone languages (Yoruba, Ewe) — is it language-specific?
3. Compare k-optimal for English, Swahili, Yoruba, Hausa on same corpus size
4. Run MDL comparison: is PAGC 27×8=216 matrix competitive with k-optimal BPE?
"""

    out = RESULTS_DIR / "report.md"
    out.write_text(report, encoding="utf-8")
    print(f"[*] Report saved: {out}")
    return report


def main():
    results = run_sweep()
    save_results(results)

    ks        = [r["k"]        for r in results]
    fertility = [r["fertility"] for r in results]

    try:
        infl_k = find_inflection(ks, fertility)
        print(f"\n[*] Detected fertility inflection at k={infl_k}")
        if abs(infl_k - 27) <= 2:
            print(f"    --> SUPPORTS PAGC (k=27 ± 2)")
        elif abs(infl_k - 27) <= 5:
            print(f"    --> WEAK SUPPORT for PAGC")
        else:
            print(f"    --> DOES NOT SUPPORT specific k=27 claim (inflection at k={infl_k})")
    except Exception as e:
        infl_k = None
        print(f"[WARN] Could not compute inflection: {e}")

    plot_results(results)
    report = generate_report(results, infl_k)

    print("\n" + "=" * 60)
    print("EXPERIMENT COMPLETE")
    print(f"Results in: {RESULTS_DIR}")
    print("=" * 60)
    print("\nSummary:")
    # Safe printing for Windows console
    safe_report = report[:800].encode('ascii', 'replace').decode('ascii')
    print(safe_report)


if __name__ == "__main__":
    main()
