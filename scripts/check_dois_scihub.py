import urllib.request, ssl, re, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()
dois = [
    '10.1016/j.jmmm.2022.169903',
    '10.1002/app.28648',
    '10.1016/j.heliyon.2023.e15193',
    '10.1021/acs.chemrev.8b00593',
    '10.3390/ijms25031668',
    '10.3390/molecules201219884'
]

for d in dois:
    url = f'https://sci-hub.ru/{d}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
            html = r.read().decode('utf-8', errors='ignore')
            print(f"=== DOI: {d} ===")
            matches = re.findall(r'//[^\s"\'<>]+\.pdf', html)
            print("  PDF matches:", matches)
            if not matches:
                if 'article not found' in html.lower():
                    print("  Status: Article not found on Sci-Hub")
                else:
                    title_m = re.search(r'<title>([^<]+)</title>', html)
                    print("  Page title:", title_m.group(1) if title_m else "No title")
    except Exception as e:
        print(f"{d} -> Error: {e}")
