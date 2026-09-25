"""
Skrip Generator Presentasi Sidang Proposal Tugas Akhir (22 Slide Lengkap, Padat & Bebas AI-Slop)
Sesuai format akademik referensi 1227030017_skripsi.pdf (Gilang Pratama)

Standar Mutu Presentasi:
1. Cover Autentik Gilang Pratama (Latar lab gelap cover_bg_gilang.png, logo pill UIN+Fisika, bingkai oranye tebal #f26522, judul gagah 19.5 pt, identitas resmi).
2. Penyelarasan Sempurna 4 Rumusan Masalah & 4 Tujuan Penelitian (Slide 3 & Slide 4) sesuai naskah proposal.
3. Slide 11 Baru: Matriks Perbandingan Penelitian Terdahulu (Wang 2021, Singhal 2024, Sun 2023, Gilang 2026, Fahry 2026).
4. Tipografi Besar Proyektor (Header 23 pt, Judul Kartu 16-17 pt, Bullet Teks 12.5-14.0 pt) agar terbaca jelas dari baris belakang ruang sidang.
5. MURNI 2 FLOWCHART per slide pada Slide 15 & Slide 19 tanpa teks perintang.
6. Seluruh 44 pustaka aktif naskah proposal tercantum secara rapi dan proporsional (Slide 20 & Slide 21).
7. Zero AI-Slop: Nol label kategori semu (4 Aspek), nol em-dash, nol kalimat klise AI.

Peneliti : Fahry Rizky Samsudin (NIM: 1237030018)
Jurusan  : Fisika, Fakultas Sains dan Teknologi, UIN Sunan Gunung Djati Bandung
Tahun    : 2026
"""

import os
import sys
import re
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
COLOR_CARD_BORDER = RGBColor(203, 213, 225) # Slate-300 (#CBD5E1) - Kontras tegas
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
TOTAL_SLIDES = 22

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
        """Header bersih tanpa repetisi label bab (Anti-Slop)"""
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.85))
        tf_t = t_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(23)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_NAVY_DARK

        if subtitle_text:
            p_sub = tf_t.add_paragraph()
            p_sub.text = subtitle_text
            p_sub.font.name = FONT_FAMILY
            p_sub.font.size = Pt(12.5)
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

        num_box = slide.shapes.add_textbox(Inches(10.8), Inches(7.06), Inches(1.733), Inches(0.3))
        tf_num = num_box.text_frame
        tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
        p_n = tf_num.paragraphs[0]
        p_n.text = f"{current_slide:02d} / {TOTAL_SLIDES:02d}"
        p_n.font.name = FONT_FAMILY
        p_n.font.size = Pt(9.5)
        p_n.font.bold = True
        p_n.font.color.rgb = COLOR_BLUE_ACCENT
        p_n.alignment = PP_ALIGN.RIGHT

    def add_card(self, slide, left, top, width, height, bg_color=COLOR_CARD_FILL, border_color=COLOR_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    def add_card_header(self, tf, title, category=None, accent_color=COLOR_NAVY_MID, title_size=17):
        p_t = tf.paragraphs[0] if len(tf.paragraphs[0].text) == 0 else tf.add_paragraph()
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(title_size)
        p_t.font.bold = True
        p_t.font.color.rgb = accent_color
        p_t.space_after = Pt(6)

    def add_bullet_item(self, tf, bold_prefix, text, pt_size=13.5, space_after=6.0, color=COLOR_TEXT_BODY):
        p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
        p.space_after = Pt(space_after)
        p.line_spacing = 1.25

        r_bullet = p.add_run()
        r_bullet.text = "\u2022 "
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
        if not os.path.exists(img_path):
            print(f"[PERINGATAN] Berkas gambar tidak ditemukan: {img_path}")
            return None

        im = Image.open(img_path)
        img_w_px, img_h_px = im.size
        img_aspect = img_w_px / img_h_px
        box_aspect = max_w / max_h

        if img_aspect > box_aspect:
            final_w = max_w
            final_h = max_w / img_aspect
        else:
            final_h = max_h
            final_w = max_h * img_aspect

        x_centered = left + (max_w - final_w) / 2
        y_centered = top + (max_h - final_h) / 2

        if border:
            card_border = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, max_w, max_h)
            card_border.fill.solid()
            card_border.fill.fore_color.rgb = COLOR_CARD_FILL
            card_border.line.color.rgb = COLOR_CARD_BORDER
            card_border.line.width = Pt(1.2)

        pic = slide.shapes.add_picture(img_path, x_centered, y_centered, width=final_w, height=final_h)

        if caption:
            cap_box = slide.shapes.add_textbox(left, top + max_h + Inches(0.04), max_w, Inches(0.28))
            tf_c = cap_box.text_frame
            tf_c.word_wrap = True
            tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
            p_c = tf_c.paragraphs[0]
            p_c.text = caption
            p_c.font.name = FONT_FAMILY
            p_c.font.size = Pt(8.5)
            p_c.font.color.rgb = COLOR_TEXT_MUTED
            p_c.alignment = PP_ALIGN.CENTER

        return pic

    def add_table(self, slide, left, top, width, height, headers, rows, col_widths=None):
        num_rows = len(rows) + 1
        num_cols = len(headers)
        table_shape = slide.shapes.add_table(num_rows, num_cols, left, top, width, height)
        table = table_shape.table

        if col_widths:
            for idx, w in enumerate(col_widths):
                table.columns[idx].width = w

        for col_idx, h_text in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.text = h_text
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_NAVY_MID
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.CENTER
                for r in p.runs:
                    r.font.name = FONT_FAMILY
                    r.font.bold = True
                    r.font.size = Pt(11.0)
                    r.font.color.rgb = RGBColor(255, 255, 255)

        for row_idx, r_data in enumerate(rows):
            is_even = (row_idx % 2 == 0)
            for col_idx, val in enumerate(r_data):
                cell = table.cell(row_idx + 1, col_idx)
                cell.text = str(val)
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_LIGHT_SLATE if is_even else COLOR_CARD_FILL
                for p in cell.text_frame.paragraphs:
                    if col_idx in [0]:
                        p.alignment = PP_ALIGN.LEFT
                    else:
                        p.alignment = PP_ALIGN.CENTER
                    for r in p.runs:
                        r.font.name = FONT_FAMILY
                        r.font.size = Pt(10.0)
                        r.font.color.rgb = COLOR_TEXT_BODY

        return table_shape

    def save(self):
        self.prs.save(self.filename)
        print(f"[SUKSES] Presentasi tersimpan: {self.filename} ({self.slide_count} slides).")


def build_presentation():
    deck = AcademicDeckBuilder("Proposal_TA_Fahry_Rizky_Samsudin.pptx")

    # --------------------------------------------------------------------------
    # SLIDE 1: JUDUL & IDENTITAS PENELITI (Layout Cover Autentik Gilang Pratama)
    # --------------------------------------------------------------------------
    s1 = deck.add_blank_slide()

    # Background cover: Foto lab fisik dengan overlay navy gelap
    cover_bg_path = "Gambar/cover_bg_gilang.png"
    if os.path.exists(cover_bg_path):
        s1.shapes.add_picture(cover_bg_path, 0, 0, Inches(13.333), Inches(7.5))
    else:
        bg_cover = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg_cover.fill.solid()
        bg_cover.fill.fore_color.rgb = RGBColor(8, 16, 30)
        bg_cover.line.fill.background()

    # Baris atas: Tahun (kiri), Logo Pill UIN+Fisika (tengah), Seminar Proposal (kanan)
    tb1_year = s1.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(2.0), Inches(0.5))
    tf1_year = tb1_year.text_frame
    tf1_year.word_wrap = True
    p1_year = tf1_year.paragraphs[0]
    p1_year.text = "2026"
    p1_year.font.name = FONT_FAMILY
    p1_year.font.size = Pt(15)
    p1_year.font.bold = True
    p1_year.font.color.rgb = RGBColor(255, 255, 255)

    # Logo Pill UIN + Fisika di tengah atas
    logo_pill_path = "Gambar/Logo/logo_uin_fisika_pill.png"
    if os.path.exists(logo_pill_path):
        deck.add_image_fitted(s1, logo_pill_path, Inches(5.4), Inches(0.28), Inches(2.533), Inches(0.9), border=False)
    else:
        # Fallback dua logo terpisah jika pill belum ada
        if os.path.exists("Gambar/Logo/Logo UIN.png"):
            deck.add_image_fitted(s1, "Gambar/Logo/Logo UIN.png", Inches(5.667), Inches(0.3), Inches(0.9), Inches(0.9), border=False)
        if os.path.exists("Gambar/Logo/Logo Fisika UIN.png"):
            deck.add_image_fitted(s1, "Gambar/Logo/Logo Fisika UIN.png", Inches(6.767), Inches(0.3), Inches(0.9), Inches(0.9), border=False)

    tb1_sem = s1.shapes.add_textbox(Inches(9.5), Inches(0.45), Inches(3.0), Inches(0.5))
    tf1_sem = tb1_sem.text_frame
    tf1_sem.word_wrap = True
    p1_sem = tf1_sem.paragraphs[0]
    p1_sem.text = "Seminar Proposal"
    p1_sem.font.name = FONT_FAMILY
    p1_sem.font.size = Pt(15)
    p1_sem.font.bold = True
    p1_sem.font.color.rgb = RGBColor(255, 255, 255)
    p1_sem.alignment = PP_ALIGN.RIGHT

    # Kotak Judul Tengah: Navy dengan border oranye tebal (#f26522, 4.5 pt)
    title_box = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.55), Inches(10.933), Inches(2.9))
    title_box.fill.solid()
    title_box.fill.fore_color.rgb = RGBColor(17, 34, 64)
    title_box.line.color.rgb = RGBColor(242, 101, 34)
    title_box.line.width = Pt(4.5)

    tb1_title = s1.shapes.add_textbox(Inches(1.5), Inches(1.75), Inches(10.333), Inches(2.5))
    tf1_title = tb1_title.text_frame
    tf1_title.word_wrap = True

    p1_main = tf1_title.paragraphs[0]
    p1_main.text = "RANCANG BANGUN INSTRUMENTASI SENSOR TUNNELING MAGNETORESISTANCE BERBASIS NANOFIBER Fe3O4/PVA-SITRAT-ADH UNTUK DETEKSI FORMALIN PADA BAKSO MENGGUNAKAN KOMPARASI MODEL SVM DAN QSVC"
    p1_main.font.name = FONT_FAMILY
    p1_main.font.size = Pt(19.5)
    p1_main.font.bold = True
    p1_main.font.color.rgb = RGBColor(255, 255, 255)
    p1_main.alignment = PP_ALIGN.CENTER
    p1_main.line_spacing = 1.18

    # Bagian bawah: Identitas langsung di atas latar gelap berwibawa
    tb1_disusun = s1.shapes.add_textbox(Inches(1.2), Inches(4.65), Inches(10.933), Inches(0.35))
    tf1_dis = tb1_disusun.text_frame
    p1_dis = tf1_dis.paragraphs[0]
    p1_dis.text = "DISUSUN OLEH:"
    p1_dis.font.name = FONT_FAMILY
    p1_dis.font.size = Pt(12.5)
    p1_dis.font.bold = True
    p1_dis.font.color.rgb = RGBColor(255, 255, 255)
    p1_dis.alignment = PP_ALIGN.CENTER

    tb1_nama = s1.shapes.add_textbox(Inches(1.2), Inches(5.0), Inches(10.933), Inches(0.45))
    tf1_nama = tb1_nama.text_frame
    p1_nama = tf1_nama.paragraphs[0]
    p1_nama.text = "FAHRY RIZKY SAMSUDIN"
    p1_nama.font.name = FONT_FAMILY
    p1_nama.font.size = Pt(17)
    p1_nama.font.bold = True
    p1_nama.font.color.rgb = RGBColor(255, 255, 255)
    p1_nama.alignment = PP_ALIGN.CENTER

    tb1_nim = s1.shapes.add_textbox(Inches(1.2), Inches(5.45), Inches(10.933), Inches(0.35))
    tf1_nim = tb1_nim.text_frame
    p1_nim = tf1_nim.paragraphs[0]
    p1_nim.text = "(NIM 1237030018)"
    p1_nim.font.name = FONT_FAMILY
    p1_nim.font.size = Pt(13.5)
    p1_nim.font.color.rgb = RGBColor(255, 255, 255)
    p1_nim.alignment = PP_ALIGN.CENTER

    # Pembimbing: Dua pill navy semi-transparan
    pill_y = Inches(5.95)
    for pill_idx, (lbl, nm) in enumerate([("Pembimbing I:", "Mada Sanjaya W.S., M.Si., Ph.D."), ("Pembimbing II:", "Drs. Eko Prasetyo, M.T.")]):
        pill_x = Inches(2.0 + pill_idx * 4.8)
        pill_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, pill_x, pill_y, Inches(4.5), Inches(0.45))
        pill_shape.fill.solid()
        pill_shape.fill.fore_color.rgb = RGBColor(17, 34, 64)
        pill_shape.line.fill.background()
        tb_pill = s1.shapes.add_textbox(pill_x + Inches(0.15), pill_y + Inches(0.05), Inches(4.2), Inches(0.35))
        tf_pill = tb_pill.text_frame
        p_pill = tf_pill.paragraphs[0]
        p_pill.alignment = PP_ALIGN.CENTER
        r_lbl = p_pill.add_run()
        r_lbl.text = lbl + " "
        r_lbl.font.name = FONT_FAMILY
        r_lbl.font.size = Pt(11)
        r_lbl.font.color.rgb = RGBColor(180, 200, 230)
        r_nm = p_pill.add_run()
        r_nm.text = nm
        r_nm.font.name = FONT_FAMILY
        r_nm.font.size = Pt(13)
        r_nm.font.bold = True
        r_nm.font.color.rgb = RGBColor(255, 255, 255)

    # Institusi
    tb1_inst = s1.shapes.add_textbox(Inches(1.2), Inches(6.55), Inches(10.933), Inches(0.5))
    tf1_inst = tb1_inst.text_frame
    p1_inst = tf1_inst.paragraphs[0]
    p1_inst.text = "JURUSAN FISIKA | FAKULTAS SAINS DAN TEKNOLOGI | UIN SUNAN GUNUNG DJATI BANDUNG | TAHUN 2026"
    p1_inst.font.name = FONT_FAMILY
    p1_inst.font.size = Pt(13.5)
    p1_inst.font.bold = True
    p1_inst.font.color.rgb = RGBColor(255, 255, 255)
    p1_inst.alignment = PP_ALIGN.CENTER

    # --------------------------------------------------------------------------
    # SLIDE 2: LATAR BELAKANG PENELITIAN (Diagram Alir Konseptual 3 Kolom)
    # --------------------------------------------------------------------------
    s2 = deck.add_blank_slide()
    deck.add_header(s2, "Latar Belakang Penelitian",
                    "Diagram Alir Konseptual: Dari Masalah Pangan, Gap Sensor Elektronik, hingga Solusi Biosensor TMR Cerdas")

    deck.add_image_fitted(s2, "output/diagrams/latar_belakang_flowchart.png",
                          Inches(0.8), Inches(1.5), Inches(11.733), Inches(4.5), border=False)

    deck.add_card(s2, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.8), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb2_fokus = s2.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(11.3), Inches(0.7))
    tf2_fokus = tb2_fokus.text_frame
    tf2_fokus.word_wrap = True
    p2_f = tf2_fokus.paragraphs[0]
    p2_f.text = "Fokus Kebaruan Riset: Mengintegrasikan reseptor nanofiber hijau Fe3O4/PVA-Sitrat-ADH, transduser kuantum TMR (ALT023-10E), akuisisi AD623-ADS1115 deterministik, dan komparasi model klasifikasi cerdas SVM klasik vs QSVC kuantum untuk deteksi formalin pada bakso."
    p2_f.font.name = FONT_FAMILY
    p2_f.font.size = Pt(11)
    p2_f.font.bold = True
    p2_f.font.color.rgb = COLOR_NAVY_MID

    deck.add_footer(s2, 2)

    # --------------------------------------------------------------------------
    # SLIDE 3: RUMUSAN MASALAH & BATASAN MASALAH (4 RM Presisi Sesuai Naskah)
    # --------------------------------------------------------------------------
    s3 = deck.add_blank_slide()
    deck.add_header(s3, "Rumusan Masalah & Batasan Masalah",
                    "Pertanyaan Kunci Penelitian (Kiri) dan Ruang Lingkup Batasan Riset (Kanan)")

    deck.add_card(s3, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb3_l = s3.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.2), Inches(4.8))
    tf3_l = tb3_l.text_frame
    tf3_l.word_wrap = True
    deck.add_card_header(tf3_l, "Rumusan Masalah", accent_color=COLOR_NAVY_MID, title_size=17)
    deck.add_bullet_item(tf3_l, "1.", "Bagaimana sensitivitas, batas deteksi (LOD), dan pengaruh gugus fungsional hidrazida ADH terhadap karakteristik respons magnetoresistif sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin?", pt_size=13.5, space_after=8)
    deck.add_bullet_item(tf3_l, "2.", "Bagaimana karakteristik medan magnetik acuan kumparan Helmholtz dan respons linearitas transduser TMR ALT023-10E sebelum dan sesudah integrasi rantai pengkondisi sinyal?", pt_size=13.5, space_after=8)
    deck.add_bullet_item(tf3_l, "3.", "Bagaimana rancangan sistem instrumentasi (AD623-ADS1115-Arduino-Raspberry Pi) menghasilkan kurva kalibrasi yang valid antara tegangan keluaran sensor dan konsentrasi formalin pada bakso?", pt_size=13.5, space_after=8)
    deck.add_bullet_item(tf3_l, "4.", "Bagaimana komparasi performa klasifikasi antara model Support Vector Machine (SVM) klasik dan Quantum Support Vector Classifier (QSVC) dalam mendeteksi dan mengklasifikasikan kandungan formalin pada sampel bakso?", pt_size=13.5, space_after=8)

    deck.add_card(s3, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb3_r = s3.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.2), Inches(4.8))
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True
    deck.add_card_header(tf3_r, "Batasan Masalah", accent_color=COLOR_EMERALD, title_size=17)
    deck.add_bullet_item(tf3_r, "1.", "Penelitian difokuskan khusus pada deteksi analit formalin; bahan tambahan pangan berbahaya lain seperti boraks atau pewarna tekstil tidak termasuk cakupan analisis.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf3_r, "2.", "Pengujian sensor diawali larutan formalin standar bertingkat (mg/L) sebelum diterapkan pada ekstrak sampel bakso riil pasar.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf3_r, "3.", "Material sensor dibatasi pada nanofiber Fe3O4/PVA dengan taut-silang termal asam sitrat (130 C) dan fungsionalisasi kemo-reseptor spesifik ADH via elektrospinning.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf3_r, "4.", "Mekanisme pengenalan formalin oleh gugus hidrazida ADH diperlakukan sebagai hipotesis yang diuji secara empiris.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf3_r, "5.", "Evaluasi sensor dibatasi pada parameter sensitivitas, linearitas, batas deteksi (LOD), dan stabilitas sinyal.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf3_r, "6.", "Pemodelan cerdas dibatasi pada perbandingan model klasik SVM dan model kuantum QSVC berbasis quantum feature map.", pt_size=12.5, space_after=6)

    deck.add_footer(s3, 3)

    # --------------------------------------------------------------------------
    # SLIDE 4: TUJUAN PENELITIAN & MANFAAT PENELITIAN (4 Tujuan Presisi Sesuai Naskah)
    # --------------------------------------------------------------------------
    s4 = deck.add_blank_slide()
    deck.add_header(s4, "Tujuan & Manfaat Penelitian",
                    "Target Capaian Ilmiah dan Dampak Kontributif Teoretis, Metodologis, serta Praktis")

    deck.add_card(s4, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb4_l = s4.shapes.add_textbox(Inches(1.05), Inches(1.7), Inches(5.2), Inches(4.8))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True
    deck.add_card_header(tf4_l, "Tujuan Penelitian", accent_color=COLOR_NAVY_MID, title_size=17)
    deck.add_bullet_item(tf4_l, "1.", "Mengevaluasi sensitivitas, batas deteksi (LOD), serta pengaruh gugus fungsional hidrazida ADH terhadap karakteristik respons magnetoresistif sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH dalam mendeteksi variasi konsentrasi formalin.", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_l, "2.", "Mengkarakterisasi medan magnetik acuan kumparan Helmholtz serta respons linearitas transduser TMR ALT023-10E sebelum dan sesudah integrasi rantai pengkondisi sinyal.", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_l, "3.", "Merancang dan memvalidasi sistem instrumentasi akuisisi data (AD623-ADS1115-Arduino-Raspberry Pi) yang menghasilkan kurva kalibrasi valid antara tegangan keluaran sensor dan konsentrasi formalin pada bakso.", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_l, "4.", "Menganalisis dan membandingkan performa klasifikasi (akurasi, presisi, recall, F1-score, dan ketahanan derau) antara model SVM klasik dan QSVC kuantum dalam mengklasifikasikan kandungan formalin pada sampel bakso.", pt_size=13.5, space_after=9)

    deck.add_card(s4, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb4_r = s4.shapes.add_textbox(Inches(7.05), Inches(1.7), Inches(5.2), Inches(4.8))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True
    deck.add_card_header(tf4_r, "Manfaat Penelitian", accent_color=COLOR_EMERALD, title_size=17)
    deck.add_bullet_item(tf4_r, "1.", "Memberikan kontribusi teoretis dalam pengembangan ilmu instrumentasi sensor dengan menghadirkan kajian empiris performa sensor TMR berbasis nanofiber Fe3O4/PVA-Sitrat-ADH.", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_r, "2.", "Menawarkan inovasi agen taut-silang ramah lingkungan asam sitrat (curing 130 C) serta kemo-reseptor spesifik ADH penangkap formaldehida (ikatan hidrazon kovalen).", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_r, "3.", "Memberikan kontribusi kebaruan ilmiah dalam penerapan Quantum Machine Learning (QSVC) untuk klasifikasi data sinyal sensor pada pengujian keamanan pangan.", pt_size=13.5, space_after=9)
    deck.add_bullet_item(tf4_r, "4.", "Menjadi dasar bagi pengembangan instrumen deteksi formalin yang cerdas, portabel, kuantitatif, dan terjangkau guna mendukung penjaminan keamanan pangan nasional.", pt_size=13.5, space_after=9)

    deck.add_footer(s4, 4)

    # --------------------------------------------------------------------------
    # SLIDE 5: METODE PENGUMPULAN DATA (4 Pilar Terstruktur)
    # --------------------------------------------------------------------------
    s5 = deck.add_blank_slide()
    deck.add_header(s5, "Metode Pengumpulan Data Penelitian",
                    "Tahapan Terstruktur Memperoleh Data Empiris, Kalibrasi Sensor, dan Validasi Model")

    pilar_data = [
        ("01", "Studi Literatur", COLOR_BLUE_ACCENT,
         "Menghimpun dan menelaah rujukan bereputasi terkait spintronika TMR, sintesis hijau Fe3O4 kelor, fungsionalisasi ADH, serta arsitektur SVM dan QSVC.",
         "Sumber: IEEE, ScienceDirect, Nature, Springer, ACS"),
        ("02", "Observasi & Desain", COLOR_EMERALD,
         "Observasi terhadap prototipe magnetoresistif terdahulu, perancangan mekatronika housing 3D, pengkondisi sinyal AD623, dan filter aktif LPF.",
         "Fokus: Eliminasi derau 50 Hz & isolasi termal"),
        ("03", "Eksperimen Laboratorium", COLOR_AMBER,
         "Pengujian bertahap: (1) Kalibrasi medan Helmholtz 0-11.5 mT, (2) Uji larutan formalin standar bertingkat, dan (3) Ekstraksi sampel bakso pasar.",
         "Standarisasi: Teslameter WT10A terkalibrasi"),
        ("04", "Analisis & Pemodelan Cerdas", COLOR_ROSE,
         "Ekstraksi 5 fitur sinyal domain waktu (Vpeak, Vsteady, dV, dV/dt, Area), pelatihan 5-fold cross validation SVM vs QSVC, dan uji ketahanan derau.",
         "Output: Metrik komparasi akurasi, presisi & F1")
    ]

    for idx, (num, title, col, desc, note) in enumerate(pilar_data):
        card_x = Inches(0.8 + idx * 3.0)
        deck.add_card(s5, card_x, Inches(1.55), Inches(2.733), Inches(5.2))
        tb_p = s5.shapes.add_textbox(card_x + Inches(0.18), Inches(1.75), Inches(2.38), Inches(4.8))
        tf_p = tb_p.text_frame
        tf_p.word_wrap = True

        p_num = tf_p.paragraphs[0]
        p_num.text = num
        p_num.font.name = FONT_FAMILY
        p_num.font.size = Pt(28)
        p_num.font.bold = True
        p_num.font.color.rgb = col
        p_num.space_after = Pt(2)

        p_t = tf_p.add_paragraph()
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_MAIN
        p_t.space_after = Pt(8)

        p_desc = tf_p.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = FONT_FAMILY
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = COLOR_TEXT_BODY
        p_desc.line_spacing = 1.2
        p_desc.space_after = Pt(8)

        p_note = tf_p.add_paragraph()
        p_note.text = note
        p_note.font.name = FONT_FAMILY
        p_note.font.size = Pt(10.0)
        p_note.font.bold = True
        p_note.font.color.rgb = col

    deck.add_footer(s5, 5)

    # --------------------------------------------------------------------------
    # SLIDE 6: DASAR TEORI 1: FISIKA TRANSDUSER TMR & KUMPARAN HELMHOLTZ (FOTO ASLI)
    # --------------------------------------------------------------------------
    s6 = deck.add_blank_slide()
    deck.add_header(s6, "Dasar Teori: Fisika Sensor TMR & Pembangkit Medan Helmholtz",
                    "Prinsip Spintronika Kuantum MTJ (Kiri) dan Superposisi Medan Biot-Savart Helmholtz (Kanan)")

    # Card Kiri: Sensor TMR MTJ
    deck.add_card(s6, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    deck.add_image_fitted(s6, "Gambar/Bab2/babII_TMR_Layer.png", Inches(1.05), Inches(1.75), Inches(5.2), Inches(1.9),
                          border=False, caption="Gambar 2. Struktur Lapisan Magnetic Tunnel Junction (MTJ) Sensor TMR (Julliere, 1975)")
    
    tb6_l = s6.shapes.add_textbox(Inches(1.05), Inches(3.85), Inches(5.2), Inches(2.0))
    tf6_l = tb6_l.text_frame
    tf6_l.word_wrap = True
    deck.add_card_header(tf6_l, "Tunneling Magnetoresistance (TMR)", accent_color=COLOR_BLUE_ACCENT, title_size=15)
    deck.add_bullet_item(tf6_l, "Efek Tunneling:", "Elektron menembus isolator MgO nanometer; resistansi minimum saat spin paralel, maksimum saat antiparalel.", pt_size=12.5, space_after=5)
    deck.add_bullet_item(tf6_l, "Rasio TMR:", "Mencapai >200% pada suhu ruang (vs GMR <20%); sensitivitas diferensial mencapai 15-25 mV/V/mT (6x lebih peka).", pt_size=12.5, space_after=5)
    
    deck.add_image_fitted(s6, "output/equations/eq_02_julliere.png", Inches(1.05), Inches(5.95), Inches(5.2), Inches(0.65), border=False)

    # Card Kanan: Kumparan Helmholtz
    deck.add_card(s6, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    deck.add_image_fitted(s6, "Gambar/Bab2/babII_Two-coils-of-WPT-system.png", Inches(7.05), Inches(1.75), Inches(5.2), Inches(1.9),
                          border=False, caption="Gambar 3. Geometri dan Konfigurasi Sepasang Kumparan Helmholtz (Zhu et al., 2023)")

    tb6_r = s6.shapes.add_textbox(Inches(7.05), Inches(3.85), Inches(5.2), Inches(2.0))
    tf6_r = tb6_r.text_frame
    tf6_r.word_wrap = True
    deck.add_card_header(tf6_r, "Kumparan Helmholtz Terstandardisasi", accent_color=COLOR_EMERALD, title_size=15)
    deck.add_bullet_item(tf6_r, "Superposisi Medan:", "Sepasang kumparan N lilitan berjari-jari R dengan jarak pisah R menghasilkan medan homogen deviasi < 1%.", pt_size=12.5, space_after=5)
    deck.add_bullet_item(tf6_r, "Akurasi Metrologis:", "Menjadi acuan medan magnetik terkontrol (0-11.5 mT) sebelum sensor digunakan untuk pengujian larutan analit.", pt_size=12.5, space_after=5)

    deck.add_image_fitted(s6, "output/equations/eq_03_helmholtz.png", Inches(7.05), Inches(5.95), Inches(5.2), Inches(0.65), border=False)

    deck.add_footer(s6, 6)

    # --------------------------------------------------------------------------
    # SLIDE 7: DASAR TEORI 2: KOMPONEN FISIK RANTAI INSTRUMENTASI (SUBBAB 2.2 DENGAN FOTO ASLI)
    # --------------------------------------------------------------------------
    s7 = deck.add_blank_slide()
    deck.add_header(s7, "Dasar Teori: Komponen Fisik Rantai Instrumentasi (Subbab 2.2)",
                    "Spesifikasi Perangkat Keras: Sensor TMR, In-Amp AD623, ADC ADS1115, Arduino Uno, Raspberry Pi 5 & Pasif")

    comp_items = [
        ("Sensor TMR ALT023-10E", "Gambar/Bab2/babII_ALT023.png", COLOR_BLUE_ACCENT,
         "Jembatan Wheatstone TMR bipolar, rentang linear +/-1.0 mT, catu daya tunggal 5.0 V, decoupling 100 nF."),
        ("In-Amp AD623 (Analog Devices)", "Gambar/Bab2/babII_AD623_Pinout.png", COLOR_EMERALD,
         "Penguat instrumentasi rail-to-rail, catu +5.0 V, VREF = 2.50 V presisi (R=1 kOhm), CMRR 90 dB."),
        ("ADC 16-Bit ADS1115 (TI)", "Gambar/Bab2/babII_ADS-1115-c.jpg", COLOR_NAVY_MID,
         "Resolusi tinggi 0.1875 mV/count pada GAIN_TWOTHIRDS (FSR 6.144 V), antarmuka I2C deterministik."),
        ("Arduino Uno R3 (ATmega328P)", "Gambar/Bab2/babII_ArduinoUno.jpg", COLOR_AMBER,
         "Unit mikrokontroler akuisisi deterministik berbasis timer interrupt, baudrate serial 115200 bps."),
        ("Raspberry Pi 5 (Quad Core)", "Gambar/Bab2/babII_Raspberry Pi 5.PNG", COLOR_ROSE,
         "Host controller 64-bit untuk GUI TMRAcquisitionApp, logging data Excel, dan eksekusi inferensi model ML."),
        ("Resistor Presisi & Kapasitor", "Gambar/Bab2/babII_Types-of-resistors.png", COLOR_BLUE_ACCENT,
         "Pembagi VREF presisi 1.0 kOhm (0.1%), filter RC LPF (fc = 10 Hz) meredam ripple PLN 50 Hz.")
    ]

    for idx, (c_name, c_img, c_col, c_desc) in enumerate(comp_items):
        row = idx // 3
        col = idx % 3
        c_x = Inches(0.8 + col * 4.0)
        c_y = Inches(1.55 + row * 2.65)
        c_w = Inches(3.733)
        c_h = Inches(2.5)

        deck.add_card(s7, c_x, c_y, c_w, c_h)
        deck.add_image_fitted(s7, c_img, c_x + Inches(0.12), c_y + Inches(0.12), Inches(1.3), Inches(1.3), border=True)

        tb_c = s7.shapes.add_textbox(c_x + Inches(1.5), c_y + Inches(0.1), Inches(2.15), Inches(2.3))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p_cn = tf_c.paragraphs[0]
        p_cn.text = c_name
        p_cn.font.name = FONT_FAMILY
        p_cn.font.size = Pt(11.5)
        p_cn.font.bold = True
        p_cn.font.color.rgb = c_col
        p_cn.space_after = Pt(4)

        p_cd = tf_c.add_paragraph()
        p_cd.text = c_desc
        p_cd.font.name = FONT_FAMILY
        p_cd.font.size = Pt(10.0)
        p_cd.font.color.rgb = COLOR_TEXT_BODY
        p_cd.line_spacing = 1.18

    deck.add_footer(s7, 7)

    # --------------------------------------------------------------------------
    # SLIDE 8: DASAR TEORI 3: MATERIAL KIMIA NANOKOMPOSIT & ADH (FOTO ASLI)
    # --------------------------------------------------------------------------
    s8 = deck.add_blank_slide()
    deck.add_header(s8, "Dasar Teori: Material Nanokomposit & Fungsionalisasi ADH",
                    "Geometri Formalin & Reaksi Hidrazon (Kiri) serta Nanofiber Elektrospinning Fe3O4/PVA (Kanan)")

    # Card Kiri: Molekul Formalin & Reaksi Hidrazon
    deck.add_card(s8, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    deck.add_image_fitted(s8, "Gambar/Bab2/babII_ikatan_formalin.png", Inches(1.05), Inches(1.75), Inches(5.2), Inches(1.9),
                          border=False, caption="Gambar 4. Struktur Geometri Molekul dan Hibridisasi sp2 Formaldehida")

    tb8_l = s8.shapes.add_textbox(Inches(1.05), Inches(3.85), Inches(5.2), Inches(2.0))
    tf8_l = tb8_l.text_frame
    tf8_l.word_wrap = True
    deck.add_card_header(tf8_l, "Formaldehida & Reseptor Selektif ADH", accent_color=COLOR_ROSE, title_size=15)
    deck.add_bullet_item(tf8_l, "Formaldehida (HCHO):", "Senyawa elektrofilik reaktif planar segitiga; dilarang keras dalam pangan (Permenkes 033/2012).", pt_size=12.5, space_after=4)
    deck.add_bullet_item(tf8_l, "Adipic Acid Dihydrazide:", "ADH membawa dua gugus terminal hidrazida (-NH-NH2) yang bereaksi selektif membentuk ikatan kovalen hidrazon (-C=N-NH-).", pt_size=12.5, space_after=4)
    deck.add_bullet_item(tf8_l, "Keunggulan vs GA:", "Glutaraldehida membawa gugus aldehida sendiri, sedangkan ADH spesifik mengikat analit formaldehida.", pt_size=12.5, space_after=4)

    deck.add_image_fitted(s8, "output/equations/eq_01_hidrazon.png", Inches(1.05), Inches(5.95), Inches(5.2), Inches(0.65), border=False)

    # Card Kanan: Nanofiber Elektrospinning Fe3O4/PVA-Sitrat
    deck.add_card(s8, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    deck.add_image_fitted(s8, "Gambar/Bab2/babII_elspinPVA.PNG", Inches(7.05), Inches(1.75), Inches(5.2), Inches(1.9),
                          border=False, caption="Gambar 5. Morfologi Matriks Nanofiber Berpori Hasil Elektrospinning (Xue et al., 2019)")

    tb8_r = s8.shapes.add_textbox(Inches(7.05), Inches(3.85), Inches(5.2), Inches(2.0))
    tf8_r = tb8_r.text_frame
    tf8_r.word_wrap = True
    deck.add_card_header(tf8_r, "Nanokomposit Fe3O4/PVA-Sitrat-ADH", accent_color=COLOR_EMERALD, title_size=15)
    deck.add_bullet_item(tf8_r, "Fe3O4 Hijau Daun Kelor:", "Sintesis kopresipitasi ekstrak daun kelor menghasilkan nanopartikel superparamagnetik tanpa histeresis pada suhu ruang.", pt_size=12.5, space_after=5)
    deck.add_bullet_item(tf8_r, "Matriks Nanofiber Berpori:", "Elektrospinning menghasilkan rasio luas permukaan terhadap volume sangat tinggi, melipatgandakan situs aktif analit.", pt_size=12.5, space_after=5)
    deck.add_bullet_item(tf8_r, "Crosslinker Asam Sitrat:", "Reaksi esterifikasi termal pada 130 C membentuk taut-silang kovalen yang tahan air dan stabil dalam pelarut cair.", pt_size=12.5, space_after=5)

    deck.add_footer(s8, 8)

    # --------------------------------------------------------------------------
    # SLIDE 9: DASAR TEORI 4: PEMODELAN ML KLASIK VS KUANTUM (FORMULA & TEORI)
    # --------------------------------------------------------------------------
    s9 = deck.add_blank_slide()
    deck.add_header(s9, "Dasar Teori: Pemodelan Machine Learning Klasik vs Kuantum",
                    "Support Vector Machine Kernel RBF (Kiri) dan Quantum Support Vector Classifier (Kanan)")

    # Card Kiri: SVM Klasik
    deck.add_card(s9, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb9_l = s9.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(3.8))
    tf9_l = tb9_l.text_frame
    tf9_l.word_wrap = True
    deck.add_card_header(tf9_l, "Support Vector Machine (SVM) Klasik", accent_color=COLOR_BLUE_ACCENT, title_size=16)
    deck.add_bullet_item(tf9_l, "Prinsip Kerja:", "Memaksimalkan margin pemisah (hyperplane) antara kelas konsentrasi formalin berdasarkan vektor pendukung (support vectors).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_l, "Kernel RBF Non-Linear:", "Kernel Radial Basis Function memetakan 5 fitur sinyal sensor ke ruang dimensi tak hingga untuk mengatasi data nonlinear.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_l, "Keunggulan Sampel Terbatas:", "Prinsip Structural Risk Minimization terbukti sangat tangguh pada dataset ukuran kecil tanpa risiko overfitting.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_l, "Sitasi Rujukan:", "Cortes & Vapnik (1995); Breiman (2001); Nainggolan et al. (2023).", pt_size=11.5, color=COLOR_BLUE_ACCENT)

    deck.add_image_fitted(s9, "output/equations/eq_06_svm.png", Inches(1.05), Inches(5.65), Inches(5.2), Inches(0.95), border=False)

    # Card Kanan: QSVC Kuantum
    deck.add_card(s9, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb9_r = s9.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(3.8))
    tf9_r = tb9_r.text_frame
    tf9_r.word_wrap = True
    deck.add_card_header(tf9_r, "Quantum Support Vector Classifier (QSVC)", accent_color=COLOR_EMERALD, title_size=16)
    deck.add_bullet_item(tf9_r, "Quantum Feature Map:", "Sirkuit ZZFeatureMap memetakan fitur sinyal ke ruang Hilbert 2^n dimensi melalui superposisi Hadamard dan fase CNOT.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_r, "Quantum Kernel Matrix:", "Nilai kernel dihitung melalui overlap keadaan kuantum |<psi(x)|psi(z)>|^2 pada simulator kuantum Qiskit Aer.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_r, "Keunggulan Separabilitas:", "Keterikatan kuantum (entanglement) secara teoretis memisahkan batas keputusan kompleks yang terdistorsi derau pangan.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf9_r, "Sitasi Rujukan:", "Havlicek et al. (Nature, 2019); Schuld & Killoran (PRL, 2019).", pt_size=11.5, color=COLOR_EMERALD)

    deck.add_image_fitted(s9, "output/equations/eq_07_qsvc.png", Inches(7.05), Inches(5.65), Inches(5.2), Inches(0.95), border=False)

    deck.add_footer(s9, 9)

    # --------------------------------------------------------------------------
    # SLIDE 10: KOMPARASI MODEL KLASIK VS KUANTUM & SOFTWARE STACK (DENGAN LOGO ASLI)
    # --------------------------------------------------------------------------
    s10 = deck.add_blank_slide()
    deck.add_header(s10, "Komparasi Model Klasik vs Kuantum & Software Stack",
                    "Matriks Evaluasi Komparatif, Peran Firmware Arduino IDE 2.0, dan Host Python Qiskit")

    # Card 1: Matriks Perbandingan
    deck.add_card(s10, Inches(0.8), Inches(1.55), Inches(4.5), Inches(5.2))
    tb10_1 = s10.shapes.add_textbox(Inches(1.0), Inches(1.75), Inches(4.1), Inches(4.8))
    tf10_1 = tb10_1.text_frame
    tf10_1.word_wrap = True
    deck.add_card_header(tf10_1, "Matriks Evaluasi Model", accent_color=COLOR_BLUE_ACCENT, title_size=15)
    deck.add_bullet_item(tf10_1, "Representasi Fitur:", "SVM menggunakan ruang Euklidian R^n, sedangkan QSVC menggunakan ruang Hilbert 2^n dimensi.", pt_size=12.0, space_after=5)
    deck.add_bullet_item(tf10_1, "Kompleksitas Hitung:", "SVM O(N^2) komputasi CPU klasik; QSVC O(N^2) kalkulasi overlap state kuantum pada Qiskit.", pt_size=12.0, space_after=5)
    deck.add_bullet_item(tf10_1, "Toleransi Derau:", "QSVC diuji ketahanannya terhadap fluktuasi medan magnet bumi dan variasi biologis matriks bakso.", pt_size=12.0, space_after=5)
    deck.add_bullet_item(tf10_1, "Validasi Silang:", "5-Fold Cross Validation dengan metrik evaluasi: Akurasi, Presisi, Recall, F1-Score, dan AUC-ROC.", pt_size=12.0, space_after=5)

    # Card 2: Arduino IDE 2.0 (FOTO ASLI)
    deck.add_card(s10, Inches(5.5), Inches(1.55), Inches(3.4), Inches(5.2))
    deck.add_image_fitted(s10, "Gambar/Bab2/babII_Arduino IDE.PNG", Inches(5.7), Inches(1.75), Inches(3.0), Inches(1.8),
                          border=True, caption="Gambar 6. Lingkungan Pengembangan Arduino IDE 2.0")
    tb10_2 = s10.shapes.add_textbox(Inches(5.7), Inches(3.8), Inches(3.0), Inches(2.8))
    tf10_2 = tb10_2.text_frame
    tf10_2.word_wrap = True
    deck.add_card_header(tf10_2, "Firmware Arduino IDE 2.0", accent_color=COLOR_EMERALD, title_size=13.5)
    deck.add_bullet_item(tf10_2, "Sampling Deterministik:", "Timer interrupt membaca ADS1115 via I2C pada kecepatan teratur.", pt_size=11.5, space_after=4)
    deck.add_bullet_item(tf10_2, "Filtering Rerata:", "Moving average filter internal untuk menekan noise frekuensi tinggi.", pt_size=11.5, space_after=4)
    deck.add_bullet_item(tf10_2, "Protokol Serial:", "Mengirim paket data terstruktur ke GUI Python (115200 bps).", pt_size=11.5, space_after=4)

    # Card 3: Python GUI & Qiskit (FOTO ASLI)
    deck.add_card(s10, Inches(9.1), Inches(1.55), Inches(3.433), Inches(5.2))
    deck.add_image_fitted(s10, "Gambar/Bab2/babII_Python.png", Inches(9.3), Inches(1.75), Inches(3.0), Inches(1.8),
                          border=True, caption="Gambar 7. Ekosistem Pemrograman Python 3.13")
    tb10_3 = s10.shapes.add_textbox(Inches(9.3), Inches(3.8), Inches(3.0), Inches(2.8))
    tf10_3 = tb10_3.text_frame
    tf10_3.word_wrap = True
    deck.add_card_header(tf10_3, "GUI Python 3 & Qiskit", accent_color=COLOR_NAVY_MID, title_size=13.5)
    deck.add_bullet_item(tf10_3, "CustomTkinter GUI:", "Visualisasi sinyal real-time dan kendali durasi akuisisi.", pt_size=11.5, space_after=4)
    deck.add_bullet_item(tf10_3, "Ekstraksi Fitur:", "Ekstraksi otomatis 5 fitur sinyal sensor domain waktu.", pt_size=11.5, space_after=4)
    deck.add_bullet_item(tf10_3, "Qiskit Machine Learning:", "Simulasi quantum circuit QSVC dan pemetaan quantum kernel.", pt_size=11.5, space_after=4)

    deck.add_footer(s10, 10)

    # --------------------------------------------------------------------------
    # SLIDE 11: PERBANDINGAN DENGAN PENELITIAN TERDAHULU & KEBARUAN RISET (SLIDE BARU)
    # --------------------------------------------------------------------------
    s11_comp = deck.add_blank_slide()
    deck.add_header(s11_comp, "Perbandingan dengan Penelitian Terdahulu & Kebaruan Riset",
                    "Matriks Komparasi Sensor Formalin, Reseptor Nanofiber, dan Algoritma Cerdas Terdahulu")

    # Tabel Komparasi 6 kolom x 6 baris (header + 5 data)
    comp_headers = ["Peneliti & Tahun", "Analit", "Transduser", "Material Reseptor", "Model Pemrosesan", "LOD & Celah Riset (Gap)"]
    comp_rows = [
        ["Wang et al. (2021)", "Gas Formaldehida", "MOS SnO2", "Lapisan Oksida", "Regresi Linier", "0.05 ppm; suhu 300 C, interferensi alkohol"],
        ["Singhal et al. (2024)", "Formalin Pangan", "Elektrokimia", "Enzim FDH", "Amperometrik", "0.02 mg/L; enzim labil <3 minggu, fouling lemak"],
        ["Sun et al. (2023)", "Formalin Makanan", "Kolorimetri Optik", "Reagen Nash", "Citra Digital & K-NN", "1.0 mg/L; bias kekeruhan & pigmen bakso"],
        ["Gilang Pratama (2026)", "Glukosa Saliva", "GMR", "Nanofiber Fe3O4/PVA-GOx", "Random Forest", "0.08 mg/mL; rasio GMR 10-15%, model klasik"],
        ["Penelitian Ini (2026)", "Formalin Bakso", "TMR ALT023-10E", "Nanofiber Fe3O4/PVA-Sitrat-ADH", "SVM vs QSVC", "Target sub-ppm; suhu ruang, hidrazon kovalen, TMR >200%"]
    ]
    table_shape = deck.add_table(s11_comp, Inches(0.8), Inches(1.55), Inches(11.733), Inches(3.5),
                                  comp_headers, comp_rows,
                                  col_widths=[Inches(1.8), Inches(1.4), Inches(1.6), Inches(2.2), Inches(1.7), Inches(3.033)])

    # Highlight baris terakhir (Penelitian Ini)
    table = table_shape.table
    for col_idx in range(6):
        cell = table.cell(5, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_NAVY_MID
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                r.font.size = Pt(10.5)

    # Kotak Kebaruan di bawah tabel
    deck.add_card(s11_comp, Inches(0.8), Inches(5.2), Inches(11.733), Inches(1.55), bg_color=COLOR_LIGHT_BLUE, border_color=COLOR_BLUE_ACCENT)
    tb11c = s11_comp.shapes.add_textbox(Inches(1.05), Inches(5.35), Inches(11.2), Inches(1.3))
    tf11c = tb11c.text_frame
    tf11c.word_wrap = True
    deck.add_card_header(tf11c, "Tiga Pilar Kebaruan Ilmiah Penelitian Ini", accent_color=COLOR_NAVY_MID, title_size=15)
    deck.add_bullet_item(tf11c, "1. Reseptor ADH Kovalen:", "Ikatan hidrazon spesifik tanpa glutaraldehida toksik; stabilitas kimiawi jauh melampaui enzim FDH.", pt_size=12.0, space_after=4)
    deck.add_bullet_item(tf11c, "2. Transduser TMR >200%:", "Sensor spintronika ALT023-10E beresolusi 6x lebih tinggi dari GMR konvensional pada suhu ruang.", pt_size=12.0, space_after=4)
    deck.add_bullet_item(tf11c, "3. Komparasi SVM vs QSVC:", "Studi komparasi pionir antara kernel RBF klasik dan quantum feature map pada matriks analitik pangan.", pt_size=12.0, space_after=4)

    deck.add_footer(s11_comp, 11)

    # --------------------------------------------------------------------------
    # SLIDE 12: METODOLOGI: WAKTU, LOKASI RISET, ALAT & BAHAN
    # --------------------------------------------------------------------------
    s12_tools = deck.add_blank_slide()
    deck.add_header(s12_tools, "Metodologi: Waktu, Lokasi Riset, dan Spesifikasi Alat & Bahan",
                    "Rincian Jadwal 4 Bulan di Bolabot, Fasilitas Instrumentasi Presisi, dan Bahan Kimia Analitik")

    deck.add_card(s12_tools, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.95), bg_color=COLOR_LIGHT_SLATE)
    tb11_lok = s12_tools.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(11.3), Inches(0.75))
    tf11_lok = tb11_lok.text_frame
    tf11_lok.word_wrap = True
    p11_w = tf11_lok.paragraphs[0]
    p11_w.text = "Waktu Pelaksanaan : September 2026 - Desember 2026 (Durasi 4 Bulan Efektif)"
    p11_w.font.name = FONT_FAMILY
    p11_w.font.size = Pt(11.5)
    p11_w.font.bold = True
    p11_w.font.color.rgb = COLOR_NAVY_DARK

    p11_l = tf11_lok.add_paragraph()
    p11_l.text = "Lokasi Penelitian : Laboratorium Fisika Instrumentasi UIN Sunan Gunung Djati Bandung & Bolabot Techno Robotic School, Bandung"
    p11_l.font.name = FONT_FAMILY
    p11_l.font.size = Pt(10.5)
    p11_l.font.color.rgb = COLOR_TEXT_BODY

    # Tabel Alat (Kiri)
    headers_alat = ["Kategori", "Nama Peralatan", "Fungsi Utama"]
    rows_alat = [
        ["Transduser", "Sensor TMR ALT023-10E", "Mendeteksi fluks medan magnet lokal jembatan Wheatstone"],
        ["Pengkondisi", "IC AD623 & LPF Aktif", "Penguatan tegangan diferensial (VREF = 2.50 V) & filter 10 Hz"],
        ["Digitasi", "ADC ADS1115 16-Bit", "Konversi analog ke digital resolusi 0.1875 mV/count via I2C"],
        ["Kontroler", "Arduino Uno & RPi 5", "Akuisisi deterministik mikrokontroler & inferensi model host"],
        ["Pembangkit", "Sepasang Helmholtz Coil", "Pembangkitan medan magnetik acuan homogen (0-11.5 mT)"],
        ["Kalibrator", "Teslameter WT10A", "Ground truth pembacaan medan magnet riil terstandardisasi"]
    ]
    deck.add_table(s12_tools, Inches(0.8), Inches(2.65), Inches(5.7), Inches(4.1), headers_alat, rows_alat,
                   col_widths=[Inches(1.2), Inches(2.1), Inches(2.4)])

    # Tabel Bahan (Kanan)
    headers_bahan = ["Bahan Kimia / Sampel", "Spesifikasi", "Fungsi dalam Penelitian"]
    rows_bahan = [
        ["Daun Kelor (M. oleifera)", "Ekstrak Segar 50 g/250 mL", "Reduktor & penudung sintesis hijau Fe3O4"],
        ["Prekursor Besi", "FeCl3.6H2O & FeCl2.4H2O", "Sumber ion Fe3+ dan Fe2+ rasio stoikiometri 2:1"],
        ["Polivinil Alkohol (PVA)", "Mw 89.000-98.000 g/mol", "Matriks polimer utama pembentuk serat nanofiber"],
        ["Asam Sitrat", "P.a. Merck (99.5%)", "Agen penaut silang (crosslinker) ramah lingkungan"],
        ["Adipic Acid Dihydrazide", "ADH Merck (98%)", "Gugus reseptor penangkap formaldehida (hidrazon)"],
        ["Sampel Bakso", "Pedagang Pasar Tradisional", "Matriks pangan riil pengujian validasi sistem"]
    ]
    deck.add_table(s12_tools, Inches(6.8), Inches(2.65), Inches(5.733), Inches(4.1), headers_bahan, rows_bahan,
                   col_widths=[Inches(1.7), Inches(1.8), Inches(2.233)])

    deck.add_footer(s12_tools, 12)

    # --------------------------------------------------------------------------
    # SLIDE 13: METODOLOGI: DIAGRAM ALIR PENELITIAN KOMPREHENSIF (6 TAHAPAN)
    # --------------------------------------------------------------------------
    s13_flow = deck.add_blank_slide()
    deck.add_header(s13_flow, "Metodologi: Diagram Alir Penelitian Komprehensif",
                    "6 Tahapan Eksekusi Riset: Dari Sintesis Material Hijau hingga Komparasi Model Klasik vs Kuantum")

    deck.add_image_fitted(s13_flow, "Gambar/Bab3/BABIII_DiagramAlirPenelitian.drawio.png",
                          Inches(0.8), Inches(1.55), Inches(5.8), Inches(5.2),
                          border=True, caption="Gambar 8. Diagram Alir Komprehensif Metodologi Penelitian")

    deck.add_card(s13_flow, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb12_r = s13_flow.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf12_r = tb12_r.text_frame
    tf12_r.word_wrap = True
    deck.add_card_header(tf12_r, "6 Tahapan Eksekusi Riset", accent_color=COLOR_NAVY_MID, title_size=16)
    deck.add_bullet_item(tf12_r, "Tahap 1: Sintesis Nanofiber:", "Ekstraksi kelor, kopresipitasi Fe3O4, formulasi sol PVA-Sitrat-ADH, dan elektrospinning 15 kV.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf12_r, "Tahap 2: Curing Termal 130 C:", "Pemanasan oven 130 C selama 1.5 jam untuk esterifikasi asam sitrat agar nanofiber kokoh.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf12_r, "Tahap 3: Rancang Mekatronika:", "Desain sirkuit PCB AD623-ADS1115-Arduino, housing 3D statif non-magnetik, dan firmware interrupt.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf12_r, "Tahap 4: Kalibrasi Helmholtz:", "Pemetaan medan 0-11.5 mT vs arus 0-1.6 A serta karakterisasi sensitivitas diferensial TMR ALT023.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf12_r, "Tahap 5: Pengujian Larutan & Bakso:", "Uji bertingkat standar formalin (mg/L) dan ekstrak bakso riil, dilanjutkan ekstraksi 5 fitur sinyal.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf12_r, "Tahap 6: Komparasi SVM vs QSVC:", "Pelatihan 5-fold cross validation, pemetaan quantum kernel pada Qiskit, dan analisis metrik.", pt_size=12.5, space_after=6)

    deck.add_footer(s13_flow, 13)

    # --------------------------------------------------------------------------
    # SLIDE 14: METODOLOGI: DESAIN HARDWARE TERPADU & SKEMATIK SIRKUIT
    # --------------------------------------------------------------------------
    s14_hw = deck.add_blank_slide()
    deck.add_header(s14_hw, "Metodologi: Desain Hardware Terpadu & Skematik Sirkuit",
                    "Skematik Elektronika Sensor TMR, Penguat AD623, Filter RC, ADC ADS1115, dan Wiring Mekatronika")

    deck.add_image_fitted(s14_hw, "Gambar/Bab3/babIII_skematik_TMR_grounding_fix.png",
                          Inches(0.8), Inches(1.55), Inches(6.8), Inches(5.2),
                          border=True, caption="Gambar 9. Skematik Sirkuit Sensor TMR, AD623, Filter RC, dan ADS1115 Grounding Fix")

    deck.add_card(s14_hw, Inches(7.8), Inches(1.55), Inches(4.733), Inches(5.2))
    tb13_r = s14_hw.shapes.add_textbox(Inches(8.05), Inches(1.75), Inches(4.2), Inches(4.8))
    tf13_r = tb13_r.text_frame
    tf13_r.word_wrap = True
    deck.add_card_header(tf13_r, "Integritas Rantai Sinyal Presisi", accent_color=COLOR_BLUE_ACCENT, title_size=16)
    deck.add_bullet_item(tf13_r, "TMR ALT023-10E:", "Jembatan Wheatstone presisi dicatu 5.0 V DC teregulasi dengan kapasitor bypass 100 nF dekat pin VCC.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf13_r, "Penguat AD623:", "Gain diferensial diatur via resistor RG. Pin 5 REF diberi tegangan 2.50 V stabil dari pembagi tegangan 1 kOhm.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf13_r, "Active RC Filter:", "Frekuensi potong fc = 10 Hz memblok derau jala-jala 50 Hz sebelum masuk ke saluran ADC.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf13_r, "ADC 16-Bit ADS1115:", "Saluran diferensial A0-GND membaca sinyal dengan resolusi 0.1875 mV/count pada FSR 6.144 V.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf13_r, "Grounding Star Fix:", "Pemisahan ground analog (AGND) dan digital (DGND) pada PCB untuk mencegah ground loop derau.", pt_size=12.5, space_after=6)

    deck.add_footer(s14_hw, 14)

    # --------------------------------------------------------------------------
    # SLIDE 15: METODOLOGI: PERANGKAT LUNAK [MURNI 2 FLOWCHART, TANPA TEKS LAIN]
    # --------------------------------------------------------------------------
    s15_sw = deck.add_blank_slide()
    deck.add_header(s15_sw, "Metodologi: Perancangan Perangkat Lunak Mikrokontroler & GUI Host",
                    "Diagram Alir Firmware Arduino Uno (Kiri) dan Aplikasi GUI Python TMRAcquisitionApp (Kanan)")

    deck.add_image_fitted(s15_sw, "Gambar/Bab3/babIII_AlurSoftwareArduino.drawio.png", Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2),
                          border=True, caption="Gambar 10. Diagram Alir Firmware Mikrokontroler Arduino Uno")

    deck.add_image_fitted(s15_sw, "Gambar/Bab3/babIII_DiagramAlirPython.drawio.png", Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2),
                          border=True, caption="Gambar 11. Diagram Alir Aplikasi GUI Python TMRAcquisitionApp")

    deck.add_footer(s15_sw, 15)

    # --------------------------------------------------------------------------
    # SLIDE 16: METODOLOGI: SINTESIS NANOFIBER & ELEKTROSPINNING
    # --------------------------------------------------------------------------
    s16_mat = deck.add_blank_slide()
    deck.add_header(s16_mat, "Metodologi: Prosedur Sintesis Hijau Fe3O4 & Fabrikasi Nanofiber",
                    "Ekstraksi Kelor, Sol Polimer, Parameter Pemintalan Elektrik, dan Curing 130 C")

    deck.add_image_fitted(s16_mat, "Gambar/Bab3/babIII_DiagramAlirSintesis.drawio.png", Inches(0.8), Inches(1.55), Inches(5.8), Inches(5.2),
                          border=True, caption="Gambar 12. Diagram Alir Kimia Sintesis Nanofiber Fe3O4/PVA-Sitrat-ADH")

    deck.add_card(s16_mat, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb15_r = s16_mat.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf15_r = tb15_r.text_frame
    tf15_r.word_wrap = True
    deck.add_card_header(tf15_r, "Parameter Optimal Laboratorium", accent_color=COLOR_EMERALD, title_size=16)
    deck.add_bullet_item(tf15_r, "Ekstraksi Daun Kelor:", "50 g daun segar dalam 250 mL akuades, pemanasan 80 C selama 30 menit, disaring kertas Whatman.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf15_r, "Kopresipitasi Fe3O4:", "FeCl3 dan FeCl2 (rasio 2:1) + 20 mL ekstrak kelor, titrasi NaOH 2 M hingga pH 11 pada 70 C.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf15_r, "Formulasi Sol Gel:", "PVA 10% wt + Fe3O4 2% wt + Asam Sitrat 5% wt + ADH 3% wt diaduk konstan pada 60 C.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf15_r, "Parameter Elektrospinning:", "Tegangan 15 kV, laju alir syringe pump 0.5 mL/jam, jarak jarum ke drum 15 cm, putaran drum 300 rpm.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf15_r, "Curing Termal Final:", "Oven pemanas pada suhu 130 C selama 1.5 jam untuk aktivasi ikatan ester tahan air.", pt_size=12.5, space_after=6)

    deck.add_footer(s16_mat, 16)

    # --------------------------------------------------------------------------
    # SLIDE 17: METODOLOGI: KALIBRASI HELMHOLTZ & KARAKTERISASI TMR
    # --------------------------------------------------------------------------
    s17_cal = deck.add_blank_slide()
    deck.add_header(s17_cal, "Metodologi: Prosedur Kalibrasi Kumparan Helmholtz & Sensor TMR",
                    "Pemetaan Faktor Konversi Medan Magnetik dan Penentuan Kurva Sensitivitas Diferensial")

    deck.add_card(s17_cal, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb16_l = s17_cal.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf16_l = tb16_l.text_frame
    tf16_l.word_wrap = True
    deck.add_card_header(tf16_l, "Tahap 1: Kalibrasi Medan Helmholtz", accent_color=COLOR_BLUE_ACCENT, title_size=16)
    deck.add_bullet_item(tf16_l, "Tujuan Kalibrasi:", "Memperoleh koefisien konversi empiris medan magnetik B (mT) terhadap arus kumparan I (A).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_l, "Variasi Eksperimen:", "Tegangan suplai power supply DC diatur bertahap 0.0 - 16.0 V menghasilkan sapuan arus 0.0 - 1.6 A.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_l, "Pengukuran Lapangan:", "Probe Hall-effect teslameter WT10A diletakkan tepat di pusat simetri kumparan (z = R/2).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_l, "Hasil Regresi Linier:", "Persamaan kalibrasi: B_ukur = k_helm * I + B_offset, memastikan linearitas R^2 > 0.998.", pt_size=12.5, space_after=6)

    deck.add_card(s17_cal, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb16_r = s17_cal.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf16_r = tb16_r.text_frame
    tf16_r.word_wrap = True
    deck.add_card_header(tf16_r, "Tahap 2: Karakterisasi Transfer TMR", accent_color=COLOR_EMERALD, title_size=16)
    deck.add_bullet_item(tf16_r, "Pemasangan Sensor:", "Sensor TMR ALT023 ditempatkan pada statif presisi di pusat medan kumparan Helmholtz.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_r, "Tegangan Nol Medan:", "Pada B = 0 mT, tegangan keluaran bertengger stabil pada Vout = 2.50 V (sesuai VREF AD623).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_r, "Rentang Sapuan Medan:", "Medan disapu bipolar dari -4.0 mT hingga +11.5 mT melintasi rentang linear +/-1.0 mT.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf16_r, "Evaluasi Sensitivitas:", "Sensitivitas diferensial dihitung via turunan numerik spline dV/dB dan regresi linier.", pt_size=12.5, space_after=6)

    deck.add_footer(s17_cal, 17)

    # --------------------------------------------------------------------------
    # SLIDE 18: METODOLOGI: PREPARASI BAKSO & EKSTRAKSI 5 FITUR SINYAL
    # --------------------------------------------------------------------------
    s18_food = deck.add_blank_slide()
    deck.add_header(s18_food, "Metodologi: Preparasi Sampel Bakso & Ekstraksi 5 Fitur Sinyal",
                    "Protokol Ekstraksi Matriks Daging dan Definisi 5 Fitur Sinyal Domain Waktu untuk Model AI")

    deck.add_card(s18_food, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb17_l = s18_food.shapes.add_textbox(Inches(1.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf17_l = tb17_l.text_frame
    tf17_l.word_wrap = True
    deck.add_card_header(tf17_l, "Protokol Ekstraksi Bakso", accent_color=COLOR_ROSE, title_size=16)
    deck.add_bullet_item(tf17_l, "Matriks Sampel Bakso:", "Sampel bakso dibeli dari pedagang pasar tradisional; dihaluskan secara mekanik menggunakan mortar.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_l, "Ekstraksi Pelarut Air:", "10 g sampel bakso halus diekstraksi dalam 50 mL akuades deionisasi pada suhu 60 C selama 15 menit.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_l, "Filtrasi Bertingkat:", "Supernatan disaring kertas saring Whatman No. 42 untuk memisahkan residu lemak dan protein kasar.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_l, "Spiking Bertingkat:", "Ekstrak di-spiking larutan formalin standar konsentrasi terkontrol: 0, 10, 50, 100, 250, dan 500 mg/L.", pt_size=12.5, space_after=6)

    deck.add_card(s18_food, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb17_r = s18_food.shapes.add_textbox(Inches(7.05), Inches(1.75), Inches(5.2), Inches(4.8))
    tf17_r = tb17_r.text_frame
    tf17_r.word_wrap = True
    deck.add_card_header(tf17_r, "5 Fitur Domain Waktu", accent_color=COLOR_BLUE_ACCENT, title_size=16)
    deck.add_bullet_item(tf17_r, "1. Vpeak (Tegangan Puncak):", "Nilai ekstrem tegangan sensor selama window akuisisi pengujian analit.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_r, "2. Vsteady (Tegangan Rerata):", "Rerata tegangan saat sinyal mencapai plateau tunak (setelah settling time 1.0 s).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_r, "3. Delta V (Selisih Tegangan):", "Pergeseran tegangan bersih terhadap garis dasar tanpa analit (baseline delta).", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_r, "4. dV/dt (Laju Transien):", "Kemiringan awal kurva respons sensor sesaat setelah sampel diteteskan.", pt_size=12.5, space_after=6)
    deck.add_bullet_item(tf17_r, "5. Integral Area Sinyal:", "Akumulasi total energi respons tegangan selama 5.0 detik akuisisi.", pt_size=12.5, space_after=6)

    deck.add_footer(s18_food, 18)

    # --------------------------------------------------------------------------
    # SLIDE 19: METODOLOGI: PEMODELAN ML [MURNI 2 FLOWCHART, TANPA TEKS LAIN]
    # --------------------------------------------------------------------------
    s19_ml = deck.add_blank_slide()
    deck.add_header(s19_ml, "Metodologi: Pipeline Pelatihan SVM vs QSVC & Deployment",
                    "Diagram Alir Model Building 5-Fold Cross Validation (Kiri) dan Model Deployment (Kanan)")

    deck.add_image_fitted(s19_ml, "Gambar/Bab3/babIII_ModelBuilding.drawio.png", Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2),
                          border=True, caption="Gambar 13. Diagram Alir Pelatihan dan Validasi Silang SVM vs QSVC")

    deck.add_image_fitted(s19_ml, "Gambar/Bab3/babIII_ModelDeploy.drawio.png", Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2),
                          border=True, caption="Gambar 14. Diagram Alir Deployment Model ke Embedded System")

    deck.add_footer(s19_ml, 19)

    # --------------------------------------------------------------------------
    # DAFTAR PUSTAKA LENGKAP: BACA SEMUA DARI data/all_52_references.txt
    # --------------------------------------------------------------------------
    all_refs = []
    if os.path.exists("data/all_52_references.txt"):
        with open("data/all_52_references.txt", "r", encoding="utf-8") as f_ref:
            for line in f_ref:
                l_str = line.strip()
                if l_str:
                    l_clean = re.sub(r'^\d+\.\s*', '', l_str)
                    all_refs.append(l_clean)
    else:
        print("[PERINGATAN] Berkas data/all_52_references.txt belum ada.")

    print(f"[INFO] Memuat {len(all_refs)} referensi untuk slide Daftar Pustaka.")

    # Bagi rata menjadi 2 slide
    half_idx = (len(all_refs) + 1) // 2
    refs_part1 = all_refs[:half_idx]
    refs_part2 = all_refs[half_idx:]

    # --------------------------------------------------------------------------
    # SLIDE 20: DAFTAR PUSTAKA UTAMA (BAGIAN 1)
    # --------------------------------------------------------------------------
    s20_ref1 = deck.add_blank_slide()
    deck.add_header(s20_ref1, f"Daftar Pustaka Lengkap Naskah Proposal (Bagian 1: Ref 01 - {half_idx:02d})",
                    "Daftar Rujukan Pustaka Ilmiah Bereputasi Sesuai Format Naskah Proposal (Alfabetis A - M)")

    half_col1 = (len(refs_part1) + 1) // 2
    deck.add_card(s20_ref1, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb20_l = s20_ref1.shapes.add_textbox(Inches(0.95), Inches(1.65), Inches(5.4), Inches(5.0))
    tf20_l = tb20_l.text_frame
    tf20_l.word_wrap = True
    for idx, ref_text in enumerate(refs_part1[:half_col1], 1):
        deck.add_bullet_item(tf20_l, f"[{idx:02d}]", ref_text, pt_size=8.5, space_after=3.0)

    deck.add_card(s20_ref1, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb20_r = s20_ref1.shapes.add_textbox(Inches(6.95), Inches(1.65), Inches(5.4), Inches(5.0))
    tf20_r = tb20_r.text_frame
    tf20_r.word_wrap = True
    for idx, ref_text in enumerate(refs_part1[half_col1:], half_col1 + 1):
        deck.add_bullet_item(tf20_r, f"[{idx:02d}]", ref_text, pt_size=8.5, space_after=3.0)

    deck.add_footer(s20_ref1, 20)

    # --------------------------------------------------------------------------
    # SLIDE 21: DAFTAR PUSTAKA UTAMA (BAGIAN 2)
    # --------------------------------------------------------------------------
    s21_ref2 = deck.add_blank_slide()
    deck.add_header(s21_ref2, f"Daftar Pustaka Lengkap Naskah Proposal (Bagian 2: Ref {half_idx+1:02d} - {len(all_refs):02d})",
                    "Daftar Rujukan Pustaka Ilmiah Bereputasi Sesuai Format Naskah Proposal (Alfabetis N - Z)")

    half_col2 = (len(refs_part2) + 1) // 2
    deck.add_card(s21_ref2, Inches(0.8), Inches(1.55), Inches(5.7), Inches(5.2))
    tb21_l = s21_ref2.shapes.add_textbox(Inches(0.95), Inches(1.65), Inches(5.4), Inches(5.0))
    tf21_l = tb21_l.text_frame
    tf21_l.word_wrap = True
    start_num2 = half_idx + 1
    for idx, ref_text in enumerate(refs_part2[:half_col2], start_num2):
        deck.add_bullet_item(tf21_l, f"[{idx:02d}]", ref_text, pt_size=8.5, space_after=3.0)

    deck.add_card(s21_ref2, Inches(6.8), Inches(1.55), Inches(5.733), Inches(5.2))
    tb21_r = s21_ref2.shapes.add_textbox(Inches(6.95), Inches(1.65), Inches(5.4), Inches(5.0))
    tf21_r = tb21_r.text_frame
    tf21_r.word_wrap = True
    for idx, ref_text in enumerate(refs_part2[half_col2:], start_num2 + half_col2):
        deck.add_bullet_item(tf21_r, f"[{idx:02d}]", ref_text, pt_size=8.5, space_after=3.0)

    deck.add_footer(s21_ref2, 21)

    # --------------------------------------------------------------------------
    # SLIDE 22: SLIDE PENUTUP ("TERIMA KASIH")
    # --------------------------------------------------------------------------
    s22_close = deck.add_blank_slide()

    deck.add_card(s22_close, Inches(1.5), Inches(1.2), Inches(10.333), Inches(4.2), bg_color=COLOR_NAVY_DARK, border_color=COLOR_BLUE_ACCENT)
    
    tb22_th = s22_close.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.733), Inches(1.5))
    tf22_th = tb22_th.text_frame
    tf22_th.word_wrap = True
    p22_th = tf22_th.paragraphs[0]
    p22_th.text = "TERIMA KASIH"
    p22_th.font.name = FONT_FAMILY
    p22_th.font.bold = True
    p22_th.font.size = Pt(40)
    p22_th.font.color.rgb = COLOR_CARD_FILL
    p22_th.alignment = PP_ALIGN.CENTER

    p22_sub1 = tf22_th.add_paragraph()
    p22_sub1.text = "SEMINAR PROPOSAL TUGAS AKHIR JURUSAN FISIKA UIN SUNAN GUNUNG DJATI BANDUNG"
    p22_sub1.font.name = FONT_FAMILY
    p22_sub1.font.bold = True
    p22_sub1.font.size = Pt(13)
    p22_sub1.font.color.rgb = COLOR_BLUE_ACCENT
    p22_sub1.alignment = PP_ALIGN.CENTER
    p22_sub1.space_before = Pt(8)

    p22_sub2 = tf22_th.add_paragraph()
    p22_sub2.text = "Rancang Bangun Instrumentasi Sensor TMR Berbasis Nanofiber Fe3O4/PVA-Sitrat-ADH untuk Deteksi Formalin pada Bakso Menggunakan Komparasi Model SVM dan QSVC"
    p22_sub2.font.name = FONT_FAMILY
    p22_sub2.font.size = Pt(12)
    p22_sub2.font.color.rgb = COLOR_LIGHT_SLATE
    p22_sub2.alignment = PP_ALIGN.CENTER
    p22_sub2.space_before = Pt(6)

    deck.add_card(s22_close, Inches(1.5), Inches(5.6), Inches(10.333), Inches(1.2), bg_color=COLOR_CARD_FILL, border_color=COLOR_CARD_BORDER)
    tb22_q = s22_close.shapes.add_textbox(Inches(1.8), Inches(5.75), Inches(9.733), Inches(0.9))
    tf22_q = tb22_q.text_frame
    tf22_q.word_wrap = True
    p22_q = tf22_q.paragraphs[0]
    p22_q.text = "Mohon Arahan, Masukan, dan Saran demi Kesempurnaan Pelaksanaan Tugas Akhir Ini"
    p22_q.font.name = FONT_FAMILY
    p22_q.font.bold = True
    p22_q.font.size = Pt(13)
    p22_q.font.color.rgb = COLOR_NAVY_DARK
    p22_q.alignment = PP_ALIGN.CENTER

    p22_qsub = tf22_q.add_paragraph()
    p22_qsub.text = "Sesi Tanya Jawab dan Diskusi Akademik Dibuka"
    p22_qsub.font.name = FONT_FAMILY
    p22_qsub.font.bold = True
    p22_qsub.font.size = Pt(12)
    p22_qsub.font.color.rgb = COLOR_BLUE_ACCENT
    p22_qsub.alignment = PP_ALIGN.CENTER
    p22_qsub.space_before = Pt(4)

    deck.add_footer(s22_close, 22)

    # --------------------------------------------------------------------------
    # SIMPAN KE FILE PPTX
    # --------------------------------------------------------------------------
    deck.save()

if __name__ == "__main__":
    build_presentation()
