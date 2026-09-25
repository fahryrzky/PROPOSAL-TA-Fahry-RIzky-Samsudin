import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set figure size and dpi
fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

# Helper function to draw rounded boxes
def draw_box(ax, x, y, w, h, text, title=None, fill="#f8fafc", edge="#334155", title_color="#0f172a", text_color="#334155", fontsize=9, title_fontsize=10, boxstyle="round,pad=0.5,rounding_size=0.8"):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle=boxstyle, facecolor=fill, edgecolor=edge, linewidth=1.5, zorder=2)
    ax.add_patch(box)
    if title:
        ax.text(x + w/2, y + h - 2.5, title, ha="center", va="center", fontsize=title_fontsize, fontweight="bold", color=title_color, zorder=3)
        ax.text(x + w/2, y + (h - 2.5)/2, text, ha="center", va="center", fontsize=fontsize, color=text_color, zorder=3, multialignment="center")
    else:
        ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fontsize, color=text_color, zorder=3, multialignment="center")

def draw_arrow(ax, x1, y1, x2, y2, color="#475569", lw=1.5):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=lw, shrinkA=2, shrinkB=2, mutation_scale=15), zorder=4)

# 1. Title / Header
ax.text(50, 97.5, "Diagram Alir Pelatihan dan Komparasi Model Klasifikasi", ha="center", va="center", fontsize=13, fontweight="bold", color="#1e293b")
ax.text(50, 95.0, "Komparasi 2 Model Klasik (SVM, Random Forest) vs 2 Model Kuantum (QSVC, VQC)", ha="center", va="center", fontsize=10, fontstyle="italic", color="#475569")

# 2. Stage 1: Dataset & Feature Extraction
draw_box(ax, 20, 85, 60, 7, 
         "Akuisisi Sinyal TMR (Tegangan vs Waktu) $\\rightarrow$ Ekstraksi 3 Fitur ($V_{\\mathrm{mean}}, \\Delta V, \\sigma_V$)\n"
         "Dataset: 60 Sampel Standar (0-100 ppm) + 30 Ekstrak Bakso Riil (90 Sampel Total)", 
         title="1. DATASET & EKSTRAKSI FITUR SINYAL", fill="#e0f2fe", edge="#0284c7", title_color="#0369a1")

draw_arrow(ax, 50, 85, 50, 78)

# 3. Stage 2: Preprocessing & Split
draw_box(ax, 25, 71, 50, 7, 
         "Standarisasi Fitur: z = (x - $\\mu$) / $\\sigma$ (StandardScaler fit hanya pada Train Set)\n"
         "Pembagian Data: 80% Pelatihan (72 Sampel) & 20% Pengujian Independen (18 Sampel)",
         title="2. PREPROCESSING & PENCEGAHAN DATA LEAKAGE", fill="#f1f5f9", edge="#64748b", title_color="#334155")

# Split arrows to Classical & Quantum
draw_arrow(ax, 40, 71, 26, 63)
draw_arrow(ax, 60, 71, 74, 63)

# Container for Classical (Left)
class_box = patches.FancyBboxPatch((4, 25), 44, 38, boxstyle="round,pad=0.8,rounding_size=1.2", facecolor="#f8fafc", edgecolor="#3b82f6", linewidth=1.5, linestyle="--", zorder=1)
ax.add_patch(class_box)
ax.text(26, 61, "PARADIGMA 1: MODEL KLASIK", ha="center", va="center", fontsize=10, fontweight="bold", color="#1d4ed8")

# Classical Model 1: SVM
draw_box(ax, 6, 44, 40, 14,
         "• Kernel Radial Basis Function (RBF Gaussian)\n"
         "• Formulasi Dual: $\\max_\\alpha \\sum \\alpha_i - \\frac{1}{2}\\sum \\alpha_i \\alpha_j y_i y_j K(x_i, x_j)$\n"
         "• Optimasi Hyperparameter: $C \\in [0.1, 100]$ & $\\gamma \\in [0.001, 1]$\n"
         "• Stratified 5-Fold Cross Validation",
         title="Model 1: Support Vector Machine (SVM)", fill="#eff6ff", edge="#3b82f6", title_color="#1d4ed8", fontsize=8)

# Classical Model 2: Random Forest
draw_box(ax, 6, 27, 40, 14,
         "• Ensemble Bagging Pohon Keputusan (Decision Trees)\n"
         "• Prediksi Agregat Mayoritas: $\\hat{y} = \\mathrm{mode}\\{h_b(x)\\}_{b=1}^B$\n"
         "• Tuning: n_estimators $\\in [50, 200]$, max_depth $\\in [3, 10]$\n"
         "• Evaluasi Feature Importance (Gini Impurity)",
         title="Model 2: Random Forest (RF)", fill="#eff6ff", edge="#3b82f6", title_color="#1d4ed8", fontsize=8)

# Container for Quantum (Right)
quant_box = patches.FancyBboxPatch((52, 25), 44, 38, boxstyle="round,pad=0.8,rounding_size=1.2", facecolor="#f0fdfa", edgecolor="#0d9488", linewidth=1.5, linestyle="--", zorder=1)
ax.add_patch(quant_box)
ax.text(74, 61, "PARADIGMA 2: MODEL KUANTUM (QISKIT)", ha="center", va="center", fontsize=10, fontweight="bold", color="#0f766e")

# Quantum Model 1: QSVC
draw_box(ax, 54, 44, 40, 14,
         "• Quantum Feature Map: ZZFeatureMap (3 Qubit, depth=2)\n"
         "• Pemetaan Ruang Hilbert 8D: $|\\Phi(x)\\rangle = U_{\\Phi(x)}|0\\rangle^{\\otimes 3}$\n"
         "• Quantum Kernel Matrix: $K_{ij}^Q = |\\langle\\Phi(x_i)|\\Phi(x_j)\\rangle|^2$\n"
         "• Optimasi Margin Klasik pada Matriks Kernel Kuantum",
         title="Model 3: Quantum Support Vector (QSVC)", fill="#ccfbf1", edge="#0d9488", title_color="#0f766e", fontsize=8)

# Quantum Model 2: VQC
draw_box(ax, 54, 27, 40, 14,
         "• Parametrized Quantum Circuit (Ansatz RealAmplitudes)\n"
         "• Status Kuantum: $|\\psi(x, \\theta)\\rangle = W(\\theta) U_{\\Phi(x)} |0\\rangle^{\\otimes 3}$\n"
         "• Optimasi Sudut Variasional $\\theta$: Optimizer COBYLA / SPSA\n"
         "• Pengukuran Nilai Ekspektasi Hamiltonian: $\\langle Z_0 \\rangle$",
         title="Model 4: Variational Quantum Classifier (VQC)", fill="#ccfbf1", edge="#0d9488", title_color="#0f766e", fontsize=8)

# Converge to Evaluation Stage
draw_arrow(ax, 26, 25, 42, 17)
draw_arrow(ax, 74, 25, 58, 17)

# Stage 4: Comprehensive Comparative Evaluation
draw_box(ax, 15, 9, 70, 8,
         "Metrik Evaluasi: Akurasi, Presisi, Recall, F1-Score, ROC-AUC, dan Confusion Matrix\n"
         "Analisis Lanjutan: Latensi Waktu Komputasi (ms) & Ketahanan Derau (Noise Robustness)\n"
         "(Injeksi Derau Gaussian Klasik $\\sigma_{\\mathrm{noise}}$ & Derau Kuantum Depolarizing Gate)",
         title="3. EVALUASI KOMPARATIF 4 MODEL (5-FOLD CROSS VALIDATION)", fill="#fef3c7", edge="#d97706", title_color="#b45309", fontsize=8.5)

draw_arrow(ax, 50, 9, 50, 5.5)

# Stage 5: Selection & Deployment
draw_box(ax, 25, 0.5, 50, 5,
         "Seleksi Model dengan Generalisasi Terbaik $\\rightarrow$ Simpan Model (.joblib / Qiskit Circuit)\n"
         "Deployment pada GUI Host Raspberry Pi 5 untuk Deteksi Formalin Realtime",
         title="4. SELEKSI MODEL OPTIMAL & DEPLOYMENT", fill="#dcfce7", edge="#16a34a", title_color="#15803d", fontsize=8)

plt.tight_layout()
plt.savefig("Gambar/Bab3/babIII_ModelBuilding.drawio.png", dpi=300, bbox_inches="tight")
plt.savefig("Gambar/Bab3/babIIIModelBuilding.drawio.png", dpi=300, bbox_inches="tight")
print("SUCCESS: High-res flowcharts saved!")
