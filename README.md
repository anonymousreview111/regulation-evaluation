# Evaluating High-Risk AI for Regulatory Conformity

Source, data, and build pipeline for the review article *"Evaluating High-Risk AI for
Regulatory Conformity: A Review of Technical Assessment Methods Mapped to the NIST AI RMF,
EU AI Act, and ISO/IEC 42001"* (target venue: *Artificial Intelligence Review*, Springer Nature).

The article organizes technical AI-evaluation methods into twelve families and proposes a
methods-to-requirements **crosswalk** grading, by technical relevance (primary / supporting /
contextual), how each family can supply evidence for each requirement of the three frameworks,
plus a gap analysis and a practitioner evidence playbook.

## Repository layout
- **`paper/`** — canonical LaTeX source: `main.tex` (content master) + `sec_*.tex` sections +
  `tab_*.tex` tables. (The Springer manuscript is generated from these; see below.)
- **`references.bib`** — bibliography (style: `sn-apacite`).
- **`corpus/`** — released data: the crosswalk (`mapping_matrix.csv`), method index
  (`method_index.csv`), gap analysis (`gap_analysis.csv`), second-coder ledger
  (`coding_audit.csv`), independent external-validation ledger (`external_validation.csv`),
  reused fairness corpus (`seed_fairness_corpus.bib`), search strategy (`search_strategy.txt`),
  regulatory clause anchors (`regulatory_clauses.json`), and the validation instrument
  (`validator_sheet.csv`). See `corpus/README_SI.md`.
- **`figures/`** — generated figures (PRISMA flow, heatmap, cross-framework, gap).
- **`springer_template/`** — Springer Nature `sn-jnl` class and style files.
- **`tools/`** — the build/QA pipeline (see below).

## Build (MiKTeX + Python via Anaconda)
Primary path — assemble and compile the Springer manuscript from the committed `paper/` sources:
```
python tools/make_figures.py        # regenerate the figures from the corpus CSVs
python tools/build_springer.py      # assemble the manuscript into paper_springer/
cd paper_springer && pdflatex main && bibtex main && pdflatex main && pdflatex main
python tools/make_packages.py       # build the Overleaf upload + Supplementary Information zips
```
`paper_springer/` and `dist/` are generated artifacts (git-ignored).

Data regenerators (optional; the `paper/tab_*.tex` files have hand-finalized captions/takeaways,
so re-running these overwrites those and the base tables must be re-finalized):
`tools/build_matrix.py` (crosswalk CSVs + base matrix/gap tables) and
`tools/make_matrix_split.py` (the upright 3-panel Springer matrix).
For a double-blind anonymized Supplementary Information bundle, use `tools/make_anon_si.py`.

## Reliability / validation
The crosswalk codes were independently second-coded by a co-author and externally recoded by an
independent reviewer (not an author), blind to the first-pass codes. Agreement statistics
(Cohen's and quadratically-weighted κ) are reported in the methodology and released in
`corpus/coding_audit.csv` and `corpus/external_validation.csv`.

## Data availability
The corpus, crosswalk, search strings, and coding/validation ledgers are archived at Zenodo
(version DOI `[DOI withheld for double-blind review]`; concept DOI `[DOI withheld for double-blind review]`).

This review is a technical contribution and does **not** constitute legal advice.
