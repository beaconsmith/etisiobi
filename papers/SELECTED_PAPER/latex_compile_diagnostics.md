# LaTeX Compile Diagnostics

Direct chain:

| Command | Exit code |
|---|---:|
| `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | 0 |
| `bibtex main` | 0 |
| `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | 0 |
| `pdflatex -interaction=nonstopmode -halt-on-error main.tex` | 0 |

Direct chain passed: `True`

latexmk command: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

latexmk exit code: `1`

Classification: `local_tooling_failure_if_direct_chain_passes`

Interpretation: if the direct chain passes and latexmk fails locally, this sprint treats latexmk as a local MiKTeX/tooling issue rather than a source-package blocker.
