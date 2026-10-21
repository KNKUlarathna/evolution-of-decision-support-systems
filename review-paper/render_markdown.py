#!/usr/bin/env python3
"""Render a reading copy with numbered references and an exported mechanism figure."""
from pathlib import Path
import json
import re
import subprocess

root = Path(__file__).resolve().parent
source = (root / 'review.tex').read_text()
order = json.loads((root / 'reference-order.json').read_text())
numbers = {key: i for i, key in enumerate(order, 1)}
title = re.search(r'\\title\{([^}]+)\}', source).group(1)
abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1)
source = re.sub(r'\\IEEEPARstart\{([^}]+)\}\{([^}]+)\}', lambda m: m.group(1)+m.group(2), source)
source = re.sub(r'\\cite\{([^}]+)\}', lambda m: ', '.join(f'[{numbers[k]}]' for k in m.group(1).split(',')), source)
for key, label in [('tab:prior', 'I'), ('tab:history', 'II'), ('tab:claims', 'III')]:
    source = source.replace(r'Table~\ref{' + key + '}', 'Table ' + label)
source = source.replace(r'Figure~\ref{fig:mechanisms}', 'Figure 1')
source = re.sub(r'\\begin\{figure\*\}.*?\\end\{figure\*\}', '\nDSSFIGUREPLACEHOLDER\n', source, flags=re.S)
captions = re.findall(r'\\begin\{table\*\}.*?\\caption\{([^}]+)\}', source, re.S)
for i, caption in enumerate(captions, 1):
    source = source.replace(r'\caption{' + caption + '}', '\nDSSTABLECAPTION' + str(i) + '\n', 1)
source = source.replace(r'\begin{IEEEkeywords}', r'\paragraph{Index terms}').replace(r'\end{IEEEkeywords}', '')
source = re.sub(r'\\begin\{thebibliography\}\{\d+\}', r'\\section*{References}\n\\begin{description}', source)
source = source.replace(r'\end{thebibliography}', r'\end{description}')
source = re.sub(r'\\bibitem\{([^}]+)\}', lambda m: r'\item[{[' + str(numbers[m.group(1)]) + ']}]', source)
result = subprocess.run(['pandoc', '--from=latex', '--to=gfm', '--wrap=none'], input=source, text=True, capture_output=True, check=True)
text = result.stdout.replace('<div class="table*">', '').replace('</div>', '').replace('DSSFIGUREPLACEHOLDER', '![Figure 1: Conditional mechanism map separating organizational demand and data growth from endogenous observation feedback.](figures/feedback-map.png)\n\n*Evidence labels: T theory; H history; A architecture; E organizational cases; F formal analysis; S simulation; X cross-study conjecture. Arrows are conditional; the complete historical loop is not causally established.*')
for i, caption in enumerate(captions, 1):
    text = text.replace('DSSTABLECAPTION' + str(i), '**Table ' + ['I', 'II', 'III'][i-1] + '. ' + caption + '**')
(root / 'review.md').write_text('# ' + title + '\n\nUnattributed review manuscript\n\n## Abstract\n\n' + abstract.strip() + '\n\n' + text)
print('Rendered review.md with numbered citations, references, and the mechanism figure.')
