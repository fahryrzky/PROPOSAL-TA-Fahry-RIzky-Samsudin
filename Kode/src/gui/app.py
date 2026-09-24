"""
================================================================================
src/gui/app.py
================================================================================
Aplikasi Utama Antarmuka CustomTkinter Instrumentasi & Kalibrasi Sensor TMR
================================================================================
"""

import os
import sys
import time
import threading
from datetime import datetime
import numpy as np

import customtkinter as ctk
from tkinter import filedialog, messagebox

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ..config import (
    PALETTE,
    ADS1115_LSB,
    AD623_VREF,
    HELMHOLTZ_COIL_R,
    HELMHOLTZ_K,
    DEFAULT_DURATION_S,
    DEFAULT_SETTLE_S,
)
from ..style import scatter_bola
from ..serial_worker import SerialManager, scan_serial_ports
from ..acquisition import StreamBuffer, DurationAcquisitionEngine
from ..analysis import CalibrationAnalyzer
from ..export_handler import (
    export_calibration_report,
    export_stream_data,
    export_high_res_plots,
)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class TMRAcquisitionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Jendela Utama
        self.title("Instrumentasi Sensor TMR ALT023-10E — Karakterisasi Medan Magnet Helmholtz")
        self.geometry("1440x900")
        self.minsize(1200, 760)
        self.configure(fg_color=PALETTE["bg_dark"])

        # Inisialisasi Modul Backend
        self.serial_mgr = SerialManager()
        self.acq_engine = DurationAcquisitionEngine(self.serial_mgr)
        self.stream_buf = StreamBuffer(max_points=150)
        self.analyzer = CalibrationAnalyzer()

        # State Aplikasi
        self.polarity = 1  # +1 = Maju, -1 = Balik Polaritas
        self.calibration_points = []
        self.latest_v = AD623_VREF
        self.latest_b = 0.0000
        self.latest_adc = int(AD623_VREF / ADS1115_LSB)
        self.last_logged_sec = -1

        # Bangun Tampilan
        self._build_header()
        self._build_body()

        # Muat Konstanta Kalibrasi Tersimpan dari Disk (Jika Ada)
        self._load_saved_calibration_constants()

        # Mulai Polling Real-Time
        self.after(200, self._poll_stream)

        # Log Selamat Datang
        self.log_message("Sistem Instrumentasi Sensor TMR ALT023-10E modular aktif.")
        self.log_message(f"ADS1115 dikonfigurasi pada rentang 5V (PGA GAIN_TWOTHIRDS, LSB = {ADS1115_LSB*1000:.4f} mV).")
        self.log_message("Akuisisi titik berbasis DURASI WAKTU (Lama Detik) siap digunakan.")

    # ------------------------------------------------------------------
    # 1. HEADER
    # ------------------------------------------------------------------
    def _build_header(self):
        header_frame = ctk.CTkFrame(
            self,
            fg_color=PALETTE["card_dark"],
            corner_radius=0,
            border_width=1,
            border_color=PALETTE["card_border"],
            height=65,
        )
        header_frame.pack(fill="x", side="top")

        left_box = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_box.pack(side="left", padx=20, pady=10)

        ctk.CTkLabel(
            left_box,
            text="⊙",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=PALETTE["emerald"],
        ).pack(side="left", padx=(0, 12))

        title_box = ctk.CTkFrame(left_box, fg_color="transparent")
        title_box.pack(side="left")

        ctk.CTkLabel(
            title_box,
            text="TMR ALT023-10E Sensor Acquisition & Helmholtz Characterization",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=PALETTE["text_main"],
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_box,
            text=f"Signal Chain: ALT023-10E -> AD623 IA (V_REF={AD623_VREF:.2f}V) -> ADS1115 16-Bit @ 5V -> Arduino Uno",
            font=ctk.CTkFont(size=11),
            text_color=PALETTE["text_sub"],
        ).pack(anchor="w")

        right_box = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_box.pack(side="right", padx=20, pady=10)

        self.badge_status = ctk.CTkLabel(
            right_box,
            text="● Offline",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=PALETTE["rose"],
            fg_color="#2b1820",
            corner_radius=6,
            padx=10,
            pady=4,
        )
        self.badge_status.pack(side="right", padx=(8, 0))

        self.badge_calib = ctk.CTkLabel(
            right_box,
            text="Kalibrasi: Belum Ada",
            font=ctk.CTkFont(size=11),
            text_color=PALETTE["text_sub"],
            fg_color=PALETTE["bg_dark"],
            corner_radius=6,
            padx=10,
            pady=4,
        )
        self.badge_calib.pack(side="right")

    # ------------------------------------------------------------------
    # 2. BODY LAYOUT
    # ------------------------------------------------------------------
    def _build_body(self):
        body_container = ctk.CTkFrame(self, fg_color="transparent")
        body_container.pack(fill="both", expand=True, padx=14, pady=10)

        # Panel Kiri (Visualisasi)
        left_panel = ctk.CTkFrame(body_container, fg_color="transparent")
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Panel Kanan (Kontrol)
        right_panel = ctk.CTkScrollableFrame(
            body_container,
            fg_color=PALETTE["card_dark"],
            corner_radius=12,
            border_width=1,
            border_color=PALETTE["card_border"],
            width=370,
        )
        right_panel.pack(side="right", fill="y", padx=0)

        self._build_telemetry_cards(left_panel)
        self._build_tabs_and_plots(left_panel)
        self._build_console_log(left_panel)

        self._build_sidebar_controls(right_panel)

    # ------------------------------------------------------------------
    # 2.1 TELEMETRI HERO CARDS
    # ------------------------------------------------------------------
    def _build_telemetry_cards(self, parent):
        cards_frame = ctk.CTkFrame(parent, fg_color="transparent")
        cards_frame.pack(fill="x", pady=(0, 10))

        # Card 1: Tegangan Output V (AD623)
        c1 = ctk.CTkFrame(cards_frame, fg_color=PALETTE["card_dark"], corner_radius=10, border_width=1, border_color=PALETTE["card_border"])
        c1.pack(side="left", fill="both", expand=True, padx=(0, 8))

        ctk.CTkLabel(c1, text="TEGANGAN OUTPUT SENSOR (V)", font=ctk.CTkFont(size=10, weight="bold"), text_color=PALETTE["teal"]).pack(anchor="w", padx=14, pady=(10, 2))
        self.lbl_card_v = ctk.CTkLabel(c1, text=f"{AD623_VREF:.4f} V", font=ctk.CTkFont(size=26, weight="bold"), text_color=PALETTE["text_main"])
        self.lbl_card_v.pack(anchor="w", padx=14, pady=0)
        self.lbl_card_v_sub = ctk.CTkLabel(c1, text=f"ADC: {self.latest_adc} LSB (ADS1115 @ 5V)", font=ctk.CTkFont(size=10), text_color=PALETTE["text_sub"])
        self.lbl_card_v_sub.pack(anchor="w", padx=14, pady=(0, 10))

        # Card 2: Medan Magnet B (mT)
        c2 = ctk.CTkFrame(cards_frame, fg_color=PALETTE["card_dark"], corner_radius=10, border_width=1, border_color=PALETTE["card_border"])
        c2.pack(side="left", fill="both", expand=True, padx=(0, 8))

        ctk.CTkLabel(c2, text="MEDAN MAGNET TERUKUR B (mT)", font=ctk.CTkFont(size=10, weight="bold"), text_color=PALETTE["emerald"]).pack(anchor="w", padx=14, pady=(10, 2))
        self.lbl_card_b = ctk.CTkLabel(c2, text="0.0000 mT", font=ctk.CTkFont(size=26, weight="bold"), text_color=PALETTE["text_main"])
        self.lbl_card_b.pack(anchor="w", padx=14, pady=0)
        self.lbl_card_b_sub = ctk.CTkLabel(c2, text="Konversi aktif dari kalibrasi", font=ctk.CTkFont(size=10), text_color=PALETTE["text_sub"])
        self.lbl_card_b_sub.pack(anchor="w", padx=14, pady=(0, 10))

        # Card 3: Power Supply Helmholtz (0 - 16 V)
        c3 = ctk.CTkFrame(cards_frame, fg_color=PALETTE["card_dark"], corner_radius=10, border_width=1, border_color=PALETTE["card_border"])
        c3.pack(side="left", fill="both", expand=True, padx=0)

        ctk.CTkLabel(c3, text="POWER SUPPLY HELMHOLTZ (0 - 16 V)", font=ctk.CTkFont(size=10, weight="bold"), text_color=PALETTE["amber"]).pack(anchor="w", padx=14, pady=(10, 2))
        self.lbl_card_helm = ctk.CTkLabel(c3, text="0.00 V  |  0.00 A", font=ctk.CTkFont(size=26, weight="bold"), text_color=PALETTE["text_main"])
        self.lbl_card_helm.pack(anchor="w", padx=14, pady=0)
        self.lbl_card_helm_sub = ctk.CTkLabel(c3, text=f"Daya Kumparan: 0.0 W • R_coil ~ {HELMHOLTZ_COIL_R} Ω", font=ctk.CTkFont(size=10), text_color=PALETTE["text_sub"])
        self.lbl_card_helm_sub.pack(anchor="w", padx=14, pady=(0, 10))

    # ------------------------------------------------------------------
    # 2.2 TABVIEW & GRAFIK MATPLOTLIB
    # ------------------------------------------------------------------
    def _build_tabs_and_plots(self, parent):
        self.tabview = ctk.CTkTabview(
            parent,
            fg_color=PALETTE["card_dark"],
            segmented_button_fg_color=PALETTE["bg_dark"],
            segmented_button_selected_color=PALETTE["emerald_dark"],
            segmented_button_selected_hover_color=PALETTE["emerald"],
            segmented_button_unselected_hover_color=PALETTE["card_border"],
            corner_radius=10,
            border_width=1,
            border_color=PALETTE["card_border"],
        )
        self.tabview.pack(fill="both", expand=True, pady=(0, 8))

        self.tab_stream = self.tabview.add("📈 Real-Time Stream B(t)")
        self.tab_calib = self.tabview.add("🔬 Kurva Kalibrasi V vs B")
        self.tab_sens = self.tabview.add("⚡ Analisis Sensitivitas dV/dB")
        self.tab_table = self.tabview.add("📋 Tabel Titik Kalibrasi")

        self._init_stream_plot(self.tab_stream)
        self._init_calib_plot(self.tab_calib)
        self._init_sens_plot(self.tab_sens)
        self._init_data_table(self.tab_table)

    def _init_stream_plot(self, parent):
        self.fig_stream, self.ax_stream = plt.subplots(figsize=(8, 3.8), facecolor=PALETTE["card_dark"])
        self.ax_stream.set_facecolor(PALETTE["plot_bg"])
        self.ax_stream.set_title("Medan Magnet Real-Time B (mT) vs Waktu", color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8)
        self.ax_stream.set_xlabel("Waktu, t (s)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_stream.set_ylabel("Medan Magnet, B (mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_stream.tick_params(colors=PALETTE["text_sub"], labelsize=8)
        for s in self.ax_stream.spines.values():
            s.set_color(PALETTE["plot_spine"])
        self.ax_stream.grid(True, color=PALETTE["plot_grid"], linestyle="--", linewidth=0.7)

        self.line_stream, = self.ax_stream.plot([], [], color=PALETTE["emerald"], lw=1.8, label="Medan Magnet B (mT)")
        self.ax_stream.legend(loc="upper right", facecolor=PALETTE["card_dark"], edgecolor=PALETTE["plot_spine"], labelcolor=PALETTE["text_main"], fontsize=8)

        self.canvas_stream = FigureCanvasTkAgg(self.fig_stream, master=parent)
        self.canvas_stream.get_tk_widget().pack(fill="both", expand=True, padx=4, pady=4)
        self.canvas_stream.draw()

    def _init_calib_plot(self, parent):
        self.fig_calib, self.ax_calib = plt.subplots(figsize=(8, 3.8), facecolor=PALETTE["card_dark"])
        self.ax_calib.set_facecolor(PALETTE["plot_bg"])
        self.ax_calib.set_title("Karakterisasi Tegangan TMR vs Medan Magnet B", color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8)
        self.ax_calib.set_xlabel("Medan Magnet B (mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_calib.set_ylabel("Tegangan Output V (Volt)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_calib.tick_params(colors=PALETTE["text_sub"], labelsize=8)
        for s in self.ax_calib.spines.values():
            s.set_color(PALETTE["plot_spine"])
        self.ax_calib.grid(True, color=PALETTE["plot_grid"], linestyle="--", linewidth=0.7)

        self.canvas_calib = FigureCanvasTkAgg(self.fig_calib, master=parent)
        self.canvas_calib.get_tk_widget().pack(fill="both", expand=True, padx=4, pady=4)
        self.canvas_calib.draw()

    def _init_sens_plot(self, parent):
        self.fig_sens, self.ax_sens = plt.subplots(figsize=(8, 3.8), facecolor=PALETTE["card_dark"])
        self.ax_sens.set_facecolor(PALETTE["plot_bg"])
        self.ax_sens.set_title("Sensitivitas Sensor dV/dB vs B (Cubic Spline Derivative)", color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8)
        self.ax_sens.set_xlabel("Medan Magnet B (mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_sens.set_ylabel("Sensitivitas dV/dB (V/mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_sens.tick_params(colors=PALETTE["text_sub"], labelsize=8)
        for s in self.ax_sens.spines.values():
            s.set_color(PALETTE["plot_spine"])
        self.ax_sens.grid(True, color=PALETTE["plot_grid"], linestyle="--", linewidth=0.7)

        self.canvas_sens = FigureCanvasTkAgg(self.fig_sens, master=parent)
        self.canvas_sens.get_tk_widget().pack(fill="both", expand=True, padx=4, pady=4)
        self.canvas_sens.draw()

    def _init_data_table(self, parent):
        self.txt_table = ctk.CTkTextbox(
            parent,
            fg_color=PALETTE["plot_bg"],
            text_color=PALETTE["text_main"],
            font=ctk.CTkFont(family="Consolas", size=10),
            corner_radius=8,
            border_width=1,
            border_color=PALETTE["plot_spine"],
        )
        self.txt_table.pack(fill="both", expand=True, padx=8, pady=8)
        self._refresh_table_view()

    # ------------------------------------------------------------------
    # 2.3 CONSOLE LOG
    # ------------------------------------------------------------------
    def _build_console_log(self, parent):
        log_frame = ctk.CTkFrame(parent, fg_color=PALETTE["card_dark"], corner_radius=10, border_width=1, border_color=PALETTE["card_border"], height=95)
        log_frame.pack(fill="x", side="bottom")

        ctk.CTkLabel(log_frame, text="≡  LOG AKTIVITAS SISTEM", font=ctk.CTkFont(size=10, weight="bold"), text_color=PALETTE["text_sub"]).pack(anchor="w", padx=12, pady=(5, 2))

        self.txt_log = ctk.CTkTextbox(
            log_frame,
            fg_color="#0e1726",
            text_color="#38bdf8",
            font=ctk.CTkFont(family="Consolas", size=10),
            height=65,
            corner_radius=6,
        )
        self.txt_log.pack(fill="x", padx=10, pady=(0, 6))

    def log_message(self, text):
        ts = datetime.now().strftime("%H:%M:%S")
        self.txt_log.insert("end", f"[{ts}]  {text}\n")
        self.txt_log.see("end")

    # ------------------------------------------------------------------
    # 3. SIDEBAR KONTROL (Kanan)
    # ------------------------------------------------------------------
    def _build_sidebar_controls(self, parent):
        # SEC 1: SERIAL KONEKSI
        sec1 = self._create_card(parent, "🔌 KONEKSI SERIAL ARDUINO")
        ctk.CTkLabel(sec1, text="Port COM:", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).pack(anchor="w", padx=12, pady=(6, 2))

        self.port_var = ctk.StringVar(value="[SIMULASI / DUMMY]")
        self.cbo_port = ctk.CTkComboBox(sec1, variable=self.port_var, values=scan_serial_ports(), fg_color=PALETTE["bg_dark"], border_color=PALETTE["card_border"])
        self.cbo_port.pack(fill="x", padx=12, pady=(0, 6))

        btn_row_port = ctk.CTkFrame(sec1, fg_color="transparent")
        btn_row_port.pack(fill="x", padx=12, pady=(0, 10))

        self.btn_connect = ctk.CTkButton(
            btn_row_port,
            text="Hubungkan",
            command=self._toggle_connection,
            fg_color=PALETTE["emerald_dark"],
            hover_color=PALETTE["emerald"],
            font=ctk.CTkFont(size=12, weight="bold"),
            height=32,
        )
        self.btn_connect.pack(side="left", fill="x", expand=True, padx=(0, 4))

        ctk.CTkButton(
            btn_row_port,
            text="↻ Scan",
            width=55,
            command=lambda: self.cbo_port.configure(values=scan_serial_ports()),
            fg_color=PALETTE["card_border"],
            hover_color="#3b4b72",
            height=32,
        ).pack(side="right")

        # SEC 2: HELMHOLTZ POWER SUPPLY (0 - 16 V)
        sec2 = self._create_card(parent, "⚡ POWER SUPPLY HELMHOLTZ (0 - 16 V)")

        self.switch_mode_external = ctk.CTkSwitch(
            sec2, text="Pengaturan Eksternal (Manual Lab)", command=self._on_mode_external_changed,
            progress_color=PALETTE["emerald"]
        )
        self.switch_mode_external.select()
        self.switch_mode_external.pack(anchor="w", padx=12, pady=(6, 2))

        self.lbl_mode_info = ctk.CTkLabel(
            sec2, text="📌 Mode Eksternal: Input manual dari instrumen lab. Nilai I & B tidak di-override slider.",
            font=ctk.CTkFont(size=10), text_color=PALETTE["emerald"], wraplength=340, justify="left"
        )
        self.lbl_mode_info.pack(anchor="w", padx=12, pady=(0, 6))

        ctk.CTkLabel(sec2, text="Tegangan Output DC (0.0 - 16.0 V):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).pack(anchor="w", padx=12, pady=(2, 2))

        self.slider_vhelm = ctk.CTkSlider(
            sec2, from_=0.0, to=16.0, number_of_steps=160, command=self._on_slider_vhelm,
            progress_color=PALETTE["amber"], button_color=PALETTE["amber"]
        )
        self.slider_vhelm.set(0.0)
        self.slider_vhelm.pack(fill="x", padx=12, pady=(2, 6))

        preset_frame = ctk.CTkFrame(sec2, fg_color="transparent")
        preset_frame.pack(fill="x", padx=10, pady=(0, 6))
        for v in [0, 2, 4, 6, 8, 10, 12, 14, 16]:
            ctk.CTkButton(
                preset_frame, text=f"{v}V", width=32, height=24, font=ctk.CTkFont(size=9),
                fg_color=PALETTE["bg_dark"], hover_color=PALETTE["amber"],
                command=lambda val=v: self._set_vhelm_preset(val)
            ).pack(side="left", expand=True, padx=1)

        param_grid = ctk.CTkFrame(sec2, fg_color="transparent")
        param_grid.pack(fill="x", padx=12, pady=(4, 6))

        ctk.CTkLabel(param_grid, text="V_helm (V):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).grid(row=0, column=0, sticky="w", pady=2)
        self.entry_vhelm = ctk.CTkEntry(param_grid, width=80, height=28, fg_color=PALETTE["bg_dark"])
        self.entry_vhelm.insert(0, "0.00")
        self.entry_vhelm.grid(row=0, column=1, sticky="e", pady=2)
        self.entry_vhelm.bind("<KeyRelease>", self._on_entry_vhelm)

        ctk.CTkLabel(param_grid, text="Arus I_helm (A):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).grid(row=1, column=0, sticky="w", pady=2)
        self.entry_ihelm = ctk.CTkEntry(param_grid, width=80, height=28, fg_color=PALETTE["bg_dark"])
        self.entry_ihelm.insert(0, "0.00")
        self.entry_ihelm.grid(row=1, column=1, sticky="e", pady=2)
        self.entry_ihelm.bind("<KeyRelease>", self._on_entry_helm_params)

        ctk.CTkLabel(param_grid, text="B Teslameter (mT):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).grid(row=2, column=0, sticky="w", pady=2)
        self.entry_btesla = ctk.CTkEntry(param_grid, width=80, height=28, fg_color=PALETTE["bg_dark"])
        self.entry_btesla.insert(0, "0.000")
        self.entry_btesla.grid(row=2, column=1, sticky="e", pady=2)
        self.entry_btesla.bind("<KeyRelease>", self._on_entry_helm_params)

        self.switch_polarity = ctk.CTkSwitch(sec2, text="Arah Arus: [+] Maju (+B)", command=self._on_polarity_changed, progress_color=PALETTE["emerald"])
        self.switch_polarity.select()
        self.switch_polarity.pack(anchor="w", padx=12, pady=(4, 10))

        # SEC 3: AKUISISI BERBASIS DURASI DETIK
        sec3 = self._create_card(parent, "⏱️ AKUISISI BERBASIS DURASI DETIK")

        dur_grid = ctk.CTkFrame(sec3, fg_color="transparent")
        dur_grid.pack(fill="x", padx=12, pady=(6, 4))

        ctk.CTkLabel(dur_grid, text="Lama Akuisisi (s):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).grid(row=0, column=0, sticky="w", pady=2)
        self.entry_duration = ctk.CTkEntry(dur_grid, width=80, height=28, fg_color=PALETTE["bg_dark"])
        self.entry_duration.insert(0, str(DEFAULT_DURATION_S))
        self.entry_duration.grid(row=0, column=1, sticky="e", pady=2)

        ctk.CTkLabel(dur_grid, text="Settling Time (s):", font=ctk.CTkFont(size=11), text_color=PALETTE["text_sub"]).grid(row=1, column=0, sticky="w", pady=2)
        self.entry_settle = ctk.CTkEntry(dur_grid, width=80, height=28, fg_color=PALETTE["bg_dark"])
        self.entry_settle.insert(0, str(DEFAULT_SETTLE_S))
        self.entry_settle.grid(row=1, column=1, sticky="e", pady=2)

        # Tombol Preset Durasi
        dur_preset_frame = ctk.CTkFrame(sec3, fg_color="transparent")
        dur_preset_frame.pack(fill="x", padx=10, pady=(2, 6))
        for d_sec in [3, 5, 10, 15, 30]:
            ctk.CTkButton(
                dur_preset_frame, text=f"{d_sec}s", width=30, height=22, font=ctk.CTkFont(size=9),
                fg_color=PALETTE["bg_dark"], hover_color=PALETTE["teal"],
                command=lambda ds=d_sec: self._set_duration_preset(ds)
            ).pack(side="left", expand=True, padx=1)

        self.progress_acq = ctk.CTkProgressBar(sec3, progress_color=PALETTE["emerald"])
        self.progress_acq.set(0.0)
        self.progress_acq.pack(fill="x", padx=12, pady=(4, 6))

        self.lbl_progress_info = ctk.CTkLabel(sec3, text="Siap mengambil data titik.", font=ctk.CTkFont(size=10), text_color=PALETTE["text_sub"])
        self.lbl_progress_info.pack(anchor="w", padx=12, pady=(0, 6))

        self.btn_acquire = ctk.CTkButton(
            sec3, text="▶ Ambil Sampel Titik Ini", command=self._start_duration_acquisition,
            fg_color=PALETTE["emerald_dark"], hover_color=PALETTE["emerald"],
            font=ctk.CTkFont(size=12, weight="bold"), height=34
        )
        self.btn_acquire.pack(fill="x", padx=12, pady=(0, 6))

        ctk.CTkButton(
            sec3, text="⚡ Muat Data Demo (Sweep 0 - 16V)", command=self._load_demo_sweep,
            fg_color="#1e3a5f", hover_color="#2b5288", font=ctk.CTkFont(size=11, weight="bold"), height=30
        ).pack(fill="x", padx=12, pady=(0, 6))

        btn_row_manage = ctk.CTkFrame(sec3, fg_color="transparent")
        btn_row_manage.pack(fill="x", padx=12, pady=(0, 10))

        ctk.CTkButton(btn_row_manage, text="Hapus Terakhir", command=self._delete_last_point, fg_color=PALETTE["card_border"], hover_color="#475569", font=ctk.CTkFont(size=10), height=28).pack(side="left", fill="x", expand=True, padx=(0, 3))
        ctk.CTkButton(btn_row_manage, text="Reset Semua", command=self._reset_all_data, fg_color="#451a24", hover_color=PALETTE["rose"], font=ctk.CTkFont(size=10), height=28).pack(side="right", fill="x", expand=True, padx=(3, 0))

        # SEC 4: EKSPOR & REPRODUSIBILITAS
        sec4 = self._create_card(parent, "💾 EKSPOR DATA & PUBLIKASI")

        ctk.CTkButton(
            sec4, text="📊 Simpan Laporan Kalibrasi (.xlsx)", command=self._export_calibration_excel,
            fg_color="#15803d", hover_color="#16a34a", font=ctk.CTkFont(size=11, weight="bold"), height=30
        ).pack(fill="x", padx=12, pady=(6, 4))

        ctk.CTkButton(
            sec4, text="📈 Simpan Stream Data Real-Time (.xlsx)", command=self._export_stream_excel,
            fg_color="#0d9488", hover_color="#14b8a6", font=ctk.CTkFont(size=11, weight="bold"), height=30
        ).pack(fill="x", padx=12, pady=(0, 4))

        ctk.CTkButton(
            sec4, text="🐍 Ekspor Modul konversi_B.py", command=self._export_python_module,
            fg_color="#0369a1", hover_color="#0284c7", font=ctk.CTkFont(size=11, weight="bold"), height=30
        ).pack(fill="x", padx=12, pady=(0, 4))

        ctk.CTkButton(
            sec4, text="🖼️ Simpan Gambar Kurva (.png)", command=self._export_png_plots,
            fg_color=PALETTE["card_border"], hover_color="#475569", font=ctk.CTkFont(size=11), height=30
        ).pack(fill="x", padx=12, pady=(0, 10))

    def _create_card(self, parent, title):
        card = ctk.CTkFrame(parent, fg_color=PALETTE["bg_dark"], corner_radius=10, border_width=1, border_color=PALETTE["card_border"])
        card.pack(fill="x", padx=4, pady=6)
        ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=11, weight="bold"), text_color=PALETTE["text_main"]).pack(anchor="w", padx=12, pady=(8, 2))
        ctk.CTkFrame(card, fg_color=PALETTE["card_border"], height=1).pack(fill="x", padx=10, pady=(0, 4))
        return card

    # ------------------------------------------------------------------
    # 4. KONEKSI & REAL-TIME STREAMING
    # ------------------------------------------------------------------
    def _toggle_connection(self):
        if self.serial_mgr.is_connected:
            self.serial_mgr.disconnect()
            self.badge_status.configure(text="● Offline", text_color=PALETTE["rose"], fg_color="#2b1820")
            self.btn_connect.configure(text="Hubungkan", fg_color=PALETTE["emerald_dark"], hover_color=PALETTE["emerald"])
            self.log_message("Koneksi serial ditutup.")
        else:
            port = self.port_var.get()
            ok, msg = self.serial_mgr.connect(port)
            if ok:
                if self.serial_mgr.is_simulated:
                    self.badge_status.configure(text="● Simulasi Aktif", text_color=PALETTE["teal"], fg_color="#132e3d")
                    self.switch_mode_external.deselect()
                    self._on_mode_external_changed()
                else:
                    self.badge_status.configure(text=f"● Terhubung ({port})", text_color=PALETTE["emerald"], fg_color="#103325")
                    self.switch_mode_external.select()
                    self._on_mode_external_changed()
                    self.log_message(f"[HARDWARE] Port fisik {port} terhubung.")
                    self.log_message("  Parameter Helmholtz diset ke: PENGATURAN EKSTERNAL (Manual Lab).")
                    self.log_message("  Nilai V, I, dan B dicatat langsung dari instrumen fisik lab;")
                    self.log_message("  Slider/parameter di GUI TIDAK akan mengirim perintah hardware atau mengubah hasil ukur.")
                self.btn_connect.configure(text="Putuskan", fg_color=PALETTE["rose"], hover_color="#be123c")
                self.log_message(msg)
            else:
                messagebox.showerror("Gagal Koneksi", f"Gagal membuka port {port}:\n{msg}")

    def _poll_stream(self):
        try:
            if not self.winfo_exists():
                return
        except Exception:
            return

        if self.serial_mgr.is_connected and not self.acq_engine.is_running:
            line = self.serial_mgr.read_line()
            if line and not line.startswith("#"):
                parts = line.split(",")
                if len(parts) >= 5:
                    try:
                        v_val = float(parts[3])
                        adc_val = int(parts[2])

                        self.latest_v = v_val
                        self.latest_adc = adc_val

                        # Konversi V -> B menggunakan regresi aktif
                        if self.analyzer.slope and self.analyzer.slope != 0:
                            self.latest_b = (v_val - self.analyzer.intercept) / self.analyzer.slope
                        else:
                            self.latest_b = (v_val - AD623_VREF) / 0.1427

                        # Tambahkan ke buffer
                        t_now = self.stream_buf.add_sample(v_val, self.latest_b)

                        # Update Hero Cards
                        self.lbl_card_v.configure(text=f"{v_val:.4f} V")
                        self.lbl_card_v_sub.configure(text=f"ADC: {adc_val} LSB (ADS1115 @ 5V)")
                        self.lbl_card_b.configure(text=f"{self.latest_b:+.4f} mT")
                        if self.analyzer.slope and self.analyzer.intercept:
                            self.lbl_card_b_sub.configure(text=f"B = (V - {self.analyzer.intercept:.4f}) / {self.analyzer.slope:.4f}")

                        # Update Grafik Stream B(t)
                        self.line_stream.set_data(self.stream_buf.times, self.stream_buf.b_fields)
                        self.ax_stream.set_title(
                            f"Medan Magnet Real-Time B(t)  [B = {self.latest_b:+.4f} mT  |  V = {v_val:.4f} V]",
                            color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8
                        )
                        self.ax_stream.relim()
                        self.ax_stream.autoscale_view()
                        self.canvas_stream.draw_idle()

                        # Cetak Log Berkala ala Mas Gilang (setiap 2 detik)
                        curr_sec = int(t_now)
                        if curr_sec != self.last_logged_sec and curr_sec % 2 == 0:
                            self.last_logged_sec = curr_sec
                            self.log_message(f"t = {t_now:.2f} s | V = {v_val:.4f} V | B = {self.latest_b:+.4f} mT (ADC: {adc_val})")
                    except Exception:
                        pass

        try:
            if self.winfo_exists():
                self.after(50, self._poll_stream)
        except Exception:
            pass

    # ------------------------------------------------------------------
    # 5. HELMHOLTZ LOGIC
    # ------------------------------------------------------------------
    def _on_mode_external_changed(self):
        if self.switch_mode_external.get() == 1:
            self.lbl_mode_info.configure(
                text="📌 Mode Eksternal: Input manual dari instrumen lab. Nilai I & B tidak di-override slider.",
                text_color=PALETTE["emerald"]
            )
            self.log_message("Mode Helmholtz: Pengaturan Eksternal aktif (Alat ukur manual lab).")
        else:
            self.lbl_mode_info.configure(
                text="⚡ Mode Simulasi: Slider menghitung estimasi teori I = V/R & B = K·I.",
                text_color=PALETTE["amber"]
            )
            self.log_message("Mode Helmholtz: Simulasi / Auto-Kalkulasi aktif.")
            try:
                v = float(self.entry_vhelm.get().strip())
                self._update_helmholtz_calculations(v)
            except ValueError:
                pass

    def _on_slider_vhelm(self, value):
        v = round(value, 2)
        self.entry_vhelm.delete(0, "end")
        self.entry_vhelm.insert(0, f"{v:.2f}")
        self._update_helmholtz_calculations(v)

    def _on_entry_vhelm(self, event=None):
        try:
            val = float(self.entry_vhelm.get().strip())
            val = max(0.0, min(16.0, val))
            self.slider_vhelm.set(val)
            self._update_helmholtz_calculations(val)
        except ValueError:
            pass

    def _on_entry_helm_params(self, event=None):
        """Dipanggil saat user mengetik I_helm atau B_teslameter secara manual dari alat lab."""
        try:
            v_helm = float(self.entry_vhelm.get().strip())
        except ValueError:
            v_helm = 0.0
        try:
            i_helm = float(self.entry_ihelm.get().strip())
        except ValueError:
            i_helm = 0.0
        try:
            b_val = float(self.entry_btesla.get().strip())
        except ValueError:
            b_val = 0.0

        power = v_helm * i_helm
        pol_sign = "+" if self.polarity > 0 else "-"
        self.lbl_card_helm.configure(text=f"{pol_sign}{v_helm:.2f} V  |  {i_helm:.2f} A")
        self.lbl_card_helm_sub.configure(text=f"Daya: {power:.2f} W • Pol: {pol_sign} • B: {b_val:.3f} mT")

    def _set_vhelm_preset(self, val):
        self.slider_vhelm.set(val)
        self.entry_vhelm.delete(0, "end")
        self.entry_vhelm.insert(0, f"{val:.2f}")
        self._update_helmholtz_calculations(val)
        self.log_message(f"Tegangan Helmholtz diset ke: {val:.1f} V")

    def _on_polarity_changed(self):
        if self.switch_polarity.get() == 1:
            self.polarity = 1
            self.switch_polarity.configure(text="Arah Arus: [+] Maju (+B)")
        else:
            self.polarity = -1
            self.switch_polarity.configure(text="Arah Arus: [-] Balik Polaritas (-B)")

        try:
            v = float(self.entry_vhelm.get().strip())
            self._update_helmholtz_calculations(v)
        except ValueError:
            pass

    def _update_helmholtz_calculations(self, v_helm):
        is_external = (
            self.switch_mode_external.get() == 1
            or (self.serial_mgr.is_connected and not self.serial_mgr.is_simulated)
        )

        if not is_external:
            # Mode Simulasi / Kalkulasi Teori Otomatis
            i_helm = v_helm / HELMHOLTZ_COIL_R
            b_est = self.polarity * (HELMHOLTZ_K * i_helm)

            self.entry_ihelm.delete(0, "end")
            self.entry_ihelm.insert(0, f"{i_helm:.2f}")

            self.entry_btesla.delete(0, "end")
            self.entry_btesla.insert(0, f"{b_est:.3f}")

            if self.serial_mgr.is_simulated and self.serial_mgr.ser:
                self.serial_mgr.ser.write(f"{b_est}\n".encode())
        else:
            # Mode Eksternal / Hardware Fisik: JANGAN PERNAH menimpa isian I_helm & B_teslameter!
            # Nilai diambil murni dari input manual yang dibaca user dari alat lab
            try:
                i_helm = float(self.entry_ihelm.get().strip())
            except ValueError:
                i_helm = v_helm / HELMHOLTZ_COIL_R
            try:
                b_est = float(self.entry_btesla.get().strip())
            except ValueError:
                b_est = 0.0

        power = v_helm * i_helm
        pol_sign = "+" if self.polarity > 0 else "-"
        self.lbl_card_helm.configure(text=f"{pol_sign}{v_helm:.2f} V  |  {i_helm:.2f} A")
        self.lbl_card_helm_sub.configure(text=f"Daya: {power:.2f} W • Pol: {pol_sign} • B_target: {b_est:.3f} mT")

    def _set_duration_preset(self, d_sec):
        self.entry_duration.delete(0, "end")
        self.entry_duration.insert(0, f"{d_sec:.1f}")
        self.log_message(f"Durasi akuisisi diatur ke: {d_sec} detik.")

    # ------------------------------------------------------------------
    # 6. AKUISISI BERBASIS DURASI DETIK
    # ------------------------------------------------------------------
    def _start_duration_acquisition(self):
        if not self.serial_mgr.is_connected:
            messagebox.showwarning("Peringatan", "Harap hubungkan port serial atau aktifkan mode [SIMULASI] terlebih dahulu.")
            return

        if self.acq_engine.is_running:
            return

        try:
            v_helm = float(self.entry_vhelm.get().strip())
            i_helm = float(self.entry_ihelm.get().strip())
            b_tesla = float(self.entry_btesla.get().strip())
            duration_s = float(self.entry_duration.get().strip())
            settle_s = float(self.entry_settle.get().strip())
        except ValueError:
            messagebox.showerror("Input Tidak Valid", "Pastikan seluruh parameter angka valid.")
            return

        if duration_s <= settle_s:
            messagebox.showerror("Durasi Terlalu Pendek", f"Durasi akuisisi ({duration_s}s) harus lebih besar dari waktu settling ({settle_s}s).")
            return

        self.btn_acquire.configure(state="disabled", text="Sedang Mengakuisisi...")
        self.progress_acq.set(0.0)

        threading.Thread(
            target=self._worker_acquisition,
            args=(v_helm, i_helm, b_tesla, duration_s, settle_s),
            daemon=True,
        ).start()

    def _worker_acquisition(self, v_helm, i_helm, b_tesla, duration_s, settle_s):
        def on_progress(frac, elapsed, total, n_valid):
            self.after(0, lambda: self.progress_acq.set(frac))
            rem = max(0.0, total - elapsed)
            info = f"Mengakuisisi... [{elapsed:.1f}s / {total:.1f}s] ({n_valid} sampel)"
            self.after(0, lambda: self.lbl_progress_info.configure(text=info))

        point_data = self.acq_engine.acquire_point(
            v_helm, i_helm, b_tesla,
            duration_seconds=duration_s,
            settle_seconds=settle_s,
            progress_callback=on_progress,
            log_callback=self.log_message,
        )

        if point_data:
            self.calibration_points.append(point_data)

        self.after(0, self._on_acquisition_finished)

    def _on_acquisition_finished(self):
        self.btn_acquire.configure(state="normal", text="▶ Ambil Sampel Titik Ini")
        self.progress_acq.set(1.0)
        self.lbl_progress_info.configure(text="Akuisisi titik selesai.")
        self._recalculate_and_refresh()
        self._refresh_table_view()

    def _delete_last_point(self):
        if self.calibration_points:
            p = self.calibration_points.pop()
            self.log_message(f"Titik terakhir (B={p['b_teslameter']} mT) dihapus.")
            self._recalculate_and_refresh()
            self._refresh_table_view()

    def _reset_all_data(self):
        if messagebox.askyesno("Reset", "Hapus seluruh titik kalibrasi?"):
            self.calibration_points.clear()
            self._recalculate_and_refresh()
            self._refresh_table_view()

    # ------------------------------------------------------------------
    # 7. DEMO CEPAT (SWEEP 0 - 16 V)
    # ------------------------------------------------------------------
    def _load_demo_sweep(self):
        self.calibration_points.clear()
        raw_b_list = [-4.0, -2.5, -1.0, 0.0, 1.5, 3.0, 5.0, 7.0, 9.0, 10.5, 12.0]

        for b in raw_b_list:
            if b < 0:
                v_h = abs(b) / HELMHOLTZ_K * 10.0 * (5.5 / (4.0 / HELMHOLTZ_K * 10.0))
                i_h = v_h / 10.0
            else:
                v_h = (b / 12.0) * 16.0
                i_h = v_h / 10.0

            v_sensor = AD623_VREF + 1.80 * np.tanh(0.185 * b / 1.80) + np.random.normal(0, 0.003)
            std_v = float(np.random.uniform(0.0018, 0.0032))

            self.calibration_points.append({
                "v_helm": round(v_h, 2),
                "i_helm": round(i_h, 2),
                "b_teslameter": round(b, 2),
                "v_sensor": round(v_sensor, 5),
                "std_v": round(std_v, 5),
                "n_samples": 640,
                "duration_s": 5.0,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

        self.log_message("[DEMO] Berhasil memuat 11 titik kalibrasi Helmholtz (Sweep 0-16V, -4 s.d. +12 mT).")
        self._recalculate_and_refresh()
        self._refresh_table_view()

    # ------------------------------------------------------------------
    # 8. ANALISIS REGRESI & GRAFIK
    # ------------------------------------------------------------------
    def _recalculate_and_refresh(self):
        self.ax_calib.clear()
        self.ax_sens.clear()

        for ax in [self.ax_calib, self.ax_sens]:
            ax.set_facecolor(PALETTE["plot_bg"])
            ax.tick_params(colors=PALETTE["text_sub"], labelsize=8)
            for s in ax.spines.values():
                s.set_color(PALETTE["plot_spine"])
            ax.grid(True, color=PALETTE["plot_grid"], linestyle="--", linewidth=0.7)

        self.ax_calib.set_xlabel("Medan Magnet B (mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_calib.set_ylabel("Tegangan Output V (Volt)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_calib.set_title("Karakterisasi Tegangan TMR vs Medan Magnet B", color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8)

        self.ax_sens.set_xlabel("Medan Magnet B (mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_sens.set_ylabel("Sensitivitas dV/dB (V/mT)", color=PALETTE["text_sub"], fontsize=9)
        self.ax_sens.set_title("Sensitivitas Sensor dV/dB vs B (Cubic Spline Derivative)", color=PALETTE["text_main"], fontsize=11, fontweight="bold", pad=8)

        if len(self.calibration_points) < 2:
            self.canvas_calib.draw_idle()
            self.canvas_sens.draw_idle()
            return

        res = self.analyzer.fit_linear(self.calibration_points)
        if res:
            slope = res["slope"]
            intercept = res["intercept"]
            r2 = res["r2"]
            b_arr = res["b_arr"]
            v_arr = res["v_arr"]
            err_arr = res["err_arr"]

            b_dense = np.linspace(min(b_arr) - 0.5, max(b_arr) + 0.5, 300)
            v_line = slope * b_dense + intercept
            self.ax_calib.plot(
                b_dense, v_line, color="#f43f5e", linestyle="--", lw=1.8,
                label=f"Regresi: V = {slope:.4f}·B + {intercept:.4f}\nR² = {r2:.4f}", zorder=2
            )
            self.ax_calib.errorbar(b_arr, v_arr, yerr=err_arr, fmt="none", ecolor="#94a3b8", capsize=3.5, elinewidth=1.0, zorder=3)
            scatter_bola(self.ax_calib, b_arr, v_arr, warna=(0.06, 0.72, 0.50), label="Data Kalibrasi TMR", zorder=4)
            self.ax_calib.legend(loc="upper left", facecolor=PALETTE["card_dark"], edgecolor=PALETTE["plot_spine"], labelcolor=PALETTE["text_main"], fontsize=8)

            # Analisis Spline
            sens_res = self.analyzer.compute_spline_sensitivity(b_arr, v_arr)
            if sens_res:
                self.ax_sens.plot(sens_res["b_dense"], sens_res["sens_dense"], color=PALETTE["teal"], lw=2.0, label="Sensitivitas dV/dB", zorder=2)
                b_pk = sens_res["b_peak"]
                s_pk = sens_res["sens_peak"]
                self.ax_sens.axvline(x=b_pk, color=PALETTE["amber"], linestyle=":", lw=1.5, label=f"B_ideal = {b_pk:.2f} mT\nMax Sens = {s_pk:.3f} V/mT")
                scatter_bola(self.ax_sens, [b_pk], [s_pk], warna=(0.96, 0.62, 0.04), zorder=5)
                self.ax_sens.legend(loc="upper right", facecolor=PALETTE["card_dark"], edgecolor=PALETTE["plot_spine"], labelcolor=PALETTE["text_main"], fontsize=8)

            # Auto-save ke disk
            self.analyzer.save_constants(len(self.calibration_points))
            m_inv = 1.0 / slope if slope != 0 else 0
            c_inv = -intercept / slope if slope != 0 else 0
            self.badge_calib.configure(text=f"B = {m_inv:.2f}·V {c_inv:+.2f}")
            self.log_message(f"[AUTO-SAVE] Konstanta baru disimpan: B = {m_inv:.4f}·V {c_inv:+.4f} mT.")

        self.canvas_calib.draw_idle()
        self.canvas_sens.draw_idle()

    def _load_saved_calibration_constants(self):
        ok, data = self.analyzer.load_constants()
        if ok:
            slope = self.analyzer.slope
            intercept = self.analyzer.intercept
            r2 = self.analyzer.r2
            m_inv = 1.0 / slope if slope != 0 else 0
            c_inv = -intercept / slope if slope != 0 else 0
            self.badge_calib.configure(text=f"B = {m_inv:.2f}·V {c_inv:+.2f}")
            self.log_message("[MEMORI] Konstanta kalibrasi TMR otomatis dimuat dari disk:")
            self.log_message(f"  V = {slope:.4f}·B + {intercept:.4f}  (R² = {r2:.4f})")
            self.log_message(f"  B = {m_inv:.4f}·V {c_inv:+.4f} [mT] -> Siap streaming tanpa perlu kalibrasi ulang!")

    def _refresh_table_view(self):
        self.txt_table.delete("1.0", "end")
        header = f"{'No':<4} | {'V_helm(V)':<10} | {'I_helm(A)':<10} | {'B(mT)':<10} | {'V_sensor(V)':<12} | {'Std(mV)':<9} | {'Dur(s)':<7} | {'Waktu'}\n"
        div = "-" * 92 + "\n"
        self.txt_table.insert("end", header)
        self.txt_table.insert("end", div)

        if not self.calibration_points:
            self.txt_table.insert("end", "  Belum ada data titik kalibrasi. Ambil data atau klik '⚡ Muat Data Demo'.\n")
            return

        sorted_pts = sorted(self.calibration_points, key=lambda x: x["b_teslameter"])
        for i, p in enumerate(sorted_pts, 1):
            dur = p.get("duration_s", 0.0)
            row = (
                f"{i:<4} | {p['v_helm']:<10.2f} | {p['i_helm']:<10.2f} | {p['b_teslameter']:<10.3f} | "
                f"{p['v_sensor']:<12.5f} | {p['std_v']*1000:<9.2f} | {dur:<7.1f} | {p['timestamp']}\n"
            )
            self.txt_table.insert("end", row)

    # ------------------------------------------------------------------
    # 9. EKSPOR DATA & LAPORAN
    # ------------------------------------------------------------------
    def _export_calibration_excel(self):
        filename = filedialog.asksaveasfilename(
            initialfile="tmr_calibration_report.xlsx", defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")]
        )
        if filename:
            ok, msg = export_calibration_report(filename, self.calibration_points, self.analyzer)
            if ok:
                self.log_message(msg)
                messagebox.showinfo("Sukses", msg)
            else:
                messagebox.showerror("Gagal Ekspor", msg)

    def _export_stream_excel(self):
        filename = filedialog.asksaveasfilename(
            initialfile="data_stream_realtime.xlsx", defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")]
        )
        if filename:
            ok, msg = export_stream_data(filename, self.stream_buf.times, self.stream_buf.voltages, self.stream_buf.b_fields)
            if ok:
                self.log_message(msg)
                messagebox.showinfo("Sukses", msg)
            else:
                messagebox.showerror("Gagal Ekspor", msg)

    def _export_python_module(self):
        ok = self.analyzer.save_constants(len(self.calibration_points))
        if ok:
            messagebox.showinfo("Sukses", "Modul konversi_B.py berhasil diperbarui dan disimpan.")
        else:
            messagebox.showwarning("Peringatan", "Lakukan regresi kalibrasi terlebih dahulu.")

    def _export_png_plots(self):
        folder = filedialog.askdirectory(title="Pilih Folder Penyimpanan Gambar")
        if folder:
            ok, msg = export_high_res_plots(folder, self.fig_calib, self.fig_sens)
            if ok:
                self.log_message(msg)
                messagebox.showinfo("Sukses", msg)
            else:
                messagebox.showerror("Gagal Menyimpan", msg)
