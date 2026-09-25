import sys, os, re, json, hashlib, base64, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

targets = {
    'shi2008citric': {
        'doi': '10.1002/app.28648',
        'file': '[shi2008citric] - Shi et al (2008) - Citric acid poly vinyl alcohol composite films (JAPS).pdf'
    },
    'xue2019electrospinning': {
        'doi': '10.1021/acs.chemrev.8b00593',
        'file': '[xue2019electrospinning] - Xue et al (2019) - Electrospinning and electrospun nanofibers methods materials (ChemRev).pdf'
    },
    'gaaz2015properties': {
        'doi': '10.3390/molecules201219884',
        'file': '[gaaz2015properties] - Gaaz et al (2015) - Properties and applications of polyvinyl alcohol nanocomposites (Molecules).pdf'
    }
}

session = requests.Session(impersonate='chrome120', doh_url='https://dns.google/dns-query')

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
    max_num = ch_data.get('maxNumber', 300000)
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
        "took": max(dt, 200)
    }
    payload_b64 = base64.b64encode(json.dumps(payload_obj, separators=(',', ':')).encode('utf-8')).decode('utf-8')
    sol_url = f"https://sci-hub.ru/captcha/solution/{ch_id}"
    r_sol = session.post(sol_url, json={"captcha": payload_b64}, headers={"Referer": current_url})
    return r_sol.json().get('success', False)

print("=== HARVESTING FROM SCI-HUB WITH AUTOMATED ALTCHA POW SOLVER ===")
for key, item in targets.items():
    doi = item['doi']
    out_file = os.path.join('referensi', item['file'])
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"[{key}] Already exists ({os.path.getsize(out_file)} bytes)")
        continue
        
    print(f"\n[{key}] Requesting DOI: {doi} ...")
    paper_url = f"https://sci-hub.ru/{doi}"
    r = session.get(paper_url)
    
    if '<altcha-widget' in r.text:
        print(f"  Altcha widget detected. Solving PoW puzzle...")
        if solve_altcha(r.text, paper_url):
            print("  Captcha solved successfully! Reloading...")
            time.sleep(1)
            r = session.get(paper_url)
        else:
            print("  Failed to solve captcha.")
            continue
            
    # Extract PDF
    pdf_match = re.search(r'//[^"\']+\.pdf', r.text)
    if not pdf_match:
        pdf_match = re.search(r'src=[\'"]([^\'"]+?\.pdf[^\'"]*)[\'"]', r.text)
    if not pdf_match:
        pdf_match = re.search(r'location\.href\s*=\s*[\'"]([^\'"]+)[\'"]', r.text)
        
    if pdf_match:
        pdf_url = pdf_match.group(0).strip('\'"')
        if pdf_url.startswith('//'):
            pdf_url = 'https:' + pdf_url
        elif pdf_url.startswith('/'):
            pdf_url = 'https://sci-hub.ru' + pdf_url
        print(f"  PDF URL found: {pdf_url}")
        r_pdf = session.get(pdf_url, headers={"Referer": paper_url})
        if r_pdf.content.startswith(b'%PDF'):
            with open(out_file, 'wb') as f:
                f.write(r_pdf.content)
            print(f"  SUCCESS! Downloaded authentic PDF ({len(r_pdf.content)} bytes)")
        else:
            print(f"  Failed: Response not PDF ({r_pdf.content[:20]})")
    else:
        if "not available" in r.text.lower():
            print(f"  Not available on Sci-Hub.")
        else:
            print(f"  No PDF found. Title snippet: {r.text[r.text.find('<title>'):r.text.find('</title>')]}")
    time.sleep(2)

print("\n=== FINISHED SCI-HUB HARVEST ===")
