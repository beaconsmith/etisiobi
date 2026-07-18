from __future__ import annotations

import json
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "security" / "unicode_channel_audit"

SCAN_ROOTS = [
    ROOT / "papers",
    ROOT / "paper",
    ROOT / "research",
    ROOT / "outputs",
    ROOT / "obsidian_vault",
    ROOT / "benchmarks",
]

TEXT_SUFFIXES = {".md", ".tex", ".txt", ".json", ".jsonl", ".csv", ".yaml", ".yml", ".html"}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def classify_char(ch: str) -> str | None:
    cp = ord(ch)
    cat = unicodedata.category(ch)
    if 0xE000 <= cp <= 0xF8FF or 0xF0000 <= cp <= 0xFFFFD or 0x100000 <= cp <= 0x10FFFD:
        return "private_use"
    if 0xE0000 <= cp <= 0xE007F:
        return "tag_character"
    if cat in {"Cf", "Cc"} and ch not in {"\n", "\r", "\t"}:
        return "format_or_control"
    if "ZERO WIDTH" in unicodedata.name(ch, ""):
        return "zero_width"
    return None


def decode_text(path: Path) -> tuple[str, str] | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if data.startswith(b"\xff\xfe"):
        return data.decode("utf-16", errors="replace"), "utf-16-le-bom"
    if data.startswith(b"\xfe\xff"):
        return data.decode("utf-16", errors="replace"), "utf-16-be-bom"
    if data.startswith(b"\xef\xbb\xbf"):
        return data.decode("utf-8-sig", errors="replace"), "utf-8-bom"
    return data.decode("utf-8", errors="replace"), "utf-8"


def scan_file(path: Path) -> tuple[list[dict[str, Any]], str | None]:
    findings: list[dict[str, Any]] = []
    decoded = decode_text(path)
    if decoded is None:
        return findings, None
    text, encoding = decoded
    for index, ch in enumerate(text):
        kind = classify_char(ch)
        if kind is None:
            continue
        line = text.count("\n", 0, index) + 1
        col = index - text.rfind("\n", 0, index)
        findings.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "line": line,
                "column": col,
                "codepoint": f"U+{ord(ch):04X}",
                "name": unicodedata.name(ch, "UNKNOWN"),
                "category": unicodedata.category(ch),
                "risk_class": kind,
            }
        )
    return findings, encoding


def files_to_scan() -> list[Path]:
    files: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if any(part in {".git", "__pycache__", "compile_logs"} for part in path.parts):
                continue
            files.append(path)
    return files


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def main() -> int:
    findings: list[dict[str, Any]] = []
    encodings: Counter[str] = Counter()
    scanned = files_to_scan()
    for path in scanned:
        file_findings, encoding = scan_file(path)
        findings.extend(file_findings)
        if encoding:
            encodings[encoding] += 1

    by_class = Counter(item["risk_class"] for item in findings)
    by_file = Counter(item["path"] for item in findings)
    non_utf8_files = sum(count for encoding, count in encodings.items() if not encoding.startswith("utf-8"))
    result = {
        "generated_at": now(),
        "status": "UNICODE_CHANNEL_AUDIT_COMPLETE",
        "files_scanned": len(scanned),
        "findings": len(findings),
        "encoding_counts": dict(encodings),
        "non_utf8_text_files": non_utf8_files,
        "risk_class_counts": dict(by_class),
        "top_files": dict(by_file.most_common(20)),
        "defensive_interpretation": "Findings are visibility and publication-safety risks, not proof of covert-channel use. UTF-16 files are tracked as portability risks instead of hidden-character findings.",
    }
    write_json(OUT / "unicode_channel_audit.json", result)
    write_json(OUT / "unicode_channel_findings.json", findings[:5000])
    lines = [
        "# Unicode Channel Audit",
        "",
        f"Generated: {result['generated_at']}",
        "",
        f"Files scanned: {result['files_scanned']}",
        f"Findings: {result['findings']}",
        f"Non-UTF-8 text files: {result['non_utf8_text_files']}",
        "",
        "## Encodings",
        "",
    ]
    for key, value in encodings.items():
        lines.append(f"- `{key}`: {value}")
    lines.extend([
        "",
        "## Risk Classes",
        "",
    ])
    for key, value in by_class.items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Interpretation", "", result["defensive_interpretation"]])
    write_text(OUT / "UNICODE_CHANNEL_AUDIT.md", "\n".join(lines))
    print("UNICODE_CHANNEL_AUDIT_COMPLETE")
    print(f"files_scanned={len(scanned)}")
    print(f"findings={len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
