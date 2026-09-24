"""
=============================================================================
konversi_B.py - Dihasilkan otomatis oleh olah_data_kalibrasi_B.py
Persamaan Kalibrasi: V = 0.143267 * B + 2.490022  (R² = 0.9809)
=============================================================================
"""

SLOPE_M = 0.143267
INTERCEPT_C = 2.490022
R_SQUARED = 0.9809

def tegangan_ke_B(v_volt):
    """Mengubah tegangan output sensor AD623 (Volt) ke medan magnet B (mT)."""
    return (v_volt - INTERCEPT_C) / SLOPE_M

def b_ke_tegangan(b_mt):
    """Mengubah medan magnet B (mT) ke estimasi tegangan output sensor (Volt)."""
    return SLOPE_M * b_mt + INTERCEPT_C

if __name__ == "__main__":
    v_uji = 2.50
    print(f"Uji Konversi: {v_uji} V -> {tegangan_ke_B(v_uji):.4f} mT")
