import urllib.request
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# 1. Download Krim et al. 2022 (TOPAS 3.6 Elekta Synergy simulation) from PMC / Viamedica
krim_url = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9347432/pdf/rpor-27-2-218.pdf"
krim_out = os.path.join("Referensi", "Krim_2022_Validation_Monte_Carlo_TOPAS_Elekta_Synergy.pdf")
print("Downloading Krim et al. 2022 from PMC...")
try:
    with urllib.request.urlopen(urllib.request.Request(krim_url, headers=headers), context=ctx, timeout=25) as resp:
        data = resp.read()
        if data[:4] == b"%PDF":
            with open(krim_out, "wb") as f:
                f.write(data)
            print(f"SUCCESS! Saved {krim_out} ({len(data)} bytes)")
except Exception as e:
    print("Krim DL error:", e)

# 2. Download N'Guessan et al. 2024 (TOPAS Monte Carlo Elekta Synergy Linac)
ng_url = "https://www.scirp.org/pdf/jbm_2024010815072049.pdf"
ng_out = os.path.join("Referensi", "NGuessan_2024_TOPAS_Monte_Carlo_Elekta_Synergy_Linac.pdf")
print("Downloading N'Guessan et al. 2024 from SCIRP...")
try:
    with urllib.request.urlopen(urllib.request.Request(ng_url, headers=headers), context=ctx, timeout=25) as resp:
        data = resp.read()
        if data[:4] == b"%PDF":
            with open(ng_out, "wb") as f:
                f.write(data)
            print(f"SUCCESS! Saved {ng_out} ({len(data)} bytes)")
except Exception as e:
    print("NGuessan DL error:", e)
