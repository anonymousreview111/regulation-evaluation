# Build & analysis pipeline

All scripts run from the repository root (`python tools/<script>.py`). Python via Anaconda;
LaTeX via MiKTeX. `paper_springer/` and `dist/` are generated and git-ignored.

## Primary build — assemble and compile the manuscript
| Order | Script | Purpose |
|------|--------|---------|
| 1 | `make_figures.py` | Regenerate the four figures (PRISMA, heatmap, cross-framework, gap) from the `corpus/` CSVs into `figures/`. |
| 2 | `build_springer.py` | Assemble the Springer (AIRE) manuscript from `paper/` + `springer_template/` + `references.bib` into `paper_springer/`. |
| 3 | *(in `paper_springer/`)* | `pdflatex main && bibtex main && pdflatex main && pdflatex main` |
| 4 | `make_packages.py` | Build `dist/AIRE_overleaf_springer.zip` (Overleaf upload) and `dist/AIRE_supplementary_information.zip` (data deposit). |

## Data regenerators (optional)
- `build_matrix.py` — regenerate the crosswalk CSVs and the base matrix/gap tables from source.
- `make_matrix_split.py` — regenerate the upright 3-panel Springer matrix (`tab_matrix_split.tex`).

> The `paper/tab_*.tex` tables carry hand-finalized captions and takeaways; re-running the
> regenerators overwrites those, so re-finalize captions afterward.

## QA checks
- `check_abstract.py` — abstract word count (AIRE limit 250) + no-citation / no-em-dash checks.
- `check_cites.py` — flags undefined / unused citation keys.
- `fix_bib_types.awk` — one-time utility that reclassified `@article` entries carrying a
  `booktitle` into the correct BibTeX type (apacite drops the venue otherwise).

## Double-blind deliverables
- `make_anon_mirror.py` — regenerate `dist/anon_repo/`, a fully anonymized mirror of the repo
  (redacts author/validator identity, affiliations, emails, named GitHub, and Zenodo DOIs).
- `make_anon_si.py` — build the anonymized Supplementary Information bundle.
