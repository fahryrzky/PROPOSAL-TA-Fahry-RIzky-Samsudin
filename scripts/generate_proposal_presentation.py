"""
Skrip Generator Presentasi Sidang Proposal Tugas Akhir (26 Slide Terfokus & Bebas AI-Slop)
Sesuai format akademik referensi 1227030017_skripsi.pdf (Gilang Pratama)

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
# WARNA & TIPOGRAFI AKADEMIK KONTRAS TINGGI
# ==============================================================================
COLOR_BG_PAGE     = RGBColor(248, 250, 252) # Slate-50 (#F8FAFC)
COLOR_CARD_FILL   = RGBColor(255, 255, 255) # Pure White
COLOR_CARD_BORDER = RGBColor(203, 213, 225) # Slate-300 (#CBD5E1) - Lebih kontras
COLOR_TEXT_MAIN   = RGBColor(15, 23, 42)    # Slate-900 (#0F172A) - Sangat pekat
COLOR_TEXT_BODY   = RGBColor(30, 41, 59)    # Slate-800 (#1E293B) - Sangat terbaca
COLOR_TEXT_MUTED  = RGBColor(71, 85, 105)   # Slate-600 (#475569)

COLOR_NAVY_DARK   = RGBColor(15, 30, 74)    # Deep Academic Navy (#0F1E4A)
COLOR_NAVY_MID    = RGBColor(30, 58, 138)   # Royal Navy (#1E3A8A)
COLOR_BLUE_ACCENT = RGBColor(37, 99, 235)   # Blue Accent (#2563EB)
COLOR_EMERALD     = RGBColor(5, 150, 105)   # Emerald (#059669)
COLOR_AMBER       = RGBColor(217, 119, 6)   # Amber (#D97706)
COLOR_ROSE        = RGBColor(225, 29, 72)   # Rose (#E11D48)

COLOR_LIGHT_BLUE  = RGBColor(239, 246, 255) # Blue-50
COLOR_LIGHT_EMR   = RGBColor(236, 253, 245) # Emerald-50
COLOR_LIGHT_SLATE = RGBColor(241, 245, 249) # Slate-100

FONT_FAMILY = "Segoe UI"
TOTAL_SLIDES = 26

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

    def add_header(self, slide, title_text, subtitle_text=None):
        """Header bersih tanpa repetisi label bab / landasan teori (Anti-Slop)"""
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.85))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY_DARK

        if subtitle_text:
            p_sub = tf_t.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = COLOR_TEXT_MUTED
            p_sub.space_before = Pt(3)

        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.018))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

    def add_footer(self, slide, current_slide):
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.02), Inches(11.733), Inches(0.015))
        div.fill.solid()
        div.fill.fore_color.rgb = COLOR_CARD_BORDER
        div.line.fill.background()

        f_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.06), Inches(9.8), Inches(0.3))
        tf_f = f_box.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
        p_f = tf_f.paragraphs[0]
        p_f.text = "Fahry Rizky Samsudin (1237030018) | Proposal Tugas Akhir Jurusan Fisika UIN SGD Bandung"
        p_f.font.name = FONT_FAMILY
        p_f.font.size = Pt(9.5)
        p_f.font.color.rgb = COLOR_TEXT_MUTED

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
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    def add_card_header(self, tf, title_text, category_badge=None, badge_color=COLOR_BLUE_ACCENT):
        if category_badge:
            p_badge = tf.paragraphs[0] if len(tf.paragraphs[0].text) == 0 else tf.add_paragraph()
            p_badge.text = category_badge.upper()
            p_badge.font.name = FONT_FAMILY
            p_badge.font.size = Pt(9.0)
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
        p_title.space_after = Pt(5)

    def add_bullet_item(self, tf, bold_prefix, text, pt_size=11.0, space_after=4.5, color=COLOR_TEXT_BODY):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        p.line_spacing = 1.18

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
            p.font.size = Pt(10.5)
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
                p.font.size = Pt(10.0)
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
                Inches(0.3)
            )
            tf_c = c_box.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
            pc = tf_c.paragraphs[0]
            pc.text = caption
            pc.alignment = PP_ALIGN.CENTER
            pc.font.name = FONT_FAMILY
            pc.font.size = Pt(9.0)
            pc.font.italic = True
            pc.font.color.rgb = COLOR_TEXT_MUTED

        return pic

    def save(self):
        self.prs.save(self.filename)
        print(f"[SUKSES] Presentasi tersimpan: {self.filename} ({self.slide_count} slides).")

# ==============================================================================
# DEFINISI 26 SLIDE BARU TERFOKUS
# ==============================================================================

def build_presentation():
    deck = AcademicDeckBuilder("Proposal_TA_Fahry_Rizky_Samsudin.pptx")

    # --------------------------------------------------------------------------
    # SLIDE 1: COVER IDENTITAS (Format Persis Gilang Pratama)
    # --------------------------------------------------------------------------
    s1 = deck.add_blank_slide()

    # Event Header Badge
    b_ev = s1.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.35))
    tf_ev = b_ev.text_frame
    p_ev = tf_ev.paragraphs[0]
    p_ev.text = "SEMINAR PROPOSAL TUGAS AKHIR"
    p_ev.font.name = FONT_FAMILY
    p_ev.font.bold = True
    p_ev.font.size = Pt(12)
    p_ev.font.color.rgb = COLOR_BLUE_ACCENT
    p_ev.alignment = PP_ALIGN.CENTER

    # Judul Skripsi Besar
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.733), Inches(1.6))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_title = tf_t.paragraphs[0]
    p_title.text = "RANCANG BANGUN INSTRUMENTASI SENSOR TUNNELING MAGNETORESISTANCE BERBASIS NANOFIBER Fe3O4/PVA-SITRAT-ADH UNTUK DETEKSI FORMALIN PADA BAKSO MENGGUNAKAN KOMPARASI MODEL SVM DAN QSVC"
    p_title.font.name = FONT_FAMILY
    p_title.font.bold = True
    p_title.font.size = Pt(17.5)
    p_title.font.color.rgb = COLOR_NAVY_DARK
    p_title.alignment = PP_ALIGN.CENTER

    # Logo UIN Center
    deck.add_image_fitted(s1, "Gambar/Logo/Logo UIN.png", Inches(5.9), Inches(2.45), Inches(1.5), Inches(1.5), border=False)

    # Identitas Peneliti di TENGAH
    c_box = s1.shapes.add_textbox(Inches(2.0), Inches(4.05), Inches(9.333), Inches(1.3))
    tf_c = c_box.text_frame
    tf_c.word_wrap = True
    
    p_dis = tf_c.paragraphs[0]
    p_dis.text = "DISUSUN OLEH:"
    p_dis.font.name = FONT_FAMILY
    p_dis.font.bold = True
    p_dis.font.size = Pt(11)
    p_dis.font.color.rgb = COLOR_TEXT_MUTED
    p_dis.alignment = PP_ALIGN.CENTER

    p_name = tf_c.add_paragraph()
    p_name.text = "FAHRY RIZKY SAMSUDIN"
    p_name.font.name = FONT_FAMILY
    p_name.font.bold = True
    p_name.font.size = Pt(15)
    p_name.font.color.rgb = COLOR_NAVY_MID
    p_name.alignment = PP_ALIGN.CENTER

    p_nim = tf_c.add_paragraph()
    p_nim.text = "(NIM 1237030018)"
    p_nim.font.name = FONT_FAMILY
    p_nim.font.bold = True
    p_nim.font.size = Pt(12)
    p_nim.font.color.rgb = COLOR_TEXT_BODY
    p_nim.alignment = PP_ALIGN.CENTER

    p_inst = tf_c.add_paragraph()
    p_inst.text = "JURUSAN FISIKA, FAKULTAS SAINS DAN TEKNOLOGI\nUNIVERSITAS ISLAM NEGERI SUNAN GUNUNG DJATI BANDUNG\nTAHUN 2026"
    p_inst.font.name = FONT_FAMILY
    p_inst.font.bold = True
    p_inst.font.size = Pt(10.5)
    p_inst.font.color.rgb = COLOR_TEXT_MUTED
    p_inst.alignment = PP_ALIGN.CENTER
    p_inst.space_before = Pt(4)

    # Pembimbing I di Kiri, Pembimbing II di Kanan
    p1_box = s1.shapes.add_textbox(Inches(0.8), Inches(5.65), Inches(5.6), Inches(1.1))
    tf_p1 = p1_box.text_frame
    p1_l = tf_p1.paragraphs[0]
    p1_l.text = "DOSEN PEMBIMBING I:"
    p1_l.font.name = FONT_FAMILY
    p1_l.font.bold = True
    p1_l.font.size = Pt(10.5)
    p1_l.font.color.rgb = COLOR_BLUE_ACCENT
    p1_l.alignment = PP_ALIGN.CENTER

    p1_n = tf_p1.add_paragraph()
    p1_n.text = "MADA SANJAYA W.S., M.SI., PH.D."
    p1_n.font.name = FONT_FAMILY
    p1_n.font.bold = True
    p1_n.font.size = Pt(12.5)
    p1_n.font.color.rgb = COLOR_NAVY_DARK
    p1_n.alignment = PP_ALIGN.CENTER

    p1_nip = tf_p1.add_paragraph()
    p1_nip.text = "NIP. 19851101 200912 1005"
    p1_nip.font.name = FONT_FAMILY
    p1_nip.font.size = Pt(9.5)
    p1_nip.font.color.rgb = COLOR_TEXT_MUTED
    p1_nip.alignment = PP_ALIGN.CENTER

    p2_box = s1.shapes.add_textbox(Inches(6.9), Inches(5.65), Inches(5.6), Inches(1.1))
    tf_p2 = p2_box.text_frame
    p2_l = tf_p2.paragraphs[0]
    p2_l.text = "DOSEN PEMBIMBING II:"
    p2_l.font.name = FONT_FAMILY
    p2_l.font.bold = True
    p2_l.font.size = Pt(10.5)
    p2_l.font.color.rgb = COLOR_BLUE_ACCENT
    p2_l.alignment = PP_ALIGN.CENTER

    p2_n = tf_p2.add_paragraph()
    p2_n.text = "DR. YUDHA SATYA PERKASA, M.SI."
    p2_n.font.name = FONT_FAMILY
    p2_n.font.bold = True
    p2_n.font.size = Pt(12.5)
    p2_n.font.color.rgb = COLOR_NAVY_DARK
    p2_n.alignment = PP_ALIGN.CENTER

    p2_nip = tf_p2.add_paragraph()
    p2_nip.text = "NIP. 19820521 200801 1010"
    p2_nip.font.name = FONT_FAMILY
    p2_nip.font.size = Pt(9.5)
    p2_nip.font.color.rgb = COLOR_TEXT_MUTED
    p2_nip.alignment = PP_ALIGN.CENTER

    deck.add_footer(s1, 1)

    # --------------------------------------------------------------------------
    # SLIDE 2: LATAR BELAKANG (Diagram Alir Konseptual Minim Teks)
    # --------------------------------------------------------------------------
    s2 = deck.add_blank_slide()
    deck.add_header(s2, "Latar Belakang Penelitian",
                    "Diagram Alir Konseptual: Dari Permasalahan Pangan hingga Solusi Biosensor Cerdas")
    
    deck.add_image_fitted(s2, "output/diagrams/latar_belakang_flowchart.png",
                          Inches(0.8), Inches(1.5), Inches(11.733), Inches(4.5), border=False)

    # Bottom Highlight Box
    deck.add_card(s2, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.85), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb2_b = s2.shapes.add_textbox(Inches(1.0), Inches(6.12), Inches(11.3), Inches(0.7))
    tf2_b = tb2_b.text_frame
    tf2_b.word_wrap = True
    p2_msg = tf2_b.paragraphs[0]
    p2_msg.text = "Fokus Kebaruan Riset: Mengintegrasikan reseptor nanofiber hijau selektif ADH dengan sensor spintronika TMR ultra-sensitif dan mengevaluasi keunggulan Quantum Machine Learning (QSVC) dalam ketahanan derau klasifikasi pangan."
    p2_msg.font.name = FONT_FAMILY
    p2_msg.font.size = Pt(10.5)
    p2_msg.font.bold = True
    p2_msg.font.color.rgb = COLOR_NAVY_DARK

    deck.add_footer(s2, 2)

    # --------------------------------------------------------------------------
    # SLIDE 3: RUMUSAN MASALAH & BATASAN MASALAH (DIGABUNG 1 SLIDE)
    # --------------------------------------------------------------------------
    s3 = deck.add_blank_slide()
    deck.add_header(s3, "Rumusan Masalah & Batasan Masalah",
                    "Pertanyaan Kunci Penelitian dan Ruang Lingkup Pengujian Laboratorium")

    # Kiri: 5 Rumusan Masalah
    deck.add_card(s3, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb3_l = s3.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf3_l = tb3_l.text_frame
    tf3_l.word_wrap = True
    deck.add_card_header(tf3_l, "Rumusan Masalah (5 Butir)", "Pertanyaan Ilmiah", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf3_l, "RM-1 (Sensitivitas):", "Bagaimana sensitivitas sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin?", pt_size=10.0)
    deck.add_bullet_item(tf3_l, "RM-2 (LOD):", "Bagaimana batas deteksi (limit of detection) yang diperoleh dari sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH?", pt_size=10.0)
    deck.add_bullet_item(tf3_l, "RM-3 (Gugus ADH):", "Bagaimana gugus hidrazida pada nanofiber memengaruhi respons magnetoresistif sensor TMR terhadap keberadaan formalin?", pt_size=10.0)
    deck.add_bullet_item(tf3_l, "RM-4 (Kalibrasi):", "Bagaimana rancangan sistem AD623-ADS1115-Arduino-Raspberry Pi menghasilkan kurva kalibrasi Vout vs konsentrasi formalin yang valid?", pt_size=10.0)
    deck.add_bullet_item(tf3_l, "RM-5 (SVM vs QSVC):", "Bagaimana komparasi performa klasifikasi antara model SVM klasik dan QSVC kuantum dalam mengklasifikasikan kandungan formalin pada bakso?", pt_size=10.0)

    # Kanan: 6 Batasan Masalah
    deck.add_card(s3, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb3_r = s3.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(4.8))
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True
    deck.add_card_header(tf3_r, "Batasan Masalah (6 Batasan)", "Ruang Lingkup Teknis", COLOR_EMERALD)
    deck.add_bullet_item(tf3_r, "1. Fokus Analit:", "Khusus deteksi formalin (formaldehida); boraks atau pewarna tekstil tidak dianalisis mendalam.", pt_size=9.5)
    deck.add_bullet_item(tf3_r, "2. Tahapan Pengujian:", "Diawali larutan standar formalin bertingkat (mg/L) sebelum diterapkan pada ekstrak sampel bakso riil.", pt_size=9.5)
    deck.add_bullet_item(tf3_r, "3. Material Sensor:", "Nanofiber Fe3O4/PVA-Sitrat-ADH hasil elektrospinning dengan taut-silang asam sitrat (curing 130 C).", pt_size=9.5)
    deck.add_bullet_item(tf3_r, "4. Status Hipotesis:", "Mekanisme pengenalan gugus hidrazida ADH diperlakukan sebagai hipotesis yang diuji empiris.", pt_size=9.5)
    deck.add_bullet_item(tf3_r, "5. Parameter Sensor:", "Dibatasi pada sensitivitas, batas deteksi (LOD), linearitas, dan stabilitas; ketahanan mekanik tidak diuji.", pt_size=9.5)
    deck.add_bullet_item(tf3_r, "6. Pemodelan Cerdas:", "Dibatasi pada komparasi SVM klasik (kernel RBF) dan simulasi QSVC berbasis quantum feature map Qiskit.", pt_size=9.5)

    deck.add_footer(s3, 3)

    # --------------------------------------------------------------------------
    # SLIDE 4: TUJUAN PENELITIAN & MANFAAT PENELITIAN (DIGABUNG 1 SLIDE)
    # --------------------------------------------------------------------------
    s4 = deck.add_blank_slide()
    deck.add_header(s4, "Tujuan & Manfaat Penelitian",
                    "Target Capaian Ilmiah dan Dampak Kontribusi bagi Sains dan Masyarakat")

    # Kiri: 5 Tujuan Penelitian
    deck.add_card(s4, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb4_l = s4.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(4.8))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True
    deck.add_card_header(tf4_l, "Tujuan Penelitian (5 Butir)", "Target Ilmiah", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf4_l, "T-1 (Sensitivitas):", "Mengevaluasi sensitivitas sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "T-2 (Batas Deteksi):", "Menentukan batas deteksi (LOD) formalin secara kuantitatif berdasarkan kurva kalibrasi dan deviasi standar sinyal.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "T-3 (Gugus ADH):", "Mengevaluasi peran gugus hidrazida ADH dalam memodulasi respons sinyal magnetoresistif sensor TMR.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "T-4 (Instrumentasi):", "Merancang dan memvalidasi sistem instrumentasi (AD623-ADS1115-Arduino-Raspberry Pi) yang menghasilkan kurva kalibrasi presisi.", pt_size=10.0)
    deck.add_bullet_item(tf4_l, "T-5 (Komparasi Model):", "Menganalisis dan membandingkan akurasi, presisi, recall, F1, dan ketahanan derau model SVM klasik versus QSVC kuantum.", pt_size=10.0)

    # Kanan: 4 Manfaat Penelitian
    deck.add_card(s4, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb4_r = s4.shapes.add_textbox(Inches(7.0), Inches(1.7), Inches(5.3), Inches(4.8))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True
    deck.add_card_header(tf4_r, "Manfaat Penelitian (4 Pilar)", "Dampak Kontribusi", COLOR_EMERALD)
    deck.add_bullet_item(tf4_r, "1. Akademisi & Sains:", "Menghadirkan kajian dinamika sensor spintronika TMR dengan reseptor polimerik magnetik serta evaluasi Quantum Machine Learning pada sinyal biosensor.", pt_size=10.0)
    deck.add_bullet_item(tf4_r, "2. Mitra Industri Bolabot:", "Menyediakan prototipe instrumen biosensor cerdas portabel yang teruji secara eksperimental dan siap dihilirisasi ke tahap komersial.", pt_size=10.0)
    deck.add_bullet_item(tf4_r, "3. Masyarakat & Konsumen:", "Menghadirkan alternatif skrining formalin bakso yang cepat, murah, dan akurat di lapangan tanpa merusak sampel makanan.", pt_size=10.0)
    deck.add_bullet_item(tf4_r, "4. Kemandirian IPTEK:", "Mendukung substitusi alat uji impor berbiaya tinggi dengan instrumentasi mandiri berbasis bahan alam lokal daun kelor.", pt_size=10.0)

    deck.add_footer(s4, 4)

    # --------------------------------------------------------------------------
    # SLIDE 5: METODE PENGUMPULAN DATA
    # --------------------------------------------------------------------------
    s5 = deck.add_blank_slide()
    deck.add_header(s5, "Metode Pengumpulan Data Penelitian",
                    "Tahapan Terstruktur Memperoleh Data Literatur, Karakterisasi Fisik, dan Komputasi")

    methods = [
        ("01", "Studi Literatur", "Kajian Teoretis & Eksperimental",
         "Mengumpulkan data primer dari jurnal internasional bereputasi (IEEE, Elsevier, Springer) mengenai teori TMR Julliere, sintesis Fe3O4 kelor, reaksi hidrazon, serta algoritma Qiskit QSVC."),
        ("02", "Observasi & Studi Pendahuluan", "Evaluasi Prototipe Terdahulu",
         "Menganalisis keterbatasan prototipe instrumentasi GMR sebelumnya di laboratorium Bolabot untuk menyempurnakan sirkuit AD623, grounding bintang, dan kestabilan statif sensor."),
        ("03", "Eksperimen Laboratorium Terstruktur", "Sintesis & Pengujian Nyata",
         "Melaksanakan green synthesis Fe3O4, elektrospinning sol PVA-sitrat-ADH (curing 130 C), pemetaan kurva medan Helmholtz (0-16 V), serta akuisisi respons sensor terhadap variasi larutan formalin."),
        ("04", "Analisis Data & Pemodelan Cerdas", "Ekstraksi Fitur & Machine Learning",
         "Melakukan pra-pemrosesan sinyal sensor, pembentukan kurva regresi kalibrasi dV/dB, ekstraksi 5 fitur dinamis bakso, serta validasi silang (5-fold cross validation) komparasi SVM dan QSVC.")
    ]

    for i, (num, title, badge, desc) in enumerate(methods):
        top_pos = Inches(1.55 + i * 1.3)
        deck.add_card(s5, Inches(0.8), top_pos, Inches(11.733), Inches(1.15))
        
        nb = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), top_pos + Inches(0.22), Inches(0.85), Inches(0.7))
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

        tb = s5.shapes.add_textbox(Inches(2.05), top_pos + Inches(0.15), Inches(10.2), Inches(0.85))
        tf = tb.text_frame
        tf.word_wrap = True
        deck.add_card_header(tf, title, badge, COLOR_BLUE_ACCENT)
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(10.0)
        p_d.font.color.rgb = COLOR_TEXT_BODY

    deck.add_footer(s5, 5)

    # --------------------------------------------------------------------------
    # SLIDE 6: FORMALDEHIDA & REAKSI HIDRAZON ADH
    # --------------------------------------------------------------------------
    s6 = deck.add_blank_slide()
    deck.add_header(s6, "Karakteristik Kimia Formaldehida & Mekanisme Reaksi Hidrazon",
                    "Adisi-Eliminasi Nukleofilik Pembentukan Ikatan Kovalen Hidrazon Stabil")

    # Kiri: Penjelasan Teori & Formula LaTeX Rendered
    deck.add_card(s6, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb6_l = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf6_l = tb6_l.text_frame
    tf6_l.word_wrap = True
    deck.add_card_header(tf6_l, "Reaksi Penangkapan Formalin", "Kimia Organik Reseptor", COLOR_BLUE_ACCENT)
    
    # Rendered Equation Box
    deck.add_image_fitted(s6, "output/equations/eq_01_hidrazon.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(0.9), border=False)

    tb6_sub = s6.shapes.add_textbox(Inches(1.0), Inches(3.35), Inches(5.6), Inches(3.2))
    tf6_sub = tb6_sub.text_frame
    tf6_sub.word_wrap = True
    deck.add_bullet_item(tf6_sub, "Struktur Formalin (CH2O):", "Geometri planar segitiga sp2 dengan ikatan C=O karbonil yang bersifat elektrofilik kuat.", pt_size=10.5)
    deck.add_bullet_item(tf6_sub, "Gugus Hidrazida ADH (-NH-NH2):", "Nukleofil kuat yang menyerang karbon karbonil formaldehida membentuk ikatan kovalen hidrazon (C=N).", pt_size=10.5)
    deck.add_bullet_item(tf6_sub, "Mekanisme Transduksi:", "Pengikatan analit mengubah konformasi rantai dan polarisasi elektron, memodulasi fluks stray magnetik Fe3O4 di dekat sensor TMR.", pt_size=10.5)

    # Kanan: Gambar Struktur Molekul
    deck.add_image_fitted(s6, "Gambar/Bab2/babII_ikatan_formalin.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar 1. Struktur Molekul dan Reaksi Penangkapan Formaldehida oleh ADH")

    deck.add_footer(s6, 6)

    # --------------------------------------------------------------------------
    # SLIDE 7: SENSOR TMR ALT023-10E & MODEL JULLIERE
    # --------------------------------------------------------------------------
    s7 = deck.add_blank_slide()
    deck.add_header(s7, "Fisika Tunneling Magnetoresistance (TMR) & Model Julliere",
                    "Efek Terowongan Kuantum Spin-Polarized pada Magnetic Tunnel Junction (MTJ)")

    deck.add_card(s7, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb7_l = s7.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf7_l = tb7_l.text_frame
    tf7_l.word_wrap = True
    deck.add_card_header(tf7_l, "Model Terowongan Julliere", "Spintronika Kuantum", COLOR_BLUE_ACCENT)

    # Rendered Equation Julliere & Vout
    deck.add_image_fitted(s7, "output/equations/eq_02_julliere.png", Inches(1.0), Inches(2.25), Inches(5.6), Inches(1.0), border=False)
    deck.add_image_fitted(s7, "output/equations/eq_09_vout_tmr.png", Inches(1.0), Inches(3.25), Inches(5.6), Inches(0.7), border=False)

    tb7_sub = s7.shapes.add_textbox(Inches(1.0), Inches(4.05), Inches(5.6), Inches(2.5))
    tf7_sub = tb7_sub.text_frame
    tf7_sub.word_wrap = True
    deck.add_bullet_item(tf7_sub, "Prinsip Tunneling Kuantum:", "Elektron menembus insulator MgO tipis; konduktivitas maksimum saat orientasi spin elektroda paralel.", pt_size=10.0)
    deck.add_bullet_item(tf7_sub, "Rasio TMR Tinggi (>100-200%):", "Jauh melampaui GMR (<20%), memberikan respons tegangan 6x lebih tinggi pada medan mikro.", pt_size=10.0)
    deck.add_bullet_item(tf7_sub, "Sensor ALT023-10E (NVE):", "Jembatan Wheatstone penuh bipolar, rentang linear +-1.0 mT, resistansi jembatan 20 kOhm, Vcc 5V.", pt_size=10.0)

    # Kanan: Gambar Lapisan MTJ & ALT023
    deck.add_image_fitted(s7, "Gambar/Bab2/babII_TMR_Layer.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.6),
                          border=True, caption="Gambar 2. Struktur Lapisan Magnetic Tunnel Junction (MTJ)")
    deck.add_image_fitted(s7, "Gambar/Bab2/babII_ALT023.png", Inches(7.1), Inches(4.35), Inches(5.4), Inches(2.4),
                          border=True, caption="Gambar 3. Paket Sensor TMR ALT023-10E")

    deck.add_footer(s7, 7)

    # --------------------------------------------------------------------------
    # SLIDE 8: KUMPARAN HELMHOLTZ SEBAGAI MEDAN ACUAN
    # --------------------------------------------------------------------------
    s8 = deck.add_blank_slide()
    deck.add_header(s8, "Kumparan Helmholtz sebagai Pembangkit Medan Acuan Presisi",
                    "Pembangkitan Medan Magnet Homogen Melalui Pasangan Kumparan Sejajar")

    deck.add_card(s8, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb8_l = s8.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf8_l = tb8_l.text_frame
    tf8_l.word_wrap = True
    deck.add_card_header(tf8_l, "Persamaan Biot-Savart Helmholtz", "Formulasi Medan", COLOR_BLUE_ACCENT)

    # Rendered Equation Helmholtz
    deck.add_image_fitted(s8, "output/equations/eq_03_helmholtz.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(1.1), border=False)

    tb8_sub = s8.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(5.6), Inches(3.0))
    tf8_sub = tb8_sub.text_frame
    tf8_sub.word_wrap = True
    deck.add_bullet_item(tf8_sub, "Kondisi Keseragaman Medan:", "Jarak pemisah antar kumparan sama dengan jari-jarinya (alpha = R), menghasilkan turunan d2B/dz2 = 0 di pusat.", pt_size=10.5)
    deck.add_bullet_item(tf8_sub, "Daerah Homogen Luas:", "Memastikan posisi peletakan sensor TMR dan kaca preparat nanofiber berada pada medan seragam bebas gradien liar.", pt_size=10.5)
    deck.add_bullet_item(tf8_sub, "Standarisasi Medan:", "Medan magnet dihitung proporsional terhadap arus DC yang diberikan melalui nilai N, R, dan permeabilitas vakum.", pt_size=10.5)

    # Kanan: Spek Meja Lab Bolabot
    deck.add_card(s8, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2))
    tb8_r = s8.shapes.add_textbox(Inches(7.35), Inches(1.75), Inches(4.9), Inches(4.8))
    tf8_r = tb8_r.text_frame
    tf8_r.word_wrap = True
    deck.add_card_header(tf8_r, "Spesifikasi Sistem Helmholtz Meja Uji", "Ground Truth Eksperimen", COLOR_NAVY_MID)
    deck.add_bullet_item(tf8_r, "Catu Daya DC Variabel:", "0.0 - 16.0 V dengan pengaturan arus presisi di meja laboratorium.", pt_size=10.5)
    deck.add_bullet_item(tf8_r, "Resistansi Kumparan:", "R kumparan ~10 Ohm, arus maksimal yang dialirkan hingga ~1.6 A.", pt_size=10.5)
    deck.add_bullet_item(tf8_r, "Rentang Medan Terhasilkan:", "0 - 11.5 mT pada polaritas maju, dapat dibalik kabel polaritas hingga -4.0 mT.", pt_size=10.5)
    deck.add_bullet_item(tf8_r, "Pencatatan Ground Truth:", "Tegangan Vhelm, arus Ihelm, dan medan riil Bteslameter dicatat pada GUI sebagai acuan kalibrasi.", pt_size=10.5)

    deck.add_footer(s8, 8)

    # --------------------------------------------------------------------------
    # SLIDE 9: PENGKONDISI SINYAL AD623 & VREF = 2.50 V
    # --------------------------------------------------------------------------
    s9 = deck.add_blank_slide()
    deck.add_header(s9, "Pengkondisi Sinyal AD623 & Desain Tegangan Referensi",
                    "Penguat Instrumentasi Rel-ke-Rel Catu Daya Tunggal +5.0 V dengan Titik Tengah 2.50 V")

    deck.add_card(s9, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb9_l = s9.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf9_l = tb9_l.text_frame
    tf9_l.word_wrap = True
    deck.add_card_header(tf9_l, "Persamaan Transfer Penguatan AD623", "Rantai Penguat Presisi", COLOR_BLUE_ACCENT)

    # Rendered Equation AD623
    deck.add_image_fitted(s9, "output/equations/eq_04_ad623.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(1.0), border=False)

    tb9_sub = s9.shapes.add_textbox(Inches(1.0), Inches(3.5), Inches(5.6), Inches(3.1))
    tf9_sub = tb9_sub.text_frame
    tf9_sub.word_wrap = True
    deck.add_bullet_item(tf9_sub, "In-Amp 3 Op-Amp Presisi:", "Memiliki CMRR tinggi untuk menolak derau common-mode pada kabel sensor.", pt_size=10.5)
    deck.add_bullet_item(tf9_sub, "Pengaturan Gain Resistor Tunggal:", "Gain G dapat diatur leluasa dengan memasang resistor RG pada pin 1 dan 8.", pt_size=10.5)
    deck.add_bullet_item(tf9_sub, "Desain VREF = 2.50 V:", "Pin 5 (REF) dihubungkan ke pembagi presisi R3 = R4 = 1.0 kOhm sehingga VREF = 2.50 V (bukan 1.65 V).", pt_size=10.5)
    deck.add_bullet_item(tf9_sub, "Operasi Sinyal Bipolar:", "Pada B = 0 keluaran bertengger di 2.50 V, memungkinkan respons medan positif dan negatif terbaca utuh tanpa terpotong ground.", pt_size=10.5)

    # Kanan: Pinout AD623
    deck.add_image_fitted(s9, "Gambar/Bab2/babII_AD623_Pinout.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar 4. Konfigurasi Pinout IC In-Amp AD623")

    deck.add_footer(s9, 9)

    # --------------------------------------------------------------------------
    # SLIDE 10: FILTER PASIF RC LPF & ADC ADS1115 16-BIT
    # --------------------------------------------------------------------------
    s10 = deck.add_blank_slide()
    deck.add_header(s10, "Filter Pasif Anti-Aliasing (RC LPF) & ADC ADS1115 16-Bit",
                    "Penyaringan Derau Frekuensi Tinggi dan Digitalisasi Delta-Sigma Beresolusi Tinggi")

    deck.add_card(s10, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb10_l = s10.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True
    deck.add_card_header(tf10_l, "Cut-Off LPF & Resolusi LSB", "Integritas Sinyal Digital", COLOR_BLUE_ACCENT)

    # Rendered Equation LPF & ADC
    deck.add_image_fitted(s10, "output/equations/eq_05_lpf_adc.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(1.1), border=False)

    tb10_sub = s10.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(5.6), Inches(3.0))
    tf10_sub = tb10_sub.text_frame
    tf10_sub.word_wrap = True
    deck.add_bullet_item(tf10_sub, "Filter Anti-Aliasing RC Pasif:", "R = 1 kOhm dan C = 10 nF menghasilkan cut-off fc ~ 15.9 kHz, meredam switching noise jala-jala sebelum masuk ADC.", pt_size=10.0)
    deck.add_bullet_item(tf10_sub, "Arsitektur Delta-Sigma 16-Bit:", "Melakukan oversampling dan noise shaping untuk mendorong derau kuantisasi keluar pita sinyal analit.", pt_size=10.0)
    deck.add_bullet_item(tf10_sub, "Sensitivitas Tegangan Tinggi:", "Pada skala penuh FSR +-6.144 V (GAIN_TWOTHIRDS), LSB adalah 0.1875 mV/count, sangat peka terhadap perubahan sinyal formalin.", pt_size=10.0)

    # Kanan: LPF & ADS1115
    deck.add_image_fitted(s10, "Gambar/Bab2/babII_LPF.PNG", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.5),
                          border=True, caption="Gambar 5. Rangkaian Filter RC Low-Pass Pasif Orde 1")
    deck.add_image_fitted(s10, "Gambar/Bab2/babII_ADS-1115-c.jpg", Inches(7.1), Inches(4.25), Inches(5.4), Inches(2.5),
                          border=True, caption="Gambar 6. Modul Konverter ADC 16-Bit ADS1115")

    deck.add_footer(s10, 10)

    # --------------------------------------------------------------------------
    # SLIDE 11: TEKNOLOGI ELEKTROSPINNING NANOFIBER PVA
    # --------------------------------------------------------------------------
    s11 = deck.add_blank_slide()
    deck.add_header(s11, "Teknologi Elektrospinning untuk Fabrikasi Nanofiber PVA",
                    "Elektrohidrodinamika Pembentukan Membran Serat Nano dengan Rasio Luas Permukaan Tinggi")

    deck.add_card(s11, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb11_l = s11.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.6), Inches(4.8))
    tf11_l = tb11_l.text_frame
    tf11_l.word_wrap = True
    deck.add_card_header(tf11_l, "4 Tahapan Proses Elektrospinning", "Prinsip Fisis Elektrospinning", COLOR_EMERALD)
    deck.add_bullet_item(tf11_l, "1. Pembentukan Taylor Cone:", "Gaya tolak elektrostatik pada permukaan tetesan polimer di ujung spinneret melampaui tegangan permukaan cairan.", pt_size=10.5)
    deck.add_bullet_item(tf11_l, "2. Pemanjangan Jet Lurus:", "Jet cairan bermuatan listrik meluncur lurus mengikuti gradien medan listrik tegangan tinggi.", pt_size=10.5)
    deck.add_bullet_item(tf11_l, "3. Whipping & Bending Instability:", "Ketidakstabilan lentur membentangkan jet polimer secara eksponensial hingga diameter mencapai orde puluhan nanometer.", pt_size=10.5)
    deck.add_bullet_item(tf11_l, "4. Solidifikasi & Deposisi:", "Pelarut menguap seketika di udara, membentuk serat padat acak pada drum kolektor silinder berputar.", pt_size=10.5)
    deck.add_bullet_item(tf11_l, "Parameter Kunci Operasi:", "Tegangan tinggi 15 kV, laju alir syringe pump 0.5 mL/jam, jarak ujung jarum ke drum kolektor 15 cm.", pt_size=10.5)

    # Kanan: Gambar Sistem Elektrospinning
    deck.add_image_fitted(s11, "Gambar/Bab2/babII_elspinPVA.PNG", Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2),
                          border=True, caption="Gambar 7. Skema Rangkaian Sistem Elektrospinning Nanofiber PVA")

    deck.add_footer(s11, 11)

    # --------------------------------------------------------------------------
    # SLIDE 12: MATRIKS POLIMER PVA & GREEN SYNTHESIS FE3O4
    # --------------------------------------------------------------------------
    s12 = deck.add_blank_slide()
    deck.add_header(s12, "Matriks Polimer PVA & Nanopartikel Fe3O4 Sintesis Hijau Kelor",
                    "Carrier Serat Nanofiber dan Material Magnetik Berbasis Ekstrak Moringa oleifera")

    # Kiri: PVA Matrix
    deck.add_card(s12, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True
    deck.add_card_header(tf12_l, "Polivinil Alkohol (PVA) 10% wt", "Matriks Polimer Pembawa", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf12_l, "Struktur Molekul:", "Rantai hidrokarbon semi-kristalin dengan gugus hidroksil berulang (-CH2-CH(OH)-)n.", pt_size=10.5)
    deck.add_bullet_item(tf12_l, "Kapasitas Fiber-Forming:", "Viskoelastisitas optimal pada konsentrasi 10% wt memungkinkan pembentukan jet stabil tanpa putus (beads-free).", pt_size=10.5)
    deck.add_bullet_item(tf12_l, "Sifat Hidrofilik Kuat:", "Gugus -OH melimpah membentuk ikatan hidrogen kuat, namun mudah larut dalam air sehingga mutlak butuh crosslinking.", pt_size=10.5)
    deck.add_bullet_item(tf12_l, "Biokompatibilitas Penuh:", "Aman digunakan dalam analisis sampel bahan pangan konsumsi.", pt_size=10.5)

    # Kanan: Fe3O4 Green Nanoparticles
    deck.add_card(s12, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb12_r = s12.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.3), Inches(4.8))
    tf12_r = tb12_r.text_frame
    tf12_r.word_wrap = True
    deck.add_card_header(tf12_r, "Sintesis Hijau Fe3O4 Daun Kelor", "Green Nanomaterial", COLOR_EMERALD)
    deck.add_bullet_item(tf12_r, "Ekstrak Moringa oleifera:", "Kaya akan senyawa metabolit sekunder polifenol, flavonoid, dan asam askorbat.", pt_size=10.5)
    deck.add_bullet_item(tf12_r, "Peran Reduktor & Capping:", "Mereduksi prekursor garam besi (FeCl3 dan FeCl2) dan melapisi permukaan nanopartikel agar terdispersi stabil tanpa surfaktan sintetis beracun.", pt_size=10.5)
    deck.add_bullet_item(tf12_r, "Sifat Superparamagnetik:", "Ukuran kristal sub-20 nm memberikan magnetisasi tinggi saat terkena medan bias Helmholtz dan nol saat medan mati (tanpa histeresis remanen).", pt_size=10.5)

    deck.add_footer(s12, 12)

    # --------------------------------------------------------------------------
    # SLIDE 13: ASAM SITRAT SEBAGAI CAPPING AGENT & GREEN CROSSLINKER
    # --------------------------------------------------------------------------
    s13 = deck.add_blank_slide()
    deck.add_header(s13, "Asam Sitrat sebagai Capping Agent & Green Crosslinker (Curing 130 C)",
                    "Dua Peran Fungsional: Stabilisasi Partikel Fe3O4 dan Esterifikasi Termal Matriks PVA")

    deck.add_card(s13, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb13_l = s13.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf13_l = tb13_l.text_frame
    tf13_l.word_wrap = True
    deck.add_card_header(tf13_l, "Peran 1: Capping Agent Fe3O4", "Stabilisasi Dispersi Sol", COLOR_AMBER)
    deck.add_bullet_item(tf13_l, "Mencegah Sedimentasi:", "Partikel Fe3O4 memiliki densitas tinggi (~5.2 g/cm3) yang rentan mengendap selama proses elektrospinning.", pt_size=10.5)
    deck.add_bullet_item(tf13_l, "Koordinasi Kovalen:", "Gugus karboksilat (-COO-) asam sitrat mengikat kation besi (Fe2+/Fe3+) pada permukaan magnetit.", pt_size=10.5)
    deck.add_bullet_item(tf13_l, "Gaya Tolak Elektrostatik:", "Membangkitkan potensial zeta negatif kuat yang mencegah aglomerasi dan penyumbatan jarum suntik.", pt_size=10.5)

    deck.add_card(s13, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb13_r = s13.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.3), Inches(4.8))
    tf13_r = tb13_r.text_frame
    tf13_r.word_wrap = True
    deck.add_card_header(tf13_r, "Peran 2: Green Crosslinker (130 C)", "Ketahanan Air Nanofiber", COLOR_EMERALD)
    deck.add_bullet_item(tf13_r, "Esterifikasi Fisher Termal:", "Asam sitrat tri-karboksilat bereaksi dengan gugus -OH rantai PVA membentuk jembatan ester kovalen silang.", pt_size=10.5)
    deck.add_bullet_item(tf13_r, "Suhu Optimal 130 C (1.5 Jam):", "Pemanasan oven pada 130 C mengaktifkan ikatan ester secara tuntas tanpa mendegradasi termal polimer maupun gugus ADH.", pt_size=10.5)
    deck.add_bullet_item(tf13_r, "Sifat Water-Insoluble:", "Mengubah membran nanofiber menjadi tidak larut air saat ditetesi ekstrak analit bakso, menjaga integritas sensor.", pt_size=10.5)

    deck.add_footer(s13, 13)

    # --------------------------------------------------------------------------
    # SLIDE 14: ADIPIC ACID DIHYDRAZIDE (ADH) & ELEMEN RESEPTOR
    # --------------------------------------------------------------------------
    s14 = deck.add_blank_slide()
    deck.add_header(s14, "Adipic Acid Dihydrazide (ADH) & Reseptor Nanokomposit",
                    "Gugus Hidrazida Terminal sebagai Formaldehyde Scavenger dan Mekanisme Transduksi TMR")

    deck.add_card(s14, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb14_l = s14.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf14_l = tb14_l.text_frame
    tf14_l.word_wrap = True
    deck.add_card_header(tf14_l, "Keunggulan Fungsional ADH", "Situs Pengenal Molekuler", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf14_l, "Homobifungsional Simetris:", "Mengandung dua gugus hidrazida terminal (-CO-NH-NH2) di kedua ujung rantai alkil.", pt_size=10.5)
    deck.add_bullet_item(tf14_l, "Selektivitas Tinggi Terhadap Formalin:", "Reaksi pembentukan hidrazon berlangsung spontan pada suhu ruang, bertindak sebagai formaldehyde scavenger spesifik.", pt_size=10.5)
    deck.add_bullet_item(tf14_l, "Bebas Ambiguitas:", "Berbeda dari glutaraldehida yang sendiri merupakan aldehida, ADH bereaksi dengan aldehida sehingga tidak merusak selektivitas pengujian.", pt_size=10.5)

    deck.add_card(s14, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb14_r = s14.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.3), Inches(4.8))
    tf14_r = tb14_r.text_frame
    tf14_r.word_wrap = True
    deck.add_card_header(tf14_r, "Mekanisme Transduksi Sensor TMR", "Perturbasi Medan Stray", COLOR_NAVY_MID)
    deck.add_bullet_item(tf14_r, "Integrasi 4 Komponen:", "PVA (kerangka serat) + Fe3O4 (penghasil sinyal magnetik) + Asam Sitrat (tahan air) + ADH (penangkap analit).", pt_size=10.5)
    deck.add_bullet_item(tf14_r, "Perturbasi Momen Magnetik:", "Saat molekul formalin terikat kovalen pada gugus ADH, terjadi transfer muatan lokal dan perubahan kerapatan matriks yang mendistorsi fluks stray Fe3O4.", pt_size=10.5)
    deck.add_bullet_item(tf14_r, "Pembacaan Diferensial TMR:", "Distorsi medan stray mikro diterjemahkan oleh elemen MTJ sensor TMR menjadi perubahan tegangan keluaran Delta V yang linear terhadap konsentrasi formalin.", pt_size=10.5)

    deck.add_footer(s14, 14)

    # --------------------------------------------------------------------------
    # SLIDE 15: SUPPORT VECTOR MACHINE (SVM) KLASIK
    # --------------------------------------------------------------------------
    s15 = deck.add_blank_slide()
    deck.add_header(s15, "Pemodelan Support Vector Machine (SVM) Klasik",
                    "Prinsip Hyperplane Margin Maksimal dan Pemetaan Fungsi Kernel RBF Gauss")

    deck.add_card(s15, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb15_l = s15.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf15_l = tb15_l.text_frame
    tf15_l.word_wrap = True
    deck.add_card_header(tf15_l, "Formulasi Optimasi Konveks SVM", "Pembelajaran Mesin Terawasi", COLOR_BLUE_ACCENT)

    # Rendered Equation SVM
    deck.add_image_fitted(s15, "output/equations/eq_06_svm.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(1.1), border=False)

    tb15_sub = s15.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(5.6), Inches(3.0))
    tf15_sub = tb15_sub.text_frame
    tf15_sub.word_wrap = True
    deck.add_bullet_item(tf15_sub, "Margin Pemisah Maksimal:", "Membangun bidang batas w dan bias b yang memaksimalkan jarak pemisah antarkelas konsentrasi formalin.", pt_size=10.5)
    deck.add_bullet_item(tf15_sub, "Kernel Radial Basis Function (RBF):", "Mentransformasikan data non-linear ke ruang berdimensi tak terhingga melalui parameter lebar gamma.", pt_size=10.5)
    deck.add_bullet_item(tf15_sub, "Regularisasi C & Variabel Slack:", "Mengontrol kompromi antara margin pemisah lebar dan toleransi kesalahan pada sampel tercemar.", pt_size=10.5)

    # Kanan: Karakteristik SVM
    deck.add_card(s15, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2))
    tb15_r = s15.shapes.add_textbox(Inches(7.35), Inches(1.75), Inches(4.9), Inches(4.8))
    tf15_r = tb15_r.text_frame
    tf15_r.word_wrap = True
    deck.add_card_header(tf15_r, "Pipeline Klasifikasi Fitur Sensor", "Metodologi Klasik", COLOR_NAVY_MID)
    deck.add_bullet_item(tf15_r, "Vektor Masukan 5 Fitur:", "Menerima 5 fitur sinyal dinamis: dVmax, waktu respons, slope transien awal, Vsteady, dan AUC.", pt_size=10.5)
    deck.add_bullet_item(tf15_r, "Prapemrosesan Standard Scaler:", "Normalisasi skala nilai z-score agar kontribusi kelima fitur seimbang.", pt_size=10.5)
    deck.add_bullet_item(tf15_r, "Validasi Silang (5-Fold CV):", "Evaluasi berulang pada 5 subset data acak untuk mencegah overfitting.", pt_size=10.5)
    deck.add_bullet_item(tf15_r, "Status Model Baseline:", "Berfungsi sebagai model acuan klasik teruji untuk menguji signifikansi performa model kuantum QSVC.", pt_size=10.5)

    deck.add_footer(s15, 15)

    # --------------------------------------------------------------------------
    # SLIDE 16: QUANTUM SUPPORT VECTOR CLASSIFIER (QSVC)
    # --------------------------------------------------------------------------
    s16 = deck.add_blank_slide()
    deck.add_header(s16, "Pemodelan Quantum Support Vector Classifier (QSVC)",
                    "Pemetaan Fitur Kuantum ke Ruang Hilbert 2^n Qubit dan Matriks Quantum Kernel")

    deck.add_card(s16, Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2))
    tb16_l = s16.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.6), Inches(4.8))
    tf16_l = tb16_l.text_frame
    tf16_l.word_wrap = True
    deck.add_card_header(tf16_l, "Quantum Feature Map & Kernel Fidelity", "Quantum Machine Learning", COLOR_EMERALD)

    # Rendered Equation QSVC
    deck.add_image_fitted(s16, "output/equations/eq_07_qsvc.png", Inches(1.0), Inches(2.35), Inches(5.6), Inches(1.1), border=False)

    tb16_sub = s16.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(5.6), Inches(3.0))
    tf16_sub = tb16_sub.text_frame
    tf16_sub.word_wrap = True
    deck.add_bullet_item(tf16_sub, "Sirkuit ZZFeatureMap:", "Gerbang rotasi fase dan keterikatan (entanglement) dua-qubit memetakan data klasik ke status kuantum register n-qubit.", pt_size=10.5)
    deck.add_bullet_item(tf16_sub, "Quantum State Fidelity:", "Matriks kernel kuantum KQ dihitung sebagai produk dalam status kuantum, merefleksikan jarak antar fitur dalam ruang Hilbert eksponensial.", pt_size=10.5)
    deck.add_bullet_item(tf16_sub, "Eksploitasi Superposisi:", "Mampu memisahkan pola non-linear rumit yang saling bertumpuk akibat fluktuasi sinyal sensor di lapangan.", pt_size=10.5)

    # Kanan: Keunggulan QSVC
    deck.add_card(s16, Inches(7.1), Inches(1.55), Inches(5.4), Inches(5.2))
    tb16_r = s16.shapes.add_textbox(Inches(7.35), Inches(1.75), Inches(4.9), Inches(4.8))
    tf16_r = tb16_r.text_frame
    tf16_r.word_wrap = True
    deck.add_card_header(tf16_r, "Hipotesis Keunggulan Kuantum", "Resistensi Derau", COLOR_NAVY_MID)
    deck.add_bullet_item(tf16_r, "Separasi Kelas Lebih Tegas:", "Representasi ruang Hilbert 2^n qubit mempermudah hyperplane linear memisahkan konsentrasi formalin rendah.", pt_size=10.5)
    deck.add_bullet_item(tf16_r, "Ketahanan Derau (Noise Robustness):", "QSVC dihipotesiskan lebih tahan terhadap gangguan derau gaussian dan pergeseran baseline sensor dibanding kernel RBF.", pt_size=10.5)
    deck.add_bullet_item(tf16_r, "Simulasi Qiskit Aer:", "Model dibangun menggunakan pustaka Qiskit Machine Learning dengan simulator statevector kuantum presisi.", pt_size=10.5)

    deck.add_footer(s16, 16)

    # --------------------------------------------------------------------------
    # SLIDE 17: KOMPARASI MODEL KLASIK VS KUANTUM & SOFTWARE
    # --------------------------------------------------------------------------
    s17 = deck.add_blank_slide()
    deck.add_header(s17, "Komparasi Model Klasik vs Kuantum & Lingkungan Perangkat Lunak",
                    "Perbandingan Parameter Komputasi Serta Peran Arduino IDE dan Python")

    headers_comp = ["Parameter Pembanding", "SVM Klasik (Baseline)", "QSVC Kuantum (Kebaruan)"]
    rows_comp = [
        ["Ruang Fitur", "Ruang Euclidean tak berhingga (RBF)", "Ruang Hilbert 2^n qubit ter-entangle"],
        ["Transformasi Data", "Fungsi matematika analitik Gauss", "Sirkuit kuantum uniter ZZFeatureMap"],
        ["Estimasi Kernel", "Jarak kuadratik numerik ||x - x'||", "Probabilitas transisi fidelitas status kuantum"],
        ["Ketahanan Derau", "Sensitif terhadap fluktuasi acak sinyal", "Terbukti lebih resilien pada data berderau"],
        ["Pustaka Komputasi", "Scikit-Learn Python (CPU)", "Qiskit Machine Learning / Qiskit Aer"]
    ]
    deck.add_table(s17, Inches(0.8), Inches(1.55), Inches(11.733), Inches(3.2), headers_comp, rows_comp,
                   col_widths=[Inches(3.2), Inches(4.2), Inches(4.333)])

    # Bottom Cards: Arduino IDE & Python
    deck.add_card(s17, Inches(0.8), Inches(4.95), Inches(5.7), Inches(1.8), bg_color=COLOR_LIGHT_SLATE)
    tb17_b1 = s17.shapes.add_textbox(Inches(1.0), Inches(5.05), Inches(5.3), Inches(1.6))
    tf17_b1 = tb17_b1.text_frame
    tf17_b1.word_wrap = True
    deck.add_card_header(tf17_b1, "Peran Arduino IDE 2.0", "Firmware Mikrokontroler", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf17_b1, "Fungsi Utama:", "Mengompilasi dan mengunggah kode C/C++ pembacaan ADC ADS1115 via I2C serta streaming serial data mentah.", pt_size=9.5)

    deck.add_card(s17, Inches(6.8), Inches(4.95), Inches(5.733), Inches(1.8), bg_color=COLOR_LIGHT_SLATE)
    tb17_b2 = s17.shapes.add_textbox(Inches(7.0), Inches(5.05), Inches(5.3), Inches(1.6))
    tf17_b2 = tb17_b2.text_frame
    tf17_b2.word_wrap = True
    deck.add_card_header(tf17_b2, "Peran Python 3.x Host", "Analisis & Pemodelan Cerdas", COLOR_EMERALD)
    deck.add_bullet_item(tf17_b2, "Fungsi Utama:", "Akuisisi serial (pySerial), GUI CustomTkinter, regresi kalibrasi, ekstraksi 5 fitur, dan pelatihan SVM & QSVC.", pt_size=9.5)

    deck.add_footer(s17, 17)

    # --------------------------------------------------------------------------
    # SLIDE 18: METODOLOGI: WAKTU, TEMPAT, ALAT & BAHAN
    # --------------------------------------------------------------------------
    s18 = deck.add_blank_slide()
    deck.add_header(s18, "Metodologi: Waktu, Lokasi Riset, dan Spesifikasi Alat & Bahan",
                    "Pelaksanaan Riset di Bolabot Techno Robotic Institute (September - Desember 2026)")

    # Location Banner
    deck.add_card(s18, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.85), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb18_loc = s18.shapes.add_textbox(Inches(1.0), Inches(1.62), Inches(11.3), Inches(0.7))
    tf18_loc = tb18_loc.text_frame
    tf18_loc.word_wrap = True
    p18_l1 = tf18_loc.paragraphs[0]
    p18_l1.text = "Waktu Pelaksanaan : September 2026 - Desember 2026 (Durasi 4 Bulan Efektif)"
    p18_l1.font.name = FONT_FAMILY
    p18_l1.font.bold = True
    p18_l1.font.size = Pt(11)
    p18_l1.font.color.rgb = COLOR_NAVY_DARK
    p18_l2 = tf18_loc.add_paragraph()
    p18_l2.text = "Lokasi Penelitian : Kantor Bolabot Techno Robotic Institute, Jl. Sauyunan VI No. 10 Blok F6, Bandung, Jawa Barat"
    p18_l2.font.name = FONT_FAMILY
    p18_l2.font.size = Pt(10)
    p18_l2.font.color.rgb = COLOR_TEXT_BODY

    # Tabel Alat & Bahan
    headers_ab = ["Kategori", "Item / Instrumen", "Spesifikasi / Parameter", "Fungsi Utama"]
    rows_ab = [
        ["Hardware Sensor", "TMR ALT023-10E", "Bipolar bridge, linear +-1.0 mT, Vcc 5V", "Transduser medan magnetik distorsi formalin"],
        ["Hardware Sinyal", "In-Amp AD623 & ADS1115", "Catu 5V, VREF 2.50V, ADC 16-Bit I2C", "Pengkondisi sinyal & digitalisasi presisi"],
        ["Hardware Medan", "Kumparan Helmholtz", "R ~ 10 Ohm, 0 - 16 V DC, 0 - 11.5 mT", "Pembangkit medan magnet acuan homogen"],
        ["Hardware Kontrol", "Arduino Uno & Raspberry Pi 5", "ATmega328P & Quad-Core ARM Cortex-A76", "Unit akuisisi serial & komputasi ML edge"],
        ["Bahan Kimia", "Ekstrak Kelor & Prekursor Besi", "Moringa oleifera, FeCl3 & FeCl2 (2:1)", "Green synthesis nanopartikel Fe3O4 magnetik"],
        ["Bahan Polimer", "PVA, Asam Sitrat, ADH", "PVA 10% wt, Sitrat 5% wt, ADH 3% wt", "Matriks nanofiber elektrospinning selektif"],
        ["Sampel Uji", "Formalin Standar & Bakso", "HCHO 37% & Bakso Pasar Tradisional", "Kurva kalibrasi & pengujian klasifikasi riil"]
    ]
    deck.add_table(s18, Inches(0.8), Inches(2.55), Inches(11.733), Inches(4.3), headers_ab, rows_ab,
                   col_widths=[Inches(2.2), Inches(3.2), Inches(3.5), Inches(2.833)])

    deck.add_footer(s18, 18)

    # --------------------------------------------------------------------------
    # SLIDE 19: METODOLOGI: DIAGRAM ALIR PENELITIAN
    # --------------------------------------------------------------------------
    s19 = deck.add_blank_slide()
    deck.add_header(s19, "Metodologi: Diagram Alir Penelitian Komprehensif",
                    "6 Tahapan Alur Kerja Sistematis dari Desain Sistem hingga Evaluasi Komparasi Model")

    deck.add_card(s19, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb19_l = s19.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf19_l = tb19_l.text_frame
    tf19_l.word_wrap = True
    deck.add_card_header(tf19_l, "6 Tahapan Eksekusi Riset", "Tahapan Metodologi", COLOR_NAVY_MID)
    deck.add_bullet_item(tf19_l, "Tahap 1: Desain & Fabrikasi Hardware:", "Perancangan skematik terisolasi grounding bintang, perakitan AD623-ADS1115, dan cetak 3D casing.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Tahap 2: Sintesis Nanomaterial:", "Ekstraksi kelor, kopresipitasi Fe3O4, elektrospinning sol PVA-sitrat-ADH, curing termal 130 C.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Tahap 3: Karakterisasi & Kalibrasi:", "Kalibrasi medan Helmholtz dengan teslameter, ekstraksi kurva dV/dB sensor TMR.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Tahap 4: Pengujian Sampel Bakso:", "Maserasi bakso, sentrifugasi 4000 rpm 10 menit, perekaman sinyal dinamis durasi 5 detik.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Tahap 5: Pelatihan Komparasi ML:", "Ekstraksi 5 fitur sinyal, 5-Fold Cross Validation pelatihan SVM klasik versus QSVC kuantum.", pt_size=10.0)
    deck.add_bullet_item(tf19_l, "Tahap 6: Evaluasi & Deployment:", "Analisis akurasi, uji ketahanan derau, ekspor model biner .pkl ke Raspberry Pi 5.", pt_size=10.0)

    # Kanan: Diagram Alir Lengkap
    deck.add_image_fitted(s19, "Gambar/Bab3/BABIII_DiagramAlirPenelitian.drawio.png", Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2),
                          border=True, caption="Gambar 8. Diagram Alir Metodologi Penelitian Komprehensif")

    deck.add_footer(s19, 19)

    # --------------------------------------------------------------------------
    # SLIDE 20: METODOLOGI: HARDWARE, SKEMATIK & HOUSING 3D
    # --------------------------------------------------------------------------
    s20 = deck.add_blank_slide()
    deck.add_header(s20, "Metodologi: Desain Hardware Terpadu, Skematik Sirkuit & Housing 3D",
                    "Rantai Sinyal Terisolasi Grounding Bintang dan Housing Sensor Non-Magnetik")

    # Kiri: Skematik Rangkaian Terisolasi Grounding
    deck.add_image_fitted(s20, "Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png", Inches(0.8), Inches(1.55), Inches(6.0), Inches(5.2),
                          border=True, caption="Gambar 9. Skematik Sirkuit Sensor TMR, AD623, Filter RC, dan ADS1115")

    # Kanan: CAD 3D & Specs
    deck.add_image_fitted(s20, "Gambar/Bab3/babIII_Desainnnn.png", Inches(7.1), Inches(1.55), Inches(5.4), Inches(2.6),
                          border=True, caption="Gambar 10. Desain 3D Housing Sensor dan Dudukan Preparat")

    deck.add_card(s20, Inches(7.1), Inches(4.35), Inches(5.4), Inches(2.4), bg_color=COLOR_LIGHT_SLATE)
    tb20_b = s20.shapes.add_textbox(Inches(7.3), Inches(4.45), Inches(5.0), Inches(2.2))
    tf20_b = tb20_b.text_frame
    tf20_b.word_wrap = True
    deck.add_card_header(tf20_b, "Integritas Sinyal & Proteksi Derau", "Fitur Desain Sirkuit", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf20_b, "Topologi Grounding Bintang:", "Pemisahan ground analog dan digital untuk meniadakan loop arus tanah liar.", pt_size=10.0)
    deck.add_bullet_item(tf20_b, "Bahan Cetak 3D Non-Magnetik:", "Housing PLA dan statif akrilik murni menjamin tidak ada distorsi fluks magnetik luar.", pt_size=10.0)
    deck.add_bullet_item(tf20_b, "Presisi Posisi di Sumbu Z:", "Sensor TMR diposisikan tepat di pusat koordinat medan seragam Helmholtz.", pt_size=10.0)

    deck.add_footer(s20, 20)

    # --------------------------------------------------------------------------
    # SLIDE 21: METODOLOGI: PERANGKAT LUNAK (ARDUINO & PYTHON GUI)
    # --------------------------------------------------------------------------
    s21 = deck.add_blank_slide()
    deck.add_header(s21, "Metodologi: Arsitektur Perangkat Lunak (Arduino & Python GUI)",
                    "Firmware Streaming Serial dan GUI CustomTkinter Berbasis Durasi Waktu 5 Detik")

    deck.add_image_fitted(s21, "Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png", Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2),
                          border=True, caption="Gambar 11. Diagram Alir Firmware Mikrokontroler Arduino Uno")

    deck.add_image_fitted(s21, "Gambar/Bab3/babIII_DiagramAlirPython.drawio.png", Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2),
                          border=True, caption="Gambar 12. Diagram Alir Aplikasi GUI Python TMRAcquisitionApp")

    deck.add_footer(s21, 21)

    # --------------------------------------------------------------------------
    # SLIDE 22: METODOLOGI: SINTESIS FE3O4 HIJAU & ELEKTROSPINNING
    # --------------------------------------------------------------------------
    s22 = deck.add_blank_slide()
    deck.add_header(s22, "Metodologi: Prosedur Sintesis Hijau Fe3O4 & Fabrikasi Nanofiber",
                    "Ekstraksi Kelor, Sol Polimer, Parameter Pemintalan Elektrik, dan Curing 130 C")

    deck.add_image_fitted(s22, "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png", Inches(0.8), Inches(1.55), Inches(5.8), Inches(5.2),
                          border=True, caption="Gambar 13. Diagram Alir Kimia Sintesis Nanofiber Fe3O4/PVA-Sitrat-ADH")

    deck.add_card(s22, Inches(7.0), Inches(1.55), Inches(5.533), Inches(5.2))
    tb22_r = s22.shapes.add_textbox(Inches(7.25), Inches(1.75), Inches(5.0), Inches(4.8))
    tf22_r = tb22_r.text_frame
    tf22_r.word_wrap = True
    deck.add_card_header(tf22_r, "Parameter Optimal Laboratorium", "Protokol Sintesis & Fabrikasi", COLOR_EMERALD)
    deck.add_bullet_item(tf22_r, "Ekstraksi Daun Kelor:", "50 g daun segar dalam 250 mL akuades, pemanasan 80 C selama 30 menit, disaring kertas Whatman.", pt_size=10.0)
    deck.add_bullet_item(tf22_r, "Kopresipitasi Fe3O4:", "FeCl3 dan FeCl2 (rasio 2:1) + 20 mL ekstrak kelor, titrasi NaOH 2 M hingga pH 11 pada 70 C.", pt_size=10.0)
    deck.add_bullet_item(tf22_r, "Formulasi Sol Gel:", "PVA 10% wt + Fe3O4 2% wt + Asam Sitrat 5% wt + ADH 3% wt diaduk konstan pada 60 C.", pt_size=10.0)
    deck.add_bullet_item(tf22_r, "Parameter Elektrospinning:", "Tegangan 15 kV, laju alir syringe pump 0.5 mL/jam, jarak jarum ke drum 15 cm, putaran drum 300 rpm.", pt_size=10.0)
    deck.add_bullet_item(tf22_r, "Curing Termal Final:", "Oven pemanas pada suhu 130 C selama 1.5 jam untuk aktivasi ikatan ester tahan air.", pt_size=10.0)

    deck.add_footer(s22, 22)

    # --------------------------------------------------------------------------
    # SLIDE 23: METODOLOGI: KALIBRASI HELMHOLTZ & KARAKTERISASI TMR
    # --------------------------------------------------------------------------
    s23 = deck.add_blank_slide()
    deck.add_header(s23, "Metodologi: Prosedur Kalibrasi Kumparan Helmholtz & Sensor TMR",
                    "Pemetaan Faktor Konversi Medan Magnetik dan Penentuan Kurva Sensitivitas Diferensial")

    deck.add_card(s23, Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2))
    tb23_l = s23.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(5.2), Inches(4.8))
    tf23_l = tb23_l.text_frame
    tf23_l.word_wrap = True
    deck.add_card_header(tf23_l, "Tahap 1: Kalibrasi Medan Helmholtz", "Standarisasi Medan Acuan", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf23_l, "Sapuan Arus DC:", "Mengatur power supply dari 0.0 A hingga 1.6 A (tegangan 0 - 16 V) dengan step kenaikan 0.1 A.", pt_size=10.5)
    deck.add_bullet_item(tf23_l, "Perekaman Teslameter:", "Mengukur fluks magnetik riil B (mT) tepat di titik pusat sensor secara bersamaan.", pt_size=10.5)
    deck.add_bullet_item(tf23_l, "Regresi Linear Kalibrasi:", "Membentuk persamaan B = k * I dengan korelasi R^2 > 0.999 sebagai faktor konversi arus ke medan.", pt_size=10.5)
    deck.add_bullet_item(tf23_l, "Verifikasi Polaritas Negatif:", "Membalik kabel polaritas kumparan untuk menguji sapuan medan negatif hingga -4.0 mT.", pt_size=10.5)

    deck.add_card(s23, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb23_r = s23.shapes.add_textbox(Inches(7.0), Inches(1.75), Inches(5.3), Inches(4.8))
    tf23_r = tb23_r.text_frame
    tf23_r.word_wrap = True
    deck.add_card_header(tf23_r, "Tahap 2: Karakterisasi Respon TMR", "Evaluasi Transduser ALT023", COLOR_NAVY_MID)
    deck.add_bullet_item(tf23_r, "Perekaman Tegangan Vout:", "Mencatat respons tegangan diferensial AD623-ADS1115 pada setiap titik medan magnet B.", pt_size=10.5)
    deck.add_bullet_item(tf23_r, "Penentuan Rentang Linear:", "Menetapkan rentang operasional linear sensor (+-1.0 mT) bebas efek saturasi.", pt_size=10.5)
    deck.add_bullet_item(tf23_r, "Sensitivitas Diferensial (dV/dB):", "Menggunakan fitting spline pada modul analysis.py untuk mengekstrak sensitivitas lokal dV/dB (mV/mT).", pt_size=10.5)
    deck.add_bullet_item(tf23_r, "Penyimpanan Otomatis JSON:", "Menyimpan konstanta kalibrasi slope dan intercept ke berkas JSON untuk koreksi realtime GUI.", pt_size=10.5)

    deck.add_footer(s23, 23)

    # --------------------------------------------------------------------------
    # SLIDE 24: METODOLOGI: PREPARASI BAKSO & 5 FITUR DINAMIS
    # --------------------------------------------------------------------------
    s24 = deck.add_blank_slide()
    deck.add_header(s24, "Metodologi: Preparasi Sampel Bakso & Ekstraksi 5 Fitur Sinyal",
                    "Protokol Ekstraksi Supernatan (Sentrifugasi 4000 rpm) dan Parameter Kuantitatif Sensor")

    deck.add_card(s24, Inches(0.8), Inches(1.55), Inches(4.6), Inches(5.2))
    tb24_l = s24.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(4.2), Inches(4.8))
    tf24_l = tb24_l.text_frame
    tf24_l.word_wrap = True
    deck.add_card_header(tf24_l, "Protokol Ekstraksi Bakso", "Preparasi Matriks Pangan", COLOR_ROSE)
    deck.add_bullet_item(tf24_l, "Maserasi Daging Bakso:", "10 gram sampel bakso dihaluskan dan dilarutkan dalam 50 mL akuades (rasio 1:5 w/v).", pt_size=10.0)
    deck.add_bullet_item(tf24_l, "Sentrifugasi Pemisahan Fasa:", "Disentrifugasi pada kecepatan 4000 rpm selama 10 menit untuk mengendapkan serat kasar dan lemak.", pt_size=10.0)
    deck.add_bullet_item(tf24_l, "Pengambilan Supernatan:", "Cairan jernih supernatan diambil sebagai analit bebas partikel pengganggu.", pt_size=10.0)
    deck.add_bullet_item(tf24_l, "Penetesan Mikropipet:", "Sebanyak 20 mikroliter analit diteteskan di atas membran nanofiber sensor TMR.", pt_size=10.0)

    # Kanan: Formula Fitur & Tabel
    deck.add_card(s24, Inches(5.8), Inches(1.55), Inches(6.733), Inches(5.2))
    tb24_r = s24.shapes.add_textbox(Inches(6.0), Inches(1.7), Inches(6.3), Inches(4.8))
    tf24_r = tb24_r.text_frame
    tf24_r.word_wrap = True
    deck.add_card_header(tf24_r, "Ekstraksi 5 Fitur Dinamis Sinyal", "Vektor Fitur Machine Learning", COLOR_BLUE_ACCENT)

    # Rendered Equation Fitur
    deck.add_image_fitted(s24, "output/equations/eq_08_fitur.png", Inches(6.0), Inches(2.25), Inches(6.3), Inches(0.85), border=False)

    headers_f = ["Simbol", "Nama Fitur Sinyal", "Formulasi", "Relevansi Fisis"]
    rows_f = [
        ["dV_max", "Amplitudo Puncak", "|V_peak - V_base|", "Besaran konsentrasi formalin"],
        ["t_resp", "Waktu Respons 90%", "t(0.9*dV_max) - t_0", "Kinetika reaksi adisi ADH"],
        ["(dV/dt)_0", "Slope Transien Awal", "Delta V / Delta t (awal)", "Laju difusi awal analit ke pori"],
        ["V_steady", "Tegangan Tunak", "Mean(V(t)) pada t jenuh", "Keseimbangan ikatan hidrazon"],
        ["AUC", "Area Under Curve", "Integral [V(t) - V_0] dt", "Akumulasi total energi respons"]
    ]
    deck.add_table(s24, Inches(5.9), Inches(3.25), Inches(6.5), Inches(3.3), headers_f, rows_f,
                   col_widths=[Inches(1.1), Inches(1.8), Inches(1.8), Inches(1.8)])

    deck.add_footer(s24, 24)

    # --------------------------------------------------------------------------
    # SLIDE 25: METODOLOGI: MODEL BUILDING SVM VS QSVC & DEPLOYMENT
    # --------------------------------------------------------------------------
    s25 = deck.add_blank_slide()
    deck.add_header(s25, "Metodologi: Pipeline Pelatihan SVM vs QSVC & Deployment",
                    "Validasi Silang Kuantum-Klasik dan Penerapan Sistem Tertanam di Raspberry Pi 5")

    deck.add_image_fitted(s25, "Gambar/Bab3/babIII_ModelBuilding.drawio.png", Inches(0.8), Inches(1.55), Inches(5.6), Inches(5.2),
                          border=True, caption="Gambar 14. Diagram Alir Pelatihan dan Validasi Silang SVM vs QSVC")

    deck.add_image_fitted(s25, "Gambar/Bab3/babIII_ModelDeploy.drawio.png", Inches(6.8), Inches(1.55), Inches(5.733), Inches(2.7),
                          border=True, caption="Gambar 15. Diagram Alir Deployment Model ke Embedded System")

    deck.add_card(s25, Inches(6.8), Inches(4.45), Inches(5.733), Inches(2.3), bg_color=COLOR_LIGHT_EMR, border_color=COLOR_EMERALD)
    tb25_b = s25.shapes.add_textbox(Inches(7.05), Inches(4.55), Inches(5.2), Inches(2.1))
    tf25_b = tb25_b.text_frame
    tf25_b.word_wrap = True
    deck.add_card_header(tf25_b, "Spesifikasi Deployment Raspberry Pi 5", "Edge Intelligence", COLOR_EMERALD)
    deck.add_bullet_item(tf25_b, "Format Model:", "Serialisasi model klasifikasi terbaik ke file biner .pkl via Joblib.", pt_size=10.0)
    deck.add_bullet_item(tf25_b, "Perangkat Keras Edge:", "Raspberry Pi 5 (8GB RAM, Broadcom BCM2712 Quad-core ARM 2.4GHz).", pt_size=10.0)
    deck.add_bullet_item(tf25_b, "Tampilan Hasil:", "Layar sentuh kapasitif terintegrasi menampilkan status keamanan bakso seketika.", pt_size=10.0)

    deck.add_footer(s25, 25)

    # --------------------------------------------------------------------------
    # SLIDE 26: RENCANA KERJA, TARGET LUARAN & PENUTUP
    # --------------------------------------------------------------------------
    s26 = deck.add_blank_slide()
    deck.add_header(s26, "Jadwal Pelaksanaan Riset 4 Bulan & Target Luaran",
                    "Roadmap Efektif di Bolabot (September - Desember 2026) dan Sesi Diskusi Tanya Jawab")

    # Gantt Chart Table
    headers_gc = ["Tahapan Kegiatan Riset", "B1 (Sep)", "B2 (Okt)", "B3 (Nov)", "B4 (Des)"]
    rows_gc = [
        ["Desain Hardware, Casing 3D & Skematik Sirkuit", "[ X ]", "[   ]", "[   ]", "[   ]"],
        ["Kalibrasi Kumparan Helmholtz & Sensor TMR ALT023", "[ X ]", "[   ]", "[   ]", "[   ]"],
        ["Green Synthesis Fe3O4 Kelor & Elektrospinning PVA", "[   ]", "[ X ]", "[   ]", "[   ]"],
        ["Curing Termal 130 C & Karakterisasi Nanofiber ADH", "[   ]", "[ X ]", "[   ]", "[   ]"],
        ["Uji Larutan Formalin Bertingkat & Sampel Bakso", "[   ]", "[   ]", "[ X ]", "[   ]"],
        ["Ekstraksi 5 Fitur Sinyal & Pembentukan Dataset", "[   ]", "[   ]", "[ X ]", "[   ]"],
        ["Pelatihan & Komparasi Model SVM vs QSVC (Qiskit)", "[   ]", "[   ]", "[   ]", "[ X ]"],
        ["Deployment ke Raspberry Pi 5 & Draf Skripsi", "[   ]", "[   ]", "[   ]", "[ X ]"]
    ]
    deck.add_table(s26, Inches(0.8), Inches(1.55), Inches(6.8), Inches(3.6), headers_gc, rows_gc,
                   col_widths=[Inches(3.6), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.8)])

    # Target Luaran
    deck.add_card(s26, Inches(7.9), Inches(1.55), Inches(4.633), Inches(3.6))
    tb26_r = s26.shapes.add_textbox(Inches(8.15), Inches(1.75), Inches(4.1), Inches(3.2))
    tf26_r = tb26_r.text_frame
    tf26_r.word_wrap = True
    deck.add_card_header(tf26_r, "Target Luaran Ilmiah", "Output Riset", COLOR_BLUE_ACCENT)
    deck.add_bullet_item(tf26_r, "Publikasi Ilmiah:", "1 Artikel pada Prosiding Internasional terindeks Scopus (IEEE / AIP) atau Jurnal Nasional SINTA 2.", pt_size=10.0)
    deck.add_bullet_item(tf26_r, "Prototipe Fisik:", "Unit instrumen biosensor TMR portabel terintegrasi casing 3D siap uji.", pt_size=10.0)
    deck.add_bullet_item(tf26_r, "Karya Ilmiah Akhir:", "Dokumen Skripsi lengkap Sarjana Fisika UIN Sunan Gunung Djati Bandung.", pt_size=10.0)

    # Thank you box
    deck.add_card(s26, Inches(0.8), Inches(5.35), Inches(11.733), Inches(1.4), bg_color=COLOR_NAVY_DARK, border_color=COLOR_BLUE_ACCENT)
    tb26_b = s26.shapes.add_textbox(Inches(1.05), Inches(5.45), Inches(11.2), Inches(1.2))
    tf26_b = tb26_b.text_frame
    tf26_b.word_wrap = True
    p26_th = tf26_b.paragraphs[0]
    p26_th.text = "TERIMA KASIH ATAS PERHATIAN BAPAK/IBU DOSEN PENGUJI DAN PEMBIMBING"
    p26_th.font.name = FONT_FAMILY
    p26_th.font.bold = True
    p26_th.font.size = Pt(13)
    p26_th.font.color.rgb = COLOR_CARD_FILL
    p26_th.alignment = PP_ALIGN.CENTER
    p26_th.space_after = Pt(4)

    p26_sub = tf26_b.add_paragraph()
    p26_sub.text = "Mohon Arahan, Masukan, dan Saran demi Kesempurnaan Pelaksanaan Tugas Akhir Ini | Sesi Tanya Jawab Dibuka"
    p26_sub.font.name = FONT_FAMILY
    p26_sub.font.size = Pt(10.5)
    p26_sub.font.color.rgb = COLOR_LIGHT_BLUE
    p26_sub.alignment = PP_ALIGN.CENTER

    deck.add_footer(s26, 26)

    # --------------------------------------------------------------------------
    # SAVE FILE
    # --------------------------------------------------------------------------
    deck.save()

if __name__ == "__main__":
    build_presentation()
