# Supplementary Information — verified corpus, crosswalk, and coding ledger

Companion data for *Evaluating High-Risk AI for Regulatory Conformity: A Review of Technical
Assessment Methods Mapped to the NIST AI RMF, EU AI Act, and ISO/IEC 42001.*

This bundle makes the review's central artifact fully inspectable. It is released so that the
proposed methods-to-requirements crosswalk can be externally validated rather than taken on
trust. Nothing here reproduces protected standard text; ISO/IEC 42001 is referenced only via
its public Annex A control structure and secondary analyses.

## Files

- **`mapping_matrix.csv`** — the machine-readable crosswalk. Rows are the twelve method
  families (M1–M12); columns are the 22 requirement points (NIST AI RMF functions/subcategories,
  EU AI Act high-risk Articles 9–15, ISO/IEC 42001 Annex A controls). Each cell is a
  technical-relevance code: `D` = primary, `P` = supporting, `I` = contextual, blank = not
  applicable. These are an engineering interpretation of relevance, not a legal determination.

- **`coding_audit.csv`** — the cell-level coding/reliability ledger. For each sampled cell:
  first-pass code, independent second-coder code, agreement flag, final adjudicated code, the
  adjudication basis, and a note. A summary block reports raw exact agreement (52.5%),
  adjacency-weighted agreement (76.2%), and the number of cells changed in adjudication.

- **`coding_sheet_secondcoder.csv`** — the blind second-coder worksheet (stratified 20% sample,
  40 cells) with the neutral per-cell prompts the second coder saw, and no access to the
  first-pass codes.

- **`external_validation.csv`** — the independent external-validation ledger: an external
  reviewer (an external reviewer, ORCID [ORCID withheld]; not an author), blind to the first-pass
  codes, recoded the same 40-cell sample. Columns give the first-pass code, the external code,
  confidence, agreement flag, adjacency, and the reviewer's comment; the SUMMARY row reports
  57.5% exact / 85.8% adjacency-weighted agreement, Cohen's kappa 0.23, quadratically-weighted
  kappa 0.49.

- **`gap_analysis.csv`** — per-requirement coverage-breadth ratings (broad / moderate / narrow)
  and the aggregate relevance scores plotted in the gap figure.

- **`method_index.csv`** — the released method index: 147 verified method references
  (141 from the structured search across families M1, M3–M11, and governance/positioning,
  plus 6 privacy-evaluation references for M12), each with key, family, year, identifier,
  and title. The reused agent-fairness corpus (M2, 202 entries) is released separately in
  `seed_fairness_corpus.bib`; with the 6 official texts the full corpus is ≈355 records.

- **`search_strategy.txt`** — the executable per-database search strings, date ranges, and
  inclusion/exclusion criteria for the structured search.

- **`regulatory_clauses.json`** — the official clause anchors (NIST subcategory IDs, EU Article
  numbers, ISO Annex A control IDs) used as the crosswalk columns.

- **`references.bib`** — the verified bibliography. Every entry was checked against its primary
  source during an adversarial citation-verification pass.

## Reproducing the figures and tables
The crosswalk figures and the matrix/gap tables are regenerated from `mapping_matrix.csv` and
`gap_analysis.csv` by the scripts in `tools/` (`build_matrix.py`, `make_matrix_split.py`,
`make_figures.py`). See the repository for the build.

## Citation
If you use this artifact, please cite the article and this dataset (DOI to be assigned on
deposit).
