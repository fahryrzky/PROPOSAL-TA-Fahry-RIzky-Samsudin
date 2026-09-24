---
name: latex-compile-clean
description: Use when compiling LaTeX documents, building proposal or thesis PDFs, cleaning auxiliary build files, or organizing compilation logs and output PDFs
---

# LaTeX Compile & Clean

## Overview
Automates clean multi-pass LaTeX compilation (`pdflatex` + `bibtex`), isolates all auxiliary build files and logs (`.aux`, `.log`, `.toc`, `.bbl`, etc.) into a dedicated `build_logs/` folder to prevent root clutter, and produces both the main PDF and a named distribution copy `Proposal Fahry Rizky Samsudin.pdf`.

## When to Use
- Compiling LaTeX documents (`skripsi.tex` or any TeX project)
- User asks to "compile", "build pdf", "rapihkan file compile", or "buat salinan proposal"
- Cleaning up temporary build artifacts (`.aux`, `.log`, `.bbl`, `.blg`, `.toc`, `.lof`, `.lot`, `.out`, etc.)
- Generating a clean, finalized PDF ready for distribution or seminar submission

## Quick Reference Commands

| Action | Command |
|---|---|
| **Full Build (Compile + Clean + Copy)** | `python scripts/build_proposal.py` atau `.\build.bat` |
| **Clean Only (Pindahkan Sampah Temp)** | `python scripts/build_proposal.py --clean-only` |
| **Direct Shell Shortcut** | `.\build.bat` |

## Standard Workflow

Whenever compiling or responding to compile requests:
1. **Execute Compilation Script**:
   Jalankan `python scripts/build_proposal.py` (atau `.\build.bat`).
   Skrip mengeksekusi 4 tahap:
   - Pass 1: `pdflatex -interaction=nonstopmode -aux-directory=build_logs skripsi.tex`
   - Pass 2: `bibtex build_logs/skripsi`
   - Pass 3: `pdflatex -interaction=nonstopmode -aux-directory=build_logs skripsi.tex`
   - Pass 4: `pdflatex -interaction=nonstopmode -aux-directory=build_logs skripsi.tex`
2. **Isolate Auxiliary Files**:
   Seluruh berkas perantara (`*.aux`, `*.log`, `*.bbl`, `*.blg`, `*.toc`, `*.lof`, `*.lot`, `*.out`) dipindahkan secara otomatis ke folder `build_logs/`.
   Folder utama (*root directory*) tetap bersih dan rapi hanya berisi berkas sumber, gambar, dan PDF akhir.
3. **Produce Final PDFs**:
   - `skripsi.pdf` (berkas kerja master)
   - `Proposal Fahry Rizky Samsudin.pdf` (salinan bersih untuk pengajuan seminar/dosen)
4. **Error Verification**:
   Memeriksa berkas `build_logs/skripsi.log` untuk memastikan 0 error LaTeX (`!`) dan tidak ada teks yang menembus margin.

## Key Rules
- JANGAN membiarkan berkas sampah temporer `.aux`, `.log`, `.bbl`, dsb. berserakan di *root directory*.
- Pastikan salinan `Proposal Fahry Rizky Samsudin.pdf` selalu sinkron dengan `skripsi.pdf`.
- Jika terjadi kesalahan kompilasi, buka dan analisis berkas catatan di `build_logs/skripsi.log`.
