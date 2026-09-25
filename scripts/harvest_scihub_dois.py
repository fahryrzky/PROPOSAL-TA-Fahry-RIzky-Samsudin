import urllib.request, ssl, re, os, sys, time
sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl._create_unverified_context()

targets = {
    'singhal2024food': {
        'doi': '10.1016/j.bios.2023.115850',
        'filename': '[singhal2024food] - Singhal et al (2024) - Advances in electrochemical biosensors for formaldehyde detection (Biosens Bioelectron).pdf'
    },
    'sun2023optical': {
        'doi': '10.1016/j.foodchem.2022.134235',
        'filename': '[sun2023optical] - Sun et al (2023) - Smartphone-integrated colorimetric sensor array for formaldehyde in meat (Food Chem).pdf'
    },
    'antarnusa2022': {
        'doi': '10.1016/j.jmmm.2022.169903',
        'filename': '[antarnusa2022] - Antarnusa et al (2022) - Synthesis of Fe3O4 and GMR bio-detection applications (JMMM).pdf'
    },
    'ardiyanti2025': {
        'doi': '10.1007/s11220-025-00597-3',
        'filename': '[ardiyanti2025] - Ardiyanti et al (2025) - ICs-Based GMR Chip Sensor with Magnetite Nanotag (Sensors and Imaging).pdf'
    },
    'xue2019electrospinning': {
        'doi': '10.1021/acs.chemrev.8b00593',
        'filename': '[xue2019electrospinning] - Xue et al (2019) - Electrospinning and electrospun nanofibers methods materials and applications (Chem Rev).pdf'
    },
    'Turkoglu2024': {
        'doi': '10.3390/ijms25031668',
        'filename': '[Turkoglu2024] - Turkoglu et al (2024) - PVA-Based Electrospun Materials A Review (IJMS).pdf'
    },
    'shi2008citric': {
        'doi': '10.1002/app.28648',
        'filename': '[shi2008citric] - Shi et al (2008) - Citric acid poly vinyl alcohol composite films for food packaging (J Appl Polym Sci).pdf'
    },
    'birck2014citric': {
        'doi': '10.3144/expresspolymlett.2014.95',
        'filename': '[birck2014citric] - Birck et al (2014) - New crosslinked cast films based on poly vinyl alcohol (Express Polym Lett).pdf'
    },
    'zhu2023': {
        'doi': '10.1016/j.heliyon.2023.e15193',
        'filename': '[zhu2023] - Zhu et al (2023) - Design of improved four-coil structure with high uniformity (Heliyon).pdf'
    },
    'shylu2020power': {
        'doi': '10.12928/TELKOMNIKA.v18i5.14034',
        'filename': '[shylu2020power] - Shylu et al (2020) - A power efficient delta-sigma ADC with series-bilinear switch capacitor (TELKOMNIKA).pdf'
    },
    'gaaz2015properties': {
        'doi': '10.3390/molecules201219884',
        'filename': '[gaaz2015properties] - Gaaz et al (2015) - Properties and applications of polyvinyl alcohol nanocomposites (Molecules).pdf'
    },
    'millman2007': {
        'doi': '10.1109/MCSE.2007.58',
        'filename': '[millman2007] - Millman & Aivazis (2007) - Python for Scientists (CiSE).pdf'
    },
    'liu2024review': {
        'doi': '10.3390/batteries10080271',
        'filename': '[liu2024review] - Liu et al (2024) - Review of Energy Storage Capacitor Technology (Batteries).pdf'
    },
    'sun2022review': {
        'doi': '10.1002/aesr.202100191',
        'filename': '[sun2022review] - Sun et al (2022) - A Review on Conventional Capacitors Supercapacitors and Hybrid Ion (AESR).pdf'
    }
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
out_dir = 'referensi'

for key, info in targets.items():
    dest_path = os.path.join(out_dir, info['filename'])
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 10000:
        print(f"[{key}] ALREADY EXISTS ({os.path.getsize(dest_path)} bytes)")
        continue
    
    doi = info['doi']
    print(f"\n[{key}] Fetching DOI: {doi} ...")
    pdf_url = None
    
    # Try sci-hub mirrors
    for mirror in ['https://sci-hub.ru/', 'https://sci-hub.st/', 'https://sci-hub.wf/']:
        url = mirror + doi
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=12) as r:
                html = r.read().decode('utf-8', errors='ignore')
                
                # Check for meta citation_pdf_url
                m = re.search(r'<meta\s+name=["\']citation_pdf_url["\']\s+content=["\']([^"\']+)["\']', html, re.I)
                if m:
                    pdf_url = m.group(1)
                    break
                
                # Check for embed/object
                m2 = re.search(r'data=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.I)
                if m2:
                    pdf_url = m2.group(1)
                    break
                
                m3 = re.search(r'src=["\']([^"\']+\.pdf[^"\']*)["\']', html, re.I)
                if m3:
                    pdf_url = m3.group(1)
                    break
        except Exception as e:
            # mirror failed or timed out
            continue
            
    if not pdf_url:
        print(f"[{key}] Could not find PDF URL via mirrors.")
        continue
        
    if pdf_url.startswith('//'):
        pdf_url = 'https:' + pdf_url
    elif pdf_url.startswith('/'):
        pdf_url = 'https://sci-hub.ru' + pdf_url
        
    print(f"[{key}] Downloading from: {pdf_url} ...")
    try:
        req = urllib.request.Request(pdf_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            content = r.read()
            if content.startswith(b'%PDF'):
                with open(dest_path, 'wb') as f:
                    f.write(content)
                print(f"[{key}] SUCCESS! Saved {len(content)} bytes to {info['filename']}")
            else:
                print(f"[{key}] FAILED: Response was not PDF (header: {content[:20]})")
    except Exception as e:
        print(f"[{key}] Download error: {e}")
        
    time.sleep(1)
