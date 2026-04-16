"""
WikiOS Server — serves the etisiobi repo as a knowledge API.
Scans all .md files, parses metadata, and serves the WikiOS frontend.

Usage:
    python serve.py
Then open: http://localhost:7891
"""

import os
import re
import json
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import datetime, timezone
import urllib.parse

# ── Config ────────────────────────────────────────────────────
REPO_ROOT   = Path(r"C:\Users\USER\code\etisiobi")
STATIC_DIR  = Path(__file__).parent   # serve.py lives inside wiki_os/
PORT        = 7891

# Folder → tag label mapping
FOLDER_TAGS = {
    "pagc_library":           "PAGC Library",
    "paper":                  "Paper Draft",
    "sources":                "Sources",
    "hermes_workspace":       "Hermes Workspace",
    "reports":                "Reports",
    "raw":                    "Raw Data",
    "kb":                     "Knowledge Base",
    "methods":                "Methods",
}

# ── Markdown Parser ───────────────────────────────────────────

def extract_title(content: str, filename: str) -> str:
    """Extract the first H1/H2 heading, or fall back to filename."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line.startswith("## "):
            return line[3:].strip()
    # Clean up filename
    name = Path(filename).stem
    name = name.replace("_", " ").replace("-", " ")
    return name.title()

def extract_excerpt(content: str, max_chars: int = 280) -> str:
    """Extract a clean text excerpt, skipping headings and code blocks."""
    lines = []
    in_code = False
    for line in content.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.strip().startswith("#"):
            continue
        if line.strip().startswith("|"):
            continue
        if line.strip().startswith("- [") or line.strip().startswith("* ["):
            continue
        clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
        clean = re.sub(r'[*_`>]', '', clean).strip()
        if clean:
            lines.append(clean)
        if sum(len(l) for l in lines) > max_chars:
            break
    text = " ".join(lines)
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + "..."
    return text or "No excerpt available."

def count_wiki_links(content: str) -> int:
    """Count [[wiki-links]] in the content."""
    return len(re.findall(r'\[\[([^\]]+)\]\]', content))

def count_external_links(content: str) -> int:
    """Count [text](url) links."""
    return len(re.findall(r'\[[^\]]+\]\(https?://[^\)]+\)', content))

def infer_tag(filepath: Path) -> str:
    """Infer a tag from the file's folder path."""
    parts = filepath.relative_to(REPO_ROOT).parts
    for part in parts:
        part_lower = part.lower()
        for key, label in FOLDER_TAGS.items():
            if key in part_lower:
                return label
    return "Note"

def get_mod_time(filepath: Path) -> str:
    """Return a human-readable modification time."""
    mtime = filepath.stat().st_mtime
    dt = datetime.fromtimestamp(mtime)
    now = datetime.now()
    delta = now - dt
    if delta.days == 0:
        hours = delta.seconds // 3600
        if hours == 0:
            minutes = delta.seconds // 60
            return f"{minutes}m ago" if minutes > 0 else "Just now"
        return f"{hours}h ago"
    elif delta.days == 1:
        return "Yesterday"
    elif delta.days < 7:
        return f"{delta.days} days ago"
    else:
        return dt.strftime("%b %d, %Y")

def word_count(content: str) -> int:
    return len(content.split())

# ── Scan Repo ─────────────────────────────────────────────────

EXCLUDE_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
EXCLUDE_FILES = {"package-lock.json"}

def scan_repo() -> list[dict]:
    notes = []
    for filepath in REPO_ROOT.rglob("*.md"):
        # Skip excluded dirs
        if any(excl in filepath.parts for excl in EXCLUDE_DIRS):
            continue
        if filepath.name in EXCLUDE_FILES:
            continue
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        rel = str(filepath.relative_to(REPO_ROOT)).replace("\\", "/")
        notes.append({
            "id":          str(filepath),
            "path":        rel,
            "filename":    filepath.name,
            "title":       extract_title(content, filepath.name),
            "tag":         infer_tag(filepath),
            "excerpt":     extract_excerpt(content),
            "date":        get_mod_time(filepath),
            "words":       word_count(content),
            "links":       count_wiki_links(content) + count_external_links(content),
            "size_kb":     round(filepath.stat().st_size / 1024, 1),
            "content":     content[:8000],  # send first 8k for preview
        })

    # Sort by modification time (newest first)
    notes.sort(key=lambda n: Path(n["id"]).stat().st_mtime, reverse=True)
    return notes

# ── Stats ─────────────────────────────────────────────────────

def get_stats(notes: list[dict]) -> dict:
    tags = {}
    total_words = 0
    total_links = 0
    for n in notes:
        tags[n["tag"]] = tags.get(n["tag"], 0) + 1
        total_words += n["words"]
        total_links += n["links"]

    # Count downloaded PDFs
    papers_dir = REPO_ROOT / "sources" / "papers"
    pdf_count = len(list(papers_dir.rglob("*.pdf"))) if papers_dir.exists() else 0

    # Count manifest entries
    manifest = REPO_ROOT / "sources" / "download_manifest.jsonl"
    manifest_count = 0
    if manifest.exists():
        with open(manifest, encoding="utf-8") as f:
            manifest_count = sum(1 for line in f if line.strip())

    return {
        "total_notes":     len(notes),
        "total_words":     total_words,
        "total_links":     total_links,
        "total_tags":      len(tags),
        "tags":            tags,
        "repo_path":       str(REPO_ROOT),
        "pdfs_downloaded": pdf_count,
        "manifest_total":  manifest_count,
    }

# ── HTTP Handler ──────────────────────────────────────────────

class WikiHandler(BaseHTTPRequestHandler):
    _notes_cache = None
    _cache_time  = 0

    def get_notes(self):
        import time
        now = time.time()
        if WikiHandler._notes_cache is None or (now - WikiHandler._cache_time) > 30:
            print(f"[WikiOS] Scanning {REPO_ROOT}...")
            WikiHandler._notes_cache = scan_repo()
            WikiHandler._cache_time = now
            print(f"[WikiOS] Found {len(WikiHandler._notes_cache)} notes.")
        return WikiHandler._notes_cache

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def send_file(self, filepath: Path):
        try:
            content = filepath.read_bytes()
            mime, _ = mimetypes.guess_type(str(filepath))
            self.send_response(200)
            self.send_header("Content-Type", mime or "text/plain")
            self.send_header("Content-Length", len(content))
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # ── API Routes ────────────────────────────────────────

        if path == "/api/notes":
            notes = self.get_notes()
            q = query.get("q", [None])[0]
            tag = query.get("tag", [None])[0]

            filtered = notes
            if q:
                q_lower = q.lower()
                filtered = [
                    n for n in filtered
                    if q_lower in n["title"].lower()
                    or q_lower in n["excerpt"].lower()
                    or q_lower in n["tag"].lower()
                    or q_lower in n["filename"].lower()
                ]
            if tag:
                filtered = [n for n in filtered if n["tag"] == tag]

            self.send_json({"notes": filtered, "total": len(filtered)})

        elif path == "/api/stats":
            notes = self.get_notes()
            self.send_json(get_stats(notes))

        elif path == "/api/note":
            note_path = query.get("path", [None])[0]
            if not note_path:
                self.send_json({"error": "path required"}, 400)
                return
            abs_path = REPO_ROOT / note_path
            try:
                content = abs_path.read_text(encoding="utf-8", errors="ignore")
                self.send_json({"path": note_path, "content": content, "title": extract_title(content, abs_path.name)})
            except Exception as e:
                self.send_json({"error": str(e)}, 404)

        elif path == "/api/refresh":
            WikiHandler._notes_cache = None
            notes = self.get_notes()
            self.send_json({"refreshed": True, "total": len(notes)})

        # ── Static Files ──────────────────────────────────────
        else:
            if path == "/" or path == "":
                path = "/index.html"
            static_path = STATIC_DIR / path.lstrip("/")
            if static_path.exists() and static_path.is_file():
                self.send_file(static_path)
            else:
                # Fallback to index.html for SPA routing
                self.send_file(STATIC_DIR / "index.html")

    def log_message(self, format, *args):
        print(f"[WikiOS] {self.address_string()} - {format % args}")

# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"""
+----------------------------------------------+
|       WikiOS -- Knowledge Server             |
+----------------------------------------------+
  Vault : {str(REPO_ROOT)}
  URL   : http://localhost:{PORT}
+----------------------------------------------+
    """)
    # Pre-warm the cache
    notes = scan_repo()
    print(f"[WikiOS] Loaded {len(notes)} notes from vault. Starting server...")
    server = HTTPServer(("0.0.0.0", PORT), WikiHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[WikiOS] Server stopped.")
