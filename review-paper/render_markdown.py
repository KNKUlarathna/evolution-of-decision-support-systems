#!/usr/bin/env python3
"""Render a reading copy while retaining numbered citations and the abstract."""
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
source = re.sub(r'\\cite\{([^}]+)\}', lambda m: ', '.join(f'[{numbers[k]}]' for k in m.group(1).split(',')), source)
source = source.replace(r'Table~\ref{tab:transitions}', 'Table I')
source = re.sub(r'\\begin\{thebibliography\}\{24\}', r'\\section*{References}\n\\begin{description}', source)
source = source.replace(r'\end{thebibliography}', r'\end{description}')
source = re.sub(r'\\bibitem\{([^}]+)\}', lambda m: r'\item[{[' + str(numbers[m.group(1)]) + ']}]', source)
result = subprocess.run(['pandoc', '--from=latex', '--to=gfm'], input=source, text=True, capture_output=True, check=True)
(root / 'review.md').write_text('# ' + title + '\n\nUnattributed review draft\n\n## Abstract\n\n' + abstract.strip() + '\n\n' + result.stdout)
print('Rendered review.md with numbered citations and references.')
