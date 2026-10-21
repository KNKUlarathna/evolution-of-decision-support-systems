#!/usr/bin/env python3
"""Bounded normalized text-overlap check against available assessed working copies."""
from pathlib import Path
import collections
import json
import re
import subprocess
import unicodedata

root = Path(__file__).resolve().parent
source = (root / 'review.tex').read_text()
abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', source, re.S).group(1)
body = source.split(r'\begin{thebibliography}')[0] + r'\end{document}'
body = re.sub(r'\\cite\{[^}]+\}', '', body)
body = re.sub(r'\\begin\{figure\*\}.*?\\end\{figure\*\}', '', body, flags=re.S)
plain = abstract + '\n' + subprocess.run(['pandoc', '-f', 'latex', '-t', 'plain'],
    input=body, text=True, capture_output=True, check=True).stdout

def words(text):
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    return re.findall('[a-z0-9]+', unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower())

a = words(plain)
results = []
for record in json.loads((root / 'source-manifest.json').read_text()):
    variants = []
    pdf = Path(record['working_pdf'])
    if pdf.exists():
        for layout in [False, True]:
            command = ['pdftotext'] + (['-layout'] if layout else []) + [str(pdf), '-']
            run = subprocess.run(command, text=True, capture_output=True, check=True)
            variants.append(words(run.stdout))
    # Assessed OCR is important for scanned foundational texts.
    text_path = record.get('working_text')
    if text_path and Path(text_path).exists():
        variants.append(words(Path(text_path).read_text(errors='replace')))
    matches = set()
    examples = set()
    for b in variants:
        index = collections.defaultdict(list)
        for j in range(len(b)-7):
            index[tuple(b[j:j+8])].append(j)
        for i in range(len(a)-7):
            for j in index.get(tuple(a[i:i+8]), []):
                n = 8
                while i+n<len(a) and j+n<len(b) and a[i+n]==b[j+n]:
                    n += 1
                matches.update(range(i, i+n))
                examples.add(' '.join(a[i:i+n]))
    results.append({'key':record['key'], 'available_text_variants':len(variants),
                    'matched_draft_words_in_runs_at_least_8':len(matches),
                    'longest_matches':sorted(examples,key=lambda x:len(x.split()),reverse=True)[:8]})
output = {'date':'2026-10-21','draft_word_tokens':len(a),'source_count':len(results),
          'scope':'Abstract and body/tables; bibliography, citation commands and TikZ figure code excluded.',
          'method':'Unicode/lowercase normalization; punctuation ignored; line-end hyphenation joined; pdf reading-order/layout and available assessed OCR checked.',
          'limits':'Not a plagiarism score or novelty certificate. Does not detect all paraphrase, translated borrowing, inaccessible literature or extraction omissions.',
          'results':results}
(root / 'text-overlap-results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='results'},indent=2))
for result in results:
    if result['matched_draft_words_in_runs_at_least_8']:
        print(json.dumps(result))
