# -*- coding: utf-8 -*-
"""
PAGC Paper Downloader — Snowball Pipeline
==========================================
Strategy:
  1. Parse all source URLs from raw_literature/ stubs and pagc_library/ bibliographies
  2. Try to get the actual full PDF via:
     a) ArXiv direct download (free, no auth)
     b) Unpaywall API (finds open access version of any DOI)
     c) Semantic Scholar Graph API (abstract + open access PDF link)
  3. For every successfully retrieved paper, snowball:
     - Fetch its references from Semantic Scholar
     - Score each reference for PAGC relevance
     - Add high-relevance ones to the download queue
  4. Save PDFs to sources/papers/<discipline>/
  5. Update the stub .md files with processing_status: downloaded
  6. Write a download manifest: sources/download_manifest.jsonl

Run:
    cd sources/research_pipeline
    python paper_downloader.py [--max 1000] [--depth 3] [--priority-only]

Requirements:
    pip install requests tqdm PyMuPDF
"""

import os
import re
import sys
import json
import time
import hashlib
import argparse
import logging
from pathlib import Path
from urllib.parse import urlparse, quote
from collections import deque
from typing import Optional

# Force UTF-8 on Windows console so log messages with non-ASCII chars don't crash
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    import requests
    from tqdm import tqdm
except ImportError:
    print("Installing requirements...")
    os.system("pip install requests tqdm")
    import requests
    from tqdm import tqdm

# ─── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_LIT_DIR = REPO_ROOT / "sources" / "raw_literature"
PAGC_LIB_DIR = REPO_ROOT / "sources" / "pagc_library"
PAPERS_DIR = REPO_ROOT / "sources" / "papers"
MANIFEST_PATH = REPO_ROOT / "sources" / "download_manifest.jsonl"
LOG_PATH = REPO_ROOT / "sources" / "downloader.log"

SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1"
UNPAYWALL_API = "https://api.unpaywall.org/v2"
UNPAYWALL_EMAIL = "pagc-research@etisiobi.io"  # required by Unpaywall TOS
CROSSREF_API = "https://api.crossref.org/works"

ARXIV_PATTERN = re.compile(
    r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]+)',
    re.IGNORECASE
)
DOI_PATTERN = re.compile(r'doi\.org/(.+?)(?:\s|$|")', re.IGNORECASE)

# PAGC relevance keywords — papers matching these get priority
PAGC_KEYWORDS = [
    "igbo", "nwagu", "aneke", "syllabary", "generative compression",
    "minimum description length", "kolmogorov complexity", "mdl",
    "byte pair encoding", "bpe", "tokenization", "subword",
    "lie group", "e6", "exceptional", "weyl group", "albert algebra",
    "genetic code", "codon", "amino acid alphabet",
    "holographic", "ads/cft", "landauer", "thermodynamics computation",
    "chunking", "working memory", "cognitive compression",
    "decolonial", "indigenous knowledge", "african linguistics",
    "information bottleneck", "shannon entropy",
    "complex adaptive", "emergence", "scale-free"
]

# Canonical seed papers — absolute must-haves regardless of snowball
SEED_PAPERS = [
    # Information Theory Foundations
    {"title": "A Mathematical Theory of Communication", "arxiv_id": None,
     "doi": "10.1002/j.1538-7305.1948.tb01338.x", "discipline": "information_theory",
     "note": "Shannon 1948 — THE foundational paper"},
    {"title": "Shannon Information and Kolmogorov Complexity",
     "arxiv_id": "cs/0410002", "doi": None, "discipline": "information_theory"},
    {"title": "The Minimum Description Length Principle in Coding and Modeling",
     "arxiv_id": None, "doi": "10.1109/18.720554", "discipline": "information_theory"},

    # BPE / Tokenization
    {"title": "Neural Machine Translation of Rare Words with Subword Units",
     "arxiv_id": "1508.07909", "doi": None, "discipline": "tokenization",
     "note": "Sennrich et al. 2016 — the BPE paper"},
    {"title": "Tokenization Is More Than Tokenization",
     "arxiv_id": "2308.01174", "doi": None, "discipline": "tokenization"},
    {"title": "Language Model Tokenizers Introduce Unfairness Between Languages",
     "arxiv_id": "2305.15425", "doi": None, "discipline": "tokenization"},
    {"title": "Theoretical Analysis of Byte Pair Encoding",
     "arxiv_id": "2112.08874", "doi": None, "discipline": "tokenization"},

    # Igbo / African Linguistics
    {"title": "Linguistic Analysis of the Nwagu Aneke Indigenous Igbo Syllabary",
     "arxiv_id": None, "doi": None,
     "semantic_scholar_id": "93f6de15a1a9ae0868f5809be546162f2b549082",
     "discipline": "african_linguistics"},
    {"title": "AfricaNLP 2025: African Language Processing",
     "arxiv_id": None,
     "url": "https://aclanthology.org/2025.africanlp-1.pdf",
     "discipline": "african_linguistics"},

    # E6 / Lie Theory
    {"title": "The Geometry of E6", "arxiv_id": "math/0503454",
     "doi": None, "discipline": "mathematics_e6"},
    {"title": "Exceptional Lie Groups and Elementary Particles",
     "arxiv_id": "hep-th/9309030", "doi": None, "discipline": "mathematics_e6"},
    {"title": "E6 and the Bipartite Entanglement of Three Qutrits",
     "arxiv_id": "quant-ph/0701078", "doi": None, "discipline": "mathematics_e6"},

    # Genetic Code
    {"title": "The genetic code is one in a million",
     "arxiv_id": None, "doi": "10.1093/molbev/msl110",
     "discipline": "synthetic_biology", "note": "Freeland & Hurst 1998"},
    {"title": "Rules Governing the Genetic Code Degeneracy",
     "url": "https://www.frontiersin.org/articles/10.3389/fams.2024.1340640/full",
     "doi": None, "discipline": "synthetic_biology"},

    # Holographic / Cosmology
    {"title": "The Large N limit of superconformal field theories and supergravity",
     "arxiv_id": "hep-th/9711200", "doi": None, "discipline": "holographic",
     "note": "Maldacena 1997 — the AdS/CFT paper"},

    # Landauer / Thermodynamics
    {"title": "Irreversibility and heat generation in the computing process",
     "arxiv_id": None, "doi": "10.1147/rd.53.0183", "discipline": "thermodynamics",
     "note": "Landauer 1961"},
    {"title": "Landauer Principle and Thermodynamics of Computation",
     "arxiv_id": "2107.05639", "doi": None, "discipline": "thermodynamics"},

    # MDL / Complexity
    {"title": "Network Reconstruction via the Minimum Description Length Principle",
     "arxiv_id": "2407.04965", "doi": None, "discipline": "information_theory"},
    {"title": "The Information-Theoretic Imperative",
     "arxiv_id": "2510.25883", "doi": None, "discipline": "information_theory"},

    # Chunking / Cognitive
    {"title": "Action Chunking as Conditional Policy Compression",
     "url": "https://lucylai.com/pubs/lai25.pdf",
     "discipline": "cognitive_science"},
    {"title": "Synaptic Theory of Chunking in Working Memory",
     "arxiv_id": "2209.09193", "doi": None, "discipline": "cognitive_science"},
]

# ─── Logging ───────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("downloader")


# ─── Helpers ───────────────────────────────────────────────────────────────────

def safe_filename(title: str, max_len=120) -> str:
    """Convert a paper title to a safe filename."""
    safe = re.sub(r'[\\/:*?"<>|]', '_', title)
    safe = re.sub(r'\s+', '_', safe.strip())
    return safe[:max_len]


def load_manifest() -> dict:
    """Load existing manifest as a dict keyed by paper_id (url or arxiv_id)."""
    manifest = {}
    if MANIFEST_PATH.exists():
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entry = json.loads(line)
                        key = entry.get("arxiv_id") or entry.get("doi") or entry.get("url", "")
                        if key:
                            manifest[key] = entry
                    except Exception:
                        pass
    return manifest


def save_to_manifest(entry: dict):
    """Append an entry to the manifest."""
    with open(MANIFEST_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def pagc_relevance_score(title: str, abstract: str = "") -> int:
    """Score a paper for PAGC relevance (0-10)."""
    text = (title + " " + abstract).lower()
    score = sum(1 for kw in PAGC_KEYWORDS if kw in text)
    return min(score, 10)


# ─── URL Parsing ───────────────────────────────────────────────────────────────

def extract_urls_from_stubs() -> list[dict]:
    """Parse all raw_literature/ and pagc_library/ markdown files for URLs."""
    sources = []

    def parse_md_file(path: Path, discipline: str):
        text = path.read_text(encoding="utf-8", errors="ignore")

        # YAML front matter: source_url
        yaml_url = re.search(r'source_url:\s*(.+)', text)
        title_match = re.search(r'title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)

        url = yaml_url.group(1).strip() if yaml_url else ""
        title = title_match.group(1).strip() if title_match else path.stem

        # Also find inline markdown links
        inline_urls = re.findall(r'\(https?://[^\)]+\)', text)
        if not url and inline_urls:
            url = inline_urls[0][1:-1]

        if url:
            # Detect arxiv IDs
            arxiv_match = ARXIV_PATTERN.search(url)
            arxiv_id = arxiv_match.group(1) if arxiv_match else None

            sources.append({
                "title": title,
                "url": url,
                "arxiv_id": arxiv_id,
                "discipline": discipline,
                "source_file": str(path)
            })

    # raw_literature — treat all as general
    for f in RAW_LIT_DIR.glob("*.md"):
        parse_md_file(f, "general")

    # pagc_library — discipline from filename
    for f in PAGC_LIB_DIR.glob("*.md"):
        discipline = f.stem.split("_(")[0].replace("_", " ").strip()
        # Extract all DOI and URL mentions from the file
        text = f.read_text(encoding="utf-8", errors="ignore")
        entries = re.findall(r'## \[\d+\] (.+?)\\n.*?URL:\*\* (https?://[^\\]+)', text)
        for title, url in entries:
            arxiv_match = ARXIV_PATTERN.search(url)
            sources.append({
                "title": title.strip(),
                "url": url.strip(),
                "arxiv_id": arxiv_match.group(1) if arxiv_match else None,
                "discipline": discipline,
            })

    # Deduplicate by URL
    seen = set()
    unique = []
    for s in sources:
        key = s.get("arxiv_id") or s.get("url", "")
        if key and key not in seen:
            seen.add(key)
            unique.append(s)

    log.info(f"Parsed {len(unique)} unique source URLs from repo stubs")
    return unique


# ─── Downloaders ───────────────────────────────────────────────────────────────

def download_arxiv(arxiv_id: str, dest_path: Path) -> bool:
    """Download PDF from ArXiv. arxiv_id can be '2407.04965' or 'cs/0410002'."""
    clean_id = arxiv_id.strip().replace("http://arxiv.org/abs/", "").replace("https://arxiv.org/abs/", "")
    url = f"https://arxiv.org/pdf/{clean_id}"
    try:
        resp = requests.get(url, timeout=30, headers={"User-Agent": "PAGC-Downloader/1.0"})
        if resp.status_code == 200 and b"%PDF" in resp.content[:10]:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_bytes(resp.content)
            log.info(f"  [OK-ARXIV] {arxiv_id} -> {dest_path.name}")
            return True
        else:
            log.debug(f"  ArXiv {arxiv_id}: HTTP {resp.status_code}")
            return False
    except Exception as e:
        log.debug(f"  ArXiv {arxiv_id} error: {e}")
        return False


def get_unpaywall_pdf(doi: str) -> Optional[str]:
    """Query Unpaywall for open-access PDF URL given a DOI."""
    if not doi:
        return None
    clean_doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    url = f"{UNPAYWALL_API}/{clean_doi}?email={UNPAYWALL_EMAIL}"
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            best = data.get("best_oa_location") or {}
            pdf_url = best.get("url_for_pdf") or best.get("url")
            return pdf_url
    except Exception:
        pass
    return None


def download_url(url: str, dest_path: Path, label: str = "") -> bool:
    """Generic URL downloader for direct PDF links."""
    try:
        resp = requests.get(
            url, timeout=30,
            headers={"User-Agent": "PAGC-Downloader/1.0 (research use)"},
            allow_redirects=True
        )
        content_type = resp.headers.get("content-type", "")
        if resp.status_code == 200 and (
            b"%PDF" in resp.content[:10] or "pdf" in content_type.lower()
        ):
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_bytes(resp.content)
            log.info(f"  [OK-DIRECT] {label or url[:60]} -> {dest_path.name}")
            return True
        else:
            log.debug(f"  Direct {url[:60]}: HTTP {resp.status_code} type={content_type[:40]}")
            return False
    except Exception as e:
        log.debug(f"  Direct download error {url[:60]}: {e}")
        return False


def semantic_scholar_lookup(title: str = None, arxiv_id: str = None,
                             ss_id: str = None) -> Optional[dict]:
    """Look up a paper on Semantic Scholar, return metadata + PDF link + references."""
    params = {"fields": "title,abstract,year,authors,references,openAccessPdf,externalIds,citationCount"}

    if ss_id:
        url = f"{SEMANTIC_SCHOLAR_API}/paper/{ss_id}"
    elif arxiv_id:
        clean = arxiv_id.replace("http://arxiv.org/abs/", "").replace("https://arxiv.org/abs/", "")
        url = f"{SEMANTIC_SCHOLAR_API}/paper/arXiv:{clean}"
    elif title:
        url = f"{SEMANTIC_SCHOLAR_API}/paper/search"
        params["query"] = title
        params["limit"] = 1
    else:
        return None

    try:
        resp = requests.get(url, params=params, timeout=20,
                            headers={"User-Agent": "PAGC-Downloader/1.0"})
        if resp.status_code == 200:
            data = resp.json()
            # Search endpoint returns {"data": [...]}
            if "data" in data:
                items = data["data"]
                return items[0] if items else None
            return data
        else:
            log.debug(f"  S2 {url}: {resp.status_code}")
    except Exception as e:
        log.debug(f"  S2 error: {e}")

    return None


# ─── Snowball Reference Scorer ─────────────────────────────────────────────────

def score_and_queue_references(paper_data: dict, queue: deque, seen_ids: set,
                                min_score: int = 2, min_citations: int = 5):
    """
    Given a Semantic Scholar paper object, score its references and
    add high-scoring ones to the download queue.
    """
    refs = paper_data.get("references", []) or []
    added = 0
    for ref in refs:
        ref_id = ref.get("paperId", "")
        if not ref_id or ref_id in seen_ids:
            continue

        title = ref.get("title", "") or ""
        abstract = ref.get("abstract", "") or ""
        citations = ref.get("citationCount", 0) or 0
        year = ref.get("year", 0) or 0

        score = pagc_relevance_score(title, abstract)

        # Filters: must be relevant AND somewhat cited (or very recent)
        if score >= min_score and (citations >= min_citations or year >= 2022):
            seen_ids.add(ref_id)
            queue.append({
                "title": title,
                "semantic_scholar_id": ref_id,
                "discipline": "snowball",
                "relevance_score": score,
                "citations": citations,
                "year": year,
            })
            added += 1

    log.info(f"  Queued {added} new references from snowball (of {len(refs)} total refs)")
    return added


# ─── Core Download Loop ────────────────────────────────────────────────────────

def download_paper(paper: dict, manifest: dict, discipline_override: str = None) -> dict:
    """
    Try every available method to get a PDF for the paper.
    Returns a result dict with status, path, etc.
    """
    title = paper.get("title", "Unknown")
    arxiv_id = paper.get("arxiv_id")
    doi = paper.get("doi")
    url = paper.get("url", "")
    ss_id = paper.get("semantic_scholar_id")
    discipline = discipline_override or paper.get("discipline", "general")

    # Normalise discipline to a safe directory name
    disc_dir = PAPERS_DIR / re.sub(r'[^\w]', '_', discipline.lower())[:40]
    filename = safe_filename(title) + ".pdf"
    dest = disc_dir / filename

    result = {
        "title": title,
        "discipline": discipline,
        "arxiv_id": arxiv_id,
        "doi": doi,
        "url": url,
        "status": "failed",
        "pdf_path": None,
        "relevance_score": paper.get("relevance_score", pagc_relevance_score(title)),
    }

    # Skip if already downloaded
    if dest.exists() and dest.stat().st_size > 5000:
        result["status"] = "already_exists"
        result["pdf_path"] = str(dest)
        return result

    # Method 1: ArXiv direct
    if arxiv_id:
        if download_arxiv(arxiv_id, dest):
            result["status"] = "downloaded_arxiv"
            result["pdf_path"] = str(dest)
            return result
        time.sleep(0.5)

    # Method 2: Semantic Scholar lookup → open access PDF
    ss_data = None
    if not ss_id:
        ss_data = semantic_scholar_lookup(title=title, arxiv_id=arxiv_id)
        if ss_data:
            ss_id = ss_data.get("paperId")
    elif ss_id:
        ss_data = semantic_scholar_lookup(ss_id=ss_id)

    if ss_data:
        oa = ss_data.get("openAccessPdf") or {}
        pdf_url = oa.get("url")
        if pdf_url:
            if download_url(pdf_url, dest, label=f"S2-OA: {title[:50]}"):
                result["status"] = "downloaded_s2"
                result["pdf_path"] = str(dest)
                result["semantic_scholar_id"] = ss_id
                return result
        time.sleep(1)

    # Method 3: Unpaywall (DOI required)
    if doi:
        pdf_url = get_unpaywall_pdf(doi)
        if pdf_url:
            if download_url(pdf_url, dest, label=f"Unpaywall: {title[:50]}"):
                result["status"] = "downloaded_unpaywall"
                result["pdf_path"] = str(dest)
                return result
        time.sleep(1)

    # Method 4: Direct URL (if it looks like a PDF endpoint)
    if url and (url.endswith(".pdf") or "pdf" in url.lower()):
        if download_url(url, dest, label=f"Direct: {title[:50]}"):
            result["status"] = "downloaded_direct"
            result["pdf_path"] = str(dest)
            return result

    log.info(f"  [FAIL] Could not download: {title[:70]}")
    result["status"] = "failed"
    return result


# ─── Main Pipeline ─────────────────────────────────────────────────────────────

def run(max_papers: int = 1000, snowball_depth: int = 3, priority_only: bool = False):
    log.info("=" * 60)
    log.info("PAGC Paper Downloader — Starting")
    log.info(f"Target: {max_papers} papers | Snowball depth: {snowball_depth}")
    log.info("=" * 60)

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()

    # Build initial queue from seeds + repo stubs
    queue = deque()
    seen_ids = set(manifest.keys())

    # Priority seeds always go first
    for seed in SEED_PAPERS:
        key = seed.get("arxiv_id") or seed.get("doi") or seed.get("url", "")
        if key and key not in seen_ids:
            seen_ids.add(key)
            queue.append(seed)

    if not priority_only:
        # Add everything from repo stubs
        repo_sources = extract_urls_from_stubs()
        for src in repo_sources:
            key = src.get("arxiv_id") or src.get("url", "")
            if key and key not in seen_ids:
                seen_ids.add(key)
                queue.append(src)

    log.info(f"Initial queue size: {len(queue)} papers")

    downloaded = 0
    failed = 0
    snowball_passes = {0: len(queue)}
    current_depth = 0
    depth_counter = snowball_passes[0]

    with tqdm(total=max_papers, desc="Downloading papers", unit="paper") as pbar:
        while queue and downloaded < max_papers:
            paper = queue.popleft()
            depth_counter -= 1

            result = download_paper(paper, manifest)
            key = result.get("arxiv_id") or result.get("doi") or result.get("url", "")

            if result["status"].startswith("downloaded") or result["status"] == "already_exists":
                save_to_manifest(result)
                downloaded += 1
                pbar.update(1)
                pbar.set_postfix({"downloaded": downloaded, "queued": len(queue), "depth": current_depth})

                # Snowball: fetch references from this paper if within depth limit
                if (result["status"].startswith("downloaded") and
                    current_depth < snowball_depth):
                    # Look up Semantic Scholar for full reference list
                    ss_id = paper.get("semantic_scholar_id")
                    arxiv_id = paper.get("arxiv_id")
                    if not ss_id:
                        ss_data = semantic_scholar_lookup(
                            title=paper.get("title"),
                            arxiv_id=arxiv_id
                        )
                    else:
                        ss_data = semantic_scholar_lookup(ss_id=ss_id)

                    if ss_data:
                        added = score_and_queue_references(ss_data, queue, seen_ids)
                        if added:
                            snowball_passes[current_depth + 1] = \
                                snowball_passes.get(current_depth + 1, 0) + added

                    time.sleep(1.5)  # Respectful rate limit for S2
            else:
                failed += 1
                save_to_manifest(result)

            # Track snowball depth
            if depth_counter <= 0 and current_depth < snowball_depth:
                current_depth += 1
                depth_counter = snowball_passes.get(current_depth, 0)
                if current_depth > 0:
                    log.info(f"\n[SNOWBALL] Entering depth {current_depth} ({depth_counter} papers)")

            time.sleep(0.3)  # Base rate limit

    log.info("\n" + "=" * 60)
    log.info(f"DONE. Downloaded: {downloaded} | Failed: {failed} | Total queued: {len(queue)} remaining")
    log.info(f"Snowball depth breakdown: {snowball_passes}")
    log.info(f"PDFs saved to: {PAPERS_DIR}")
    log.info(f"Manifest: {MANIFEST_PATH}")
    log.info("=" * 60)

    # Print summary by discipline
    print("\n=== Download Summary by Discipline ===")
    if PAPERS_DIR.exists():
        for disc_dir in sorted(PAPERS_DIR.iterdir()):
            if disc_dir.is_dir():
                count = len(list(disc_dir.glob("*.pdf")))
                print(f"  {disc_dir.name}: {count} PDFs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PAGC Paper Downloader (Snowball)")
    parser.add_argument("--max", type=int, default=500,
                        help="Max papers to download (default: 500)")
    parser.add_argument("--depth", type=int, default=2,
                        help="Snowball reference depth (default: 2)")
    parser.add_argument("--priority-only", action="store_true",
                        help="Only download the seed canonical papers")
    args = parser.parse_args()

    run(max_papers=args.max, snowball_depth=args.depth, priority_only=args.priority_only)
