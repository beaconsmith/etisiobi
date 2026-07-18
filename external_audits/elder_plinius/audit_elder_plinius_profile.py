from __future__ import annotations

import json
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPOS_DIR = ROOT / "repos"
RAW_REPOS = ROOT / "repos_raw.json"
OUT_JSON = ROOT / "profile_code_inventory.json"
OUT_MD = ROOT / "profile_code_audit.md"

CODE_SUFFIXES = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".html",
    ".css",
    ".mjs",
    ".cjs",
    ".json",
    ".yaml",
    ".yml",
    ".md",
    ".sh",
    ".sol",
}

SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", "__pycache__", ".venv", "venv"}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def run(cmd: list[str], cwd: Path | None = None, timeout: int = 120) -> tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )
    return proc.returncode, proc.stdout.strip()


def load_repos() -> list[dict[str, Any]]:
    return json.loads(RAW_REPOS.read_text(encoding="utf-8"))


def clone_or_update(repo: dict[str, Any]) -> dict[str, Any]:
    REPOS_DIR.mkdir(parents=True, exist_ok=True)
    name = repo["name"]
    url = repo["clone_url"]
    dest = REPOS_DIR / name
    if dest.exists():
        code, output = run(["git", "fetch", "--depth=1", "origin"], cwd=dest, timeout=120)
        if code == 0:
            code, output = run(["git", "reset", "--hard", "origin/HEAD"], cwd=dest, timeout=120)
        action = "updated"
    else:
        code, output = run(["git", "clone", "--depth=1", url, str(dest)], timeout=240)
        action = "cloned"
    return {"name": name, "action": action, "ok": code == 0, "output": output[-1000:]}


def iter_files(repo_path: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_path.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in CODE_SUFFIXES:
            continue
        files.append(path)
    return files


def safe_head(path: Path, max_chars: int = 4000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:max_chars]
    except OSError:
        return ""


def classify_repo(repo: dict[str, Any], repo_path: Path) -> dict[str, Any]:
    files = iter_files(repo_path)
    suffix_counts = Counter(path.suffix.lower() or "[none]" for path in files)
    top_level = sorted([path.name for path in repo_path.iterdir() if path.name != ".git"])[:80] if repo_path.exists() else []
    readmes = [path for path in files if path.name.lower().startswith("readme")]
    papers = [path for path in files if path.name.lower() in {"paper.md", "paper.html"} or "paper" in path.name.lower()]
    results = [path for path in files if "result" in path.name.lower() or "experiment" in path.as_posix().lower()]
    package_files = [path for path in files if path.name in {"package.json", "requirements.txt", "pyproject.toml", "pom.xml"}]

    text = "\n".join(
        [
            repo.get("name", ""),
            repo.get("description") or "",
            "\n".join(safe_head(path, 2000) for path in readmes[:2]),
        ]
    ).lower()
    themes: list[str] = []
    theme_keywords = {
        "research_report": ["paper", "experiment", "results", "benchmark", "replication"],
        "red_team_security": ["red team", "jailbreak", "prompt leak", "stego", "adversarial", "defender"],
        "agent_automation": ["agent", "autonomous", "orchestrator", "self-improvement"],
        "symbolic_language": ["language", "translation", "glyph", "morphology", "xeno"],
        "public_demo": ["index.html", "demo", "ui", "visualizer"],
        "llm_parameter_search": ["temperature", "hyperparameter", "tune"],
    }
    for theme, keywords in theme_keywords.items():
        if any(keyword in text for keyword in keywords):
            themes.append(theme)

    safe_lessons = []
    if "research_report" in themes:
        safe_lessons.append("Pair claims with raw result files, figures, and explicit correction logs.")
    if "agent_automation" in themes:
        safe_lessons.append("Turn autonomous workflows into measurable loops with keep/reject decisions.")
    if "symbolic_language" in themes:
        safe_lessons.append("Make symbolic systems deterministic, inspectable, and benchmarkable.")
    if "public_demo" in themes:
        safe_lessons.append("Expose a demo/dashboard that lets outsiders inspect the artifact.")
    if "llm_parameter_search" in themes:
        safe_lessons.append("Use sweep-style baselines before claiming model or prompt improvements.")
    if "red_team_security" in themes:
        safe_lessons.append("Adopt adversarial audit discipline, but do not copy offensive mechanics.")

    return {
        "name": repo["name"],
        "html_url": repo["html_url"],
        "description": repo.get("description"),
        "stars": repo.get("stargazers_count"),
        "language": repo.get("language"),
        "license": (repo.get("license") or {}).get("spdx_id") if repo.get("license") else None,
        "file_count": len(files),
        "suffix_counts": dict(suffix_counts.most_common()),
        "top_level": top_level,
        "readme_count": len(readmes),
        "paper_like_files": [str(path.relative_to(repo_path)).replace("\\", "/") for path in papers[:20]],
        "result_like_files": [str(path.relative_to(repo_path)).replace("\\", "/") for path in results[:20]],
        "package_files": [str(path.relative_to(repo_path)).replace("\\", "/") for path in package_files],
        "themes": themes,
        "safe_lessons_for_etisiobi": safe_lessons,
    }


def main() -> int:
    repos = load_repos()
    clone_results = []
    inventories = []
    for repo in repos:
        clone_results.append(clone_or_update(repo))
        repo_path = REPOS_DIR / repo["name"]
        if repo_path.exists():
            inventories.append(classify_repo(repo, repo_path))

    theme_counts = Counter(theme for item in inventories for theme in item["themes"])
    language_counts = Counter((item.get("language") or "unknown") for item in inventories)
    star_leaders = sorted(inventories, key=lambda item: item.get("stars") or 0, reverse=True)[:15]
    by_theme: dict[str, list[str]] = defaultdict(list)
    for item in inventories:
        for theme in item["themes"]:
            by_theme[theme].append(item["name"])

    result = {
        "generated_at": now(),
        "source_profile": "https://github.com/elder-plinius",
        "repo_count": len(repos),
        "cloned_or_updated": clone_results,
        "language_counts": dict(language_counts),
        "theme_counts": dict(theme_counts),
        "star_leaders": [{"name": item["name"], "stars": item["stars"], "url": item["html_url"]} for item in star_leaders],
        "theme_repos": dict(by_theme),
        "repositories": inventories,
        "safety_note": "This audit reads public code and metadata only. It does not execute external code or reproduce offensive implementation details.",
    }
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# elder-plinius Profile Code Audit",
        "",
        f"Generated: {result['generated_at']}",
        f"Source: {result['source_profile']}",
        f"Repos audited: {result['repo_count']}",
        "",
        "## Safety Boundary",
        "",
        result["safety_note"],
        "",
        "## Theme Counts",
        "",
    ]
    for theme, count in theme_counts.most_common():
        lines.append(f"- `{theme}`: {count}")
    lines.extend(["", "## Star Leaders", ""])
    for item in star_leaders:
        lines.append(f"- [{item['name']}]({item['html_url']}) — {item['stars']} stars")
    lines.extend(["", "## Lessons For Etisiobi", ""])
    lessons = Counter(lesson for item in inventories for lesson in item["safe_lessons_for_etisiobi"])
    for lesson, count in lessons.most_common():
        lines.append(f"- {lesson} ({count} repos)")
    lines.extend(["", "## Repository Inventory", ""])
    for item in inventories:
        lines.append(f"### {item['name']}")
        lines.append("")
        lines.append(f"- URL: {item['html_url']}")
        lines.append(f"- Description: {item.get('description') or ''}")
        lines.append(f"- Stars: {item.get('stars')}")
        lines.append(f"- Language: {item.get('language') or 'unknown'}")
        lines.append(f"- Files inventoried: {item['file_count']}")
        lines.append(f"- Themes: {', '.join(item['themes']) if item['themes'] else 'unclassified'}")
        if item["paper_like_files"]:
            lines.append(f"- Paper-like files: {', '.join(item['paper_like_files'][:5])}")
        if item["result_like_files"]:
            lines.append(f"- Result/experiment files: {', '.join(item['result_like_files'][:5])}")
        if item["safe_lessons_for_etisiobi"]:
            lines.append("- Safe lessons:")
            for lesson in item["safe_lessons_for_etisiobi"]:
                lines.append(f"  - {lesson}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print("ELDER_PLINIUS_PROFILE_AUDIT_COMPLETE")
    print(f"repos={len(inventories)}")
    print(f"themes={dict(theme_counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
