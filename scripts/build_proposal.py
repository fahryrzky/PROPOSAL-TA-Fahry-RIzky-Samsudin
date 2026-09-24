import os
import shutil
import subprocess
import sys
import glob

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUILD_DIR = os.path.join(PROJECT_ROOT, "build_logs")
MAIN_TEX = "skripsi.tex"
JOB_NAME = "skripsi"
TARGET_COPY_PDF = "Proposal Fahry Rizky Samsudin.pdf"

TEMP_EXTENSIONS = [
    "*.aux", "*.log", "*.bbl", "*.blg", "*.toc",
    "*.lof", "*.lot", "*.out", "*.synctex.gz",
    "*.nav", "*.snm", "*.vrb", "*.fls", "*.fdb_latexmk"
]

def clean_temp_files():
    """Move all temp build files from project root to BUILD_DIR."""
    os.makedirs(BUILD_DIR, exist_ok=True)
    moved_count = 0
    for ext in TEMP_EXTENSIONS:
        for fpath in glob.glob(os.path.join(PROJECT_ROOT, ext)):
            fname = os.path.basename(fpath)
            dest = os.path.join(BUILD_DIR, fname)
            try:
                shutil.move(fpath, dest)
                moved_count += 1
            except Exception as e:
                # If destination already exists, overwrite it
                try:
                    os.remove(dest)
                    shutil.move(fpath, dest)
                    moved_count += 1
                except Exception:
                    pass
    # Also check subdirectories like Isi/ and Header/ for stray .aux files
    for subdir in ["Isi", "Header"]:
        subpath = os.path.join(PROJECT_ROOT, subdir)
        if os.path.isdir(subpath):
            for aux_file in glob.glob(os.path.join(subpath, "*.aux")):
                fname = f"{subdir}_{os.path.basename(aux_file)}"
                dest = os.path.join(BUILD_DIR, fname)
                try:
                    shutil.move(aux_file, dest)
                    moved_count += 1
                except Exception:
                    pass
    return moved_count

def run_command(cmd_list, description):
    print(f"[*] {description} ...")
    result = subprocess.run(
        cmd_list,
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="latin-1",
        errors="replace"
    )
    if result.returncode != 0:
        print(f"[!] Warning: {description} returned code {result.returncode}")
    return result

def compile_latex():
    os.makedirs(BUILD_DIR, exist_ok=True)
    print("==================================================")
    print("  MEMULAI KOMPILASI PROPOSAL SKRIPSI (4 TAHAP)    ")
    print("==================================================")

    # Stage 1: pdflatex (Pass 1)
    # Use -aux-directory=build_logs so MiKTeX places auxiliary files there
    cmd_pdf1 = ["pdflatex", "-interaction=nonstopmode", f"-aux-directory={BUILD_DIR}", MAIN_TEX]
    res1 = run_command(cmd_pdf1, "Tahap 1/4: pdflatex (Pass 1)")

    # Stage 2: bibtex
    # BibTeX needs to find the .aux file
    aux_in_build = os.path.join(BUILD_DIR, f"{JOB_NAME}.aux")
    if os.path.exists(aux_in_build):
        cmd_bib = ["bibtex", os.path.join(BUILD_DIR, JOB_NAME)]
    else:
        cmd_bib = ["bibtex", JOB_NAME]
    res_bib = run_command(cmd_bib, "Tahap 2/4: bibtex")

    # Stage 3: pdflatex (Pass 2)
    cmd_pdf2 = ["pdflatex", "-interaction=nonstopmode", f"-aux-directory={BUILD_DIR}", MAIN_TEX]
    res2 = run_command(cmd_pdf2, "Tahap 3/4: pdflatex (Pass 2 - Sinkronisasi Referensi)")

    # Stage 4: pdflatex (Pass 3)
    cmd_pdf3 = ["pdflatex", "-interaction=nonstopmode", f"-aux-directory={BUILD_DIR}", MAIN_TEX]
    res3 = run_command(cmd_pdf3, "Tahap 4/4: pdflatex (Pass 3 - Finalisasi Nomor & Halaman)")

    # Sweep any auxiliary files that might have been created in the root
    moved = clean_temp_files()
    if moved > 0:
        print(f"[*] Membersihkan {moved} berkas temporer/log ke folder '{os.path.basename(BUILD_DIR)}/'")

    # Verify primary PDF
    src_pdf = os.path.join(PROJECT_ROOT, f"{JOB_NAME}.pdf")
    dest_pdf = os.path.join(PROJECT_ROOT, TARGET_COPY_PDF)

    if os.path.exists(src_pdf):
        # Create user requested copy
        shutil.copy2(src_pdf, dest_pdf)
        pdf_size_mb = os.path.getsize(dest_pdf) / (1024 * 1024)
        print("--------------------------------------------------")
        print("  KOMPILASI SELESAI DENGAN SUKSES!               ")
        print("--------------------------------------------------")
        print(f" [OK] Berkas Utama   : {src_pdf} ({pdf_size_mb:.2f} MB)")
        print(f" [OK] Salinan Proposal: {dest_pdf}")
        print(f" [OK] Folder Log/Temp : {BUILD_DIR}")
    else:
        print("[!] Gagal menemukan output skripsi.pdf! Periksa log pada folder build_logs/")
        return 1

    # Check for LaTeX errors in log file
    log_file = os.path.join(BUILD_DIR, f"{JOB_NAME}.log")
    if not os.path.exists(log_file):
        log_file = os.path.join(PROJECT_ROOT, f"{JOB_NAME}.log")
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="latin-1", errors="replace") as f:
            log_content = f.read()
        err_lines = [l for l in log_content.splitlines() if l.startswith("!")]
        if err_lines:
            print(f"[!] Ditemukan {len(err_lines)} error pada log:")
            for l in err_lines[:5]:
                print("   ", l)
        else:
            print(" [OK] Status Log       : 0 LaTeX Error (Sempurna)")

    return 0

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--clean-only":
        count = clean_temp_files()
        print(f"Berhasil merapikan {count} file temp ke {BUILD_DIR}")
        sys.exit(0)
    sys.exit(compile_latex())
