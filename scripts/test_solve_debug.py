import sys, os, re, json, hashlib, base64, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

session = requests.Session(impersonate='chrome120', doh_url='https://dns.google/dns-query')

doi = "10.1021/acs.chemrev.8b00593"
paper_url = f"https://sci-hub.ru/{doi}"
r = session.get(paper_url)
print("Initial status:", r.status_code)

ch_match = re.search(r'challengeurl\s*=\s*[\'"]([^\'"]+)[\'"]', r.text)
if not ch_match:
    print("No challenge found in page")
    sys.exit()

ch_url = ch_match.group(1)
ch_id = ch_url.split('/')[-1]
print("Challenge URL:", ch_url, "ID:", ch_id)

r_ch = session.get(f"https://sci-hub.ru{ch_url}")
ch_data = r_ch.json()
print("Challenge data:", ch_data)

target = ch_data['challenge']
salt = ch_data['salt']
max_num = ch_data.get('maxNumber', 1000000)
print(f"Brute-forcing up to {max_num}...")

salt_bytes = salt.encode('utf-8')
t0 = time.time()
solution = None
for n in range(max_num + 1):
    if hashlib.sha256(salt_bytes + str(n).encode('utf-8')).hexdigest() == target:
        solution = n
        break

dt = int((time.time() - t0) * 1000)
print(f"Solved in {dt} ms. Solution: {solution}")

if solution is not None:
    payload_obj = {
        "algorithm": ch_data['algorithm'],
        "challenge": target,
        "number": solution,
        "salt": salt,
        "signature": ch_data['signature'],
        "took": max(dt, 300)
    }
    payload_b64 = base64.b64encode(json.dumps(payload_obj, separators=(',', ':')).encode('utf-8')).decode('utf-8')
    sol_url = f"https://sci-hub.ru/captcha/solution/{ch_id}"
    r_sol = session.post(sol_url, json={"captcha": payload_b64}, headers={"Referer": paper_url})
    print("Solution response:", r_sol.text)
    
    time.sleep(1)
    r2 = session.get(paper_url)
    print("Page after solve status:", r2.status_code, "Length:", len(r2.text))
    pdf_match = re.search(r'//[^"\']+\.pdf', r2.text) or re.search(r'src=[\'"]([^\'"]+?\.pdf[^\'"]*)[\'"]', r2.text)
    if pdf_match:
        print("PDF match:", pdf_match.group(0))
    else:
        print("Title:", r2.text[r2.text.find('<title>'):r2.text.find('</title>')])
