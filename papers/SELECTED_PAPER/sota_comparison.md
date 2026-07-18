# Local-vs-SOTA Comparison

| Dimension | External baseline | Local capability | Gap | Novelty signal |
|---|---|---|---|---|
| Source localization | IIIF Presentation API + TEI locators | BMC records link each cell to a TEI locator and IIIF canvas. | No reviewed pixel/region selectors yet. | medium |
| Annotation model | W3C Web Annotation body/target/motivation | BMC stores annotation identity, source target, row/vowel body, and review status. | Needs full Web Annotation JSON-LD export. | weak |
| Provenance | PROV-O entities, activities, agents | BMC links provenance activity, lineage checksum, and claim dependencies. | BMC records are not fully serialized as PROV-O RDF. | medium |
| Research object packaging | RO-Crate | Repo has RO-Crate-like packaging and release manifest. | Selected paper package is not a formally profiled BMC RO-Crate yet. | weak |
| Cultural heritage ontology | CIDOC CRM | BMC KG has artifact, dataset, base, modifier, and BMC object nodes. | No CIDOC CRM class/property mapping has been validated. | medium |
| FAIR/data citation | FAIR + DataCite | Release metadata, CFF, checksums, and source registry exist. | Public data release is blocked by rights/authority review. | weak |
| Autoresearch | Karpathy autoresearch optimizes ML training metrics. | Publication loop optimizes paper-readiness dimensions and keeps/rejects claims. | Only one bounded sprint run; no long-run ablation of loop effects. | strong |
| Publication readiness | arXiv source package and ACM acmart constraints | Selected draft uses acmart manuscript and local source bundle. | Authority/rights review blocks readiness claim. | medium |
