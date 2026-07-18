#!/usr/bin/env bash
set -euo pipefail

pdftotext -layout -enc UTF-8 research/pagc/primary_sources/nwagu_aneke/azuonye_1992.pdf experiments/EXP-0001-pagc-base-inventory-resolution/logs/azuonye_1992_pdftotext.txt
python scripts/phase5_arxiv_ready.py
