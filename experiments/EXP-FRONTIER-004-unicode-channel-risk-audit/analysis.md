# EXP-FRONTIER-004 Analysis

## Result

The encoding-aware audit scanned 939 text-like files. It found:

- 936 UTF-8 files.
- 3 UTF-16LE files with BOM markers.
- 2 real `format_or_control` findings, both in
  `research/pagc/sources/pagc_library/african_linguistics___igbo_phonology.md`.

The initial non-encoding-aware scan produced 40,187 apparent findings because it
read UTF-16 files as UTF-8. The audit script was corrected to decode UTF-16 files
before classifying characters. This matters because an A-grade lab should not
turn an encoding artifact into a false research result.

## Interpretation

This experiment does not establish covert-channel activity. It establishes a
defensive control:

```text
public research artifact -> text visibility audit -> portability/control-character report
```

That control is useful for PDFs, Markdown papers, source dossiers, benchmark
cases, and release packages.

## Effect On Frontier Research

The useful GLOSSOPETRAE lesson for Etisiobi is not covert-channel construction.
It is that symbolic systems should be evaluated through deterministic tasks,
raw traces, and visibility/safety audits. EXP-FRONTIER-004 converts that lesson
into a concrete lab control.

## Remaining Work

- Decide whether the two control characters in the PAGC source note are source
  encoding artifacts or should be normalized in a derived cleaned copy.
- Convert the three UTF-16 Markdown drafts to UTF-8 before any public release
  package.
- Add this audit to release preflight for future papers and benchmark datasets.

