# Evolution of Decision Support Systems

The current review examines how organizational complexity, data growth and decision-support arrangements can reinforce or balance one another over time.

- [Read the review paper (PDF)](review-paper/review.pdf)
- [Read the paper on GitHub](review-paper/review.md)
- [Evidence, source records and build instructions](review-paper/README.md)

The manuscript uses IEEE-style journal formatting. It draws on 24 purposively selected, full-text-assessed works and distinguishes historical interpretation, organizational cases, technical mechanisms, theory and simulation. Authorship remains unattributed.

## Literature collection

`DSS_Evolution_Literature.json` is the original 67-entry discovery catalog, including 42 direct PDF links. `DSS_PDFs/` contains 38 previously downloaded papers, grouped by category. Additional research working copies were acquired for the revised review; their versions, provenance, access status and evidence are recorded under `review-paper/`.

`DSS_Download_Results.csv` preserves an earlier blocked run and does not describe the present PDF collection.

## Original downloader

Python 3 and network access to the paper hosts are required; there are no third-party Python dependencies. The original command is:

```sh
python3 download_papers.py --all
```

It writes PDFs under `DSS_PDFs/` and overwrites `DSS_Download_Results.csv`. For an exploratory run that preserves those repository files, copy the script and catalog into a separate working directory before running it.
