# BMC Goal Dependency Graph

```mermaid
graph LR
  G001["GOAL-001 BMC formal reconstruction"] --> G002["GOAL-002 count reconciliation"]
  G002 --> G003["GOAL-003 claim gate"]
  G002 --> G004["GOAL-004 grammar induction"]
  G004 --> G005["GOAL-005 compression / MDL"]
  G003 --> G006["GOAL-006 certainty propagation"]
  G006 --> G007["GOAL-007 knowledge graph"]
  G007 --> G008["GOAL-008 benchmarks"]
  G003 --> G009["GOAL-009 authority-aware review"]
  G006 --> G009
  G001 --> G010["GOAL-010 BMC-to-paper hyperloop"]
  G002 --> G010
  G003 --> G010
  G004 --> G010
  G005 --> G010
  G006 --> G010
  G007 --> G010
  G008 --> G010
  G009 --> G010
```

## Activation Rule

Activate only GOAL-001, GOAL-002, and GOAL-003 now. Do not activate GOAL-004 or GOAL-005 until GOAL-002 confirms stable count layers. Do not activate GOAL-010 until the claim gate has approved or blocked core claims.
