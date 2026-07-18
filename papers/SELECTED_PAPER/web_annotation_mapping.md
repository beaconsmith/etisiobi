# BMC to W3C Web Annotation Mapping

Export: `exports/web_annotation/bmc_web_annotations.jsonld`

Mapping:

| BMC concept | Web Annotation concept | Status |
|---|---|---|
| BMC record | Annotation | mapped |
| reading / row / vowel | TextualBody | mapped |
| IIIF canvas | Target source | mapped |
| TEI locator | target metadata | partial |
| certainty basis | TextualBody with assessing purpose | mapped |
| source region | FragmentSelector | only when available |
| provenance activity | annotation metadata | partial |

Compliance note: this is a partial mapping proposal. Most BMC records do not yet have reviewed pixel or region selectors, so the export should not be described as complete Web Annotation compliance.
