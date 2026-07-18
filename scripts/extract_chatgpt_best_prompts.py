#!/usr/bin/env python3
"""Extract and rank user prompts from local ChatGPT export archives.

The script is intentionally standard-library only. It can read normal OpenAI
export ZIP files and salvage conversation JSON entries from ZIP files whose
central directory is missing, as long as the local file headers include sizes.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import struct
import sys
import zipfile
import zlib
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


CONVERSATION_ENTRY_RE = re.compile(
    r"(^|/)(conversations(-\d+)?|shared_conversations)\.json$", re.IGNORECASE
)

TRIVIAL_RE = re.compile(
    r"^\s*(ok|okay|yes|yep|no|nah|thanks|thank you|continue|go on|proceed|nice|good|sure|done)[.!?\s]*$",
    re.IGNORECASE,
)

WORD_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_'/-]*")

ACTION_TERMS = {
    "analyze",
    "audit",
    "build",
    "classify",
    "compare",
    "convert",
    "create",
    "critique",
    "debug",
    "design",
    "diagnose",
    "distill",
    "draft",
    "evaluate",
    "extract",
    "find",
    "fix",
    "generate",
    "harden",
    "identify",
    "implement",
    "improve",
    "investigate",
    "map",
    "orchestrate",
    "plan",
    "rank",
    "recommend",
    "refactor",
    "research",
    "review",
    "rewrite",
    "scan",
    "score",
    "simulate",
    "study",
    "summarize",
    "synthesize",
    "test",
    "triage",
    "validate",
    "write",
}

DELIVERABLE_TERMS = {
    "acceptance criteria",
    "brief",
    "calendar",
    "checklist",
    "dashboard",
    "doc",
    "essay",
    "framework",
    "json",
    "manifesto",
    "markdown",
    "matrix",
    "outline",
    "pdf",
    "plan",
    "prd",
    "prompt",
    "report",
    "roadmap",
    "rubric",
    "spec",
    "table",
    "template",
    "timeline",
}

QUALITY_TERMS = {
    "accurate",
    "citation",
    "cite",
    "constraints",
    "double check",
    "evidence",
    "metric",
    "must",
    "requirements",
    "score",
    "source",
    "test",
    "verify",
}

PROJECT_TERMS = {
    "agent",
    "ai",
    "archive",
    "beaconos",
    "beaconsmith",
    "bitcoin",
    "citrea",
    "codex",
    "community",
    "enugu",
    "etisiobi",
    "frontend",
    "governance",
    "grok",
    "icegov",
    "memory",
    "nigeria",
    "oroma",
    "pagc",
    "product",
    "research",
    "twitter",
    "x archive",
}

CATEGORY_KEYWORDS = {
    "agent_orchestration": {
        "agent",
        "agents",
        "orchestrate",
        "workflow",
        "loop",
        "swarm",
        "delegate",
        "command center",
        "memory",
        "automation",
    },
    "product_build": {
        "product",
        "prd",
        "mvp",
        "roadmap",
        "feature",
        "release",
        "oroma",
        "beaconos",
        "sagaforge",
        "app",
        "platform",
    },
    "frontend_design": {
        "frontend",
        "ui",
        "ux",
        "design",
        "visual",
        "interface",
        "dashboard",
        "screen",
        "layout",
        "codex grade",
    },
    "research_analysis": {
        "research",
        "paper",
        "study",
        "literature",
        "citation",
        "evidence",
        "icegov",
        "pagc",
        "governance",
        "framework",
    },
    "strategy_operations": {
        "strategy",
        "operations",
        "operating",
        "system",
        "plan",
        "cadence",
        "decision",
        "risk",
        "priority",
        "execution",
    },
    "writing_content": {
        "tweet",
        "thread",
        "essay",
        "article",
        "write",
        "rewrite",
        "story",
        "narrative",
        "content",
        "post",
    },
    "code_debugging": {
        "code",
        "bug",
        "debug",
        "test",
        "repo",
        "script",
        "function",
        "api",
        "error",
        "implement",
    },
    "data_archive": {
        "archive",
        "extract",
        "dataset",
        "csv",
        "json",
        "logs",
        "scan",
        "x archive",
        "twitter",
        "chatgpt",
    },
    "finance_grants": {
        "finance",
        "grant",
        "budget",
        "cash",
        "runway",
        "invoice",
        "funding",
        "sponsor",
        "proposal",
    },
    "personal_meta": {
        "career",
        "profile",
        "bio",
        "personal",
        "voice",
        "identity",
        "persona",
        "style",
        "motif",
    },
}

SENSITIVE_PATTERNS = {
    "possible_email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "possible_phone": re.compile(r"(\+\d{1,3}[\s.-]?)?(\(?\d{3,4}\)?[\s.-]?){2,4}\d{2,4}"),
    "possible_secret": re.compile(
        r"\b(api[_-]?key|secret|password|token|private key|seed phrase|sk-[A-Za-z0-9_-]+)\b",
        re.IGNORECASE,
    ),
    "possible_address": re.compile(r"\b(address|passport|visa|bank|account number|bvn|nin)\b", re.IGNORECASE),
}


@dataclass
class SourceStatus:
    path: str
    mode: str
    entries_seen: int = 0
    conversation_entries: int = 0
    parse_errors: list[str] | None = None

    def add_error(self, message: str) -> None:
        if self.parse_errors is None:
            self.parse_errors = []
        if len(self.parse_errors) < 20:
            self.parse_errors.append(message)


@dataclass
class PromptRecord:
    prompt_id: str
    normalized_hash: str
    score: float
    category: str
    title: str
    create_time: str | None
    update_time: str | None
    conversation_id: str | None
    message_id: str | None
    source_zip: str
    source_entry: str
    word_count: int
    char_count: int
    line_count: int
    privacy_flags: list[str]
    preview: str
    text: str


def normalized_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def stable_hash(text: str) -> str:
    return hashlib.sha256(normalized_text(text).lower().encode("utf-8", "ignore")).hexdigest()


def timestamp_to_iso(value: Any) -> str | None:
    if value in (None, ""):
        return None
    if isinstance(value, str):
        if re.match(r"^\d+(\.\d+)?$", value):
            value = float(value)
        else:
            return value
    if isinstance(value, (int, float)):
        try:
            return dt.datetime.fromtimestamp(value, tz=dt.timezone.utc).isoformat()
        except (OverflowError, OSError, ValueError):
            return None
    return None


def text_from_part(part: Any) -> str:
    if isinstance(part, str):
        return part
    if isinstance(part, dict):
        for key in ("text", "content", "value", "caption", "transcript"):
            value = part.get(key)
            if isinstance(value, str):
                return value
        if part.get("content_type") in {"image_asset_pointer", "audio_asset_pointer", "file_asset_pointer"}:
            return ""
    return ""


def message_text(message: dict[str, Any]) -> str:
    content = message.get("content")
    if isinstance(content, str):
        return normalized_text(content)
    if not isinstance(content, dict):
        return ""

    parts = content.get("parts")
    if isinstance(parts, list):
        text = "\n\n".join(t for t in (text_from_part(part) for part in parts) if t)
        return normalized_text(text)

    for key in ("text", "content", "result"):
        value = content.get(key)
        if isinstance(value, str):
            return normalized_text(value)
    return ""


def iter_conversation_entries(path: Path) -> tuple[SourceStatus, list[tuple[str, bytes]]]:
    entries: list[tuple[str, bytes]] = []
    status = SourceStatus(path=str(path), mode="zipfile")
    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            status.entries_seen = len(infos)
            for info in infos:
                if CONVERSATION_ENTRY_RE.search(info.filename):
                    entries.append((info.filename, archive.read(info)))
                    status.conversation_entries += 1
        return status, entries
    except zipfile.BadZipFile:
        status.mode = "local_header_salvage"
        return salvage_conversation_entries(path, status)
    except Exception as exc:  # pragma: no cover - defensive report path
        status.mode = "zipfile_error"
        status.add_error(f"{type(exc).__name__}: {exc}")
        return status, entries


def salvage_conversation_entries(path: Path, status: SourceStatus) -> tuple[SourceStatus, list[tuple[str, bytes]]]:
    entries: list[tuple[str, bytes]] = []
    local_header = struct.Struct("<IHHHHHIIIHH")
    with path.open("rb") as handle:
        pos = 0
        file_size = path.stat().st_size
        while pos + local_header.size <= file_size:
            handle.seek(pos)
            header_bytes = handle.read(local_header.size)
            if len(header_bytes) < local_header.size:
                break
            (
                signature,
                _version_needed,
                flags,
                method,
                _mtime,
                _mdate,
                _crc32,
                compressed_size,
                _uncompressed_size,
                filename_len,
                extra_len,
            ) = local_header.unpack(header_bytes)

            if signature != 0x04034B50:
                break

            raw_name = handle.read(filename_len)
            filename = raw_name.decode("utf-8", "replace")
            handle.seek(extra_len, 1)
            data_pos = handle.tell()
            status.entries_seen += 1

            if flags & 0x08:
                status.add_error(f"Cannot salvage {filename}: local header uses data descriptor")
                break

            next_pos = data_pos + compressed_size
            if next_pos > file_size:
                status.add_error(f"Cannot salvage {filename}: compressed size exceeds file length")
                break

            if CONVERSATION_ENTRY_RE.search(filename):
                handle.seek(data_pos)
                compressed = handle.read(compressed_size)
                try:
                    if method == 0:
                        raw = compressed
                    elif method == 8:
                        raw = zlib.decompress(compressed, -15)
                    else:
                        status.add_error(f"Unsupported compression method {method} for {filename}")
                        raw = b""
                    if raw:
                        entries.append((filename, raw))
                        status.conversation_entries += 1
                except Exception as exc:
                    status.add_error(f"{filename}: {type(exc).__name__}: {exc}")

            pos = next_pos

    return status, entries


def conversation_list_from_json(raw: bytes, source_label: str) -> list[dict[str, Any]]:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{source_label}: JSON parse failed at {exc.pos}: {exc.msg}") from exc

    candidates: list[Any]
    if isinstance(data, list):
        candidates = data
    elif isinstance(data, dict):
        if isinstance(data.get("conversations"), list):
            candidates = data["conversations"]
        elif isinstance(data.get("items"), list):
            candidates = data["items"]
        elif isinstance(data.get("data"), list):
            candidates = data["data"]
        else:
            candidates = [data]
    else:
        return []

    conversations: list[dict[str, Any]] = []
    for item in candidates:
        if not isinstance(item, dict):
            continue
        if isinstance(item.get("conversation"), dict):
            conversations.append(item["conversation"])
        elif "mapping" in item or "messages" in item:
            conversations.append(item)
    return conversations


def iter_user_messages(conversation: dict[str, Any]) -> Iterable[tuple[str | None, dict[str, Any]]]:
    mapping = conversation.get("mapping")
    messages: list[tuple[str | None, dict[str, Any], float]] = []
    if isinstance(mapping, dict):
        for node_id, node in mapping.items():
            if not isinstance(node, dict):
                continue
            message = node.get("message")
            if not isinstance(message, dict):
                continue
            created = message.get("create_time") or node.get("create_time") or 0
            try:
                sort_key = float(created or 0)
            except (TypeError, ValueError):
                sort_key = 0.0
            messages.append((str(node_id), message, sort_key))
    elif isinstance(conversation.get("messages"), list):
        for index, message in enumerate(conversation["messages"]):
            if isinstance(message, dict):
                created = message.get("create_time") or 0
                try:
                    sort_key = float(created or 0)
                except (TypeError, ValueError):
                    sort_key = float(index)
                messages.append((str(message.get("id") or index), message, sort_key))

    for node_id, message, _sort_key in sorted(messages, key=lambda row: row[2]):
        author = message.get("author")
        role = author.get("role") if isinstance(author, dict) else message.get("role")
        if role == "user":
            yield node_id, message


def is_probably_prompt(text: str) -> bool:
    norm = normalized_text(text)
    if len(norm) < 25:
        return False
    if TRIVIAL_RE.match(norm):
        return False
    if re.fullmatch(r"https?://\S+", norm):
        return False
    if norm.lower() in {"image", "file", "audio", "screenshot"}:
        return False
    return True


def count_terms(lower: str, terms: Iterable[str]) -> int:
    count = 0
    for term in terms:
        if " " in term:
            if term in lower:
                count += 1
        elif re.search(rf"\b{re.escape(term)}\b", lower):
            count += 1
    return count


def score_prompt(text: str) -> float:
    norm = normalized_text(text)
    lower = norm.lower()
    words = WORD_RE.findall(norm)
    word_count = len(words)
    line_count = max(1, norm.count("\n") + 1)
    score = 0.0

    if word_count < 6:
        score -= 60
    elif word_count < 15:
        score += 4
    elif word_count < 40:
        score += 15
    elif word_count < 120:
        score += 28
    elif word_count < 400:
        score += 34
    else:
        score += 28

    if word_count > 1800:
        score -= 12
    if word_count > 4000:
        score -= 22

    action_hits = count_terms(lower, ACTION_TERMS)
    score += min(30, action_hits * 4)

    deliverable_hits = count_terms(lower, DELIVERABLE_TERMS)
    score += min(24, deliverable_hits * 3)

    quality_hits = count_terms(lower, QUALITY_TERMS)
    score += min(20, quality_hits * 3)

    project_hits = count_terms(lower, PROJECT_TERMS)
    score += min(20, project_hits * 3)

    if re.search(r"\b(act as|you are|role:|persona|expert|senior|founder|ceo)\b", lower):
        score += 8
    if re.search(r"\b(context|task|goal|output|format|constraints|examples?|deliverables?)\b", lower):
        score += 9
    if re.search(r"(^|\n)\s*(#{1,4}\s|\d+[.)]\s+|[-*]\s+)", norm):
        score += 9
    if re.search(r"\b(do not|don't|must|should|avoid|without|before|after)\b", lower):
        score += 7
    if re.search(r"\b(json|csv|markdown|table|schema|yaml|checklist|rubric)\b", lower):
        score += 7
    if re.search(r"\b(test|verify|validate|evidence|source|citation|double check)\b", lower):
        score += 8
    if re.search(r"\b(loop|orchestrate|agent|workflow|memory|command center|dashboard)\b", lower):
        score += 8
    if re.search(r"[A-Za-z]:\\|/[\w.-]+/|\.md\b|\.json\b|\.tsx\b|\.py\b|\.zip\b", norm):
        score += 6
    if re.search(r"\b\d{4}-\d{2}-\d{2}\b|\bQ[1-4]\b|\b\d+\s*(day|week|month|hour)s?\b", lower):
        score += 4

    if TRIVIAL_RE.match(norm):
        score -= 80
    if re.search(r"^\s*(continue|proceed|fix it|make it better)\b", lower) and word_count < 25:
        score -= 35
    if line_count > 150 and action_hits < 2:
        score -= 18
    if norm.count("{") + norm.count("}") > 80 and action_hits < 2:
        score -= 15
    if len(re.findall(r"https?://", norm)) > 15 and action_hits < 2:
        score -= 10

    return round(score, 2)


def categorize_prompt(text: str) -> str:
    lower = text.lower()
    scores = {
        category: count_terms(lower, keywords)
        for category, keywords in CATEGORY_KEYWORDS.items()
    }
    best_category, best_score = max(scores.items(), key=lambda item: item[1])
    if best_score == 0:
        return "general_prompting"
    return best_category


def privacy_flags(text: str) -> list[str]:
    return [name for name, pattern in SENSITIVE_PATTERNS.items() if pattern.search(text)]


def short_preview(text: str, limit: int = 240) -> str:
    norm = normalized_text(text)
    if len(norm) <= limit:
        return norm
    return norm[: limit - 1].rstrip() + "..."


def find_candidate_archives(downloads: Path) -> list[Path]:
    candidates: list[Path] = []
    for path in downloads.glob("*.zip"):
        name = path.name.lower()
        if "d6ba99" in name or "chatgpt" in name or "openai" in name:
            candidates.append(path)
    return sorted(candidates, key=lambda p: p.stat().st_mtime, reverse=True)


def extract_prompts(archives: list[Path]) -> tuple[list[PromptRecord], list[SourceStatus], Counter]:
    records_by_hash: dict[str, PromptRecord] = {}
    source_statuses: list[SourceStatus] = []
    counters: Counter = Counter()

    for archive_path in archives:
        status, entries = iter_conversation_entries(archive_path)
        source_statuses.append(status)
        counters["archives_seen"] += 1
        counters["conversation_entries_seen"] += len(entries)

        for entry_name, raw in entries:
            try:
                conversations = conversation_list_from_json(raw, f"{archive_path.name}:{entry_name}")
            except ValueError as exc:
                status.add_error(str(exc))
                counters["entry_parse_errors"] += 1
                continue

            counters["conversations_seen"] += len(conversations)
            for conversation in conversations:
                title = str(conversation.get("title") or "Untitled")
                conversation_id = conversation.get("id") or conversation.get("conversation_id")
                create_time = timestamp_to_iso(conversation.get("create_time"))
                update_time = timestamp_to_iso(conversation.get("update_time"))
                for node_id, message in iter_user_messages(conversation):
                    text = message_text(message)
                    counters["user_messages_seen"] += 1
                    if not is_probably_prompt(text):
                        counters["user_messages_filtered"] += 1
                        continue

                    norm_hash = stable_hash(text)
                    if norm_hash in records_by_hash:
                        counters["duplicate_prompts"] += 1
                        existing = records_by_hash[norm_hash]
                        if existing.create_time is None and timestamp_to_iso(message.get("create_time")):
                            existing.create_time = timestamp_to_iso(message.get("create_time"))
                        continue

                    clean = normalized_text(text)
                    words = WORD_RE.findall(clean)
                    record = PromptRecord(
                        prompt_id=f"cgpt-{len(records_by_hash) + 1:06d}",
                        normalized_hash=norm_hash,
                        score=score_prompt(clean),
                        category=categorize_prompt(clean),
                        title=title,
                        create_time=timestamp_to_iso(message.get("create_time")) or create_time,
                        update_time=timestamp_to_iso(message.get("update_time")) or update_time,
                        conversation_id=str(conversation_id) if conversation_id is not None else None,
                        message_id=str(message.get("id") or node_id) if (message.get("id") or node_id) else None,
                        source_zip=str(archive_path),
                        source_entry=entry_name,
                        word_count=len(words),
                        char_count=len(clean),
                        line_count=max(1, clean.count("\n") + 1),
                        privacy_flags=privacy_flags(clean),
                        preview=short_preview(clean),
                        text=clean,
                    )
                    records_by_hash[norm_hash] = record
                    counters["prompts_kept"] += 1

    records = sorted(records_by_hash.values(), key=lambda item: (-item.score, -item.word_count, item.title))
    for index, record in enumerate(records, start=1):
        record.prompt_id = f"cgpt-{index:06d}"
    return records, source_statuses, counters


def select_best(records: list[PromptRecord], threshold: float, min_count: int, max_count: int) -> list[PromptRecord]:
    selected = [record for record in records if record.score >= threshold]
    if len(selected) < min_count:
        selected = records[:min(min_count, len(records))]
    return selected[:max_count]


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_csv(path: Path, records: list[PromptRecord]) -> None:
    fieldnames = [
        "prompt_id",
        "score",
        "category",
        "title",
        "create_time",
        "word_count",
        "char_count",
        "privacy_flags",
        "source_zip",
        "source_entry",
        "preview",
        "text",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            row = asdict(record)
            row["privacy_flags"] = ";".join(record.privacy_flags)
            writer.writerow({key: row.get(key) for key in fieldnames})


def markdown_escape_fence(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return fence


def write_best_markdown(path: Path, records: list[PromptRecord], generated_at: str) -> None:
    lines = [
        "# ChatGPT Best Prompts",
        "",
        f"Generated: {generated_at}",
        "",
        "Private local extraction from ChatGPT export logs. Prompts are ranked with a heuristic that rewards specificity, reusable structure, deliverables, verification language, and agent/product/research usefulness.",
        "",
        f"Selected prompts: {len(records)}",
        "",
    ]
    for index, record in enumerate(records, start=1):
        flags = ", ".join(record.privacy_flags) if record.privacy_flags else "none"
        lines.extend(
            [
                f"## {index}. {record.title}",
                "",
                f"- ID: `{record.prompt_id}`",
                f"- Score: `{record.score}`",
                f"- Category: `{record.category}`",
                f"- Created: `{record.create_time or 'unknown'}`",
                f"- Words: `{record.word_count}`",
                f"- Privacy flags: `{flags}`",
                f"- Source: `{Path(record.source_zip).name}` / `{record.source_entry}`",
                "",
            ]
        )
        fence = markdown_escape_fence(record.text)
        lines.extend([f"{fence}text", record.text, fence, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_categories_markdown(path: Path, records: list[PromptRecord], generated_at: str) -> None:
    grouped: dict[str, list[PromptRecord]] = defaultdict(list)
    for record in records:
        grouped[record.category].append(record)

    lines = ["# Prompt Categories", "", f"Generated: {generated_at}", ""]
    for category, items in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        lines.extend([f"## {category} ({len(items)})", ""])
        for record in items[:40]:
            lines.append(f"- `{record.prompt_id}` score `{record.score}` - {record.preview}")
        if len(items) > 40:
            lines.append(f"- ... {len(items) - 40} more in best_prompts.json")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_report(
    path: Path,
    records: list[PromptRecord],
    best: list[PromptRecord],
    source_statuses: list[SourceStatus],
    counters: Counter,
    generated_at: str,
    threshold: float,
) -> None:
    category_counts = Counter(record.category for record in best)
    privacy_counts = Counter(flag for record in best for flag in record.privacy_flags)
    lines = [
        "# ChatGPT Prompt Extraction Report",
        "",
        f"Generated: {generated_at}",
        "",
        "## Summary",
        "",
        f"- Archives scanned: {counters['archives_seen']}",
        f"- Conversation JSON entries read: {counters['conversation_entries_seen']}",
        f"- Conversations scanned: {counters['conversations_seen']}",
        f"- User messages seen: {counters['user_messages_seen']}",
        f"- User messages filtered as too small/trivial: {counters['user_messages_filtered']}",
        f"- Duplicate prompts removed: {counters['duplicate_prompts']}",
        f"- Deduped prompt candidates kept: {len(records)}",
        f"- Selected best prompts: {len(best)}",
        f"- Selection threshold: {threshold}",
        "",
        "## Sources",
        "",
    ]

    for status in source_statuses:
        lines.extend(
            [
                f"### {Path(status.path).name}",
                "",
                f"- Mode: `{status.mode}`",
                f"- Entries seen: `{status.entries_seen}`",
                f"- Conversation entries: `{status.conversation_entries}`",
                "",
            ]
        )
        if status.parse_errors:
            lines.append("Errors or limitations:")
            for error in status.parse_errors:
                lines.append(f"- {error}")
            lines.append("")

    lines.extend(["## Selected Categories", ""])
    for category, count in category_counts.most_common():
        lines.append(f"- {category}: {count}")
    lines.append("")

    lines.extend(["## Privacy Flags In Selected Set", ""])
    if privacy_counts:
        for flag, count in privacy_counts.most_common():
            lines.append(f"- {flag}: {count}")
    else:
        lines.append("- none")
    lines.append("")

    lines.extend(
        [
            "## Method Notes",
            "",
            "- Only `user` role messages were extracted.",
            "- Prompts were deduped by normalized SHA-256 hash.",
            "- Ranking is heuristic, not a claim that lower-ranked prompts are unimportant.",
            "- The newest archive may be reported as `local_header_salvage` if its ZIP central directory is missing.",
            "- Full selected prompt text is in `best_prompts.md`, `best_prompts.json`, and `best_prompts.csv`.",
            "- The all-prompts index uses previews, hashes, and metadata rather than dumping every prompt body.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--downloads", type=Path, default=Path.home() / "Downloads")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--threshold", type=float, default=52.0)
    parser.add_argument("--min-count", type=int, default=150)
    parser.add_argument("--max-count", type=int, default=500)
    parser.add_argument("--archive", action="append", type=Path, default=[])
    args = parser.parse_args(argv)

    downloads = args.downloads.expanduser().resolve()
    output_dir = args.out or downloads / f"chatgpt_best_prompts_{dt.date.today().isoformat()}"
    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    archives = [path.expanduser().resolve() for path in args.archive]
    if not archives:
        archives = find_candidate_archives(downloads)

    if not archives:
        print(f"No candidate ChatGPT/OpenAI ZIP exports found in {downloads}", file=sys.stderr)
        return 2

    records, source_statuses, counters = extract_prompts(archives)
    best = select_best(records, args.threshold, args.min_count, args.max_count)
    generated_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")

    write_best_markdown(output_dir / "best_prompts.md", best, generated_at)
    write_json(output_dir / "best_prompts.json", [asdict(record) for record in best])
    write_csv(output_dir / "best_prompts.csv", best)
    write_categories_markdown(output_dir / "prompt_categories.md", best, generated_at)

    write_jsonl(
        output_dir / "all_user_prompts_index.jsonl",
        (
            {
                key: value
                for key, value in asdict(record).items()
                if key not in {"text"}
            }
            for record in records
        ),
    )

    manifest = {
        "generated_at": generated_at,
        "downloads": str(downloads),
        "output_dir": str(output_dir),
        "archives": [str(path) for path in archives],
        "counts": dict(counters),
        "deduped_prompts": len(records),
        "selected_best_prompts": len(best),
        "threshold": args.threshold,
        "min_count": args.min_count,
        "max_count": args.max_count,
        "source_statuses": [asdict(status) for status in source_statuses],
    }
    write_json(output_dir / "manifest.json", manifest)
    write_report(
        output_dir / "extraction_report.md",
        records,
        best,
        source_statuses,
        counters,
        generated_at,
        args.threshold,
    )

    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
