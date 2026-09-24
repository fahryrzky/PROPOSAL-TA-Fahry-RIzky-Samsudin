"""
================================================================================
src/analysis.py
================================================================================
Perhitungan Regresi Linear, Analisis Sensitivitas Spline & Persistensi Kalibrasi
================================================================================
"""

import os
import json
from datetime import datetime
import numpy as np
from scipy.interpolate import UnivariateSpline

from .config import (
    CALIBRATION_JSON_PATH,
    CALIBRATION_JSON_ROOT,
    CONVERSION_MODULE_PATH,
    CONVERSION_MODULE_ROOT,
)


class CalibrationAnalyzer:
    """Mesin analisis matematika & regresi kalibrasi sensor TMR."""
    def __init__(self):
        self.slope = None
        self.intercept = None
        self.r2 = None
        self.b_ideal = None

    def fit_linear(self, calibration_points):
        """Melakukan regresi linear V = m * B + c."""
        if len(calibration_points) < 2:
            return None

        sorted_pts = sorted(calibration_points, key=lambda x: x["b_teslameter"])
        b_arr = np.array([p["b_teslameter"] for p in sorted_pts])
        v_arr = np.array([p["v_sensor"] for p in sorted_pts])

        slope, intercept = np.polyfit(b_arr, v_arr, 1)
        v_pred = slope * b_arr + intercept
        ss_res = np.sum((v_arr - v_pred) ** 2)
        ss_tot = np.sum((v_arr - np.mean(v_arr)) ** 2)
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot != 0 else 0.0

        self.slope = float(slope)
        self.intercept = float(intercept)
        self.r2 = float(r2)

        return {
            "slope": self.slope,
            "intercept": self.intercept,
            "r2": self.r2,
            "b_arr": b_arr,
            "v_arr": v_arr,
            "err_arr": np.array([p["std_v"] for p in sorted_pts]),
        }

    def compute_spline_sensitivity(self, b_arr, v_arr, n_points=300):
        """Menghitung turunan pertama cubic spline dV/dB dan mencari titik B_ideal."""
        if len(b_arr) < 4:
            return None

        try:
            b_dense = np.linspace(min(b_arr) - 0.5, max(b_arr) + 0.5, n_points)
            spline = UnivariateSpline(b_arr, v_arr, s=len(b_arr) * 0.0001)
            spline_deriv = spline.derivative(n=1)
            sens_dense = spline_deriv(b_dense)

            idx_peak = np.argmax(sens_dense)
            b_peak = float(b_dense[idx_peak])
            sens_peak = float(sens_dense[idx_peak])
            self.b_ideal = b_peak

            return {
                "b_dense": b_dense,
                "sens_dense": sens_dense,
                "b_peak": b_peak,
                "sens_peak": sens_peak,
            }
        except Exception:
            return None

    def save_constants(self, n_points=0):
        """Menyimpan konstanta kalibrasi ke file JSON dan file modul Python."""
        if self.slope is None:
            return False

        data = {
            "slope": self.slope,
            "intercept": self.intercept,
            "r2": self.r2,
            "b_ideal": self.b_ideal,
            "satuan_B": "mT",
            "n_titik_kalibrasi": n_points,
            "dibuat": datetime.now().isoformat(),
            "keterangan": "V = slope*B + intercept  |  B = (V - intercept) / slope"
        }

        # Simpan ke data/ dan root
        for path in [CALIBRATION_JSON_PATH, CALIBRATION_JSON_ROOT]:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
            except Exception:
                pass

        # Buat modul Python konversi_B.py
        code = f'''"""
=============================================================================
konversi_B.py
=============================================================================
Modul otomatis konversi Tegangan (V) <-> Medan Magnet (mT)
Sensor TMR ALT023-10E + Pengkondisi Sinyal AD623
Dibuat otomatis oleh Sistem Kalibrasi TMR pada {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Persamaan Kalibrasi: V = {self.slope:.6f} * B + {self.intercept:.6f}
Koefisien Determinasi R² = {self.r2:.4f}
=============================================================================
"""

SLOPE_M = {self.slope:.6f}
INTERCEPT_C = {self.intercept:.6f}
R_SQUARED = {self.r2:.4f}
B_IDEAL = {self.b_ideal if self.b_ideal is not None else 0.0:.4f}

def tegangan_ke_B(v_volt):
    """Mengubah tegangan output sensor AD623 (Volt) ke medan magnet B (mT)."""
    return (v_volt - INTERCEPT_C) / SLOPE_M

def b_ke_tegangan(b_mt):
    """Mengubah medan magnet B (mT) ke estimasi tegangan output sensor (Volt)."""
    return SLOPE_M * b_mt + INTERCEPT_C

if __name__ == "__main__":
    v_test = 2.50
    print(f"Uji Konversi: {{v_test}} V -> {{tegangan_ke_B(v_test):.4f}} mT")
'''
        for p in [CONVERSION_MODULE_PATH, CONVERSION_MODULE_ROOT]:
            try:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(code)
            except Exception:
                pass

        return True

    def load_constants(self):
        """Membaca konstanta kalibrasi tersimpan dari disk."""
        target_path = CALIBRATION_JSON_PATH if os.path.exists(CALIBRATION_JSON_PATH) else CALIBRATION_JSON_ROOT
        if os.path.exists(target_path):
            try:
                with open(target_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.slope = float(data.get("slope", 0.14273))
                self.intercept = float(data.get("intercept", 2.5075))
                self.r2 = float(data.get("r2", 0.9774))
                self.b_ideal = float(data.get("b_ideal", -1.47)) if "b_ideal" in data else -1.47
                return True, data
            except Exception as e:
                return False, str(e)
        return False, "File konstanta kalibrasi belum tersedia."
