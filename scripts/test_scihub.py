import urllib.request, ssl, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
url = 'https://sci-hub.ru/10.3390/molecules201219884'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
        print("HTML len:", len(html))
        print("HTML head:", html[:300])
except Exception as e:
    print("Error:", e)
