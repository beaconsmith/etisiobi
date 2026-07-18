from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def tex_escape(value: object) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def inventory_table() -> None:
    observations = read_jsonl(ROOT / "corpus" / "pagc_inventory_observations.jsonl")
    selected = [
        row
        for row in observations
        if row.get("inventory_observation_id") in {"INV-0001", "INV-0002", "INV-0003", "INV-0004", "INV-0005", "INV-0006"}
    ]
    lines = [
        r"\begin{table*}[t]",
        r"\small",
        r"\caption{PAGC base-inventory observations used in the audit.}",
        r"\label{tab:inventory}",
        r"\begin{tabular}{p{0.22\linewidth}p{0.10\linewidth}p{0.18\linewidth}p{0.14\linewidth}p{0.20\linewidth}p{0.10\linewidth}}",
        r"\hline",
        r"source & observed count & abstraction level & support strength & contradiction status & decision \\",
        r"\hline",
    ]
    for row in selected:
        lines.append(
            " & ".join(
                [
                    tex_escape(row["source_path"]),
                    tex_escape(row["observed_count"]),
                    tex_escape(row["abstraction_level"]),
                    tex_escape(row["support_strength"]),
                    tex_escape(row["contradiction_status"]),
                    tex_escape(row["decision_effect"]),
                ]
            )
            + r" \\"
        )
    lines.extend([r"\hline", r"\end{tabular}", r"\end{table*}"])
    write_text(ROOT / "paper" / "tables" / "table_inventory.tex", "\n".join(lines))


def claim_gate_summary_table() -> None:
    gate_path = ROOT / "paper" / "claim_gate.json"
    data = json.loads(gate_path.read_text(encoding="utf-8")) if gate_path.exists() else {"summary": {}}
    summary = data.get("summary", {})
    columns = [
        "total_claims",
        "READY",
        "NEEDS_CITATION",
        "NEEDS_EXPERIMENT",
        "CONTRADICTED",
        "REMOVE",
        "REWRITE_AS_LIMITATION",
    ]
    lines = [
        r"\begin{table}[t]",
        r"\small",
        r"\caption{Claim gate summary.}",
        r"\label{tab:claim-gate}",
        r"\begin{tabular}{lrrrrrrr}",
        r"\hline",
        r"total & ready & needs citation & needs experiment & contradicted & removed & rewritten \\",
        r"\hline",
        " & ".join(tex_escape(summary.get(col, 0)) for col in columns) + r" \\",
        r"\hline",
        r"\end{tabular}",
        r"\end{table}",
    ]
    write_text(ROOT / "paper" / "tables" / "table_claim_gate_summary.tex", "\n".join(lines))


def experiment_summary_table() -> None:
    rows = []
    for exp_dir in sorted((ROOT / "experiments").glob("EXP-*")):
        result_path = exp_dir / "results.json"
        if not result_path.exists():
            continue
        data = json.loads(result_path.read_text(encoding="utf-8"))
        if data.get("include_in_phase5_paper") is False:
            continue
        rows.append(
            {
                "experiment": exp_dir.name.split("-", 2)[0] + "-" + exp_dir.name.split("-", 2)[1],
                "purpose": data.get("purpose", "not recorded"),
                "status": data.get("status", "unknown"),
                "result": data.get("decision", data.get("result", "not recorded")),
                "effect": data.get("effect_on_paper", "not recorded"),
            }
        )
    lines = [
        r"\begin{table*}[t]",
        r"\small",
        r"\caption{Experiment summary.}",
        r"\label{tab:experiments}",
        r"\begin{tabular}{p{0.10\linewidth}p{0.23\linewidth}p{0.14\linewidth}p{0.20\linewidth}p{0.24\linewidth}}",
        r"\hline",
        r"experiment & purpose & status & result & effect on paper \\",
        r"\hline",
    ]
    for row in rows:
        lines.append(
            " & ".join(tex_escape(row[col]) for col in ["experiment", "purpose", "status", "result", "effect"])
            + r" \\"
        )
    lines.extend([r"\hline", r"\end{tabular}", r"\end{table*}"])
    write_text(ROOT / "paper" / "tables" / "table_experiment_summary.tex", "\n".join(lines))


def write_csv_assets() -> None:
    observations = read_jsonl(ROOT / "corpus" / "pagc_inventory_observations.jsonl")
    (ROOT / "paper" / "tables").mkdir(parents=True, exist_ok=True)
    with (ROOT / "paper" / "tables" / "inventory_observations.csv").open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "inventory_observation_id",
            "observed_count",
            "source_path",
            "source_locator",
            "abstraction_level",
            "support_strength",
            "contradiction_status",
            "decision_effect",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in observations:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    inventory_table()
    claim_gate_summary_table()
    experiment_summary_table()
    write_csv_assets()
    print("paper assets generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
