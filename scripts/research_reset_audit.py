from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

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
    ".css",
    ".html",
    ".xml",
    ".ttl",
}

NARRATIVE_EXTENSIONS = {
    ".md",
    ".txt",
    ".json",
    ".jsonl",
    ".yaml",
    ".yml",
    ".toml",
    ".csv",
    ".tex",
    ".bib",
}

RESEARCH_EXTENSIONS = TEXT_EXTENSIONS | {".pdf", ".png", ".jpg", ".jpeg", ".svg"}

SOURCE_PATH_RE = re.compile(
    r"(^|/)(library|external_sources/source_notes|research/[^/]+/sources|research/pagc/primary_sources|artifacts|annotations|data|release)(/|$)"
)
GENERATED_PATH_RE = re.compile(
    r"(^|/)(paper|papers/SELECTED_PAPER|outputs|obsidian_vault|autoresearch_runs|research_runs|corpus|exports|ro_crate|visual_atlas|research_goals)(/|$)"
)
WORKING_PATH_RE = re.compile(r"(^|/)(research|experiments|spine|scripts|wiki|benchmarks|sota_methods|systematic_reviews)(/|$)")
QUARANTINE_PATH_RE = re.compile(
    r"(^|/)(quarantine|NS modifier|paper/arxiv_package|papers/SELECTED_PAPER/arxiv_package|outputs/reviewer_packet|autoresearch_runs)(/|$)"
)

CANONICAL_TERMS = [
    "single source of truth",
    "canonical",
    "everything else",
    "start every session",
    "current active",
    "current focus",
    "status:",
    "frozen",
    "submission readiness",
]

OVERCLAIM_TERMS = [
    "universal compression",
    "e6",
    "e₆",
    "principia",
    "genetic-code isomorphism",
    "genetic code isomorphism",
    "proves",
    "provably",
    "validated",
    "27-base",
    "27 base",
    "216-token",
    "216 token",
    "exactly 27",
]

QUALIFIER_TERMS = [
    "false until proven",
    "unproven",
    "hypothesis",
    "speculative",
    "not prove",
    "does not prove",
    "unsupported",
    "blocked",
    "limitation",
    "derived",
    "claim gate",
    "removed",
    "reset",
    "falsification",
]

AGREED_FOUNDATION_PATTERNS = [
    re.compile(r"26\s*(?:x|×|by)\s*8\s*(?:=|equals)?\s*208", re.I),
    re.compile(r"27\s*/\s*216.*derived", re.I),
    re.compile(r"f/v.*split", re.I),
]

STALE_COUNT_PATTERNS = [
    re.compile(r"27[-\s]?base\s*(?:x|×|by)\s*8", re.I),
    re.compile(r"27\s*(?:x|×|by)\s*8.*source", re.I),
    re.compile(r"source[-\s]?derived.*27", re.I),
    re.compile(r"originating from.*27[-\s]?base", re.I),
]

README_CORE = {
    "AGENTS.md",
    "research/AGENTS.md",
    "research/EVIDENCE_POLICY.md",
    "research/CITATION_POLICY.md",
    "research/QUALITY_BAR.md",
    "research/KILL_CRITERIA.md",
    "research/SUBMISSION_RULES.md",
    "research/pagc/PAGC_RESET.md",
    "research/pagc/DERIVED_HYPOTHESIS_CHARTER.md",
    "research/pagc/primary_sources/nwagu_aneke/README.md",
    "wiki/index.md",
}

CONTROL_PLANE_GENERATED = {
    "spine/retrieval_manifest.yaml",
    "spine/events/artifact_event_index.json",
    "spine/events/current_state.json",
    "spine/events/current_state.md",
}

COLLISION_FLAGS = {
    "incomplete_projection",
    "retrieval_risk",
    "stale_count_claim",
    "unqualified_overclaim_language",
}


@dataclass
class Artifact:
    path: str
    size: int
    extension: str
    sha256: str
    text_sha256: str | None = None
    classification: str = "unknown-needs-review"
    confidence: float = 0.0
    reasons: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    canonical_score: int = 0
    reachable: bool = False
    missing_links: list[str] = field(default_factory=list)
    overclaim_hits: list[str] = field(default_factory=list)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            text=True,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout.strip() or result.stderr.strip()
    except OSError:
        return "git unavailable"


def iter_candidate_files() -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in PRUNE_DIRS]
        current = Path(dirpath)
        for filename in filenames:
            path = current / filename
            if path.suffix.lower() in RESEARCH_EXTENSIONS:
                yield path


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
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        try:
            return data.decode("utf-8", errors="replace")
        except UnicodeDecodeError:
            return None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_text_hash(text: str) -> str:
    normalized = re.sub(r"\s+", " ", text.strip().lower())
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def snippet(text: str, start: int, end: int, width: int = 90) -> str:
    left = max(0, start - width // 2)
    right = min(len(text), end + width // 2)
    return re.sub(r"\s+", " ", text[left:right]).strip()


def is_qualified(text: str, start: int, end: int) -> bool:
    window = text[max(0, start - 180) : min(len(text), end + 180)].lower()
    return any(term in window for term in QUALIFIER_TERMS)


def classify(path: Path, text: str | None) -> Artifact:
    r = rel(path)
    artifact = Artifact(
        path=r,
        size=path.stat().st_size,
        extension=path.suffix.lower(),
        sha256=sha256_file(path),
    )
    if text is not None:
        artifact.text_sha256 = normalized_text_hash(text)

    lowered = text.lower() if text else ""
    reasons: list[str] = []
    flags: list[str] = []

    narrative = path.suffix.lower() in NARRATIVE_EXTENSIONS

    if r == "scripts/research_reset_audit.py":
        artifact.classification = "working"
        artifact.confidence = 0.95
        reasons.append("reset-audit tool; code constants are excluded from research-claim classification")
        artifact.reasons = reasons
        return artifact
    if r == "research_reset_audit.md":
        artifact.classification = "generated"
        artifact.confidence = 0.95
        reasons.append("reset-audit output; generated diagnostic report is excluded from canonical collision scoring")
        artifact.reasons = reasons
        return artifact
    elif r in README_CORE:
        artifact.classification = "canonical"
        artifact.confidence = 0.80
        reasons.append("listed in reset-safe canonical control set")
    elif QUARANTINE_PATH_RE.search(r):
        artifact.classification = "quarantine-candidate"
        artifact.confidence = 0.72
        reasons.append("generated package, reviewer output, app, or run output should not be normal retrieval")
    elif GENERATED_PATH_RE.search(r):
        artifact.classification = "generated"
        artifact.confidence = 0.70
        reasons.append("path is a generated projection/output area")
    elif r.startswith("papers/") and path.suffix.lower() == ".pdf":
        artifact.classification = "generated"
        artifact.confidence = 0.90
        reasons.append("compiled manuscript PDF under papers/ is generated output, not source evidence")
    elif SOURCE_PATH_RE.search(r) or path.suffix.lower() == ".pdf":
        artifact.classification = "source"
        artifact.confidence = 0.78
        reasons.append("path/extension indicates source or evidence artifact")
    elif WORKING_PATH_RE.search(r):
        artifact.classification = "working"
        artifact.confidence = 0.62
        reasons.append("path is active research, experiment, script, or wiki workspace")
    else:
        artifact.classification = "unknown-needs-review"
        artifact.confidence = 0.35
        reasons.append("no strong path/content classification rule matched")

    if text and narrative:
        canonical_hits = [term for term in CANONICAL_TERMS if term in lowered]
        artifact.canonical_score = len(canonical_hits)
        if canonical_hits:
            flags.append("claims_authority")
            reasons.append("contains authority/status language: " + ", ".join(canonical_hits[:4]))

        if "stub" in lowered or "needs compiling" in lowered:
            flags.append("incomplete_projection")
            if artifact.classification == "canonical":
                artifact.classification = "working"
                artifact.confidence = max(artifact.confidence, 0.72)
                reasons.append("canonical candidate states it is stub/incomplete")

        stale_count = any(pattern.search(text) for pattern in STALE_COUNT_PATTERNS)
        agreed_count = any(pattern.search(text) for pattern in AGREED_FOUNDATION_PATTERNS)
        if stale_count and not agreed_count and not any(q in lowered for q in QUALIFIER_TERMS):
            flags.append("stale_count_claim")
            artifact.classification = "stale" if artifact.classification != "source" else artifact.classification
            artifact.confidence = max(artifact.confidence, 0.82)
            reasons.append("states 27/216-style count without source/derived qualifier")

        file_level_reset = any(
            phrase in lowered
            for phrase in (
                "all pagc claims are false until proven",
                "does not prove",
                "do not use:",
                "hard gate",
            )
        )
        if not file_level_reset:
            for term in OVERCLAIM_TERMS:
                for match in re.finditer(re.escape(term), lowered):
                    if not is_qualified(lowered, match.start(), match.end()):
                        artifact.overclaim_hits.append(snippet(text, match.start(), match.end()))
                        if len(artifact.overclaim_hits) >= 3:
                            break
                if len(artifact.overclaim_hits) >= 3:
                    break
        if artifact.overclaim_hits:
            flags.append("unqualified_overclaim_language")
            if artifact.classification in {"working", "generated", "unknown-needs-review"}:
                artifact.classification = "do-not-cite"
                artifact.confidence = max(artifact.confidence, 0.80)
            reasons.append("contains overclaim language without nearby reset/limitation qualifier")

    artifact.reachable = is_reachable_by_default(r, artifact)
    if artifact.reachable:
        flags.append("reachable_by_default")
    if artifact.classification in {"generated", "quarantine-candidate", "do-not-cite", "stale"} and artifact.reachable:
        flags.append("retrieval_risk")
        reasons.append("ordinary agent retrieval can reach this non-authoritative artifact")

    artifact.reasons = reasons
    artifact.flags = sorted(set(flags))
    return artifact


def is_reachable_by_default(r: str, artifact: Artifact) -> bool:
    if r.startswith("."):
        return False
    if "/node_modules/" in r or r.startswith("NS modifier/node_modules/"):
        return False
    if artifact.extension in {".map", ".woff", ".woff2"}:
        return False
    return artifact.extension in TEXT_EXTENSIONS and not r.startswith(".git/")


def parse_markdown_links(path: Path, text: str) -> list[str]:
    missing: list[str] = []
    base = path.parent
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for match in link_pattern.finditer(text):
        target = match.group(1).strip()
        if not target or re.match(r"^[a-z]+:", target, re.I):
            continue
        target = target.split("#", 1)[0].strip()
        if not target:
            continue
        target = target.replace("%20", " ")
        candidate = (base / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not candidate.exists():
            missing.append(target)
            if len(missing) >= 20:
                break
    return missing


def gather_artifacts() -> list[Artifact]:
    artifacts: list[Artifact] = []
    for path in sorted(iter_candidate_files(), key=lambda p: rel(p).lower()):
        text = read_text(path)
        artifact = classify(path, text)
        if text and path.suffix.lower() == ".md":
            artifact.missing_links = parse_markdown_links(path, text)
            if artifact.missing_links:
                artifact.flags.append("missing_links")
                artifact.reasons.append(f"{len(artifact.missing_links)} markdown link(s) resolve to missing files")
        artifacts.append(artifact)
    return artifacts


def group_duplicates(artifacts: list[Artifact]) -> tuple[list[list[str]], list[list[str]]]:
    by_sha: dict[str, list[str]] = defaultdict(list)
    by_text_sha: dict[str, list[str]] = defaultdict(list)
    for artifact in artifacts:
        by_sha[artifact.sha256].append(artifact.path)
        if artifact.text_sha256:
            by_text_sha[artifact.text_sha256].append(artifact.path)
    exact = [paths for paths in by_sha.values() if len(paths) > 1]
    text = [paths for paths in by_text_sha.values() if len(paths) > 1]
    exact.sort(key=lambda group: (-len(group), group[0]))
    text.sort(key=lambda group: (-len(group), group[0]))
    return exact, text


def status_contradictions(artifacts: list[Artifact]) -> list[dict[str, str]]:
    checks = [
        ("ICEGOV deadline drift", re.compile(r"(April 24, 2026|Apr 24 2026|May 8, 2026)", re.I)),
        ("submission readiness drift", re.compile(r"(READY_FOR_HUMAN_ARXIV_REVIEW|NOT_READY_[A-Z_]+|NOT_READY_BUT_PAPER_DRAFT_EXISTS)", re.I)),
        ("PAGC count drift", re.compile(r"(26\s*(?:x|×|by)\s*8|27[-\s]?base|27\s*/\s*216|216[-\s]?token|f/v)", re.I)),
        ("E6/universal drift", re.compile(r"(E6|E₆|universal compression|genetic[-\s]?code isomorphism)", re.I)),
    ]
    rows: list[dict[str, str]] = []
    artifact_map = {a.path: a for a in artifacts}
    for label, pattern in checks:
        hits: list[tuple[str, str]] = []
        for artifact in artifacts:
            if artifact.extension not in TEXT_EXTENSIONS:
                continue
            text = read_text(ROOT / artifact.path)
            if not text:
                continue
            for match in pattern.finditer(text):
                hits.append((artifact.path, snippet(text, match.start(), match.end(), width=120)))
                break
        if hits:
            live_hits = [
                (path, snip)
                for path, snip in hits
                if artifact_map[path].classification in {"canonical", "working", "generated", "stale", "do-not-cite"}
            ]
            rows.append(
                {
                    "label": label,
                    "hit_count": str(len(hits)),
                    "live_hit_count": str(len(live_hits)),
                    "examples": json.dumps(live_hits[:8], ensure_ascii=True),
                }
            )
    return rows


def canonical_collisions(artifacts: list[Artifact]) -> list[Artifact]:
    candidates = [
        artifact
        for artifact in artifacts
        if artifact.canonical_score >= 2
        and artifact.classification in {"canonical", "working", "generated", "stale", "do-not-cite"}
        and artifact.reachable
        and artifact.path not in CONTROL_PLANE_GENERATED
        and (
            artifact.classification != "canonical"
            or bool(COLLISION_FLAGS.intersection(artifact.flags))
        )
    ]
    candidates.sort(key=lambda a: (-a.canonical_score, a.path))
    return candidates


def canonical_core(artifacts: list[Artifact]) -> list[Artifact]:
    by_path = {a.path: a for a in artifacts}
    core: list[Artifact] = []
    for path in sorted(README_CORE):
        artifact = by_path.get(path)
        if artifact:
            core.append(artifact)
    return core


def do_not_retrieve(artifacts: list[Artifact]) -> list[Artifact]:
    rows = [
        artifact
        for artifact in artifacts
        if artifact.classification in {"stale", "do-not-cite", "quarantine-candidate"}
        or "retrieval_risk" in artifact.flags
    ]
    rows.sort(key=lambda a: (a.classification, a.path))
    return rows


def stale_projection_candidates(artifacts: list[Artifact]) -> list[Artifact]:
    rows = [
        artifact
        for artifact in artifacts
        if artifact.classification in {"generated", "working", "canonical"}
        and any(flag in artifact.flags for flag in {"claims_authority", "incomplete_projection", "stale_count_claim"})
    ]
    rows.sort(key=lambda a: (-a.canonical_score, a.path))
    return rows


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def table(rows: list[list[str]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(md_escape(str(cell)) for cell in row) + " |")
    return "\n".join(out)


def write_report(path: Path, artifacts: list[Artifact], exit_code: int) -> None:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    branch = run_git(["branch", "--show-current"])
    commit = run_git(["rev-parse", "HEAD"])
    status = run_git(["status", "--short", "--branch"])
    exact_dupes, text_dupes = group_duplicates(artifacts)
    collisions = canonical_collisions(artifacts)
    contradictions = status_contradictions(artifacts)
    core = canonical_core(artifacts)
    do_not = do_not_retrieve(artifacts)
    stale_candidates = stale_projection_candidates(artifacts)
    class_counts = Counter(a.classification for a in artifacts)
    flag_counts = Counter(flag for a in artifacts for flag in a.flags)
    missing_link_count = sum(len(a.missing_links) for a in artifacts)
    overclaim_count = sum(1 for a in artifacts if a.overclaim_hits)

    lines: list[str] = []
    lines.append("# Etisiobi Research Reset Audit")
    lines.append("")
    lines.append("> Read-only audit. This report recommends retrieval and canonical-state changes; it does not move, delete, or rewrite research artifacts.")
    lines.append("")
    lines.append("## Run Metadata")
    lines.append("")
    lines.append(table(
        [
            ["generated_at", now],
            ["git_branch", branch],
            ["git_commit", commit],
            ["exit_code", str(exit_code)],
            ["artifact_count", str(len(artifacts))],
        ],
        ["field", "value"],
    ))
    lines.append("")
    lines.append("## Git Status Snapshot")
    lines.append("")
    lines.append("```text")
    lines.append(status[:12000])
    lines.append("```")
    lines.append("")
    lines.append("## Executive Finding")
    lines.append("")
    if collisions:
        lines.append("Exit status is `2`: multiple reachable artifacts claim canonical or live authority. The repo should not start another broad research-generation pass until normal retrieval is constrained to the canonical core and stale/generated outputs are excluded by default.")
    elif missing_link_count:
        lines.append("Exit status is `3`: the audit completed, but broken links or dependency issues need review before declaring the research state clean.")
    else:
        lines.append("Exit status is `0`: no fatal canonical collision was detected.")
    lines.append("")
    lines.append("The confirmed restart foundation for PAGC-derived applications should be treated as:")
    lines.append("")
    lines.append("```text")
    lines.append("source-observed layer: 26 rows x 8 vowel/modifier columns = 208 records")
    lines.append("derived-operational layer: 27 / 216 only when the f/v row is split")
    lines.append("research target: applications and systems that preserve the source/derived distinction")
    lines.append("```")
    lines.append("")
    lines.append("## Classification Summary")
    lines.append("")
    lines.append(table([[k, str(v)] for k, v in sorted(class_counts.items())], ["classification", "count"]))
    lines.append("")
    lines.append("## Flag Summary")
    lines.append("")
    lines.append(table([[k, str(v)] for k, v in sorted(flag_counts.items())], ["flag", "count"]))
    lines.append("")
    lines.append("## CANONICAL_CORE")
    lines.append("")
    lines.append("Smallest safe core for ordinary agent retrieval during the reset. Some entries may still need line-level edits later, but they are the right control plane.")
    lines.append("")
    lines.append(table(
        [[a.path, a.classification, f"{a.confidence:.2f}", "; ".join(a.reasons[:3])] for a in core],
        ["path", "class", "confidence", "reason"],
    ))
    lines.append("")
    lines.append("## Canonical Authority Collisions")
    lines.append("")
    if collisions:
        lines.append(table(
            [[a.path, a.classification, str(a.canonical_score), ", ".join(a.flags), "; ".join(a.reasons[:3])] for a in collisions[:80]],
            ["path", "class", "authority_score", "flags", "reason"],
        ))
    else:
        lines.append("No reachable canonical authority collisions detected.")
    lines.append("")
    lines.append("## Contradiction Scan")
    lines.append("")
    if contradictions:
        lines.append(table(
            [[row["label"], row["hit_count"], row["live_hit_count"], row["examples"][:800]] for row in contradictions],
            ["check", "hits", "reachable/live hits", "examples"],
        ))
    else:
        lines.append("No tracked contradiction markers found.")
    lines.append("")
    lines.append("## DO_NOT_RETRIEVE_BY_DEFAULT")
    lines.append("")
    lines.append("These artifacts may remain historically valuable, but ordinary research agents should not use them as live evidence or current belief state.")
    lines.append("")
    lines.append(table(
        [[a.path, a.classification, f"{a.confidence:.2f}", ", ".join(a.flags), "; ".join(a.reasons[:3])] for a in do_not[:250]],
        ["path", "class", "confidence", "flags", "reason"],
    ))
    if len(do_not) > 250:
        lines.append("")
        lines.append(f"_Truncated in report: {len(do_not) - 250} additional do-not-retrieve candidates._")
    lines.append("")
    lines.append("## Stale Projection Candidates")
    lines.append("")
    lines.append(table(
        [[a.path, a.classification, str(a.canonical_score), ", ".join(a.flags), "; ".join(a.reasons[:3])] for a in stale_candidates[:120]],
        ["path", "class", "authority_score", "flags", "reason"],
    ))
    lines.append("")
    lines.append("## Duplicate And Copy Risk")
    lines.append("")
    lines.append(f"- Exact duplicate groups: {len(exact_dupes)}")
    lines.append(f"- Text-normalized duplicate groups: {len(text_dupes)}")
    lines.append("")
    if exact_dupes[:20]:
        lines.append("### Exact Duplicate Examples")
        lines.append("")
        lines.append(table([[str(len(group)), "; ".join(group[:6])] for group in exact_dupes[:20]], ["count", "paths"]))
        lines.append("")
    if text_dupes[:20]:
        lines.append("### Text-Normalized Duplicate Examples")
        lines.append("")
        lines.append(table([[str(len(group)), "; ".join(group[:6])] for group in text_dupes[:20]], ["count", "paths"]))
        lines.append("")
    lines.append("## Missing Link Risk")
    lines.append("")
    link_rows = [a for a in artifacts if a.missing_links]
    if link_rows:
        lines.append(table(
            [[a.path, str(len(a.missing_links)), "; ".join(a.missing_links[:8])] for a in link_rows[:120]],
            ["path", "missing_count", "examples"],
        ))
        if len(link_rows) > 120:
            lines.append("")
            lines.append(f"_Truncated in report: {len(link_rows) - 120} additional files with missing links._")
    else:
        lines.append("No missing markdown links found by the local resolver.")
    lines.append("")
    lines.append("## Overclaim Language Risk")
    lines.append("")
    overclaim_rows = [a for a in artifacts if a.overclaim_hits]
    if overclaim_rows:
        lines.append(table(
            [[a.path, a.classification, " / ".join(a.overclaim_hits[:2])] for a in overclaim_rows[:120]],
            ["path", "class", "example"],
        ))
        if len(overclaim_rows) > 120:
            lines.append("")
            lines.append(f"_Truncated in report: {len(overclaim_rows) - 120} additional overclaim-risk files._")
    else:
        lines.append("No unqualified overclaim language detected by the configured patterns.")
    lines.append("")
    lines.append("## Full Artifact Classification")
    lines.append("")
    lines.append("Confidence is rule-based. It is not a scientific truth label; it tells the next reviewer how strongly the audit can classify the file from path, content, and retrieval-risk evidence.")
    lines.append("")
    full_rows = []
    for a in artifacts:
        full_rows.append([
            a.path,
            a.classification,
            f"{a.confidence:.2f}",
            ", ".join(a.flags),
            "; ".join(a.reasons[:4]),
        ])
    lines.append(table(full_rows, ["path", "class", "confidence", "flags", "reasons"]))
    lines.append("")
    lines.append("## Recommended Next Action")
    lines.append("")
    lines.append("1. Treat `CANONICAL_CORE` as the only normal retrieval set for the next research restart pass.")
    lines.append("2. Add retrieval metadata or an allowlist so `DO_NOT_RETRIEVE_BY_DEFAULT` artifacts cannot be used as live claims.")
    lines.append("3. Update stale root instructions that still present 27-base/E6/universal-compression work as current live truth.")
    lines.append("4. Start the first flagship experiment only after the stale-retrieval gate passes: Layered Symbolic Systems source-only vs flattened-derived vs layered representations.")
    lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only reset audit for Etisiobi research state.")
    parser.add_argument("--output", default="research_reset_audit.md", help="Audit report path relative to repo root.")
    args = parser.parse_args()

    artifacts = gather_artifacts()
    collisions = canonical_collisions(artifacts)
    unreadable_high_risk = [a for a in artifacts if a.classification == "unknown-needs-review" and a.size > 5_000_000]
    missing_link_count = sum(len(a.missing_links) for a in artifacts)

    if collisions:
        exit_code = 2
    elif missing_link_count:
        exit_code = 3
    elif unreadable_high_risk:
        exit_code = 4
    else:
        exit_code = 0

    output = (ROOT / args.output).resolve()
    output.relative_to(ROOT.resolve())
    write_report(output, artifacts, exit_code)
    print(f"wrote {output}")
    print(f"artifacts={len(artifacts)} exit_code={exit_code}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
