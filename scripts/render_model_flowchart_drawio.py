import os, sys, urllib.parse
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, PngImagePlugin

XML_PATH_1 = "Gambar/Bab3/babIII_ModelBuilding.drawio"
XML_PATH_2 = "Gambar/Bab3/babIIIModelBuilding.drawio"
OUTPUT_PNG_1 = "Gambar/Bab3/babIII_ModelBuilding.drawio.png"
OUTPUT_PNG_2 = "Gambar/Bab3/babIIIModelBuilding.drawio.png"

def generate_drawio_xml():
    xml = """<mxfile host="app.diagrams.net" version="28.2.5" scale="1" border="0">
  <diagram name="Page-1" id="model_building_classical_quantum">
    <mxGraphModel dx="1000" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Edge n1 -> n2 -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n1" target="n2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n1: Mulai -->
        <mxCell id="n1" value="Mulai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="105" y="20" width="120" height="45" as="geometry" />
        </mxCell>

        <!-- Edge n2 -> n3 -->
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n2" target="n3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n2: Memuat Dataset -->
        <mxCell id="n2" value="Memuat Dataset Sinyal Sensor TMR&#xa;Variasi Konsentrasi Formalin pada Bakso" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="25" y="95" width="280" height="55" as="geometry" />
        </mxCell>

        <!-- Edge n3 -> n4 -->
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n3" target="n4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n3: Ekstraksi Fitur -->
        <mxCell id="n3" value="Ekstraksi Fitur Respons Sinyal:&#xa;Vmean, Pergeseran Sinyal ΔV, Stdev Derau σV&#xa;serta Standarisasi dengan StandardScaler" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="25" y="175" width="280" height="55" as="geometry" />
        </mxCell>

        <!-- Edges n4 -> n5a and n4 -> n5b -->
        <mxCell id="e4a" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.25;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n4" target="n5a">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4b" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n4" target="n5b">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n4: Pembagian Dataset -->
        <mxCell id="n4" value="Pembagian Dataset:&#xa;Data Latih (80%) dan Data Uji (20%)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="25" y="255" width="280" height="50" as="geometry" />
        </mxCell>

        <!-- n5a: Model Klasik (SVM & Random Forest) -->
        <mxCell id="n5a" value="&lt;b&gt;Model Klasik&lt;/b&gt;&#xa;&lt;b&gt;(SVM &amp;amp; RF)&lt;/b&gt;&#xa;&#xa;• Support Vector Machine&#xa;  Kernel RBF &amp; Linear&#xa;  GridSearch (C, γ)&#xa;• Random Forest (RF)&#xa;  Ensemble Decision Tree&#xa;• Pelatihan Data Latih" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="18" y="335" width="142" height="135" as="geometry" />
        </mxCell>

        <!-- n5b: Model Kuantum (QSVC & VQC) -->
        <mxCell id="n5b" value="&lt;b&gt;Model Kuantum&lt;/b&gt;&#xa;&lt;b&gt;(QSVC &amp;amp; VQC)&lt;/b&gt;&#xa;&#xa;• Quantum SVC (QSVC)&#xa;  ZZFeatureMap Hilbert&#xa;  Quantum Kernel Matrix&#xa;• Variational Classifier&#xa;  Ansatz VQC (COBYLA)&#xa;• Simulasi Statevector" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="170" y="335" width="142" height="135" as="geometry" />
        </mxCell>

        <!-- Edge connecting parallel models to Column 2 -->
        <mxCell id="e_merge" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n5a" target="n6">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="89" y="490" />
              <mxPoint x="165" y="490" />
              <mxPoint x="165" y="657" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="e_merge2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="n5b">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="165" y="490" as="targetPoint" />
            <Array as="points">
              <mxPoint x="241" y="490" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Edge n6 -> n7 -->
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n6: Evaluasi Komparatif Data Uji -->
        <mxCell id="n6" value="Evaluasi Komparatif pada Data Uji (20%):&#xa;Akurasi, Presisi, Recall, F1-Score,&#xa;Confusion Matrix, serta ROC-AUC" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="345" y="625" width="280" height="65" as="geometry" />
        </mxCell>

        <!-- Edge n7 -> n8 -->
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="n7" target="n8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n7: Pengujian Ketahanan Derau -->
        <mxCell id="n7" value="Pengujian Ketahanan Derau (Noise Robustness):&#xa;Simulasi Injeksi Derau Gaussian Klasik&#xa;&amp; Model Derau Depolarizing Kuantum" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="345" y="535" width="280" height="60" as="geometry" />
        </mxCell>

        <!-- Edge n8 -> n9 -->
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="n8" target="n9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n8: Validasi Silang -->
        <mxCell id="n8" value="Validasi Silang K-Fold (Stratified 5-Fold CV)&#xa;untuk Stabilitas &amp; Generalisasi Model" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="345" y="445" width="280" height="60" as="geometry" />
        </mxCell>

        <!-- Edge n9 -> n10 -->
        <mxCell id="e9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n10">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n9: Pemilihan Model Terbaik -->
        <mxCell id="n9" value="Pemilihan Model Terbaik Berdasarkan ROC-AUC&#xa;&amp; Penyimpanan Model Terlatih (.joblib)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="345" y="355" width="280" height="60" as="geometry" />
        </mxCell>

        <!-- Edge n10 -> n11 -->
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="n10" target="n11">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- n10: Penyimpanan Data Metrik -->
        <mxCell id="n10" value="Penyimpanan Data Metrik Komparasi&#xa;&amp; Laporan Hasil Evaluasi dalam Format .csv" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="345" y="255" width="280" height="70" as="geometry" />
        </mxCell>

        <!-- n11: Selesai -->
        <mxCell id="n11" value="Selesai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="425" y="155" width="120" height="45" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def render_flowchart_image():
    # Canvas: 650 x 720
    fig, ax = plt.subplots(figsize=(6.5, 7.2), dpi=220)
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')
    ax.set_xlim(0, 650)
    ax.set_ylim(720, 0) # Inverted Y: 0 is at top
    ax.axis('off')

    BG_COLOR = '#dae8fc'
    BORDER_COLOR = '#6c8ebf'
    TEXT_COLOR = '#000000'
    LINE_COLOR = '#000000'
    FONT_FAMILY = 'sans-serif'

    def draw_ellipse(cx, cy, w, h, text):
        e = patches.Ellipse((cx, cy), w, h, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.3, zorder=2)
        ax.add_patch(e)
        ax.text(cx, cy, text, ha='center', va='center', fontsize=9.5, fontweight='bold', fontfamily=FONT_FAMILY, color=TEXT_COLOR, zorder=3)

    def draw_rect(x, y, w, h, text, font_size=8.0):
        r = patches.Rectangle((x, y), w, h, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.3, zorder=2)
        ax.add_patch(r)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=font_size, fontfamily=FONT_FAMILY, color=TEXT_COLOR, multialignment='center', zorder=3)

    def draw_parallelogram(x, y, w, h, text, font_size=8.2, skew=18):
        pts = [
            (x + skew, y),
            (x + w, y),
            (x + w - skew, y + h),
            (x, y + h)
        ]
        p = patches.Polygon(pts, closed=True, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.3, zorder=2)
        ax.add_patch(p)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=font_size, fontfamily=FONT_FAMILY, color=TEXT_COLOR, multialignment='center', zorder=3)

    def draw_model_card(x, y, w, h, header_lines, body_lines):
        r = patches.Rectangle((x, y), w, h, facecolor=BG_COLOR, edgecolor=BORDER_COLOR, linewidth=1.3, zorder=2)
        ax.add_patch(r)
        # Header lines
        cur_y = y + 14
        for hl in header_lines:
            ax.text(x + w/2, cur_y, hl, ha='center', va='center', fontsize=7.6, fontweight='bold', fontfamily=FONT_FAMILY, color=TEXT_COLOR, zorder=3)
            cur_y += 11.5
        cur_y += 2
        # Body lines
        for bl in body_lines:
            is_bullet = bl.startswith("•")
            fw = 'bold' if is_bullet else 'normal'
            fs = 6.8 if is_bullet else 6.4
            ax.text(x + w/2, cur_y, bl, ha='center', va='center', fontsize=fs, fontweight=fw, fontfamily=FONT_FAMILY, color=TEXT_COLOR, zorder=3)
            cur_y += 9.8

    def draw_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(facecolor=LINE_COLOR, edgecolor=LINE_COLOR, arrowstyle='->', lw=1.3, shrinkA=0, shrinkB=0), zorder=4)

    # -------------------------------------------------------------
    # KOLOM 1: KIRI (Data -> Ekstraksi -> Split -> 4 Model)
    # -------------------------------------------------------------
    col1_cx = 165
    col1_w = 280
    col1_x = col1_cx - col1_w / 2 # 25

    # n1: Mulai
    draw_ellipse(col1_cx, 42.5, 120, 45, "Mulai")
    draw_arrow(col1_cx, 65, col1_cx, 95)

    # n2: Memuat Dataset
    draw_parallelogram(col1_x, 95, col1_w, 55, "Memuat Dataset Sinyal Sensor TMR\nVariasi Konsentrasi Formalin pada Bakso", font_size=8.2)
    draw_arrow(col1_cx, 150, col1_cx, 175)

    # n3: Ekstraksi Fitur
    draw_rect(col1_x, 175, col1_w, 55, "Ekstraksi Fitur Respons Sinyal:\nVmean, Pergeseran Sinyal ΔV, Stdev Derau σV\nserta Standarisasi dengan StandardScaler", font_size=8.0)
    draw_arrow(col1_cx, 230, col1_cx, 255)

    # n4: Pembagian Dataset
    draw_rect(col1_x, 255, col1_w, 50, "Pembagian Dataset:\nData Latih (80%) dan Data Uji (20%)", font_size=8.2)

    # Cabang Paralel ke n5a & n5b
    card_w = 142
    card_h = 135
    n5a_x = 18
    n5a_cx = n5a_x + card_w / 2 # 89
    n5b_x = 170
    n5b_cx = n5b_x + card_w / 2 # 241

    ax.plot([col1_cx, n5a_cx], [305, 320], color=LINE_COLOR, lw=1.3, zorder=1)
    ax.plot([col1_cx, n5b_cx], [305, 320], color=LINE_COLOR, lw=1.3, zorder=1)
    draw_arrow(n5a_cx, 320, n5a_cx, 335)
    draw_arrow(n5b_cx, 320, n5b_cx, 335)

    # n5a: Model Klasik
    draw_model_card(n5a_x, 335, card_w, card_h,
                    header_lines=["Model Klasik", "(SVM & RF)"],
                    body_lines=[
                        "• Support Vector Machine",
                        "  Kernel RBF & Linear",
                        "  GridSearch (C, γ)",
                        "• Random Forest (RF)",
                        "  Ensemble Decision Tree",
                        "• Pelatihan Data Latih"
                    ])

    # n5b: Model Kuantum
    draw_model_card(n5b_x, 335, card_w, card_h,
                    header_lines=["Model Kuantum", "(QSVC & VQC)"],
                    body_lines=[
                        "• Quantum SVC (QSVC)",
                        "  ZZFeatureMap Hilbert",
                        "  Quantum Kernel Matrix",
                        "• Variational Classifier",
                        "  Ansatz VQC (COBYLA)",
                        "• Simulasi Statevector"
                    ])

    # Merge koneksi dari n5a dan n5b
    # Dari bottom n5a (89, 470) dan bottom n5b (241, 470) turun ke y=490
    ax.plot([n5a_cx, n5a_cx, n5b_cx, n5b_cx], [470, 490, 490, 470], color=LINE_COLOR, lw=1.3, zorder=1)
    # Dari titik temu (165, 490) turun ke y=657.5 (level dengan pusat n6)
    ax.plot([col1_cx, col1_cx], [490, 657.5], color=LINE_COLOR, lw=1.3, zorder=1)
    # Belok ke kanan menyeberang ke Kolom 2 di x=345
    draw_arrow(col1_cx, 657.5, 345, 657.5)

    # -------------------------------------------------------------
    # KOLOM 2: KANAN (Alur Naik: Evaluasi -> Derau -> CV -> Seleksi -> Simpan -> Selesai)
    # -------------------------------------------------------------
    col2_cx = 485
    col2_w = 280
    col2_x = col2_cx - col2_w / 2 # 345

    # n6: Evaluasi Komparatif Data Uji (20%)
    draw_rect(col2_x, 625, col2_w, 65, "Evaluasi Komparatif pada Data Uji (20%):\nAkurasi, Presisi, Recall, F1-Score,\nConfusion Matrix, serta ROC-AUC", font_size=8.0)
    draw_arrow(col2_cx, 625, col2_cx, 595)

    # n7: Pengujian Ketahanan Derau
    draw_rect(col2_x, 535, col2_w, 60, "Pengujian Ketahanan Derau (Noise Robustness):\nSimulasi Injeksi Derau Gaussian Klasik\n& Model Derau Depolarizing Kuantum", font_size=7.8)
    draw_arrow(col2_cx, 535, col2_cx, 505)

    # n8: Validasi Silang
    draw_rect(col2_x, 445, col2_w, 60, "Validasi Silang K-Fold (Stratified 5-Fold CV)\nuntuk Stabilitas & Generalisasi Model", font_size=8.0)
    draw_arrow(col2_cx, 445, col2_cx, 415)

    # n9: Pemilihan Model Terbaik
    draw_rect(col2_x, 355, col2_w, 60, "Pemilihan Model Terbaik Berdasarkan ROC-AUC\n& Penyimpanan Model Terlatih (.joblib)", font_size=8.0)
    draw_arrow(col2_cx, 355, col2_cx, 325)

    # n10: Penyimpanan Data Metrik
    draw_parallelogram(col2_x, 255, col2_w, 70, "Penyimpanan Data Metrik Komparasi\n& Laporan Hasil Evaluasi dalam Format .csv", font_size=8.2)
    draw_arrow(col2_cx, 255, col2_cx, 200)

    # n11: Selesai
    draw_ellipse(col2_cx, 177.5, 120, 45, "Selesai")

    # Simpan PNG sementara
    temp_png = "Gambar/Bab3/temp_model_clean.png"
    plt.tight_layout(pad=0.2)
    plt.savefig(temp_png, dpi=220, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()

    # Dapatkan XML dan sematkan mxfile metadata
    xml_content = generate_drawio_xml()
    encoded_xml = urllib.parse.quote(xml_content)

    im = Image.open(temp_png)
    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("mxfile", encoded_xml)
    im.save(OUTPUT_PNG_1, "PNG", pnginfo=pnginfo)
    im.save(OUTPUT_PNG_2, "PNG", pnginfo=pnginfo)

    # Simpan berkas .drawio
    with open(XML_PATH_1, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    with open(XML_PATH_2, 'w', encoding='utf-8') as f:
        f.write(xml_content)

    if os.path.exists(temp_png):
        os.remove(temp_png)

    print("SUCCESS: Model flowchart successfully generated without AI slop and perfectly aligned!")

if __name__ == "__main__":
    render_flowchart_image()
