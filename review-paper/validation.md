# Validation and research boundary record

Completed 21 October 2026 for the complexity–data-feedback revision.

## Completed checks

- **Corpus identity:** 24 distinct included citation keys, reconciled aliases for overlapping research routes. Each included record has a full-text working copy, assessed-version metadata and source provenance. Unassessed candidates are separate; no download count is called a screened study population.
- **Argument checks:** separate AI-assisted reviews checked organizational theory, feedback/source fidelity, prior-review positioning and causal claims. Corrected the distinction between gross added work and net burden, resident-report assumptions, policy dependence versus sample independence, filtering versus task-complexity reduction, and the distinction between quantity-driven demand and observation/retraining feedback. These are internal checks, not external scholarly peer review.
- **Source fidelity:** the 14-interview/551-response Microsoft case details, health-case scope and formal/simulation evidence labels were checked against assessed sources. Foundational papers cite the actually read working-paper versions. The whole historical feedback closure is explicitly conjectural.
- **Citations:** all 24 bibliography entries are cited, every citation key resolves, and bibliography ordering follows first citation. References distinguish preprint/working-paper versions from final publications where relevant.
- **Document build:** `python3 build.py` successfully runs pdfLaTeX twice. No unresolved citations/cross-references or overfull boxes remain. Output is a 10-page IEEEtran journal-format PDF. The original figure is exported as PDF, PNG and editable TikZ.
- **Reading copy:** `python3 render_markdown.py` retains the abstract, numbered citations, three tables and embedded mechanism figure.
- **Visual inspection:** checked the first page, historical comparison table and two-panel mechanism figure at rendered page scale; corrected overlapping diagram labels before completion.
- **Bounded text overlap:** `python3 check_text_overlap.py` compares normalized abstract/body/table wording against the 24 included working texts, using reading-order/layout extraction and available OCR. No exact runs of 8 or more normalized words were found. Bibliography and figure code are excluded. This is not a plagiarism percentage, semantic-novelty result or exhaustive publication search. Full output is in `text-overlap-results.json`.
- **Repository hygiene:** existing source catalog, downloader, historic results CSV and original 38-PDF collection were not changed. `git diff --check` passes.

## Limits that remain

The manuscript is a critical integrative review with purposive, access-dependent selection. No complete historical causal loop is estimated, no new experiment or organization-level dataset is reported, and no meta-analytic effect is claimed. Some potentially relevant works remain inaccessible. Search/extraction records make those limitations visible.

Final authorship, venue selection, human scholarly verification and venue-specific submission compliance remain with the eventual submitting authors. An IEEE-style build is not IEEE acceptance or an independent guarantee of publication readiness.
