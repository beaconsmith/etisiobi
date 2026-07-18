from __future__ import annotations

import csv
import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
SELECTED = ROOT / "papers" / "SELECTED_PAPER"


def clean(text: str) -> str:
    stripped = dedent(text).strip()
    return "\n".join(line[8:] if line.startswith("        ") else line for line in stripped.splitlines())


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(text) + "\n", encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tex_escape(value: object) -> str:
    text = str(value)
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
    return "".join(replacements.get(ch, ch) for ch in text)


def table_tex(path: Path, headers: list[str], rows: list[list[object]], caption: str, label: str) -> None:
    align = "|".join(["p{0.22\\linewidth}"] * len(headers))
    header = " & ".join(tex_escape(h) for h in headers) + r" \\"
    body = "\n".join(" & ".join(tex_escape(cell) for cell in row) + r" \\" for row in rows)
    write_text(
        path,
        f"""
        \\begin{{table*}}[t]
        \\caption{{{tex_escape(caption)}}}
        \\label{{{label}}}
        \\small
        \\begin{{tabular}}{{|{align}|}}
        \\hline
        {header}
        \\hline
        {body}
        \\hline
        \\end{{tabular}}
        \\end{{table*}}
        """,
    )


def generate(selected_dir: Path = SELECTED) -> None:
    bmc = read_jsonl(ROOT / "corpus" / "base_modifier_cache.jsonl")
    count = read_json(ROOT / "corpus" / "bmc_count_reconciliation.json")
    local_sota = read_json(ROOT / "external_sources" / "local_vs_sota_comparison.json")
    claim_gate = read_jsonl(ROOT / "corpus" / "bmc_claim_gate.jsonl")
    completion = read_json(ROOT / "research_goals" / "bmc" / "completion_audit.json")

    table_dir = selected_dir / "tables"
    fig_dir = selected_dir / "figures"
    table_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)

    with (table_dir / "table1_bmc_inventory.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["artifact", "count", "evidence"])
        writer.writerow(["BMC records", len(bmc), "corpus/base_modifier_cache.jsonl"])
        writer.writerow(["Row labels", count["checks"]["bmc_rows"], "TEI rows and glyph annotations"])
        writer.writerow(["Vowel modifiers", count["checks"]["bmc_vowels"], "TEI vowel inventory"])
        writer.writerow(["BMC object KG nodes", read_json(ROOT / "corpus" / "bmc_hyperloop_result.json")["kg_bmc_object_nodes"], "knowledge_graph/bmc_kg.jsonld"])

    table_tex(
        table_dir / "table1_bmc_inventory.tex",
        ["Artifact", "Count", "Evidence"],
        [
            ["BMC records", len(bmc), "base_modifier_cache.jsonl"],
            ["Row labels", count["checks"]["bmc_rows"], "TEI + glyph annotations"],
            ["Vowel modifiers", count["checks"]["bmc_vowels"], "TEI vowel inventory"],
            ["KG BMC nodes", 208, "bmc_kg.jsonld"],
        ],
        "BMC artifact inventory generated from repo-local evidence.",
        "tab:bmc-inventory",
    )

    table_tex(
        table_dir / "table2_count_layers.tex",
        ["Layer", "Count", "Evidence locator", "Interpretation"],
        [
            ["Source rows", 26, "bmc_count_reconciliation.json", "printed row layer"],
            ["Source vowels", 8, "bmc_count_reconciliation.json", "observed modifier columns"],
            ["Source cells", 208, "BMC records", "26 x 8"],
            ["Derived rows", 27, "f/v split rule", "derived, not source-observed"],
            ["Derived cells", 216, "27 x 8", "derived normalization"],
        ],
        "Count-layer reconciliation: source layer versus derived f/v split layer.",
        "tab:count-layers",
    )

    table_tex(
        table_dir / "table3_local_vs_sota.tex",
        ["Dimension", "External baseline", "Local capability", "Gap"],
        [
            [row["dimension"], row["external_baseline"], row["local_capability"], row["local_gap"]]
            for row in local_sota["dimensions"][:8]
        ],
        "Local-vs-SOTA comparison against external standards and prior work.",
        "tab:local-sota",
    )

    status_counts: dict[str, int] = {}
    for row in claim_gate:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1
    table_tex(
        table_dir / "table4_claim_gate.tex",
        ["Claim status", "Count", "Meaning"],
        [[status, count, "BMC claim-gate outcome"] for status, count in sorted(status_counts.items())],
        "BMC claim gate summary.",
        "tab:claim-gate",
    )

    table_tex(
        table_dir / "table5_autoresearch.tex",
        ["Goal", "Decision", "Experiment"],
        [[row["goal_id"], row["decision"], row["experiment"]] for row in completion["goals"]],
        "Autoresearch/BMC experiment decisions.",
        "tab:autoresearch-decisions",
    )

    write_text(
        fig_dir / "figure1_bmc_pipeline.tex",
        r"""
        \begin{figure*}[t]
        \caption{BMC pipeline from source evidence to manuscript claim gate.}
        \label{fig:bmc-pipeline}
        \centering
        \fbox{\begin{minipage}{0.95\linewidth}\centering
        Source artifacts $\rightarrow$ IIIF/TEI locators $\rightarrow$ glyph and cell annotations $\rightarrow$ Base Modifier Cache $\rightarrow$ certainty/provenance/lineage $\rightarrow$ knowledge graph $\rightarrow$ claim gate $\rightarrow$ manuscript decision
        \end{minipage}}
        \end{figure*}
        """,
    )
    write_text(
        fig_dir / "figure2_count_layers.tex",
        r"""
        \begin{figure}[t]
        \caption{Count-layer model.}
        \label{fig:count-layers}
        \centering
        \fbox{\begin{minipage}{0.88\linewidth}\centering
        Source layer: $26 \times 8 = 208$\\[3pt]
        Derived layer: split f/v $\Rightarrow 27 \times 8 = 216$\\[3pt]
        Rule: do not report 27 or 216 as source-observed.
        \end{minipage}}
        \end{figure}
        """,
    )
    write_text(
        fig_dir / "figure3_autoresearch_loop.tex",
        r"""
        \begin{figure}[t]
        \caption{Publication autoresearch loop.}
        \label{fig:autoresearch-loop}
        \centering
        \fbox{\begin{minipage}{0.88\linewidth}\centering
        hypothesis $\rightarrow$ evidence $\rightarrow$ comparison/experiment $\rightarrow$ score $\rightarrow$ keep/revise/reject $\rightarrow$ manuscript patch
        \end{minipage}}
        \end{figure}
        """,
    )
    write_text(
        fig_dir / "bmc_standard_mapping_graph.tex",
        r"""
        \begin{figure*}[t]
        \caption{BMC mapped to external scholarly infrastructure standards.}
        \label{fig:standard-map}
        \centering
        \fbox{\begin{minipage}{0.95\linewidth}\centering
        BMC record links IIIF Canvas/TEI locator, Web Annotation-style body-target semantics, PROV-O activity/entity/agent traces, RO-Crate packaging, FAIR/DataCite release metadata, and CIDOC-CRM-ready cultural heritage relations.
        \end{minipage}}
        \end{figure*}
        """,
    )
    write_text(
        fig_dir / "bmc_standard_mapping_graph.md",
        """
        # BMC Standard Mapping Graph

        ```mermaid
        graph LR
          Source["Source artifact"] --> IIIF["IIIF Canvas"]
          Source --> TEI["TEI locator"]
          IIIF --> BMC["BMC record"]
          TEI --> BMC
          BMC --> WA["Web Annotation shape"]
          BMC --> PROV["PROV-O trace"]
          BMC --> RO["RO-Crate package"]
          BMC --> FAIR["FAIR/DataCite metadata"]
          BMC --> CIDOC["CIDOC CRM mapping"]
          BMC --> Gate["Claim gate"]
          Gate --> Paper["Manuscript decision"]
        ```
        """,
    )
    print(f"publication assets generated in {selected_dir}")


if __name__ == "__main__":
    generate()
