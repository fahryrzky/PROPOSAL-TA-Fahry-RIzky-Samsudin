"""
Skrip Pembuat Presentasi Seminar Proposal Tugas Akhir (24 Slide Lengkap)
Peneliti : Fahry Rizky Samsudin (NIM: 1237030018)
Jurusan  : Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
Tahun    : 2026
"""

import os
import sys
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# KONFIGURASI WARNA & TIPOGRAFI (Academic Minimalist - Anti Slop)
# ==============================================================================
COLOR_BG_PAGE     = RGBColor(248, 250, 252) # Slate-50 (#F8FAFC)
COLOR_CARD_FILL   = RGBColor(255, 255, 255) # Pure White
COLOR_CARD_BORDER = RGBColor(226, 232, 240) # Slate-200 (#E2E8F0)
COLOR_TEXT_MAIN   = RGBColor(15, 23, 42)    # Slate-900 (#0F172A)
COLOR_TEXT_BODY   = RGBColor(51, 65, 85)    # Slate-700 (#334155)
COLOR_TEXT_MUTED  = RGBColor(100, 116, 139) # Slate-500 (#64748B)

COLOR_NAVY_DARK   = RGBColor(15, 30, 74)    # Deep Academic Navy (#0F1E4A)
COLOR_NAVY_MID    = RGBColor(30, 58, 138)   # Royal Navy (#1E3A8A)
COLOR_BLUE_ACCENT = RGBColor(37, 99, 235)   # Blue Accent (#2563EB)
COLOR_EMERALD     = RGBColor(5, 150, 105)   # Emerald (#059669)
COLOR_AMBER       = RGBColor(217, 119, 6)   # Amber (#D97706)
COLOR_LIGHT_BLUE  = RGBColor(239, 246, 255) # Blue-50 (#EFF6FF)
COLOR_LIGHT_EMR   = RGBColor(236, 253, 245) # Emerald-50 (#ECFDF5)
COLOR_LIGHT_AMB   = RGBColor(255, 251, 235) # Amber-50 (#FFFBEB)

FONT_FAMILY = "Segoe UI"
TOTAL_SLIDES = 24

# ==============================================================================
# BUILDER CLASS
# ==============================================================================
class AcademicDeckBuilder:
    def __init__(self, filename="Proposal_TA_Fahry_Rizky_Samsudin.pptx"):
        self.filename = filename
        self.prs = Presentation()
        # Widescreen 16:9 (13.333 x 7.5 Inches)
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]
        self.slide_count = 0

    def add_blank_slide(self):
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.slide_count += 1
        # Latar belakang bersih
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_PAGE
        bg.line.fill.background()
        return slide

    def add_header(self, slide, section_name, title_text, subtitle_text=None):
        """Header akademik dengan posisi identik di semua slide."""
        # Badge Section
        b_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(10), Inches(0.32))
        tf_b = b_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.text = section_name.upper()
        p_b.font.name = FONT_FAMILY
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_BLUE_ACCENT

        # Title Box
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.70), Inches(11.733), Inches(0.65))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(19)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY_DARK

        if subtitle_text:
            p_sub = tf_t.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED
            p_sub.space_before = Pt(2)

        # Dividing Line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.38), Inches(11.733), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

    def add_footer(self, slide, current_slide, footnote_text=None):
        """Footer akademik konsisten dengan penomoran slide."""
        # Garis pemisah footer
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.012))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

        # Teks Footer Kiri
        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.06), Inches(9.8), Inches(0.3))
        tf_f = f_box.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        if footnote_text:
            p_f.text = footnote_text
            p_f.font.size = Pt(9)
            p_f.font.color.rgb = COLOR_TEXT_MUTED
        else:
            p_f.text = "Fahry Rizky Samsudin (1237030018) | Proposal Tugas Akhir Fisika UIN Sunan Gunung Djati Bandung"
            p_f.font.size = Pt(9.5)
            p_f.font.color.rgb = COLOR_TEXT_MUTED
        p_f.font.name = FONT_FAMILY

        # Nomor Halaman Kanan
        p_box = slide.shapes.add_textbox(Inches(10.8), Inches(7.06), Inches(1.733), Inches(0.3))
        tf_p = p_box.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
        pp = tf_p.paragraphs[0]
        pp.text = f"{current_slide} / {TOTAL_SLIDES}"
        pp.alignment = PP_ALIGN.RIGHT
        pp.font.name = FONT_FAMILY
        pp.font.size = Pt(9.5)
        pp.font.bold = True
        pp.font.color.rgb = COLOR_NAVY_MID

    def add_card(self, slide, left, top, width, height, bg_color=COLOR_CARD_FILL, border_color=COLOR_CARD_BORDER):
        """Membuat kontainer kartu bersih minimalis."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    def add_card_header(self, tf, title_text, category_badge=None, badge_color=COLOR_BLUE_ACCENT):
        """Menambahkan header di dalam kartu."""
        if category_badge:
            p_badge = tf.paragraphs[0] if len(tf.paragraphs[0].text) == 0 else tf.add_paragraph()
            p_badge.text = category_badge.upper()
            p_badge.font.name = FONT_FAMILY
            p_badge.font.size = Pt(8.5)
            p_badge.font.bold = True
            p_badge.font.color.rgb = badge_color
            p_badge.space_after = Pt(2)
            
            p_title = tf.add_paragraph()
        else:
            p_title = tf.paragraphs[0] if len(tf.paragraphs[0].text) == 0 else tf.add_paragraph()

        p_title.text = title_text
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(13)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY_DARK
        p_title.space_after = Pt(6)

    def add_bullet_item(self, tf, bold_prefix, text, pt_size=11.5, space_after=6, color=COLOR_TEXT_BODY):
        """Menambahkan poin daftar dengan prefiks bold."""
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        p.line_spacing = 1.15

        r_bullet = p.add_run()
        r_bullet.text = "• "
        r_bullet.font.name = FONT_FAMILY
        r_bullet.font.bold = True
        r_bullet.font.color.rgb = COLOR_BLUE_ACCENT
        r_bullet.font.size = Pt(pt_size)

        if bold_prefix:
            r_bold = p.add_run()
            r_bold.text = bold_prefix + " "
            r_bold.font.name = FONT_FAMILY
            r_bold.font.bold = True
            r_bold.font.color.rgb = COLOR_TEXT_MAIN
            r_bold.font.size = Pt(pt_size)

        r_text = p.add_run()
        r_text.text = text
        r_text.font.name = FONT_FAMILY
        r_text.font.color.rgb = color
        r_text.font.size = Pt(pt_size)

    def add_image_fitted(self, slide, img_path, left, top, max_w, max_h, border=True, caption=None):
        """Menyisipkan gambar dengan kalkulasi aspect ratio presisi tanpa distorsi."""
        if not os.path.exists(img_path):
            print(f"[WARN] File gambar tidak ditemukan: {img_path}")
            return None

        im = Image.open(img_path)
        im_w, im_h = im.size
        aspect = im_w / im_h

        box_w = max_w.inches
        box_h = max_h.inches

        if (box_w / box_h) > aspect:
            calc_h = box_h
            calc_w = calc_h * aspect
        else:
            calc_w = box_w
            calc_h = calc_w / aspect

        final_left = left.inches + (box_w - calc_w) / 2
        final_top = top.inches + (box_h - calc_h) / 2

        if border:
            self.add_card(
                slide,
                Inches(final_left - 0.04),
                Inches(final_top - 0.04),
                Inches(calc_w + 0.08),
                Inches(calc_h + 0.08),
                bg_color=COLOR_CARD_FILL,
                border_color=COLOR_CARD_BORDER
            )

        pic = slide.shapes.add_picture(
            img_path,
            Inches(final_left),
            Inches(final_top),
            Inches(calc_w),
            Inches(calc_h)
        )

        if caption:
            c_box = slide.shapes.add_textbox(
                Inches(final_left - 0.2),
                Inches(final_top + calc_h + 0.05),
                Inches(calc_w + 0.4),
                Inches(0.3)
            )
            tf_c = c_box.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
            pc = tf_c.paragraphs[0]
            pc.text = caption
            pc.alignment = PP_ALIGN.CENTER
            pc.font.name = FONT_FAMILY
            pc.font.size = Pt(8.5)
            pc.font.italic = True
            pc.font.color.rgb = COLOR_TEXT_MUTED

        return pic

    def save(self):
        self.prs.save(self.filename)
        print(f"[SUKSES] Presentasi tersimpan: {self.filename} ({self.slide_count} slides).")

# ==============================================================================
# FUNGSI PEMBUAT SLIDE 1 HINGGA 24
# ==============================================================================

def build_slide_1(builder):
    """Slide 1: Cover Proposal"""
    slide = builder.add_blank_slide()

    # Card Luar Utama Cover
    builder.add_card(slide, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9), bg_color=COLOR_CARD_FILL, border_color=COLOR_CARD_BORDER)

    # Aksen Atas Kartu
    accent_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.12))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = COLOR_NAVY_MID
    accent_bar.line.fill.background()

    # Logo UIN di Kiri Atas
    logo_path = "Gambar/Logo/Logo UIN.png"
    if os.path.exists(logo_path):
        builder.add_image_fitted(slide, logo_path, Inches(1.3), Inches(1.4), Inches(1.5), Inches(1.5), border=False)

    # Box Teks Judul Cover
    tb = slide.shapes.add_textbox(Inches(3.1), Inches(1.3), Inches(9.0), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_badge = tf.paragraphs[0]
    p_badge.text = "SEMINAR PROPOSAL TUGAS AKHIR"
    p_badge.font.name = FONT_FAMILY
    p_badge.font.size = Pt(11)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_BLUE_ACCENT
    p_badge.space_after = Pt(8)

    p_title = tf.add_paragraph()
    p_title.text = "Rancang Bangun Instrumentasi Sensor Tunneling Magnetoresistance Berbasis Nanofiber Fe3O4/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC"
    p_title.font.name = FONT_FAMILY
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY_DARK
    p_title.space_after = Pt(8)

    p_sub = tf.add_paragraph()
    p_sub.text = "Kajian Eksperimental Sensor TMR ALT023-10E, Fungsionalisasi Nanomaterial Magnetik, dan Pembelajaran Mesin Kuantum"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    # Garis Pembatas Identitas
    div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.3), Inches(4.7), Inches(10.733), Inches(0.015))
    div.fill.solid()
    div.fill.fore_color.rgb = COLOR_CARD_BORDER
    div.line.fill.background()

    # Kolom Identitas Peneliti & Pembimbing
    tb_id = slide.shapes.add_textbox(Inches(1.3), Inches(4.9), Inches(5.5), Inches(1.5))
    tf_id = tb_id.text_frame
    tf_id.word_wrap = True
    tf_id.margin_left = tf_id.margin_top = tf_id.margin_right = tf_id.margin_bottom = 0

    p1 = tf_id.paragraphs[0]
    p1.text = "PENELITI / MAHASISWA"
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(9.5)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_BLUE_ACCENT
    p1.space_after = Pt(2)

    p2 = tf_id.add_paragraph()
    p2.text = "Fahry Rizky Samsudin"
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_TEXT_MAIN

    p3 = tf_id.add_paragraph()
    p3.text = "NIM: 1237030018 | Jurusan Fisika"
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = COLOR_TEXT_BODY

    # Kolom Institusi
    tb_inst = slide.shapes.add_textbox(Inches(7.2), Inches(4.9), Inches(4.8), Inches(1.5))
    tf_inst = tb_inst.text_frame
    tf_inst.word_wrap = True
    tf_inst.margin_left = tf_inst.margin_top = tf_inst.margin_right = tf_inst.margin_bottom = 0

    pi1 = tf_inst.paragraphs[0]
    pi1.text = "INSTITUSI & TAHUN"
    pi1.font.name = FONT_FAMILY
    pi1.font.size = Pt(9.5)
    pi1.font.bold = True
    pi1.font.color.rgb = COLOR_BLUE_ACCENT
    pi1.space_after = Pt(2)

    pi2 = tf_inst.add_paragraph()
    pi2.text = "Fakultas Sains dan Teknologi"
    pi2.font.name = FONT_FAMILY
    pi2.font.size = Pt(12)
    pi2.font.bold = True
    pi2.font.color.rgb = COLOR_TEXT_MAIN

    pi3 = tf_inst.add_paragraph()
    pi3.text = "UIN Sunan Gunung Djati Bandung — 2026"
    pi3.font.name = FONT_FAMILY
    pi3.font.size = Pt(10.5)
    pi3.font.color.rgb = COLOR_TEXT_BODY

    builder.add_footer(slide, 1, "Seminar Proposal Skripsi Program Studi Fisika UIN Sunan Gunung Djati Bandung")


def build_slide_2(builder):
    """Slide 2: Agenda Paparan"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Sistematika Presentasi", "Agenda Paparan Proposal Penelitian", "Struktur paparan proposal mencakup empat pilar bahasan ilmiah terpadu")

    # 4 Card Grid (2 Baris x 2 Kolom)
    cards = [
        ("01. PENDAHULUAN", "Latar Belakang & Perumusan Masalah", [
            ("Urgensi Pangan:", "Bahaya formalin pada bakso & keterbatasan uji konvensional."),
            ("Teknologi TMR:", "Peluang sensor magnetoresistansi ultra-sensitif."),
            ("Rumusan & Batasan:", "Fokus masalah terukur & ruang lingkup kerja."),
            ("Tujuan & Manfaat:", "Target luaran ilmiah dan kontribusi aplikatif.")
        ]),
        ("02. LANDASAN TEORI", "Fisika Instrumentasi, Material & Model ML", [
            ("Sensor TMR ALT023:", "Mekanisme MTJ dan formula model Julliere."),
            ("Rantai Sinyal:", "Pengondisi sinyal AD623 (Vref=2.50V) & ADC ADS1115."),
            ("Nanofiber Fungsional:", "Fe3O4/PVA-Sitrat dan reseptor spesifik ADH."),
            ("Komparasi Model:", "Kernel SVM klasik vs ruang Hilbert kuantum (QSVC).")
        ]),
        ("03. METODE PENELITIAN", "Desain Hardware, Software & Sintesis", [
            ("Waktu & Tempat:", "Lab Fisika Instrumentasi & Lab Sains Terpadu UIN SGD."),
            ("Desain Perangkat:", "Skematik PCB, casing 3D & Helmholtz 0-16V."),
            ("Perangkat Lunak:", "Firmware Arduino & GUI Python OriginLab 3D."),
            ("Sintesis & Karakterisasi:", "Electrospinning 15 kV & kalibrasi respons sensor.")
        ]),
        ("04. RENCANA & LUARAN", "Pengujian Analit & Roadmap Penelitian", [
            ("Protokol Sampel:", "Spiking formalin bakso (0-1000 ppm) & ekstraksi 5 fitur."),
            ("Pipeline Evaluasi:", "5-Fold CV, metrik ROC-AUC, dan waktu inferensi."),
            ("Deploy Instrumentasi:", "Integrasi model klasifikasi ke GUI desktop."),
            ("Roadmap 6 Bulan:", "Jadwal kerja sistematis Semester Genap 2026.")
        ])
    ]

    coords = [
        (Inches(0.8), Inches(1.65)),
        (Inches(6.8), Inches(1.65)),
        (Inches(0.8), Inches(4.3)),
        (Inches(6.8), Inches(4.3))
    ]

    for (cat, title, items), (c_left, c_top) in zip(cards, coords):
        builder.add_card(slide, c_left, c_top, Inches(5.733), Inches(2.45))
        tb = slide.shapes.add_textbox(c_left + Inches(0.25), c_top + Inches(0.2), Inches(5.233), Inches(2.05))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        builder.add_card_header(tf, title, cat)
        for b_prefix, b_text in items:
            builder.add_bullet_item(tf, b_prefix, b_text, pt_size=10.5, space_after=4)

    builder.add_footer(slide, 2)


def build_slide_3(builder):
    """Slide 3: Latar Belakang I"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Latar Belakang I: Bahaya Formalin & Limitasi Pengujian Eksisting", "Krisis keamanan pangan dan urgensi pengembangan metode deteksi portabel kuantitatif")

    # Card Kiri: Bahaya Formalin
    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(3.7)
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Penyalahgunaan Formalin pada Produk Bakso", "URGENSI KESEHATAN MASYARAKAT", COLOR_AMBER)
    builder.add_bullet_item(tf1, "Karsinogen Golongan 1:", "IARC mengklasifikasikan formaldehida sebagai senyawa karsinogenik terbukti pada manusia.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Motif Penyalahgunaan:", "Sering disalahgunakan secara ilegal sebagai pengawet bakso untuk menghambat pembusukan mikroba dan memanipulasi kekenyalan tekstur daging.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Dampak Kesehatan Akut & Kronis:", "Paparan jangka panjang memicu iritasi mukosa, kerusakan fungsi hepar dan ginjal, hingga karsinoma nasofaring.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Realitas di Pasar Tradisional:", "Survei BPOM RI masih kerap mendeteksi residu formalin pada sampel pangan olahan daging basah.", pt_size=11, space_after=6)

    # Card Kanan: Limitasi Metode Eksisting
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Keterbatasan Metode Pengujian Eksisting", "LIMITASI ANALITIK KONVENSIONAL")
    builder.add_bullet_item(tf2, "Uji Laboratorium (HPLC / GC-MS):", "Sangat akurat, namun destruktif, biaya operasional tinggi, membutuhkan tenaga ahli, dan tidak dapat digunakan untuk inspeksi lapangan.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "Test Kit Kolorimetri Kimiawi:", "Cepat dan portabel, tetapi bersifat semi-kuantitatif, sensitivitas rendah, dan rawan salah interpretasi akibat degradasi warna reagen.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "Kebutuhan Nyata:", "Dibutuhkan sistem instrumentasi baru yang cepat, portabel, non-destruktif, memiliki sensitivitas tinggi, serta mampu mengukur konsentrasi secara kuantitatif.", pt_size=11, space_after=6)

    # Highlight Banner Bawah
    hb_left, hb_top, hb_w, hb_h = Inches(0.8), Inches(5.55), Inches(11.733), Inches(1.15)
    builder.add_card(slide, hb_left, hb_top, hb_w, hb_h, bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb_h = slide.shapes.add_textbox(hb_left + Inches(0.3), hb_top + Inches(0.18), hb_w - Inches(0.6), hb_h - Inches(0.36))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    tf_h.margin_left = tf_h.margin_top = tf_h.margin_right = tf_h.margin_bottom = 0

    p_hb_title = tf_h.paragraphs[0]
    p_hb_title.text = "SOLUSI YANG DIAJUKAN:"
    p_hb_title.font.name = FONT_FAMILY
    p_hb_title.font.size = Pt(10)
    p_hb_title.font.bold = True
    p_hb_title.font.color.rgb = COLOR_BLUE_ACCENT
    p_hb_title.space_after = Pt(2)

    p_hb_text = tf_h.add_paragraph()
    p_hb_text.text = "Pengembangan biosensor magnetik berbasis Tunneling Magnetoresistance (TMR) dengan membran nanofiber Fe3O4/PVA-Sitrat-ADH sebagai transduser spesifik yang terintegrasi pengondisi sinyal presisi dan pembelajaran mesin."
    p_hb_text.font.name = FONT_FAMILY
    p_hb_text.font.size = Pt(11)
    p_hb_text.font.bold = True
    p_hb_text.font.color.rgb = COLOR_NAVY_DARK

    builder.add_footer(slide, 3, "Referensi: IARC Formaldehyde Monograph (2012); BPOM RI Laporan Tahunan (2024); Widyasari et al. (2022).")


def build_slide_4(builder):
    """Slide 4: Latar Belakang II"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Latar Belakang II: Prinsip Sensor TMR & Nanofiber Magnetik", "Sinergi efek spintronika magnetoresistif dengan nanomaterial fungsional")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)
    
    # Card Kiri: Sensor TMR
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Keunggulan Sensor TMR ALT023-10E", "TEKNOLOGI SENSOR TRANSDUSER")
    builder.add_bullet_item(tf1, "Efek Tunneling Magnetoresistance:", "Transpor elektron terpolarisasi spin menembus penghalang isolator tipis pada Magnetic Tunnel Junction (MTJ).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Rasio MR & Sensitivitas Tinggi:", "TMR mencapai > 100%, menghasilkan sensitivitas medan hingga 11–18 mV/V/mT, melampaui sensor Hall dan GMR konvensional.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Rentang Linier Medan Rendah:", "Sensor ALT023-10E memiliki rentang linier saturasi ±1.0 mT, sangat ideal untuk mendeteksi perubahan medan magnet mikro dari analit.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Stabilitas & Konsumsi Daya Rendah:", "Menggunakan konfigurasi jembatan Wheatstone penuh (~20 kΩ) dengan kompensasi termal otomatis.", pt_size=11, space_after=8)

    # Card Kanan: Nanofiber Fe3O4/PVA-Sitrat-ADH
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Fungsionalisasi Nanofiber Komposit", "MEMBRAN PENANGKAP ANALIT")
    builder.add_bullet_item(tf2, "Matriks Nanofiber Elektrospinning:", "PVA dan asam sitrat membentuk jaringan serat berpori dengan luas permukaan spesifik tinggi (> 50 m²/g).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Nanopartikel Superparamagnetik Fe3O4:", "Terdistribusi seragam di dalam serat; memiliki momen magnetik tinggi tanpa histeresis permanen pada B=0.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Reseptor Adipic Dihydrazide (ADH):", "Gugus hidrazida (-NH-NH2) pada ADH berikatan kovalen spesifik dengan gugus aldehida (-CHO) formalin membentuk ikatan hidrazon.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Mekanisme Transduksi:", "Pengikatan formalin memicu perubahan permeabilitas lokal dan momen dipol magnetik Fe3O4 yang terbaca langsung sebagai pergeseran tegangan TMR.", pt_size=11, space_after=8)

    builder.add_footer(slide, 4)


def build_slide_5(builder):
    """Slide 5: Latar Belakang III"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Latar Belakang III: Peluang Machine Learning (SVM vs QSVC)", "Pengenalan pola sinyal sensorik dari pembelajaran mesin klasik hingga komputasi kuantum")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: SVM Klasik
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Support Vector Machine (SVM)", "BENCHMARK PEMBELAJARAN MESIN KLASIK")
    builder.add_bullet_item(tf1, "Prinsip Dasar:", "Menemukan bidang pemisah (hyperplane) optimal yang memaksimalkan jarak margin antar-kelas data.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Kernel Radial Basis Function (RBF):", "Mampu memetakan relasi non-linear fitur sinyal sensor ke ruang dimensi lebih tinggi secara matematis terbukti.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Keunggulan:", "Cepat dalam proses pelatihan, stabil pada dataset ukuran terbatas, dan memiliki beban komputasi rendah.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Limitasi Tantangan:", "Dapat mengalami degradasi separabilitas ketika fitur sinyal pada konsentrasi mikro saling bertumpuk (overlapping noise).", pt_size=11, space_after=8)

    # Card Kanan: QSVC Kuantum
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Quantum Support Vector Classifier (QSVC)", "PARADIGMA PEMBELAJARAN MESIN KUANTUM", COLOR_EMERALD)
    builder.add_bullet_item(tf2, "Pemetaan Ruang Hilbert:", "Memetakan data masukan ke keadaan kuantum |Phi(x)> berdimensi eksponensial (2^n) menggunakan sirkuit ZZFeatureMap.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Entanglement & Kuantum Kernel:", "Kernel kuantum K(xi, xj) = |<Phi(xi)|Phi(xj)>|^2 mengeksploitasi korelasi fitur yang tidak terjangkau fungsi kernel klasik.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Potensi Keunggulan Kuantum:", "Mampu memisahkan klaster konsentrasi analit rendah dengan margin keputusan yang lebih tegas dan tahan terhadap dispersi data.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Urgensi Komparasi:", "Memberikan tolok ukur komparatif empiris antara algoritma klasik dan kuantum pada data sensor fisik riil.", pt_size=11, space_after=8)

    builder.add_footer(slide, 5)


def build_slide_6(builder):
    """Slide 6: Rumusan Masalah"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Rumusan Masalah Penelitian", "Empat fokus pertanyaan ilmiah terukur yang menjadi landasan pelaksanaan tugas akhir")

    cards = [
        ("01. RANCANG BANGUN INSTRUMENTASI", [
            ("Pertanyaan Fokus:", "Bagaimana merancang dan merealisasikan rantai instrumentasi sensor TMR ALT023-10E dengan in-amp AD623 (Vref=2.50V) dan ADC ADS1115 16-bit yang stabil dan minim noise?")
        ]),
        ("02. SINTESIS & FUNGSIONALISASI NANOFIBER", [
            ("Pertanyaan Fokus:", "Bagaimana pengaruh fungsionalisasi nanofiber Fe3O4/PVA-Sitrat-ADH terhadap respons modulasi medan magnetik yang terdeteksi oleh sensor TMR?")
        ]),
        ("03. KARAKTERISASI RESPON FORMALIN", [
            ("Pertanyaan Fokus:", "Bagaimana sensitivitas, batas deteksi (LOD), waktu respons, dan kurva tegangan sensor TMR terhadap variasi konsentrasi formalin pada bakso (0–1000 ppm)?")
        ]),
        ("04. KOMPARASI MODEL SVM VS QSVC", [
            ("Pertanyaan Fokus:", "Bagaimana komparasi performa akurasi, presisi, recall, F1-score, dan efisiensi waktu komputasi antara model SVM klasik dan QSVC kuantum dalam klasifikasi konsentrasi formalin?")
        ])
    ]

    coords = [
        (Inches(0.8), Inches(1.65)),
        (Inches(6.8), Inches(1.65)),
        (Inches(0.8), Inches(4.3)),
        (Inches(6.8), Inches(4.3))
    ]

    for (cat, items), (c_left, c_top) in zip(cards, coords):
        builder.add_card(slide, c_left, c_top, Inches(5.733), Inches(2.45))
        tb = slide.shapes.add_textbox(c_left + Inches(0.3), c_top + Inches(0.2), Inches(5.133), Inches(2.05))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        builder.add_card_header(tf, cat, "RUMUSAN MASALAH")
        for b_prefix, b_text in items:
            builder.add_bullet_item(tf, b_prefix, b_text, pt_size=11.5, space_after=4)

    builder.add_footer(slide, 6)


def build_slide_7(builder):
    """Slide 7: Batasan Masalah & Asumsi"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Batasan Masalah & Asumsi Kerja", "Ruang lingkup operasional, parameter perangkat keras, dan batasan komputasi sistem")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Batasan Hardware & Sensor
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Batasan Perangkat Keras & Rantai Sinyal", "SPESIFIKASI ELEKTRIK & MEKANIK")
    builder.add_bullet_item(tf1, "Sensor Magnetik:", "Menggunakan TMR ALT023-10E pada rentang linier saturasi ±1.0 mT.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Pengkondisi Sinyal AD623:", "Catu daya tunggal +5.0 V dengan pin REF terkunci pada VREF = 2.50 V menggunakan pembagi tegangan resistor presisi R3=R4=1.0 kΩ.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "ADC ADS1115 16-Bit:", "Beroperasi pada penguatan internal GAIN_TWOTHIRDS (FSR ±6.144 V) dengan resolusi 0.1875 mV/count.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Kumparan Helmholtz:", "Catu daya DC 0.0–16.0 V (arus maks ~1.6 A, medan 0–11.5 mT, sapuan karakterisasi ±4.0 mT) diatur secara eksternal manual.", pt_size=11, space_after=8)

    # Card Kanan: Batasan Sampel & Model
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Batasan Sampel Kimia & Komputasi", "ANALIT PANGAN & SIMULATOR ML")
    builder.add_bullet_item(tf2, "Komposisi Nanofiber:", "PVA 10% wt, asam sitrat 5% wt, nanopartikel Fe3O4 3% wt, difungsionalisasi dengan Adipic Dihydrazide (ADH).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Sampel Analit Bakso:", "Bakso daging sapi segar pasar tradisional yang di-spiking larutan formalin pada 6 tingkat konsentrasi: 0, 10, 50, 100, 500, dan 1000 ppm.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Metode Akuisisi:", "Berbasis Durasi Waktu ('Lama Detik', default 5.0 s) dengan pembuangan waktu stabilisasi awal 1.0 s.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Komputasi Kuantum:", "Model QSVC disimulasikan menggunakan sirkuit kuantum statevector pada framework IBM Qiskit (4-qubit feature map).", pt_size=11, space_after=8)

    builder.add_footer(slide, 7)


def build_slide_8(builder):
    """Slide 8: Tujuan Penelitian"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Tujuan Penelitian", "Target capaian terukur yang berkorespondensi 1:1 dengan rumusan masalah")

    cards = [
        ("TUJUAN 1 (HARDWARE & INSTRUMENTASI)", [
            ("Target Capaian:", "Merancang, memfabrikasi, dan menguji rantai instrumentasi sensor TMR ALT023-10E dengan penguat in-amp AD623 (Vref=2.50V) dan ADC ADS1115 16-bit berbasis mikrokontroler.")
        ]),
        ("TUJUAN 2 (SINTESIS & FUNGSIONALISASI)", [
            ("Target Capaian:", "Mensintesis membran nanofiber komposit Fe3O4/PVA-Sitrat-ADH melalui teknik electrospinning dan menganalisis pengaruh fungsionalisasinya terhadap respons medan magnetik.")
        ]),
        ("TUJUAN 3 (PENGUJIAN & KARAKTERISASI)", [
            ("Target Capaian:", "Mengkarakterisasi sensitivitas (S = dV/dB), limit deteksi, kurva respons transien, dan stabilitas elektrik sensor TMR terhadap sampel bakso berformalin (0–1000 ppm).")
        ]),
        ("TUJUAN 4 (PEMODELAN ML & KOMPARASI)", [
            ("Target Capaian:", "Mengembangkan dan membandingkan performa akurasi, presisi, recall, F1-score, serta efisiensi waktu komputasi antara model SVM klasik dan QSVC kuantum.")
        ])
    ]

    coords = [
        (Inches(0.8), Inches(1.65)),
        (Inches(6.8), Inches(1.65)),
        (Inches(0.8), Inches(4.3)),
        (Inches(6.8), Inches(4.3))
    ]

    for (cat, items), (c_left, c_top) in zip(cards, coords):
        builder.add_card(slide, c_left, c_top, Inches(5.733), Inches(2.45))
        tb = slide.shapes.add_textbox(c_left + Inches(0.3), c_top + Inches(0.2), Inches(5.133), Inches(2.05))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        builder.add_card_header(tf, cat, "KORESPONDENSI 1:1", COLOR_EMERALD)
        for b_prefix, b_text in items:
            builder.add_bullet_item(tf, b_prefix, b_text, pt_size=11.5, space_after=4)

    builder.add_footer(slide, 8)


def build_slide_9(builder):
    """Slide 9: Manfaat Penelitian"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab I: Pendahuluan", "Manfaat Penelitian", "Kontribusi terhadap perkembangan ilmu fisika instrumentasi dan aplikasi perlindungan pangan")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Manfaat Teoretis
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Manfaat Teoretis & Akademis", "KONTRIBUSI ILMIAH FISIKA")
    builder.add_bullet_item(tf1, "Pengembangan Fisika Instrumentasi:", "Memperkaya kajian integrasi transduser spintronika magnetoresistif dengan nanomaterial fungsional cerdas.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Penerapan Quantum Machine Learning:", "Menyajikan data empiris performa model kuantum (QSVC) dalam mengklasifikasikan sinyal sensor fisik riil.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Penguatan Literatur Nanomaterial:", "Menjadi rujukan ilmiah mengenai rekayasa electrospinning membran PVA-Sitrat-ADH sebagai matriks biosensor.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Target Publikasi Ilmiah:", "Menghasilkan publikasi artikel ilmiah pada jurnal nasional terakreditasi SINTA atau prosiding internasional bereputasi.", pt_size=11, space_after=8)

    # Card Kanan: Manfaat Praktis
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Manfaat Praktis & Aplikatif", "DAMPAK SOSIAL & INDUSTRI", COLOR_EMERALD)
    builder.add_bullet_item(tf2, "Inspeksi Cepat di Lapangan:", "Menghadirkan alternatif instrumen portabel berbiaya terjangkau untuk deteksi formalin pada pasar tradisional.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Dukungan bagi Instansi Pengawas:", "Membantu instansi terkait (BPOM & Dinas Kesehatan) dalam pengawasan mutu pangan secara cepat sebelum uji lab mahal.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Keamanan Konsumen:", "Memberikan kontribusi nyata dalam menekan peredaran makanan berbahaya dan melindungi kesehatan masyarakat.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Potensi Hilirisasi Teknologi:", "Membuka peluang pengembangan prototipe biosensor pangan komersial karya mahasiswa fisika Indonesia.", pt_size=11, space_after=8)

    builder.add_footer(slide, 9)


def build_slide_10(builder):
    """Slide 10: Landasan Teori I (TMR)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab II: Tinjauan Pustaka", "Landasan Teori I: Sensor TMR ALT023-10E & Tunneling Magnetoresistance", "Mekanisme fisika Magnetic Tunnel Junction (MTJ) dan model matematis Julliere")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.2), Inches(5.05)

    # Kolom Kiri: Teori & Formula
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Prinsip Fisika Magnetic Tunnel Junction", "SPINTRONIKA KUANTUM")
    builder.add_bullet_item(tf1, "Fenomena TMR:", "Dua lapisan feromagnetik dipisahkan lapisan isolator nanometer (MgO/Al2O3). Peluang tunneling elektron bergantung pada kesejajaran spin.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Model Julliere (1975):", "TMR = (RAP - RP) / RP = 2·P1·P2 / (1 - P1·P2), dengan P1 dan P2 adalah polarisasi spin kedua elektroda feromagnetik.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Konfigurasi Bipolar ALT023-10E:", "Mengintegrasikan jembatan Wheatstone 4 elemen MTJ dengan sensitivitas ~11-18 mV/V/mT pada rentang ±1.0 mT.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Resistansi Jembatan:", "Resistansi jembatan nominal ~20 kΩ, menghasilkan konsumsi daya rendah dan disipasi panas minimal.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Struktur MTJ & Sensor ALT023
    img1 = "Gambar/Bab2/babII_TMR_Layer.png"
    img2 = "Gambar/Bab2/babII_ALT023.png"
    builder.add_image_fitted(slide, img1, Inches(7.3), Inches(1.65), Inches(5.2), Inches(2.35), border=True, caption="Gambar 2.1: Struktur Lapisan MTJ dan Orientasi Spin Feromagnetik")
    builder.add_image_fitted(slide, img2, Inches(7.3), Inches(4.35), Inches(5.2), Inches(2.25), border=True, caption="Gambar 2.2: Sensor TMR ALT023-10E (Kemasan SOIC-8 NVE Corp.)")

    builder.add_footer(slide, 10, "Referensi: Julliere (1975); NVE Corporation ALT023-10E Datasheet (2022).")


def build_slide_11(builder):
    """Slide 11: Landasan Teori II (AD623 & ADS1115)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab II: Tinjauan Pustaka", "Landasan Teori II: Rantai Pengkondisi Sinyal AD623 & ADS1115", "Arsitektur penguat instrumentasi single-supply presisi dan ADC 16-bit")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.2), Inches(5.05)

    # Kolom Kiri: Teori Rantai Sinyal
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Spesifikasi Rantai Sinyal Elektrik", "PENGUAT & KONVERTER ANALOG")
    builder.add_bullet_item(tf1, "In-Amp AD623:", "Penguat instrumentasi rail-to-rail beroperasi pada single supply +5.0 V dengan CMRR tinggi (> 90 dB).", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Penguatan (Gain):", "G = 1 + (100 kΩ / RG). Nilai RG disesuaikan untuk menghasilkan penguatan optimal 50x–100x.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Tegangan Referensi VREF = 2.50 V:", "Pin 5 (REF) dihubungkan ke pembagi tegangan resistor presisi R3=R4=1.0 kΩ sehingga Vout(B=0) ≈ 2.50 V.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "ADC ADS1115 16-Bit:", "Komunikasi I2C 100 kHz, GAIN_TWOTHIRDS (FSR ±6.144 V), resolusi 0.1875 mV/count pada mode diferensial A0-A1.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar AD623 Pinout & ADS1115
    img1 = "Gambar/Bab2/babII_AD623_Pinout.png"
    img2 = "Gambar/Bab2/babII_ADS-1115-c.jpg"
    builder.add_image_fitted(slide, img1, Inches(7.3), Inches(1.65), Inches(5.2), Inches(2.35), border=True, caption="Gambar 2.3: Diagram Pinout IC Penguat Instrumentasi AD623")
    builder.add_image_fitted(slide, img2, Inches(7.3), Inches(4.35), Inches(5.2), Inches(2.25), border=True, caption="Gambar 2.4: Modul Konverter Analog-ke-Digital ADS1115 16-Bit")

    builder.add_footer(slide, 11, "Referensi: Analog Devices AD623 Datasheet; Texas Instruments ADS1115 Datasheet.")


def build_slide_12(builder):
    """Slide 12: Landasan Teori III (Nanofiber)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab II: Tinjauan Pustaka", "Landasan Teori III: Nanofiber Fe3O4/PVA-Sitrat-ADH & Interaksi Formalin", "Rekayasa fungsionalisasi gugus hidrazon untuk pengikatan spesifik formaldehida")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Komposisi & Reaksi Kimia
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Interaksi Kimia Pembentukan Hidrazon", "MEKANISME PENGIKATAN ANALIT")
    builder.add_bullet_item(tf1, "PVA & Asam Sitrat:", "Asam sitrat berperan ganda sebagai agen crosslinking esterifikasi gugus -OH PVA (ketahanan air) dan penambat molekul ADH.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Adipic Dihydrazide (ADH):", "Mengandung gugus terminal hidrazida (-NH-NH2) yang sangat reaktif dan selektif terhadap gugus karbonil aldehida.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Persamaan Reaksi Hidrazon:", "R-CHO + H2N-NH-R' ---> R-CH=N-NH-R' + H2O. Terbentuk ikatan kovalen hidrazon stabil yang menempel pada permukaan nanofiber.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Perturbasi Medan Magnetik:", "Pengikatan formalin mengubah momen dipol dielektrik lokal dan memodulasi fluks magnetik Fe3O4 yang ditangkap sensor TMR.", pt_size=11, space_after=8)

    # Card Kanan: Tabel Komposisi Bahan
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Peran Fungsional Masing-Masing Komponen", "KOMPOSISI MATERIAL BIOSENSOR", COLOR_EMERALD)
    builder.add_bullet_item(tf2, "PVA 10% wt:", "Matriks polimer utama pembentuk jalinan nanofiber electrospinning yang fleksibel dan seragam.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Asam Sitrat 5% wt:", "Crosslinker ramah lingkungan (non-glutaraldehida) untuk ketahanan mekanis membran dalam medium cair analit.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Nanopartikel Fe3O4 3% wt:", "Elemen transduser magnetik superparamagnetik berukuran ~12 nm pembawa fluks respons medan.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "ADH (Adipic Dihydrazide):", "Reseptor biokimia spesifik untuk memastikan selektivitas tinggi terhadap formalin dibanding zat pengganggu lain.", pt_size=11, space_after=8)

    builder.add_footer(slide, 12)


def build_slide_13(builder):
    """Slide 13: Landasan Teori IV (SVM vs QSVC)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab II: Tinjauan Pustaka", "Landasan Teori IV: Komparasi Model SVM Klasik vs QSVC Kuantum", "Perbedaan matematis pemetaan ruang fitur kernel klasik dan quantum feature map")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Teori SVM
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Support Vector Machine (SVM)", "MODEL BENCHMARK KLASIK")
    builder.add_bullet_item(tf1, "Formulasi Margin Optimal:", "Memaksimalkan batas pemisah: min (1/2)||w||^2 + C * sum(xi) terhadap kendala margin kelas.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Fungsi Kernel RBF:", "K(x, x') = exp(-gamma * ||x - x'||^2). Memetakan fitur ke ruang dimensi kontinu tak berhingga.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Kelebihan Komputasi:", "Proses optimasi kuadratik konveks yang matang, eksekusi cepat, dan bebas dari isu barrens plateau.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Evaluasi Kinerja:", "Divalidasi menggunakan 5-Fold Stratified Cross Validation dengan metrik F1-score dan ROC-AUC.", pt_size=11, space_after=8)

    # Card Kanan: Teori QSVC
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Quantum Support Vector Classifier", "MODEL BERBASIS SIRKUIT KUANTUM", COLOR_EMERALD)
    builder.add_bullet_item(tf2, "Sirkuit ZZFeatureMap:", "Keadaan kuantum |Phi(x)> dikonstruksi melalui gerbang Hadamard H dan gerbang fasa terbelit exp(i * phi_ij * Zi * Zj).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Quantum Kernel Matrix:", "Elemen matriks kernel dihitung melalui overlap kuantum: K(xi, xj) = |<Phi(xi)|Phi(xj)>|^2.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Kapasitas Representasi Kuantum:", "Menyediakan ruang Hilbert berdimensi 2^4 = 16 untuk memisahkan fitur sensorik yang memiliki korelasi kompleks.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Simulasi Qiskit:", "Dieksekusi menggunakan backend statevector/qasm simulator untuk membandingkan akurasi dan latensi inferensi.", pt_size=11, space_after=8)

    builder.add_footer(slide, 13, "Referensi: Cortes & Vapnik (1995); Havlicek et al. (Nature, 2019).")


def build_slide_14(builder):
    """Slide 14: Metodologi Penelitian"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Metodologi Penelitian: Waktu, Tempat, serta Alat & Bahan", "Jadwal dan rincian peralatan laboratorium instrumentasi dan sintesis kimia")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Waktu & Lokasi
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Waktu & Lokasi Penelitian", "JADWAL & FASILITAS LAB")
    builder.add_bullet_item(tf1, "Waktu Pelaksanaan:", "Semester Genap Tahun Akademik 2025/2026 (Maret – Agustus 2026).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Lab Fisika Instrumentasi UIN SGD:", "Fabrikasi sirkuit PCB, perakitan mekanik 3D kumparan Helmholtz, kalibrasi sensor TMR, dan pengujian akuisisi sinyal elektrik.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Lab Sains Terpadu UIN SGD:", "Sintesis sol-gel, elektrospinning nanofiber, fungsionalisasi ikatan ADH, dan preparasi kimia larutan spiking bakso.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Pusat Komputasi Fisika:", "Pelatihan model komparasi machine learning klasik (SVM) dan simulasi sirkuit kuantum (QSVC Qiskit).", pt_size=11, space_after=8)

    # Card Kanan: Alat & Bahan
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Spesifikasi Alat & Bahan Utama", "INVENTARIS PENELITIAN")
    builder.add_bullet_item(tf2, "Perangkat Sensor & Sinyal:", "Sensor TMR ALT023-10E (NVE Corp.), IC In-Amp AD623, ADC ADS1115 16-Bit, mikrokontroler Arduino Uno R3.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "Perangkat Sumber Medan:", "Kumparan Helmholtz laboratorium (R ≈ 10 Ω), DC Power Supply variabel 0.0–16.0 V, Teslameter Digital presisi.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "Bahan Kimia & Sintesis:", "Polyvinyl Alcohol (PVA MW 89-98 kDa), Asam Sitrat p.a., Nanopartikel Fe3O4 (~12 nm), Adipic Dihydrazide (ADH), Formalin 37% p.a.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "Sampel Uji Pangan:", "Bakso sapi segar dari pasar tradisional teruji bebas pengawet.", pt_size=11, space_after=6)

    builder.add_footer(slide, 14)


def build_slide_15(builder):
    """Slide 15: Flowchart Komprehensif"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Diagram Alir Komprehensif Penelitian", "Tahapan sistematis penelitian dari studi literatur, sintesis, fabrikasi, hingga pemodelan")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.2), Inches(5.05)

    # Kolom Kiri: Rincian 5 Tahapan
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "5 Tahapan Utama Penelitian", "STRUKTUR KERJA RISET")
    builder.add_bullet_item(tf1, "Tahap 1 (Persiapan & Desain):", "Studi literatur, perancangan skematik PCB AD623/ADS1115, dan pemodelan statif 3D kumparan Helmholtz.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Tahap 2 (Sintesis Nanofiber):", "Sol-gel PVA/Fe3O4/Sitrat, electrospinning tegangan tinggi 15 kV, dan fungsionalisasi reseptor ADH.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Tahap 3 (Hardware & Software):", "Fabrikasi PCB rantai sinyal presisi, firmware Arduino, dan GUI Python visualisasi 3D.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Tahap 4 (Karakterisasi & Sampel):", "Kalibrasi Helmholtz, pengujian sensitivitas TMR, dan pengujian analit bakso spiking formalin 0–1000 ppm.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Tahap 5 (Machine Learning):", "Ekstraksi 5 fitur sinyal, pelatihan SVM vs QSVC, evaluasi metrik validasi, dan integrasi GUI.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Diagram Alir Penelitian
    img_flow = "Gambar/Bab3/babIII_DiagramAlirPenelitian.drawio.png"
    builder.add_image_fitted(slide, img_flow, Inches(7.3), Inches(1.65), Inches(5.2), Inches(5.05), border=True, caption="Gambar 3.1: Diagram Alir Komprehensif Penelitian")

    builder.add_footer(slide, 15)


def build_slide_16(builder):
    """Slide 16: Desain Hardware & 3D Box"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Rancang Bangun Perangkat Keras (Hardware & Casing 3D)", "Skematik PCB pengkondisi sinyal presisi dan konstruksi mekanik statif sensor")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.0), Inches(5.05)

    # Kolom Kiri: Deskripsi Hardware
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Integrasi Rantai Sinyal Elektrik", "ARSITEKTUR PERANGKAT KERAS")
    builder.add_bullet_item(tf1, "Sensor TMR ALT023-10E:", "Dicatu tegangan +5.0 V dengan kapasitor decoupling 100 nF untuk meredam noise switching catu daya.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "In-Amp AD623 & VREF = 2.50 V:", "Tegangan diferensial TMR diperkuat dengan gain RG. Pin REF dihubungkan ke pembagi presisi 1.0 kΩ sehingga Vout berpusat di 2.50 V.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "ADC ADS1115 & Bus I2C:", "Membaca sinyal penguat secara diferensial dan mentransmisikan data digital ke Arduino pada 100 kHz.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Statif Non-Magnetik 3D:", "Dicetak menggunakan filament PLA non-magnetik untuk memposisikan sensor tepat di sumbu tengah medan seragam kumparan Helmholtz.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Skematik & Casing 3D
    img1 = "Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png"
    img2 = "Gambar/Bab3/babIII_Desainnnn.png"
    builder.add_image_fitted(slide, img1, Inches(7.1), Inches(1.65), Inches(5.4), Inches(2.35), border=True, caption="Gambar 3.2: Skematik PCB Rantai Sinyal TMR, AD623 & ADS1115")
    builder.add_image_fitted(slide, img2, Inches(7.1), Inches(4.35), Inches(5.4), Inches(2.25), border=True, caption="Gambar 3.3: Desain 3D Casing & Statif Posisi Sensor TMR")

    builder.add_footer(slide, 16)


def build_slide_17(builder):
    """Slide 17: Desain Software (Arduino & Python)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Rancang Bangun Perangkat Lunak (Arduino & Python GUI)", "Firmware akuisisi digital dan antarmuka analitik real-time berbasis CustomTkinter")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.0), Inches(5.05)

    # Kolom Kiri: Deskripsi Software
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Spesifikasi Perangkat Lunak", "FIRMWARE & GUI ANALISIS")
    builder.add_bullet_item(tf1, "Firmware Arduino:", "Mengonfigurasi ADS1115 mode diferensial, menerapkan filter moving average N=10, dan mentransmisikan data serial 115200 baud.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Engine Akuisisi Berbasis Durasi:", "Menggunakan durasi waktu terukur ('Lama Detik', default 5.0 s) dengan eliminasi waktu transien awal (settling time 1.0 s).", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Visualisasi OriginLab 3D Scatter:", "Rendering grafik kurva respons kalibrasi dan pengujian analit bergaya bola 3D OriginLab beresolusi 300 DPI.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Auto-Save Laporan Komprehensif:", "Otomasi ekspor data ke format spreadsheet multi-sheet Excel (.xlsx) dan metadata konstanta regresi JSON.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Flowchart Arduino & Python
    img1 = "Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png"
    img2 = "Gambar/Bab3/babIII_DiagramAlirPython.drawio.png"
    builder.add_image_fitted(slide, img1, Inches(7.1), Inches(1.65), Inches(2.55), Inches(5.05), border=True, caption="Gambar 3.4: Flowchart Arduino")
    builder.add_image_fitted(slide, img2, Inches(9.85), Inches(1.65), Inches(2.65), Inches(5.05), border=True, caption="Gambar 3.5: Flowchart GUI Python")

    builder.add_footer(slide, 17)


def build_slide_18(builder):
    """Slide 18: Sintesis Nanofiber"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Tahap Sintesis Nanofiber Fe3O4/PVA-Sitrat-ADH", "Proses sol-gel, electrospinning tegangan tinggi 15 kV, dan fungsionalisasi reseptor ADH")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.2), Inches(5.05)

    # Kolom Kiri: Parameter Sintesis
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Prosedur Fabrikasi Nanomaterial", "SINTESIS & FUNGSIONALISASI")
    builder.add_bullet_item(tf1, "Preparasi Larutan Sol-Gel:", "PVA 10% wt dilarutkan dalam akuades pada 80°C selama 2 jam. Nanopartikel Fe3O4 3% wt dan asam sitrat 5% wt didispersikan via sonikasi 30 menit.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Parameter Operasi Electrospinning:", "Tegangan tinggi: +15 kV DC; Jarak jarum ke kolektor: 12 cm; Laju alir pompa syringe: 0.5 mL/jam.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Pematangan Crosslinking:", "Membran nanofiber dipanaskan pada 120°C selama 1 jam untuk menyempurnakan esterifikasi asam sitrat.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Imobilisasi Reseptor ADH:", "Membran direndam dalam larutan Adipic Dihydrazide dengan aktivator EDC/NHS agar gugus hidrazida tertambat kokoh pada serat.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Diagram Alir Sintesis
    img_sintesis = "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png"
    builder.add_image_fitted(slide, img_sintesis, Inches(7.3), Inches(1.65), Inches(5.2), Inches(5.05), border=True, caption="Gambar 3.6: Diagram Alir Sintesis & Fungsionalisasi Nanofiber")

    builder.add_footer(slide, 18)


def build_slide_19(builder):
    """Slide 19: Karakterisasi Helmholtz & TMR"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Karakterisasi Kumparan Helmholtz & Kalibrasi Sensor TMR", "Pemetaan homogenitas medan magnetik dan kurva kalibrasi sensitivitas tegangan")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Kumparan Helmholtz
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Karakterisasi Kumparan Helmholtz", "SUMBER MEDAN MAGNETIK TERKONTROL")
    builder.add_bullet_item(tf1, "Persamaan Medan Magnetik Pusat:", "B = (4/5)^(3/2) * (mu0 * N * I / R). Memberikan medan magnet seragam pada rongga pusat kumparan.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Catu Daya Variabel 0–16 V:", "Arus DC dialirkan dari 0 hingga ~1.6 A pada kumparan R ≈ 10 Ω, menghasilkan rentang medan hingga 11.5 mT.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Sapuan Medan Karakterisasi:", "Rentang sapuan -4.0 mT hingga +4.0 mT dengan membalik polaritas terminal kumparan.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Validasi Ground Truth:", "Medan diverifikasi langsung menggunakan teslameter digital presisi laboratorium.", pt_size=11, space_after=8)

    # Card Kanan: Kalibrasi TMR
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Kalibrasi Sensitivitas Sensor TMR", "KARAKTERISTIK SENSOR ALT023", COLOR_EMERALD)
    builder.add_bullet_item(tf2, "Model Respon Linear:", "Vout(B) = S * B + Voffset. Nilai kemiringan S merepresentasikan sensitivitas sensor (target S >= 15.0 mV/mT).", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Koefisien Determinasi:", "Target linearitas R^2 >= 0.995 pada rentang linear sensor.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Penetapan Voffset:", "Pada B = 0, tegangan keluaran bertengger stabil di Voffset ≈ 2.50 V sesuai tegangan referensi AD623.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf2, "Penyimpanan Konstanta Kalibrasi:", "Parameter S dan Voffset disimpan otomatis ke file JSON konfigurasi untuk konversi instan pada pengujian analit.", pt_size=11, space_after=8)

    builder.add_footer(slide, 19)


def build_slide_20(builder):
    """Slide 20: Preparasi Sampel & Ekstraksi Fitur"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Protokol Preparasi Sampel Bakso & Ekstraksi Fitur Sinyal", "Standardisasi pengujian analit dan ekstraksi 5 parameter fitur dinamis sensor")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Preparasi Sampel
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Preparasi Sampel Bakso & Spiking", "STANDARISASI PENGUJIAN ANALIT")
    builder.add_bullet_item(tf1, "Homogenisasi Sampel Bakso:", "Bakso sapi bebas formalin dihaluskan dan diekstraksi filtratnya menggunakan akuades steril.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Variasi Konsentrasi Spiking:", "Dibuat 6 tingkat konsentrasi formalin: 0 ppm (kontrol murni), 10 ppm, 50 ppm, 100 ppm, 500 ppm, dan 1000 ppm.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Volume Penetesan Mikro:", "Sebanyak 20 mikroliter larutan analit diteteskan secara presisi menggunakan mikropipet di atas membran nanofiber sensor.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Replikasi Pengujian:", "Setiap tingkat konsentrasi diuji sebanyak minimal 10 kali pengulangan untuk menjamin signifikansi statistik.", pt_size=11, space_after=8)

    # Card Kanan: Ekstraksi 5 Fitur Sinyal
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Ekstraksi 5 Fitur Sinyal Respons", "REPRESENTASI FITUR DINAMIS", COLOR_BLUE_ACCENT)
    builder.add_bullet_item(tf2, "1. Delta_V_max:", "Pergeseran tegangan maksimum antara baseline awal dan puncak respons: |Vpeak - Vbaseline|.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "2. t_response:", "Waktu yang dibutuhkan kurva respons untuk mencapai 90% dari nilai saturasi tegangan.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "3. (dV/dt)_initial:", "Kemiringan laju transien awal interaksi kinetika antara analit formalin dengan reseptor ADH.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "4. V_steady:", "Nilai tegangan kesetimbangan pada kondisi akhir pengukuran.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf2, "5. AUC (Area Under Curve):", "Integral total luasan di bawah kurva respons tegangan terhadap waktu pengujian.", pt_size=11, space_after=6)

    builder.add_footer(slide, 20)


def build_slide_21(builder):
    """Slide 21: Alur Pemodelan ML (SVM vs QSVC)"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Alur Pemodelan Machine Learning (SVM vs QSVC) & Validasi", "Pipeline prapemrosesan data, pelatihan model klasik & kuantum, serta metrik evaluasi")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.0), Inches(5.05)

    # Kolom Kiri: Pipeline ML
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Pipeline Pelatihan & Evaluasi Model", "KLASIK VS KUANTUM")
    builder.add_bullet_item(tf1, "Prapemrosesan Data:", "Standarisasi skala data menggunakan StandardScaler (mean=0, std=1) untuk menjaga netralitas kontribusi fitur.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Pembagian Dataset:", "80% data latih (training set) dan 20% data uji (test set) dengan skema 5-Fold Stratified Cross Validation.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Pelatihan SVM Klasik:", "Kernel RBF dioptimasi melalui GridSearchCV untuk menentukan parameter C dan gamma terbaik.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Pelatihan QSVC Kuantum:", "Sirkuit ZZFeatureMap 4-qubit pada Qiskit Aer untuk komputasi matriks quantum kernel.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Metrik Evaluasi:", "Komparasi menyeluruh mencakup Akurasi, Presisi, Recall, F1-Score, kurva ROC-AUC, dan waktu inferensi.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Diagram Alir Model Building
    img_mb = "Gambar/Bab3/babIII_ModelBuilding.drawio.png"
    builder.add_image_fitted(slide, img_mb, Inches(7.1), Inches(1.65), Inches(5.4), Inches(5.05), border=True, caption="Gambar 3.7: Diagram Alir Pelatihan & Evaluasi Model SVM vs QSVC")

    builder.add_footer(slide, 21)


def build_slide_22(builder):
    """Slide 22: Integrasi & Deploy Sistem"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Integrasi & Deploy Sistem Instrumentasi", "Implementasi model terlatih ke dalam GUI antarmuka untuk klasifikasi real-time")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(6.0), Inches(5.05)

    # Kolom Kiri: Deskripsi Integrasi
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Arsitektur Integrasi Sistem Cerdas", "DEKSTOP GUI DEPLOYMENT")
    builder.add_bullet_item(tf1, "Serialisasi Model Terlatih:", "Model klasifikasi terbaik diekspor ke berkas biner (joblib / qpy) untuk diakses langsung oleh GUI Python.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Pipeline Inferensi Real-Time:", "Saat pengujian sampel selesai (5.0 detik), GUI mengekstrak 5 fitur secara otomatis dan memasukkannya ke model.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Indikator Visual Cepat:", "Tampilan status instan pada layar: 'SAMPEL AMAN (Bebas Formalin)' atau 'TERKONTAMINASI FORMALIN (Estimasi X ppm)'.", pt_size=11, space_after=6)
    builder.add_bullet_item(tf1, "Penyimpanan Data Terpusat:", "Semua riwayat pengujian, nilai fitur, dan grafik respons tersimpan otomatis ke berkas Excel dan database lokal.", pt_size=11, space_after=6)

    # Kolom Kanan: Gambar Deploy & Foto Alat
    img1 = "Gambar/Bab3/babIII_ModelDeploy.drawio.png"
    img2 = "Gambar/Bab3/babIII_desainluar.jpg"
    builder.add_image_fitted(slide, img1, Inches(7.1), Inches(1.65), Inches(2.6), Inches(5.05), border=True, caption="Gambar 3.8: Alur Deploy Model")
    builder.add_image_fitted(slide, img2, Inches(9.9), Inches(1.65), Inches(2.6), Inches(5.05), border=True, caption="Gambar 3.9: Fisik Prototipe Alat")

    builder.add_footer(slide, 22)


def build_slide_23(builder):
    """Slide 23: Jadwal & Roadmap 6 Bulan"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Bab III: Metode Penelitian", "Jadwal & Rencana Kerja Penelitian (Roadmap 6 Bulan)", "Rencana kerja sistematis pelaksanaan tugas akhir Semester Genap 2026")

    # Grid 6 Kartu Bulan (2 Baris x 3 Kolom)
    months = [
        ("BULAN 1 (MARET 2026)", "Persiapan & Pengadaan Komponen", [
            ("Studi Pustaka:", "Kajian mendalam TMR, AD623 & Qiskit."),
            ("Pengadaan Komponen:", "Sensor ALT023, ADS1115 & reagen."),
            ("Desain Awal:", "Skematik PCB & statif kumparan.")
        ]),
        ("BULAN 2 (APRIL 2026)", "Fabrikasi Hardware & Software", [
            ("Fabrikasi Sirkuit:", "Perakitan PCB pengondisi sinyal."),
            ("Pencetakan 3D:", "Casing PLA dan statif sensor."),
            ("Firmware & GUI:", "Pemrograman Arduino & antarmuka Python.")
        ]),
        ("BULAN 3 (MEI 2026)", "Sintesis Nanofiber Fungsional", [
            ("Sol-Gel:", "Pencampuran PVA, Fe3O4 & asam sitrat."),
            ("Electrospinning:", "Penarikan serat tegangan tinggi 15 kV."),
            ("Fungsionalisasi:", "Imobilisasi reseptor ADH pada serat.")
        ]),
        ("BULAN 4 (JUNI 2026)", "Kalibrasi Sensor & Helmholtz", [
            ("Karakterisasi Helmholtz:", "Pemetaan medan magnet 0–11.5 mT."),
            ("Kalibrasi TMR:", "Pengujian sensitivitas (target S >= 15 mV/mT)."),
            ("Validasi Sistem:", "Uji stabilitas & noise rantai sinyal.")
        ]),
        ("BULAN 5 (JULI 2026)", "Pengujian Sampel Bakso Formalin", [
            ("Preparasi Analit:", "Spiking formalin bakso (0–1000 ppm)."),
            ("Akuisisi Data:", "Perekaman respons tegangan sensor TMR."),
            ("Ekstraksi Fitur:", "Ekstraksi 5 parameter fitur sinyal.")
        ]),
        ("BULAN 6 (AGUSTUS 2026)", "Pemodelan ML, Evaluasi & Laporan", [
            ("Pelatihan Model:", "Optimasi SVM vs simulasi QSVC Qiskit."),
            ("Komparasi Metrik:", "Analisis akurasi, presisi & waktu."),
            ("Penyusunan Skripsi:", "Penulisan laporan akhir & publikasi.")
        ])
    ]

    col_w = Inches(3.75)
    row_h = Inches(2.45)
    col_lefts = [Inches(0.8), Inches(4.783), Inches(8.766)]
    row_tops = [Inches(1.65), Inches(4.3)]

    for idx, (cat, title, items) in enumerate(months):
        r = idx // 3
        c = idx % 3
        c_left = col_lefts[c]
        c_top = row_tops[r]

        builder.add_card(slide, c_left, c_top, col_w, row_h)
        tb = slide.shapes.add_textbox(c_left + Inches(0.2), c_top + Inches(0.18), col_w - Inches(0.4), row_h - Inches(0.36))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        builder.add_card_header(tf, title, cat, COLOR_NAVY_MID if idx < 3 else COLOR_EMERALD)
        for b_prefix, b_text in items:
            builder.add_bullet_item(tf, b_prefix, b_text, pt_size=10, space_after=3)

    builder.add_footer(slide, 23)


def build_slide_24(builder):
    """Slide 24: Kesimpulan Sementara & Penutup"""
    slide = builder.add_blank_slide()
    builder.add_header(slide, "Penutup", "Kesimpulan Sementara & Sesi Tanya Jawab", "Komitmen capaian kontribusi penelitian dan permohonan masukan dewan penguji")

    c1_left, c1_top, c_w, c_h = Inches(0.8), Inches(1.65), Inches(5.733), Inches(5.05)

    # Card Kiri: Kesimpulan Target Riset
    builder.add_card(slide, c1_left, c1_top, c_w, c_h)
    tb1 = slide.shapes.add_textbox(c1_left + Inches(0.3), c1_top + Inches(0.25), c_w - Inches(0.6), c_h - Inches(0.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    builder.add_card_header(tf1, "Kesimpulan Sementara Proposal", "KOMITMEN TARGET KONTRIBUSI")
    builder.add_bullet_item(tf1, "Inovasi Biosensor Magnetik:", "Sistem instrumentasi sensor TMR ALT023-10E dengan fungsionalisasi nanofiber Fe3O4/PVA-Sitrat-ADH memberikan pendekatan baru yang sensitif dan selektif untuk deteksi formalin pada pangan.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Rantai Sinyal Stabil & Terkalibrasi:", "Pengondisi in-amp AD623 (Vref=2.50V) dan ADC ADS1115 menjamin resolusi tinggi (0.1875 mV/count) dan stabilitas pengukuran.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Eksplorasi Komparasi Klasik vs Kuantum:", "Perbandingan model SVM dan QSVC membuka wawasan empiris terkait penerapan Quantum Machine Learning pada pengolahan sinyal sensorik fisik.", pt_size=11, space_after=8)
    builder.add_bullet_item(tf1, "Kesiapan Pelaksanaan:", "Seluruh desain skematik, firmware, GUI analitik, dan prosedur sintesis telah siap direalisasikan secara penuh.", pt_size=11, space_after=8)

    # Card Kanan: Sesi Tanya Jawab
    c2_left = Inches(6.8)
    builder.add_card(slide, c2_left, c1_top, c_w, c_h, bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb2 = slide.shapes.add_textbox(c2_left + Inches(0.4), c1_top + Inches(0.35), c_w - Inches(0.8), c_h - Inches(0.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0

    builder.add_card_header(tf2, "Sesi Diskusi & Tanya Jawab", "SEMINAR PROPOSAL SKRIPSI", COLOR_BLUE_ACCENT)

    p_thx = tf2.add_paragraph()
    p_thx.text = "Terima kasih yang sebesar-besarnya kepada Dewan Dosen Penguji dan Dosen Pembimbing atas arahan, bimbingan, dan evaluasi ilmiah yang diberikan."
    p_thx.font.name = FONT_FAMILY
    p_thx.font.size = Pt(11.5)
    p_thx.font.color.rgb = COLOR_TEXT_MAIN
    p_thx.space_before = Pt(8)
    p_thx.space_after = Pt(12)

    p_ask = tf2.add_paragraph()
    p_ask.text = "Kritik, masukan, dan saran yang konstruktif sangat kami harapkan guna penyempurnaan dan keberhasilan pelaksanaan penelitian ini."
    p_ask.font.name = FONT_FAMILY
    p_ask.font.size = Pt(11)
    p_ask.font.color.rgb = COLOR_TEXT_BODY
    p_ask.space_after = Pt(18)

    p_sig = tf2.add_paragraph()
    p_sig.text = "Fahry Rizky Samsudin | NIM 1237030018\nJurusan Fisika — UIN Sunan Gunung Djati Bandung (2026)"
    p_sig.font.name = FONT_FAMILY
    p_sig.font.size = Pt(11)
    p_sig.font.bold = True
    p_sig.font.color.rgb = COLOR_NAVY_DARK

    builder.add_footer(slide, 24, "Seminar Proposal Skripsi Program Studi Fisika UIN Sunan Gunung Djati Bandung")


# ==============================================================================
# MAIN RUNNER
# ==============================================================================
def main():
    print("=" * 70)
    print("MEMULAI GENERASI 24 SLIDE PRESENTASI PROPOSAL SKRIPSI AKADEMIK")
    print("=" * 70)

    builder = AcademicDeckBuilder("Proposal_TA_Fahry_Rizky_Samsudin.pptx")

    builders = [
        build_slide_1,  build_slide_2,  build_slide_3,  build_slide_4,
        build_slide_5,  build_slide_6,  build_slide_7,  build_slide_8,
        build_slide_9,  build_slide_10, build_slide_11, build_slide_12,
        build_slide_13, build_slide_14, build_slide_15, build_slide_16,
        build_slide_17, build_slide_18, build_slide_19, build_slide_20,
        build_slide_21, build_slide_22, build_slide_23, build_slide_24,
    ]

    for i, b_fn in enumerate(builders, start=1):
        print(f"-> Membangun Slide {i} / {TOTAL_SLIDES}...")
        b_fn(builder)

    builder.save()
    print("=" * 70)
    print("SEMUA 24 SLIDE BERHASIL DIBUAT DENGAN SUKSES!")
    print("Berkas: Proposal_TA_Fahry_Rizky_Samsudin.pptx")
    print("=" * 70)

if __name__ == "__main__":
    main()
