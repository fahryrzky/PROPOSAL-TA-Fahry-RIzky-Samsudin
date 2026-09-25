import os, sys, urllib.parse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, PngImagePlugin

OUTPUT_PATH = "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png"
XML_PATH = "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio"

def draw_flowchart():
    # Figure size 6.4 x 9.6 inches at 150 DPI gives 960 x 1440, crisp and readable
    fig, ax = plt.subplots(figsize=(6.4, 9.6), dpi=150)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 640)
    ax.set_ylim(960, 0) # Inverted Y so 0 is at top, like draw.io
    ax.axis('off')

    BG_COLOR = '#d5e8d4'
    BORDER_COLOR = '#82b366'
    TEXT_COLOR = '#000000'
    FONT_FAMILY = 'sans-serif'

    def draw_ellipse(cx, cy, w, h, text, font_weight='bold'):
        e = patches.Ellipse((cx, cy), w, h, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.2, zorder=2)
        ax.add_patch(e)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=9.5, fontweight=font_weight, fontfamily=FONT_FAMILY, color=TEXT_COLOR, zorder=3)

    def draw_rect(x, y, w, h, text, font_size=8.0):
        r = patches.Rectangle((x, y), w, h, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.2, zorder=2)
        ax.add_patch(r)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=font_size, fontfamily=FONT_FAMILY, color=TEXT_COLOR, multialignment='center', zorder=3)

    def draw_parallelogram(x, y, w, h, text, font_size=8.0, skew=18):
        pts = [
            (x + skew, y),
            (x + w, y),
            (x + w - skew, y + h),
            (x, y + h)
        ]
        p = patches.Polygon(pts, closed=True, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.2, zorder=2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=font_size, fontfamily=FONT_FAMILY, color=TEXT_COLOR, multialignment='center', zorder=3)

    def draw_rhombus(cx, cy, w, h, text, font_size=8.5):
        pts = [
            (cx, cy - h/2),
            (cx + w/2, cy),
            (cx, cy + h/2),
            (cx - w/2, cy)
        ]
        p = patches.Polygon(pts, closed=True, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.2, zorder=2)
        ax.add_patch(p)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=font_size, fontfamily=FONT_FAMILY, color=TEXT_COLOR, multialignment='center', zorder=3)

    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle='->', lw=1.2), zorder=1)

    # -------------------------------------------------------------
    # KOLOM KIRI (Prekursor & Fe3O4 Kopresipitasi)
    # -------------------------------------------------------------
    col1_cx = 160
    col1_w = 240
    col1_x = col1_cx - col1_w / 2 # 40

    # m1: Mulai
    draw_ellipse(col1_cx, 47, 120, 45, "Mulai")
    draw_arrow(col1_cx, 70, col1_cx, 100)

    # m2: Preparasi Prekursor
    draw_parallelogram(col1_x, 100, col1_w, 55, "Preparasi Prekursor FeSO4 & FeCl3\nserta Ekstrak Daun Kelor (MO)", font_size=8.2)
    draw_arrow(col1_cx, 155, col1_cx, 185)

    # m3: Pencampuran Prekursor
    draw_rect(col1_x, 185, col1_w, 50, "Pencampuran Prekursor & Ekstrak MO\nserta Pemanasan Awal 60°C (600 rpm)", font_size=8.2)
    draw_arrow(col1_cx, 235, col1_cx, 265)

    # m4: Presipitasi Kopresipitasi
    draw_rect(col1_x, 265, col1_w, 55, "Presipitasi Kopresipitasi:\nPenambahan NH4OH Tetes demi Tetes\n(Periode 90 Menit hingga Terbentuk Fe3O4)", font_size=7.8)
    draw_arrow(col1_cx, 320, col1_cx, 350)

    # m5: Pemisahan Magnetik
    draw_rect(col1_x, 350, col1_w, 60, "Pemisahan Magnetik Menggunakan Magnet\n& Pencucian Endapan Fe3O4 dengan\nAquades (7 Siklus Pemurnian)", font_size=7.8)
    draw_arrow(col1_cx, 410, col1_cx, 440)

    # m6: Pengeringan Partikel
    draw_rect(col1_x, 440, col1_w, 50, "Pengeringan Partikel Magnetit Fe3O4\ndi Furnace (2 Jam)", font_size=8.2)
    draw_arrow(col1_cx, 490, col1_cx, 520)

    # m7: Stabilisasi Penudung Citrate Capping
    draw_rect(col1_x, 520, col1_w, 65, "Stabilisasi Penudung (Citrate Capping):\nDispersi 0,2 g Fe3O4 + Asam Sitrat\ndalam 1 mL Aquades (Sonikasi 30 Menit)\n[Mencegah Pengendapan di Jarum Syringe]", font_size=7.6)

    # -------------------------------------------------------------
    # KONEKSI KOLOM KIRI KE KOLOM KANAN (Bawah)
    # -------------------------------------------------------------
    col2_cx = 480
    col2_w = 240
    col2_x = col2_cx - col2_w / 2 # 360

    # m7 bottom to m8 bottom
    # Jalur pipa: dari (col1_x + col1_w, 552) -> (320, 552) -> (320, 810) -> (col2_x, 810)
    ax.plot([col1_x + col1_w, 320, 320, col2_x], [552, 552, 810, 810], color='black', lw=1.2, zorder=1)
    ax.annotate('', xy=(col2_x, 810), xytext=(col2_x - 10, 810),
                arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle='->', lw=1.2), zorder=1)

    # -------------------------------------------------------------
    # KOLOM KANAN (Alur Naik: Sol, Elektrospinning, Curing 130 C, ADH)
    # -------------------------------------------------------------
    # m8: Pelarutan Matriks Polimer PVA
    draw_rect(col2_x, 780, col2_w, 60, "Pelarutan Matriks Polimer PVA 11% b/v\n(0,55 g dalam 5 mL, 85-90°C, 60 Menit)\n& Pencampuran Dispersi Fe3O4-Sitrat", font_size=7.8)
    draw_arrow(col2_cx, 780, col2_cx, 750)

    # m9: Homogenisasi Larutan
    draw_rect(col2_x, 695, col2_w, 55, "Homogenisasi Larutan Komposit:\nPengadukan Magnetik 30 Menit &\nSonikasi Ultrasonic Bath 15 Menit", font_size=8.0)
    draw_arrow(col2_cx, 695, col2_cx, 665)

    # m10: Pemintalan Elektrospinning
    draw_rect(col2_x, 580, col2_w, 85, "Pemintalan Elektrospinning Optimal:\nTegangan: 17 kV | Laju Alir: 0,6 mL/jam\nJarak TCD: 14 cm | Jarum: 22G\nKecepatan Drum Kolektor: 1000 rpm", font_size=7.8)
    draw_arrow(col2_cx, 580, col2_cx, 540)

    # m11: Belah Ketupat Evaluasi Morfologi
    draw_rhombus(col2_cx, 505, 160, 70, "Apakah Nanofiber\nTerbentuk Rata?", font_size=8.0)
    
    # Cabang Ya (ke atas m12)
    draw_arrow(col2_cx, 470, col2_cx, 420)
    ax.text(col2_cx + 8, 445, "Ya", fontsize=8.5, fontweight='bold', fontfamily=FONT_FAMILY)

    # Cabang Tidak (loop kembali ke m10)
    # dari (col2_cx + 80, 505) -> (615, 505) -> (615, 622) -> (col2_x + col2_w, 622)
    ax.plot([col2_cx + 80, 615, 615, col2_x + col2_w], [505, 505, 622, 622], color='black', lw=1.2, zorder=1)
    ax.annotate('', xy=(col2_x + col2_w, 622), xytext=(col2_x + col2_w + 10, 622),
                arrowprops=dict(facecolor='black', edgecolor='black', arrowstyle='->', lw=1.2), zorder=1)
    ax.text(col2_cx + 88, 495, "Tidak", fontsize=8.0, fontfamily=FONT_FAMILY)

    # m12: Thermal Curing Asam Sitrat (Koreksi: 1,5 Jam, Guna Esterifikasi Tahan Air)
    draw_rect(col2_x, 365, col2_w, 55, "Perlakuan Thermal Curing Asam Sitrat:\nPemanasan dalam Oven 130°C (1,5 Jam)\nGuna Membentuk Ikatan Esterifikasi Tahan Air", font_size=7.6)
    draw_arrow(col2_cx, 365, col2_cx, 335)

    # m13: Fungsionalisasi Kemo-Reseptor ADH (Koreksi: 30 Menit, Gugus Hidrazida Penangkap Formalin)
    draw_rect(col2_x, 275, col2_w, 60, "Fungsionalisasi Kemo-Reseptor ADH:\nPerendaman dalam ADH 2% b/v (30 Menit)\nGugus Hidrazida (-NH-NH2) Penangkap Formalin", font_size=7.6)
    draw_arrow(col2_cx, 275, col2_cx, 235)

    # m14: Membran Siap Pasang
    draw_parallelogram(col2_x, 175, col2_w, 60, "Membran Nanofiber Komposit\nFe3O4/PVA-Sitrat-ADH Siap Pasang\npada Permukaan Sensor TMR", font_size=8.0)
    draw_arrow(col2_cx, 175, col2_cx, 115)

    # m15: Selesai
    draw_ellipse(col2_cx, 90, 120, 50, "Selesai")

    # Save initial PNG
    temp_png = "Gambar/Bab3/temp_sintesis.png"
    plt.tight_layout(pad=0.2)
    plt.savefig(temp_png, dpi=150, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()

    # Read XML content from .drawio file to embed as mxfile
    with open(XML_PATH, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    encoded_xml = urllib.parse.quote(xml_content)

    # Open with PIL and save with mxfile metadata
    im = Image.open(temp_png)
    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("mxfile", encoded_xml)
    im.save(OUTPUT_PATH, "PNG", pnginfo=pnginfo)
    os.remove(temp_png)
    print(f"[SUKSES] Flowchart sintesis berhasil diperbarui: {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH)} bytes)")

if __name__ == '__main__':
    draw_flowchart()
