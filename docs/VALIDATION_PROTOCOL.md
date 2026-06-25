# Independent validation — instructions for the expert (and the exact prompt)

This sheet asks an **independent expert** (not an author) to judge a 40-cell stratified sample
of our AI-evaluation-to-regulation crosswalk. It is the external-validation step reviewers
asked for. Two parts below: **(A)** what you ([author withheld]) attach and where it lives, and **(B)** the
self-contained instructions/prompt to send the expert verbatim.

---

## A. Files (for the author — what to send, where it is)

- **The instrument to send the expert (the only file they need):**
  `C:\Users\rohit\Documents\Research Papers\ResearchPaper10-Regulation evaluation review\corpus\validator_sheet.csv`
  40 rows; the expert fills three columns: `EXPERT_CODE`, `CONFIDENCE`, `EXPERT_COMMENT`.
- **Do NOT send** these (they contain our own codes — the check must stay blind):
  `…\corpus\coding_audit.csv` and `…\corpus\mapping_matrix.csv`.
- **When the filled sheet comes back, save it as:**
  `C:\Users\rohit\Documents\Research Papers\ResearchPaper10-Regulation evaluation review\corpus\validator_sheet_<name>_completed.csv`
  then tell me and I'll compute agreement (κ) and update the manuscript's reliability subsection.

The recruitment email is in
`C:\Users\rohit\Documents\Research Papers\ResearchPaper10-Regulation evaluation review\VALIDATOR_RECRUITMENT.md`.

---

## B. Instructions / prompt to send the expert (paste verbatim)

> **What this is.** Attached is a spreadsheet (`validator_sheet.csv`) with 40 rows. Each row
> pairs one *technical AI-evaluation method* with one *requirement* from a governance framework
> (NIST AI RMF, the EU AI Act, or ISO/IEC 42001). Your task is to judge, for each row, **how
> relevant that method's output is as technical evidence for that requirement** — independently,
> using your own expertise. There are no "correct" answers to recall; we want your judgment.
>
> **What each row already gives you (read-only columns — do not edit):**
> - `cell_id` — row identifier (e.g., C001).
> - `method_family` — the evaluation method (e.g., "M3 Robustness & distribution shift").
> - `what_this_method_produces` — plain-language description of the method's output.
> - `framework` — NIST AI RMF / EU AI Act / ISO/IEC 42001.
> - `requirement` — the specific clause/function/control.
> - `what_the_requirement_asks_for` — plain-language description of the obligation.
>
> **What you fill in (three columns):**
> 1. **`EXPERT_CODE`** — choose exactly one:
>    - **primary** — this method's output is a *core / leading* source of technical evidence the
>      requirement chiefly asks for.
>    - **supporting** — it provides *partial or corroborating* evidence, but is insufficient on
>      its own.
>    - **contextual** — it is only *indirectly* related; it informs but does not evidence the
>      requirement.
>    - **not-applicable** — no meaningful relevance.
> 2. **`CONFIDENCE`** — high / medium / low.
> 3. **`EXPERT_COMMENT`** — optional; one line, especially if you disagree or it's borderline.
>
> **How to judge "relevance" (the rubric we used — apply it your own way):** ask *"if a deployer
> handed this method's output to an assessor as evidence for this requirement, how far would it
> go?"* Core evidence → primary; helps but not enough → supporting; merely informative →
> contextual; unrelated → not-applicable. Judge **technical relevance only** — not whether it
> would satisfy the law (that depends on thresholds and the conformity route, which are out of
> scope here).
>
> **Rules.** Work top to bottom; ~30–45 minutes. No external lookups are needed — the two
> plain-language columns are enough. Please **do not** consult the authors' codes (we are keeping
> this blind). Fill every row. Save the file and send it back. We will report inter-rater
> agreement in aggregate and acknowledge your contribution (or offer co-authorship for a larger
> role, by agreement).
>
> **Scale, one line:** primary = core evidence · supporting = partial/corroborating · contextual
> = indirect · not-applicable = none.

---

## C. What happens next (author + assistant)
Once the completed sheet is back at
`…\corpus\validator_sheet_<name>_completed.csv`, the assistant will: align it with the
authors' first-pass codes in `corpus\coding_audit.csv`; compute raw agreement, adjacency-weighted
agreement, and Cohen's / quadratically-weighted κ; adjudicate confident disagreements; and update
the Methodology reliability subsection (`paper\sec_method.tex`) plus the Acknowledgements/
Declarations. That turns the paper's current "external validation is the key next step" into
"externally validated by N independent expert(s)."
