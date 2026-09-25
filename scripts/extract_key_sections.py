import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

html2 = 'File/Sensor Formaldehida pada Bakso Nanofiber + Fe₃O₄ + 6ef17e587f8f4e95a8ad1f3e2a0cd38e.html'
with open(html2, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Split by h2 tags
h2_splits = re.split(r'<h2[^>]*>(.*?)</h2>', content, flags=re.IGNORECASE | re.DOTALL)

sections = {}
for i in range(1, len(h2_splits), 2):
    title = re.sub(r'<[^>]+>', ' ', h2_splits[i]).strip()
    title = re.sub(r'\s+', ' ', title)
    body = h2_splits[i+1] if i+1 < len(h2_splits) else ""
    clean_body = re.sub(r'<[^>]+>', ' ', body).strip()
    clean_body = re.sub(r'\s+', ' ', clean_body)
    sections[title] = clean_body

print(f"Total H2 sections extracted: {len(sections)}")

target_keywords = ['Top 3 Receptor', 'Final Receptor', 'TMR Design', 'Magnetic Mechanism', 'AD623 Design', 'ADS1115 Design', 'Final Recommended']

for title, body in sections.items():
    if any(k.lower() in title.lower() for k in target_keywords):
        print(f"\n=======================================================")
        print(f"SECTION: {title}")
        print(f"=======================================================")
        print(body[:1500])
        print("...")
