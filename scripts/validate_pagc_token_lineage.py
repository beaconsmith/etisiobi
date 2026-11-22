"""Validate PAGC token lineage, not merely layer-qualified identifiers.

Independent of the EXP-APP-003 generator. Read-only. Verifies the shape and
parentage of source, derived and domain-mapped *research objects*; it does not
authenticate the underlying historical manuscript or any community authority.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
APP1 = ROOT / "experiments" / "EXP-APP-001-count-layer-design-grammar"
APP2 = ROOT / "experiments" / "EXP-APP-002-governance-state-grammar"
SOURCE_PATH = APP1 / "tokens_source_layer.jsonl"
DERIVED_PATH = APP1 / "tokens_derived_layer.jsonl"
DOMAIN_PATH = APP2 / "governance_state_tokens.jsonl"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        item = json.loads(line)
        if not isinstance(item, dict):
            raise ValueError(f"{path}:{line_no} is not an object")
        rows.append(item)
    return rows


def validate_lineage(
    source: list[dict[str, Any]],
    derived: list[dict[str, Any]],
    domain: list[dict[str, Any]],
) -> dict[str, Any]:
    errors: list[str] = []
    canonical: dict[str, dict[str, Any]] = {}
    source_ids: set[str] = set()

    for i, row in enumerate(source):
        loc = f"source[{i}]"
        if row.get("layer") != "source_observed" or row.get("source_observed") is not True:
            errors.append(f"{loc}: source classification must be source_observed with source_observed=true")
        bmc = row.get("source_bmc_id")
        token = row.get("token_id")
        if not isinstance(bmc, str) or not bmc or not isinstance(token, str) or not token:
            errors.append(f"{loc}: missing source_bmc_id or token_id")
            continue
        if bmc in canonical or token in source_ids:
            errors.append(f"{loc}: duplicate source identity")
        canonical[bmc] = row
        source_ids.add(token)

    derived_ids: set[str] = set()
    children: dict[str, list[dict[str, Any]]] = defaultdict(list)
    carried = 0
    splits = 0
    for i, row in enumerate(derived):
        loc = f"derived[{i}]"
        if row.get("layer") != "derived_fv_split" or row.get("source_observed") is not False:
            errors.append(f"{loc}: derived classification must be derived_fv_split with source_observed=false")
        token = row.get("token_id")
        if not isinstance(token, str) or not token:
            errors.append(f"{loc}: missing token_id")
        elif token in derived_ids:
            errors.append(f"{loc}: duplicate derived token identity {token}")
        else:
            derived_ids.add(token)
        parent_id = row.get("source_bmc_id")
        if not isinstance(parent_id, str) or parent_id not in canonical:
            errors.append(f"{loc}: missing or unrecognized source parent {parent_id!r}")
            continue
        parent = canonical[parent_id]
        children[parent_id].append(row)
        same = all(row.get(key) == parent.get(key) for key in ("token_id", "base", "modifier", "reading"))
        if same:
            carried += 1
            if row.get("derived_rule"):
                errors.append(f"{loc}: unchanged carry-through must not claim an explicit split")
            continue
        splits += 1
        base = row.get("base")
        valid_split = (
            parent.get("base") == "f/v"
            and base in ("f", "v")
            and row.get("modifier") == parent.get("modifier")
            and row.get("token_id") == f"{parent['token_id']}-{base}"
            and row.get("reading") == f"{base}{parent['modifier']}"
            and row.get("derived_rule") == "split f/v row into f and v"
        )
        if not valid_split:
            errors.append(f"{loc}: transformed child lacks a valid f/v split lineage")

    for parent_id, parent in canonical.items():
        rows = children.get(parent_id, [])
        if parent.get("base") == "f/v":
            if len(rows) != 2 or {row.get("base") for row in rows} != {"f", "v"}:
                errors.append(f"{parent_id}: combined f/v source requires exactly two f/v children")
        elif len(rows) != 1 or rows[0].get("token_id") != parent.get("token_id"):
            errors.append(f"{parent_id}: ordinary source requires exactly one unchanged child")

    domain_ids: set[str] = set()
    for i, row in enumerate(domain):
        loc = f"domain[{i}]"
        if row.get("layer") != "domain_mapped_from_pagc_count_layer":
            errors.append(f"{loc}: incorrect domain-mapped layer")
        if row.get("source_observed") is True:
            errors.append(f"{loc}: domain analogy cannot assert source_observed=true")
        if row.get("evidence_status") != "derived_design_hypothesis":
            errors.append(f"{loc}: domain mapping cannot be promoted beyond a design hypothesis here")
        token = row.get("token_id")
        if not isinstance(token, str) or not token or token in domain_ids:
            errors.append(f"{loc}: duplicate/missing domain token identity")
        else:
            domain_ids.add(token)
        if not isinstance(row.get("source"), str) or not row["source"].strip():
            errors.append(f"{loc}: missing domain design reference")

    return {
        "valid": not errors,
        "counts": {
            "source_observed": len(source),
            "derived_fv_split": len(derived),
            "derived_carry_through": carried,
            "derived_explicit_fv_split": splits,
            "domain_mapped_design_hypotheses": len(domain),
        },
        "errors": errors,
        "scope": "internal_token_representation_not_primary_source_authentication",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_PATH)
    parser.add_argument("--derived", type=Path, default=DERIVED_PATH)
    parser.add_argument("--domain", type=Path, default=DOMAIN_PATH)
    args = parser.parse_args(argv)
    try:
        result = validate_lineage(read_jsonl(args.source), read_jsonl(args.derived), read_jsonl(args.domain))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
