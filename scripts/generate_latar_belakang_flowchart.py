"""
Skrip Generator Diagram Alir Konseptual Latar Belakang (Infografis Grafis Minim Teks)
Untuk Slide Latar Belakang Presentasi Proposal Tugas Akhir Fahry Rizky Samsudin
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = "output/diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_flowchart():
    fig, ax = plt.subplots(figsize=(13.333, 5.4), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.axis('off')

    # Dimensi & Posisi Node (7 Tahapan Alur Horisontal-Vertikal Terstruktur)
    nodes = [
        {
            "id": 1,
            "title": "1. MASALAH PANGAN",
            "tag": "Urgensi Kesehatan",
            "tag_color": "#E11D48",
            "box_color": "#FFF1F2",
            "border_color": "#FDA4AF",
            "points": [
                r"$\bullet$ Formalin pada bakso (karsinogenik)",
                r"$\bullet$ Temuan pasar hingga 4.506 ppm",
                r"$\bullet$ Batas aman EFSA hanya 100 ppm"
            ],
            "x": 0.4, "y": 2.8, "w": 3.6, "h": 2.2
        },
        {
            "id": 2,
            "title": "2. GAP METODE SAAT INI",
            "tag": "Limitasi Analisis",
            "tag_color": "#D97706",
            "box_color": "#FFFBEB",
            "border_color": "#FDE68A",
            "points": [
                r"$\bullet$ Kolorimetri: Destruktif, kualitatif",
                r"$\bullet$ GC-MS / HPLC: Sangat mahal",
                r"$\bullet$ Tidak portabel untuk pasar rakyat"
            ],
            "x": 4.4, "y": 2.8, "w": 3.6, "h": 2.2
        },
        {
            "id": 3,
            "title": "3. INOVASI RESEPTOR",
            "tag": "Nanomaterial Hijau",
            "tag_color": "#059669",
            "box_color": "#ECFDF5",
            "border_color": "#A7F3D0",
            "points": [
                r"$\bullet$ $\mathrm{Fe_3O_4}$ hijau ekstrak daun kelor",
                r"$\bullet$ Asam sitrat curing $130^\circ\mathrm{C}$ tahan air",
                r"$\bullet$ ADH: penangkap selektif hidrazon"
            ],
            "x": 8.4, "y": 2.8, "w": 4.5, "h": 2.2
        },
        {
            "id": 4,
            "title": "4. TRANSDUSER TMR",
            "tag": "Spintronika Presisi",
            "tag_color": "#2563EB",
            "box_color": "#EFF6FF",
            "border_color": "#BFDBFE",
            "points": [
                r"$\bullet$ Sensor TMR ALT023-10E",
                r"$\bullet$ Sinyal $6\times$ lebih tinggi dari GMR",
                r"$\bullet$ Resolusi medan mikro nT--mT"
            ],
            "x": 0.4, "y": 0.2, "w": 3.6, "h": 2.2
        },
        {
            "id": 5,
            "title": "5. RANTAI SINYAL",
            "tag": "Akuisisi Rendah Derau",
            "tag_color": "#4F46E5",
            "box_color": "#EEF2FF",
            "border_color": "#C7D2FE",
            "points": [
                r"$\bullet$ In-Amp AD623 ($V_{\mathrm{REF}} = 2{,}50\ \mathrm{V}$)",
                r"$\bullet$ Filter RC LPF ($f_c \approx 15{,}9\ \mathrm{kHz}$)",
                r"$\bullet$ ADC 16-Bit ADS1115 (0,1875 mV)"
            ],
            "x": 4.4, "y": 0.2, "w": 3.6, "h": 2.2
        },
        {
            "id": 6,
            "title": "6. KOMPARASI ML",
            "tag": "Klasik vs Kuantum",
            "tag_color": "#7C3AED",
            "box_color": "#F5F3FF",
            "border_color": "#DDD6FE",
            "points": [
                r"$\bullet$ Model Klasik: SVM (Kernel RBF)",
                r"$\bullet$ Model Kuantum: QSVC (Qiskit)",
                r"$\bullet$ Hilbert space $2^n$ qubit & uji derau"
            ],
            "x": 8.4, "y": 0.2, "w": 4.5, "h": 2.2
        }
    ]

    for n in nodes:
        # Card Background
        rect = patches.FancyBboxPatch(
            (n["x"], n["y"]), n["w"], n["h"],
            boxstyle="round,pad=0.08,rounding_size=0.15",
            facecolor=n["box_color"],
            edgecolor=n["border_color"],
            linewidth=1.8
        )
        ax.add_patch(rect)

        # Badge
        badge = patches.FancyBboxPatch(
            (n["x"] + 0.15, n["y"] + n["h"] - 0.42), 1.6, 0.28,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor='#FFFFFF',
            edgecolor=n["border_color"],
            linewidth=1.2
        )
        ax.add_patch(badge)
        ax.text(n["x"] + 0.95, n["y"] + n["h"] - 0.28, n["tag"],
                fontsize=8.5, weight='bold', color=n["tag_color"],
                ha='center', va='center')

        # Title
        ax.text(n["x"] + 0.15, n["y"] + n["h"] - 0.68, n["title"],
                fontsize=11.5, weight='bold', color='#0F1E4A',
                ha='left', va='center')

        # Divider
        ax.plot([n["x"] + 0.15, n["x"] + n["w"] - 0.15],
                [n["y"] + n["h"] - 0.88, n["y"] + n["h"] - 0.88],
                color=n["border_color"], lw=1.0)

        # Bullet Points
        cur_y = n["y"] + n["h"] - 1.15
        for p in n["points"]:
            ax.text(n["x"] + 0.2, cur_y, p,
                    fontsize=9.5, color='#1E293B',
                    ha='left', va='center')
            cur_y -= 0.38

    # Panah Penghubung Alur (Flow Arrows)
    arrow_props = dict(facecolor='#2563EB', edgecolor='none', width=2.5, headwidth=8.0, headlength=7.0)

    # 1 -> 2
    ax.annotate('', xy=(4.35, 3.9), xytext=(4.05, 3.9), arrowprops=arrow_props)
    # 2 -> 3
    ax.annotate('', xy=(8.35, 3.9), xytext=(8.05, 3.9), arrowprops=arrow_props)
    # 3 -> 4 (Turun melengkung dari baris atas ke baris bawah)
    arrow_down = dict(facecolor='#2563EB', edgecolor='none', width=2.5, headwidth=8.0, headlength=7.0)
    ax.annotate('', xy=(2.2, 2.45), xytext=(2.2, 2.75), arrowprops=arrow_down)
    # 4 -> 5
    ax.annotate('', xy=(4.35, 1.3), xytext=(4.05, 1.3), arrowprops=arrow_props)
    # 5 -> 6
    ax.annotate('', xy=(8.35, 1.3), xytext=(8.05, 1.3), arrowprops=arrow_props)

    ax.set_xlim(0, 13.333)
    ax.set_ylim(0, 5.4)

    filepath = os.path.join(OUTPUT_DIR, "latar_belakang_flowchart.png")
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close(fig)
    print(f"[OK] Diagram alir latar belakang berhasil dibuat: {filepath}")

if __name__ == "__main__":
    generate_flowchart()
