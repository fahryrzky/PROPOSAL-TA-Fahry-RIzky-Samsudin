import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('data/extracted_literature_refs_97.txt', 'r', encoding='utf-8') as f:
    refs = f.readlines()

print(f"Total references in extracted_literature_refs_97.txt: {len(refs)}")

# Categorize
categories = {
    'Receptor / ADH / Hydrazide / Amina / Formaldehyde Detection': [],
    'Nanofiber / Electrospinning / PVA / Citric Acid Crosslinking': [],
    'Magnetic Nanoparticles / Fe3O4 / TMR / GMR / Sensors': [],
    'Formalin pada Bakso / Food Matrix / Standard Method': [],
    'Hardware / Instrumentation / ADC / OPAMP': []
}

for r in refs:
    r_low = r.lower()
    if any(k in r_low for k in ['hydrazide', 'hidrazida', 'adh', 'amine', 'aza-cope', 'fluorescent probe', 'formaldehyde', 'formaldehida', 'formalin', 'swcnt']):
        if any(k in r_low for k in ['bakso', 'meat', 'food', 'tofu', 'fish', 'cfs', 'bpom', 'efsa']):
            categories['Formalin pada Bakso / Food Matrix / Standard Method'].append(r.strip())
        else:
            categories['Receptor / ADH / Hydrazide / Amina / Formaldehyde Detection'].append(r.strip())
    elif any(k in r_low for k in ['nanofiber', 'electrospinning', 'pva', 'poly(vinyl alcohol)', 'citric', 'crosslink', 'chitosan']):
        categories['Nanofiber / Electrospinning / PVA / Citric Acid Crosslinking'].append(r.strip())
    elif any(k in r_low for k in ['tmr', 'gmr', 'fe3o4', 'magnetic', 'sensor', 'alt023', 'magnetite', 'tunneling']):
        categories['Magnetic Nanoparticles / Fe3O4 / TMR / GMR / Sensors'].append(r.strip())
    elif any(k in r_low for k in ['ad623', 'ads1115', 'arduino', 'amplifier', 'adc']):
        categories['Hardware / Instrumentation / ADC / OPAMP'].append(r.strip())
    else:
        # Check other
        if any(k in r_low for k in ['meat', 'food', 'bakso', 'tofu', 'fish', 'cfs', 'bpom', 'efsa']):
            categories['Formalin pada Bakso / Food Matrix / Standard Method'].append(r.strip())
        else:
            categories['Receptor / ADH / Hydrazide / Amina / Formaldehyde Detection'].append(r.strip())

for cat, items in categories.items():
    print(f"\n=== {cat} ({len(items)} references) ===")
    for it in items[:6]:
        print(f"  {it[:120]}...")
