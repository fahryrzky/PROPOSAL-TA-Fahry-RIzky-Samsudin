import urllib.request, ssl, json, sys
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()

dois = {
    'Turkoglu2024': '10.3390/ijms25031668',
    'gaaz2015properties': '10.3390/molecules201219884',
    'liu2024review': '10.3390/batteries10080271',
    'zhu2023': '10.1016/j.heliyon.2023.e15193',
    'xue2019electrospinning': '10.1021/acs.chemrev.8b00593',
    'shi2008citric': '10.1002/app.28648',
    'millman2007': '10.1109/MCSE.2007.58',
    'antarnusa2022': '10.1016/j.jmmm.2022.169903',
    'ardiyanti2025': '10.1007/s11220-025-00597-3',
    'singhal2024food': '10.1016/j.bios.2023.115850',
    'sun2023optical': '10.1016/j.foodchem.2022.134235',
    'shylu2020power': '10.12928/TELKOMNIKA.v18i5.14034'
}

for k, d in dois.items():
    try:
        url = f'https://api.unpaywall.org/v2/{d}?email=fahry@uinsgd.ac.id'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
            data = json.loads(r.read().decode('utf-8'))
            is_oa = data.get('is_oa')
            best = data.get('best_oa_location') or {}
            pdf_url = best.get('url_for_pdf')
            landing = best.get('url_for_landing_page')
            oa_locations = data.get('oa_locations') or []
            print(f"[{k}] OA={is_oa} | Best PDF={pdf_url}")
            for loc in oa_locations[:3]:
                if loc.get('url_for_pdf') and loc.get('url_for_pdf') != pdf_url:
                    print(f"    Alt PDF: {loc.get('url_for_pdf')}")
    except Exception as e:
        print(f"[{k}] {d} -> {e}")
