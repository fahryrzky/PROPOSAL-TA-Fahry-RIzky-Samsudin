import sys, os, re, json, hashlib, base64, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

session = requests.Session(impersonate='chrome120', doh_url='https://dns.google/dns-query')

targets = [
    {
        'key': 'xue2019electrospinning',
        'doi': '10.1021/acs.chemrev.8b00593',
        'filename': '[xue2019electrospinning] - Xue et al (2019) - Electrospinning and Electrospun Nanofibers Methods Materials and Applications (ChemRev).pdf'
    },
    {
        'key': 'gaaz2015properties',
        'doi': '10.3390/molecules201219884',
        'filename': '[gaaz2015properties] - Gaaz et al (2015) - Properties and Applications of Polyvinyl Alcohol Halloysite Nanotubes Nanocomposites.pdf'
    },
    {
        'key': 'antarnusa2022',
        'doi': '10.1016/j.jmmm.2022.169903',
        'filename': '[antarnusa2022] - Antarnusa et al (2022) - Synthesis of Fe3O4 at different reaction temperatures.pdf'
    },
    {
        'key': 'singhal2024food',
        'doi': '10.1016/j.bios.2023.115850',
        'filename': '[singhal2024food] - Singhal et al (2024) - Advances in electrochemical biosensors for formaldehyde detection.pdf'
    },
    {
        'key': 'sun2023optical',
        'doi': '10.1016/j.foodchem.2022.134235',
        'filename': '[sun2023optical] - Sun et al (2023) - Smartphone-integrated colorimetric sensor array for rapid detection of formaldehyde.pdf'
    },
    {
        'key': 'ardiyanti2025',
        'doi': '10.1007/s11220-025-00597-3',
        'filename': '[ardiyanti2025] - Ardiyanti et al (2025) - Facile and Fast Assay of Biomolecule Using ICs-Based GMR.pdf'
    }
]

def solve_altcha(r_html, current_url):
    ch_match = re.search(r'challengeurl\s*=\s*[\'"]([^\'"]+)[\'"]', r_html)
    if not ch_match:
        return False
    ch_url = ch_match.group(1)
    ch_id = ch_url.split('/')[-1]
    r_ch = session.get(f"https://sci-hub.ru{ch_url}")
    ch_data = r_ch.json()
    
    target = ch_data['challenge']
    salt = ch_data['salt']
    max_num = ch_data.get('maxNumber', 1000000)
    salt_bytes = salt.encode('utf-8')
    
    t0 = time.time()
    solution = None
    for n in range(max_num + 1):
        if hashlib.sha256(salt_bytes + str(n).encode('utf-8')).hexdigest() == target:
            solution = n
            break
    dt = int((time.time() - t0) * 1000)
    if solution is None:
        return False
        
    payload_obj = {
        "algorithm": ch_data['algorithm'],
        "challenge": target,
        "number": solution,
        "salt": salt,
        "signature": ch_data['signature'],
        "took": max(dt, 250)
    }
    payload_b64 = base64.b64encode(json.dumps(payload_obj, separators=(',', ':')).encode('utf-8')).decode('utf-8')
    sol_url = f"https://sci-hub.ru/captcha/solution/{ch_id}"
    r_sol = session.post(sol_url, json={"captcha": payload_b64}, headers={"Referer": current_url})
    return r_sol.json().get('success', False)

print("=== STARTING ROBUST SCI-HUB HARVESTER ===")
out_dir = "referensi"

for t in targets:
    key = t['key']
    doi = t['doi']
    dest = os.path.join(out_dir, t['filename'])
    if os.path.exists(dest) and os.path.getsize(dest) > 10000:
        print(f"[{key}] Already downloaded ({os.path.getsize(dest)} bytes)")
        continue
        
    print(f"\n[{key}] Requesting {doi} ...")
    paper_url = f"https://sci-hub.ru/{doi}"
    r = session.get(paper_url)
    
    if '<altcha-widget' in r.text:
        print("  Altcha challenge detected. Solving SHA-256 PoW...")
        if solve_altcha(r.text, paper_url):
            print("  Captcha solved successfully! Fetching paper...")
            time.sleep(1)
            r = session.get(paper_url)
        else:
            print("  Failed to solve captcha.")
            continue
            
    # Search for PDF link
    pdf_rel = None
    m = re.search(r'citation_pdf_url"\s+content="([^"]+)"', r.text)
    if m:
        pdf_rel = m.group(1)
    if not pdf_rel:
        m = re.search(r'(/storage/[^"\'\s>]+\.pdf)', r.text)
        if m:
            pdf_rel = m.group(1)
    if not pdf_rel:
        m = re.search(r'src=[\'"]([^\'"]+?\.pdf[^\'"]*)[\'"]', r.text)
        if m:
            pdf_rel = m.group(1)
    if not pdf_rel:
        m = re.search(r'//[^"\']+\.pdf', r.text)
        if m:
            pdf_rel = m.group(0)

    if pdf_rel:
        pdf_url = pdf_rel
        if pdf_url.startswith('//'):
            pdf_url = 'https:' + pdf_url
        elif pdf_url.startswith('/'):
            pdf_url = 'https://sci-hub.ru' + pdf_url
        print(f"  Downloading PDF: {pdf_url} ...")
        r_pdf = session.get(pdf_url, headers={"Referer": paper_url})
        if r_pdf.content.startswith(b'%PDF'):
            with open(dest, 'wb') as f:
                f.write(r_pdf.content)
            print(f"  [SUCCESS] Saved {dest} ({len(r_pdf.content)} bytes)")
        else:
            print(f"  [FAIL] Downloaded content is not PDF ({r_pdf.content[:20]})")
    else:
        title_snippet = r.text[r.text.find('<title>'):r.text.find('</title>')+8] if '<title>' in r.text else 'No title'
        print(f"  [NOTICE] No direct PDF link found. {title_snippet}")
    
    time.sleep(2)

print("\n=== HARVEST COMPLETE ===")
