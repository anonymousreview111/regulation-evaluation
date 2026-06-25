# Evaluating High-Risk AI for Regulatory Conformity

Source, data, and reproducible build pipeline for the review article

> **Evaluating High-Risk AI for Regulatory Conformity: A Review of Technical Assessment Methods
> Mapped to the NIST AI RMF, EU AI Act, and ISO/IEC 42001**
> Target venue: *Artificial Intelligence Review* (Springer Nature).

The article organizes technical AI-evaluation methods into **twelve families** and proposes a
methods-to-requirements **crosswalk** that grades, by technical relevance (primary / supporting /
contextual), how each family can supply evidence for each requirement of the three frameworks,
followed by a gap analysis and a practitioner evidence playbook. Every cell is grounded in the
official clause text; the corpus, crosswalk, and coding/validation ledgers are released here for
full reproducibility.

## Repository structure
```
.
├── README.md                  this file
├── references.bib             bibliography (sn-apacite style)
├── paper/                     canonical LaTeX source
│   ├── main.tex               content master (abstract + body + \input order)
│   ├── sec_*.tex              section sources
│   └── tab_*.tex              table sources (hand-finalized captions/takeaways)
├── corpus/                    released data (see corpus/README_SI.md)
├── figures/                   generated figures (PRISMA, heatmap, cross-framework, gap)
├── springer_template/         Springer sn-jnl class + sn-apacite + support .sty
├── tools/                     build & analysis pipeline (see tools/README.md)
└── docs/                      protocol documentation (validation protocol)
```
`paper_springer/` (assembled manuscript) and `dist/` (zips, anon mirror) are generated and
git-ignored.

## Reproduce the manuscript
Requires MiKTeX (LaTeX) and Python via Anaconda (`matplotlib` for figures).
```bash
python tools/make_figures.py          # figures from corpus CSVs
python tools/build_springer.py        # assemble paper_springer/ from paper/ + template + bib
cd paper_springer
pdflatex main && bibtex main && pdflatex main && pdflatex main
```
The result is the ~57-page Springer manuscript. `python tools/make_packages.py` builds the
Overleaf upload and the Supplementary Information deposit. See **`tools/README.md`** for the full
pipeline and the optional data regenerators.

## Corpus / data dictionary
The released data lives in `corpus/` and is documented in `corpus/README_SI.md`. Highlights:
- `mapping_matrix.csv` — the methods × requirements crosswalk (the central artifact).
- `method_index.csv` — the twelve method families and their representative methods.
- `gap_analysis.csv` — aggregate coverage per requirement and the principal gaps.
- `coding_audit.csv` — second-coder reliability ledger.
- `external_validation.csv` — external-validation ledger (an external validator, not an author,
  blind to the first-pass codes, recoded a stratified sample).
- `search_strategy.txt` — per-database Boolean search strings and dates.
- `regulatory_clauses.json` — the official NIST / EU / ISO clause anchors used for grounding.
- `seed_fairness_corpus.bib` — the reused, previously verified fairness corpus.

## Reliability & external validation
The crosswalk codes were independently second-coded by a co-author and externally recoded by an
**external validator** (not an author of this study), blind to the first-pass codes. Cohen's and
quadratically-weighted κ are reported in the methodology and released in `corpus/coding_audit.csv`
and `corpus/external_validation.csv`. The validation instrument and protocol are in
`docs/VALIDATION_PROTOCOL.md`.

## Data availability
The corpus, crosswalk, search strings, and coding/validation ledgers are archived at Zenodo
(version DOI `[DOI withheld for double-blind review]`; concept DOI `[DOI withheld for double-blind review]`).

## Citation
```bibtex
@article{conformity2026review,
  title   = {Evaluating High-Risk AI for Regulatory Conformity: A Review of Technical
             Assessment Methods Mapped to the NIST AI RMF, EU AI Act, and ISO/IEC 42001},
  author  = {[author withheld] and [author withheld]},
  journal = {Artificial Intelligence Review (under review)},
  year    = {2026}
}
```

## License
The corpus and code are released for academic reuse; please cite the paper. (A formal `LICENSE`
file can be added on request — e.g. CC BY 4.0 for the data/text and MIT for the scripts.)

---
This review is a technical contribution and does **not** constitute legal advice.
