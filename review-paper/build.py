#!/usr/bin/env python3
"""Build the IEEE-style PDF without leaving auxiliary files in the checkout."""
from pathlib import Path
import shutil
import subprocess
import tempfile

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix="dss-review-") as directory:
    for _ in range(2):
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={directory}", "review.tex"],
            cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        if result.returncode:
            print(result.stdout)
            raise SystemExit(result.returncode)
    log = (Path(directory) / "review.log").read_text()
    problems = [line for line in log.splitlines() if
                "undefined" in line.lower() or "Overfull" in line or
                "Rerun to get cross-references right" in line]
    if problems:
        raise SystemExit("Build validation failed:\n" + "\n".join(problems))
    shutil.copy2(Path(directory) / "review.pdf", root / "review.pdf")
print("Built review.pdf; citations, references, and box overflow checks passed.")
