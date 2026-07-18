# BMC Web Annotation Export

This directory contains a JSON-LD mapping from Base Modifier Cache records to the W3C Web Annotation pattern.

Status: partial mapping proposal. Each BMC record becomes an Annotation with TextualBody entries for reading and certainty, and a SpecificResource target using the IIIF canvas and TEI locator. Most records lack reviewed pixel selectors, so this is not claimed as full Web Annotation compliance.
