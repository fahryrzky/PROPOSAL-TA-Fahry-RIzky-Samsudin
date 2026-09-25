import urllib.request
import re
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.researchgate.net/publication/392947116_Monte_Carlo_modeling_of_the_Elekta_Synergy_linear_accelerator_platform_with_Agility_MLC_using_TOPASMC_for_secondary_dose_calculation"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
    "Sec-Ch-Ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1"
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("RG fetched successfully, len:", len(html))
        # Look for fulltext download or file links
        for m in re.finditer(r'href="([^"]+download[^"]*)"', html):
            print("Download link:", m.group(1))
        for m in re.finditer(r'href="([^"]+\.pdf[^"]*)"', html):
            print("PDF link:", m.group(1))
        # Check if fulltext is available or "Request full-text"
        if "Request full-text" in html:
            print("STATUS: Full-text is private on ResearchGate (Request full-text button only).")
        if "Download full-text" in html:
            print("STATUS: Full-text download button found!")
except Exception as e:
    print("RG Error:", e)
