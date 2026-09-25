import urllib.request, ssl, os

ctx = ssl._create_unverified_context()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

oa_downloads = [
    (
        "[havlicek2019supervised] - Havlicek et al (2019) - Supervised learning with quantum-enhanced feature spaces (Nature).pdf",
        "https://arxiv.org/pdf/1804.11326"
    ),
    (
        "[schuld2019quantum] - Schuld & Killoran (2019) - Quantum machine learning in feature Hilbert spaces (PRL).pdf",
        "https://arxiv.org/pdf/1803.07128"
    ),
    (
        "[dheyab2020citric] - Dheyab et al (2020) - Simple rapid stabilization method through citric acid modification for magnetite nanoparticles (SciRep).pdf",
        "https://www.nature.com/articles/s41598-020-67869-8.pdf"
    ),
    (
        "[gaaz2015properties] - Gaaz et al (2015) - Properties and applications of polyvinyl alcohol halloysite nanotubes and their nanocomposites (Molecules).pdf",
        "https://www.mdpi.com/1420-3049/20/12/19884/pdf?version=1450518458"
    ),
    (
        "[Turkoglu2024] - Turkoglu et al (2024) - PVA-Based Electrospun Materials Nanofiber Mats Review (IJMS).pdf",
        "https://www.mdpi.com/1422-0067/25/3/1668/pdf?version=1706587131"
    ),
    (
        "[liu2024review] - Liu et al (2024) - Review of Energy Storage Capacitor Technology (Batteries).pdf",
        "https://www.mdpi.com/2313-0105/10/8/271/pdf"
    ),
    (
        "[zhu2023] - Zhu et al (2023) - Design of improved four-coil structure with high uniformity and effective coverage rate (Heliyon).pdf",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC10119714/pdf/main.pdf"
    ),
    (
        "[shylu2020power] - Shylu et al (2020) - A power efficient delta-sigma ADC with series-bilinear switch capacitor (TELKOMNIKA).pdf",
        "http://journal.uad.ac.id/index.php/TELKOMNIKA/article/download/14034/9069"
    )
]

for filename, url in oa_downloads:
    filepath = os.path.join("referensi", filename)
    print(f"Downloading {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
            data = r.read()
            if data.startswith(b"%PDF") or b"%PDF" in data[:1024]:
                with open(filepath, "wb") as f:
                    f.write(data)
                print(f"  -> SUCCESS ({len(data)//1024} KB)")
            else:
                print(f"  -> FAILED: content not PDF ({len(data)} bytes)")
    except Exception as e:
        print(f"  -> ERROR: {e}")
