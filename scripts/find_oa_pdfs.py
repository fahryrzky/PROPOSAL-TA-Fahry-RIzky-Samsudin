import urllib.request, json, ssl

ctx = ssl._create_unverified_context()

dois = {
    'wang2021mos': '10.1016/j.snb.2021.129651',
    'singhal2024food': '10.1016/j.bios.2023.115850',
    'sun2023optical': '10.1016/j.foodchem.2022.134235',
    'antarnusa2022': '10.1016/j.jmmm.2022.169903',
    'ardiyanti2025': '10.1007/s11220-025-00597-3',
    'xue2019electrospinning': '10.1021/acs.chemrev.8b00593',
    'Turkoglu2024': '10.3390/ijms25031668',
    'shi2008citric': '10.1002/app.28648',
    'birck2014citric': '10.3144/expresspolymlett.2014.95',
    'zhu2023': '10.1016/j.heliyon.2023.e15193',
    'shylu2020power': '10.12928/TELKOMNIKA.v18i5.14034',
    'gaaz2015properties': '10.3390/molecules201219884',
    'millman2007': '10.1109/MCSE.2007.58',
    'liu2024review': '10.3390/batteries10080271',
    'sun2022review': '10.1002/aesr.202100191'
}

for k, doi in dois.items():
    try:
        url = f'https://api.openalex.org/works/https://doi.org/{doi}'
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:fahry@uinsgd.ac.id'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            data = json.loads(r.read().decode('utf-8'))
            oa = data.get('open_access', {})
            is_oa = oa.get('is_oa')
            best_loc = data.get('best_oa_location') or {}
            pdf = best_loc.get('pdf_url')
            landing = best_loc.get('landing_page_url')
            print(f"[{k}] OA={is_oa} | PDF={pdf} | Landing={landing}")
    except Exception as e:
        print(f"[{k}] Error: {e}")
