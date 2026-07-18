from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = [
    ROOT / "papers" / "nwagu_aneke_articles",
    ROOT / "papers" / "nwagu_aneke_articles_cycle2",
]


def now() -> str:
    return datetime.now().astimezone().replace(microsecond=0).isoformat()


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def article_dirs(package: Path) -> list[Path]:
    return sorted(path for path in package.iterdir() if path.is_dir() and path.name[:3].isdigit())


def rewrite_manifest(package: Path) -> None:
    manifest_path = package / "manifest.json"
    if not manifest_path.exists():
        return
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["status"] = "QUARANTINED_AI_TO_AI_PROCESS_TRACES_NOT_PAPER_CANDIDATES"
    data["arxiv_quality_status"] = "FAILED_ARXIV_QUALITY_GATE"
    data["allowed_use"] = "negative examples, process archaeology, validator hardening, and branch selection only"
    for article in data.get("articles", []):
        if isinstance(article, dict):
            article["readiness_status"] = "QUARANTINED_NOT_PAPER_CANDIDATE"
    write_json(manifest_path, data)


def rewrite_approved_metadata(article_dir: Path) -> None:
    path = article_dir / "approved_paper.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    data["status"] = "QUARANTINED_GENERATED_PROCESS_TRACE_NOT_PAPER_CANDIDATE"
    data["arxiv_quality_status"] = "FAILED_ARXIV_QUALITY_GATE"
    data["not_paper_candidate"] = True
    data["reason"] = "Internal/generated process artifact; not arXiv-quality and not a paper candidate."
    write_json(path, data)


def main() -> int:
    stamped = []
    for package in PACKAGES:
        if not package.exists():
            continue
        if package.name == "nwagu_aneke_articles_cycle2":
            rewrite_manifest(package)
        package_status = {
            "status": "NOT_ARXIV_QUALITY_GENERATED_WORKING_DRAFTS",
            "created_at": now(),
            "reason": "The package passed internal structure gates but failed the arXiv-quality gate as AI-to-AI/internal process writing without substantive article-specific results.",
            "quality_gate": "python scripts\\validate_arxiv_quality_gate.py",
            "allowed_use": [
                "internal branch notes",
                "source for selecting one real submission candidate",
                "negative examples for validator hardening",
            ],
            "not_allowed_use": [
                "arXiv submission",
                "impact-journal submission",
                "public release as research papers",
                "evidence that Etisiobi has 20 submission-quality papers",
            ],
        }
        write_json(package / "arxiv_quality_status.json", package_status)
        stamped.append(package.relative_to(ROOT).as_posix())
        for article_dir in article_dirs(package):
            if package.name == "nwagu_aneke_articles_cycle2":
                rewrite_approved_metadata(article_dir)
            write_json(
                article_dir / "arxiv_quality_status.json",
                {
                    "status": "NOT_ARXIV_QUALITY_GENERATED_WORKING_DRAFT",
                    "created_at": now(),
                    "reason": "Generated/internal approval artifact. Requires substantive experiment, external prior art, source/rights review, and manuscript rewrite before any submission lane.",
                    "next_gate": "python scripts\\validate_arxiv_quality_gate.py",
                },
            )
    print("GENERATED_PAPERS_MARKED_NOT_ARXIV_QUALITY")
    for item in stamped:
        print(item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
