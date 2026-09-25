import sys, re, time
from curl_cffi import requests

sys.stdout.reconfigure(encoding='utf-8')

session = requests.Session(impersonate='chrome120')

url = 'https://www.mdpi.com/1422-0067/25/3/1668/pdf'
r = session.get(url)
print("Initial status:", r.status_code)

match = re.search(r'URL=[\'"]([^\'"]+)[\'"]', r.text)
if match:
    refresh_url = match.group(1)
    if refresh_url.startswith('/'):
        refresh_url = 'https://www.mdpi.com' + refresh_url
    print("Following meta-refresh to:", refresh_url[:80], "...")
    # wait 5 seconds as specified by content="5; ..."
    print("Waiting 5 seconds...")
    time.sleep(5)
    r2 = session.get(refresh_url, headers={'Referer': url})
    print("Second status:", r2.status_code, "Length:", len(r2.content), "Header:", r2.content[:20])
    if r2.content.startswith(b'%PDF'):
        print("SUCCESS! PDF retrieved!")
    else:
        print("Snippet:", r2.text[:300])
