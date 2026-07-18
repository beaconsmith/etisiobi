# EXP-FRONTIER-004: Unicode Channel Risk Audit

## Question

Can Etisiobi detect hidden, invisible, private-use, tag, or control characters in
research outputs before public release?

## Motivation

GLOSSOPETRAE shows that symbolic systems and tokenizer-visible text can become
research instruments. Etisiobi should adapt that lesson defensively: public
research artifacts must be inspected for text visibility and portability risks
before publication.

## Command

```powershell
python scripts\audit_unicode_channel_risk.py
```

## Scope

The audit scans text-like files under:

- `papers/`
- `paper/`
- `research/`
- `outputs/`
- `obsidian_vault/`
- `benchmarks/`

## Success Criteria

- The audit completes.
- Findings are written as structured JSON and a human-readable report.
- UTF-16/non-UTF-8 files are separated from actual hidden/control-character
  findings.
- Interpretation remains defensive and does not claim covert-channel use.

## Non-Goals

- Do not construct covert-channel payloads.
- Do not publish monitor-evasion techniques.
- Do not interpret Unicode findings as malicious without evidence.

