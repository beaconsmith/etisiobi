# BMC to CIDOC CRM / CRMdig Mapping

Export: `exports/cidoc_crm/bmc_cidoc_mapping.jsonld`

Mapping:

| BMC/lab concept | CIDOC/CRMdig concept | Status |
|---|---|---|
| Nwagu Aneke source artifact reference | `crm:E22_Human-Made_Object` | placeholder pending authority review |
| BMC dataset | `crm:E73_Information_Object` | mapped |
| BMC generation / annotation activity | `crm:E13_Attribute_Assignment`, `crmdig:D7_Digital_Machine_Event` | proposal |
| Etisiobi Research Collective | `crm:E39_Actor` | mapped |
| BMC record | `crm:E73_Information_Object` | mapped |
| claim dependencies | BMC extension metadata | partial |

Compliance note: this is a lightweight mapping proposal, not a validated CIDOC CRM profile. A cultural-heritage ontology expert should review class/property choices before publication claims rely on it.
