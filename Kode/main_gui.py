"""
================================================================================
Kode/main_gui.py
================================================================================
Entry point utama untuk GUI Instrumentasi & Karakterisasi Sensor TMR ALT023-10E
Menerapkan arsitektur modular berorientasi objek dari paket `src/`.
================================================================================
"""

import sys
import os

# Pastikan direktori root 'Kode' terdaftar dalam sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.gui import TMRAcquisitionApp

def main():
    app = TMRAcquisitionApp()
    app.mainloop()

if __name__ == "__main__":
    main()
