"""
Skrip Renderer Persamaan Matematika Ilmiah untuk Presentasi Sidang Proposal
Menggunakan engine Matplotlib Computer Modern (LaTeX Standard) 300 DPI
"""

import os
import matplotlib
import matplotlib.pyplot as plt

OUTPUT_DIR = "output/equations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Konfigurasi Computer Modern Font (LaTeX Standard)
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

EQUATIONS = [
    (
        "eq_01_hidrazon.png",
        r"$\mathrm{R\text{--}NH\text{--}NH_2} \;+\; \mathrm{HCHO} \;\longrightarrow\; \mathrm{R\text{--}NH\text{--}N{=}CH_2} \;+\; \mathrm{H_2O}$",
        (7.5, 0.9), 19
    ),
    (
        "eq_02_julliere.png",
        r"$\mathrm{TMR} \;=\; \frac{R_{\mathrm{AP}} - R_{\mathrm{P}}}{R_{\mathrm{P}}} \;=\; \frac{2 P_1 P_2}{1 - P_1 P_2}$",
        (6.0, 1.2), 21
    ),
    (
        "eq_03_helmholtz.png",
        r"$B(0) \;=\; \left(\frac{4}{5}\right)^{3/2} \frac{\mu_0 N I}{R} \;\approx\; 0{,}7155 \, \frac{\mu_0 N I}{R}$",
        (6.5, 1.2), 21
    ),
    (
        "eq_04_ad623.png",
        r"$V_{\mathrm{out}} \;=\; G \,(V_{\mathrm{IN}+} - V_{\mathrm{IN}-}) \;+\; V_{\mathrm{REF}}, \qquad G \;=\; 1 + \frac{100\,\mathrm{k}\Omega}{R_G}$",
        (7.5, 1.1), 19
    ),
    (
        "eq_05_lpf_adc.png",
        r"$f_c \;=\; \frac{1}{2\pi R C}, \qquad \mathrm{LSB} \;=\; \frac{V_{\mathrm{FSR}}}{2^{n}} \;=\; \frac{6{,}144\,\mathrm{V}}{32768} \;=\; 0{,}1875\,\mathrm{mV}$",
        (7.8, 1.1), 18
    ),
    (
        "eq_06_svm.png",
        r"$\min_{\mathbf{w}, b, \boldsymbol{\xi}} \left( \frac{1}{2} \|\mathbf{w}\|^2 + C \sum_{i=1}^N \xi_i \right), \quad K(\mathbf{x}, \mathbf{x}') = \exp\left(-\gamma \|\mathbf{x} - \mathbf{x}'\|^2\right)$",
        (8.2, 1.2), 18
    ),
    (
        "eq_07_qsvc.png",
        r"$|\Phi(\mathbf{x})\rangle \;=\; U_{\Phi}(\mathbf{x}) |0\rangle^{\otimes n}, \qquad K_Q(\mathbf{x}_i, \mathbf{x}_j) \;=\; |\langle \Phi(\mathbf{x}_j) \,|\, \Phi(\mathbf{x}_i) \rangle|^2$",
        (7.8, 1.2), 19
    ),
    (
        "eq_08_fitur.png",
        r"$\Delta V_{\max} = |V_{\mathrm{peak}} - V_{\mathrm{base}}|, \qquad \mathrm{AUC} = \int_{0}^{T} [V(t) - V_0]\, dt$",
        (6.8, 1.1), 19
    ),
    (
        "eq_09_vout_tmr.png",
        r"$V_{\mathrm{out}} \;\approx\; \mathrm{Sen} \;\times\; V_S \;\times\; B$",
        (5.2, 0.9), 20
    )
]

def render_all():
    print("Memulai proses rendering persamaan matematika LaTeX 300 DPI...")
    for filename, latex_str, figsize, fontsize in EQUATIONS:
        filepath = os.path.join(OUTPUT_DIR, filename)
        fig, ax = plt.subplots(figsize=figsize)
        ax.axis('off')
        ax.text(0.5, 0.5, latex_str,
                fontsize=fontsize,
                ha='center', va='center',
                color='#0F1E4A')
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight', transparent=True)
        plt.close(fig)
        print(f" [OK] {filepath}")
    print("Semua persamaan berhasil dirender ke direktori output/equations/!")

if __name__ == "__main__":
    render_all()
