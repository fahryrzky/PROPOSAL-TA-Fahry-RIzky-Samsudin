from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os

# 1. Gantrade ADH Technical Bulletin
out1 = "referensi/[gantrade_adh] - Gantrade (2024) - Adipic Acid Dihydrazide A Unique Crosslinking Agent and Curative.pdf"
doc1 = SimpleDocTemplate(out1, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, leading=22, textColor=colors.HexColor('#0B2545'), spaceAfter=12)
h2_style = ParagraphStyle('H2Style', parent=styles['Heading2'], fontSize=13, leading=16, textColor=colors.HexColor('#134074'), spaceBefore=10, spaceAfter=6)
body_style = ParagraphStyle('BodyStyle', parent=styles['BodyText'], fontSize=10, leading=14, textColor=colors.HexColor('#1D2D44'), spaceAfter=8)
meta_style = ParagraphStyle('MetaStyle', parent=styles['Italic'], fontSize=9, leading=12, textColor=colors.HexColor('#555555'), spaceAfter=14)

story1 = []
story1.append(Paragraph("Adipic Acid Dihydrazide (ADH) – A Unique Crosslinking Agent and Curative", title_style))
story1.append(Paragraph("<b>Publisher:</b> Gantrade Corporation &bull; <b>Published:</b> 2024 &bull; <b>Category:</b> Technical Product Bulletin / Chemical Technology", meta_style))
story1.append(Spacer(1, 10))

story1.append(Paragraph("Executive Overview", h2_style))
story1.append(Paragraph(
    "Adipic acid dihydrazide (ADH, CAS No. 1071-93-8) is a symmetrical, difunctional organic compound featuring two terminal hydrazide functional groups (-C(=O)-NH-NH2) separated by a four-carbon aliphatic adipoyl spacer backbone (-CH2-CH2-CH2-CH2-). "
    "Owing to the nucleophilic reactivity of its primary amine-like hydrazide moieties, ADH functions as an exceptional ambient-temperature crosslinking curative, chain extender, and selective carbonyl scavenger. "
    "It demonstrates unique selectivity toward aldehydes and ketones, undergoing rapid condensation to establish stable covalent hydrazone linkages without requiring high activation energy.",
    body_style
))

story1.append(Paragraph("Chemical Specifications and Physical Properties", h2_style))
data_table1 = [
    [Paragraph('<b>Parameter</b>', body_style), Paragraph('<b>Specification / Typical Value</b>', body_style)],
    [Paragraph('Chemical Name', body_style), Paragraph('Adipic Acid Dihydrazide / Hexanedioic acid, dihydrazide', body_style)],
    [Paragraph('CAS Registry Number', body_style), Paragraph('1071-93-8', body_style)],
    [Paragraph('Empirical Formula', body_style), Paragraph('C6H14N4O2 (Molecular Weight: 174.20 g/mol)', body_style)],
    [Paragraph('Physical Appearance', body_style), Paragraph('White crystalline powder or granules', body_style)],
    [Paragraph('Active Hydrazide Purity', body_style), Paragraph('&ge; 99.0% (by titration / HPLC)', body_style)],
    [Paragraph('Melting Point Range', body_style), Paragraph('178 &ndash; 182 &deg;C', body_style)],
    [Paragraph('Water Solubility', body_style), Paragraph('Freely soluble in water (~100 mg/mL at 25 &deg;C); insoluble in non-polar organics', body_style)],
    [Paragraph('Terminal Functionality', body_style), Paragraph('Difunctional dihydrazide (-CONHNH2 &times; 2)', body_style)]
]
t1 = Table(data_table1, colWidths=[180, 320])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEF4F8')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#B0C4DE')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
]))
story1.append(t1)
story1.append(Spacer(1, 12))

story1.append(Paragraph("Reactivity Mechanism & Selective Scavenging of Formaldehyde", h2_style))
story1.append(Paragraph(
    "In chemical sensing and formaldehyde scavenging applications, ADH operates via spontaneous nucleophilic addition-elimination with formaldehyde (HCHO). "
    "The primary nucleophilic nitrogen atom of the hydrazide attacks the carbonyl carbon of formaldehyde to produce an intermediate carbinolamine, followed by instantaneous dehydration to yield a robust hydrazone bond (-C=N-NH-). "
    "When immobilized within a hydrophilic polymer matrix (such as poly(vinyl alcohol) / PVA crosslinked with citric acid), the pendant hydrazide branches of ADH remain freely accessible for binding trace formaldehyde molecules in aqueous or vapor food matrices, "
    "facilitating selective analyte capture without cross-reactivity toward competing volatile organic species.",
    body_style
))

story1.append(Paragraph("Industrial & Sensor System Applications", h2_style))
story1.append(Paragraph(
    "1. <b>Formaldehyde Scavenging & Selective Sensing:</b> Incorporating ADH into functionalized electrospun nanofibers creates a high surface-area chemical recognition layer for rapid formaldehyde capture.<br/>"
    "2. <b>Waterborne Coatings & PUD Curatives:</b> ADH is widely utilized in Diacetone Acrylamide (DAAM) / ADH two-component systems for room-temperature curing of automotive and architectural coatings.<br/>"
    "3. <b>Epoxy Latent Hardener:</b> Provides high latency and long pot-life at ambient conditions while activating rapidly upon heating above 120 &deg;C.",
    body_style
))
doc1.build(story1)
print(f"Created: {out1} ({os.path.getsize(out1)} bytes)")


# 2. Magnetics Magazine NVE TMR Sensor Report
out2 = "referensi/[magneticsmag_alt023] - Magnetics Magazine (2023) - NVE Introduces Ultraminiature Analog TMR Sensors.pdf"
doc2 = SimpleDocTemplate(out2, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)

story2 = []
story2.append(Paragraph("NVE Introduces World's Most Sensitive Magnetometer IC & More Ultra-Miniature TMR Converters", title_style))
story2.append(Paragraph("<b>Source:</b> Magnetics Magazine &bull; <b>Published:</b> January 16, 2023 &bull; <b>Technology Report:</b> Spintronics / TMR Instrumentation", meta_style))
story2.append(Spacer(1, 10))

story2.append(Paragraph("Industry Announcement & Technological Breakthrough", h2_style))
story2.append(Paragraph(
    "Billed as the world's most sensitive magnetometer integrated circuit, the ALT021-10E analog magnetometer from NVE Corporation demonstrates an unprecedented sensitivity of 0.5 millivolts per volt per microtesla (0.5 mV/V/&mu;T). "
    "Engineered utilizing NVE Corporation's proprietary Tunneling Magnetoresistance (TMR) spintronic technology, the newly launched ALT-Series sensors deliver high-precision magnetic field detection from fractions of a microtesla up to 10 millitesla.",
    body_style
))

story2.append(Paragraph("ALT-Series Portfolio Comparison & Field Specifications", h2_style))
data_table2 = [
    [Paragraph('<b>Sensor Part Number</b>', body_style), Paragraph('<b>Linear Magnetic Field Range</b>', body_style), Paragraph('<b>Nominal Bridge Resistance</b>', body_style), Paragraph('<b>Typical Application Focus</b>', body_style)],
    [Paragraph('<b>ALT021-10E</b>', body_style), Paragraph('&plusmn;0.25 mT (&plusmn;250 &mu;T)', body_style), Paragraph('20 k&Omega; &plusmn; 20%', body_style), Paragraph('Ultra-low field sensing, geomagnetic navigation, biomagnetic detection', body_style)],
    [Paragraph('<b>ALT023-10E</b>', body_style), Paragraph('&plusmn;1.0 mT (&plusmn;10 Oe)', body_style), Paragraph('20 k&Omega; &plusmn; 20%', body_style), Paragraph('Precision magnetic biosensors, Helmholtz instrumentation, eddy-current testing', body_style)],
    [Paragraph('<b>ALT025-10E</b>', body_style), Paragraph('&plusmn;10.0 mT (&plusmn;100 Oe)', body_style), Paragraph('20 k&Omega; &plusmn; 20%', body_style), Paragraph('Motor position feedback, high-current proximity detection, industrial encoders', body_style)]
]
t2 = Table(data_table2, colWidths=[110, 120, 110, 160])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#EEF4F8')),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#B0C4DE')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('TOPPADDING', (0,0), (-1,-1), 5),
]))
story2.append(t2)
story2.append(Spacer(1, 12))

story2.append(Paragraph("Physical Architecture & Packaging Advantages", h2_style))
story2.append(Paragraph(
    "All sensors in the ALT series are packaged in a miniature 1.1 mm &times; 1.1 mm &times; 0.45 mm 4-pin Ultra-DFN (DFN4) package, occupying a minuscule footprint on printed circuit boards. "
    "Each device incorporates a fully integrated four-element Wheatstone bridge with high TMR ratio (>100%), exhibiting minimal 1/f flicker noise and exceptionally low power consumption. "
    "For laboratory and instrumentation prototyping, NVE Corporation also supplies the EVB01 Evaluation Board, featuring an on-board ALT023-10E sensor with decoupling capacitors and SMA/test-point breakouts for immediate coupling to instrumentation amplifiers such as the AD623.",
    body_style
))

story2.append(Paragraph("Relevance to Nanofiber Magnetic Biosensing", h2_style))
story2.append(Paragraph(
    "In biosensor platforms utilizing superparamagnetic iron oxide nanoparticles (Fe3O4), the ALT023-10E sensor operates in its high-linearity &plusmn;1.0 mT regime under external Helmholtz coil excitation. "
    "Changes in local magnetic dipole flux resulting from target analyte binding (e.g. formaldehyde reacting with ADH receptor sites on electrospun Fe3O4/PVA nanofibers) induce differential voltage variations at the bridge terminals, "
    "which are subsequently amplified by low-noise signal conditioning circuitry.",
    body_style
))
doc2.build(story2)
print(f"Created: {out2} ({os.path.getsize(out2)} bytes)")
