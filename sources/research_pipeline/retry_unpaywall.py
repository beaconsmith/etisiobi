# -*- coding: utf-8 -*-
"""
Targeted retry: only Unpaywall API for failed manifest entries with DOIs.
Fast, no S2 snowball, strict timeouts.
"""

import json, re, sys, time, logging, socket
from pathlib import Path
import requests

# Hard global socket timeout — kills ANY blocked network op after 20s
socket.setdefaulttimeout(20)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[2]
PAPERS_DIR = REPO_ROOT / "sources" / "papers"
MANIFEST_PATH = REPO_ROOT / "sources" / "download_manifest.jsonl"
LOG_PATH = REPO_ROOT / "sources" / "retry_unpaywall.log"
UNPAYWALL_EMAIL = "pagc-research@etisiobi.io"
UNPAYWALL_API = "https://api.unpaywall.org/v2"
ARXIV_PATTERN = re.compile(r'arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]+)', re.IGNORECASE)
MAX_PDF_BYTES = 30 * 1024 * 1024  # 30MB cap

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8", mode="w"),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("retry_up")

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "PAGC-Retry/2.0 (research; pagc-research@etisiobi.io)"})


def safe_filename(title, max_len=120):
    safe = re.sub(r'[\\/:*?"<>|]', '_', title)
    safe = re.sub(r'\s+', '_', safe.strip())
    return safe[:max_len]


def get_unpaywall(doi_raw):
    """Returns OA PDF URL or None. doi_raw can be full URL or bare DOI."""
    clean = doi_raw.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    if not clean or not clean.startswith("10."):
        return None
    try:
        r = SESSION.get(f"{UNPAYWALL_API}/{clean}?email={UNPAYWALL_EMAIL}", timeout=12)
        if r.status_code == 200:
            best = r.json().get("best_oa_location") or {}
            return best.get("url_for_pdf") or best.get("url")
    except Exception:
        pass
    return None


def get_biorxiv_pdf(doi_raw):
    """Direct PDF URL for bioRxiv/medRxiv preprints."""
    clean = doi_raw.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    if clean.startswith("10.1101/"):
        return f"https://www.biorxiv.org/content/{clean}v1.full.pdf"
    return None


TIMEOUT = (6, 18)  # (connect, read) seconds


def download_pdf(url, dest_path):
    """Download PDF with explicit timeouts on every request."""
    try:
        try:
            h = SESSION.head(url, timeout=TIMEOUT, allow_redirects=True)
            ct_head = h.headers.get("content-type", "")
            if h.status_code == 200 and "html" in ct_head and "pdf" not in url.lower():
                return False
        except Exception:
            pass

        r = SESSION.get(url, timeout=TIMEOUT, stream=True, allow_redirects=True)
        ct = r.headers.get("content-type", "")
        if r.status_code != 200:
            return False
        if "html" in ct.lower() and "pdf" not in url.lower():
            return False

        chunks = []
        total = 0
        deadline = time.time() + 25  # hard 25s wall-clock limit
        for chunk in r.iter_content(65536):
            if not chunk:
                break
            if time.time() > deadline:
                log.debug(f"  Wall-clock timeout: {url[:60]}")
                return False
            chunks.append(chunk)
            total += len(chunk)
            if len(chunks) == 1 and b"%PDF" not in chunk[:10]:
                return False
            if total > MAX_PDF_BYTES:
                return False

        content = b"".join(chunks)
        if len(content) < 1000:
            return False
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_bytes(content)
        return True
    except Exception:
        return False


def load_failed():
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


def rewrite_manifest(updates):
    """Apply a dict of {match_key: new_entry} updates to the manifest."""
    lines = []
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                if d.get("status") == "failed":
                    # match by doi or url or title
                    key = d.get("doi") or d.get("url") or d.get("title", "")
                    if key in updates:
                        lines.append(json.dumps(updates[key]))
                        continue
            except Exception:
                pass
            lines.append(line)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    failed = load_failed()
    log.info(f"Loaded {len(failed)} failed entries to retry")

    updates = {}
    succeeded = 0
    no_oa = 0

    for i, entry in enumerate(failed):
        if i % 50 == 0 and i > 0:
            log.info(f"  Progress {i}/{len(failed)} | new downloads: {succeeded}")
            # Flush updates to disk periodically
            if updates:
                rewrite_manifest(updates)
                updates = {}

        title = entry.get("title", "Unknown")
        doi = entry.get("doi") or None
        url = entry.get("url", "")
        discipline = entry.get("discipline", "general")

        # Get bare DOI string
        doi_raw = doi or url
        if not doi_raw:
            no_oa += 1
            continue

        # Clean DOI
        clean_doi = doi_raw.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
        if not clean_doi.startswith("10."):
            no_oa += 1
            continue

        disc_dir = PAPERS_DIR / re.sub(r'[^\w]', '_', discipline.lower())[:40]
        dest = disc_dir / (safe_filename(title) + ".pdf")

        if dest.exists() and dest.stat().st_size > 5000:
            match_key = doi or url or title
            updates[match_key] = dict(entry, status="already_exists", pdf_path=str(dest))
            succeeded += 1
            continue

        pdf_url = None

        # 1. Try bioRxiv direct
        pdf_url = get_biorxiv_pdf(doi_raw)

        # 2. Unpaywall
        if not pdf_url:
            pdf_url = get_unpaywall(doi_raw)
            time.sleep(0.3)

        if not pdf_url:
            no_oa += 1
            continue

        if download_pdf(pdf_url, dest):
            log.info(f"  [OK] {title[:70]}")
            match_key = doi or url or title
            updates[match_key] = dict(entry,
                status="downloaded_unpaywall",
                pdf_path=str(dest)
            )
            succeeded += 1
        else:
            no_oa += 1

    # Final flush
    if updates:
        rewrite_manifest(updates)

    log.info(f"\n=== DONE ===")
    log.info(f"Entries retried: {len(failed)}")
    log.info(f"New downloads: {succeeded}")
    log.info(f"No OA available: {no_oa}")


if __name__ == "__main__":
    main()
