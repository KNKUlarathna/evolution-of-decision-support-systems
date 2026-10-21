# Organizational complexity, data growth, and DSS evolution

**Organizational Complexity, Data Growth, and Decision Support Systems: A Critical Integrative Review of Their Feedback Dynamics**

- [Read the 10-page PDF](review.pdf)
- [Read on GitHub](review.md)
- [LaTeX manuscript](review.tex)
- [Assessed-source matrix](evidence-matrix.md)
- [Claim-to-evidence matrix](claim-evidence.md)
- [Source manifest and assessed versions](source-manifest.json)
- [Selection register](selection-register.csv) and [unassessed/excluded candidates](excluded-candidates.json)
- [Research protocol, search/retrieval logs and detailed extractions](supplement/README.md)
- [Validation record](validation.md)

The manuscript develops a conditional explanation of how organizational information requirements, data growth and DSS arrangements interact. It distinguishes quantity from meaning, theoretical mechanisms from organizational observations, and reinforcing pathways from simplification and stabilization. It includes 24 purposively selected full-text works, five historical configurations, three comparison/evidence tables, an original two-panel mechanism figure and five propositions.

It is a critical integrative review, not an exhaustive systematic review or a new empirical test of the complete historical feedback loop. Authorship remains unattributed as requested. The prior six-page draft is preserved in Git history at commit `704c71c`; this version replaces it on the `review-complexity-data-feedback` branch.

## Build and render

Requires Python 3, pdfLaTeX with the included IEEEtran class and standard `fontenc`, `inputenc`, `cite`, `booktabs`, `array`, `graphicx`, `tikz` and `hyperref` packages, the `standalone` class, Poppler `pdftoppm`, and Pandoc for Markdown. From this directory:

```sh
python3 build.py
python3 render_markdown.py
```

The build runs pdfLaTeX twice, rejects unresolved citations/references and overfull boxes, exports the original figure as PDF/PNG/TeX, and keeps auxiliary files temporary. The Markdown renderer preserves numbered references and embeds the figure. No network access is needed to build the checked-out manuscript.

## Sources and working library

New research working copies are stored outside the checkout under `/workspace/dss-research/`; metadata, hashes, provenance and page/section-located extraction are recorded here. Public source links allow readers to locate the assessed versions. New article PDFs are not automatically redistributed with this manuscript. The previously committed `DSS_PDFs/` collection is unchanged by this revision. PDF availability is not treated as evidence that a source is high quality.

## Format and submission status

The manuscript uses IEEEtran **journal** format with two columns, an abstract, index terms, numbered sections and references. It has not been submitted to or accepted by IEEE. A final target venue must determine length, anonymization, disclosure and reference requirements, and human authors must take responsibility for scholarly verification and submission. The paper contains an explicit AI-assistance statement.

The unmodified IEEEtran.cls version 1.8b was obtained from https://ctan.math.illinois.edu/macros/latex/contrib/IEEEtran/IEEEtran.cls; its embedded LaTeX Project Public License notice is retained. The original mechanism figure was generated for this manuscript, rather than reproduced from another paper.
