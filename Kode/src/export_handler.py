"""
================================================================================
src/export_handler.py
================================================================================
Ekspor Laporan Kalibrasi Dual-Sheet Excel, Data Stream Real-Time & Gambar Plot
================================================================================
"""

import os
from datetime import datetime
import numpy as np
import pandas as pd
from scipy.interpolate import UnivariateSpline

from .config import OUTPUT_DIR, DEFAULT_EXCEL_REPORT, DEFAULT_STREAM_EXCEL


def export_calibration_report(filename, calibration_points, analyzer):
    """
    Menyimpan laporan kalibrasi dengan 2 sheet persis standar lab Mas Gilang:
    Sheet 1: Calibration Data
    Sheet 2: Regression Info
    """
    if not calibration_points:
        return False, "Tidak ada data kalibrasi untuk diekspor."

    if not filename:
        filename = DEFAULT_EXCEL_REPORT

    try:
        sorted_pts = sorted(calibration_points, key=lambda x: x["b_teslameter"])
        b_arr = np.array([p["b_teslameter"] for p in sorted_pts])
        v_arr = np.array([p["v_sensor"] for p in sorted_pts])

        # Sheet 1: Calibration Data
        v_smooth = v_arr.copy()
        dvdb_list = [0.0] * len(b_arr)
        if len(b_arr) >= 4:
            spline = UnivariateSpline(b_arr, v_arr, s=len(b_arr) * 0.0001)
            v_smooth = spline(b_arr)
            dvdb_list = list(spline.derivative(n=1)(b_arr))

        slope = analyzer.slope if analyzer.slope else 0.14273
        intercept = analyzer.intercept if analyzer.intercept else 2.5075
        b_fit = (v_arr - intercept) / slope

        df_calib = pd.DataFrame({
            "B_mT": b_arr,
            "V_chip-avg_V": v_arr,
            "V_smooth_V": np.round(v_smooth, 6),
            "dVdB_V_per_mT": np.round(dvdb_list, 6),
            "B_fit_from_V": np.round(b_fit, 6),
            "v_helm_V": [p.get("v_helm", 0.0) for p in sorted_pts],
            "I_helm_A": [p.get("i_helm", 0.0) for p in sorted_pts],
            "std_v_mV": [round(p.get("std_v", 0.0) * 1000, 3) for p in sorted_pts],
            "n_samples": [p.get("n_samples", 0) for p in sorted_pts],
            "duration_s": [p.get("duration_s", 0.0) for p in sorted_pts],
        })

        # Sheet 2: Regression Info
        m_inv = 1.0 / slope if slope != 0 else 0
        c_inv = -intercept / slope if slope != 0 else 0

        df_reg = pd.DataFrame([{
            "Regression_V_from_B": f"V = {slope:.6f}*B + {intercept:.6f}",
            "Regression_B_from_V": f"B = {m_inv:.6f}*V + {c_inv:.6f}",
            "Slope_V_per_mT": slope,
            "Intercept_V": intercept,
            "R_Squared": analyzer.r2 if analyzer.r2 else 0.0,
            "B_ideal_mT": analyzer.b_ideal if analyzer.b_ideal else 0.0,
            "Calibration_Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }])

        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            df_calib.to_excel(writer, sheet_name="Calibration Data", index=False)
            df_reg.to_excel(writer, sheet_name="Regression Info", index=False)

        return True, f"Laporan kalibrasi 2-sheet berhasil disimpan:\n{filename}"
    except Exception as e:
        return False, str(e)


def export_stream_data(filename, stream_times, stream_voltages, stream_b):
    """Menyimpan data aliran streaming real-time (t, V, B) ke file Excel."""
    if not stream_times:
        return False, "Belum ada data streaming real-time yang terhimpun."

    if not filename:
        filename = DEFAULT_STREAM_EXCEL

    try:
        df_stream = pd.DataFrame({
            "t (s)": [round(t, 3) for t in stream_times],
            "V (V)": [round(v, 5) for v in stream_voltages],
            "B (mT)": [round(b, 5) for b in stream_b],
        })
        df_stream.to_excel(filename, index=False)
        return True, f"Data stream real-time berhasil disimpan ke:\n{filename}"
    except Exception as e:
        return False, str(e)


def export_high_res_plots(folder, fig_calib, fig_sens):
    """Menyimpan grafik kalibrasi dalam format resolusi tinggi (300 DPI)."""
    if not folder:
        folder = OUTPUT_DIR

    try:
        os.makedirs(folder, exist_ok=True)
        p1 = os.path.join(folder, "kurva_V_vs_B.png")
        p2 = os.path.join(folder, "kurva_sensitivitas_B.png")
        fig_calib.savefig(p1, dpi=300, bbox_inches="tight")
        fig_sens.savefig(p2, dpi=300, bbox_inches="tight")
        return True, f"Kedua grafik berhasil disimpan ke folder:\n{folder}"
    except Exception as e:
        return False, str(e)
