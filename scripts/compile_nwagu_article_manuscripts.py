from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "papers" / "nwagu_aneke_articles"
LOG_DIR = PACKAGE / "compile_logs"
BUILD_EXTENSIONS = {".aux", ".bbl", ".blg", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"}
COMMANDS = [
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
    ["bibtex", "main"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
]


def is_inside(child: Path, parent: Path) -> bool:
    child_resolved = child.resolve()
    parent_resolved = parent.resolve()
    return child_resolved == parent_resolved or parent_resolved in child_resolved.parents


def clean_build_files(article_dir: Path) -> None:
    if not is_inside(article_dir, PACKAGE):
        raise RuntimeError(f"Refusing to clean outside package: {article_dir}")
    for path in article_dir.iterdir():
        if path.is_file() and path.stem == "main" and path.suffix in BUILD_EXTENSIONS:
            path.unlink()


def run_command(command: list[str], cwd: Path, env: dict[str, str]) -> dict[str, object]:
    executable = shutil.which(command[0])
    if executable is None:
        return {
            "command": command,
            "returncode": 127,
            "stdout": "",
            "stderr": f"Missing executable: {command[0]}",
        }
    completed = None
    attempts = []
    for attempt in range(1, 4):
        completed = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env=env,
        )
        attempts.append(
            {
                "attempt": attempt,
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
            }
        )
        lock_failure = "I can't write on file `main.log'" in completed.stdout
        if completed.returncode == 0 or not lock_failure:
            break
        time.sleep(1.0)
    return {
        "command": command,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "attempts": attempts,
    }


def compile_article(article_dir: Path, env: dict[str, str]) -> dict[str, object]:
    clean_build_files(article_dir)
    runs = []
    for command in COMMANDS:
        result = run_command(command, article_dir, env)
        runs.append(result)
        if result["returncode"] != 0:
            break
    pdf_path = article_dir / "main.pdf"
    return {
        "article_dir": article_dir.relative_to(ROOT).as_posix(),
        "status": "compiled" if pdf_path.exists() and all(run["returncode"] == 0 for run in runs) else "failed",
        "pdf": pdf_path.relative_to(ROOT).as_posix() if pdf_path.exists() else None,
        "runs": runs,
    }


def write_report(results: list[dict[str, object]]) -> None:
    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    (LOG_DIR / "compile_results.json").write_text(json.dumps({"generated_at": generated_at, "results": results}, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Nwagu Aneke Article Compile Report",
        "",
        f"Generated: {generated_at}",
        "",
        "| Article | Status | PDF |",
        "|---|---|---|",
    ]
    for result in results:
        article = result["article_dir"]
        status = result["status"]
        pdf = result["pdf"] or ""
        lines.append(f"| `{article}` | `{status}` | `{pdf}` |")
        article_slug = Path(str(article)).name
        log_text = []
        for run in result["runs"]:  # type: ignore[index]
            log_text.append("$ " + " ".join(run["command"]))  # type: ignore[index]
            log_text.append(f"returncode={run['returncode']}")
            log_text.append(str(run["stdout"]))
            if run["stderr"]:
                log_text.append("STDERR:")
                log_text.append(str(run["stderr"]))
        (LOG_DIR / f"{article_slug}.log").write_text("\n".join(log_text), encoding="utf-8")
    (PACKAGE / "compile_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    env = os.environ.copy()
    env["MIKTEX_DISABLE_INSTALLER"] = "1"
    article_dirs = sorted(path for path in PACKAGE.iterdir() if path.is_dir() and (path / "main.tex").exists())
    results = [compile_article(article_dir, env) for article_dir in article_dirs]
    write_report(results)
    failed = [result for result in results if result["status"] != "compiled"]
    if failed:
        print("NWAGU_ARTICLE_MANUSCRIPTS_COMPILE_FAILED")
        print(f"compiled={len(results) - len(failed)}")
        print(f"failed={len(failed)}")
        return 1
    print("NWAGU_ARTICLE_MANUSCRIPTS_COMPILED")
    print(f"compiled={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
