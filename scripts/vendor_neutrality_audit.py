from __future__ import annotations

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "vendor_neutrality_audit.md"
PRUNE_DIRS = {
    ".git",
    "node_modules",
    ".next",
    ".turbo",
    "dist",
    "build",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
}
TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".mjs",
    ".json",
    ".jsonl",
    ".yaml",
    ".yml",
    ".toml",
    ".csv",
    ".tex",
    ".bib",
    ".html",
}
TERMS = [
    "claude",
    "anthropic",
    "ANTHROPIC_API_KEY",
    "api.anthropic.com",
    "@anthropic-ai",
    ".claude",
]
TERM_PATTERNS = [
    re.compile(r"(?<![A-Za-z])claude(?![A-Za-z])", re.I),
    re.compile(r"(?<![A-Za-z])anthropic(?![A-Za-z])", re.I),
    re.compile(r"ANTHROPIC_API_KEY", re.I),
    re.compile(r"api\.anthropic\.com", re.I),
    re.compile(r"@anthropic-ai", re.I),
    re.compile(r"\.claude", re.I),
]

NON_BLOCKING_PREFIXES = (
    "quarantine/",
    "library/",
    "data/",
    "external_sources/",
    "research/pagc/sources/",
    "ETISIOBI_REPO_ALIGNMENT_AUDIT.md",
    "log.md",
    "research_reset_audit.md",
    "vendor_neutrality_audit.md",
)

SCANNER_FILES = {
    "scripts/vendor_neutrality_audit.py",
}

GENERATED_PREFIXES = (
    "corpus/",
    "repo_index.json",
    "repo_map.md",
    "research_repo_audit.md",
    "papers/SELECTED_PAPER/freeze_manifest",
    "spine/retrieval_manifest.yaml",
    "obsidian_vault/",
)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def iter_files() -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in PRUNE_DIRS]
        current = Path(dirpath)
        for filename in filenames:
            files.append(current / filename)
    return sorted(files, key=lambda item: rel(item).lower())


def read_text(path: Path, limit: int = 1_000_000) -> str | None:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return None
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data[:4096]:
        return None
    if len(data) > limit:
        data = data[:limit]
    return data.decode("utf-8", errors="replace")


def find_term(text: str) -> re.Match[str] | None:
    for pattern in TERM_PATTERNS:
        match = pattern.search(text)
        if match:
            return match
    return None


def scope_for(path_text: str) -> str:
    if path_text in SCANNER_FILES:
        return "scanner-self"
    if path_text.startswith(NON_BLOCKING_PREFIXES):
        return "historical-or-source"
    if path_text.startswith(GENERATED_PREFIXES):
        return "generated-projection"
    return "operational"


def is_blocking(path_text: str) -> bool:
    return scope_for(path_text) == "operational"


def audit() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    filename_hits: list[dict[str, str]] = []
    content_hits: list[dict[str, str]] = []
    for path in iter_files():
        path_text = rel(path)
        filename_match = find_term(path_text)
        if filename_match:
            filename_hits.append(
                {
                    "path": path_text,
                    "match": filename_match.group(0),
                    "scope": scope_for(path_text),
                    "blocking": str(is_blocking(path_text)).lower(),
                }
            )
        text = read_text(path)
        if not text:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            match = find_term(line)
            if match:
                content_hits.append(
                    {
                        "path": path_text,
                        "line": str(line_no),
                        "match": match.group(0),
                        "scope": scope_for(path_text),
                        "blocking": str(is_blocking(path_text)).lower(),
                        "context": line.strip()[:220],
                    }
                )
                break
    return filename_hits, content_hits


def render(filename_hits: list[dict[str, str]], content_hits: list[dict[str, str]]) -> str:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    blocking_hits = [
        hit for hit in [*filename_hits, *content_hits] if hit.get("blocking") == "true"
    ]
    status = "VENDOR_NEUTRALITY_FAIL" if blocking_hits else "VENDOR_NEUTRALITY_PASS"
    lines = [
        "# Vendor Neutrality Audit",
        "",
        f"generated_at: `{generated_at}`",
        f"status: `{status}`",
        f"blocking_hits: `{len(blocking_hits)}`",
        f"nonblocking_hits: `{len(filename_hits) + len(content_hits) - len(blocking_hits)}`",
        "",
        "Operational vendor terms are not allowed in public or operational surfaces unless explicitly quarantined as historical provenance.",
        "",
        "## Filename Hits",
        "",
    ]
    if filename_hits:
        lines.extend(["| path | match | scope | blocking |", "|---|---|---|---|"])
        for hit in filename_hits:
            lines.append(f"| `{hit['path']}` | `{hit['match']}` | `{hit['scope']}` | `{hit['blocking']}` |")
    else:
        lines.append("None.")
    lines.extend(["", "## Content Hits", ""])
    if content_hits:
        lines.extend(["| path | line | match | scope | blocking | context |", "|---|---:|---|---|---|---|"])
        for hit in content_hits:
            context = hit["context"].replace("|", "\\|")
            lines.append(
                f"| `{hit['path']}` | {hit['line']} | `{hit['match']}` | `{hit['scope']}` | `{hit['blocking']}` | {context} |"
            )
    else:
        lines.append("None.")
    lines.extend(
        [
            "",
            "## Policy",
            "",
            "Use provider-neutral capability names in operational docs: `planner`, `retriever`, `scientist`, `coder`, `critic`, `reviewer`, `embedding`, `vision`.",
            "Historical vendor traces should either be quarantined with metadata or deliberately preserved under an explicit provenance policy.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit operational vendor coupling terms.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output markdown path.")
    args = parser.parse_args()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    filename_hits, content_hits = audit()
    output.write_text(render(filename_hits, content_hits), encoding="utf-8")
    print(f"wrote {output}")
    blocking_hits = [
        hit for hit in [*filename_hits, *content_hits] if hit.get("blocking") == "true"
    ]
    print(f"filename_hits={len(filename_hits)} content_hits={len(content_hits)} blocking_hits={len(blocking_hits)}")
    return 1 if blocking_hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
