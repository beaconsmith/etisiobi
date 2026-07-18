---
type: interface_index
program: nwagu_aneke_frontier
status: active_internal_with_scored_usability_packet
created: "2026-06-22"
updated: "2026-06-22T18:34:57+01:00"
goal: GOAL-FRONTIER-001
---

# Nwagu Aneke Interfaces

This directory holds internal interface outlines for making Nwagu Aneke research
layers legible without promoting restricted, derived, speculative, or applied
records into source facts.

No source images, restricted manuscript content, or publication-ready figures
belong here until rights and authority review support them.

## Artifacts

| Artifact | Status | Purpose |
|---|---|---|
| `count_layer_view_outline.md` | first_outline_complete | Static outline for a layer-aware count-model view driven by `claim_layer_fixtures.jsonl`. |
| `count_layer_data_to_view_map.jsonl` | first_map_complete | Maps fixture records to target panels, required visible labels, forbidden display language, and blocked public-release conditions. |
| `count_layer_static_prototype.html` | internal_static_prototype | File-openable rights-safe prototype with layer filters and no source images or restricted glyphs. |
| `usability/` | protocol_ready_with_scorer_no_human_results | Comprehension-test packet, run sheet, scoring guide, response directory, and scorer for checking whether readers keep `26/208` source-observed and `27/216` derived. |

## Validator

Run:

```powershell
python scripts\validate_count_layer_view_map.py
python scripts\validate_count_layer_static_prototype.py
python scripts\validate_count_layer_usability_packet.py
python tests\research\test_count_layer_comprehension_scoring.py
```

## Operating Rule

Interfaces are readers for the evidence system, not evidence themselves. A view
may make distinctions easier to understand, but it cannot strengthen a claim's
evidence layer.
