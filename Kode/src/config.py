"""
================================================================================
src/config.py
================================================================================
Konfigurasi Tema, Parameter Listrik & Jalur File Sistem Instrumentasi TMR
================================================================================
"""

import os

# Direktori Basis
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
FIRMWARE_DIR = os.path.join(BASE_DIR, "firmware")

# Pastikan folder ada
for d in [DATA_DIR, OUTPUT_DIR, FIRMWARE_DIR]:
    os.makedirs(d, exist_ok=True)

# Jalur File Data & Output
CALIBRATION_JSON_PATH = os.path.join(DATA_DIR, "konstanta_kalibrasi_B.json")
CALIBRATION_JSON_ROOT = os.path.join(BASE_DIR, "konstanta_kalibrasi_B.json")
CONVERSION_MODULE_PATH = os.path.join(DATA_DIR, "konversi_B.py")
CONVERSION_MODULE_ROOT = os.path.join(BASE_DIR, "konversi_B.py")
DEFAULT_EXCEL_REPORT = os.path.join(DATA_DIR, "tmr_calibration_report.xlsx")
DEFAULT_STREAM_EXCEL = os.path.join(DATA_DIR, "data_stream_realtime.xlsx")
RAW_DATA_CSV = os.path.join(DATA_DIR, "data_mentah_karakterisasi_B.csv")

# Palet Warna Akademik (Dark Navy Slate & Emerald Accent)
PALETTE = {
    "bg_dark": "#0b1329",         # Deep navy slate
    "card_dark": "#162038",       # Slate card background
    "card_border": "#283556",     # Muted slate border
    "text_main": "#f8fafc",       # Crisp white
    "text_sub": "#94a3b8",        # Slate gray
    "emerald": "#10b981",         # Academic emerald green
    "emerald_dark": "#047857",
    "teal": "#06b6d4",            # Cyan / teal
    "amber": "#f59e0b",           # Amber
    "rose": "#f43f5e",            # Rose red
    "blue": "#3b82f6",            # Royal blue
    "plot_bg": "#121a2f",         # Matplotlib inner face
    "plot_spine": "#334155",      # Matplotlib spines
    "plot_grid": "#1e293b",       # Matplotlib grid
}

# Parameter Listrik & Pengkondisi Sinyal
ADS1115_VDD = 5.0                 # Catu daya ADC ADS1115 (Volt)
ADS1115_PGA_FSR = 6.144           # Rentang Skala Penuh GAIN_TWOTHIRDS (+-6.144 V)
ADS1115_LSB = 6.144 / 32768.0     # 0.0001875 V = 0.1875 mV per count
AD623_VREF = 2.50                 # Tegangan bias referensi Pin 5 AD623 (5V / 2)

# Parameter Helmholtz & Power Supply (0 - 16 V)
HELMHOLTZ_MAX_V = 16.0            # Rentang batas atas power supply DC
HELMHOLTZ_COIL_R = 10.0           # Resistansi kumparan (Ohm)
HELMHOLTZ_K = 0.72                # Konstanta medan B per satuan arus (mT/A)

# Parameter Default Akuisisi Berbasis Durasi Detik
DEFAULT_DURATION_S = 5.0          # Lama waktu akuisisi per titik (detik)
DEFAULT_SETTLE_S = 1.0            # Waktu stabilisasi awal yang dibuang (detik)
DEFAULT_BAUD = 115200             # Baud rate komunikasi serial
