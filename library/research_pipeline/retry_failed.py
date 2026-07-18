# -*- coding: utf-8 -*-
"""
Retry downloader for 'failed' manifest entries.
Uses Unpaywall + Semantic Scholar + direct DOI resolution.
"""

import json, re, sys, time, logging
from pathlib import Path
import requests

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[2]
PAPERS_DIR = REPO_ROOT / "sources" / "papers"
MANIFEST_PATH = REPO_ROOT / "sources" / "download_manifest.jsonl"
LOG_PATH = REPO_ROOT / "sources" / "retry_failed.log"

UNPAYWALL_EMAIL = "pagc-research@etisiobi.io"
UNPAYWALL_API = "https://api.unpaywall.org/v2"
S2_API = "https://api.semanticscholar.org/graph/v1"
ARXIV_PATTERN = re.compile(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]+)', re.IGNORECASE)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("retry")


def safe_filename(title, max_len=120):
    safe = re.sub(r'[\\/:*?"<>|]', '_', title)
    safe = re.sub(r'\s+', '_', safe.strip())
    return safe[:max_len]


MAX_PDF_BYTES = 50 * 1024 * 1024  # 50MB cap

def download_url(url, dest_path, label=""):
    try:
        resp = requests.get(url, timeout=(10, 60),
                            headers={"User-Agent": "PAGC-Retry/1.0 (research use)"},
                            allow_redirects=True, stream=True)
        ct = resp.headers.get("content-type", "")
        if resp.status_code == 200:
            chunks = []
            total = 0
            for chunk in resp.iter_content(65536):
                chunks.append(chunk)
                total += len(chunk)
                if total > MAX_PDF_BYTES:
                    log.debug(f"  [SKIP-TOOBIG] {url[:60]} > 50MB")
                    return False
            content = b"".join(chunks)
            if b"%PDF" in content[:10] or "pdf" in ct.lower():
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                dest_path.write_bytes(content)
                log.info(f"  [OK] {label or url[:60]} -> {dest_path.name}")
                return True
        log.debug(f"  [SKIP] {url[:60]} HTTP {resp.status_code} ct={ct[:30]}")
    except Exception as e:
        log.debug(f"  [ERR] {url[:60]}: {e}")
    return False


def get_unpaywall_pdf(doi):
    clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    url = f"{UNPAYWALL_API}/{clean}?email={UNPAYWALL_EMAIL}"
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            data = r.json()
            best = data.get("best_oa_location") or {}
            return best.get("url_for_pdf") or best.get("url")
    except Exception:
        pass
    return None


def get_s2_oa_pdf(doi=None, title=None):
    params = {"fields": "title,openAccessPdf"}
    try:
        if doi:
            clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
            url = f"{S2_API}/paper/DOI:{clean}"
            r = requests.get(url, params=params, timeout=15,
                             headers={"User-Agent": "PAGC-Retry/1.0"})
        elif title:
            url = f"{S2_API}/paper/search"
            params["query"] = title
            params["limit"] = 1
            r = requests.get(url, params=params, timeout=15,
                             headers={"User-Agent": "PAGC-Retry/1.0"})
            if r.status_code == 200:
                items = r.json().get("data", [])
                if items:
                    oa = items[0].get("openAccessPdf") or {}
                    return oa.get("url")
            return None
        else:
            return None

        if r.status_code == 200:
            oa = r.json().get("openAccessPdf") or {}
            return oa.get("url")
    except Exception:
        pass
    return None


def try_doi_direct(doi):
    """Try common open-access DOI endpoints directly."""
    if not doi:
        return None
    clean = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    # bioRxiv / medRxiv
    if clean.startswith("10.1101/"):
        biorxiv_id = clean.split("10.1101/")[1]
        return f"https://www.biorxiv.org/content/{clean}v1.full.pdf"
    # OSF preprints
    if clean.startswith("10.31234/osf.io/"):
        osf_id = clean.split("/")[-1]
        return f"https://psyarxiv.com/{osf_id}/download"
    # Research Square
    if clean.startswith("10.21203/"):
        return f"https://www.researchsquare.com/article/{clean.split('/')[-1]}/v1.pdf"
    # MDPI (10.3390)
    if clean.startswith("10.3390/"):
        return f"https://doi.org/{clean}"  # MDPI redirects to PDF
    # PeerJ
    if clean.startswith("10.7717/"):
        return f"https://doi.org/{clean}"
    # eLife
    if clean.startswith("10.7554/"):
        return f"https://doi.org/{clean}"
    # SSRN preprints (10.2139)
    if clean.startswith("10.2139/"):
        return None  # Usually paywalled
    return None


def load_failed_entries():
    entries = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                if d.get("status") == "failed":
                    entries.append(d)
            except Exception:
                pass
    return entries


def entry_matches(d, old_entry):
    """Check if manifest entry d matches old_entry to update."""
    if d.get("status") != "failed":
        return False
    # Match by url, doi, or title
    if old_entry.get("url") and d.get("url") == old_entry["url"]:
        return True
    if old_entry.get("doi") and d.get("doi") == old_entry["doi"]:
        return True
    if old_entry.get("title") and d.get("title") == old_entry["title"]:
        return True
    return False


def update_manifest_entry(old_entry, new_entry):
    """Rewrite manifest replacing the failed entry with new one."""
    lines = []
    replaced = False
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                if not replaced and entry_matches(d, old_entry):
                    lines.append(json.dumps(new_entry))
                    replaced = True
                else:
                    lines.append(line)
            except Exception:
                lines.append(line)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    failed = load_failed_entries()
    log.info(f"Retrying {len(failed)} failed entries...")

    succeeded = 0
    still_failed = 0

    for i, entry in enumerate(failed):
        title = entry.get("title", "Unknown")
        url = entry.get("url", "")
        discipline = entry.get("discipline", "general")

        # Extract DOI — from explicit doi field OR embedded in URL
        doi = entry.get("doi") or None
        if not doi and "doi.org/" in url:
            doi = url  # full doi.org URL
        if doi and not doi.startswith("http") and not doi.startswith("10."):
            doi = None  # invalid

        # Extract arxiv ID
        arxiv_match = ARXIV_PATTERN.search(url) if url else None
        arxiv_id = entry.get("arxiv_id") or (arxiv_match.group(1) if arxiv_match else None)

        if i % 100 == 0:
            log.info(f"Progress: {i}/{len(failed)} processed | downloaded so far: {succeeded}")

        disc_dir = PAPERS_DIR / re.sub(r'[^\w]', '_', discipline.lower())[:40]
        dest = disc_dir / (safe_filename(title) + ".pdf")

        if dest.exists() and dest.stat().st_size > 5000:
            log.info(f"  [SKIP-EXISTS] {title[:60]}")
            new_entry = dict(entry)
            new_entry["status"] = "already_exists"
            new_entry["pdf_path"] = str(dest)
            update_manifest_entry(entry, new_entry)
            succeeded += 1
            continue

        pdf_url = None
        method = None

        # 1. Direct OA detection by DOI prefix
        if doi:
            pdf_url = try_doi_direct(doi)
            if pdf_url:
                method = "doi_direct"

        # 2. Unpaywall
        if not pdf_url and doi:
            pdf_url = get_unpaywall_pdf(doi)
            if pdf_url:
                method = "unpaywall"
            time.sleep(0.5)

        # 3. Semantic Scholar OA
        if not pdf_url:
            pdf_url = get_s2_oa_pdf(doi=doi, title=title if not doi else None)
            if pdf_url:
                method = "s2_oa"
            time.sleep(0.5)

        # 4. ArXiv (if URL contains arxiv)
        if not pdf_url and arxiv_id:
            from paper_downloader import download_arxiv
            if download_arxiv(arxiv_id, dest):
                new_entry = dict(entry)
                new_entry["status"] = "downloaded_arxiv"
                new_entry["pdf_path"] = str(dest)
                update_manifest_entry(entry, new_entry)
                succeeded += 1
                if i % 50 == 0:
                    log.info(f"Progress: {i}/{len(failed)} | Success: {succeeded} | Failed: {still_failed}")
                continue
            time.sleep(0.5)

        # Attempt download
        if pdf_url:
            if download_url(pdf_url, dest, label=f"{method}: {title[:50]}"):
                new_entry = dict(entry)
                new_entry["status"] = f"downloaded_{method}"
                new_entry["pdf_path"] = str(dest)
                update_manifest_entry(entry, new_entry)
                succeeded += 1
                if i % 50 == 0:
                    log.info(f"Progress: {i}/{len(failed)} | Success: {succeeded} | Failed: {still_failed}")
                continue

        still_failed += 1
        if i % 100 == 0 and i > 0:
            log.info(f"Progress: {i}/{len(failed)} | Success: {succeeded} | Failed: {still_failed}")

    log.info(f"\n=== RETRY COMPLETE ===")
    log.info(f"Total retried: {len(failed)}")
    log.info(f"Newly downloaded: {succeeded}")
    log.info(f"Still failed: {still_failed}")


if __name__ == "__main__":
    main()
