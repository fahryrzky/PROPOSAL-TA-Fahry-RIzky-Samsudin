import sys, re, json, hashlib, base64, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

doi = "10.1016/j.jmmm.2022.169903"
session = requests.Session(impersonate='chrome120', doh_url='https://dns.google/dns-query')

print(f"1. Fetching paper page for DOI: {doi} ...")
r = session.get(f"https://sci-hub.ru/{doi}")
print(f"  Status: {r.status_code}")

# Check if already direct PDF or captcha
if '<altcha-widget' in r.text:
    print("2. Altcha widget detected! Extracting challenge URL...")
    ch_match = re.search(r'challengeurl\s*=\s*[\'"]([^\'"]+)[\'"]', r.text)
    if not ch_match:
        print("  Could not find challengeurl!")
        sys.exit(1)
        
    ch_url = ch_match.group(1)
    ch_id = ch_url.split('/')[-1]
    print(f"  Challenge URL: {ch_url} (ID: {ch_id})")
    
    # Fetch challenge
    r_ch = session.get(f"https://sci-hub.ru{ch_url}")
    ch_data = r_ch.json()
    print(f"  Challenge data: algorithm={ch_data.get('algorithm')}, maxNumber={ch_data.get('maxNumber')}")
    
    # Solve PoW
    target = ch_data['challenge']
    salt = ch_data['salt']
    max_num = ch_data.get('maxNumber', 200000)
    salt_bytes = salt.encode('utf-8')
    
    t0 = time.time()
    solution = None
    for n in range(max_num + 1):
        h = hashlib.sha256(salt_bytes + str(n).encode('utf-8')).hexdigest()
        if h == target:
            solution = n
            break
            
    dt = int((time.time() - t0) * 1000)
    print(f"3. Solved PoW in {dt} ms! Solution number: {solution}")
    
    if solution is None:
        print("  Failed to find solution within maxNumber!")
        sys.exit(1)
        
    payload_obj = {
        "algorithm": ch_data['algorithm'],
        "challenge": target,
        "number": solution,
        "salt": salt,
        "signature": ch_data['signature'],
        "took": max(dt, 200)
    }
    payload_b64 = base64.b64encode(json.dumps(payload_obj, separators=(',', ':')).encode('utf-8')).decode('utf-8')
    
    # Post solution
    print("4. Posting solution...")
    sol_url = f"https://sci-hub.ru/captcha/solution/{ch_id}"
    r_sol = session.post(sol_url, json={"captcha": payload_b64}, headers={"Referer": f"https://sci-hub.ru/{doi}"})
    print(f"  Solution status: {r_sol.status_code}, response: {r_sol.text}")
    
    # Reload paper page
    print("5. Reloading paper page...")
    time.sleep(1)
    r = session.get(f"https://sci-hub.ru/{doi}")
    print(f"  Reload status: {r.status_code}")

# Check for PDF
print("6. Checking for PDF link on paper page...")
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
    print(f"  PDF URL FOUND: {pdf_url}")
    
    # Fetch PDF
    print("7. Fetching authentic PDF bytes...")
    r_pdf = session.get(pdf_url, headers={"Referer": f"https://sci-hub.ru/{doi}"})
    print(f"  PDF fetch status: {r_pdf.status_code}, bytes: {len(r_pdf.content)}, header: {r_pdf.content[:10]}")
    if r_pdf.content.startswith(b'%PDF'):
        out_file = r"referensi/[antarnusa2022] - Antarnusa et al (2022) - Synthesis of Fe3O4 at different reaction temperatures (JMMM).pdf"
        with open(out_file, 'wb') as f:
            f.write(r_pdf.content)
        print(f"  SUCCESS! Saved {out_file} ({len(r_pdf.content)} bytes)")
else:
    print("  No PDF link found yet. Text snippet:\n", r.text[:500])
