import re
import os
import json

active_files = [
    'Header/sampul.tex',
    'Header/Keaslian.tex',
    'Header/persetujuan.tex',
    'Header/prakata.tex',
    'Isi/Pendahuluan.tex',
    'Isi/Tinjauan Pustaka.tex',
    'Isi/Metode Penelitian.tex'
]

cites = set()
for f in active_files:
    if os.path.exists(f):
        content = open(f, encoding='utf-8').read()
        for group in re.findall(r'\\cite\{([^}]+)\}', content):
            for c in group.split(','):
                cites.add(c.strip())

bib_str = open('references.bib', encoding='utf-8').read()
raw_entries = re.split(r'\n@', bib_str)
parsed = {}

for e in raw_entries:
    m = re.match(r'([a-zA-Z]+)\s*\{\s*([^,]+),', e)
    if m:
        etype = m.group(1).lower()
        key = m.group(2).strip()
        if key in cites:
            def get_field(fieldname):
                # Match fieldname = {val} or fieldname = "val"
                pat = rf'{fieldname}\s*=\s*[\"{{](.*?)[\"}}]'
                found = re.search(pat, e, re.DOTALL | re.IGNORECASE)
                if found:
                    return found.group(1).replace('\n', ' ').strip(' {}')
                return ''

            parsed[key] = {
                'key': key,
                'type': etype,
                'title': get_field('title'),
                'author': get_field('author'),
                'year': get_field('year'),
                'journal': get_field('journal') or get_field('booktitle'),
                'doi': get_field('doi'),
                'url': get_field('url'),
                'publisher': get_field('publisher'),
                'organization': get_field('organization'),
                'school': get_field('school')
            }

print(f"Total active cites: {len(cites)}")
print(f"Matched in references.bib: {len(parsed)}")

# Print DOI coverage
doi_count = sum(1 for v in parsed.values() if v['doi'])
url_count = sum(1 for v in parsed.values() if v['url'])
print(f"Entries with DOI: {doi_count}")
print(f"Entries with URL: {url_count}")

with open('scripts/active_references.json', 'w', encoding='utf-8') as f:
    json.dump(parsed, f, indent=2)
