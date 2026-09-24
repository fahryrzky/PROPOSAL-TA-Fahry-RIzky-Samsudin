"""
=========================================================================
Kode/scripts/olah_data_kalibrasi_B.py
=========================================================================
Olah data hasil kalibrasi sensor TMR ALT023-10E:
  1. Regresi linear V = m*B + c (R²) + rumus kebalikan B = (V-c)/m
  2. Kurva sensitivitas (spline halus + dV/dB) -> cari B ideal & rentang sensitif
  3. Menyimpan konstanta kalibrasi ke:
     - konstanta_kalibrasi_B.json
     - konversi_B.py (modul otomatis siap import)
=========================================================================
"""

import os
import sys
import json
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Resolusi path direktori
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

for d in [DATA_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from src.style import scatter_bola
except ImportError:
    try:
        from origin_style import scatter_bola
    except ImportError:
        def scatter_bola(ax, x, y, warna=(0.16, 0.45, 0.78), label=None, **kwargs):
            return ax.scatter(x, y, color=warna, label=label)

WARNA_DATA = (0.16, 0.45, 0.78)
WARNA_PUNCAK = (0.85, 0.35, 0.10)

# Cari file input (cek di data/ lalu direktori lokal)
INPUT_CANDIDATES = [
    os.path.join(DATA_DIR, "titik_kalibrasi_B.xlsx"),
    os.path.join(DATA_DIR, "tmr_calibration_report.xlsx"),
    os.path.join(BASE_DIR, "titik_kalibrasi_B.xlsx"),
    "titik_kalibrasi_B.xlsx",
]

INPUT_FILE = None
for cand in INPUT_CANDIDATES:
    if os.path.exists(cand):
        INPUT_FILE = cand
        break

if INPUT_FILE is None:
    INPUT_FILE = os.path.join(DATA_DIR, "titik_kalibrasi_B.xlsx")

SATUAN_B = "mT"
PLOT_FILE = os.path.join(OUTPUT_DIR, "kurva_V_vs_B.png")
SENSITIVITY_PLOT_FILE = os.path.join(OUTPUT_DIR, "kurva_sensitivitas_B.png")
KONSTANTA_JSON_FILE = os.path.join(DATA_DIR, "konstanta_kalibrasi_B.json")
KONVERSI_MODULE_FILE = os.path.join(DATA_DIR, "konversi_B.py")
SPLINE_SMOOTHING = None


def cari_rentang_kontigu(mask, peak_idx):
    kiri = peak_idx
    while kiri > 0 and mask[kiri - 1]:
        kiri -= 1
    kanan = peak_idx
    while kanan < len(mask) - 1 and mask[kanan + 1]:
        kanan += 1
    return kiri, kanan


def main():
    print(f"Membaca data dari: {INPUT_FILE}")
    if not os.path.exists(INPUT_FILE):
        print(f"[ERROR] File '{INPUT_FILE}' tidak ditemukan!")
        print("Pastikan data kalibrasi sudah diekspor dari GUI atau jalankan generate_dummy_tmr_data.py.")
        return

    try:
        df = pd.read_excel(INPUT_FILE, sheet_name=0)
    except Exception as e:
        print(f"[ERROR] Gagal membaca Excel: {e}")
        return

    # Normalisasi nama kolom
    col_map = {}
    for c in df.columns:
        cl = str(c).lower().strip()
        if "b_mt" in cl or cl == "b" or "b_tesla" in cl:
            col_map["B"] = c
        elif "v_mean" in cl or "v_chip" in cl or "v_sensor" in cl:
            col_map["V"] = c
        elif "v_std" in cl or "std" in cl:
            col_map["std"] = c

    if "B" not in col_map or "V" not in col_map:
        print(f"[ERROR] Kolom B dan Tegangan tidak terdeteksi. Kolom tersedia: {list(df.columns)}")
        return

    b_col = col_map["B"]
    v_col = col_map["V"]
    std_col = col_map.get("std", None)

    df_clean = df.dropna(subset=[b_col, v_col]).sort_values(by=b_col)
    B = df_clean[b_col].to_numpy(dtype=float)
    V = df_clean[v_col].to_numpy(dtype=float)
    Verr = df_clean[std_col].to_numpy(dtype=float) if std_col else np.zeros_like(V)

    # 1. Regresi Linear
    slope, intercept = np.polyfit(B, V, 1)
    v_pred = slope * B + intercept
    ss_res = np.sum((V - v_pred) ** 2)
    ss_tot = np.sum((V - np.mean(V)) ** 2)
    r2 = 1.0 - (ss_res / ss_tot) if ss_tot != 0 else 0.0

    print("\n" + "=" * 60)
    print("HASIL REGRESI LINEAR SENSOR TMR ALT023-10E")
    print("=" * 60)
    print(f"Persamaan Kalibrasi : V = {slope:.6f} * B + {intercept:.6f}")
    print(f"Koefisien Det (R²)  : {r2:.4f}")
    print(f"Sensitivitas Linear : {slope*1000:.2f} mV/mT")
    if slope != 0:
        print(f"Persamaan Konversi  : B = (V - {intercept:.6f}) / {slope:.6f}  [{SATUAN_B}]")
        print(f"                    : B = {1.0/slope:.6f} * V + {-intercept/slope:.6f}")
    print("=" * 60)

    # Simpan konstanta ke JSON
    data_konstanta = {
        "slope": float(slope),
        "intercept": float(intercept),
        "r2": float(r2),
        "satuan_B": SATUAN_B,
        "n_titik": len(B),
        "timestamp": datetime.now().isoformat()
    }
    for p_json in [KONSTANTA_JSON_FILE, os.path.join(BASE_DIR, "konstanta_kalibrasi_B.json")]:
        try:
            with open(p_json, "w", encoding="utf-8") as f:
                json.dump(data_konstanta, f, indent=2)
        except Exception:
            pass

    # Buat modul konversi_B.py
    code_modul = f'''"""
=============================================================================
konversi_B.py - Dihasilkan otomatis oleh olah_data_kalibrasi_B.py
Persamaan Kalibrasi: V = {slope:.6f} * B + {intercept:.6f}  (R² = {r2:.4f})
=============================================================================
"""

SLOPE_M = {slope:.6f}
INTERCEPT_C = {intercept:.6f}
R_SQUARED = {r2:.4f}

def tegangan_ke_B(v_volt):
    """Mengubah tegangan output sensor AD623 (Volt) ke medan magnet B ({SATUAN_B})."""
    return (v_volt - INTERCEPT_C) / SLOPE_M

def b_ke_tegangan(b_mt):
    """Mengubah medan magnet B ({SATUAN_B}) ke estimasi tegangan output sensor (Volt)."""
    return SLOPE_M * b_mt + INTERCEPT_C

if __name__ == "__main__":
    v_uji = 2.50
    print(f"Uji Konversi: {{v_uji}} V -> {{tegangan_ke_B(v_uji):.4f}} {SATUAN_B}")
'''
    for p_mod in [KONVERSI_MODULE_FILE, os.path.join(BASE_DIR, "konversi_B.py")]:
        try:
            with open(p_mod, "w", encoding="utf-8") as f:
                f.write(code_modul)
        except Exception:
            pass

    # Plot 1: V vs B
    fig, ax = plt.subplots(figsize=(8, 6))
    if np.any(Verr > 0):
        ax.errorbar(B, V, yerr=Verr, fmt="none", ecolor="gray", capsize=4, zorder=1)
    b_dense = np.linspace(min(B) - 0.5, max(B) + 0.5, 300)
    ax.plot(b_dense, slope * b_dense + intercept, "r--", zorder=2,
            label=f"V = {slope:.4f}·B + {intercept:.4f}\nR² = {r2:.4f}")
    scatter_bola(ax, B, V, warna=WARNA_DATA, label="Data Pengukuran TMR", zorder=3)
    ax.set_xlabel(f"Medan Magnet Riil B ({SATUAN_B})")
    ax.set_ylabel("Tegangan Output AD623 (V)")
    ax.set_title("Karakterisasi Sensor TMR ALT023-10E: V vs B")
    ax.axhline(2.50, color="gray", linewidth=0.5, linestyle=":", label="V_REF = 2.50 V")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=300)
    print(f"[OK] Plot V vs B disimpan ke: {PLOT_FILE}")

    # Plot 2: Analisis Sensitivitas dV/dB
    if len(B) >= 4:
        s = SPLINE_SMOOTHING if SPLINE_SMOOTHING is not None else len(B) * 0.0001
        spline = UnivariateSpline(B, V, k=3, s=s)
        b_dense_sens = np.linspace(B.min() - 0.5, B.max() + 0.5, 400)
        v_smooth = spline(b_dense_sens)
        dvdb = spline.derivative()(b_dense_sens)

        peak_idx = int(np.argmax(np.abs(dvdb)))
        b_ideal = b_dense_sens[peak_idx]
        peak_dvdb = dvdb[peak_idx]
        threshold = 0.5 * abs(peak_dvdb)
        mask = np.abs(dvdb) >= threshold
        kiri, kanan = cari_rentang_kontigu(mask, peak_idx)
        b_low, b_high = b_dense_sens[kiri], b_dense_sens[kanan]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

        ax1.plot(b_dense_sens, v_smooth, label="Smoothed V", zorder=2)
        scatter_bola(ax1, B, V, warna=WARNA_DATA, label="Raw V", zorder=3)
        ax1.axvline(b_ideal, color="tab:orange", linestyle="--", label=f"Peak at {b_ideal:.2f} {SATUAN_B}")
        ax1.axvspan(b_low, b_high, color="orange", alpha=0.15,
                    label=f"Sensitive range {b_low:.2f}-{b_high:.2f} {SATUAN_B}")
        ax1.set_ylabel("V_chip-avg (V)")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        ax2.plot(b_dense_sens, dvdb, label="dV/dB", color="teal", lw=2, zorder=2)
        scatter_bola(ax2, [b_ideal], [peak_dvdb], warna=WARNA_PUNCAK, zoom=0.6,
                     label=f"Peak dV/dB = {peak_dvdb:.4f} V/{SATUAN_B}", zorder=5)
        ax2.axhline(threshold if peak_dvdb >= 0 else -threshold, color="tab:blue", linestyle=":", label="50% peak")
        ax2.set_xlabel(f"Medan Magnet B ({SATUAN_B})")
        ax2.set_ylabel(f"Sensitivitas dV/dB (V/{SATUAN_B})")
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig(SENSITIVITY_PLOT_FILE, dpi=300)
        print(f"[OK] Plot Sensitivitas disimpan ke: {SENSITIVITY_PLOT_FILE}")
        print(f"  -> B_ideal (puncak) : {b_ideal:.4f} {SATUAN_B}")
        print(f"  -> Rentang sensitif : {b_low:.4f} s.d. {b_high:.4f} {SATUAN_B}")


if __name__ == "__main__":
    main()
