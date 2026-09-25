"""
Skrip Generator Presentasi Sidang Proposal Tugas Akhir (30 Slide Lengkap & Komprehensif)
Peneliti : Fahry Rizky Samsudin (NIM: 1237030018)
Jurusan  : Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
Mitra    : Bolabot Techno Robotic Institute Bandung
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
# WARNA & TIPOGRAFI (Anti-Slop Palette: High contrast, academic, purposeful)
# ==============================================================================
COLOR_BG_PAGE     = RGBColor(248, 250, 252) # Slate-50 (#F8FAFC)
COLOR_CARD_FILL   = RGBColor(255, 255, 255) # Pure White (#FFFFFF)
COLOR_CARD_BORDER = RGBColor(226, 232, 240) # Slate-200 (#E2E8F0)
COLOR_TEXT_MAIN   = RGBColor(15, 23, 42)    # Slate-900 (#0F172A)
COLOR_TEXT_BODY   = RGBColor(51, 65, 85)    # Slate-700 (#334155)
COLOR_TEXT_MUTED  = RGBColor(100, 116, 139) # Slate-500 (#64748B)

COLOR_NAVY_DARK   = RGBColor(15, 30, 74)    # Deep Academic Navy (#0F1E4A)
COLOR_NAVY_MID    = RGBColor(30, 58, 138)   # Royal Navy (#1E3A8A)
COLOR_BLUE_ACCENT = RGBColor(37, 99, 235)   # Blue Accent (#2563EB)
COLOR_EMERALD     = RGBColor(5, 150, 105)   # Emerald (#059669)
COLOR_AMBER       = RGBColor(217, 119, 6)   # Amber (#D97706)
COLOR_ROSE        = RGBColor(225, 29, 72)   # Rose (#E11D48)

COLOR_LIGHT_BLUE  = RGBColor(239, 246, 255) # Blue-50 (#EFF6FF)
COLOR_LIGHT_EMR   = RGBColor(236, 253, 245) # Emerald-50 (#ECFDF5)
COLOR_LIGHT_AMB   = RGBColor(255, 251, 235) # Amber-50 (#FFFBEB)
COLOR_LIGHT_SLATE = RGBColor(241, 245, 249) # Slate-100 (#F1F5F9)

FONT_FAMILY = "Segoe UI"
FONT_MATH   = "Georgia"
TOTAL_SLIDES = 30

class AcademicDeckBuilder:
    def __init__(self, filename="Proposal_TA_Fahry_Rizky_Samsudin.pptx"):
        self.filename = filename
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.blank_layout = self.prs.slide_layouts[6]
        self.slide_count = 0

    def add_blank_slide(self):
        slide = self.prs.slides.add_slide(self.blank_layout)
        self.slide_count += 1
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_PAGE
        bg.line.fill.background()
        return slide

    def add_header(self, slide, section_name, title_text, subtitle_text=None):
        b_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10), Inches(0.30))
        tf_b = b_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.text = section_name.upper()
        p_b.font.name = FONT_FAMILY
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_BLUE_ACCENT

        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.733), Inches(0.65))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(17.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY_DARK

        if subtitle_text:
            p_sub = tf_t.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(10.5)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED
            p_sub.space_before = Pt(2)

        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

    def add_footer(self, slide, current_slide, footnote_text=None):
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.02), Inches(11.733), Inches(0.012))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.07), Inches(9.8), Inches(0.3))
        tf_f = f_box.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        if footnote_text:
            p_f.text = footnote_text
            p_f.font.size = Pt(8.5)
            p_f.font.color.rgb = COLOR_TEXT_MUTED
        else:
            p_f.text = "Fahry Rizky Samsudin (1237030018) | Proposal Tugas Akhir Fisika UIN SGD Bandung & Bolabot"
            p_f.font.size = Pt(9.0)
            p_f.font.color.rgb = COLOR_TEXT_MUTED
        p_f.font.name = FONT_FAMILY

        p_box = slide.shapes.add_textbox(Inches(10.8), Inches(7.07), Inches(1.733), Inches(0.3))
        tf_p = p_box.text_frame
        tf_p.word_wrap = True
        tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
        pp = tf_p.paragraphs[0]
        pp.text = f"{current_slide} / {TOTAL_SLIDES}"
        pp.alignment = PP_ALIGN.RIGHT
        pp.font.name = FONT_FAMILY
        pp.font.size = Pt(9.0)
        pp.font.bold = True
        pp.font.color.rgb = COLOR_NAVY_MID

    def add_card(self, slide, left, top, width, height, bg_color=COLOR_CARD_FILL, border_color=COLOR_CARD_BORDER):
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
        p_title.font.size = Pt(11.5)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_NAVY_DARK
        p_title.space_after = Pt(4)

    def add_bullet_item(self, tf, bold_prefix, text, pt_size=10.0, space_after=3.5, color=COLOR_TEXT_BODY):
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

    def add_equation_box(self, slide, left, top, width, height, eq_title, eq_formula, legend_items):
        self.add_card(slide, left, top, width, height, bg_color=COLOR_LIGHT_SLATE, border_color=COLOR_CARD_BORDER)
        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_t = tf.paragraphs[0]
        p_t.text = eq_title.upper()
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(8.5)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_BLUE_ACCENT
        p_t.space_after = Pt(2)

        p_eq = tf.add_paragraph()
        p_eq.text = eq_formula
        p_eq.font.name = FONT_MATH
        p_eq.font.size = Pt(13.5)
        p_eq.font.bold = True
        p_eq.font.color.rgb = COLOR_NAVY_DARK
        p_eq.space_after = Pt(4)

        for var_name, var_desc in legend_items:
            p_leg = tf.add_paragraph()
            p_leg.space_after = Pt(1.5)
            r_v = p_leg.add_run()
            r_v.text = var_name + " : "
            r_v.font.name = FONT_FAMILY
            r_v.font.bold = True
            r_v.font.size = Pt(8.5)
            r_v.font.color.rgb = COLOR_NAVY_MID

            r_d = p_leg.add_run()
            r_d.text = var_desc
            r_d.font.name = FONT_FAMILY
            r_d.font.size = Pt(8.5)
            r_d.font.color.rgb = COLOR_TEXT_BODY

    def add_table(self, slide, left, top, width, height, headers, rows, col_widths=None):
        num_rows = len(rows) + 1
        num_cols = len(headers)
        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        table = table_shape.table

        if col_widths and len(col_widths) == num_cols:
            for idx, w in enumerate(col_widths):
                table.columns[idx].width = w

        for col_idx, header in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_NAVY_MID
            p = cell.text_frame.paragraphs[0]
            p.text = str(header)
            p.font.name = FONT_FAMILY
            p.font.bold = True
            p.font.size = Pt(9.5)
            p.font.color.rgb = COLOR_CARD_FILL
            p.alignment = PP_ALIGN.CENTER

        for row_idx, row_data in enumerate(rows):
            bg = COLOR_LIGHT_SLATE if row_idx % 2 == 1 else COLOR_CARD_FILL
            for col_idx, cell_value in enumerate(row_data):
                cell = table.cell(row_idx + 1, col_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = bg
                p = cell.text_frame.paragraphs[0]
                p.text = str(cell_value)
                p.font.name = FONT_FAMILY
                p.font.size = Pt(9.0)
                p.font.color.rgb = COLOR_TEXT_MAIN
                if col_idx == 0:
                    p.font.bold = True
        return table_shape

    def add_image_fitted(self, slide, img_path, left, top, max_w, max_h, border=True, caption=None):
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
                Inches(final_top + calc_h + 0.04),
                Inches(calc_w + 0.4),
                Inches(0.28)
            )
            tf_c = c_box.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
            pc = tf_c.paragraphs[0]
            pc.text = caption
            pc.alignment = PP_ALIGN.CENTER
            pc.font.name = FONT_FAMILY
            pc.font.size = Pt(8.0)
            pc.font.italic = True
            pc.font.color.rgb = COLOR_TEXT_MUTED

        return pic

    def save(self):
        self.prs.save(self.filename)
        print(f"[SUKSES] Presentasi tersimpan: {self.filename} ({self.slide_count} slides).")

# ==============================================================================
# DEFINISI 30 SLIDE LENGKAP
# ==============================================================================

def build_presentation():
    deck = AcademicDeckBuilder("Proposal_TA_Fahry_Rizky_Samsudin.pptx")

    # --------------------------------------------------------------------------
    # SLIDE 1: COVER
    # --------------------------------------------------------------------------
    s1 = deck.add_blank_slide()
    # Left accent band
    band = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.4), Inches(7.5))
    band.fill.solid()
    band.fill.fore_color.rgb = COLOR_NAVY_MID
    band.line.fill.background()

    # Logo UIN
    deck.add_image_fitted(s1, "Gambar/Logo/Logo UIN.png", Inches(0.8), Inches(0.6), Inches(1.3), Inches(1.3), border=False)

    # Title box
    t_box = s1.shapes.add_textbox(Inches(2.3), Inches(0.6), Inches(10.2), Inches(3.2))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = tf1.margin_right = tf1.margin_bottom = 0

    p_badge = tf1.paragraphs[0]
    p_badge.text = "SEMINAR PROPOSAL TUGAS AKHIR | PROGRAM STUDI FISIKA"
    p_badge.font.name = FONT_FAMILY
    p_badge.font.size = Pt(10)
    p_badge.font.bold = True
    p_badge.font.color.rgb = COLOR_BLUE_ACCENT
    p_badge.space_after = Pt(8)

    p_title = tf1.add_paragraph()
    p_title.text = "RANCANG BANGUN INSTRUMENTASI SENSOR TUNNELING MAGNETORESISTANCE BERBASIS NANOFIBER Fe3O4/PVA-SITRAT-ADH UNTUK DETEKSI FORMALIN PADA BAKSO MENGGUNAKAN KOMPARASI MODEL KLASIK (SVM, RANDOM FOREST) DAN KUANTUM (QSVC, VQC)"
    p_title.font.name = FONT_FAMILY
    p_title.font.size = Pt(17)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY_DARK
    p_title.line_spacing = 1.15
    p_title.space_after = Pt(8)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Integrasi Nanokomposit Magnetik, Rantai Akuisisi Presisi AD623-ADS1115, dan Quantum Machine Learning"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = COLOR_TEXT_MUTED

    # Card Peneliti & Pembimbing
    card1 = deck.add_card(s1, Inches(0.8), Inches(4.1), Inches(5.6), Inches(2.6))
    tb_c1 = s1.shapes.add_textbox(Inches(1.0), Inches(4.25), Inches(5.2), Inches(2.3))
    tfc1 = tb_c1.text_frame
    tfc1.word_wrap = True
    deck.add_card_header(tfc1, "Identitas Peneliti", category_badge="Peneliti Utama", badge_color=COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tfc1, "Nama Lengkap:", "Fahry Rizky Samsudin", pt_size=10)
    deck.add_bullet_item(tfc1, "Nomor Induk (NIM):", "1237030018", pt_size=10)
    deck.add_bullet_item(tfc1, "Program Studi:", "Fisika, Fakultas Sains dan Teknologi", pt_size=10)
    deck.add_bullet_item(tfc1, "Institusi:", "UIN Sunan Gunung Djati Bandung", pt_size=10)

    card2 = deck.add_card(s1, Inches(6.8), Inches(4.1), Inches(5.7), Inches(2.6))
    tb_c2 = s1.shapes.add_textbox(Inches(7.0), Inches(4.25), Inches(5.3), Inches(2.3))
    tfc2 = tb_c2.text_frame
    tfc2.word_wrap = True
    deck.add_card_header(tfc2, "Dewan Pembimbing & Mitra", category_badge="Akademik & Industri", badge_color=COLOR_EMERALD)
    deck.add_bullet_item(tfc2, "Pembimbing I:", "Mada Sanjaya W.S., Ph.D.", pt_size=10)
    deck.add_bullet_item(tfc2, "Pembimbing II:", "Yudha Satya Perkasa, M.T.", pt_size=10)
    deck.add_bullet_item(tfc2, "Mitra Penelitian:", "Bolabot Techno Robotic Institute Bandung", pt_size=10)
    deck.add_bullet_item(tfc2, "Tahun Akademik:", "2026", pt_size=10)

    deck.add_footer(s1, 1, "Proposal Tugas Akhir Fisika UIN Sunan Gunung Djati Bandung")

    # --------------------------------------------------------------------------
    # SLIDE 2: PROFIL MITRA INDUSTRI (BOLABOT TECHNO ROBOTIC INSTITUTE)
    # --------------------------------------------------------------------------
    s2 = deck.add_blank_slide()
    deck.add_header(s2, "Kemitraan Industri", "Profil Mitra Riset: Bolabot Techno Robotic Institute",
                    "Pusat Riset dan Inovasi Robotika, Instrumentasi Medis, dan AI Terapan")
    
    # Left Card: Sejarah & Lokasi
    deck.add_card(s2, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb2_l = s2.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(4.8))
    tf2_l = tb2_l.text_frame
    tf2_l.word_wrap = True
    deck.add_card_header(tf2_l, "Identitas & Legalitas Industri", "Entitas Mitra Riset", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf2_l, "Nama Entitas:", "Bolabot Techno Robotic Institute", pt_size=10.5)
    deck.add_bullet_item(tf2_l, "Pendiri & Direktur:", "Mada Sanjaya W.S., Ph.D. (Berdiri sejak 2010)", pt_size=10.5)
    deck.add_bullet_item(tf2_l, "Lokasi Fasilitas:", "Jl. Sauyunan VI No. 10 Blok F6, Bandung, Jawa Barat", pt_size=10.5)
    deck.add_bullet_item(tf2_l, "Fasilitas Lab:", "Lab Fabrikasi 3D, Lab Sintesis Kimia, Lab Kalibrasi Medan Magnet Helmholtz, Stasiun Komputasi AI", pt_size=10.5)
    deck.add_bullet_item(tf2_l, "Periode Riset:", "September - Desember 2026 (Durasi 4 Bulan Efektif)", pt_size=10.5)

    # Right Card: 4 Pilar Roadmap
    deck.add_card(s2, Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb2_r = s2.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf2_r = tb2_r.text_frame
    tf2_r.word_wrap = True
    deck.add_card_header(tf2_r, "Roadmap Riset Bolabot (4 Pilar Utama)", "Fokus Inovasi Terapan", COLOR_EMERALD)
    deck.add_bullet_item(tf2_r, "Pilar 1: Robotika Edukasi & Otomasi", "Platform edukasi mekatronika dan mikrokontroler nasional.", pt_size=10.0)
    deck.add_bullet_item(tf2_r, "Pilar 2: Robotika Medis & Rehabilitasi", "Pengembangan eksoskeleton dan perangkat bantu terapi medis.", pt_size=10.0)
    deck.add_bullet_item(tf2_r, "Pilar 3: Sensor Biomedis Cerdas", "Rancang bangun instrumen biosensor berbasis nanokomposit magnetik (GMR & TMR) untuk keamanan pangan dan deteksi klinis.", pt_size=10.0)
    deck.add_bullet_item(tf2_r, "Pilar 4: Komputasi AI & Quantum ML", "Integrasi model machine learning klasik dan algoritma kuantum (QSVC) pada sistem tertanam (edge devices).", pt_size=10.0)

    deck.add_footer(s2, 2)

    # --------------------------------------------------------------------------
    # SLIDE 3: SISTEMATIKA PRESENTASI (5 AGENDA UTAMA)
    # --------------------------------------------------------------------------
    s3 = deck.add_blank_slide()
    deck.add_header(s3, "Struktur Presentasi", "Sistematika Paparan Sidang Proposal",
                    "Rangkuman 5 Agenda Pokok Pembahasan Proposal Tugas Akhir")

    agendas = [
        ("01", "BAB I: PENDAHULUAN", "Latar Belakang, 5 Rumusan Masalah, 6 Batasan, 5 Tujuan, Manfaat Riset, dan 4 Metode Pengumpulan Data."),
        ("02", "BAB II: TINJAUAN PUSTAKA", "Fisika TMR Julliere, Reaksi Hidrazon ADH, Kumparan Helmholtz, AD623, ADS1115, Nanofiber Sitrat, SVM & QSVC."),
        ("03", "BAB III: METODE PENELITIAN", "Spesifikasi Alat Bahan, Diagram Alir, Rangkaian Skematik, Casing 3D, Sintesis Nanofiber, Kalibrasi, & Pipeline ML."),
        ("04", "RENCANA KERJA 4 BULAN", "Timeline Gantt Chart pelaksanaan riset di Bolabot (September - Desember 2026) dan alokasi sumber daya."),
        ("05", "TARGET LUARAN & PENUTUP", "Target publikasi prosiding internasional bereputasi / jurnal SINTA 2, prototipe instrumen, dan sesi diskusi.")
    ]

    for i, (num, title, desc) in enumerate(agendas):
        top_pos = Inches(1.55 + i * 1.05)
        deck.add_card(s3, Inches(0.8), top_pos, Inches(11.733), Inches(0.92))
        
        # Num Badge
        nb = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), top_pos + Inches(0.16), Inches(0.75), Inches(0.6))
        nb.fill.solid()
        nb.fill.fore_color.rgb = COLOR_LIGHT_BLUE
        nb.line.color.rgb = COLOR_BLUE_ACCENT
        p_nb = nb.text_frame.paragraphs[0]
        p_nb.text = num
        p_nb.font.name = FONT_FAMILY
        p_nb.font.bold = True
        p_nb.font.size = Pt(13)
        p_nb.font.color.rgb = COLOR_BLUE_ACCENT
        p_nb.alignment = PP_ALIGN.CENTER

        tb = s3.shapes.add_textbox(Inches(1.95), top_pos + Inches(0.12), Inches(10.3), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.bold = True
        p_t.font.size = Pt(11)
        p_t.font.color.rgb = COLOR_NAVY_DARK
        p_t.space_after = Pt(2)

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = COLOR_TEXT_BODY

    deck.add_footer(s3, 3)

    # --------------------------------------------------------------------------
    # SLIDE 4: LATAR BELAKANG I: BAHAYA FORMALIN & LIMITASI KONVENSIONAL
    # --------------------------------------------------------------------------
    s4 = deck.add_blank_slide()
    deck.add_header(s4, "Bab I: Pendahuluan", "Latar Belakang I: Urgensi Deteksi Formalin pada Pangan",
                    "Penyalahgunaan Pengawet Berbahaya dan Limitasi Metode Analisis Saat Ini")

    deck.add_card(s4, Inches(0.8), Inches(1.55), Inches(5.6), Inches(3.6))
    tb4_l = s4.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(3.2))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True
    deck.add_card_header(tf4_l, "Bahaya Formalin pada Produk Bakso", "Urgensi Kesehatan Pangan", COLOR_ROSE)
    deck.add_bullet_item(tf4_l, "Status Regulasi:", "Formalin (formaldehida terlarut) dilarang keras sebagai bahan tambahan pangan (Permenkes RI).", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "Toksisitas Kronis:", "Karsinogenik Golongan 1 (IARC), pemicu iritasi saluran cerna, gagal ginjal, dan kanker nasofaring.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "Temuan Lapangan:", "Studi di Pekanbaru menemukan formalin hingga 4.506 ppm pada bakso jalanan; temuan serupa di Padang dan Yogyakarta.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "Ambang Toleransi:", "Ambang batas asupan harian maksimum EFSA hanya 100 ppm, paparan kumulatif sangat fatal.", pt_size=10.0)

    deck.add_card(s4, Inches(6.8), Inches(1.55), Inches(5.7), Inches(3.6))
    tb4_r = s4.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(3.2))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True
    deck.add_card_header(tf4_r, "Keterbatasan Metode Deteksi Saat Ini", "Gap Analisis Laboratorium", COLOR_AMBER)
    deck.add_bullet_item(tf4_r, "Uji Kimia Kolorimetri (KMnO4):", "Hanya kualitatif, rentan positif palsu oleh senyawa pereduksi alami, destruktif terhadap sampel.", pt_size=10.0)
    deck.add_bullet_item(tf4_r, "Kromatografi (HPLC / GC-MS):", "Sangat akurat namun biaya tinggi, preparasi rumit berjam-jam, membutuhkan teknisi ahli, tidak portabel.", pt_size=10.0)
    deck.add_bullet_item(tf4_r, "Spektrofotometri UV-Vis:", "Memerlukan reagen toksik (asam kromotropat), tidak fleksibel untuk inspeksi cepat di pasar tradisional.", pt_size=10.0)

    # Bottom Full Width Solution Box
    deck.add_card(s4, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.4), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb4_b = s4.shapes.add_textbox(Inches(1.05), Inches(5.45), Inches(11.2), Inches(1.2))
    tf4_b = tb4_b.text_frame
    tf4_b.word_wrap = True
    deck.add_card_header(tf4_b, "Solusi yang Diusulkan pada Penelitian Ini", "Arah Inovasi Instrumentasi", COLOR_BLUE_ACCENT)
    p_sol = tf4_b.add_paragraph()
    p_sol.text = "Pengembangan instrumen biosensor terintegrasi: memanfaatkan efek Tunneling Magnetoresistance (TMR) berbiaya rendah, fungsionalisasi nanofiber selektif ADH, dan kecerdasan komputasi Quantum Machine Learning untuk deteksi cepat, kuantitatif, portabel, dan non-destruktif."
    p_sol.font.name = FONT_FAMILY
    p_sol.font.size = Pt(9.5)
    p_sol.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s4, 4)

    # --------------------------------------------------------------------------
    # SLIDE 5: LATAR BELAKANG II: KEUNGGULAN TMR VS GMR
    # --------------------------------------------------------------------------
    s5 = deck.add_blank_slide()
    deck.add_header(s5, "Bab I: Pendahuluan", "Latar Belakang II: Keunggulan Sensor Tunneling Magnetoresistance (TMR)",
                    "Komparasi Fenomena Spintronika terhadap Sensor GMR dan Hall Effect")

    headers_tmr = ["Parameter Evaluasi", "Efek Hall Konvensional", "Giant Magnetoresistance (GMR)", "Tunneling Magnetoresistance (TMR)"]
    rows_tmr = [
        ["Prinsip Fisika Dasar", "Gaya Lorentz defleksi muatan", "Spin-dependent scattering (logam)", "Spin-dependent quantum tunneling"],
        ["Struktur Lapisan", "Semikonduktor silikon/GaAs", "Ferromagnet / Logam Non-magnetik", "Ferromagnet / Insulator Tipis (MgO)"],
        ["Rasio Magnetoresistansi", "< 1% (Sangat Kecil)", "10% - 20% pada suhu ruang", "> 100% - 200% pada suhu ruang"],
        ["Sensitivitas Medan", "Rendah (0.1 - 10 V/T)", "Menengah (10 - 50 V/T)", "Sangat Tinggi (hingga 6x lipat GMR)"],
        ["Konsumsi Daya", "Menengah (milliwatt)", "Rendah (milliwatt)", "Ultra-rendah (mikrowatt)"],
        ["Platform Terpilih", "-", "AA005-02 (Riset Terdahulu)", "ALT023-10E NVE (Penelitian Ini)"]
    ]
    deck.add_table(s5, Inches(0.8), Inches(1.55), Inches(11.733), Inches(3.4), headers_tmr, rows_tmr,
                   col_widths=[Inches(2.5), Inches(3.0), Inches(3.1), Inches(3.133)])

    # Bottom Insight Card
    deck.add_card(s5, Inches(0.8), Inches(5.15), Inches(11.733), Inches(1.6), bg_color=COLOR_LIGHT_SLATE, border_color=COLOR_CARD_BORDER)
    tb5_b = s5.shapes.add_textbox(Inches(1.05), Inches(5.25), Inches(11.2), Inches(1.4))
    tf5_b = tb5_b.text_frame
    tf5_b.word_wrap = True
    deck.add_card_header(tf5_b, "Landasan Ilmiah Pemilihan Sensor TMR ALT023-10E", "Keunggulan Spintronika", COLOR_NAVY_MID)
    deck.add_bullet_item(tf5_b, "Amplitudo Sinyal Lebih Besar:", "Output tegangan TMR mencapai 6x lipat lebih tinggi dari GMR, mengurangi kebutuhan penguatan bertingkat ekstrim yang rawan derau.", pt_size=9.5)
    deck.add_bullet_item(tf5_b, "Deteksi Medan Mikro:", "Mampu merespons distorsi fluks magnetik skala nano-Tesla hingga milli-Tesla saat molekul formalin terikat pada permukaan reseptor nanofiber.", pt_size=9.5)

    deck.add_footer(s5, 5)

    # --------------------------------------------------------------------------
    # SLIDE 6: LATAR BELAKANG III: INOVASI NANOFIBER SITRAT-ADH
    # --------------------------------------------------------------------------
    s6 = deck.add_blank_slide()
    deck.add_header(s6, "Bab I: Pendahuluan", "Latar Belakang III: Fungsionalisasi Nanofiber Fe3O4/PVA-Sitrat-ADH",
                    "Agen Taut-Silang Non-Toksik dan Gugus Pengenal Formaldehida Selektif")

    headers_adh = ["Parameter Komparasi", "Glutaraldehida (GA) [Riset Umum]", "Adipic Acid Dihydrazide (ADH) [Penelitian Ini]"]
    rows_adh = [
        ["Sifat Toksisitas", "Toksik, uap iritatif kuat, karsinogenik", "Ramah lingkungan, biokompatibel, aman laboratorium"],
        ["Identitas Gugus Fungsi", "Dialdehida (-CHO dan -CHO)", "Dihidrazida (-NH-NH2 dan -NH-NH2)"],
        ["Interaksi dengan Formalin", "Ambiguitas pengenalan (sama-sama aldehida)", "Reaksi spesifik membentuk ikatan hidrazon kovalen"],
        ["Fungsi Kimiawi Utama", "Crosslinker umum non-spesifik", "Formaldehyde scavenger berdaya tangkap tinggi"],
        ["Crosslinker Pendukung", "Tidak ada (mandiri)", "Asam Sitrat Termal 130 C (esterifikasi tahan air)"]
    ]
    deck.add_table(s6, Inches(0.8), Inches(1.55), Inches(7.0), Inches(3.2), headers_adh, rows_adh,
                   col_widths=[Inches(2.2), Inches(2.4), Inches(2.4)])

    # Right Card: Green Nanoparticle Fe3O4
    deck.add_card(s6, Inches(8.0), Inches(1.55), Inches(4.533), Inches(5.2))
    tb6_r = s6.shapes.add_textbox(Inches(8.2), Inches(1.75), Inches(4.1), Inches(4.8))
    tf6_r = tb6_r.text_frame
    tf6_r.word_wrap = True
    deck.add_card_header(tf6_r, "Sintesis Hijau Fe3O4 & Polimer", "Keunggulan Green Nanomaterial", COLOR_EMERALD)
    deck.add_bullet_item(tf6_r, "Ekstrak Daun Kelor:", "Moringa oleifera kaya senyawa polifenol alami sebagai pereduksi ion besi dan capping agent ramah lingkungan.", pt_size=9.5)
    deck.add_bullet_item(tf6_r, "Superparamagnetisme:", "Nanopartikel Fe3O4 berukuran sub-20 nm memiliki suseptibilitas tinggi tanpa histeresis remanen.", pt_size=9.5)
    deck.add_bullet_item(tf6_r, "Matriks PVA 10% wt:", "Membentuk jejaring nanofiber homogen berdiameter puluhan nanometer melalui electrospinning.", pt_size=9.5)
    deck.add_bullet_item(tf6_r, "Taut-Silang Asam Sitrat:", "Curing 130 C selama 1.5 jam mengikat gugus hidroksil PVA menjadi ikatan ester tak larut air.", pt_size=9.5)

    # Bottom Left Card: Hipotesis Mekanisme
    deck.add_card(s6, Inches(0.8), Inches(4.95), Inches(7.0), Inches(1.8), bg_color=COLOR_LIGHT_AMB, border_color=COLOR_AMBER)
    tb6_bl = s6.shapes.add_textbox(Inches(1.0), Inches(5.05), Inches(6.6), Inches(1.6))
    tf6_bl = tb6_bl.text_frame
    tf6_bl.word_wrap = True
    deck.add_card_header(tf6_bl, "Hipotesis Efek Magnetoresistif Gugus ADH", "Mekanisme Transduksi Sensor", COLOR_AMBER)
    p_hip = tf6_bl.add_paragraph()
    p_hip.text = "Pengikatan molekul formaldehida oleh gugus hidrazida terminal ADH memicu transfer muatan lokal dan konformasi rantai polimer, mendistorsi medan fluks magnetik stray Fe3O4 yang terbaca seketika sebagai pergeseran kurva resistansi TMR."
    p_hip.font.name = FONT_FAMILY
    p_hip.font.size = Pt(9.5)
    p_hip.font.color.rgb = COLOR_TEXT_MAIN

    deck.add_footer(s6, 6)

    # --------------------------------------------------------------------------
    # SLIDE 7: LATAR BELAKANG IV: MACHINE LEARNING KLASIK (SVM) VS KUANTUM (QSVC)
    # --------------------------------------------------------------------------
    s7 = deck.add_blank_slide()
    deck.add_header(s7, "Bab I: Pendahuluan", "Latar Belakang IV: Komparasi Model Cerdas SVM vs QSVC",
                    "Eksplorasi Quantum Machine Learning untuk Robustness Klasifikasi Sensor Pangan")

    # Left: SVM Klasik
    deck.add_card(s7, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb7_l = s7.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(4.8))
    tf7_l = tb7_l.text_frame
    tf7_l.word_wrap = True
    deck.add_card_header(tf7_l, "Support Vector Machine (SVM) Klasik", "Metode Klasik Teruji", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf7_l, "Prinsip Kerja:", "Membangun hyperplane optimal dengan memaksimalkan margin pemisah antarkelas pada ruang fitur berdimensi tinggi.", pt_size=10.0)
    deck.add_bullet_item(tf7_l, "Fungsi Kernel:", "Radial Basis Function (RBF) Kernel mentransformasikan data non-linear secara numerik.", pt_size=10.0)
    deck.add_bullet_item(tf7_l, "Keunggulan:", "Komputasi cepat, stabil, tidak mudah overfitting pada ukuran sampel terbatas, implementasi praktis di mikrokomputer.", pt_size=10.0)
    deck.add_bullet_item(tf7_l, "Keterbatasan:", "Rentan degradasi akurasi apabila fitur sinyal memiliki tumpang tindih derau ekstrem atau fluktuasi non-linear tinggi.", pt_size=10.0)

    # Right: QSVC Kuantum
    deck.add_card(s7, Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb7_r = s7.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf7_r = tb7_r.text_frame
    tf7_r.word_wrap = True
    deck.add_card_header(tf7_r, "Quantum Support Vector Classifier (QSVC)", "Inovasi Quantum Machine Learning", COLOR_EMERALD)
    deck.add_bullet_item(tf7_r, "Prinsip Kerja:", "Memetakan vektor fitur sinyal sensor ke ruang Hilbert 2^n qubit melalui gerbang uniter ter-entangle (Quantum Feature Map).", pt_size=10.0)
    deck.add_bullet_item(tf7_r, "Quantum Kernel:", "Menghitung derajat ketumpangtindihan status kuantum (Quantum State Fidelity) antar-sampel pengujian.", pt_size=10.0)
    deck.add_bullet_item(tf7_r, "Potensi Keunggulan:", "Mampu menangkap korelasi non-linear kompleks yang sulit diakses kernel klasik; memiliki resistensi tinggi terhadap derau gaussian.", pt_size=10.0)
    deck.add_bullet_item(tf7_r, "Relevansi:", "Studi komparasi empiris pertama di Indonesia untuk biosensor TMR keamanan pangan.", pt_size=10.0)

    deck.add_footer(s7, 7)

    # --------------------------------------------------------------------------
    # SLIDE 8: RUMUSAN MASALAH (5 BUTIR LENGKAP)
    # --------------------------------------------------------------------------
    s8 = deck.add_blank_slide()
    deck.add_header(s8, "Bab I: Pendahuluan", "Rumusan Masalah Penelitian (5 Butir Spesifik)",
                    "Pertanyaan Ilmiah Kunci yang Menjadi Fokus Investigasi Tugas Akhir")

    rumusan = [
        ("RM-1", "Sensitivitas Sensor TMR terhadap Formalin",
         "Bagaimana sensitivitas sensor Tunneling Magnetoresistance (TMR) yang berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin?"),
        ("RM-2", "Batas Deteksi (Limit of Detection / LOD)",
         "Bagaimana batas deteksi (limit of detection) yang diperoleh dari sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin?"),
        ("RM-3", "Pengaruh Gugus Hidrazida ADH pada Sinyal",
         "Bagaimana gugus hidrazida pada nanofiber Fe3O4/PVA-Sitrat-ADH memengaruhi respons magnetoresistif sensor TMR terhadap keberadaan formalin?"),
        ("RM-4", "Validitas Kurva Kalibrasi Instrumentasi",
         "Bagaimana rancangan sistem instrumentasi (AD623-ADS1115-Arduino-Raspberry Pi) menghasilkan kurva kalibrasi yang valid antara tegangan keluaran sensor dan konsentrasi formalin pada bakso?"),
        ("RM-5", "Komparasi Kinerja Model Klasifikasi SVM vs QSVC",
         "Bagaimana komparasi performa klasifikasi antara model Support Vector Machine (SVM) klasik dan Quantum Support Vector Classifier (QSVC) dalam mendeteksi dan mengklasifikasikan kandungan formalin pada sampel bakso?")
    ]

    for i, (tag, title, desc) in enumerate(rumusan):
        top_pos = Inches(1.55 + i * 1.05)
        deck.add_card(s8, Inches(0.8), top_pos, Inches(11.733), Inches(0.92))
        
        # Tag Badge
        tb_tag = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), top_pos + Inches(0.18), Inches(0.95), Inches(0.55))
        tb_tag.fill.solid()
        tb_tag.fill.fore_color.rgb = COLOR_LIGHT_BLUE
        tb_tag.line.color.rgb = COLOR_BLUE_ACCENT
        p_tag = tb_tag.text_frame.paragraphs[0]
        p_tag.text = tag
        p_tag.font.name = FONT_FAMILY
        p_tag.font.bold = True
        p_tag.font.size = Pt(11)
        p_tag.font.color.rgb = COLOR_BLUE_ACCENT
        p_tag.alignment = PP_ALIGN.CENTER

        tb = s8.shapes.add_textbox(Inches(2.1), top_pos + Inches(0.12), Inches(10.2), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.bold = True
        p_t.font.size = Pt(11)
        p_t.font.color.rgb = COLOR_NAVY_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = COLOR_TEXT_BODY

    deck.add_footer(s8, 8)

    # --------------------------------------------------------------------------
    # SLIDE 9: BATASAN MASALAH (6 BATASAN TEKNIS)
    # --------------------------------------------------------------------------
    s9 = deck.add_blank_slide()
    deck.add_header(s9, "Bab I: Pendahuluan", "Batasan Masalah Penelitian (6 Batasan)",
                    "Ruang Lingkup dan Asumsi Operasional Pengujian Laboratorium")

    batasan_list = [
        ("01", "Spesifisitas Analit", "Penelitian berfokus eksklusif pada deteksi analit formalin (formaldehida terlarut); bahan pengawet/pewarna sintetis lain (boraks, rhodamin B) tidak dianalisis."),
        ("02", "Tahapan Sampel", "Pengujian kurva respons diawali larutan standar formalin bertingkat (mg/L terkontrol) sebelum diterapkan pada supernatan ekstrak sampel bakso riil."),
        ("03", "Formulasi Material", "Material sensor dibatasi pada nanokomposit Fe3O4/PVA hasil elektrospinning dengan taut-silang asam sitrat (curing 130 C) dan fungsionalisasi ADH."),
        ("04", "Status Hipotesis Reseptor", "Mekanisme pengenalan molekul formalin oleh gugus hidrazida ADH diperlakukan sebagai hipotesis yang diuji secara empiris, bukan mekanisme aksioma."),
        ("05", "Parameter Evaluasi Fisik", "Karakterisasi sensor dibatasi pada parameter sensitivitas, batas deteksi (LOD), linearitas, dan kestabilan sinyal; ketahanan mekanik jangka panjang tidak diuji."),
        ("06", "Lingkup Pemodelan Cerdas", "Model kecerdasan buatan dibatasi pada komparasi algoritma klasik SVM (RBF kernel) dan simulasi QSVC berbasis quantum feature map Qiskit.")
    ]

    for i, (num, title, desc) in enumerate(batasan_list):
        row = i // 2
        col = i % 2
        l = Inches(0.8 + col * 6.0)
        t = Inches(1.55 + row * 1.75)
        w = Inches(5.733)
        h = Inches(1.6)

        deck.add_card(s9, l, t, w, h)
        tb = s9.shapes.add_textbox(l + Inches(0.2), t + Inches(0.15), w - Inches(0.4), h - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        deck.add_card_header(tf, f"Batasan {num}: {title}", None, COLOR_BLUE_ACCENT)
        p = tf.add_paragraph()
        p.text = desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.color.rgb = COLOR_TEXT_BODY
        p.line_spacing = 1.15

    deck.add_footer(s9, 9)

    # --------------------------------------------------------------------------
    # SLIDE 10: TUJUAN PENELITIAN (5 BUTIR SINKRON)
    # --------------------------------------------------------------------------
    s10 = deck.add_blank_slide()
    deck.add_header(s10, "Bab I: Pendahuluan", "Tujuan Penelitian (5 Butir Sinkron)",
                    "Target Capaian Ilmiah yang Sinkron 1-ke-1 dengan Rumusan Masalah")

    tujuan = [
        ("T-1", "Evaluasi Sensitivitas Sensor TMR",
         "Mengevaluasi sensitivitas sensor Tunneling Magnetoresistance (TMR) berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi larutan formalin."),
        ("T-2", "Penentuan Batas Deteksi Kuantitatif (LOD)",
         "Menentukan batas deteksi (Limit of Detection / LOD) formalin secara kuantitatif berdasarkan kurva respons sensor dan simpangan baku baseline sinyal."),
        ("T-3", "Investigasi Peran Gugus Hidrazida ADH",
         "Mengevaluasi peran fungsional gugus hidrazida pada nanofiber Fe3O4/PVA-Sitrat-ADH dalam memodulasi respons sinyal magnetoresistif sensor TMR."),
        ("T-4", "Validasi Sistem Instrumentasi & Kalibrasi",
         "Merancang dan memvalidasi rantai instrumentasi (AD623-ADS1115-Arduino-Raspberry Pi) yang menghasilkan kurva kalibrasi presisi antara tegangan sensor dan kadar formalin bakso."),
        ("T-5", "Komparasi Evaluatif Model SVM vs QSVC",
         "Menganalisis dan membandingkan performa akurasi, presisi, recall, F1-score, serta ketahanan derau model SVM klasik versus QSVC kuantum pada klasifikasi keamanan bakso.")
    ]

    for i, (tag, title, desc) in enumerate(tujuan):
        top_pos = Inches(1.55 + i * 1.05)
        deck.add_card(s10, Inches(0.8), top_pos, Inches(11.733), Inches(0.92))
        
        # Tag Badge
        tb_tag = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), top_pos + Inches(0.18), Inches(0.95), Inches(0.55))
        tb_tag.fill.solid()
        tb_tag.fill.fore_color.rgb = COLOR_LIGHT_EMR
        tb_tag.line.color.rgb = COLOR_EMERALD
        p_tag = tb_tag.text_frame.paragraphs[0]
        p_tag.text = tag
        p_tag.font.name = FONT_FAMILY
        p_tag.font.bold = True
        p_tag.font.size = Pt(11)
        p_tag.font.color.rgb = COLOR_EMERALD
        p_tag.alignment = PP_ALIGN.CENTER

        tb = s10.shapes.add_textbox(Inches(2.1), top_pos + Inches(0.12), Inches(10.2), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.bold = True
        p_t.font.size = Pt(11)
        p_t.font.color.rgb = COLOR_NAVY_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = COLOR_TEXT_BODY

    deck.add_footer(s10, 10)

    # --------------------------------------------------------------------------
    # SLIDE 11: MANFAAT PENELITIAN (4 DIMENSI STRATEGIS)
    # --------------------------------------------------------------------------
    s11 = deck.add_blank_slide()
    deck.add_header(s11, "Bab I: Pendahuluan", "Manfaat Penelitian (4 Dimensi Strategis)",
                    "Kontribusi Signifikan bagi Sains, Industri, Pengawasan Pangan, dan IPTEK Nasional")

    manfaat = [
        ("Akademisi & Sains", COLOR_BLUE_ACCENT,
         "Memberikan kajian baru mengenai dinamika antarmuka sensor spintronika TMR dengan reseptor nanokomposit polimer, serta mengevaluasi penerapan Quantum Machine Learning pada pengolahan sinyal biosensor."),
        ("Mitra Industri Bolabot", COLOR_EMERALD,
         "Menyediakan prototipe instrumentasi biosensor cerdas portabel yang teruji secara eksperimental dan siap dihilirisasi ke tahap produksi komersial alat uji pangan cepat."),
        ("Masyarakat & BPOM", COLOR_AMBER,
         "Menghadirkan alternatif instrumen skrining formalin yang cepat, murah, dan akurat di lapangan tanpa merusak produk pangan, melindungi masyarakat dari bahaya karsinogenik."),
        ("Kemandirian IPTEK Nasional", COLOR_NAVY_MID,
         "Mendukung substitusi alat uji impor berbiaya miliaran rupiah dengan instrumentasi berbasis komponen terbuka, sintesis hijau lokal, dan perangkat lunak mandiri.")
    ]

    for i, (title, color, desc) in enumerate(manfaat):
        row = i // 2
        col = i % 2
        l = Inches(0.8 + col * 6.0)
        t = Inches(1.55 + row * 2.65)
        w = Inches(5.733)
        h = Inches(2.45)

        deck.add_card(s11, l, t, w, h)
        tb = s11.shapes.add_textbox(l + Inches(0.25), t + Inches(0.2), w - Inches(0.5), h - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True
        deck.add_card_header(tf, title, f"Pilar Manfaat 0{i+1}", color)
        p = tf.add_paragraph()
        p.text = desc
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10.0)
        p.font.color.rgb = COLOR_TEXT_BODY
        p.line_spacing = 1.2

    deck.add_footer(s11, 11)

    # --------------------------------------------------------------------------
    # SLIDE 12: METODE PENGUMPULAN DATA (4 METODE POKOK)
    # --------------------------------------------------------------------------
    s12 = deck.add_blank_slide()
    deck.add_header(s12, "Bab I: Pendahuluan", "Metode Pengumpulan Data Penelitian",
                    "Tahapan Sistematis Perolehan Data Teoretis, Eksperimental, dan Komputasional")

    metode_data = [
        ("01", "Studi Literatur", "Kajian Jurnal & Teori Dasar",
         "Mengumpulkan data primer dari jurnal bereputasi internasional (IEEE, Elsevier, Springer) mengenai efek TMR, mekanisme reaksi hidrazon formalin-ADH, sintesis nanopartikel Fe3O4 daun kelor, serta kerangka kerja Qiskit QSVC."),
        ("02", "Observasi & Studi Pendahuluan", "Evaluasi Prototipe Terdahulu",
         "Menganalisis keterbatasan prototipe GMR sebelumnya di laboratorium Bolabot untuk menyempurnakan tata letak sirkuit pengkondisi sinyal AD623, peredaman derau ground loop, dan kestabilan dudukan sensor."),
        ("03", "Eksperimen Laboratorium Terstruktur", "Sintesis & Karakterisasi Fisik",
         "Melaksanakan sintesis kopresipitasi Fe3O4, elektrospinning sol PVA-sitrat-ADH (curing 130 C), pemetaan kurva medan Helmholtz (0-16 V), serta akuisisi respons tegangan sensor terhadap larutan formalin bertingkat."),
        ("04", "Analisis Data & Pemodelan Cerdas", "Ekstraksi Fitur & Machine Learning",
         "Melakukan pra-pemrosesan sinyal sensor, pembentukan kurva kalibrasi regresi dV/dB, ekstraksi 5 fitur dinamis sampel bakso, serta validasi silang (5-fold cross validation) model komparasi SVM dan QSVC.")
    ]

    for i, (num, title, badge, desc) in enumerate(metode_data):
        top_pos = Inches(1.55 + i * 1.3)
        deck.add_card(s12, Inches(0.8), top_pos, Inches(11.733), Inches(1.15))
        
        nb = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), top_pos + Inches(0.22), Inches(0.85), Inches(0.7))
        nb.fill.solid()
        nb.fill.fore_color.rgb = COLOR_LIGHT_SLATE
        nb.line.color.rgb = COLOR_CARD_BORDER
        p_nb = nb.text_frame.paragraphs[0]
        p_nb.text = num
        p_nb.font.name = FONT_FAMILY
        p_nb.font.bold = True
        p_nb.font.size = Pt(14)
        p_nb.font.color.rgb = COLOR_NAVY_MID
        p_nb.alignment = PP_ALIGN.CENTER

        tb = s12.shapes.add_textbox(Inches(2.05), top_pos + Inches(0.15), Inches(10.2), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        deck.add_card_header(tf, title, badge, COLOR_BLUE_ACCENT)
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(9.5)
        p_d.font.color.rgb = COLOR_TEXT_BODY

    deck.add_footer(s12, 12)

    # --------------------------------------------------------------------------
    # SLIDE 13: LANDASAN TEORI I: FORMALDEHID & REAKSI HIDRAZON ADH
    # --------------------------------------------------------------------------
    s13 = deck.add_blank_slide()
    deck.add_header(s13, "Bab II: Tinjauan Pustaka", "Landasan Teori I: Reaksi Kimia Formaldehid & Gugus Hidrazida ADH",
                    "Mekanisme Adisi-Eliminasi Nukleofilik Pembentukan Ikatan Kovalen Hidrazon Stabil")

    # Left: Equation & Teori
    deck.add_equation_box(
        s13, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Persamaan Reaksi Ikatan Hidrazon",
        "R-NH-NH2  +  HCHO  -->  R-NH-N=CH2  +  H2O",
        [
            ("R-NH-NH2", "Adipic acid dihydrazide (ADH) dengan gugus hidrazida terminal aktif"),
            ("HCHO", "Molekul formaldehida bebas (gugus karbonil elektrofilik)"),
            ("R-NH-N=CH2", "Ikatan hidrazon kovalen stabil hasil penangkapan formaldehida"),
            ("H2O", "Molekul air hasil reaksi kondensasi adisi-eliminasi nukleofilik")
        ]
    )
    # Extra explanation in left box
    tb13_extra = s13.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.6), Inches(2.1))
    tf13_ex = tb13_extra.text_frame
    tf13_ex.word_wrap = True
    p13_h = tf13_ex.paragraphs[0]
    p13_h.text = "Pengaruh terhadap Transduksi Sensor Magnetik:"
    p13_h.font.name = FONT_FAMILY
    p13_h.font.bold = True
    p13_h.font.size = Pt(9.5)
    p13_h.font.color.rgb = COLOR_NAVY_DARK
    p13_h.space_after = Pt(3)
    p13_d = tf13_ex.add_paragraph()
    p13_d.text = "Pembentukan ikatan hidrazon menyebabkan delokalisasi elektron dan perubahan konformasi spasial rantai polimer, mengubah momen dipol magnetik stray nanopartikel Fe3O4 di sekitar sensor TMR."
    p13_d.font.name = FONT_FAMILY
    p13_d.font.size = Pt(9.0)
    p13_d.font.color.rgb = COLOR_TEXT_BODY

    # Right: Gambar ikatan formalin
    deck.add_image_fitted(s13, "Gambar/Bab2/babII_ikatan_formalin.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar II.1 Diagram Reaksi Penangkapan Formaldehida oleh Gugus Hidrazida")

    deck.add_footer(s13, 13)

    # --------------------------------------------------------------------------
    # SLIDE 14: LANDASAN TEORI II: FISIKA TUNNELING MAGNETORESISTANCE (TMR)
    # --------------------------------------------------------------------------
    s14 = deck.add_blank_slide()
    deck.add_header(s14, "Bab II: Tinjauan Pustaka", "Landasan Teori II: Fisika Tunneling Magnetoresistance (TMR)",
                    "Fenomena Terowongan Kuantum Spin-Polarized pada Sambungan MgO Terowongan Magnetik")

    # Left: Formula Julliere
    deck.add_equation_box(
        s14, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Model Terowongan Julliere (Rasio TMR)",
        "TMR = (R_AP - R_P) / R_P = (2 * P1 * P2) / (1 - P1 * P2)",
        [
            ("TMR", "Rasio perubahan resistansi tunneling magnetik (%)"),
            ("R_AP", "Resistansi sambungan saat orientasi spin elektroda anti-paralel"),
            ("R_P", "Resistansi sambungan saat orientasi spin elektroda paralel"),
            ("P1, P2", "Derajat polarisasi spin elektron pada ferromagnetik 1 dan 2"),
            ("ALT023-10E", "Sensor jembatan Wheatstone penuh bipolar dengan rentang linear +-1.0 mT")
        ]
    )
    tb14_ex = s14.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.6), Inches(2.1))
    tf14_ex = tb14_ex.text_frame
    tf14_ex.word_wrap = True
    p14_h = tf14_ex.paragraphs[0]
    p14_h.text = "Spesifikasi Sensor ALT023-10E (NVE Corporation):"
    p14_h.font.name = FONT_FAMILY
    p14_h.font.bold = True
    p14_h.font.size = Pt(9.5)
    p14_h.font.color.rgb = COLOR_NAVY_DARK
    p14_h.space_after = Pt(2)
    deck.add_bullet_item(tf14_ex, "Tegangan Suplai:", "5.0 V DC tunggal dengan kapasitor bypass 100 nF.", pt_size=9.0)
    deck.add_bullet_item(tf14_ex, "Resistansi Jembatan:", "~20 kOhm per elemen jembatan Wheatstone.", pt_size=9.0)
    deck.add_bullet_item(tf14_ex, "Sensitivitas:", "Jauh melampaui sensor GMR konvensional pada medan lemah.", pt_size=9.0)

    # Right: Gambar TMR Layer & ALT023
    deck.add_image_fitted(s14, "Gambar/Bab2/babII_TMR_Layer.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.7),
                          border=True, caption="Gambar II.2 Struktur Lapisan Magnetic Tunnel Junction (MTJ)")
    deck.add_image_fitted(s14, "Gambar/Bab2/babII_ALT023.png", Inches(7.1), Inches(4.45), Inches(5.4), Inches(2.3),
                          border=True, caption="Gambar II.3 Paket dan Konfigurasi Pin Sensor TMR ALT023-10E")

    deck.add_footer(s14, 14)

    # --------------------------------------------------------------------------
    # SLIDE 15: LANDASAN TEORI III: MEDAN ACUAN KUMPARAN HELMHOLTZ
    # --------------------------------------------------------------------------
    s15 = deck.add_blank_slide()
    deck.add_header(s15, "Bab II: Tinjauan Pustaka", "Landasan Teori III: Kumparan Helmholtz sebagai Medan Acuan Presisi",
                    "Pembangkitan Medan Magnet Homogen Melalui Pasangan Kumparan Koaksial Sejajar")

    # Left: Formula Helmholtz
    deck.add_equation_box(
        s15, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Persamaan Medan Magnetik Pusat Helmholtz",
        "B(0) = (4/5)^(3/2) * (mu_0 * N * I) / R  ~=  0.7155 * (mu_0 * N * I) / R",
        [
            ("B(0)", "Kuat medan magnetik homogen tepat di pusat kumparan (Tesla)"),
            ("mu_0", "Permeabilitas magnetik ruang hampa (4*pi * 10^-7 T*m/A)"),
            ("N", "Jumlah lilitan kawat per kumparan tembaga"),
            ("I", "Arus listrik DC yang mengalir melintasi kumparan (Ampere)"),
            ("R", "Jari-jari kumparan dan jarak pemisah antarkumparan (meter)"),
            ("Kondisi", "Turunan kedua medan d^2B/dz^2 = 0 pada titik pusat (homogen)")
        ]
    )

    # Right Card: Spesifikasi Meja Lab Bolabot
    deck.add_card(s15, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2))
    tb15_r = s15.shapes.add_textbox(Inches(7.35), Inches(1.75), Inches(4.9), Inches(4.8))
    tf15_r = tb15_r.text_frame
    tf15_r.word_wrap = True
    deck.add_card_header(tf15_r, "Spesifikasi Sistem Helmholtz Bolabot", "Ground Truth Fisik", COLOR_NAVY_MID)
    deck.add_bullet_item(tf15_r, "Catu Daya Variabel:", "Power supply DC 0.0 - 16.0 V dengan pembacaan arus presisi.", pt_size=10.0)
    deck.add_bullet_item(tf15_r, "Resistansi Kumparan:", "R kumparan ~10 Ohm, mengalirkan arus maksimal hingga ~1.6 A.", pt_size=10.0)
    deck.add_bullet_item(tf15_r, "Rentang Medan Terhasilkan:", "Medan positif 0 - 11.5 mT, dapat dibalik polaritas hingga -4.0 mT.", pt_size=10.0)
    deck.add_bullet_item(tf15_r, "Operasi Eksternal:", "Diatur melalui knob fisik laboratorium; GUI mencatat parameter Vhelm, Ihelm, dan Bteslameter sebagai ground truth manual.", pt_size=10.0)
    deck.add_bullet_item(tf15_r, "Verifikasi Medan:", "Divalidasi langsung menggunakan teslameter digital bersertifikasi tepat di pusat sumbu z kumparan.", pt_size=10.0)

    deck.add_footer(s15, 15)

    # --------------------------------------------------------------------------
    # SLIDE 16: LANDASAN TEORI IV: PENGKONDISI SINYAL AD623 & VREF = 2.50 V
    # --------------------------------------------------------------------------
    s16 = deck.add_blank_slide()
    deck.add_header(s16, "Bab II: Tinjauan Pustaka", "Landasan Teori IV: Pengkondisi Sinyal AD623 & Tegangan Referensi",
                    "Penguat Instrumentasi Presisi Rel-ke-Rel dengan Catu Daya Tunggal +5.0 V")

    # Left: Equation AD623
    deck.add_equation_box(
        s16, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Persamaan Penguatan AD623",
        "V_out = G * (V_IN+ - V_IN-) + V_REF ,   G = 1 + (100 kOhm / R_G)",
        [
            ("V_out", "Tegangan keluaran analog penguat instrumentasi (Volt)"),
            ("G", "Faktor penguatan diferensial (Gain)"),
            ("R_G", "Resistor gain eksternal yang terpasang pada pin 1 dan pin 8"),
            ("V_IN+, V_IN-", "Tegangan masukan diferensial dari jembatan sensor TMR"),
            ("V_REF", "Tegangan referensi offset pada Pin 5 = 2.50 V")
        ]
    )
    tb16_ex = s16.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.6), Inches(2.1))
    tf16_ex = tb16_ex.text_frame
    tf16_ex.word_wrap = True
    p16_h = tf16_ex.paragraphs[0]
    p16_h.text = "Desain Kritis Tegangan Referensi VREF = 2.50 V:"
    p16_h.font.name = FONT_FAMILY
    p16_h.font.bold = True
    p16_h.font.size = Pt(9.5)
    p16_h.font.color.rgb = COLOR_NAVY_DARK
    p16_h.space_after = Pt(2)
    deck.add_bullet_item(tf16_ex, "Pembagi Tegangan Resistor:", "Resistor presisi R3 = R4 = 1.0 kOhm membagi suplai +5.0 V tepat menjadi VREF = 2.50 V (bukan 1.65 V).", pt_size=9.0)
    deck.add_bullet_item(tf16_ex, "Titik Nol Medan (B = 0):", "Keluaran bertengger stabil di 2.50 V, memungkinkan pembacaan medan bipolar (+- B) tanpa terpotong rel ground.", pt_size=9.0)

    # Right: Pinout AD623
    deck.add_image_fitted(s16, "Gambar/Bab2/babII_AD623_Pinout.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar II.4 Konfigurasi Pinout IC Penguat Instrumentasi AD623")

    deck.add_footer(s16, 16)

    # --------------------------------------------------------------------------
    # SLIDE 17: LANDASAN TEORI V: RC LPF ANTI-ALIASING & ADC ADS1115
    # --------------------------------------------------------------------------
    s17 = deck.add_blank_slide()
    deck.add_header(s17, "Bab II: Tinjauan Pustaka", "Landasan Teori V: Filter Pasif Anti-Aliasing (RC LPF) & ADC ADS1115",
                    "Penyaringan Derau Frekuensi Tinggi dan Digitalisasi 16-Bit Beresolusi Tinggi")

    # Left: Equation Cutoff & LSB
    deck.add_equation_box(
        s17, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Formula Frekuensi Cut-off & Resolusi LSB",
        "f_c = 1 / (2*pi * R * C) ,   LSB = FSR / 2^15 = 6.144 V / 32768 = 0.1875 mV",
        [
            ("f_c", "Frekuensi batas cut-off filter low pass pasif satu kutub (~15.9 kHz)"),
            ("R, C", "Resistor filter 1 kOhm dan kapasitor keramik 10 nF (decoupling 100 nF)"),
            ("LSB", "Resolusi terkecil ADC per hitungan count (0.1875 mV/count)"),
            ("FSR", "Full-Scale Range ADC pada penguatan GAIN_TWOTHIRDS (+-6.144 V)"),
            ("Resolusi", "16-Bit konversi diferensial atau single-ended via antarmuka I2C")
        ]
    )
    tb17_ex = s17.shapes.add_textbox(Inches(1.0), Inches(4.6), Inches(5.6), Inches(2.0))
    tf17_ex = tb17_ex.text_frame
    tf17_ex.word_wrap = True
    p17_h = tf17_ex.paragraphs[0]
    p17_h.text = "Fungsi Proteksi Sinyal:"
    p17_h.font.name = FONT_FAMILY
    p17_h.font.bold = True
    p17_h.font.size = Pt(9.5)
    p17_h.font.color.rgb = COLOR_NAVY_DARK
    p17_h.space_after = Pt(2)
    deck.add_bullet_item(tf17_ex, "Peredaman Aliasing:", "Memotong interferensi derau induksi jala-jala listrik dan switching power supply sebelum sampling ADC.", pt_size=9.0)
    deck.add_bullet_item(tf17_ex, "Presisi Konversi:", "Menjamin fluktuasi sub-milivolt akibat interaksi formalin terekam akurat tanpa kehilangan informasi.", pt_size=9.0)

    # Right: Images LPF & ADS1115
    deck.add_image_fitted(s17, "Gambar/Bab2/babII_LPF.PNG", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.4),
                          border=True, caption="Gambar II.5 Skema Sirkuit Filter RC Low-Pass Pasif")
    deck.add_image_fitted(s17, "Gambar/Bab2/babII_ADS-1115-c.jpg", Inches(7.1), Inches(4.15), Inches(5.4), Inches(2.6),
                          border=True, caption="Gambar II.6 Modul Konverter Analog-ke-Digital ADS1115 16-Bit")

    deck.add_footer(s17, 17)

    # --------------------------------------------------------------------------
    # SLIDE 18: LANDASAN TEORI VI: GREEN SYNTHESIS FE3O4 & MATRIKS PVA
    # --------------------------------------------------------------------------
    s18 = deck.add_blank_slide()
    deck.add_header(s18, "Bab II: Tinjauan Pustaka", "Landasan Teori VI: Sintesis Hijau Nanopartikel Fe3O4 & Polimer PVA",
                    "Pemanfaatan Ekstrak Daun Kelor (Moringa oleifera) dan Polivinil Alkohol sebagai Carrier")

    # Left: Fe3O4 Green Synthesis
    deck.add_card(s18, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb18_l = s18.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(4.8))
    tf18_l = tb18_l.text_frame
    tf18_l.word_wrap = True
    deck.add_card_header(tf18_l, "Sintesis Hijau Fe3O4 Daun Kelor", "Green Nanotechnology", COLOR_EMERALD)
    deck.add_bullet_item(tf18_l, "Fitokimia Moringa oleifera:", "Ekstrak daun kelor kaya akan senyawa bioaktif polifenol, flavonoid, dan asam askorbat.", pt_size=10.0)
    deck.add_bullet_item(tf18_l, "Peran Agen Pereduksi:", "Mereduksi prekursor garam besi (FeCl3 dan FeCl2) secara bertahap menuju kristal magnetit Fe3O4.", pt_size=10.0)
    deck.add_bullet_item(tf18_l, "Capping Agent Alami:", "Mencegah aglomerasi partikel secara alami tanpa memerlukan surfaktan sintetis toksik (seperti CTAB atau oleat).", pt_size=10.0)
    deck.add_bullet_item(tf18_l, "Karakter Superparamagnetik:", "Menghasilkan suseptibilitas tinggi saat dikenai medan luar dan kembali nol seketika saat medan dihilangkan.", pt_size=10.0)

    # Right: Polimer PVA Matrix
    deck.add_card(s18, Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb18_r = s18.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf18_r = tb18_r.text_frame
    tf18_r.word_wrap = True
    deck.add_card_header(tf18_r, "Matriks Polimer Polivinil Alkohol (PVA)", "Carrier Serat Elektrospinning", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf18_r, "Formulasi Optimum 10% wt:", "Konsentrasi 10% wt menghasilkan viskositas sol yang ideal untuk perentangan jet cairan elektrospinning tanpa pembentukan butiran manik-manik (beads-free).", pt_size=10.0)
    deck.add_bullet_item(tf18_r, "Struktur Rantai Hidrofilik:", "Memiliki kelimpahan gugus hidroksil (-OH) yang membentuk ikatan hidrogen intermolekul yang kuat.", pt_size=10.0)
    deck.add_bullet_item(tf18_r, "Distribusi Homogen:", "Menjaga nanopartikel Fe3O4 dan molekul ADH terdispersi merata di sepanjang diameter poros nanofiber.", pt_size=10.0)
    deck.add_bullet_item(tf18_r, "Biokompatibilitas Penuh:", "Aman digunakan dalam analisis sampel bahan pangan konsumsi.", pt_size=10.0)

    deck.add_footer(s18, 18)

    # --------------------------------------------------------------------------
    # SLIDE 19: LANDASAN TEORI VII: CROSSLINKING ASAM SITRAT (130 C) & ADH
    # --------------------------------------------------------------------------
    s19 = deck.add_blank_slide()
    deck.add_header(s19, "Bab II: Tinjauan Pustaka", "Landasan Teori VII: Crosslinking Asam Sitrat & Enkapsulasi ADH",
                    "Esterifikasi Termal 130 C untuk Ketahanan Air Nanofiber dan Penangkapan Formalin")

    # Left: Mekanisme Asam Sitrat 130 C
    deck.add_card(s19, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb19_l = s19.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.5), Inches(4.8))
    tf19_l = tb19_l.text_frame
    tf19_l.word_wrap = True
    deck.add_card_header(tf19_l, "Taut-Silang Asam Sitrat (Curing 130 C)", "Stabilisasi Jaringan Nanofiber", COLOR_AMBER)
    deck.add_bullet_item(tf19_l, "Reaksi Esterifikasi Termal:", "Asam sitrat (tri-karboksilat) bereaksi dengan gugus -OH rantai PVA membentuk jembatan ester kovalen.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Suhu Curing Optimal 130 C:", "Pemanasan selama 1.5 jam pada suhu 130 C memaksimalkan taut-silang tanpa memicu degradasi termal polimer maupun kerusakan gugus ADH.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Ketahanan Air (Water Insoluble):", "Mengubah film nanofiber menjadi tidak larut saat ditetesi analit cairan bakso, menjaga integritas struktur selama pengukuran.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Enkapsulasi ADH:", "Dua gugus hidrazida terminal ADH tetap bebas terekspos di permukaan serat, siap mengikat formaldehida secara selektif.", pt_size=10.0)

    # Right: Gambar Electrospinning
    deck.add_image_fitted(s19, "Gambar/Bab2/babII_elspinPVA.PNG", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar II.7 Skema Pembentukan Nanofiber Melalui Metode Elektrospinning")

    deck.add_footer(s19, 19)

    # --------------------------------------------------------------------------
    # SLIDE 20: LANDASAN TEORI VIII: KLASIFIKASI SUPPORT VECTOR MACHINE (SVM)
    # --------------------------------------------------------------------------
    s20 = deck.add_blank_slide()
    deck.add_header(s20, "Bab II: Tinjauan Pustaka", "Landasan Teori VIII: Pemodelan Support Vector Machine (SVM)",
                    "Prinsip Hyperplane Margin Maksimal dan Transformasi Kernel Gaussian RBF")

    # Left: Optimasi SVM
    deck.add_equation_box(
        s20, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Formulasi Optimasi SVM & Kernel RBF",
        "min (1/2 ||w||^2 + C * sum(xi_i)) ,   K(x, x') = exp(-gamma * ||x - x'||^2)",
        [
            ("w", "Vektor bobot normal yang mendefinisikan bidang pemisah hyperplane"),
            ("C", "Parameter regularisasi trade-off antara margin lebar dan toleransi eror"),
            ("xi_i", "Variabel slack untuk mentoleransi titik data yang melanggar batas margin"),
            ("K(x, x')", "Kernel Radial Basis Function (RBF) memetakan data ke ruang tak berhingga"),
            ("gamma", "Parameter invers lebar pengaruh sampel data tunggal (1 / 2*sigma^2)")
        ]
    )
    tb20_ex = s20.shapes.add_textbox(Inches(1.0), Inches(4.5), Inches(5.6), Inches(2.1))
    tf20_ex = tb20_ex.text_frame
    tf20_ex.word_wrap = True
    p20_h = tf20_ex.paragraphs[0]
    p20_h.text = "Keunggulan & Keterbatasan Model SVM:"
    p20_h.font.name = FONT_FAMILY
    p20_h.font.bold = True
    p20_h.font.size = Pt(9.5)
    p20_h.font.color.rgb = COLOR_NAVY_DARK
    p20_h.space_after = Pt(2)
    deck.add_bullet_item(tf20_ex, "Keunggulan:", "Sangat tangguh pada data berdimensi sedang, kepastian solusi konvergen global optimum.", pt_size=9.0)
    deck.add_bullet_item(tf20_ex, "Tantangan:", "Penentuan hyperparameter C dan gamma memerlukan pencarian grid search; rentan terhadap derau dinamis non-linear.", pt_size=9.0)

    # Right Card: Skema Alur SVM
    deck.add_card(s20, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2))
    tb20_r = s20.shapes.add_textbox(Inches(7.35), Inches(1.75), Inches(4.9), Inches(4.8))
    tf20_r = tb20_r.text_frame
    tf20_r.word_wrap = True
    deck.add_card_header(tf20_r, "Arsitektur Klasifikasi Sinyal Sensor", "Metodologi Klasik", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf20_r, "Input Vektor (5 Fitur):", "Menerima 5 fitur dinamis terstandarisasi: dVmax, respon waktu, slope awal, Vsteady, dan AUC.", pt_size=10.0)
    deck.add_bullet_item(tf20_r, "Prapemrosesan Standard Scaler:", "Normalisasi skala nilai z-score agar kontribusi antarfitur seimbang.", pt_size=10.0)
    deck.add_bullet_item(tf20_r, "Validasi Silang (5-Fold CV):", "Evaluasi berulang pada 5 subset data acak untuk mencegah overfitting.", pt_size=10.0)
    deck.add_bullet_item(tf20_r, "Metrik Penilaian:", "Akurasi, Presisi, Recall, F1-Score, dan matriks konfusi antarkelas formalin.", pt_size=10.0)

    deck.add_footer(s20, 20)

    # --------------------------------------------------------------------------
    # SLIDE 21: LANDASAN TEORI IX: QUANTUM SUPPORT VECTOR CLASSIFIER (QSVC)
    # --------------------------------------------------------------------------
    s21 = deck.add_blank_slide()
    deck.add_header(s21, "Bab II: Tinjauan Pustaka", "Landasan Teori IX: Quantum Support Vector Classifier (QSVC)",
                    "Pemetaan Fitur Kuantum ke Ruang Hilbert 2^n Qubit dan Matriks Quantum Kernel")

    # Left: Quantum State & Kernel
    deck.add_equation_box(
        s21, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
        "Pemetaan Kuantum & Matriks Kernel Kuantum",
        "|psi(x)> = U_Phi(x) |0^n> ,   K_Q(x, x') = |<psi(x') | psi(x)>|^2",
        [
            ("|0^n>", "Status awal dasar register n qubit kuantum (|00...0>)"),
            ("U_Phi(x)", "Operator uniter sirkuit kuantum berparameter (ZZFeatureMap)"),
            ("|psi(x)>", "Vektor status kuantum ter-entangle di ruang Hilbert berdimensi 2^n"),
            ("K_Q(x, x')", "Nilai matriks kernel kuantum berdasarkan Quantum State Fidelity"),
            ("Separasi", "Memisahkan pola korelasi non-linear yang tidak terurai oleh kernel klasik")
        ]
    )

    # Right: Komparasi Spesifikasi SVM vs QSVC
    headers_q = ["Fitur Pembanding", "SVM Klasik", "QSVC Kuantum (Qiskit)"]
    rows_q = [
        ["Ruang Pemetaan", "Ruang Euclidean berdimensi tinggi", "Ruang Hilbert berdimensi 2^n qubit"],
        ["Transformasi Fitur", "Fungsi matematika RBF Gauss", "Sirkuit kuantum uniter & keterikatan (entanglement)"],
        ["Kalkulasi Kernel", "Jarak kuadratik numerik ||x - x'||", "Transisi probabilitas fidelitas status kuantum"],
        ["Ketahanan Derau", "Sensitif terhadap fluktuasi sinyal", "Terbukti lebih resilien terhadap noise gaussian"],
        ["Lingkungan Eksekusi", "Scikit-Learn (CPU)", "Qiskit Aer Statevector Simulator"]
    ]
    deck.add_table(s21, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2), headers_q, rows_q,
                   col_widths=[Inches(1.8), Inches(1.8), Inches(1.8)])

    deck.add_footer(s21, 21)

    # --------------------------------------------------------------------------
    # SLIDE 22: METODOLOGI: WAKTU, TEMPAT, ALAT & BAHAN
    # --------------------------------------------------------------------------
    s22 = deck.add_blank_slide()
    deck.add_header(s22, "Bab III: Metode Penelitian", "Waktu, Tempat, dan Spesifikasi Alat & Bahan",
                    "Pelaksanaan Riset di Bolabot Techno Robotic Institute (September - Desember 2026)")

    # Top Location Banner
    deck.add_card(s22, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.95), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb22_t = s22.shapes.add_textbox(Inches(1.05), Inches(1.62), Inches(11.2), Inches(0.8))
    tf22_t = tb22_t.text_frame
    tf22_t.word_wrap = True
    p22_l1 = tf22_t.paragraphs[0]
    p22_l1.text = "Waktu Pelaksanaan : September 2026 - Desember 2026 (Durasi 4 Bulan Efektif)"
    p22_l1.font.name = FONT_FAMILY
    p22_l1.font.bold = True
    p22_l1.font.size = Pt(10.5)
    p22_l1.font.color.rgb = COLOR_NAVY_DARK
    p22_l2 = tf22_t.add_paragraph()
    p22_l2.text = "Tempat Riset       : Kantor Bolabot Techno Robotic Institute, Jl. Sauyunan VI No. 10 Blok F6, Bandung, Jawa Barat"
    p22_l2.font.name = FONT_FAMILY
    p22_l2.font.size = Pt(9.5)
    p22_l2.font.color.rgb = COLOR_TEXT_BODY

    # Table Alat & Bahan
    headers_ab = ["Kategori", "Item / Instrumen Spesifik", "Spesifikasi / Parameter Teknis", "Fungsi Utama dalam Riset"]
    rows_ab = [
        ["Hardware", "Sensor TMR ALT023-10E", "Bipolar bridge, linear +-1.0 mT, Vcc 5V", "Transduser medan magnetik distorsi formalin"],
        ["Hardware", "In-Amp AD623 & ADS1115", "Catu 5V, VREF 2.50V, ADC 16-Bit I2C", "Pengkondisi sinyal & digitalisasi presisi tinggi"],
        ["Hardware", "Kumparan Helmholtz", "R ~10 Ohm, 0 - 16 V DC, 0 - 11.5 mT", "Pembangkit medan magnet acuan homogen"],
        ["Hardware", "Sistem Mikrokontroler", "Arduino Uno R3 & Raspberry Pi 5", "Akuisisi serial & stasiun komputasi ML edge"],
        ["Kimia / Bahan", "Ekstrak Daun Kelor & Besi", "Moringa oleifera, FeCl3 & FeCl2 (2:1)", "Green synthesis nanopartikel superparamagnetik Fe3O4"],
        ["Kimia / Bahan", "Polimer PVA, Sitrat, ADH", "PVA 10% wt, Asam Sitrat, ADH 98%", "Matriks nanofiber elektrospinning selektif formalin"],
        ["Sampel Uji", "Formalin & Sampel Bakso", "Standar HCHO 37% & Bakso Pasar Riil", "Pembuatan kurva kalibrasi & validasi klasifikasi"]
    ]
    deck.add_table(s22, Inches(0.8), Inches(2.65), Inches(11.733), Inches(4.2), headers_ab, rows_ab,
                   col_widths=[Inches(1.8), Inches(3.0), Inches(3.6), Inches(3.333)])

    deck.add_footer(s22, 22)

    # --------------------------------------------------------------------------
    # SLIDE 23: METODOLOGI: DIAGRAM ALIR PENELITIAN LENGKAP
    # --------------------------------------------------------------------------
    s23 = deck.add_blank_slide()
    deck.add_header(s23, "Bab III: Metode Penelitian", "Diagram Alir Penelitian Komprehensif (6 Tahapan Utama)",
                    "Alur Kerja Menyeluruh dari Perancangan Desain hingga Evaluasi Komparasi Model Cerdas")

    # Left: 6 Tahapan Text Card
    deck.add_card(s23, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb23_l = s23.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(4.8))
    tf23_l = tb23_l.text_frame
    tf23_l.word_wrap = True
    deck.add_card_header(tf23_l, "6 Tahapan Eksekusi Riset", "Alur Kerja Sistematis", COLOR_NAVY_MID)
    deck.add_bullet_item(tf23_l, "Tahap 1: Desain & Fabrikasi Hardware", "Perancangan skematik terisolasi grounding, perakitan AD623-ADS1115, dan cetak 3D casing.", pt_size=9.5)
    deck.add_bullet_item(tf23_l, "Tahap 2: Sintesis Nanomaterial", "Ekstraksi kelor, kopresipitasi Fe3O4, elektrospinning sol PVA-sitrat-ADH, curing 130 C.", pt_size=9.5)
    deck.add_bullet_item(tf23_l, "Tahap 3: Karakterisasi & Kalibrasi", "Kalibrasi medan Helmholtz dengan teslameter, uji kurva dV/dB sensor TMR.", pt_size=9.5)
    deck.add_bullet_item(tf23_l, "Tahap 4: Pengujian Sampel Bakso", "Maserasi bakso, sentrifugasi 4000 rpm 10 min, perekaman sinyal dinamis 5 detik.", pt_size=9.5)
    deck.add_bullet_item(tf23_l, "Tahap 5: Ekstraksi Fitur & Pelatihan ML", "Ekstraksi 5 fitur dinamis, 5-Fold Cross Validation komparasi SVM dan QSVC.", pt_size=9.5)
    deck.add_bullet_item(tf23_l, "Tahap 6: Evaluasi & Deployment", "Analisis akurasi, uji ketahanan derau, ekspor model .pkl ke Raspberry Pi 5.", pt_size=9.5)

    # Right: Gambar Diagram Alir Penelitian
    deck.add_image_fitted(s23, "Gambar/Bab3/BABIII_DiagramAlirPenelitian.drawio.png", Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2),
                          border=True, caption="Gambar III.1 Diagram Alir Metodologi Penelitian Tugas Akhir")

    deck.add_footer(s23, 23)

    # --------------------------------------------------------------------------
    # SLIDE 24: METODOLOGI: HARDWARE, CASING 3D & SKEMATIK SIRKUIT
    # --------------------------------------------------------------------------
    s24 = deck.add_blank_slide()
    deck.add_header(s24, "Bab III: Metode Penelitian", "Desain Hardware, Casing 3D & Skematik Sirkuit Presisi",
                    "Pengondisi Sinyal AD623, Isolasi Grounding Bintang, dan Housing Statif Non-Magnetik")

    # Left: Skematik Rangkaian
    deck.add_image_fitted(s24, "Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png", Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
                          border=True, caption="Gambar III.2 Skematik Sirkuit Terintegrasi TMR, AD623, Filter RC, dan ADS1115")

    # Right Top: Casing 3D
    deck.add_image_fitted(s24, "Gambar/Bab3/babIII-desainTMR.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.7),
                          border=True, caption="Gambar III.3 Desain 3D Housing Sensor dan Dudukan Kaca Preparat")

    # Right Bottom: Key Hardware Specs
    deck.add_card(s24, Inches(7.1), Inches(4.45), Inches(5.4), Inches(2.3), bg_color=COLOR_LIGHT_SLATE, border_color=COLOR_CARD_BORDER)
    tb24_b = s24.shapes.add_textbox(Inches(7.3), Inches(4.55), Inches(5.0), Inches(2.1))
    tf24_b = tb24_b.text_frame
    tf24_b.word_wrap = True
    deck.add_card_header(tf24_b, "Fitur Desain Fisik & Proteksi Derau", "Integritas Sinyal", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf24_b, "Bintang Grounding (Star Topology):", "Pemisahan jalur ground analog dan digital untuk meniadakan ground loop.", pt_size=9.0)
    deck.add_bullet_item(tf24_b, "Material Non-Magnetik:", "Housing sensor dan statif menggunakan filament PLA dan akrilik murni.", pt_size=9.0)
    deck.add_bullet_item(tf24_b, "Presisi Posisi:", "Memastikan sensor TMR berada tepat di pusat medan homogen Helmholtz.", pt_size=9.0)

    deck.add_footer(s24, 24)

    # --------------------------------------------------------------------------
    # SLIDE 25: METODOLOGI: PERANGKAT LUNAK (ARDUINO & GUI PYTHON)
    # --------------------------------------------------------------------------
    s25 = deck.add_blank_slide()
    deck.add_header(s25, "Bab III: Metode Penelitian", "Arsitektur Perangkat Lunak: Arduino Uno & GUI Python",
                    "Firmware Streaming Serial dan Antarmuka CustomTkinter Berbasis Durasi Waktu")

    # Left: Alur Arduino Uno
    deck.add_image_fitted(s25, "Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png", Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2),
                          border=True, caption="Gambar III.4 Diagram Alir Firmware Mikrokontroler Arduino Uno")

    # Right: Alur GUI Python
    deck.add_image_fitted(s25, "Gambar/Bab3/babIII_DiagramAlirPython.drawio.png", Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2),
                          border=True, caption="Gambar III.5 Diagram Alir Aplikasi GUI Python TMRAcquisitionApp")

    deck.add_footer(s25, 25)

    # --------------------------------------------------------------------------
    # SLIDE 26: METODOLOGI: SINTESIS FE3O4 HIJAU & ELEKTROSPINNING
    # --------------------------------------------------------------------------
    s26 = deck.add_blank_slide()
    deck.add_header(s26, "Bab III: Metode Penelitian", "Sintesis Hijau Fe3O4 & Fabrikasi Nanofiber Elektrospinning",
                    "Prosedur Ekstraksi Kelor, Sol Polimer, Parameter Pemintalan Elektrik, dan Curing 130 C")

    # Left: Diagram Sintesis
    deck.add_image_fitted(s26, "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png", Inches(0.8), Inches(1.55), Inches(5.8), Inches(5.2),
                          border=True, caption="Gambar III.6 Diagram Alir Prosedur Kimia Sintesis Nanofiber Fe3O4/PVA-Sitrat-ADH")

    # Right: Parameter Kunci
    deck.add_card(s26, Inches(7.0), Inches(1.55), Inches(5.533), Inches(5.2))
    tb26_r = s26.shapes.add_textbox(Inches(7.25), Inches(1.75), Inches(5.0), Inches(4.8))
    tf26_r = tb26_r.text_frame
    tf26_r.word_wrap = True
    deck.add_card_header(tf26_r, "Parameter Optimal Laboratorium", "Protokol Sintesis & Fabrikasi", COLOR_EMERALD)
    deck.add_bullet_item(tf26_r, "Ekstraksi Daun Kelor:", "50 g daun segar dalam 250 mL akuades, ekstraksi maserasi panas pada suhu 80 C selama 30 menit, disaring kertas Whatman.", pt_size=9.5)
    deck.add_bullet_item(tf26_r, "Kopresipitasi Fe3O4:", "FeCl3 dan FeCl2 (rasio molar 2:1) + 20 mL ekstrak kelor, titrasi NaOH 2 M hingga pH 11 pada 70 C, dicuci hingga pH netral.", pt_size=9.5)
    deck.add_bullet_item(tf26_r, "Formulasi Sol Gel:", "PVA 10% wt + Fe3O4 2% wt + Asam Sitrat 5% wt + ADH 3% wt diaduk konstan pada 60 C hingga homogen.", pt_size=9.5)
    deck.add_bullet_item(tf26_r, "Parameter Elektrospinning:", "Tegangan tinggi 15 kV, laju alir syringe pump 0.5 mL/jam, jarak ujung jarum ke drum kolektor 15 cm, drum 300 rpm.", pt_size=9.5)
    deck.add_bullet_item(tf26_r, "Curing Termal Final:", "Oven pemanas pada suhu 130 C selama 1.5 jam untuk pembentukan ikatan taut-silang ester permanen.", pt_size=9.5)

    deck.add_footer(s26, 26)

    # --------------------------------------------------------------------------
    # SLIDE 27: METODOLOGI: KALIBRASI HELMHOLTZ & KARAKTERISASI TMR
    # --------------------------------------------------------------------------
    s27 = deck.add_blank_slide()
    deck.add_header(s27, "Bab III: Metode Penelitian", "Prosedur Kalibrasi Kumparan Helmholtz & Sensor TMR",
                    "Pemetaan Faktor Konversi Medan Magnetik dan Penentuan Kurva Sensitivitas Diferensial")

    # Left: Kalibrasi Helmholtz
    deck.add_card(s27, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb27_l = s27.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.1), Inches(4.8))
    tf27_l = tb27_l.text_frame
    tf27_l.word_wrap = True
    deck.add_card_header(tf27_l, "Tahap 1: Kalibrasi Medan Helmholtz", "Standarisasi Medan Acuan", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf27_l, "Sapuan Arus DC:", "Mengatur power supply dari 0.0 A hingga 1.6 A (tegangan 0 - 16 V) dengan kenaikan bertahap 0.1 A.", pt_size=10.0)
    deck.add_bullet_item(tf27_l, "Perekaman Teslameter:", "Mengukur medan magnet riil B (mT) di pusat kumparan secara simultan menggunakan teslameter digital.", pt_size=10.0)
    deck.add_bullet_item(tf27_l, "Regresi Linear Kalibrasi:", "Memperoleh persamaan linear B = k * I dengan korelasi R^2 > 0.999 sebagai faktor konversi arus ke medan magnet.", pt_size=10.0)
    deck.add_bullet_item(tf27_l, "Verifikasi Polaritas:", "Menguji pembalikan polaritas kabel kumparan untuk sapuan medan negatif hingga -4.0 mT.", pt_size=10.0)

    # Right: Karakterisasi TMR
    deck.add_card(s27, Inches(6.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb27_r = s27.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf27_r = tb27_r.text_frame
    tf27_r.word_wrap = True
    deck.add_card_header(tf27_r, "Tahap 2: Karakterisasi Respon TMR", "Evaluasi Transduser ALT023", COLOR_NAVY_MID)
    deck.add_bullet_item(tf27_r, "Perekaman Tegangan Vout:", "Mencatat respon tegangan AD623-ADS1115 pada setiap titik medan magnet B yang diterapkan.", pt_size=10.0)
    deck.add_bullet_item(tf27_r, "Penentuan Rentang Linear:", "Menetapkan batas linearitas operasional sensor (+-1.0 mT) di mana respon tegangan berbanding lurus dengan medan.", pt_size=10.0)
    deck.add_bullet_item(tf27_r, "Sensitivitas Diferensial (dV/dB):", "Menggunakan fitting spline numerik pada modul analysis.py untuk mengekstrak sensitivitas lokal dV/dB (mV/mT).", pt_size=10.0)
    deck.add_bullet_item(tf27_r, "Penyimpanan Konstanta Kalibrasi:", "Menyimpan nilai intercept dan slope secara otomatis ke format JSON untuk koreksi realtime GUI.", pt_size=10.0)

    deck.add_footer(s27, 27)

    # --------------------------------------------------------------------------
    # SLIDE 28: METODOLOGI: PREPARASI SAMPEL BAKSO & 5 FITUR DINAMIS
    # --------------------------------------------------------------------------
    s28 = deck.add_blank_slide()
    deck.add_header(s28, "Bab III: Metode Penelitian", "Preparasi Sampel Bakso & Ekstraksi 5 Fitur Sinyal Dinamis",
                    "Protokol Ekstraksi Supernatan (Sentrifugasi 4000 rpm) dan Parameter Kuantitatif Sensor")

    # Left: Preparasi Ekstrak
    deck.add_card(s28, Inches(0.8), Inches(1.55), Inches(5.0), Inches(5.2))
    tb28_l = s28.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(4.5), Inches(4.8))
    tf28_l = tb28_l.text_frame
    tf28_l.word_wrap = True
    deck.add_card_header(tf28_l, "Protokol Ekstraksi Sampel Bakso", "Preparasi Matriks Pangan", COLOR_ROSE)
    deck.add_bullet_item(tf28_l, "Penghalusan Sampel (Maserasi):", "10 gram sampel bakso dihaluskan dan ditambahkan 50 mL akuades deionisasi (rasio 1:5 w/v).", pt_size=9.5)
    deck.add_bullet_item(tf28_l, "Sentrifugasi Pemisahan Fasa:", "Disentrifugasi pada kecepatan 4000 rpm selama 10 menit untuk mengendapkan serat daging dan lipid.", pt_size=9.5)
    deck.add_bullet_item(tf28_l, "Pengambilan Supernatan:", "Cairan jernih supernatan diambil sebagai analit bebas partikel pengganggu.", pt_size=9.5)
    deck.add_bullet_item(tf28_l, "Penetesan Mikropipet:", "Sebanyak 20 mikroliter analit diteteskan presisi di atas permukaan nanofiber sensor TMR.", pt_size=9.5)

    # Right: 5 Fitur Sinyal
    headers_f = ["Simbol Fitur", "Nama Fitur Dinamis", "Formulasi Matematika", "Relevansi Fisik"]
    rows_f = [
        ["dV_max", "Amplitudo Puncak", "|V_peak - V_baseline|", "Kekuatan respon konsentrasi formalin"],
        ["t_response", "Waktu Respon (90%)", "t(0.9 * dV_max) - t_0", "Kinetika reaksi adisi nukleofilik ADH"],
        ["(dV/dt)_0", "Slope Transien Awal", "Delta V / Delta t (awal)", "Laju difusi awal molekul ke pori serat"],
        ["V_steady", "Tegangan Tunak", "Mean(V(t)) pada t jenuh", "Keseimbangan ikatan kimia hidrazon"],
        ["AUC", "Area Under Curve", "Integral [V(t) - V_0] dt", "Akumulasi total energi respon interaksi"]
    ]
    deck.add_table(s28, Inches(6.1), Inches(1.55), Inches(6.433), Inches(5.2), headers_f, rows_f,
                   col_widths=[Inches(1.2), Inches(1.8), Inches(1.7), Inches(1.733)])

    deck.add_footer(s28, 28)

    # --------------------------------------------------------------------------
    # SLIDE 29: METODOLOGI: MODEL BUILDING SVM VS QSVC & DEPLOYMENT
    # --------------------------------------------------------------------------
    s29 = deck.add_blank_slide()
    deck.add_header(s29, "Bab III: Metode Penelitian", "Pelatihan Model SVM vs QSVC & Pipeline Deployment",
                    "Validasi Silang Kuantum-Klasik dan Penerapan Sistem Tertanam di Raspberry Pi 5")

    # Left: Model Building
    deck.add_image_fitted(s29, "Gambar/Bab3/babIII_ModelBuilding.drawio.png", Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2),
                          border=True, caption="Gambar III.7 Diagram Alir Pelatihan dan Validasi Komparasi Model SVM vs QSVC")

    # Right Top: Model Deploy
    deck.add_image_fitted(s29, "Gambar/Bab3/babIII_ModelDeploy.drawio.png", Inches(6.8), Inches(1.55), Inches(5.7), Inches(2.7),
                          border=True, caption="Gambar III.8 Diagram Alir Deployment Model ke Embedded System")

    # Right Bottom: Deployment Specs
    deck.add_card(s29, Inches(6.8), Inches(4.45), Inches(5.7), Inches(2.3), bg_color=COLOR_LIGHT_EMR, border_color=COLOR_EMERALD)
    tb29_b = s29.shapes.add_textbox(Inches(7.05), Inches(4.55), Inches(5.2), Inches(2.1))
    tf29_b = tb29_b.text_frame
    tf29_b.word_wrap = True
    deck.add_card_header(tf29_b, "Spesifikasi Deployment Raspberry Pi 5", "Edge Intelligence", COLOR_EMERALD)
    deck.add_bullet_item(tf29_b, "Format Model:", "Serialisasi model klasifikasi terbaik ke file biner .pkl via Joblib / Pickle.", pt_size=9.0)
    deck.add_bullet_item(tf29_b, "Perangkat Keras Edge:", "Raspberry Pi 5 (8GB RAM, Broadcom BCM2712 Quad-core ARM Cortex-A76 2.4GHz).", pt_size=9.0)
    deck.add_bullet_item(tf29_b, "Tampilan Hasil:", "Layar sentuh kapasitif terintegrasi menampilkan status keamanan bakso secara instan.", pt_size=9.0)

    deck.add_footer(s29, 29)

    # --------------------------------------------------------------------------
    # SLIDE 30: RENCANA KERJA, TARGET LUARAN & PENUTUP
    # --------------------------------------------------------------------------
    s30 = deck.add_blank_slide()
    deck.add_header(s30, "Penutup & Rencana Kerja", "Jadwal Pelaksanaan Riset 4 Bulan & Target Luaran",
                    "Roadmap Efektif di Bolabot (September - Desember 2026) dan Sesi Diskusi Tanya Jawab")

    # Left: Gantt Chart Table
    headers_gc = ["Tahapan Kegiatan Riset", "B1 (Sep)", "B2 (Okt)", "B3 (Nov)", "B4 (Des)"]
    rows_gc = [
        ["Desain Rangkaian Hardware, Casing 3D & Skematik", "[ X ]", "[   ]", "[   ]", "[   ]"],
        ["Kalibrasi Kumparan Helmholtz & Sensor TMR ALT023", "[ X ]", "[   ]", "[   ]", "[   ]"],
        ["Green Synthesis Fe3O4 Kelor & Elektrospinning PVA", "[   ]", "[ X ]", "[   ]", "[   ]"],
        ["Curing Termal 130 C & Karakterisasi Nanofiber ADH", "[   ]", "[ X ]", "[   ]", "[   ]"],
        ["Uji Larutan Formalin Bertingkat & Sampel Bakso", "[   ]", "[   ]", "[ X ]", "[   ]"],
        ["Ekstraksi 5 Fitur Sinyal & Pembentukan Dataset", "[   ]", "[   ]", "[ X ]", "[   ]"],
        ["Pelatihan & Komparasi Model SVM vs QSVC (Qiskit)", "[   ]", "[   ]", "[   ]", "[ X ]"],
        ["Deployment Model ke Raspberry Pi 5 & Draf Skripsi", "[   ]", "[   ]", "[   ]", "[ X ]"]
    ]
    deck.add_table(s30, Inches(0.8), Inches(1.55), Inches(6.8), Inches(3.6), headers_gc, rows_gc,
                   col_widths=[Inches(3.6), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.8)])

    # Right: Target Luaran
    deck.add_card(s30, Inches(7.9), Inches(1.55), Inches(4.633), Inches(3.6))
    tb30_r = s30.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.1), Inches(3.2))
    tf30_r = tb30_r.text_frame
    tf30_r.word_wrap = True
    deck.add_card_header(tf30_r, "Target Luaran Wajib & Tambahan", "Output Ilmiah", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf30_r, "Publikasi Ilmiah:", "1 Artikel pada Prosiding Internasional terindeks Scopus (IEEE / AIP) atau Jurnal Nasional Terakreditasi SINTA 2.", pt_size=9.5)
    deck.add_bullet_item(tf30_r, "Prototipe Instrumen Fisik:", "Unit instrumen biosensor TMR portabel terintegrasi casing 3D siap uji.", pt_size=9.5)
    deck.add_bullet_item(tf30_r, "Karya Ilmiah Akhir:", "Dokumen Skripsi lengkap Sarjana Fisika UIN Sunan Gunung Djati Bandung.", pt_size=9.5)

    # Bottom Full Width Thank You Card
    deck.add_card(s30, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.4), bg_color=COLOR_NAVY_DARK, border_color=COLOR_BLUE_ACCENT)
    tb30_b = s30.shapes.add_textbox(Inches(1.05), Inches(5.45), Inches(11.2), Inches(1.2))
    tf30_b = tb30_b.text_frame
    tf30_b.word_wrap = True
    p30_th = tf30_b.paragraphs[0]
    p30_th.text = "TERIMA KASIH ATAS PERHATIAN BAPAK/IBU DOSEN PENGUJI DAN PEMBIMBING"
    p30_th.font.name = FONT_FAMILY
    p30_th.font.bold = True
    p30_th.font.size = Pt(13)
    p30_th.font.color.rgb = COLOR_CARD_FILL
    p30_th.alignment = PP_ALIGN.CENTER
    p30_th.space_after = Pt(4)

    p30_sub = tf30_b.add_paragraph()
    p30_sub.text = "Mohon Arahan, Masukan, dan Saran demi Kesempurnaan Pelaksanaan Tugas Akhir Ini | Sesi Tanya Jawab Dibuka"
    p30_sub.font.name = FONT_FAMILY
    p30_sub.font.size = Pt(10)
    p30_sub.font.color.rgb = COLOR_LIGHT_BLUE
    p30_sub.alignment = PP_ALIGN.CENTER

    deck.add_footer(s30, 30)

    # --------------------------------------------------------------------------
    # SAVE FILE
    # --------------------------------------------------------------------------
    deck.save()

if __name__ == "__main__":
    build_presentation()
