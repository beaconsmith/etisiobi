# EXP-FRONTIER-005 Runner Packet

This directory contains the frozen input packet for real Layer Promotion Error
evaluation.

## Files

- `frozen_annotation_queue.csv`: frozen cases copied from EXP-FRONTIER-003.
- `annotation_inputs/*.csv`: independent reviewer templates.
- `agent_run_templates/*.csv`: output templates for agent conditions.
- `manifest.json`: packet checksum and status.

## Rule

Do not score this experiment until `gold_labels.csv` and agent run files exist.
Synthetic labels are allowed only for pilot testing and must not be reported as
frontier evidence.
