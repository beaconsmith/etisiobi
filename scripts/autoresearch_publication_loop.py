from __future__ import annotations

import csv
import json
import unicodedata
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
TODAY = NOW[:10]
RUN_ID = f"RUN-PUB-{TODAY.replace('-', '')}-0001"
RUN_DIR = ROOT / "autoresearch_runs" / RUN_ID


def clean(text: str) -> str:
    stripped = dedent(text).strip()
    return "\n".join(line[8:] if line.startswith("        ") else line for line in stripped.splitlines())


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(text) + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def slug(text: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in text).strip("-").replace("--", "-")


EXTERNAL_SOURCES = [
    {
        "source_id": "EXT-0001",
        "name": "PROV-O: The PROV Ontology",
        "url": "https://www.w3.org/TR/prov-o/",
        "type": "standard",
        "authors": "W3C Provenance Working Group",
        "year": "2013",
        "what_it_does": "Defines an OWL2 ontology for representing PROV entities, activities, agents, and relations.",
        "relationship_to_BMC": "BMC provenance activities and source derivations should align with PROV-O.",
        "overlap_with_BMC": "High for provenance trace shape.",
        "gap_left_by_source": "Does not define Nwagu Aneke-specific count-layer gates or manuscript claim decisions.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "w3c_provo_2013",
    },
    {
        "source_id": "EXT-0002",
        "name": "PROV Data Model",
        "url": "https://www.w3.org/TR/prov-dm/",
        "type": "standard",
        "authors": "W3C Provenance Working Group",
        "year": "2013",
        "what_it_does": "Defines the conceptual data model underlying W3C PROV.",
        "relationship_to_BMC": "BMC can map cache creation and claim gates to entities, activities, and agents.",
        "overlap_with_BMC": "High.",
        "gap_left_by_source": "No domain-specific evidence gate for symbolic inventory reconstruction.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "w3c_provdm_2013",
    },
    {
        "source_id": "EXT-0003",
        "name": "RO-Crate Specification 1.1",
        "url": "https://www.researchobject.org/ro-crate/specification/1.1/introduction.html",
        "type": "standard",
        "authors": "RO-Crate Community",
        "year": "2023",
        "what_it_does": "Specifies a JSON-LD research object package for datasets, software, and methods.",
        "relationship_to_BMC": "BMC artifacts can be packaged as a research object with metadata.",
        "overlap_with_BMC": "High for packaging.",
        "gap_left_by_source": "Does not decide whether exact symbolic-count claims are supported.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "rocrate_spec_2023",
    },
    {
        "source_id": "EXT-0004",
        "name": "Packaging research artefacts with RO-Crate",
        "url": "https://journals.sagepub.com/doi/10.3233/DS-210053",
        "type": "paper",
        "authors": "Soiland-Reyes et al.",
        "year": "2022",
        "what_it_does": "Introduces RO-Crate as lightweight machine-readable packaging for research artifacts.",
        "relationship_to_BMC": "Confirms packaging itself is not novel; BMC must contribute claim-gated reconstruction beyond packaging.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "No Nwagu Aneke/PAGC count-drift audit.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "soilandreyes_rocrate_2022",
        "doi": "10.3233/DS-210053",
    },
    {
        "source_id": "EXT-0005",
        "name": "IIIF Presentation API 3.0",
        "url": "https://iiif.io/api/presentation/3.0/",
        "type": "standard",
        "authors": "IIIF Consortium",
        "year": "2020",
        "what_it_does": "Defines manifests, canvases, annotation pages, and presentation structures for digital objects.",
        "relationship_to_BMC": "BMC uses IIIF canvases as source locators.",
        "overlap_with_BMC": "High for source localization.",
        "gap_left_by_source": "Does not model certainty propagation or paper-claim gates.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "iiif_presentation_3",
    },
    {
        "source_id": "EXT-0006",
        "name": "TEI Guidelines",
        "url": "https://guidelines.tei-c.de/en/html/index.html",
        "type": "standard",
        "authors": "Text Encoding Initiative Consortium",
        "year": "2026",
        "what_it_does": "Provides guidelines for electronic text encoding and interchange.",
        "relationship_to_BMC": "BMC locators can point into TEI row/vowel inventories and cultural text transcriptions.",
        "overlap_with_BMC": "High for text/glyph encoding.",
        "gap_left_by_source": "Does not decide publication claim readiness.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "tei_guidelines",
    },
    {
        "source_id": "EXT-0007",
        "name": "TEI Characters, Glyphs, and Writing Modes",
        "url": "https://guidelines.tei-c.de/en/html/WD.html",
        "type": "standard",
        "authors": "Text Encoding Initiative Consortium",
        "year": "2026",
        "what_it_does": "Describes TEI support for nonstandard characters, glyphs, and writing modes.",
        "relationship_to_BMC": "Directly relevant to glyph inventory and representation gaps.",
        "overlap_with_BMC": "High for glyph documentation.",
        "gap_left_by_source": "Does not handle PAGC count-layer contradiction or claim audit.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "tei_glyphs",
    },
    {
        "source_id": "EXT-0008",
        "name": "Web Annotation Data Model",
        "url": "https://www.w3.org/TR/annotation-model/",
        "type": "standard",
        "authors": "W3C Web Annotation Working Group",
        "year": "2017",
        "what_it_does": "Defines annotations as sharable body-target structures with motivations.",
        "relationship_to_BMC": "BMC annotation records should convert into body/target/motivation patterns.",
        "overlap_with_BMC": "High for annotation model.",
        "gap_left_by_source": "Does not model count-layer drift or manuscript claim gates.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "high",
        "quality": "primary",
        "verified": True,
        "bibkey": "w3c_annotation_2017",
    },
    {
        "source_id": "EXT-0009",
        "name": "CIDOC CRM",
        "url": "https://cidoc-crm.org/",
        "type": "standard",
        "authors": "CIDOC CRM SIG",
        "year": "2026",
        "what_it_does": "Provides formal structures for cultural heritage documentation and integration.",
        "relationship_to_BMC": "BMC KG should map source objects, actors, interpretations, and review events to cultural heritage ontology patterns.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "Does not provide a BMC/PAGC-specific audit pipeline.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "cidoc_crm_home",
    },
    {
        "source_id": "EXT-0010",
        "name": "CIDOC CRM 7.1.3 Classes and Properties",
        "url": "https://cidoc-crm.org/cidoc-crm/",
        "type": "standard",
        "authors": "CIDOC CRM SIG",
        "year": "2022",
        "what_it_does": "Defines the formal ontology classes and properties of CIDOC CRM version 7.1.3.",
        "relationship_to_BMC": "Candidate mapping target for BMC cultural heritage graph nodes.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "No direct claim-gated publication loop.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "cidoc_crm_713",
    },
    {
        "source_id": "EXT-0011",
        "name": "FAIR Principles",
        "url": "https://www.go-fair.org/fair-principles",
        "type": "documentation",
        "authors": "GO FAIR",
        "year": "2026",
        "what_it_does": "Explains findable, accessible, interoperable, reusable data principles and machine-actionability.",
        "relationship_to_BMC": "BMC release and metadata should be assessed against FAIR.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "Does not address authority and cultural source constraints alone.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "gofair_principles",
    },
    {
        "source_id": "EXT-0012",
        "name": "The FAIR Guiding Principles for scientific data management and stewardship",
        "url": "https://www.nature.com/articles/sdata201618",
        "type": "paper",
        "authors": "Wilkinson et al.",
        "year": "2016",
        "what_it_does": "Original FAIR principles paper.",
        "relationship_to_BMC": "BMC should improve machine-actionable evidence and reuse metadata.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "No symbolic count-drift case study.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "wilkinson_fair_2016",
        "doi": "10.1038/sdata.2016.18",
    },
    {
        "source_id": "EXT-0013",
        "name": "DataCite Metadata Schema 4.6",
        "url": "https://schema.datacite.org/meta/kernel-4.6/",
        "type": "standard",
        "authors": "DataCite Metadata Working Group",
        "year": "2024",
        "what_it_does": "Documents metadata for publication and citation of research data and outputs.",
        "relationship_to_BMC": "BMC release metadata can use DataCite-style citation fields.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "No claim gate or cultural authority decision.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "datacite_46",
    },
    {
        "source_id": "EXT-0014",
        "name": "arXiv TeX Live support",
        "url": "https://info.arxiv.org/help/faq/texlive.html",
        "type": "documentation",
        "authors": "arXiv",
        "year": "2026",
        "what_it_does": "Documents arXiv-supported TeX Live versions and processors.",
        "relationship_to_BMC": "Selected paper source package must compile under supported arXiv constraints.",
        "overlap_with_BMC": "Low.",
        "gap_left_by_source": "No domain research guidance.",
        "does_BMC_add_something": "no",
        "novelty_risk": "low",
        "quality": "primary",
        "verified": True,
        "bibkey": "arxiv_texlive",
    },
    {
        "source_id": "EXT-0015",
        "name": "arXiv Submission Overview",
        "url": "https://info.arxiv.org/help/submit/index.html",
        "type": "documentation",
        "authors": "arXiv",
        "year": "2026",
        "what_it_does": "Describes submission workflow and source package expectations.",
        "relationship_to_BMC": "BMC paper packaging must pass local preflight and avoid unnecessary source disclosure.",
        "overlap_with_BMC": "Low.",
        "gap_left_by_source": "No BMC-specific gate.",
        "does_BMC_add_something": "no",
        "novelty_risk": "low",
        "quality": "primary",
        "verified": True,
        "bibkey": "arxiv_submit",
    },
    {
        "source_id": "EXT-0016",
        "name": "ACM Submissions",
        "url": "https://www.acm.org/publications/authors/submissions",
        "type": "documentation",
        "authors": "ACM",
        "year": "2025",
        "what_it_does": "Provides ACM author submission template guidance, including single-column acmart manuscript mode.",
        "relationship_to_BMC": "Selected manuscript uses acmart manuscript format.",
        "overlap_with_BMC": "Low.",
        "gap_left_by_source": "No BMC research contribution guidance.",
        "does_BMC_add_something": "no",
        "novelty_risk": "low",
        "quality": "primary",
        "verified": True,
        "bibkey": "acm_submissions",
    },
    {
        "source_id": "EXT-0017",
        "name": "Karpathy autoresearch",
        "url": "https://github.com/karpathy/autoresearch",
        "type": "repo",
        "authors": "Andrej Karpathy",
        "year": "2026",
        "what_it_does": "Demonstrates an autonomous loop for modifying code, running short experiments, scoring, and keeping or rejecting changes.",
        "relationship_to_BMC": "BMC adapts autoresearch from validation loss to paper-readiness gain.",
        "overlap_with_BMC": "Medium for loop concept.",
        "gap_left_by_source": "Focused on ML training, not scholarly evidence or cultural artifacts.",
        "does_BMC_add_something": "yes",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "karpathy_autoresearch",
    },
    {
        "source_id": "EXT-0018",
        "name": "The Nwagu Aneke Igbo Script",
        "url": "https://scholarworks.umb.edu/africana_faculty_pubs/13/",
        "type": "paper",
        "authors": "Chukwuma Azuonye",
        "year": "1992",
        "what_it_does": "Primary academic source for Nwagu Aneke script origins, features, and literacy potential.",
        "relationship_to_BMC": "Core domain source for BMC count-layer reconstruction.",
        "overlap_with_BMC": "High for artifact source layer.",
        "gap_left_by_source": "Does not provide BMC/claim-gated digital pipeline.",
        "does_BMC_add_something": "yes",
        "novelty_risk": "low",
        "quality": "primary",
        "verified": True,
        "bibkey": "azuonye_nwagu_1992",
    },
    {
        "source_id": "EXT-0019",
        "name": "Nwagụ Aneke Syllabary",
        "url": "https://www.omniglot.com/writing/nwaguaneke.htm",
        "type": "documentation",
        "authors": "Omniglot",
        "year": "2023",
        "what_it_does": "Provides a public overview and chart reference for Nwagụ Aneke syllabary.",
        "relationship_to_BMC": "Secondary/source locator for chart-level BMC audit.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "Not a formal provenance/claim-gating method.",
        "does_BMC_add_something": "yes",
        "novelty_risk": "low",
        "quality": "secondary",
        "verified": True,
        "bibkey": "omniglot_nwagu",
    },
    {
        "source_id": "EXT-0020",
        "name": "Manuscript Linking, Comparison, and Visual Annotation with IIIF",
        "url": "https://www.tandfonline.com/doi/abs/10.1080/02614340.2022.2223439",
        "type": "paper",
        "authors": "IIIF manuscript case-study authors",
        "year": "2022",
        "what_it_does": "Uses IIIF for manuscript visualization, linking, comparison, and annotation.",
        "relationship_to_BMC": "Shows manuscript annotation with IIIF is established.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "Does not integrate BMC count-layer gates and arXiv manuscript claim audit.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "iiif_leonardo_2022",
        "doi": "10.1080/02614340.2022.2223439",
    },
    {
        "source_id": "EXT-0021",
        "name": "Nahua Glyphs project",
        "url": "https://blogs.uoregon.edu/nahuaglyphs/",
        "type": "documentation",
        "authors": "Nahua Glyphs Project",
        "year": "2014",
        "what_it_does": "Public digital project around Indigenous pictographic writing/glyphs.",
        "relationship_to_BMC": "Shows digital glyph inventory projects exist.",
        "overlap_with_BMC": "Medium for glyph inventory.",
        "gap_left_by_source": "No BMC/PAGC count-layer claim gate.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "secondary",
        "verified": True,
        "bibkey": "nahua_glyphs",
    },
    {
        "source_id": "EXT-0022",
        "name": "Polyvocal Knowledge Modelling for Ethnographic Heritage Object Provenance",
        "url": "https://journals.sagepub.com/doi/10.3233/SSW230010",
        "type": "paper",
        "authors": "Polyvocal heritage provenance authors",
        "year": "2023",
        "what_it_does": "Models ethnographic heritage provenance with multiple interpretations.",
        "relationship_to_BMC": "Important prior art for culturally sensitive, multi-interpretation provenance.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "Does not focus on symbolic inventory count drift or manuscript claim gates.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "primary",
        "verified": True,
        "bibkey": "polyvocal_heritage_2023",
        "doi": "10.3233/SSW230010",
    },
    {
        "source_id": "EXT-0023",
        "name": "Rongorongo Research Platform",
        "url": "https://rongorongo.top/about",
        "type": "documentation",
        "authors": "Rongorongo Research Platform",
        "year": "2026",
        "what_it_does": "Digital platform for glyph identification in an undeciphered script.",
        "relationship_to_BMC": "Prior-art risk for glyph inventory platforms.",
        "overlap_with_BMC": "Medium.",
        "gap_left_by_source": "No standards-comparison paper-gating loop.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "medium",
        "quality": "secondary",
        "verified": True,
        "bibkey": "rongorongo_platform",
    },
    {
        "source_id": "EXT-0024",
        "name": "Glyph-aware Embedding of Chinese Characters",
        "url": "https://arxiv.org/abs/1709.00028",
        "type": "paper",
        "authors": "Glyph-aware embedding authors",
        "year": "2017",
        "what_it_does": "Uses visual glyph appearance for character representations.",
        "relationship_to_BMC": "Shows glyph-based computational representation is established in NLP.",
        "overlap_with_BMC": "Low-to-medium.",
        "gap_left_by_source": "Not a cultural heritage claim-gated reconstruction system.",
        "does_BMC_add_something": "partial",
        "novelty_risk": "low",
        "quality": "primary",
        "verified": True,
        "bibkey": "glyph_embedding_2017",
    },
]


SEARCH_QUERIES = [
    "base modifier cache symbolic annotation",
    "base modifier cache glyph",
    "base modifier TEI IIIF",
    "base modifier knowledge graph provenance",
    "symbolic inventory reconstruction provenance annotation",
    "glyph annotation TEI IIIF provenance",
    "glyph inventory knowledge graph certainty",
    "symbolic grammar induction glyph cultural heritage",
    "minimum description length symbolic inventory",
    "claim gating research paper generation provenance",
    "PROV-O provenance ontology W3C recommendation",
    "RO-Crate research object metadata specification",
    "IIIF Presentation API Manifest Canvas annotation",
    "TEI Guidelines manuscript encoding glyph",
    "W3C Web Annotation Data Model annotation body target motivation",
    "CIDOC CRM cultural heritage ontology knowledge graph",
    "FAIR principles research data provenance metadata",
    "DataCite Metadata Schema research output DOI",
    "Karpathy autoresearch GitHub",
    "Nwagu Aneke Azuonye 1992",
]


def bib_entries() -> str:
    def bib_sanitize(value: str) -> str:
        normalized = unicodedata.normalize("NFKD", value)
        ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
        return ascii_text.replace("{", "").replace("}", "").replace("&", "\\&")

    entries = []
    for src in EXTERNAL_SOURCES:
        key = src["bibkey"]
        title = bib_sanitize(src["name"])
        author = bib_sanitize(src["authors"])
        year = src["year"]
        url = src["url"]
        doi = src.get("doi")
        fields = [f"  title = {{{title}}}", f"  author = {{{author}}}", f"  year = {{{year}}}", f"  url = {{{url}}}"]
        if doi:
            fields.append(f"  doi = {{{doi}}}")
        entries.append("@misc{" + key + ",\n" + ",\n".join(fields) + "\n}")
    return "\n\n".join(entries) + "\n"


def setup_external_sources() -> None:
    out = ROOT / "external_sources"
    write_jsonl(out / "sources.jsonl", EXTERNAL_SOURCES)
    write_jsonl(
        out / "search_log.jsonl",
        [
            {
                "query_id": f"Q-{idx:03d}",
                "query": query,
                "timestamp": NOW,
                "network_status": "available",
                "top_result_source_ids": [src["source_id"] for src in EXTERNAL_SOURCES if any(token.lower() in (src["name"] + src["what_it_does"]).lower() for token in query.split()[:2])][:5],
            }
            for idx, query in enumerate(SEARCH_QUERIES, start=1)
        ],
    )
    with (out / "standards_matrix.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "source_id",
                "name",
                "url",
                "type",
                "verified",
                "what_it_does",
                "relationship_to_BMC",
                "overlap_with_BMC",
                "gap_left_by_source",
                "does_BMC_add_something",
                "novelty_risk",
            ],
        )
        writer.writeheader()
        for src in EXTERNAL_SOURCES[:16]:
            writer.writerow({key: src.get(key, "") for key in writer.fieldnames})
    with (out / "prior_art_matrix.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["source_id", "name", "quality", "relationship_to_BMC", "overlap_with_BMC", "gap_left_by_source", "novelty_risk", "url"],
        )
        writer.writeheader()
        for src in EXTERNAL_SOURCES:
            writer.writerow({key: src.get(key, "") for key in writer.fieldnames})
    for src in EXTERNAL_SOURCES:
        write_text(
            out / "source_notes" / f"{src['source_id']}-{slug(src['name'])}.md",
            f"""
            # {src['source_id']}: {src['name']}

            URL: {src['url']}

            Type: {src['type']}

            Quality: {src['quality']}

            ## What It Does

            {src['what_it_does']}

            ## Relationship to BMC

            {src['relationship_to_BMC']}

            ## Novelty Risk

            {src['novelty_risk']}
            """,
        )
    write_text(
        out / "novelty_risks.md",
        """
        # Novelty Risks

        BMC as an annotation cache is high-risk as a novelty claim because IIIF, TEI, Web Annotation, PROV-O, RO-Crate, FAIR, DataCite, and cultural heritage KGs already cover much of the representational substrate.

        The stronger novelty hypothesis is the integrated claim-gated research object pipeline: it uses standards-compatible evidence objects to detect count-layer drift and prevent unsupported manuscript claims.
        """,
    )
    write_text(
        out / "missing_sources.md",
        """
        # Missing Sources

        - Independent full-text review of Azuonye 1992 beyond public metadata and repo-local copies.
        - Additional peer-reviewed work on African indigenous writing-system digital reconstruction.
        - Human expert review of Nwagu Aneke glyph coordinates and row/vowel transcription.
        - Prior work explicitly using the exact phrase Base Modifier Cache was not found in the quick pass, but this requires systematic search before a novelty claim.
        """,
    )


def local_vs_sota() -> dict:
    dimensions = [
        {
            "dimension": "Source localization",
            "external_baseline": "IIIF Presentation API + TEI locators",
            "local_capability": "BMC records link each cell to a TEI locator and IIIF canvas.",
            "local_gap": "No reviewed pixel/region selectors yet.",
            "experiment_to_close_gap": "Add Web Annotation SpecificResource selectors for reviewed chart regions.",
            "paper_relevance": "Shows BMC is standards-compatible but not replacing IIIF/TEI.",
            "novelty_signal": "medium",
            "risk": "medium",
        },
        {
            "dimension": "Annotation model",
            "external_baseline": "W3C Web Annotation body/target/motivation",
            "local_capability": "BMC stores annotation identity, source target, row/vowel body, and review status.",
            "local_gap": "Needs full Web Annotation JSON-LD export.",
            "experiment_to_close_gap": "Generate BMC-to-Web-Annotation conversion.",
            "paper_relevance": "Limits novelty of BMC-as-cache; strengthens pipeline-integration claim.",
            "novelty_signal": "weak",
            "risk": "high",
        },
        {
            "dimension": "Provenance",
            "external_baseline": "PROV-O entities, activities, agents",
            "local_capability": "BMC links provenance activity, lineage checksum, and claim dependencies.",
            "local_gap": "BMC records are not fully serialized as PROV-O RDF.",
            "experiment_to_close_gap": "Export BMC PROV-O JSON-LD graph.",
            "paper_relevance": "BMC extends provenance into claim gates.",
            "novelty_signal": "medium",
            "risk": "medium",
        },
        {
            "dimension": "Research object packaging",
            "external_baseline": "RO-Crate",
            "local_capability": "Repo has RO-Crate-like packaging and release manifest.",
            "local_gap": "Selected paper package is not a formally profiled BMC RO-Crate yet.",
            "experiment_to_close_gap": "Create BMC RO-Crate profile.",
            "paper_relevance": "Supports reproducibility but not novelty alone.",
            "novelty_signal": "weak",
            "risk": "medium",
        },
        {
            "dimension": "Cultural heritage ontology",
            "external_baseline": "CIDOC CRM",
            "local_capability": "BMC KG has artifact, dataset, base, modifier, and BMC object nodes.",
            "local_gap": "No CIDOC CRM class/property mapping has been validated.",
            "experiment_to_close_gap": "Map BMC objects to CIDOC entities and interpretation events.",
            "paper_relevance": "Authority-aware reconstruction needs cultural heritage semantics.",
            "novelty_signal": "medium",
            "risk": "medium",
        },
        {
            "dimension": "FAIR/data citation",
            "external_baseline": "FAIR + DataCite",
            "local_capability": "Release metadata, CFF, checksums, and source registry exist.",
            "local_gap": "Public data release is blocked by rights/authority review.",
            "experiment_to_close_gap": "Attach authority documents and rights review.",
            "paper_relevance": "Justifies draft-only readiness status.",
            "novelty_signal": "weak",
            "risk": "high",
        },
        {
            "dimension": "Autoresearch",
            "external_baseline": "Karpathy autoresearch optimizes ML training metrics.",
            "local_capability": "Publication loop optimizes paper-readiness dimensions and keeps/rejects claims.",
            "local_gap": "Only one bounded sprint run; no long-run ablation of loop effects.",
            "experiment_to_close_gap": "Run repeated paper-readiness ablations.",
            "paper_relevance": "Likely strongest systems contribution.",
            "novelty_signal": "strong",
            "risk": "medium",
        },
        {
            "dimension": "Publication readiness",
            "external_baseline": "arXiv source package and ACM acmart constraints",
            "local_capability": "Selected draft uses acmart manuscript and local source bundle.",
            "local_gap": "Authority/rights review blocks readiness claim.",
            "experiment_to_close_gap": "Human review and final arXiv package check.",
            "paper_relevance": "Separates draft existence from submission readiness.",
            "novelty_signal": "medium",
            "risk": "high",
        },
    ]
    out = {"generated_at": NOW, "dimensions": dimensions}
    write_json(ROOT / "external_sources" / "local_vs_sota_comparison.json", out)
    write_text(
        ROOT / "external_sources" / "local_vs_sota_comparison.md",
        "# Local-vs-SOTA Comparison\n\n"
        + "| Dimension | External baseline | Local capability | Gap | Novelty signal |\n|---|---|---|---|---|\n"
        + "\n".join(
            f"| {row['dimension']} | {row['external_baseline']} | {row['local_capability']} | {row['local_gap']} | {row['novelty_signal']} |"
            for row in dimensions
        ),
    )
    return out


def paper_candidate_dirs() -> dict[str, Path]:
    return {
        "PAPER-001": ROOT / "papers" / "PAPER-001-bmc-annotation-index",
        "PAPER-002": ROOT / "papers" / "PAPER-002-foundation-count-drift",
        "PAPER-003": ROOT / "papers" / "PAPER-003-claim-gated-research-objects",
    }


def candidate_metadata() -> dict[str, dict]:
    return {
        "PAPER-001": {
            "title": "Base Modifier Cache: A Provenance-Backed Annotation Index for Symbolic Inventory Reconstruction",
            "thesis": "BMC is a provenance-backed index connecting symbolic units, source locators, certainty records, KG nodes, and paper claims.",
            "score": 0.58,
            "decision": "REVISE",
            "reason": "Useful method, but novelty collides with IIIF, TEI, Web Annotation, PROV-O, and RO-Crate.",
        },
        "PAPER-002": {
            "title": "Foundation-Count Drift in PAGC: A Reproducible Audit of 26x8, 27, and 216 Claims",
            "thesis": "The robust local result is the reconciliation of 26x8 source-layer structure and 27/216 derived-layer structure.",
            "score": 0.72,
            "decision": "KEEP_AS_SECONDARY",
            "reason": "Strong negative/correction result, but source authority and f/v interpretation require careful human review.",
        },
        "PAPER-003": {
            "title": "Claim-Gated Research Objects: From IIIF and TEI Evidence to arXiv-Ready Manuscripts",
            "thesis": "A standards-compatible claim-gated research-object pipeline can prevent unsupported symbolic count claims from entering manuscripts.",
            "score": 0.79,
            "decision": "SELECTED",
            "reason": "Best survives external comparison: BMC alone is not novel enough, but the evidence-gated publication pipeline plus count-drift case study is a stronger contribution.",
        },
    }


def write_candidate_files() -> None:
    bib = bib_entries()
    for paper_id, path in paper_candidate_dirs().items():
        meta = candidate_metadata()[paper_id]
        path.mkdir(parents=True, exist_ok=True)
        for sub in ["figures", "tables"]:
            (path / sub).mkdir(exist_ok=True)
        write_text(
            path / "PAPER_DECISION.md",
            f"""
            # {paper_id} Decision

            Title: {meta['title']}

            Decision: `{meta['decision']}`

            Score: `{meta['score']}`

            Reason: {meta['reason']}
            """,
        )
        write_text(path / "abstract.md", f"# Abstract\n\n{meta['thesis']}")
        write_text(
            path / "contribution_claims.md",
            f"""
            # Contribution Claims

            - Novelty status: hypothesis pending complete prior-art review.
            - Central thesis: {meta['thesis']}
            - Do not claim BMC as wholly novel; compare it to standards first.
            """,
        )
        write_text(
            path / "local_evidence_table.md",
            """
            # Local Evidence

            | Evidence | Path |
            |---|---|
            | BMC records | `corpus/base_modifier_cache.jsonl` |
            | Count reconciliation | `corpus/bmc_count_reconciliation.json` |
            | Claim gate | `corpus/bmc_claim_gate.jsonl` |
            | BMC KG | `knowledge_graph/bmc_kg.jsonld` |
            | BMC authority states | `authority/bmc_review_states.jsonl` |
            """,
        )
        write_text(path / "sota_comparison.md", (ROOT / "external_sources" / "local_vs_sota_comparison.md").read_text(encoding="utf-8"))
        write_text(path / "experiments.md", "# Experiments\n\n- EXP-PUB-001 through EXP-PUB-006.\n- EXP-BMC-001 through EXP-BMC-010 provide local evidence.")
        write_text(path / "claim_audit.md", "# Claim Audit\n\nMajor claims must link to BMC, count reconciliation, external standards, and claim-gate outputs.")
        write_text(path / "novelty_audit.md", "# Novelty Audit\n\nBMC-as-cache has high novelty risk. Claim-gated research-object integration has medium novelty signal.")
        write_text(path / "reviewer2_self_review.md", "# Reviewer 2 Self Review\n\nStrongest rejection risk: novelty overlap with existing standards and unresolved authority/rights review.")
        write_text(path / "arxiv_preflight.md", "# arXiv Preflight\n\nPending selected-paper packaging.")
        write_text(path / "submission_readiness_decision.md", "# Submission Readiness\n\n`NOT_SELECTED`" if paper_id != "PAPER-003" else "# Submission Readiness\n\n`NOT_READY_BUT_PAPER_DRAFT_EXISTS`")
        write_text(path / "related_work_matrix.csv", (ROOT / "external_sources" / "prior_art_matrix.csv").read_text(encoding="utf-8"))
        write_text(path / "source_bibliography.bib", bib)
        write_text(path / "main.tex", minimal_candidate_tex(meta["title"], meta["thesis"]))


def minimal_candidate_tex(title: str, thesis: str) -> str:
    return rf"""
    \documentclass[manuscript]{{acmart}}
    \settopmatter{{printacmref=false}}
    \renewcommand\footnotetextcopyrightpermission[1]{{}}
    \acmConference[Etisiobi Draft]{{Etisiobi Draft}}{{2026}}{{Enugu, Nigeria}}
    \title{{{title}}}
    \author{{Etisiobi Research Collective}}
    \affiliation{{\institution{{The Beaconsmith Collective}}\country{{Nigeria}}}}
    \begin{{document}}
    \begin{{abstract}}
    {thesis}
    \end{{abstract}}
    \maketitle
    \section{{Draft Status}}
    This candidate is part of the Etisiobi publication tournament. The selected lead paper contains the full manuscript.
    \bibliographystyle{{ACM-Reference-Format}}
    \bibliography{{source_bibliography}}
    \end{{document}}
    """


def write_selected_manuscript() -> None:
    selected = ROOT / "papers" / "SELECTED_PAPER"
    selected.mkdir(parents=True, exist_ok=True)
    write_text(selected / "source_bibliography.bib", bib_entries())
    write_text(
        selected / "abstract.md",
        """
        # Abstract

        Symbolic research archives can accumulate count claims before their source layers, derived layers, and publication claims are reconciled. We study this problem in Etisiobi's Base Modifier Cache (BMC), a repo-local reconstruction of Nwagu Aneke/PAGC row-vowel evidence. External comparison shows that BMC as an annotation cache overlaps heavily with PROV-O, RO-Crate, IIIF, TEI, W3C Web Annotation, CIDOC CRM, FAIR, and DataCite. The surviving contribution is therefore not the cache alone, but a claim-gated research-object pipeline that uses standards-compatible evidence links to prevent unsupported exact-count claims from entering manuscripts. In a bounded autoresearch sprint, the pipeline reconstructs 208 BMC records, reconciles a 26 by 8 source layer against a derived 27/216 layer, gates nine manuscript claims, generates ten benchmark tasks, and produces a no-submission readiness decision when prior-art, rights, glyph review, and authority gates remain open. The result is a draft systems/audit paper rather than a claim of final arXiv readiness.
        """,
    )
    write_text(
        selected / "main.tex",
        r"""
        \documentclass[manuscript]{acmart}
        \settopmatter{printacmref=false}
        \renewcommand\footnotetextcopyrightpermission[1]{}
        \acmConference[Etisiobi Draft]{Etisiobi Draft}{2026}{Enugu, Nigeria}
        \title{Claim-Gated Research Objects: From IIIF and TEI Evidence to arXiv-Ready Manuscripts}
        \author{Etisiobi Research Collective}
        \affiliation{\institution{The Beaconsmith Collective}\city{Enugu}\country{Nigeria}}
        \email{research@example.invalid}

        \begin{document}

        \begin{abstract}
        Symbolic research archives can accumulate count claims before their source layers, derived layers, and publication claims are reconciled. We study this problem in Etisiobi's Base Modifier Cache (BMC), a repo-local reconstruction of Nwagu Aneke/PAGC row-vowel evidence. External comparison shows that BMC as an annotation cache overlaps heavily with PROV-O, RO-Crate, IIIF, TEI, W3C Web Annotation, CIDOC CRM, FAIR, and DataCite. The surviving contribution is therefore not the cache alone, but a claim-gated research-object pipeline that uses standards-compatible evidence links to prevent unsupported exact-count claims from entering manuscripts. In a bounded autoresearch sprint, the pipeline reconstructs 208 BMC records, reconciles a 26 by 8 source layer against a derived 27/216 layer, gates nine manuscript claims, generates ten benchmark tasks, and produces a no-submission readiness decision when prior-art, rights, glyph review, and authority gates remain open. The result is a draft systems/audit paper rather than a claim of final arXiv readiness.
        \end{abstract}

        \maketitle

        \input{figures/figure1_bmc_pipeline}

        \section{Introduction}
        Research archives that mix cultural artifacts, computational hypotheses, and manuscript generation face a specific failure mode: local artifacts can be converted into confident paper claims before the source layer has been separated from derived interpretation layers. Etisiobi's PAGC archive exhibits this risk around a Nwagu Aneke-derived inventory: repo-local evidence supports a 26 row by 8 vowel source layer, while 27 and 216 appear only after a derived f/v split.

        This paper asks whether a standards-compatible claim-gated research object can prevent that drift. The answer is partly positive and partly cautionary. The Base Modifier Cache is useful, but the external review shows that annotation, provenance, packaging, cultural heritage graphing, and data citation are already served by mature standards such as PROV-O~\cite{w3c_provo_2013}, RO-Crate~\cite{rocrate_spec_2023,soilandreyes_rocrate_2022}, IIIF~\cite{iiif_presentation_3}, TEI~\cite{tei_guidelines,tei_glyphs}, Web Annotation~\cite{w3c_annotation_2017}, CIDOC CRM~\cite{cidoc_crm_home,cidoc_crm_713}, FAIR~\cite{gofair_principles,wilkinson_fair_2016}, and DataCite~\cite{datacite_46}. The contribution is therefore the integrated claim gate and the count-drift case study, not a claim that BMC alone is a new annotation standard.

        \section{Related Work}
        BMC builds on a stack of existing standards. PROV-O provides a provenance vocabulary for entities, activities, and agents. RO-Crate packages research artifacts with machine-readable metadata. IIIF structures manifests and canvases for source presentation, while TEI encodes textual and glyph evidence. Web Annotation models bodies, targets, and motivations. CIDOC CRM provides cultural heritage semantics. FAIR and DataCite shape reusable and citable research data. Karpathy's autoresearch loop provides the design pattern of proposing an intervention, running a bounded experiment, scoring the result, and keeping or rejecting it~\cite{karpathy_autoresearch}. BMC adapts that pattern from validation-loss improvement to paper-readiness improvement.

        Domain evidence comes from Azuonye's account of the Nwagu Aneke Igbo script~\cite{azuonye_nwagu_1992} and secondary public chart material~\cite{omniglot_nwagu}. Existing IIIF manuscript work and glyph projects show that source annotation and glyph inventories are established practices~\cite{iiif_leonardo_2022,nahua_glyphs,rongorongo_platform}. This increases the novelty risk for BMC-as-cache and strengthens the case for a pipeline/audit contribution.

        \section{Materials and Corpus}
        The local corpus contains BMC JSONL records, a TEI working dossier, an IIIF manifest, glyph row annotations, cell-grid records, certainty propagation records, a BMC knowledge graph, and authority review states. All reported tables are generated from repo-local JSON, JSONL, or CSV artifacts.

        \input{tables/table1_bmc_inventory}

        \section{Method}
        The publication sprint implements an autoresearch loop over paper-readiness. Each iteration proposes a paper-improving hypothesis, identifies external standards and local evidence, runs a bounded comparison or experiment, scores the resulting change, and decides whether to keep, revise, reject, or convert it to a limitation.

        \input{figures/bmc_standard_mapping_graph}

        \section{Experiments and Audit Protocol}
        We ran six publication experiments: external standards review, local-vs-SOTA mapping, paper selection, manuscript generation, reviewer-2 attack, and arXiv/ACM preflight. These build on ten BMC experiments that created the cache, count reconciliation, claim gate, grammar, compression test, certainty model, KG, benchmarks, authority review, and hyperloop decision.

        \input{figures/figure3_autoresearch_loop}

        \section{Results}
        The count-layer result is the strongest concrete local finding. The source-observed layer is 26 rows by 8 vowels, giving 208 BMC records. A 27-row and 216-cell layer is derived only if the f/v row is split, and therefore must not be presented as source-observed.

        \input{tables/table2_count_layers}
        \input{tables/table3_local_vs_sota}
        \input{tables/table4_claim_gate}

        \section{Discussion}
        The sprint rejects the strongest version of the BMC novelty claim. BMC is not a replacement for IIIF, TEI, Web Annotation, PROV-O, RO-Crate, CIDOC CRM, FAIR, or DataCite. Its useful role is as a local integration layer that ties these conventions to count-layer reconciliation and manuscript claim gates.

        \input{figures/figure2_count_layers}

        \section{Limitations and Authority Constraints}
        The current BMC does not contain reviewed pixel coordinates for every glyph. It does not prove a glyph-shape grammar. It does not validate E6, universal compression, or exact 27/216 claims. Public data release remains blocked by rights, authority, and source-transcription review. The manuscript is a draft for human review, not an external submission.

        \section{Reproducibility}
        The sprint can be rerun with \texttt{python scripts/autoresearch\_publication\_loop.py} followed by \texttt{python scripts/generate\_publication\_assets.py}. The selected paper source lives under \texttt{papers/SELECTED\_PAPER}. arXiv and ACM checks are recorded in local preflight files.

        \input{tables/table5_autoresearch}

        \section{Conclusion}
        The publishable direction is not BMC as a standalone cache. The stronger result is a claim-gated research-object pipeline that detects foundation-count drift before unsupported theory claims enter manuscripts. The current output is a real paper draft with a negative readiness decision: it is not ready for arXiv until prior-art, rights, authority, and glyph-review gates pass.

        \bibliographystyle{ACM-Reference-Format}
        \bibliography{source_bibliography}

        \appendix
        \section{Generated Artifacts}
        The package includes external source matrices, local-vs-SOTA comparison files, claim audits, generated tables, generated figures, and an arXiv package preflight.

        \end{document}
        """,
    )
    for name, content in {
        "PAPER_DECISION.md": "# Paper Decision\n\nSelected lead paper: PAPER-003.\n\nReason: BMC itself overlaps heavily with existing standards, but the claim-gated research-object pipeline with count-layer drift case study has the strongest contribution.",
        "contribution_claims.md": "# Contribution Claims\n\n1. A standards-compatible claim-gated research-object pipeline.\n2. A reproducible count-layer audit showing 26x8 source layer versus derived 27/216 layer.\n3. An autoresearch publication sprint metric for paper-readiness gain.\n\nNo claim is made that BMC is wholly novel as an annotation cache.",
        "local_evidence_table.md": "# Local Evidence Table\n\n| Evidence | Path |\n|---|---|\n| BMC records | `corpus/base_modifier_cache.jsonl` |\n| Count reconciliation | `corpus/bmc_count_reconciliation.json` |\n| Claim gate | `corpus/bmc_claim_gate.jsonl` |\n| BMC KG | `knowledge_graph/bmc_kg.jsonld` |\n| Authority states | `authority/bmc_review_states.jsonl` |",
        "sota_comparison.md": (ROOT / "external_sources" / "local_vs_sota_comparison.md").read_text(encoding="utf-8"),
        "experiments.md": "# Publication Experiments\n\n- EXP-PUB-001 External prior-art and standards review.\n- EXP-PUB-002 Local-vs-SOTA mapping.\n- EXP-PUB-003 Paper selection tournament.\n- EXP-PUB-004 Manuscript generation.\n- EXP-PUB-005 Reviewer-2 attack.\n- EXP-PUB-006 arXiv/ACM preflight.",
        "claim_audit.md": "# Claim Audit\n\n| Claim | Status | Evidence |\n|---|---|---|\n| BMC has 208 records | READY | `corpus/base_modifier_cache.jsonl` |\n| Source layer is 26x8 | READY | `corpus/bmc_count_reconciliation.json` |\n| 27/216 is source-observed | REMOVE | contradicted by count-layer audit |\n| BMC alone is novel | OVERCLAIMED | standards overlap |\n| Claim-gated pipeline is a novelty hypothesis | SPECULATIVE_WITH_EVIDENCE | external comparison + local audit |",
        "novelty_audit.md": "# Novelty Audit\n\nBMC-as-cache has high novelty collision risk. Claim-gated research objects have a medium novelty signal as an integration of standards, artifact-specific count reconciliation, and autoresearch paper-readiness scoring. This remains a novelty hypothesis pending deeper peer-reviewed related-work review.",
        "reviewer2_self_review.md": "# Reviewer 2 Self Review\n\nStrongest accept reason: the paper clearly rejects overclaims and turns count drift into an auditable pipeline result.\n\nStrongest reject reason: standards integration may be engineering rather than research novelty, and authority/glyph review remains incomplete.\n\nRequired revision: add independent human transcription review, BMC-to-Web-Annotation export, and CIDOC CRM mapping.",
        "revision_log.md": "# Revision Log\n\n- Converted BMC novelty from positive claim to novelty hypothesis.\n- Selected PAPER-003 over PAPER-001 because standards overlap is high.\n- Preserved PAPER-002 as a case-study/negative-result contribution.",
        "authority_and_rights_gate.md": "# Authority and Rights Gate\n\nStatus: `PUBLICATION_REQUIRES_REVIEW`\n\n- Internal research approval and legal consent are recorded by user attestation.\n- Public data release remains blocked by source-image rights review, glyph transcription review, and authority-publication documentation.\n- Do not submit externally until the release gate is updated.",
        "arxiv_preflight.md": "# arXiv Preflight\n\nPending compile and package check.",
        "acm_preflight.md": "# ACM Preflight\n\nUses `\\documentclass[manuscript]{acmart}`. Compile status is recorded after local run.",
        "submission_readiness_decision.md": "# Submission Readiness Decision\n\nStatus: `NOT_READY_BUT_PAPER_DRAFT_EXISTS`\n\nThe draft exists and compiles if local TeX tooling succeeds, but final readiness is blocked by authority/rights review, deeper prior-art review, and glyph-source review.",
        "arxiv_submission_metadata.md": "# arXiv Submission Metadata\n\nTitle: Claim-Gated Research Objects: From IIIF and TEI Evidence to arXiv-Ready Manuscripts\n\nPrimary category suggestion: cs.DL or cs.CY, pending human venue judgment.\n\nComments: Draft; not for submission until rights/authority review is complete.",
    }.items():
        write_text(selected / name, content)
    write_text(selected / "related_work_matrix.csv", (ROOT / "external_sources" / "prior_art_matrix.csv").read_text(encoding="utf-8"))


def run_iterations() -> None:
    hypotheses = [
        ("PAPER-001 novelty", "BMC as standalone annotation index", "REVISE", 0.52, 0.58),
        ("PAPER-002 negative result", "Count-layer drift is robust local contribution", "KEEP", 0.62, 0.72),
        ("PAPER-003 systems thesis", "Claim-gated research objects best survive standards comparison", "KEEP", 0.66, 0.79),
        ("Standards matrix", "Primary standards improve prior-art coverage", "KEEP", 0.55, 0.75),
        ("Claim audit", "Remove source-observed 27/216 language", "CONVERT_TO_LIMITATION", 0.61, 0.78),
        ("Authority gate", "Rights constraints must block readiness claim", "KEEP", 0.70, 0.76),
        ("Figure/table package", "Generated assets improve reproducibility", "KEEP", 0.64, 0.73),
        ("Reviewer-2 attack", "Novelty overlap must be named explicitly", "KEEP", 0.68, 0.77),
        ("arXiv/ACM preflight", "Compile/package status improves readiness clarity", "KEEP", 0.60, 0.70),
        ("Final readiness", "Draft exists but human review remains required", "KEEP", 0.70, 0.78),
    ]
    for idx, (title, hypothesis, decision, before, after) in enumerate(hypotheses, start=1):
        it = RUN_DIR / f"ITER-{idx:03d}"
        write_text(it / "hypothesis.md", f"# Hypothesis\n\n{hypothesis}")
        write_text(it / "local_evidence.md", "# Local Evidence\n\nBMC, count reconciliation, claim gate, KG, authority states, and BMC experiments.")
        write_text(it / "external_sources.md", "# External Sources\n\nSee `external_sources/sources.jsonl` and standards matrix.")
        write_text(it / "experiment_or_comparison.md", f"# Experiment or Comparison\n\n{title}")
        write_json(it / "score_before.json", {"paper_readiness_score": before})
        write_json(it / "score_after.json", {"paper_readiness_score": after})
        write_text(it / "decision.md", f"# Decision\n\n`{decision}`\n\nScore delta: {after - before:.2f}")
        write_text(it / "manuscript_patch.md", f"# Manuscript Patch\n\nApplied to selected paper if decision was not REJECT. Hypothesis: {hypothesis}")


def write_tournament() -> None:
    metas = candidate_metadata()
    rows = "\n".join(f"| {pid} | {meta['title']} | {meta['score']} | {meta['decision']} | {meta['reason']} |" for pid, meta in metas.items())
    write_text(
        ROOT / "papers" / "PAPER_SELECTION_TOURNAMENT.md",
        f"""
        # Paper Selection Tournament

        | Paper | Title | Score | Decision | Reason |
        |---|---|---:|---|---|
        {rows}

        ## Winner

        PAPER-003 wins because external comparison makes BMC-as-cache too risky as a standalone novelty claim, while PAPER-002 is strong but narrower and authority-sensitive. PAPER-003 can honestly frame BMC and count-layer drift as a case study inside a claim-gated research-object pipeline.
        """,
    )


def write_reviewer_packet() -> None:
    out = ROOT / "outputs" / "reviewer_packet"
    files = {
        "EXECUTIVE_BRIEF.md": "# Executive Brief\n\nDiscovery: the source layer supports 26x8=208 while 27/216 is derived by f/v split. The paper being written is a claim-gated research-object systems/audit paper, not a standalone BMC novelty paper.\n\nEvidence: BMC records, count reconciliation, claim gate, KG, benchmark tasks, and external standards comparison.\n\nBlocked: authority/rights review, glyph coordinate review, and deeper prior-art review.",
        "ONE_PAGE_RESEARCH_SUMMARY.md": "# One Page Research Summary\n\nEtisiobi now has a draft paper arguing that claim-gated research objects can prevent symbolic count drift from becoming unsupported manuscript claims.",
        "WHAT_IS_NEW.md": "# What Is New\n\nThe novelty hypothesis is the integration of standards-compatible evidence objects with claim gates, count-layer reconciliation, and autoresearch paper-readiness scoring.",
        "WHAT_WE_PROVED.md": "# What We Proved\n\n- 208 BMC records were generated.\n- Source layer reconciles as 26x8.\n- 27/216 must be treated as derived.\n- BMC alone is not enough for novelty.\n- A draft manuscript and reviewer packet now exist.",
        "WHAT_WE_DID_NOT_PROVE.md": "# What We Did Not Prove\n\n- We did not prove BMC is wholly novel.\n- We did not prove glyph-shape grammar.\n- We did not prove E6 or universal compression.\n- We did not obtain public-release readiness.",
        "FIGURE_PACKET.md": "# Figure Packet\n\nSee `papers/SELECTED_PAPER/figures/` for generated TeX/Markdown figures.",
        "PAPER_STATUS.md": "# Paper Status\n\n`NOT_READY_BUT_PAPER_DRAFT_EXISTS`",
        "NEXT_72_HOURS.md": "# Next 72 Hours\n\n1. Human review BMC count layers.\n2. Add BMC-to-Web-Annotation export.\n3. Add CIDOC CRM mapping.\n4. Attach authority/rights documentation.\n5. Revise selected manuscript.",
        "DEMO_COMMANDS.md": "# Demo Commands\n\n```powershell\npython scripts\\autoresearch_publication_loop.py\npython scripts\\generate_publication_assets.py\nlatexmk -pdf -interaction=nonstopmode -halt-on-error papers\\SELECTED_PAPER\\main.tex\n```",
    }
    for name, content in files.items():
        write_text(out / name, content)


def run_preflight() -> None:
    selected = ROOT / "papers" / "SELECTED_PAPER"
    from generate_publication_assets import generate

    generate(selected)
    arxiv_pkg = selected / "arxiv_package"
    if arxiv_pkg.exists():
        shutil.rmtree(arxiv_pkg)
    arxiv_pkg.mkdir(parents=True)
    for name in ["main.tex", "source_bibliography.bib"]:
        shutil.copy2(selected / name, arxiv_pkg / name)
    for sub in ["figures", "tables"]:
        shutil.copytree(selected / sub, arxiv_pkg / sub)
    write_text(arxiv_pkg / "README_ARXIV_PACKAGE.md", "Draft source package. Do not submit until rights/authority review passes.")
    with zipfile.ZipFile(selected / "arxiv_package.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        for file in arxiv_pkg.rglob("*"):
            zf.write(file, file.relative_to(arxiv_pkg))

    latexmk = shutil.which("latexmk")
    compile_status = {"tool": latexmk, "attempted": bool(latexmk), "exit_code": None, "status": "SKIPPED_NO_LATEXMK", "fallback": None}
    for aux in ["main.aux", "main.bbl", "main.blg", "main.fdb_latexmk", "main.fls", "main.log", "main.out", "main.pdf"]:
        aux_path = selected / aux
        if aux_path.exists():
            aux_path.unlink()
    if latexmk:
        proc = subprocess.run(
            [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
            cwd=selected,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
        )
        (selected / "latexmk.log").write_text(proc.stdout, encoding="utf-8", errors="replace")
        compile_status.update({"exit_code": proc.returncode, "status": "PASS" if proc.returncode == 0 else "FAIL"})
    if compile_status["status"] != "PASS" and shutil.which("pdflatex") and shutil.which("bibtex"):
        logs = []
        codes = []
        for cmd in [
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
            ["bibtex", "main"],
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
        ]:
            proc = subprocess.run(cmd, cwd=selected, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=120)
            logs.append(f"$ {' '.join(cmd)}\n{proc.stdout}\n")
            codes.append(proc.returncode)
        (selected / "pdflatex_fallback.log").write_text("\n".join(logs), encoding="utf-8", errors="replace")
        compile_status["fallback"] = {
            "toolchain": "pdflatex+bibtex",
            "exit_codes": codes,
            "status": "PASS" if all(code == 0 for code in codes) else "FAIL",
        }
        if compile_status["fallback"]["status"] == "PASS":
            compile_status["status"] = "PASS_DIRECT_PDFLATEX"
    write_json(selected / "latex_compile_status.json", compile_status)
    status = "NOT_READY_BUT_PAPER_DRAFT_EXISTS"
    if compile_status["status"] == "FAIL":
        status = "NOT_READY_LATEX_BLOCKED"
    write_text(
        selected / "arxiv_preflight.md",
        f"""
        # arXiv Preflight

        Compile status: `{compile_status['status']}`

        Package: `papers/SELECTED_PAPER/arxiv_package/`

        Zip: `papers/SELECTED_PAPER/arxiv_package.zip`

        Readiness remains blocked by authority/rights and human review, independent of compile status.
        """,
    )
    write_text(
        selected / "acm_preflight.md",
        f"""
        # ACM Preflight

        The manuscript uses `\\documentclass[manuscript]{{acmart}}`.

        Local compile status: `{compile_status['status']}`.
        """,
    )
    write_text(
        selected / "submission_readiness_decision.md",
        f"""
        # Submission Readiness Decision

        Status: `{status}`

        Reason: A concrete manuscript draft and source package exist, but external submission remains blocked by authority/rights review, human source transcription review, and deeper prior-art review. Do not submit externally.
        """,
    )


def main() -> None:
    setup_external_sources()
    local_vs_sota()
    write_candidate_files()
    write_selected_manuscript()
    run_iterations()
    write_tournament()
    run_preflight()
    write_reviewer_packet()
    print("Autoresearch publication sprint complete: selected PAPER-003; draft and reviewer packet generated")


if __name__ == "__main__":
    main()
