"""
fetch_igbo_corpus.py — Download real Igbo text corpus from open sources
=======================================================================
Sources (all open access):
  1. OPUS JW300  — Jehovah's Witnesses multilingual corpus, has Igbo (igb)
  2. FLORES-200  — Meta's benchmark, includes Igbo dev/devtest splits
  3. Leipzig Corpora — igb_wikipedia_2016 sentence corpus
  4. Masakhane MT — African NLP community Igbo data
  5. Common Crawl (CC-100) — Igbo extracted web text
  6. Nollywood subtitles via OPUS OpenSubtitles (if available)

Output:
  data/igbo_corpus/raw/  — raw downloaded files
  data/igbo_corpus/merged.txt — deduped, cleaned, one sentence per line
  data/igbo_corpus/train.txt  (90%)
  data/igbo_corpus/val.txt    (5%)
  data/igbo_corpus/test.txt   (5%)

Run:
    python experiments/01_bpe_igbo_k27/fetch_corpus.py
"""

import os
import re
import sys
import gzip
import json
import hashlib
import urllib.request
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR  = REPO_ROOT / "data" / "igbo_corpus"
RAW_DIR   = DATA_DIR / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# ── Corpus sources ─────────────────────────────────────────────
# (url, local_filename, parser_fn_name)
SOURCES = [

    # 1) FLORES-200 Igbo dev + devtest (Meta, 1012 sentences, gold standard)
    {
        "name": "FLORES-200 Igbo dev",
        "url": "https://raw.githubusercontent.com/facebookresearch/flores/main/flores200_dataset/dev/ibo_Latn.dev",
        "local": "flores200_igbo_dev.txt",
        "format": "lines",
    },
    {
        "name": "FLORES-200 Igbo devtest",
        "url": "https://raw.githubusercontent.com/facebookresearch/flores/main/flores200_dataset/devtest/ibo_Latn.devtest",
        "local": "flores200_igbo_devtest.txt",
        "format": "lines",
    },

    # 2) Masakhane MT en-ig training corpus (parallel, take target side)
    {
        "name": "Masakhane en-ig (target)",
        "url": "https://raw.githubusercontent.com/masakhane-io/masakhane-mt/master/benchmarks/train-lang-pairs/en-ig/train.ig",
        "local": "masakhane_ig_train.txt",
        "format": "lines",
    },
    {
        "name": "Masakhane en-ig dev (target)",
        "url": "https://raw.githubusercontent.com/masakhane-io/masakhane-mt/master/benchmarks/train-lang-pairs/en-ig/dev.ig",
        "local": "masakhane_ig_dev.txt",
        "format": "lines",
    },
    {
        "name": "Masakhane en-ig test (target)",
        "url": "https://raw.githubusercontent.com/masakhane-io/masakhane-mt/master/benchmarks/train-lang-pairs/en-ig/test.ig",
        "local": "masakhane_ig_test.txt",
        "format": "lines",
    },

    # 3) IgboNLP Bible corpus (public domain)
    {
        "name": "IgboNLP Bible",
        "url": "https://raw.githubusercontent.com/IgnatiusEzeani/IGBONLP/master/ig_en_mt/ig_en_bible/igbo_bible.txt",
        "local": "igbonlp_bible.txt",
        "format": "lines",
    },

    # 4) AfricaNLP workshop data (Hausa/Igbo news)
    {
        "name": "NaijaSenti Igbo",
        "url": "https://raw.githubusercontent.com/hausanlp/NaijaSenti/main/data/igbo/train.csv",
        "local": "naijasenti_igbo_train.csv",
        "format": "csv_text_col",
        "text_col": "tweet",
    },

    # 5) Igbo Wikipedia dump index (we extract article titles + snippets)
    {
        "name": "Igbo Wikipedia article list",
        "url": "https://dumps.wikimedia.org/igwiki/latest/igwiki-latest-all-titles-in-ns0.gz",
        "local": "igwiki_titles.gz",
        "format": "wiki_titles_gz",
    },
]

MANUAL_SOURCES = """
## Additional sources to add manually if automated fetch fails:

1. JW300 Igbo (OPUS) — https://opus.nlpl.eu/JW300/igbo.html
   Download: JW300.igb.gz → extract → data/igbo_corpus/raw/jw300_igbo.txt

2. CC-100 Igbo (Common Crawl) — https://data.statmt.org/cc-100/
   File: ig.txt.xz (~15MB) → data/igbo_corpus/raw/cc100_igbo.txt

3. Leipzig Igbo newscrawl 2016 — https://downloads.wortschatz-leipzig.de/corpora/
   File: igb_newscrawl_2016_1M-sentences.txt.gz

4. MAFAND-MT Igbo — https://github.com/masakhane-io/mafand
"""


def download_file(url: str, dest: Path, name: str) -> bool:
    """Download a file with progress reporting."""
    if dest.exists() and dest.stat().st_size > 100:
        print(f"  [SKIP] {name} — already downloaded ({dest.stat().st_size:,} bytes)")
        return True
    try:
        print(f"  [GET]  {name}")
        print(f"         {url}")
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "PAGC-Corpus-Builder/1.0 (research)"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
        dest.write_bytes(content)
        print(f"         -> {dest.name} ({len(content):,} bytes)")
        return True
    except Exception as e:
        print(f"  [FAIL] {name}: {e}")
        return False


def parse_lines(path: Path) -> list[str]:
    """Read file as plain lines."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
        return [l.strip() for l in text.splitlines() if l.strip()]
    except Exception:
        return []


def parse_csv_text_col(path: Path, text_col: str) -> list[str]:
    """Extract text column from CSV."""
    lines = []
    try:
        import csv
        with open(path, encoding="utf-8", errors="ignore", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                val = row.get(text_col, "").strip()
                if val:
                    lines.append(val)
    except Exception as e:
        print(f"  [WARN] CSV parse error: {e}")
    return lines


def parse_wiki_titles_gz(path: Path) -> list[str]:
    """Extract Wikipedia article titles from gzipped list."""
    titles = []
    try:
        with gzip.open(path, "rt", encoding="utf-8", errors="ignore") as f:
            for line in f:
                t = line.strip().replace("_", " ")
                if t and len(t) > 2:
                    titles.append(t)
    except Exception as e:
        print(f"  [WARN] Wiki gz parse error: {e}")
    return titles


def clean_line(line: str) -> str:
    """Basic cleaning for Igbo text."""
    # Remove URLs
    line = re.sub(r'https?://\S+', '', line)
    # Remove HTML entities
    line = re.sub(r'&\w+;', '', line)
    # Normalize whitespace
    line = re.sub(r'\s+', ' ', line).strip()
    # Must have at least 3 alphabetic chars (filters junk)
    if len(re.findall(r'[a-zA-ZÀ-ÿịọụẹọ]', line)) < 3:
        return ""
    return line


def deduplicate(lines: list[str]) -> list[str]:
    """Remove duplicate lines."""
    seen = set()
    unique = []
    for line in lines:
        h = hashlib.md5(line.encode()).hexdigest()
        if h not in seen:
            seen.add(h)
            unique.append(line)
    return unique


def split_corpus(lines: list[str], train=0.90, val=0.05):
    """Split into train/val/test."""
    import random
    random.seed(42)
    random.shuffle(lines)
    n = len(lines)
    t = int(n * train)
    v = int(n * val)
    return lines[:t], lines[t:t+v], lines[t+v:]


def main():
    print("=" * 60)
    print("PAGC Igbo Corpus Fetcher")
    print("=" * 60)

    all_sentences = []

    for src in SOURCES:
        dest = RAW_DIR / src["local"]
        ok = download_file(src["url"], dest, src["name"])
        if not ok or not dest.exists():
            continue

        fmt = src["format"]
        if fmt == "lines":
            sents = parse_lines(dest)
        elif fmt == "csv_text_col":
            sents = parse_csv_text_col(dest, src.get("text_col", "text"))
        elif fmt == "wiki_titles_gz":
            sents = parse_wiki_titles_gz(dest)
        else:
            sents = parse_lines(dest)

        # Clean
        sents = [clean_line(s) for s in sents]
        sents = [s for s in sents if s]
        print(f"  -> {len(sents):,} clean sentences from {src['name']}")
        all_sentences.extend(sents)

    # Dedup
    all_sentences = deduplicate(all_sentences)
    print(f"\n[*] Total unique sentences after dedup: {len(all_sentences):,}")

    if len(all_sentences) < 100:
        print("\n[WARN] Very few sentences retrieved from automated sources.")
        print("       Please add manual sources (see instructions below):\n")
        print(MANUAL_SOURCES)
    
    # Save merged
    merged_path = DATA_DIR / "merged.txt"
    merged_path.write_text("\n".join(all_sentences), encoding="utf-8")
    print(f"[*] Merged corpus saved: {merged_path} ({merged_path.stat().st_size:,} bytes)")

    # Split
    train, val, test = split_corpus(all_sentences)
    (DATA_DIR / "train.txt").write_text("\n".join(train), encoding="utf-8")
    (DATA_DIR / "val.txt").write_text("\n".join(val), encoding="utf-8")
    (DATA_DIR / "test.txt").write_text("\n".join(test), encoding="utf-8")

    print(f"[*] Split: train={len(train):,}  val={len(val):,}  test={len(test):,}")
    print(f"\n[DONE] Corpus in: {DATA_DIR}")
    print("\nNext step: python experiments/01_bpe_igbo_k27/train_bpe_sweep.py")


if __name__ == "__main__":
    main()
