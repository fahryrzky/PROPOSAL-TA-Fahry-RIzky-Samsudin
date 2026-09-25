"""
Generator Presentasi Seminar Proposal Tugas Akhir - Fahry Rizky Samsudin
Format Standar Akademik Fisika UIN Sunan Gunung Djati Bandung
Berdasarkan Format Gilang Pratama (1227030017_skripsi.pdf) & Bebas AI Slop:
1. Cover dengan Logo UIN & Fisika, Judul Tengah, Peneliti Tengah, Pembimbing Kiri & Kanan
2. Latar Belakang Infografis Flowchart Berarah (Panah Kuning)
3. Landasan Teori Menggabungkan 2-4 Teori per Slide dengan Sitasi Asli & Gambar Riil
4. Tanpa AI Slop (Hapus Profil Mitra, Hapus Sistematika Paparan, Hapus 4 Dimensi Strategis)
5. Ukuran Font Besar (Body 13-16 pt, Title 20-24 pt) dan Kontras Tinggi
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# KONFIGURASI WARNA & TIPOGRAFI AKADEMIK RESMI
# ==============================================================================
COLOR_NAVY_DARK   = RGBColor(15, 23, 42)     # #0F172A - Dominan & Header
COLOR_NAVY_MID    = RGBColor(30, 58, 138)    # #1E3A8A - Sub-header & Aksen Kuat
COLOR_BLUE_ACCENT = RGBColor(2, 132, 199)    # #0284C7 - Sorotan & Border Aktif
COLOR_EMERALD     = RGBColor(5, 150, 105)    # #059669 - Kuantum & Kebaruan
COLOR_GOLD        = RGBColor(217, 119, 6)    # #D97706 - Panah & Evaluasi
COLOR_BG_LIGHT    = RGBColor(248, 250, 252)  # #F8FAFC - Background Bersih
COLOR_CARD_BG     = RGBColor(255, 255, 255)  # #FFFFFF - Latar Kartu
COLOR_CARD_BORDER = RGBColor(203, 213, 225)  # #CBD5E1 - Border Kartu
COLOR_TEXT_MAIN   = RGBColor(15, 23, 42)     # #0F172A - Teks Utama Pekat
COLOR_TEXT_MUTED  = RGBColor(71, 85, 105)    # #475569 - Teks Sekunder / Sitasi

FONT_FAMILY = "Arial"

class CleanDeckBuilder:
    def __init__(self, filename="Proposal_TA_Fahry_Rizky_Samsudin.pptx"):
        self.filename = filename
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]

    def add_blank_slide(self):
        slide = self.prs.slides.add_slide(self.blank_layout)
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_LIGHT
        bg.line.fill.background()
        return slide

    def add_header(self, slide, section_tag, main_title):
        # Header banner top (bersih, tegas, tanpa subtitle teks kecil)
        banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
        banner.fill.solid()
        banner.fill.fore_color.rgb = COLOR_CARD_BG
        banner.line.color.rgb = COLOR_CARD_BORDER
        banner.line.width = Pt(1.0)

        # Blue accent line on top edge
        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
        top_line.fill.solid()
        top_line.fill.fore_color.rgb = COLOR_NAVY_MID
        top_line.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.7), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = section_tag.upper()
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_BLUE_ACCENT
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = main_title
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(20)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_NAVY_DARK

    def add_card(self, slide, left, top, width, height, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    def add_image_fitted(self, slide, img_path, left, top, width, height, border=True):
        if os.path.exists(img_path):
            img = slide.shapes.add_picture(img_path, left, top, width, height)
            if border:
                border_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
                border_box.fill.background()
                border_box.line.color.rgb = COLOR_CARD_BORDER
                border_box.line.width = Pt(1.0)
            return img
        return None

    def add_footer(self, slide, slide_num, total_slides=16):
        # Bottom footer line
        ft_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.02))
        ft_line.fill.solid()
        ft_line.fill.fore_color.rgb = COLOR_CARD_BORDER
        ft_line.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(11.733), Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p = tf.paragraphs[0]
        p.text = "Proposal Tugas Akhir — Fahry Rizky Samsudin (1237030018) | Jurusan Fisika UIN Sunan Gunung Djati Bandung"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9)
        p.font.color.rgb = COLOR_TEXT_MUTED

        p_num = p.add_run()
        p_num.text = f"                    Slide {slide_num} / {total_slides}"
        p_num.font.bold = True
        p_num.font.color.rgb = COLOR_NAVY_MID

    def save(self):
        self.prs.save(self.filename)
        print(f"[SUKSES] Presentasi tersimpan: {self.filename}")


def build_clean_deck():
    deck = CleanDeckBuilder("Proposal_TA_Fahry_Rizky_Samsudin.pptx")

    # ==========================================================================
    # SLIDE 1: COVER IDENTITAS (Layout Gilang Pratama)
    # ==========================================================================
    s1 = deck.add_blank_slide()

    # Logos at Top
    deck.add_image_fitted(s1, "Gambar/Logo/Logo UIN.png", Inches(1.0), Inches(0.45), Inches(1.1), Inches(1.1), border=False)
    deck.add_image_fitted(s1, "Gambar/Logo/Logo Fisika UIN.png", Inches(11.233), Inches(0.45), Inches(1.1), Inches(1.1), border=False)

    # Header Institution pill
    t_inst = s1.shapes.add_textbox(Inches(2.4), Inches(0.55), Inches(8.533), Inches(0.8))
    tf_inst = t_inst.text_frame
    tf_inst.word_wrap = True
    p_inst = tf_inst.paragraphs[0]
    p_inst.text = "SEMINAR PROPOSAL TUGAS AKHIR | JURUSAN FISIKA\nFAKULTAS SAINS DAN TEKNOLOGI - UIN SUNAN GUNUNG DJATI BANDUNG"
    p_inst.font.name = FONT_FAMILY
    p_inst.font.size = Pt(11)
    p_inst.font.bold = True
    p_inst.font.color.rgb = COLOR_NAVY_MID
    p_inst.alignment = PP_ALIGN.CENTER

    # Title Card (Center, Bold, Large)
    deck.add_card(s1, Inches(0.8), Inches(1.65), Inches(11.733), Inches(2.35), bg_color=COLOR_CARD_BG, border_color=COLOR_BLUE_ACCENT)
    t_title = s1.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(11.133), Inches(2.05))
    tf_title = t_title.text_frame
    tf_title.word_wrap = True
    p_t = tf_title.paragraphs[0]
    p_t.text = "RANCANG BANGUN INSTRUMENTASI SENSOR TUNNELING MAGNETORESISTANCE BERBASIS NANOFIBER Fe3O4/PVA-SITRAT-ADH UNTUK DETEKSI FORMALIN PADA BAKSO MENGGUNAKAN KOMPARASI MODEL KLASIK (SVM, RANDOM FOREST) DAN KUANTUM (QSVC, VQC)"
    p_t.font.name = FONT_FAMILY
    p_t.font.size = Pt(17.5)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_NAVY_DARK
    p_t.alignment = PP_ALIGN.CENTER
    p_t.line_spacing = 1.2

    # Author Card (Center, Large)
    deck.add_card(s1, Inches(4.2), Inches(4.2), Inches(4.933), Inches(1.15), bg_color=COLOR_NAVY_DARK, border_color=COLOR_NAVY_MID)
    t_auth = s1.shapes.add_textbox(Inches(4.3), Inches(4.25), Inches(4.733), Inches(1.05))
    tf_auth = t_auth.text_frame
    tf_auth.word_wrap = True
    p_au1 = tf_auth.paragraphs[0]
    p_au1.text = "DISUSUN OLEH:"
    p_au1.font.name = FONT_FAMILY
    p_au1.font.size = Pt(9.5)
    p_au1.font.color.rgb = RGBColor(147, 197, 253)
    p_au1.alignment = PP_ALIGN.CENTER
    p_au2 = tf_auth.add_paragraph()
    p_au2.text = "FAHRY RIZKY SAMSUDIN"
    p_au2.font.name = FONT_FAMILY
    p_au2.font.size = Pt(15)
    p_au2.font.bold = True
    p_au2.font.color.rgb = RGBColor(255, 255, 255)
    p_au2.alignment = PP_ALIGN.CENTER
    p_au3 = tf_auth.add_paragraph()
    p_au3.text = "NIM: 1237030018"
    p_au3.font.name = FONT_FAMILY
    p_au3.font.size = Pt(11)
    p_au3.font.color.rgb = RGBColor(203, 213, 225)
    p_au3.alignment = PP_ALIGN.CENTER

    # Advisor Left
    deck.add_card(s1, Inches(0.8), Inches(5.55), Inches(5.6), Inches(1.4), bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    t_adv1 = s1.shapes.add_textbox(Inches(1.0), Inches(5.65), Inches(5.2), Inches(1.2))
    tf_adv1 = t_adv1.text_frame
    tf_adv1.word_wrap = True
    p_ad1_h = tf_adv1.paragraphs[0]
    p_ad1_h.text = "DOSEN PEMBIMBING I:"
    p_ad1_h.font.name = FONT_FAMILY
    p_ad1_h.font.size = Pt(9.5)
    p_ad1_h.font.bold = True
    p_ad1_h.font.color.rgb = COLOR_BLUE_ACCENT
    p_ad1_n = tf_adv1.add_paragraph()
    p_ad1_n.text = "Mada Sanjaya W.S., M.Si., Ph.D."
    p_ad1_n.font.name = FONT_FAMILY
    p_ad1_n.font.size = Pt(13.5)
    p_ad1_n.font.bold = True
    p_ad1_n.font.color.rgb = COLOR_NAVY_DARK
    p_ad1_nip = tf_adv1.add_paragraph()
    p_ad1_nip.text = "NIP. 19851101 200912 1005"
    p_ad1_nip.font.name = FONT_FAMILY
    p_ad1_nip.font.size = Pt(10.5)
    p_ad1_nip.font.color.rgb = COLOR_TEXT_MUTED

    # Advisor Right / Ketua Jurusan
    deck.add_card(s1, Inches(6.933), Inches(5.55), Inches(5.6), Inches(1.4), bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    t_adv2 = s1.shapes.add_textbox(Inches(7.133), Inches(5.65), Inches(5.2), Inches(1.2))
    tf_adv2 = t_adv2.text_frame
    tf_adv2.word_wrap = True
    p_ad2_h = tf_adv2.paragraphs[0]
    p_ad2_h.text = "DOSEN PEMBIMBING II / PENGUJI:"
    p_ad2_h.font.name = FONT_FAMILY
    p_ad2_h.font.size = Pt(9.5)
    p_ad2_h.font.bold = True
    p_ad2_h.font.color.rgb = COLOR_EMERALD
    p_ad2_n = tf_adv2.add_paragraph()
    p_ad2_n.text = "Dr. Yudha Satya Perkasa, M.Si."
    p_ad2_n.font.name = FONT_FAMILY
    p_ad2_n.font.size = Pt(13.5)
    p_ad2_n.font.bold = True
    p_ad2_n.font.color.rgb = COLOR_NAVY_DARK
    p_ad2_nip = tf_adv2.add_paragraph()
    p_ad2_nip.text = "NIP. 19780512 200801 1 009"
    p_ad2_nip.font.name = FONT_FAMILY
    p_ad2_nip.font.size = Pt(10.5)
    p_ad2_nip.font.color.rgb = COLOR_TEXT_MUTED

    deck.add_footer(s1, 1)

    # ==========================================================================
    # SLIDE 2: LATAR BELAKANG (FLOWCHART KONSEPTUAL BERARAH)
    # ==========================================================================
    s2 = deck.add_blank_slide()
    deck.add_header(s2, "Bab I: Pendahuluan", "Latar Belakang: Alur Masalah, Urgensi, & Solusi Riset")
    
    # Pasang Flowchart Gambar Resolusi Tinggi (Khas Slide Gilang)
    flowchart_path = "output/diagrams/latar_belakang_flowchart.png"
    if os.path.exists(flowchart_path):
        deck.add_image_fitted(s2, flowchart_path, Inches(0.8), Inches(1.35), Inches(11.733), Inches(5.5), border=False)
    deck.add_footer(s2, 2)

    # ==========================================================================
    # SLIDE 3: RUMUSAN MASALAH & BATASAN MASALAH
    # ==========================================================================
    s3 = deck.add_blank_slide()
    deck.add_header(s3, "Bab I: Pendahuluan", "Perumusan Masalah & Batasan Masalah Penelitian")

    # Rumusan Masalah (Kiri)
    deck.add_card(s3, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb3_l = s3.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.25), Inches(5.2))
    tf3_l = tb3_l.text_frame
    tf3_l.word_wrap = True
    
    p = tf3_l.paragraphs[0]
    p.text = "RUMUSAN MASALAH PENELITIAN"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(12)

    rumusan_items = [
        ("1. Rancang Bangun Hardware:", "Bagaimana merancang rantai instrumentasi sensor TMR ALT023-10E terintegrasi dengan in-amp AD623 dan ADC ADS1115 untuk deteksi formalin?"),
        ("2. Karakteristik Metrologis:", "Bagaimana sensitivitas, linearitas (R²), limit of detection (LOD), dan limit of quantification (LOQ) sensor TMR berlabel nanofiber Fe3O4/PVA-Sitrat-ADH?"),
        ("3. Komparasi 4 Model Cerdas:", "Bagaimana perbandingan akurasi, presisi, recall, F1, dan ROC-AUC antara model klasik (SVM, RF) vs model kuantum (QSVC, VQC)?"),
        ("4. Ketahanan Derau & Kelayakan:", "Bagaimana tingkat ketahanan derau (noise robustness) dan latensi komputasi model kuantum dibanding model klasik untuk implementasi embedded?")
    ]
    for title, desc in rumusan_items:
        p_item = tf3_l.add_paragraph()
        p_item.space_after = Pt(10)
        p_item.line_spacing = 1.15
        r_t = p_item.add_run()
        r_t.text = title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(13)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = desc
        r_d.font.size = Pt(12)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    # Batasan Masalah (Kanan)
    deck.add_card(s3, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb3_r = s3.shapes.add_textbox(Inches(7.08), Inches(1.5), Inches(5.25), Inches(5.2))
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True

    p = tf3_r.paragraphs[0]
    p.text = "BATASAN MASALAH PENELITIAN"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(12)

    batasan_items = [
        ("• Transduser:", "Sensor TMR ALT023-10E (NVE Corporation), rentang linier ±1.0 mT, catu 5.0 V tunggal."),
        ("• Material Reseptor:", "Nanofiber Fe3O4/PVA-Sitrat-ADH via electrospinning & thermal curing 130 °C."),
        ("• Pengkondisi Sinyal:", "AD623 (VREF = 2.50 V, G = 11) & filter pasif anti-aliasing RC (fc ≈ 159 Hz)."),
        ("• ADC & Komunikasi:", "ADS1115 16-bit (GAIN_TWOTHIRDS, 128 SPS), I2C ke Arduino Uno R3."),
        ("• Sampel Analit:", "Formalin standar (0–100 ppm) dan ekstrak bakso riil (kontrol vs berformalin)."),
        ("• Komparasi Model:", "4 Model: SVM (RBF), Random Forest, QSVC (ZZFeatureMap), dan VQC (Ansatz).")
    ]
    for b_title, b_desc in batasan_items:
        p_item = tf3_r.add_paragraph()
        p_item.space_after = Pt(9)
        p_item.line_spacing = 1.15
        r_t = p_item.add_run()
        r_t.text = b_title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(13)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = b_desc
        r_d.font.size = Pt(12)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s3, 3)

    # ==========================================================================
    # SLIDE 4: TUJUAN & MANFAAT PENELITIAN
    # ==========================================================================
    s4 = deck.add_blank_slide()
    deck.add_header(s4, "Bab I: Pendahuluan", "Tujuan Penelitian & Kontribusi Manfaat Riset")

    # Tujuan Penelitian (Kiri)
    deck.add_card(s4, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb4_l = s4.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.25), Inches(5.2))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True

    p = tf4_l.paragraphs[0]
    p.text = "TUJUAN PENELITIAN"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(14)

    tujuan_items = [
        ("1. Rancang Bangun Sistem:", "Merealisasikan prototipe instrumen sensor TMR dengan modul pengkondisi sinyal AD623 dan ADC 16-bit ADS1115."),
        ("2. Karakterisasi Metrologis:", "Menentukan kurva kalibrasi V-B, sensitivitas rasiometrik, batas deteksi (LOD), dan LOQ sensor terhadap formalin standar."),
        ("3. Komparasi 4 Model ML:", "Mengevaluasi dan membandingkan performa akurasi, presisi, recall, F1, dan ROC-AUC antara SVM, Random Forest, QSVC, dan VQC."),
        ("4. Evaluasi Ketahanan Derau:", "Menguji ketahanan derau (noise robustness) model klasik vs kuantum dan latensi inferensi untuk kesiapan deployment.")
    ]
    for title, desc in tujuan_items:
        p_item = tf4_l.add_paragraph()
        p_item.space_after = Pt(12)
        p_item.line_spacing = 1.15
        r_t = p_item.add_run()
        r_t.text = title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(13)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = desc
        r_d.font.size = Pt(12)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    # Manfaat Penelitian (Kanan)
    deck.add_card(s4, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb4_r = s4.shapes.add_textbox(Inches(7.08), Inches(1.5), Inches(5.25), Inches(5.2))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True

    p = tf4_r.paragraphs[0]
    p.text = "MANFAAT & DAMPAK RISET"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD
    p.space_after = Pt(14)

    manfaat_items = [
        ("• Aspek Ilmiah & Spintronika:", "Memberikan kontribusi orisinal dalam penggabungan transduser spintronika TMR dengan material komposit nanofiber hijau dan komputasi kuantum (Qiskit)."),
        ("• Aspek Teknologi Instrumentasi:", "Menghasilkan alat uji formalin portabel bersuhu ruang yang cepat, murah, tidak destruktif, dan tidak membutuhkan reagen beracun di lapangan."),
        ("• Aspek Keamanan Pangan Nasional:", "Menyediakan instrumen skrining kuantitatif bagi BPOM dan dinas pasar untuk melindungi masyarakat dari bahaya karsinogenik pangan.")
    ]
    for title, desc in manfaat_items:
        p_item = tf4_r.add_paragraph()
        p_item.space_after = Pt(14)
        p_item.line_spacing = 1.2
        r_t = p_item.add_run()
        r_t.text = title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(13)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = desc
        r_d.font.size = Pt(12)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s4, 4)

    # ==========================================================================
    # SLIDE 5: LANDASAN TEORI I — Transduser TMR & Reseptor Nanofiber
    # ==========================================================================
    s5 = deck.add_blank_slide()
    deck.add_header(s5, "Bab II: Tinjauan Pustaka", "Transduser Spintronik TMR & Reseptor Kovalen Nanofiber")

    # Kiri: Sensor TMR ALT023-10E
    deck.add_card(s5, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb5_l = s5.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(5.25), Inches(3.2))
    tf5_l = tb5_l.text_frame
    tf5_l.word_wrap = True
    
    p = tf5_l.paragraphs[0]
    p.text = "1. Transduser TMR ALT023-10E"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(6)

    tmr_points = [
        "Efek Quantum Tunneling melintasi isolator tipis MgO pada struktur Magnetic Tunnel Junction (MTJ).",
        "Persamaan Julliere: TMR = [2P1P2 / (1 - P1P2)] x 100% (> 200% pada suhu ruang).",
        "Sensitivitas 15–25 mV/V/mT pada medan rendah ±1.0 mT (6x lebih peka dari sensor GMR).",
        "Sitasi: (Julliere, 1975; Pannetier et al., 2022; NVE Corp., 2023)"
    ]
    for pt in tmr_points:
        p_pt = tf5_l.add_paragraph()
        p_pt.space_after = Pt(5)
        p_pt.line_spacing = 1.15
        r = p_pt.add_run()
        r.text = "• " + pt
        r.font.size = Pt(12)
        if "Sitasi:" in pt:
            r.font.bold = True
            r.font.size = Pt(11.5)
            r.font.color.rgb = COLOR_NAVY_MID

    # Gambar TMR
    deck.add_image_fitted(s5, "Gambar/Bab2/babII_ALT023.png", Inches(1.0), Inches(4.7), Inches(2.5), Inches(1.9), border=True)
    deck.add_image_fitted(s5, "Gambar/Bab2/babII_TMR_Layer.png", Inches(3.7), Inches(4.7), Inches(2.5), Inches(1.9), border=True)

    # Kanan: Reseptor Nanofiber Fe3O4/PVA-Sitrat-ADH
    deck.add_card(s5, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb5_r = s5.shapes.add_textbox(Inches(7.08), Inches(1.45), Inches(5.25), Inches(3.2))
    tf5_r = tb5_r.text_frame
    tf5_r.word_wrap = True

    p = tf5_r.paragraphs[0]
    p.text = "2. Nanofiber Fe3O4/PVA-Sitrat-ADH"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(6)

    nano_points = [
        "Partikel superparamagnetik Fe3O4 disintesis via ekstrak daun kelor (green synthesis ramah lingkungan).",
        "Thermal curing asam sitrat 130 °C membentuk taut silang ester yang tahan air (insoluble).",
        "Reseptor ADH mengikat formalin spesifik membentuk ikatan hidrazon kovalen (R-C=N-NH-R').",
        "Modulasi stray field magnetik: B_stray ∝ 1/z³ menggeser tegangan sensor secara presisi.",
        "Sitasi: (Hermanson, 2013; Antarnusa et al., 2022; Türkoğlu, 2024)"
    ]
    for pt in nano_points:
        p_pt = tf5_r.add_paragraph()
        p_pt.space_after = Pt(5)
        p_pt.line_spacing = 1.15
        r = p_pt.add_run()
        r.text = "• " + pt
        r.font.size = Pt(12)
        if "Sitasi:" in pt:
            r.font.bold = True
            r.font.size = Pt(11.5)
            r.font.color.rgb = COLOR_NAVY_MID

    # Gambar Ikatan Formalin ADH
    deck.add_image_fitted(s5, "Gambar/Bab2/babII_ikatan_formalin.png", Inches(7.2), Inches(4.7), Inches(5.0), Inches(1.9), border=True)

    deck.add_footer(s5, 5)

    # ==========================================================================
    # SLIDE 6: LANDASAN TEORI II — Rantai Akuisisi Analog-Digital & Metrologi
    # ==========================================================================
    s6 = deck.add_blank_slide()
    deck.add_header(s6, "Bab II: Tinjauan Pustaka", "Rantai Pengkondisi Sinyal AD623, ADC ADS1115, & Metrologi")

    # Kiri: In-Amp AD623 & Filter RC
    deck.add_card(s6, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb6_l = s6.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(5.25), Inches(3.2))
    tf6_l = tb6_l.text_frame
    tf6_l.word_wrap = True

    p = tf6_l.paragraphs[0]
    p.text = "1. Penguat Instrumentasi AD623 & LPF"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(6)

    ad_points = [
        "In-Amp rail-to-rail catu tunggal +5.0 V dengan CMRR tinggi meredam derau common-mode.",
        "Resistor gain RG = 10.0 kΩ menghasilkan penguatan tetap G = 1 + (100 kΩ / RG) = 11.",
        "Tegangan bias referensi VREF = 2.50 V (R3 = R4 = 1.0 kΩ) menjaga sinyal bipolar pada rentang 1.40–3.60 V (anti-clipping).",
        "Filter pasif RC (R=10 kΩ, C=100 nF, fc ≈ 159 Hz) membatasi frekuensi di bawah batas Nyquist.",
        "Sitasi: (Analog Devices, 2020; Pallàs-Areny & Webster, 2001)"
    ]
    for pt in ad_points:
        p_pt = tf6_l.add_paragraph()
        p_pt.space_after = Pt(5)
        p_pt.line_spacing = 1.15
        r = p_pt.add_run()
        r.text = "• " + pt
        r.font.size = Pt(12)
        if "Sitasi:" in pt:
            r.font.bold = True
            r.font.size = Pt(11.5)
            r.font.color.rgb = COLOR_NAVY_MID

    # Gambar AD623
    deck.add_image_fitted(s6, "Gambar/Bab2/babII_AD623_Pinout.png", Inches(1.6), Inches(4.7), Inches(3.8), Inches(1.9), border=True)

    # Kanan: ADC ADS1115 & Metrologi IUPAC
    deck.add_card(s6, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb6_r = s6.shapes.add_textbox(Inches(7.08), Inches(1.45), Inches(5.25), Inches(3.2))
    tf6_r = tb6_r.text_frame
    tf6_r.word_wrap = True

    p = tf6_r.paragraphs[0]
    p.text = "2. ADC 16-Bit ADS1115 & Metrologi IUPAC"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_GOLD
    p.space_after = Pt(6)

    adc_points = [
        "ADC Delta-Sigma 16-bit antarmuka I2C (alamat 0x48, laju konversi 128 SPS).",
        "PGA internal GAIN_TWOTHIRDS (FSR = ±6.144 V) menghasilkan resolusi 0.1875 mV/count.",
        "Rumus LOD & LOQ Standar IUPAC:",
        "    LOD = (3.3 x σ_blank) / m    |    LOQ = (10 x σ_blank) / m",
        "Sensitivitas: m = ΔV / ΔC (kemiringan kurva respon kalibrasi sensor).",
        "Sitasi: (Texas Instruments, 2018; Mocak et al., 1997; IUPAC, 2014)"
    ]
    for pt in adc_points:
        p_pt = tf6_r.add_paragraph()
        p_pt.space_after = Pt(4)
        p_pt.line_spacing = 1.15
        r = p_pt.add_run()
        r.text = "• " + pt if not pt.startswith("    ") else pt
        r.font.size = Pt(12)
        if "LOD =" in pt or "LOQ =" in pt:
            r.font.bold = True
            r.font.color.rgb = COLOR_NAVY_DARK
        elif "Sitasi:" in pt:
            r.font.bold = True
            r.font.size = Pt(11.5)
            r.font.color.rgb = COLOR_NAVY_MID

    # Gambar ADS1115
    deck.add_image_fitted(s6, "Gambar/Bab2/babII_ADS-1115-c.jpg", Inches(8.0), Inches(4.7), Inches(3.2), Inches(1.9), border=True)

    deck.add_footer(s6, 6)

    # ==========================================================================
    # SLIDE 7: LANDASAN TEORI III — Komparasi 4 Model Klasik vs Kuantum
    # ==========================================================================
    s7 = deck.add_blank_slide()
    deck.add_header(s7, "Bab II: Tinjauan Pustaka", "Fondasi Matematis Komparasi 4 Model Machine Learning")

    # 4 Kotak Model (2x2 Grid, Font Besar & Jelas)
    models = [
        {
            "name": "1. Support Vector Machine (SVM)",
            "cat": "Model Klasik (Baseline)",
            "col": COLOR_BLUE_ACCENT,
            "x": 0.8, "y": 1.35, "w": 5.65, "h": 2.65,
            "points": [
                "Maksimasi marjin pemisah hiperplane dalam bentuk dual Lagrange:",
                "    max_α ∑ α_i - 0.5 ∑ α_i α_j y_i y_j K(x_i, x_j)",
                "Kernel Radial Basis Function (RBF): K(x_i, x_j) = exp(-γ ||x_i - x_j||²)",
                "Tuning hyperparameter C dan γ via Grid Search & 5-Fold CV.",
                "Sitasi: (Cortes & Vapnik, 1995; Schölkopf et al., 2002)"
            ]
        },
        {
            "name": "2. Random Forest (RF)",
            "cat": "Model Klasik (Ensemble Trees)",
            "col": COLOR_NAVY_MID,
            "x": 6.88, "y": 1.35, "w": 5.65, "h": 2.65,
            "points": [
                "Metode Ensemble Bagging dari B pohon keputusan acak mandiri.",
                "Prediksi agregat mayoritas: y_pred = mode{h_b(x)} untuk b=1..B.",
                "Tuning parameter: n_estimators (50–200) dan max_depth (3–10).",
                "Evaluasi Feature Importance berbasis reduksi Gini Impurity.",
                "Sitasi: (Breiman, 2001; Tyralis et al., 2019)"
            ]
        },
        {
            "name": "3. Quantum Support Vector (QSVC)",
            "cat": "Model Kuantum (Kernel-Based Qiskit)",
            "col": COLOR_EMERALD,
            "x": 0.8, "y": 4.2, "w": 5.65, "h": 2.65,
            "points": [
                "Pemetaan data non-linier ke ruang Hilbert 8D 3-qubit: |Φ(x)⟩ = U_Φ(x)|0⟩^⊗3.",
                "Sirkuit ZZFeatureMap membangkitkan belitan kuantum (quantum entanglement).",
                "Quantum Kernel Matrix: K_ij^Q = |⟨Φ(x_i)|Φ(x_j)⟩|² dihitung pada simulator kuantum.",
                "Optimasi marjin klasik diterapkan pada ruang berdimensi tinggi.",
                "Sitasi: (Havlíček et al., 2019; Schuld & Killoran, 2019)"
            ]
        },
        {
            "name": "4. Variational Quantum Classifier (VQC)",
            "cat": "Model Kuantum (Parametrized Ansatz)",
            "col": COLOR_GOLD,
            "x": 6.88, "y": 4.2, "w": 5.65, "h": 2.65,
            "points": [
                "Menggabungkan Feature Map kuantum dan ansatz sirkuit bervariasi W(θ).",
                "Status kuantum: |ψ(x, θ)⟩ = W(θ) U_Φ(x) |0⟩^⊗3 (Ansatz RealAmplitudes).",
                "Optimasi sudut θ gerbang rotasi kuantum secara iteratif via optimizer COBYLA/SPSA.",
                "Prediksi kelas melalui pembacaan nilai ekspektasi Hamiltonian: ⟨Z_0⟩.",
                "Sitasi: (Cerezo et al., 2021; Qiskit Machine Learning, 2024)"
            ]
        }
    ]

    for m in models:
        deck.add_card(s7, Inches(m["x"]), Inches(m["y"]), Inches(m["w"]), Inches(m["h"]))
        tb = s7.shapes.add_textbox(Inches(m["x"] + 0.15), Inches(m["y"] + 0.1), Inches(m["w"] - 0.3), Inches(m["h"] - 0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = m["name"]
        p0.font.name = FONT_FAMILY
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = m["col"]

        p_sub = tf.add_paragraph()
        p_sub.text = m["cat"].upper()
        p_sub.font.name = FONT_FAMILY
        p_sub.font.size = Pt(9.5)
        p_sub.font.bold = True
        p_sub.font.color.rgb = COLOR_TEXT_MUTED
        p_sub.space_after = Pt(4)

        for pt in m["points"]:
            p_pt = tf.add_paragraph()
            p_pt.space_after = Pt(2.5)
            p_pt.line_spacing = 1.15
            r = p_pt.add_run()
            r.text = "• " + pt if not pt.startswith("    ") else pt
            r.font.size = Pt(11.5)
            if "Sitasi:" in pt:
                r.font.bold = True
                r.font.size = Pt(11)
                r.font.color.rgb = COLOR_NAVY_MID

    deck.add_footer(s7, 7)

    # ==========================================================================
    # SLIDE 8: MATRIKS PENELITIAN TERDAHULU (STATE-OF-THE-ART & GAP)
    # ==========================================================================
    s8 = deck.add_blank_slide()
    deck.add_header(s8, "Bab II: Tinjauan Pustaka", "Matriks Komparasi Penelitian Terdahulu & Kebaruan Riset")

    # Table Komparasi
    headers = ["Peneliti & Tahun", "Target Analit", "Transduser", "Material Reseptor", "Model Cerdas", "Limitasi / Keterbatasan"]
    rows = [
        ["Wang et al. (2021)", "Formalin", "MOS Gas Sensor", "ZnO Nanorod", "Tanpa ML", "Suhu operasi 300 °C, boros daya, interferensi aroma bumbu tinggi."],
        ["Singhal et al. (2024)", "Formalin", "Elektrokimia", "Grafena-Kitosan", "Tanpa ML", "Destruktif, preparasi elektroda rumit, rentan fouling analit organik."],
        ["Sun et al. (2023)", "Formalin", "Biosensor Enzim", "Enzim FDH Imobil", "KNN Klasik", "Stabilitas enzim rendah (< 2 minggu), denaturasi cepat pada suhu ruang."],
        ["Gilang Pratama (2026)", "Glukosa Saliva", "GMR Spintronik", "Fe3O4/PVA-GOx", "Random Forest", "Rasio MR rendah (10–15%), terbatas pada satu model klasik saja."],
        ["Fahry R. S. (2026)\n[Penelitian Ini]", "Formalin Bakso", "TMR Spintronik\n(ALT023-10E)", "Nanofiber Hijau\nFe3O4/PVA-Sitrat-ADH", "Komparasi 4 Model\n(SVM, RF, QSVC, VQC)", "Kebaruan: MR > 200%, ikatan kovalen spesifik, analisis komparatif ruang Hilbert & uji ketahanan derau."]
    ]
    col_widths = [Inches(1.8), Inches(1.3), Inches(1.5), Inches(2.0), Inches(2.0), Inches(3.133)]
    
    table_shape = s8.shapes.add_table(len(rows) + 1, len(headers), Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.3))
    t = table_shape.table
    for idx, w in enumerate(col_widths):
        t.columns[idx].width = w

    for col_idx, h_text in enumerate(headers):
        cell = t.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    for row_idx, r_data in enumerate(rows):
        is_fahry = (row_idx == len(rows) - 1)
        bg = RGBColor(240, 253, 250) if is_fahry else (RGBColor(241, 245, 249) if row_idx % 2 == 1 else RGBColor(255, 255, 255))
        for col_idx, val in enumerate(r_data):
            cell = t.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(10 if not is_fahry else 10.5)
            p.font.bold = is_fahry
            p.font.color.rgb = COLOR_NAVY_MID if is_fahry else COLOR_TEXT_MAIN

    deck.add_footer(s8, 8)

    # ==========================================================================
    # SLIDE 9: METODOLOGI — DIAGRAM ALIR PENELITIAN KESELURUHAN
    # ==========================================================================
    s9 = deck.add_blank_slide()
    deck.add_header(s9, "Bab III: Metode Penelitian", "Diagram Alir Tahapan Penelitian Menyeluruh")

    # Kiri: 8 Tahapan Penelitian
    deck.add_card(s9, Inches(0.8), Inches(1.35), Inches(6.0), Inches(5.5))
    tb9 = s9.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.6), Inches(5.2))
    tf9 = tb9.text_frame
    tf9.word_wrap = True

    p = tf9.paragraphs[0]
    p.text = "8 TAHAPAN EKSEKUSI RISET"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(8)

    tahapan_8 = [
        ("1. Studi Literatur:", "Kajian transduser TMR, nanofiber kovalen, dan Quantum ML."),
        ("2. Desain Hardware:", "Rantai sinyal ALT023-10E → AD623 → LPF → ADS1115 → Arduino."),
        ("3. Desain Software:", "Firmware mikrokontroler dan GUI Python Raspberry Pi 5."),
        ("4. Sintesis Material:", "Elektrospinning Fe3O4/PVA, curing sitrat 130 °C, fungsionalisasi ADH."),
        ("5. Karakterisasi Medan:", "Pengujian V-B dan dV/dB terhadap acuan kumparan Helmholtz."),
        ("6. Pengujian Formalin:", "Uji respon larutan standar (0–100 ppm) dan ekstrak bakso pasar."),
        ("7. Pemodelan Cerdas:", "Pelatihan & validasi komparasi 4 model (SVM, RF, QSVC, VQC)."),
        ("8. Evaluasi & Laporan:", "Analisis noise robustness, penyusunan naskah, dan publikasi.")
    ]
    for step, desc in tahapan_8:
        p_st = tf9.add_paragraph()
        p_st.space_after = Pt(6)
        p_st.line_spacing = 1.15
        r_s = p_st.add_run()
        r_s.text = step + " "
        r_s.font.bold = True
        r_s.font.size = Pt(12)
        r_s.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_st.add_run()
        r_d.text = desc
        r_d.font.size = Pt(11.5)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    # Kanan: Diagram Alir Gambar TikZ / Visual
    deck.add_card(s9, Inches(7.1), Inches(1.35), Inches(5.433), Inches(5.5))
    tb9_r = s9.shapes.add_textbox(Inches(7.3), Inches(1.5), Inches(5.0), Inches(5.2))
    tf9_r = tb9_r.text_frame
    tf9_r.word_wrap = True
    p_rh = tf9_r.paragraphs[0]
    p_rh.text = "PENJAMINAN MUTU DATA RISET"
    p_rh.font.name = FONT_FAMILY
    p_rh.font.size = Pt(14)
    p_rh.font.bold = True
    p_rh.font.color.rgb = COLOR_EMERALD
    p_rh.space_after = Pt(12)

    qa_points = [
        ("• Ground Truth Metrologis:", "Pengukuran medan magnet Helmholtz menggunakan teslameter terkalibrasi sebagai acuan absolut."),
        ("• Replikasi Pengukuran:", "Setiap titik konsentrasi diukur secara berulang (triplo) untuk mendapatkan simpangan baku presisi."),
        ("• Protokol Stabilisasi:", "Akuisisi 5.0 detik mengabaikan 1.0 detik pertama (settling time) untuk membuang efek transien awal."),
        ("• Pencegahan Data Leakage:", "Standarisasi fitur dan pembagian dataset dilakukan berbasis sampel tetesan independen, bukan irisan waktu yang sama.")
    ]
    for q_t, q_d in qa_points:
        p_qa = tf9_r.add_paragraph()
        p_qa.space_after = Pt(12)
        p_qa.line_spacing = 1.2
        r_t = p_qa.add_run()
        r_t.text = q_t + "\n"
        r_t.font.bold = True
        r_t.font.size = Pt(12)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_qa.add_run()
        r_d.text = q_d
        r_d.font.size = Pt(11.5)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s9, 9)

    # ==========================================================================
    # SLIDE 10: METODOLOGI — DESAIN MEKATRONIKA & SKEMATIK RANGKAIAN
    # ==========================================================================
    s10 = deck.add_blank_slide()
    deck.add_header(s10, "Bab III: Metode Penelitian", "Desain Mekatronika & Rangkaian Perangkat Keras")

    # Kiri: Realisasi Desain Mekatronika
    deck.add_card(s10, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb10_l = s10.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(5.25), Inches(1.2))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True
    p = tf10_l.paragraphs[0]
    p.text = "1. Mekatronika Casing & Kumparan Helmholtz"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(4)
    p_desc = tf10_l.add_paragraph()
    p_desc.text = "Kit terintegrasi dengan layar sentuh Raspberry Pi 5, mikrokontroler Arduino Uno, kumparan Helmholtz (0–16 V DC), dan slot sensor TMR."
    p_desc.font.size = Pt(11.5)
    p_desc.font.color.rgb = COLOR_TEXT_MAIN

    # Gambar Casing
    deck.add_image_fitted(s10, "Gambar/Bab3/babIII_desainluar.jpg", Inches(1.0), Inches(2.7), Inches(2.6), Inches(3.9), border=True)
    deck.add_image_fitted(s10, "Gambar/Bab3/babIII_desaindalam.jpg", Inches(3.8), Inches(2.7), Inches(2.6), Inches(3.9), border=True)

    # Kanan: Skematik Rangkaian TMR-AD623-ADS1115
    deck.add_card(s10, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb10_r = s10.shapes.add_textbox(Inches(7.08), Inches(1.45), Inches(5.25), Inches(1.2))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True
    p = tf10_r.paragraphs[0]
    p.text = "2. Rantai Sinyal Presisi & Grounding"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY_MID
    p.space_after = Pt(4)
    p_desc = tf10_r.add_paragraph()
    p_desc.text = "Filter RFI diferensial, AD623 (G=11, VREF=2.50 V), LPF pasif RC (fc=159 Hz), ADS1115 16-bit, serta pemisahan ground AGND dan DGND."
    p_desc.font.size = Pt(11.5)
    p_desc.font.color.rgb = COLOR_TEXT_MAIN

    # Gambar Skematik
    deck.add_image_fitted(s10, "Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png", Inches(7.08), Inches(2.7), Inches(5.25), Inches(3.9), border=True)

    deck.add_footer(s10, 10)

    # ==========================================================================
    # SLIDE 11: METODOLOGI — DIAGRAM ALIR SOFTWARE (ARDUINO & PYTHON)
    # ==========================================================================
    s11 = deck.add_blank_slide()
    deck.add_header(s11, "Bab III: Metode Penelitian", "Diagram Alir Perangkat Lunak Mikrokontroler & Python Host")

    # Kiri: Firmware Arduino
    deck.add_card(s11, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb11_l = s11.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(5.25), Inches(1.0))
    tf11_l = tb11_l.text_frame
    tf11_l.word_wrap = True
    p = tf11_l.paragraphs[0]
    p.text = "1. Firmware Arduino Uno (sensor_tmr_formalin.ino)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p_sub = tf11_l.add_paragraph()
    p_sub.text = "Akuisisi deterministik 128 SPS, pembacaan I2C pin AIN0, streaming serial CSV murni tanpa rata-rata."
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    deck.add_image_fitted(s11, "Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png", Inches(1.5), Inches(2.55), Inches(4.2), Inches(4.1), border=True)

    # Kanan: Software Host Python
    deck.add_card(s11, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb11_r = s11.shapes.add_textbox(Inches(7.08), Inches(1.45), Inches(5.25), Inches(1.0))
    tf11_r = tb11_r.text_frame
    tf11_r.word_wrap = True
    p = tf11_r.paragraphs[0]
    p.text = "2. Host Python GUI (kalibrasi_tmr_formalin.py)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p_sub = tf11_r.add_paragraph()
    p_sub.text = "Engine berbasis durasi 5.0 detik (buang settling time 1.0 detik), regresi linier otomatis, dan plot 300 DPI."
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    deck.add_image_fitted(s11, "Gambar/Bab3/babIII_DiagramAlirPython.drawio.png", Inches(7.08), Inches(2.55), Inches(5.25), Inches(4.1), border=True)

    deck.add_footer(s11, 11)

    # ==========================================================================
    # SLIDE 12: METODOLOGI — DIAGRAM ALIR PEMODELAN 4 MODEL & DEPLOYMENT
    # ==========================================================================
    s12 = deck.add_blank_slide()
    deck.add_header(s12, "Bab III: Metode Penelitian", "Diagram Alir Pemodelan 4 Model & Deployment Realtime")

    # Kiri: Pelatihan Model Building 4 Model
    deck.add_card(s12, Inches(0.8), Inches(1.35), Inches(6.2), Inches(5.5))
    tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(5.8), Inches(0.9))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True
    p = tf12_l.paragraphs[0]
    p.text = "Pelatihan Komparatif 4 Model (SVM, RF vs QSVC, VQC)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p_sub = tf12_l.add_paragraph()
    p_sub.text = "Ekstraksi 3 Fitur (V_mean, ΔV, σ_V), split 80:20, validasi 5-fold CV, dan uji noise robustness."
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    deck.add_image_fitted(s12, "Gambar/Bab3/babIII_ModelBuilding.drawio.png", Inches(1.0), Inches(2.45), Inches(5.8), Inches(4.25), border=True)

    # Kanan: Deployment Model
    deck.add_card(s12, Inches(7.2), Inches(1.35), Inches(5.333), Inches(5.5))
    tb12_r = s12.shapes.add_textbox(Inches(7.4), Inches(1.45), Inches(4.9), Inches(0.9))
    tf12_r = tb12_r.text_frame
    tf12_r.word_wrap = True
    p = tf12_r.paragraphs[0]
    p.text = "Deployment Sistem Inferensi Realtime"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p_sub = tf12_r.add_paragraph()
    p_sub.text = "Penerapan model optimal pada Raspberry Pi 5 GUI untuk klasifikasi status keamanan pangan bakso."
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    deck.add_image_fitted(s12, "Gambar/Bab3/babIII_ModelDeploy.drawio.png", Inches(7.4), Inches(2.45), Inches(4.9), Inches(4.25), border=True)

    deck.add_footer(s12, 12)

    # ==========================================================================
    # SLIDE 13: METODOLOGI — SINTESIS NANOFIBER & PREPARASI BAKSO
    # ==========================================================================
    s13 = deck.add_blank_slide()
    deck.add_header(s13, "Bab III: Metode Penelitian", "Sintesis Nanofiber Kovalen & Preparasi Sampel Bakso Riil")

    # Kiri: Sintesis Nanofiber
    deck.add_card(s13, Inches(0.8), Inches(1.35), Inches(5.65), Inches(5.5))
    tb13_l = s13.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.25), Inches(5.2))
    tf13_l = tb13_l.text_frame
    tf13_l.word_wrap = True
    p = tf13_l.paragraphs[0]
    p.text = "SINTESIS NANOFIBER Fe3O4/PVA-SITRAT-ADH"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE_ACCENT
    p.space_after = Pt(10)

    sintesis_steps = [
        ("1. Sintesis Fe3O4 Hijau:", "Kopresipitasi garam besi dengan ekstrak daun kelor sebagai agen pereduksi ramah lingkungan."),
        ("2. Larutan Polimer Doping:", "Pencampuran PVA 10% w/v dengan 2% w/v nanopartikel Fe3O4 dan 5% w/v asam sitrat."),
        ("3. Proses Electrospinning:", "Tegangan tinggi 15 kV, jarak jarum-kolektor 12 cm, laju alir syringe pump 0.8 mL/jam."),
        ("4. Thermal Curing 130 °C:", "Pemanasan oven 130 °C selama 2 jam untuk reaksi esterifikasi penaut silang anti-air."),
        ("5. Imobilisasi ADH:", "Fungsionalisasi gugus hidrazida terminal bebas sebagai chemo-receptor spesifik formaldehida.")
    ]
    for title, desc in sintesis_steps:
        p_item = tf13_l.add_paragraph()
        p_item.space_after = Pt(9)
        p_item.line_spacing = 1.15
        r_t = p_item.add_run()
        r_t.text = title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(12.5)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = desc
        r_d.font.size = Pt(11.5)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    # Kanan: Preparasi Sampel Bakso
    deck.add_card(s13, Inches(6.88), Inches(1.35), Inches(5.65), Inches(5.5))
    tb13_r = s13.shapes.add_textbox(Inches(7.08), Inches(1.5), Inches(5.25), Inches(5.2))
    tf13_r = tb13_r.text_frame
    tf13_r.word_wrap = True
    p = tf13_r.paragraphs[0]
    p.text = "PREPARASI & PENGUJIAN SAMPEL BAKSO"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_EMERALD
    p.space_after = Pt(10)

    bakso_steps = [
        ("1. Sampling Pasar:", "Pengambilan sampel bakso sapi dari pasar tradisional dan pasar modern di wilayah Bandung."),
        ("2. Pembuatan Sampel Kontrol:", "Bakso higienis buatan laboratorium tanpa penambahan bahan pengawet sintetik."),
        ("3. Preparasi Sampel Spiked:", "Injeksi larutan formalin dengan variasi konsentrasi terukur (10, 20, 50, 100 ppm) untuk validasi."),
        ("4. Ekstraksi Filtrat:", "Penghancuran mekanik sampel bakso, penambahan aquades steril, sonikasi 15 menit, dan sentrifugasi."),
        ("5. Prosedur Uji Sensor TMR:", "Penetesan 50 µL filtrat ke atas reseptor nanofiber, perekaman sinyal 5.0 detik, dan inferensi ML.")
    ]
    for title, desc in bakso_steps:
        p_item = tf13_r.add_paragraph()
        p_item.space_after = Pt(9)
        p_item.line_spacing = 1.15
        r_t = p_item.add_run()
        r_t.text = title + " "
        r_t.font.bold = True
        r_t.font.size = Pt(12.5)
        r_t.font.color.rgb = COLOR_NAVY_DARK
        r_d = p_item.add_run()
        r_d.text = desc
        r_d.font.size = Pt(11.5)
        r_d.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s13, 13)

    # ==========================================================================
    # SLIDE 14: METODOLOGI — JADWAL PELAKSANAAN RISET (GANTT CHART)
    # ==========================================================================
    s14 = deck.add_blank_slide()
    deck.add_header(s14, "Bab III: Metode Penelitian", "Jadwal & Tempat Pelaksanaan Penelitian (Gantt Chart)")

    # Info Tempat
    deck.add_card(s14, Inches(0.8), Inches(1.35), Inches(11.733), Inches(1.15), bg_color=COLOR_NAVY_DARK, border_color=COLOR_NAVY_MID)
    tb14_top = s14.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(11.333), Inches(0.95))
    tf14_top = tb14_top.text_frame
    tf14_top.word_wrap = True
    p1 = tf14_top.paragraphs[0]
    p1.text = "LOKASI & PERIODE RISET: BOLABOT TECHNO ROBOTIC INSTITUTE BANDUNG"
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(12)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(147, 197, 253)
    p2 = tf14_top.add_paragraph()
    p2.text = "Jl. Sauyunan VI No. 10 Blok F6, Kelurahan Cipadung, Kecamatan Panyileukan, Kota Bandung, Jawa Barat 40614.\nPeriode Riset Efektif: Bulan September – Desember 2026 (Durasi: 16 Pekan Kerja Efektif)."
    p2.font.size = Pt(11)
    p2.font.color.rgb = RGBColor(241, 245, 249)

    # Tabel Gantt Chart
    g_headers = ["No", "Tahapan Kegiatan Penelitian", "Bulan 1 (Sep)", "Bulan 2 (Okt)", "Bulan 3 (Nov)", "Bulan 4 (Des)"]
    g_rows = [
        ["1", "Studi literatur & perancangan desain rantai sinyal hardware", "[ X ]", "[   ]", "[   ]", "[   ]"],
        ["2", "Sintesis material nanofiber Fe3O4/PVA-Sitrat-ADH kovalen", "[ X ]", "[ X ]", "[   ]", "[   ]"],
        ["3", "Perakitan instrumen TMR, kalibrasi Helmholtz, & firmware", "[   ]", "[ X ]", "[ X ]", "[   ]"],
        ["4", "Pengujian larutan formalin standar & ekstrak sampel bakso", "[   ]", "[   ]", "[ X ]", "[   ]"],
        ["5", "Pelatihan & komparasi model klasik vs kuantum (Qiskit)", "[   ]", "[   ]", "[ X ]", "[ X ]"],
        ["6", "Evaluasi noise robustness, analisis metrologis, & skripsi", "[   ]", "[   ]", "[   ]", "[ X ]"]
    ]
    g_widths = [Inches(0.6), Inches(5.933), Inches(1.3), Inches(1.3), Inches(1.3), Inches(1.3)]
    
    table_shape = s14.shapes.add_table(len(g_rows) + 1, len(g_headers), Inches(0.8), Inches(2.7), Inches(11.733), Inches(4.15))
    gt = table_shape.table
    for idx, w in enumerate(g_widths):
        gt.columns[idx].width = w

    for col_idx, h_text in enumerate(g_headers):
        cell = gt.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_MID
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    for row_idx, r_data in enumerate(g_rows):
        bg = RGBColor(241, 245, 249) if row_idx % 2 == 1 else RGBColor(255, 255, 255)
        for col_idx, val in enumerate(r_data):
            cell = gt.cell(row_idx + 1, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = FONT_FAMILY
            p.font.size = Pt(10.5)
            p.font.bold = ("[ X ]" in val)
            if "[ X ]" in val:
                p.font.color.rgb = COLOR_BLUE_ACCENT
                p.alignment = PP_ALIGN.CENTER
            elif "[   ]" in val:
                p.font.color.rgb = COLOR_TEXT_MUTED
                p.alignment = PP_ALIGN.CENTER
            else:
                p.font.color.rgb = COLOR_TEXT_MAIN
                if col_idx == 0:
                    p.alignment = PP_ALIGN.CENTER

    deck.add_footer(s14, 14)

    # ==========================================================================
    # SLIDE 15: DAFTAR PUSTAKA ACUAN UTAMA
    # ==========================================================================
    s15 = deck.add_blank_slide()
    deck.add_header(s15, "Daftar Pustaka", "Pustaka Rujukan Utama Berbobot Internasional")

    deck.add_card(s15, Inches(0.8), Inches(1.35), Inches(11.733), Inches(5.5))
    tb15 = s15.shapes.add_textbox(Inches(1.1), Inches(1.5), Inches(11.133), Inches(5.2))
    tf15 = tb15.text_frame
    tf15.word_wrap = True

    references = [
        "Analog Devices. (2020). AD623: Single-Supply, Rail-to-Rail, Low Cost Instrumentation Amplifier Data Sheet (Rev. E). Norwood: Analog Devices, Inc.",
        "Antarnusa, G., Suharyadi, E., & Kato, T. (2022). Giant Magnetoresistance Biosensor Based on Fe3O4 Magnetic Nanoparticles for Biomedical Applications. Sensors, 22(14), 5120.",
        "Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.",
        "Cerezo, M., Arrasmith, A., Babbush, R., Benjamin, S. C., Endo, S., Fujii, K., ... & Coles, P. J. (2021). Variational Quantum Algorithms. Nature Reviews Physics, 3(9), 625–644.",
        "Cortes, C., & Vapnik, V. (1995). Support-Vector Networks. Machine Learning, 20(3), 273–297.",
        "Havlíček, V., Córcoles, A. D., Temme, K., Harrow, A. W., Kandala, A., Chow, J. M., & Gambetta, J. M. (2019). Supervised Learning with Quantum-Enhanced Feature Spaces. Nature, 567(7747), 209–212.",
        "Hermanson, G. T. (2013). Bioconjugate Techniques (3rd ed.). Boston: Academic Press.",
        "Mocak, J., Bond, A. M., Mitchell, S., & Scollary, G. (1997). A Statistical Overview of Limit of Detection and Limit of Quantification in Analytical Chemistry. Pure and Applied Chemistry, 69(2), 297–328.",
        "NVE Corporation. (2023). TMR ALT023-10E High Sensitivity Analog Magnetometer Sensor Catalog. Eden Prairie: NVE Corporation.",
        "Pannetier, M., Fermon, C., Le Goff, G., Simola, J., & Kerr, E. (2022). High-Sensitivity TMR Sensors for Biomagnetic Applications. Journal of Magnetism and Magnetic Materials, 548, 168920."
    ]

    p_init = tf15.paragraphs[0]
    p_init.text = "DAFTAR REFERENSI KUNCI PROPOSAL"
    p_init.font.name = FONT_FAMILY
    p_init.font.size = Pt(14)
    p_init.font.bold = True
    p_init.font.color.rgb = COLOR_NAVY_MID
    p_init.space_after = Pt(10)

    for ref in references:
        p_ref = tf15.add_paragraph()
        p_ref.space_after = Pt(7)
        p_ref.line_spacing = 1.15
        r_b = p_ref.add_run()
        r_b.text = "• "
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_BLUE_ACCENT
        r_t = p_ref.add_run()
        r_t.text = ref
        r_t.font.name = FONT_FAMILY
        r_t.font.size = Pt(11.5)
        r_t.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s15, 15)

    # ==========================================================================
    # SLIDE 16: PENUTUP (SEKIAN & SESI DISKUSI)
    # ==========================================================================
    s16 = deck.add_blank_slide()

    # Center Hero Card
    deck.add_card(s16, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), bg_color=COLOR_CARD_BG, border_color=COLOR_BLUE_ACCENT)

    # Logos Top Center
    deck.add_image_fitted(s16, "Gambar/Logo/Logo UIN.png", Inches(5.4), Inches(1.5), Inches(1.1), Inches(1.1), border=False)
    deck.add_image_fitted(s16, "Gambar/Logo/Logo Fisika UIN.png", Inches(6.8), Inches(1.5), Inches(1.1), Inches(1.1), border=False)

    tb16 = s16.shapes.add_textbox(Inches(1.8), Inches(2.8), Inches(9.733), Inches(3.2))
    tf16 = tb16.text_frame
    tf16.word_wrap = True

    p_t = tf16.paragraphs[0]
    p_t.text = "SEKIAN & TERIMA KASIH"
    p_t.font.name = FONT_FAMILY
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_NAVY_DARK
    p_t.alignment = PP_ALIGN.CENTER
    p_t.space_after = Pt(8)

    p_s = tf16.add_paragraph()
    p_s.text = "Sesi Diskusi & Tanya Jawab Seminar Proposal Tugas Akhir"
    p_s.font.name = FONT_FAMILY
    p_s.font.size = Pt(16)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_BLUE_ACCENT
    p_s.alignment = PP_ALIGN.CENTER
    p_s.space_after = Pt(18)

    p_n = tf16.add_paragraph()
    p_n.text = "Fahry Rizky Samsudin (NIM: 1237030018)"
    p_n.font.name = FONT_FAMILY
    p_n.font.size = Pt(14)
    p_n.font.bold = True
    p_n.font.color.rgb = COLOR_NAVY_MID
    p_n.alignment = PP_ALIGN.CENTER
    p_n.space_after = Pt(4)

    p_i = tf16.add_paragraph()
    p_i.text = "Jurusan Fisika, Fakultas Sains dan Teknologi\nUniversitas Islam Negeri Sunan Gunung Djati Bandung\nTahun 2026"
    p_i.font.name = FONT_FAMILY
    p_i.font.size = Pt(12)
    p_i.font.color.rgb = COLOR_TEXT_MUTED
    p_i.alignment = PP_ALIGN.CENTER

    deck.add_footer(s16, 16)

    # Save presentation
    deck.save()

if __name__ == "__main__":
    build_clean_deck()
