"""
Skrip Generator Diagram Alir Konseptual Latar Belakang (Infografis Grafis Minim Teks)
Sesuai format slide referensi 1227030017_skripsi.pdf (Gilang Pratama)
Dengan alur panah melengkung (curved arrows) dan sitasi berbasis nama & tahun.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = "output/diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_flowchart():
    # Resolusi tinggi 300 DPI, rasio 16:9 yang pas untuk slide 1280x720 / 13.33x7.5 inci
    fig, ax = plt.subplots(figsize=(13.0, 5.0), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 13.0)
    ax.set_ylim(0, 5.0)
    ax.axis('off')

    # Palet warna akademik kontras tinggi
    COLOR_ARROW = '#F59E0B' # Amber gold khas slide Gilang

    # Definisi 6 Blok Alur (3 Kolom x 2 Baris)
    # Kolom 1 (Kiri): 1 (Top) -> 2 (Bottom)
    # Kolom 2 (Tengah): 3 (Top) -> 4 (Bottom)
    # Kolom 3 (Kanan): 5 (Top) -> 6 (Bottom - GAP RESEARCH)
    blocks = [
        {
            "id": 1,
            "badge": "1. MASALAH PANGAN",
            "badge_bg": "#FFE4E6",
            "badge_fg": "#E11D48",
            "border": "#FDA4AF",
            "bg": "#FFFFFF",
            "x": 0.4, "y": 2.65, "w": 3.7, "h": 2.15,
            "title": "Bahaya Formalin pada Bakso",
            "items": [
                r"Formalin (HCHO): Karsinogenik Gol. 1 (WHO/IARC)",
                r"Penyalahgunaan pengawet ilegal pada bakso pasar",
                r"Batas residu EFSA < 100 ppm, temuan > 1.000 ppm",
                r"Sitasi: (BPOM, 2023; IARC, 2018)"
            ]
        },
        {
            "id": 2,
            "badge": "2. GAP SENSOR ELEKTRONIK",
            "badge_bg": "#FEF3C7",
            "badge_fg": "#D97706",
            "border": "#FDE68A",
            "bg": "#FFFFFF",
            "x": 0.4, "y": 0.2, "w": 3.7, "h": 2.15,
            "title": "Limitasi Metode & Sensor Ada",
            "items": [
                r"HPLC / UV-Vis: Destruktif, lama, butuh lab khusus",
                r"Sensor Gas MOS: Boros daya (300 C) & peka bumbu",
                r"Biosensor Enzim: Cepat rusak (< 3 mgg) & fouling",
                r"Sitasi: (Wang, 2021; Singhal, 2024; Sun, 2023)"
            ]
        },
        {
            "id": 3,
            "badge": "3. INOVASI RESEPTOR",
            "badge_bg": "#DCFCE7",
            "badge_fg": "#059669",
            "border": "#A7F3D0",
            "bg": "#FFFFFF",
            "x": 4.65, "y": 2.65, "w": 3.7, "h": 2.15,
            "title": "Nanofiber Fe3O4/PVA-Sitrat-ADH",
            "items": [
                r"Fe3O4 hijau kelor: Superparamagnetik ramah lingkungan",
                r"PVA ditaut-silang asam sitrat (curing 130 C anti-air)",
                r"Gugus ADH mengikat formalin via reaksi hidrazon",
                r"Sitasi: (Antarnusa et al., 2022; Türkoğlu, 2024)"
            ]
        },
        {
            "id": 4,
            "badge": "4. TRANSDUSER PRESISI",
            "badge_bg": "#DBEAFE",
            "badge_fg": "#2563EB",
            "border": "#BFDBFE",
            "bg": "#FFFFFF",
            "x": 4.65, "y": 0.2, "w": 3.7, "h": 2.15,
            "title": "Sensor TMR ALT023-10E",
            "items": [
                r"Efek Tunneling Magnetoresistance (Julliere model)",
                r"Sensitivitas 6x lebih tinggi dibanding GMR",
                r"Jembatan Wheatstone peka perturbasi medan stray",
                r"Sitasi: (Julliere, 1975; NVE Corp, 2021)"
            ]
        },
        {
            "id": 5,
            "badge": "5. RANTAI SINYAL",
            "badge_bg": "#E0E7FF",
            "badge_fg": "#4F46E5",
            "border": "#C7D2FE",
            "bg": "#FFFFFF",
            "x": 8.9, "y": 2.65, "w": 3.7, "h": 2.15,
            "title": "Akuisisi Data Rendah Derau",
            "items": [
                r"In-Amp AD623 rail-to-rail (VREF = 2.50 V stabil)",
                r"Filter pasif RC low-pass (fc = 15.9 kHz anti-aliasing)",
                r"ADC 16-Bit ADS1115 (Resolusi 0.1875 mV/count)",
                r"Sitasi: (Green et al., 2019; Shylu et al., 2020)"
            ]
        },
        {
            "id": 6,
            "badge": "6. GAP RESEARCH",
            "badge_bg": "#F3E8FF",
            "badge_fg": "#7C3AED",
            "border": "#DDD6FE",
            "bg": "#FFFFFF",
            "x": 8.9, "y": 0.2, "w": 3.7, "h": 2.15,
            "title": "Model Klasik vs Kuantum",
            "items": [
                r"SVM (RBF) & Random Forest (RF) baseline",
                r"QSVC & VQC (3 Qubit ter-entangle)",
                r"Uji komparasi akurasi & ketahanan derau",
                r"Sitasi: (Havlíček, 2019; Breiman, 2001)"
            ]
        }
    ]

    # Render Card Boxes
    for b in blocks:
        # Card Background
        rect = patches.FancyBboxPatch(
            (b["x"], b["y"]), b["w"], b["h"],
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor=b["bg"], edgecolor=b["border"],
            linewidth=1.8, zorder=2
        )
        ax.add_patch(rect)

        # Header Badge Pill
        badge_box = patches.FancyBboxPatch(
            (b["x"] + 0.15, b["y"] + b["h"] - 0.42), 2.2, 0.3,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor=b["badge_bg"], edgecolor=b["badge_fg"],
            linewidth=1.0, zorder=3
        )
        ax.add_patch(badge_box)

        ax.text(
            b["x"] + 1.25, b["y"] + b["h"] - 0.27,
            b["badge"],
            ha='center', va='center',
            fontsize=9.0, fontweight='bold',
            color=b["badge_fg"], zorder=4
        )

        # Title
        ax.text(
            b["x"] + 0.18, b["y"] + b["h"] - 0.65,
            b["title"],
            ha='left', va='center',
            fontsize=11.0, fontweight='bold',
            color='#0F172A', zorder=4
        )

        # Divider line
        ax.plot(
            [b["x"] + 0.18, b["x"] + b["w"] - 0.18],
            [b["y"] + b["h"] - 0.78, b["y"] + b["h"] - 0.78],
            color=b["border"], linewidth=0.8, zorder=3
        )

        # Bullet Points
        start_y = b["y"] + b["h"] - 0.98
        for j, pt in enumerate(b["items"]):
            is_citation = (j == len(b["items"]) - 1)
            bullet_char = "" if is_citation else "• "
            font_col = "#475569" if is_citation else "#0F172A"
            font_wt = "bold" if is_citation else "normal"
            font_sz = 8.6 if is_citation else 9.2

            ax.text(
                b["x"] + 0.18, start_y - j * 0.31,
                bullet_char + pt,
                ha='left', va='center',
                fontsize=font_sz, fontweight=font_wt,
                color=font_col, zorder=4
            )

    # Render Curved Yellow Arrows (Khas Slide Gilang)
    arrow_props = dict(
        arrowstyle="-|>,head_length=0.35,head_width=0.22",
        color=COLOR_ARROW, lw=2.8, zorder=5
    )

    # 1 -> 2 (Kolom 1: Turun ke bawah)
    arr12 = patches.FancyArrowPatch(
        (2.25, 2.65), (2.25, 2.38),
        connectionstyle="arc3,rad=0.0",
        **arrow_props
    )
    ax.add_patch(arr12)

    # 2 -> 3 (Dari bawah Kolom 1 melengkung ke atas Kolom 2 di celah kolom)
    arr23 = patches.FancyArrowPatch(
        (4.15, 1.28), (4.60, 3.72),
        connectionstyle="arc3,rad=-0.18",
        **arrow_props
    )
    ax.add_patch(arr23)

    # 3 -> 4 (Kolom 2: Turun ke bawah)
    arr34 = patches.FancyArrowPatch(
        (6.50, 2.65), (6.50, 2.38),
        connectionstyle="arc3,rad=0.0",
        **arrow_props
    )
    ax.add_patch(arr34)

    # 4 -> 5 (Dari bawah Kolom 2 melengkung ke atas Kolom 3 di celah kolom)
    arr45 = patches.FancyArrowPatch(
        (8.40, 1.28), (8.85, 3.72),
        connectionstyle="arc3,rad=-0.18",
        **arrow_props
    )
    ax.add_patch(arr45)

    # 5 -> 6 (Kolom 3: Turun ke bawah menuju GAP RESEARCH)
    arr56 = patches.FancyArrowPatch(
        (10.75, 2.65), (10.75, 2.38),
        connectionstyle="arc3,rad=0.0",
        **arrow_props
    )
    ax.add_patch(arr56)

    out_file = os.path.join(OUTPUT_DIR, "latar_belakang_flowchart.png")
    plt.tight_layout(pad=0.2)
    plt.savefig(out_file, facecolor=fig.get_facecolor(), edgecolor='none', dpi=300)
    plt.close()
    print(f"[SUKSES] Diagram alir latar belakang berhasil dibuat: {out_file}")

if __name__ == "__main__":
    generate_flowchart()
