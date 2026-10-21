#!/usr/bin/env python3
"""Build the paper and export its original figure, keeping auxiliary files temporary."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='dss-review-') as directory:
    for _ in range(2):
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
             f'-output-directory={directory}', 'review.tex'], cwd=root,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode:
            print(result.stdout)
            raise SystemExit(result.returncode)
    log = (Path(directory) / 'review.log').read_text()
    problems = [line for line in log.splitlines() if
                'undefined' in line.lower() or 'Overfull' in line or
                'Rerun to get cross-references right' in line]
    if problems:
        raise SystemExit('Build validation failed:\n' + '\n'.join(problems))
    figure = re.search(r'(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})',
                       (root / 'review.tex').read_text(), re.S).group(1)
    figure_source = ('\\documentclass[tikz,border=4pt]{standalone}\n'
                     '\\usetikzlibrary{arrows.meta,positioning,fit}\n'
                     '\\begin{document}\n' + figure + '\n\\end{document}\n')
    figure_tex = Path(directory) / 'feedback-map.tex'
    figure_tex.write_text(figure_source)
    result = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                             str(figure_tex)], cwd=directory, capture_output=True, text=True)
    if result.returncode:
        print(result.stdout)
        raise SystemExit(result.returncode)
    subprocess.run(['pdftoppm', '-singlefile', '-scale-to', '2000', '-png',
                    str(Path(directory) / 'feedback-map.pdf'),
                    str(Path(directory) / 'feedback-map')], check=True, capture_output=True)
    figures = root / 'figures'
    figures.mkdir(exist_ok=True)
    for suffix in ['tex', 'pdf', 'png']:
        shutil.copy2(Path(directory) / ('feedback-map.' + suffix), figures / ('feedback-map.' + suffix))
    shutil.copy2(Path(directory) / 'review.pdf', root / 'review.pdf')
print('Built review.pdf and original figure; citations, cross-references and overflow checks passed.')
