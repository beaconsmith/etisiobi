from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()


SOURCES = [
    {
        "id": "NA-SRC-001",
        "title": "Azuonye 1992 official landing page and local PDF",
        "kind": "primary/academic",
        "status": "verified landing page; local PDF archived",
        "evidence": "Azuonye frames the work as a study of origins, features, significance, mechanics, possibilities, and problems of the Nwagu Aneke Igbo Syllabary.",
        "locator": "ScholarWorks lines 32-55; local research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf",
        "url": "https://scholarworks.umb.edu/africana_faculty_pubs/13/",
        "confidence": 0.92,
        "label": "EXTERNAL+OBSERVED",
        "lane": "source",
    },
    {
        "id": "NA-SRC-002",
        "title": "Azuonye Appendix I chart render",
        "kind": "local source artifact",
        "status": "audited in EXP-0001",
        "evidence": "The rendered chart shows 26 printed consonant rows and 8 vowel columns; f/v is a combined row.",
        "locator": "experiments/EXP-0001-pagc-base-inventory-resolution/analysis.md; corpus/pagc_inventory_observations.jsonl",
        "url": "",
        "confidence": 0.92,
        "label": "OBSERVED",
        "lane": "inventory",
    },
    {
        "id": "NA-SRC-003",
        "title": "Omniglot Nwagu Aneke page",
        "kind": "secondary web reference",
        "status": "web page and local HTML archived",
        "evidence": "Describes the script as a syllabary for Umuleri Igbo, left-to-right, with logographic symbols and no independent vowels.",
        "locator": "Omniglot lines 16-25; local omniglot_nwaguaneke.html",
        "url": "https://www.omniglot.com/writing/nwaguaneke.htm",
        "confidence": 0.82,
        "label": "EXTERNAL",
        "lane": "typology",
    },
    {
        "id": "NA-SRC-004",
        "title": "Ahamefula 2012 USEM article",
        "kind": "academic article",
        "status": "web text located; not locally archived by this script",
        "evidence": "Reports 224 ideal Igbo syllabary symbols, 164 actual Aneke symbols, around 30 multivalent characters, ten duplicate-symbol syllables, and f/v sharing.",
        "locator": "USEM PDF lines 1134-1156 and 1175-1183",
        "url": "https://www.usemjournal.com/pdf/volume-3.pdf",
        "confidence": 0.86,
        "label": "EXTERNAL",
        "lane": "repertoire",
    },
    {
        "id": "NA-SRC-005",
        "title": "Unicode L2/23-203 African scripts update",
        "kind": "standards status",
        "status": "web PDF inspected",
        "evidence": "Lists Nwagu Aneke as an unencoded syllabary with some logographic symbols, written left to right, and notes more than 100 books.",
        "locator": "Unicode PDF lines 311-315",
        "url": "https://www.unicode.org/L2/L2023/23203-update-african-scripts.pdf",
        "confidence": 0.83,
        "label": "EXTERNAL",
        "lane": "digitization",
    },
    {
        "id": "NA-SRC-006",
        "title": "Oxford Handbook of African Languages chapter",
        "kind": "background/prior art",
        "status": "web snippet inspected",
        "evidence": "Places the Nwagu Aneke Igbo syllabary among recent African orthography and writing-system inventions.",
        "locator": "Oxford page line 49",
        "url": "https://academic.oup.com/edited-volume/38608/chapter/334730045",
        "confidence": 0.72,
        "label": "EXTERNAL",
        "lane": "comparative",
    },
]


CLAIMS = [
    {
        "claim": "The research object is not a modifier atlas; it is the Nwagu Aneke script and archive.",
        "status": "READY",
        "evidence": "Repo AGENTS.md and research/pagc/WIKI.md identify PAGC as a program around Nwagu Aneke source-derived structure.",
        "type": "OBSERVED",
    },
    {
        "claim": "The 27-base figure is not source-observed in the chart; it is derived only if f/v is split.",
        "status": "REWRITE_AS_DERIVED",
        "evidence": "EXP-0001 and corpus inventory observations INV-0001 through INV-0004.",
        "type": "EXPERIMENTAL",
    },
    {
        "claim": "Ahamefula adds a richer count problem: 224 ideal syllables vs 164 actual symbols.",
        "status": "NEW_RESEARCH_THREAD",
        "evidence": "USEM article lines 1134-1138; needs local archival and line-verified extraction before becoming a repo claim.",
        "type": "EXTERNAL",
    },
    {
        "claim": "The f/v collapse is not a nuisance; it is a linguistic feature of the Umuleri-specific repertoire.",
        "status": "NEW_RESEARCH_THREAD",
        "evidence": "USEM article lines 1148-1152 plus EXP-0001 f/v row audit.",
        "type": "DERIVED",
    },
    {
        "claim": "Logographs must be modeled as a separate inventory from CV syllabary cells.",
        "status": "READY",
        "evidence": "Omniglot feature list, Azuonye appendix audit, and Ahamefula logograph examples.",
        "type": "DERIVED",
    },
    {
        "claim": "A Unicode/repertoire proposal would require a character inventory, names, glyph sources, usage evidence, and community review.",
        "status": "SPECULATIVE_ONLY",
        "evidence": "Unicode status document says no encoding proposal yet; additional proposal requirements are inferred from standards practice, not proven here.",
        "type": "SPECULATIVE",
    },
]


THREADS = [
    {
        "id": "NA-THREAD-001",
        "title": "Repertoire Reconstruction",
        "question": "Can we reconstruct the actual Aneke symbol repertoire from Azuonye Appendix I/II and Ahamefula's 164-symbol claim?",
        "next": "Convert Appendix I/II into structured CSV: row, vowel, glyph id, reading, duplicate/multivalent flag.",
        "risk": "medium",
        "color": "#7c3aed",
    },
    {
        "id": "NA-THREAD-002",
        "title": "Ideal vs Actual Syllabary Space",
        "question": "Why does Ahamefula say Igbo would require 224 symbols, while the Aneke syllabary has 164?",
        "next": "Model the 224 ideal space and map missing/merged/duplicate cells.",
        "risk": "medium",
        "color": "#0f9f6e",
    },
    {
        "id": "NA-THREAD-003",
        "title": "f/v Collapse",
        "question": "Is f/v sharing an Umuleri phonological economy, an orthographic simplification, or a transcription artifact?",
        "next": "Compare f/v examples in Ahamefula, Azuonye Appendix II, and Igbo/Umuleri phonology sources.",
        "risk": "low",
        "color": "#e11d48",
    },
    {
        "id": "NA-THREAD-004",
        "title": "Logograph Lexicon",
        "question": "Which whole-word symbols exist, and do they form a semantic core of the archive?",
        "next": "Create a logograph ledger from Azuonye Appendix II and Ahamefula examples.",
        "risk": "medium",
        "color": "#d97706",
    },
    {
        "id": "NA-THREAD-005",
        "title": "Manuscript Corpus Access",
        "question": "Where are the 100+ books/exercise books, and can usage examples be ethically studied?",
        "next": "Build a contact/provenance map: University of Nigeria, family/estate, cited project team, archives.",
        "risk": "high",
        "color": "#2563eb",
    },
    {
        "id": "NA-THREAD-006",
        "title": "Digitization and Unicode",
        "question": "What would be required for a defensible digital repertoire, keyboard, font, or Unicode proposal?",
        "next": "Track unencoded-script status and assemble character naming, glyph variation, and evidence requirements.",
        "risk": "high",
        "color": "#0891b2",
    },
    {
        "id": "NA-THREAD-007",
        "title": "Comparative African Syllabaries",
        "question": "How does Nwagu Aneke compare with Vai, Mende Kikakui, Loma, Bété, and Bamum in standardization path?",
        "next": "Create comparison matrix: symbol count, usage corpus, standardization, encoding, pedagogy.",
        "risk": "medium",
        "color": "#9333ea",
    },
]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_html() -> str:
    source_cards = "\n".join(
        f"""
        <article class="source-card {escape(src['lane'])}">
          <div class="card-top">
            <span>{escape(src['label'])}</span>
            <strong>{escape(src['id'])}</strong>
          </div>
          <h3>{escape(src['title'])}</h3>
          <p>{escape(src['evidence'])}</p>
          <small>{escape(src['locator'])}</small>
          {f'<a href="{escape(src["url"])}">source</a>' if src["url"] else ''}
        </article>
        """
        for src in SOURCES
    )
    thread_cards = "\n".join(
        f"""
        <article class="thread-card" style="--accent:{thread['color']}">
          <div class="thread-id">{escape(thread['id'])}</div>
          <h3>{escape(thread['title'])}</h3>
          <p class="question">{escape(thread['question'])}</p>
          <p><strong>Next autonomous move:</strong> {escape(thread['next'])}</p>
          <span class="risk risk-{escape(thread['risk'])}">{escape(thread['risk'])} risk</span>
        </article>
        """
        for thread in THREADS
    )
    claim_rows = "\n".join(
        f"""
        <tr>
          <td>{escape(claim['type'])}</td>
          <td>{escape(claim['claim'])}</td>
          <td>{escape(claim['status'])}</td>
          <td>{escape(claim['evidence'])}</td>
        </tr>
        """
        for claim in CLAIMS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Nwagu Aneke Research Map</title>
  <style>
    :root {{
      --ink: #15111f;
      --muted: #5a556b;
      --paper: #fffaf2;
      --panel: rgba(255, 255, 255, 0.78);
      --line: rgba(21, 17, 31, 0.14);
      --violet: #7c3aed;
      --rose: #e11d48;
      --amber: #d97706;
      --teal: #0891b2;
      --green: #0f9f6e;
      --blue: #2563eb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background:
        radial-gradient(circle at 10% 8%, rgba(124, 58, 237, 0.22), transparent 28rem),
        radial-gradient(circle at 91% 12%, rgba(225, 29, 72, 0.18), transparent 26rem),
        radial-gradient(circle at 72% 92%, rgba(15, 159, 110, 0.18), transparent 28rem),
        linear-gradient(135deg, #fffaf2 0%, #f3fbff 42%, #fff7fb 100%);
      min-height: 100vh;
    }}
    header, main {{ width: min(1180px, calc(100% - 36px)); margin: 0 auto; }}
    header {{ padding: 58px 0 22px; }}
    .hero {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 28px;
      align-items: stretch;
    }}
    h1 {{
      margin: 0;
      font-size: clamp(42px, 7vw, 92px);
      line-height: 0.91;
      letter-spacing: 0;
      max-width: 860px;
    }}
    .lede {{
      margin-top: 22px;
      max-width: 760px;
      color: var(--muted);
      font-size: 20px;
      line-height: 1.55;
    }}
    .formula {{
      display: grid;
      align-content: center;
      gap: 14px;
      border: 1px solid var(--line);
      background: linear-gradient(145deg, rgba(255,255,255,0.82), rgba(255,255,255,0.45));
      border-radius: 28px;
      padding: 26px;
      box-shadow: 0 24px 70px rgba(21, 17, 31, 0.12);
    }}
    .formula strong {{ font-size: 15px; text-transform: uppercase; letter-spacing: 0.12em; color: var(--muted); }}
    .chain {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      font-size: 18px;
      line-height: 1.4;
    }}
    .chain span {{
      border: 1px solid var(--line);
      background: #fff;
      border-radius: 999px;
      padding: 8px 12px;
      white-space: nowrap;
    }}
    section {{ padding: 34px 0; }}
    .section-title {{
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 20px;
      margin-bottom: 16px;
    }}
    .section-title h2 {{ margin: 0; font-size: clamp(28px, 4vw, 48px); line-height: 1; }}
    .section-title p {{ margin: 0; max-width: 520px; color: var(--muted); line-height: 1.5; }}
    .signal-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }}
    .signal {{
      min-height: 144px;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 24px;
      padding: 18px;
      backdrop-filter: blur(12px);
    }}
    .signal b {{ display: block; font-size: 42px; line-height: 1; margin-bottom: 10px; }}
    .signal strong {{ display:block; font-size: 18px; margin-bottom: 8px; }}
    .signal p {{ margin: 0; color: var(--muted); line-height: 1.4; }}
    .sig-1 b {{ color: var(--rose); }}
    .sig-2 b {{ color: var(--violet); }}
    .sig-3 b {{ color: var(--green); }}
    .sig-4 b {{ color: var(--teal); }}
    .research-board {{
      position: relative;
      min-height: 570px;
      border: 1px solid var(--line);
      border-radius: 34px;
      background:
        linear-gradient(rgba(21,17,31,0.055) 1px, transparent 1px),
        linear-gradient(90deg, rgba(21,17,31,0.055) 1px, transparent 1px),
        rgba(255,255,255,0.56);
      background-size: 34px 34px;
      overflow: hidden;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.55), 0 28px 80px rgba(21, 17, 31, 0.12);
    }}
    .node {{
      position: absolute;
      width: 190px;
      min-height: 116px;
      padding: 16px;
      border-radius: 24px;
      color: #fff;
      box-shadow: 0 22px 48px rgba(21, 17, 31, 0.22);
    }}
    .node small {{ display:block; opacity: .78; margin-bottom: 8px; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
    .node strong {{ display:block; font-size: 19px; line-height: 1.05; margin-bottom: 8px; }}
    .node p {{ margin:0; line-height:1.28; opacity:.9; }}
    .n1 {{ left: 6%; top: 11%; background: linear-gradient(135deg, #7c3aed, #a855f7); }}
    .n2 {{ left: 34%; top: 8%; background: linear-gradient(135deg, #2563eb, #0891b2); }}
    .n3 {{ right: 7%; top: 16%; background: linear-gradient(135deg, #0f9f6e, #22c55e); }}
    .n4 {{ left: 14%; top: 56%; background: linear-gradient(135deg, #e11d48, #f97316); }}
    .n5 {{ left: 42%; top: 43%; background: linear-gradient(135deg, #d97706, #facc15); color: #2d1d02; }}
    .n6 {{ right: 8%; top: 58%; background: linear-gradient(135deg, #111827, #4f46e5); }}
    .line {{
      position: absolute;
      height: 3px;
      background: rgba(21, 17, 31, 0.18);
      transform-origin: left center;
      border-radius: 999px;
    }}
    .l1 {{ left: 22%; top: 25%; width: 170px; transform: rotate(-5deg); }}
    .l2 {{ left: 50%; top: 24%; width: 210px; transform: rotate(8deg); }}
    .l3 {{ left: 24%; top: 50%; width: 270px; transform: rotate(22deg); }}
    .l4 {{ left: 58%; top: 49%; width: 230px; transform: rotate(-23deg); }}
    .l5 {{ left: 30%; top: 70%; width: 420px; transform: rotate(-2deg); }}
    .sources {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }}
    .source-card, .thread-card {{
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 24px;
      padding: 18px;
      min-height: 224px;
      box-shadow: 0 16px 38px rgba(21,17,31,.08);
    }}
    .card-top {{
      display:flex;
      justify-content:space-between;
      gap:12px;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .08em;
      margin-bottom: 14px;
    }}
    .source-card h3, .thread-card h3 {{ margin: 0 0 10px; font-size: 21px; line-height: 1.1; }}
    .source-card p, .thread-card p {{ color: var(--muted); line-height: 1.45; }}
    .source-card small {{ display:block; color: #776f85; line-height: 1.35; margin-bottom: 12px; }}
    .source-card a {{ color: var(--violet); font-weight: 750; text-decoration: none; }}
    .threads {{ display:grid; grid-template-columns: repeat(2, 1fr); gap: 14px; }}
    .thread-card {{ border-top: 8px solid var(--accent); }}
    .thread-id {{ color: var(--accent); font-weight: 850; letter-spacing: .08em; font-size: 12px; }}
    .question {{ font-size: 17px; color: var(--ink) !important; }}
    .risk {{ display:inline-flex; border-radius: 999px; padding: 8px 11px; font-weight: 800; font-size: 12px; text-transform: uppercase; }}
    .risk-low {{ background: rgba(15,159,110,.14); color: #047857; }}
    .risk-medium {{ background: rgba(217,119,6,.15); color: #92400e; }}
    .risk-high {{ background: rgba(225,29,72,.13); color: #be123c; }}
    table {{
      width: 100%;
      border-collapse: collapse;
      border: 1px solid var(--line);
      overflow: hidden;
      border-radius: 24px;
      background: rgba(255,255,255,.78);
      box-shadow: 0 16px 38px rgba(21,17,31,.08);
    }}
    th, td {{ text-align: left; padding: 14px; border-bottom: 1px solid var(--line); vertical-align: top; }}
    th {{ font-size: 12px; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); background: rgba(21,17,31,.04); }}
    td {{ line-height: 1.42; }}
    footer {{
      width: min(1180px, calc(100% - 36px));
      margin: 0 auto;
      padding: 38px 0 60px;
      color: var(--muted);
      line-height: 1.5;
    }}
    @media (max-width: 920px) {{
      .hero, .sources, .threads {{ grid-template-columns: 1fr; }}
      .signal-grid {{ grid-template-columns: repeat(2, 1fr); }}
      .research-board {{ min-height: 920px; }}
      .node {{ position: relative; left: auto !important; right: auto !important; top: auto !important; margin: 16px; width: calc(100% - 32px); }}
      .line {{ display:none; }}
    }}
    @media (max-width: 560px) {{
      header, main, footer {{ width: min(100% - 22px, 1180px); }}
      .signal-grid {{ grid-template-columns: 1fr; }}
      th, td {{ display:block; width:100%; }}
      th {{ display:none; }}
      td {{ border-bottom:0; padding-bottom: 7px; }}
      tr {{ display:block; border-bottom:1px solid var(--line); padding: 9px 0; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="hero">
      <div>
        <h1>Nwagu Aneke Research Map</h1>
        <p class="lede">A colorful working map for continuing the research, not closing it: source provenance, symbol inventory, f/v ambiguity, logographs, manuscript access, digitization, and the experiments that can still be run.</p>
      </div>
      <aside class="formula">
        <strong>Research chain</strong>
        <div class="chain">
          <span>Source</span><span>→</span><span>Glyph</span><span>→</span><span>Syllable</span><span>→</span><span>Word</span><span>→</span><span>Manuscript</span><span>→</span><span>Use</span>
        </div>
        <p class="lede" style="font-size:16px;margin:0">The core question is no longer “is it 27?” It is: what repertoire did Aneke actually use, how was it organized, and what evidence is still missing?</p>
      </aside>
    </div>
  </header>
  <main>
    <section>
      <div class="signal-grid">
        <div class="signal sig-1"><b>26</b><strong>Printed rows</strong><p>EXP-0001 chart audit; f/v appears as a combined row.</p></div>
        <div class="signal sig-2"><b>27</b><strong>Derived split</strong><p>Possible only if f/v is separated into two phonemic bases.</p></div>
        <div class="signal sig-3"><b>164</b><strong>Actual symbols</strong><p>Ahamefula reports the Aneke syllabary has 164 symbols.</p></div>
        <div class="signal sig-4"><b>224</b><strong>Ideal space</strong><p>Ahamefula frames this as the symbol count Igbo would require under an ideal syllabary.</p></div>
      </div>
    </section>

    <section>
      <div class="section-title">
        <h2>Evidence Flow</h2>
        <p>Color is used to keep uncertainty visible. Green/blue nodes are usable evidence; rose/amber nodes are unresolved research pressure.</p>
      </div>
      <div class="research-board">
        <div class="line l1"></div><div class="line l2"></div><div class="line l3"></div><div class="line l4"></div><div class="line l5"></div>
        <div class="node n1"><small>Source</small><strong>Azuonye 1992</strong><p>Origins, mechanics, appendices, literacy potential.</p></div>
        <div class="node n2"><small>Chart</small><strong>26 rows × 8 columns</strong><p>Observed display grid; f/v combined.</p></div>
        <div class="node n3"><small>Typology</small><strong>Syllabary + logographs</strong><p>CV signs plus whole-word signs.</p></div>
        <div class="node n4"><small>Contradiction</small><strong>27 and 216 drift</strong><p>Derived normalization cannot masquerade as source fact.</p></div>
        <div class="node n5"><small>New thread</small><strong>164 actual vs 224 ideal</strong><p>Ahamefula opens a deeper repertoire-reconstruction problem.</p></div>
        <div class="node n6"><small>Future</small><strong>Manuscripts and Unicode</strong><p>Needs usage evidence, rights review, community review, and character names.</p></div>
      </div>
    </section>

    <section>
      <div class="section-title">
        <h2>Research Threads</h2>
        <p>These are the autonomous loops that should keep running. Each one has a concrete next move and a risk level.</p>
      </div>
      <div class="threads">{thread_cards}</div>
    </section>

    <section>
      <div class="section-title">
        <h2>Claim Gate</h2>
        <p>Every visual claim keeps its epistemic label. The point is expansion with discipline, not premature theory closure.</p>
      </div>
      <table>
        <thead><tr><th>Label</th><th>Claim</th><th>Status</th><th>Evidence</th></tr></thead>
        <tbody>{claim_rows}</tbody>
      </table>
    </section>

    <section>
      <div class="section-title">
        <h2>Source Cards</h2>
        <p>Only evidence-bearing sources are shown. External pages are leads until mirrored, extracted, and claim-gated locally.</p>
      </div>
      <div class="sources">{source_cards}</div>
    </section>
  </main>
  <footer>
    Generated {TODAY}. This is a research visualization, not a publication claim. It deliberately preserves unresolved questions so the Nwagu Aneke investigation can continue beyond the Phase 5 arXiv gate.
  </footer>
</body>
</html>
"""


def make_markdown() -> str:
    source_lines = "\n".join(
        f"- **{src['id']} {src['title']}** ({src['label']}): {src['evidence']} Locator: {src['locator']} {src['url']}"
        for src in SOURCES
    )
    claim_lines = "\n".join(
        f"| {claim['type']} | {claim['claim']} | {claim['status']} | {claim['evidence']} |"
        for claim in CLAIMS
    )
    thread_lines = "\n".join(
        f"## {thread['id']}: {thread['title']}\n\n**Question:** {thread['question']}\n\n**Next autonomous move:** {thread['next']}\n\n**Risk:** {thread['risk']}\n"
        for thread in THREADS
    )
    return f"""# Nwagu Aneke Research Map

Generated: {TODAY}

This artifact corrects course from a generic modifier atlas to the actual research object: the Nwagu Aneke script, its source trail, its symbol repertoire, and the autonomous research loops still open.

## Core Research Chain

Source -> Glyph -> Syllable -> Word -> Manuscript -> Use -> Standardization

## Current Count Landscape

| Count | Status | Meaning |
|---:|---|---|
| 26 | OBSERVED | Printed consonant rows in the audited chart, with f/v combined. |
| 27 | DERIVED | Possible phonemic count if f/v is split. |
| 164 | EXTERNAL | Ahamefula reports this as the number of actual Aneke symbols. |
| 224 | EXTERNAL | Ahamefula reports this as an ideal Igbo syllabary requirement. |
| 216 | REWRITE | Derived 27 x 8 normalization; not source-observed. |

## Claim Gate

| Label | Claim | Status | Evidence |
|---|---|---|---|
{claim_lines}

## Autonomous Research Threads

{thread_lines}

## Sources

{source_lines}

## Visual Artifact

Open `research/pagc/nwagu_aneke/NWAGU_ANEKE_RESEARCH_MAP.html`.
"""


def make_canvas() -> dict:
    nodes = []
    edges = []
    positions = [
        ("source", "Azuonye 1992\nsource anchor", -580, -220, "#7c3aed"),
        ("chart", "Chart audit\n26 rows x 8 columns", -230, -220, "#2563eb"),
        ("fv", "f/v combined row\n27 only derived", 130, -220, "#e11d48"),
        ("ahamefula", "Ahamefula thread\n164 actual / 224 ideal", -340, 70, "#d97706"),
        ("logographs", "Logograph lexicon\nseparate inventory", 40, 70, "#0f9f6e"),
        ("manuscripts", "100+ books?\nprovenance and access", 410, 70, "#0891b2"),
        ("unicode", "Digitization / Unicode\nunencoded status", 170, 340, "#111827"),
    ]
    for node_id, text, x, y, color in positions:
        nodes.append(
            {
                "id": node_id,
                "type": "text",
                "text": text,
                "x": x,
                "y": y,
                "width": 260,
                "height": 130,
                "color": color,
            }
        )
    for edge_id, from_node, to_node in [
        ("e1", "source", "chart"),
        ("e2", "chart", "fv"),
        ("e3", "chart", "ahamefula"),
        ("e4", "ahamefula", "logographs"),
        ("e5", "logographs", "manuscripts"),
        ("e6", "manuscripts", "unicode"),
        ("e7", "fv", "unicode"),
    ]:
        edges.append(
            {
                "id": edge_id,
                "fromNode": from_node,
                "fromSide": "right",
                "toNode": to_node,
                "toSide": "left",
            }
        )
    return {"nodes": nodes, "edges": edges}


def main() -> None:
    out_dir = ROOT / "research" / "pagc" / "nwagu_aneke"
    html_path = out_dir / "NWAGU_ANEKE_RESEARCH_MAP.html"
    md_path = out_dir / "NWAGU_ANEKE_RESEARCH_MAP.md"
    data_path = ROOT / "corpus" / "nwagu_aneke_research_threads.json"
    obsidian_md = ROOT / "obsidian_vault" / "09_Nwagu_Aneke_Research_Map.md"
    canvas_path = ROOT / "obsidian_vault" / "Canvases" / "Nwagu Aneke Research Map.canvas"

    write_text(html_path, make_html())
    markdown = make_markdown()
    write_text(md_path, markdown)
    write_text(obsidian_md, markdown.replace("# Nwagu Aneke Research Map", "# [[Nwagu Aneke]] Research Map"))
    write_json(data_path, {"generated_at": TODAY, "sources": SOURCES, "claims": CLAIMS, "threads": THREADS})
    write_json(canvas_path, make_canvas())
    print(f"wrote {html_path}")
    print(f"wrote {md_path}")
    print(f"wrote {data_path}")
    print(f"wrote {obsidian_md}")
    print(f"wrote {canvas_path}")


if __name__ == "__main__":
    main()
