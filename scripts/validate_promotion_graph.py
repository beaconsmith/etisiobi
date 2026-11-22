"""Check source-layer non-promotion over the *entire* allowed transition graph.

Read-only and independent of the proof artifact generator. Emits counterexample
paths instead of treating a list of forbidden declarations as an executed gate.
"""
from __future__ import annotations

import argparse
from collections import deque
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RULES = ROOT / "experiments/EXP-APP-003-layer-safety-proof/promotion_rules.json"
SOURCE = "source_observed"


def verify_rules(rules: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    layers = rules.get("layers")
    allowed = rules.get("allowed_promotions")
    forbidden = rules.get("forbidden_promotions")
    if not isinstance(layers, list) or not layers or any(not isinstance(x, str) or not x for x in layers):
        return {"valid": False, "errors": ["layers must be a nonempty list of strings"], "counterexamples": []}
    if len(set(layers)) != len(layers) or SOURCE not in layers:
        errors.append("layer names must be unique and include source_observed")
    if not isinstance(allowed, list) or not isinstance(forbidden, list):
        return {"valid": False, "errors": errors + ["allowed_promotions and forbidden_promotions must be lists"], "counterexamples": []}
    known = set(layers)
    adjacency: dict[str, set[str]] = {layer: set() for layer in layers}
    forbid_pairs: set[tuple[str, str]] = set()
    for i, row in enumerate(forbidden):
        if not isinstance(row, dict) or row.get("from") not in known or row.get("to") not in known:
            errors.append(f"forbidden_promotions[{i}]: unknown layer or malformed rule")
            continue
        forbid_pairs.add((row["from"], row["to"]))
    for i, row in enumerate(allowed):
        if (not isinstance(row, dict) or row.get("from") not in known
                or row.get("to") not in known or not isinstance(row.get("operation"), str)
                or not row["operation"].strip()):
            errors.append(f"allowed_promotions[{i}]: unknown layer or missing operation")
            continue
        src, dst = row["from"], row["to"]
        adjacency[src].add(dst)
        if (src, dst) in forbid_pairs:
            errors.append(f"allowed_promotions[{i}] conflicts with a forbidden promotion: {src} -> {dst}")

    # Reachability is checked for EVERY non-source layer, not just the three
    # layer names mentioned in the existing forbidden list.
    counterexamples: list[dict[str, Any]] = []
    for start in layers:
        if start == SOURCE:
            continue
        queue = deque([(start, [start])])
        visited = {start}
        while queue:
            node, path = queue.popleft()
            if node == SOURCE:
                counterexamples.append({"start": start, "path": path})
                break
            for next_node in sorted(adjacency[node]):
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))
    return {
        "valid": not errors and not counterexamples,
        "layer_count": len(layers),
        "allowed_edge_count": sum(len(v) for v in adjacency.values()),
        "errors": errors,
        "counterexamples": counterexamples,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    args = parser.parse_args(argv)
    try:
        rules = json.loads(args.rules.read_text(encoding="utf-8"))
        if not isinstance(rules, dict):
            raise ValueError("promotion rules root must be an object")
        result = verify_rules(rules)
    except (OSError, ValueError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)], "counterexamples": []}))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
