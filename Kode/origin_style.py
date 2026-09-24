"""
================================================================================
Kode/origin_style.py
================================================================================
Modul pembantu gaya visualisasi bola 3D/bevel ala OriginLab.
Mengimpor implementasi utama dari paket modular `src/style.py`.
================================================================================
"""

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.style import scatter_bola, buat_marker_bola

__all__ = ["scatter_bola", "buat_marker_bola"]
