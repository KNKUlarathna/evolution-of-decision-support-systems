# DSS evolution review paper

An unattributed critical narrative review focused on why each major DSS approach emerged: the prior limitation, contribution of computational capacity, architectural change, and unresolved decision requirement.

- [Read the PDF](review.pdf)
- [Read the editable manuscript](review.md)
- [LaTeX source](review.tex)
- [Source evidence matrix](evidence-matrix.md)

The manuscript uses the unmodified IEEEtran conference class, two columns, an abstract and index terms, numbered sections, a comparison table, and numbered references. It is an IEEE-style review draft, not an accepted paper or a claim of compliance with a particular journal’s submission rules. Authorship is intentionally unattributed. It discloses AI assistance and the limits of its narrative review method. The 24 references are purposefully selected; the paper does not claim a new systematic search, experiments, or a comprehensive 2026 survey.

## Build

Requires Python 3 (for this command wrapper), pdfLaTeX and the standard LaTeX `fontenc`, `cite`, `booktabs`, `array`, and `hyperref` packages. No network access is required after checkout because IEEEtran.cls is included.

From this directory:

```sh
python3 build.py
```

Auxiliary files go to a temporary directory. The command runs pdfLaTeX twice, rejects unresolved citations/references and overfull boxes, and copies the completed PDF here. To regenerate the reading copy (requires Pandoc):

```sh
python3 render_markdown.py
```

The PDF is the authoritative formatted artifact; the Markdown is a convenience reading copy.

## Template provenance

`IEEEtran.cls` is version 1.8b, retrieved unchanged from the CTAN mirror at https://ctan.math.illinois.edu/macros/latex/contrib/IEEEtran/IEEEtran.cls. Its embedded LaTeX Project Public License notice is retained. The class is not authored by this repository’s owner. No IEEE logo or claim of IEEE endorsement is used.

## Before submission

The eventual author should review the argument and original sources, provide authorship and affiliations, choose a target venue, check its length and reference rules, and confirm the venue’s current AI disclosure requirements. The draft makes no claim that cited benchmark improvements demonstrate organizational decision quality.
