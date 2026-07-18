---
type: source_recovery_audit
program: nwagu_aneke_frontier
source_id: NA-SRC-001
status: blocked_not_recovered
created: "2026-06-22"
updated: "2026-06-22T11:42:00+01:00"
goal: GOAL-FRONTIER-001
claim_ceiling: recovery_audit_only
---

# Azuonye 1992 Appendix II Recovery Audit

## Question

Can the Azuonye 1992 Appendix II "Alphabetical List of Nwagu Aneke's
Characters" be recovered from the current repo, local PDF, or official
repository endpoint?

## Decision

Appendix II is not recovered in the current evidence package.

The local Azuonye PDF names Appendix II, but the extractable/rendered body of
the PDF does not expose the alphabetical character list. Automated refresh from
the official ScholarWorks download endpoint was blocked by a 403 response. This
means Appendix II remains a live source blocker, not a confirmed missing
historical object.

## Reviewed Local Evidence

| Evidence | Result | Implication |
|---|---|---|
| `rg` search for Appendix II / Donatus Nwoga / character-list terms | Found only prior blocker references and no Appendix II transcription. | No local structured character list exists. |
| `pdfinfo research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf` | Local PDF has 18 pages and is not encrypted. | File is readable, but page count alone does not prove Appendix II body exists. |
| `pdfimages -list research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf` | One large image appears on PDF page 16; no separate large image appears for Appendix II. | Appendix I chart is embedded as an image; Appendix II body is not similarly exposed. |
| `pdftotext -layout -f 15 -l 18 ...` | Pages 15-18 expose references, Appendix I chart page header, an Appendix I/II title leaf, and a blank tail page. | Text extraction does not recover the Appendix II list. |
| Existing rendered pages in `experiments/EXP-0001-pagc-base-inventory-resolution/figures/` | Page 16 renders Appendix I; pages 17-18 render an appendix title leaf and a blank tail page. | Visual render does not recover the Appendix II list. |
| `tmp` official download attempt from ScholarWorks endpoint | `Invoke-WebRequest` and `curl` returned 403/HTML rather than a PDF. | Current automated refresh cannot determine whether the hosted file differs from the local PDF. |

## External Leads Found

| Lead | Status | Use |
|---|---|---|
| ScholarWorks landing page | Verified metadata and downloadable article listing. | Citation anchor and source trail; not enough to recover Appendix II body. |
| ScholarWorks direct PDF result | Search snippet names Appendix II and page 18, but direct automated fetch is blocked. | Manual browser retrieval should be tried before declaring the hosted PDF identical to the local PDF. |
| Ahamefula CV | Bibliographic lead confirming Ahamefula and Mbah 2011 in JILL 3:95-103 plus related Nwagu Aneke publications. | Useful for alternate repertoire evidence; not a substitute for Appendix II. |
| Academia-hosted Igbo-language paper page | Bibliography mentions `Nwagu Aneke Project Proposal (n.d.)`. | Lead toward the proposal source that Appendix I says it drew from; reliability and access need review. |

## Claim-Layer Effect

| Claim | Current status after recovery audit |
|---|---|
| Appendix I has 26 printed rows and 8 printed columns | Still strengthened by local visual/PDF audit. |
| Appendix I has one combined `f/v` row | Still supported by local visual/PDF audit. |
| 27/216 is source-observed | Still rejected. |
| 27/216 is a derived f/v split | Still allowed with explicit layer label. |
| Appendix II character list is recovered | Rejected for current evidence package. |
| Complete character inventory is available | Blocked. |
| Ahamefula 164/224 counts can replace Appendix II | Not allowed; they are independent external leads needing local archival and extraction. |

## Recovery Targets

1. Manually retrieve the current ScholarWorks PDF through a browser and compare
   hash, page count, page images, and Appendix II visibility against the local
   PDF.
2. Locate `Nwagu Aneke Research Project Proposal`, especially page 5 and any
   attached Donatus Nwoga 1991 character list.
3. Locate Donatus Nwoga 1991 Appendix II list through University of Nigeria,
   Nsukka, Institute of African Studies, family/estate, or library channels.
4. Locate and locally review Ahamefula and Mbah 2011 only as an independent
   repertoire comparator, not as a replacement for Appendix II.

## Exact Next Action

Human-review the unsent ScholarWorks request draft at
`research/frontier/nwagu_aneke/source_reviews/request_drafts/scholarworks_appendix_ii_request.md`,
then decide whether to send it through the public repository support route.
