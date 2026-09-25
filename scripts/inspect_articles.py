import json
import urllib.request
import ssl

ctx = ssl._create_unverified_context()
with open("scripts/active_references.json", "r", encoding="utf-8") as f:
    refs = json.load(f)

articles = {k: v for k, v in refs.items() if v["type"] in ("article", "inproceedings")}
print(f"Total articles + inproceedings: {len(articles)}\n")

for k, v in sorted(articles.items()):
    doi = v.get("doi", "")
    print(f"Key: {k}")
    print(f"  Title: {v.get('title')}")
    print(f"  Journal: {v.get('journal')}")
    print(f"  DOI: {doi}")
    if doi:
        # Check OpenAlex
        url = f"https://api.openalex.org/works/https://doi.org/{doi}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ProposalResearcher/1.0 (mailto:fahry@example.com)"})
            with urllib.request.urlopen(req, context=ctx, timeout=8) as r:
                d = json.loads(r.read().decode())
                is_oa = d.get("open_access", {}).get("is_oa")
                oa_status = d.get("open_access", {}).get("oa_status")
                oa_url = d.get("open_access", {}).get("oa_url")
                pdf_url = d.get("primary_location", {}).get("pdf_url")
                if not pdf_url:
                    for loc in d.get("locations", []):
                        if loc.get("pdf_url"):
                            pdf_url = loc.get("pdf_url")
                            break
                print(f"  OpenAlex OA: {is_oa} ({oa_status}) | PDF: {pdf_url or oa_url}")
        except Exception as e:
            print(f"  OpenAlex Err: {e}")
    else:
        print(f"  Direct URL: {v.get('url')}")
    print()
