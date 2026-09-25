import urllib.request
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

doi = '10.3390/foods11091351'
url = f"https://api.europepmc.org/search?query=DOI:{doi}&format=json&resultType=core"
print(f"Querying Europe PMC for DOI: {doi}")
req = urllib.request.Request(url, headers={'User-Agent': 'ResearchAssistant/1.0'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        results = data.get('resultList', {}).get('result', [])
        print(f"Found {len(results)} results in Europe PMC.")
        if results:
            item = results[0]
            pmcid = item.get('pmcid')
            print(f"Title: {item.get('title')}")
            print(f"PMCID: {pmcid}")
            print(f"isOpenAccess: {item.get('isOpenAccess')}")
            if pmcid:
                pmc_pdf_url = f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"
                print(f"PMC PDF URL: {pmc_pdf_url}")
                pdf_req = urllib.request.Request(pmc_pdf_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(pdf_req, timeout=20) as p_resp:
                    pdf_bytes = p_resp.read()
                    print(f"Downloaded bytes: {len(pdf_bytes)}, starts with: {pdf_bytes[:10]}")
                    if pdf_bytes.startswith(b'%PDF'):
                        out_file = 'referensi/[rovina2022formaldehyde] - Rovina et al (2022) - Formaldehyde in Food Review (Foods).pdf'
                        with open(out_file, 'wb') as out_f:
                            out_f.write(pdf_bytes)
                        print(f"Saved {out_file} successfully ({len(pdf_bytes)/1024:.1f} KB)!")
except Exception as e:
    print(f"Error: {e}")
