# Evolution of Decision Support Systems

The literature catalog contains 67 entries, including 42 with PDF links.

## Download papers

Requires Python 3 and network access to the paper hosts. No third-party Python packages are required.

```sh
python download_papers.py --all
```

PDFs are saved under `DSS_PDFs/`, grouped by category. The script writes `DSS_Download_Results.csv`.

## Current run

Command: `python download_papers.py --all --retries 1 --timeout 10`

All 42 downloads failed with `Operation not permitted` in the execution environment. The paper hosts are outside its allowed network list. No PDFs were downloaded. The CSV records these failed attempts; these errors do not establish that the source links are invalid.
