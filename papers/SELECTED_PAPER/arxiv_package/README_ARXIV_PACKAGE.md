# arXiv Package

Human-review package for PAPER-003. Do not submit externally until `final_submission_readiness_decision.md` is upgraded by human authority, rights, and glyph/source review.

Compile chain used locally:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
