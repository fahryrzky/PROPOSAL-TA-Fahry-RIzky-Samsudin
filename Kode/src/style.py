"""
================================================================================
src/style.py
================================================================================
Utilitas Rendering Marker 3D Sphere / Bevel Bergaya OriginLab untuk Publikasi
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def _buat_gambar_bola(warna_rgb, resolusi=64):
    """
    Membuat sprite bola 3D (shading specular + diffuse) bergaya OriginLab.
    """
    y, x = np.mgrid[-1:1:resolusi * 1j, -1:1:resolusi * 1j]
    r = np.sqrt(x**2 + y**2)

    # Vektor normal permukaan setengah bola
    z = np.zeros_like(r)
    mask = r <= 1.0
    z[mask] = np.sqrt(1.0 - r[mask]**2)

    # Sumber cahaya dari kiri-atas-depan (OriginLab default light)
    light = np.array([-0.5, -0.5, 0.7])
    light /= np.linalg.norm(light)

    # Komponen Diffuse Lambertian
    diffuse = np.zeros_like(r)
    diffuse[mask] = np.clip(
        x[mask] * light[0] + y[mask] * light[1] + z[mask] * light[2], 0, 1
    )

    # Komponen Specular Blinn-Phong
    view = np.array([0.0, 0.0, 1.0])
    half = light + view
    half /= np.linalg.norm(half)
    specular = np.zeros_like(r)
    specular[mask] = np.clip(
        x[mask] * half[0] + y[mask] * half[1] + z[mask] * half[2], 0, 1
    ) ** 20

    ambient = 0.28
    shade = ambient + (1.0 - ambient) * diffuse

    # Matriks RGBA
    img = np.zeros((resolusi, resolusi, 4), dtype=float)
    for c in range(3):
        img[..., c] = np.clip(warna_rgb[c] * shade + 0.85 * specular, 0, 1)

    # Antialiasing di pinggiran bola
    edge = np.clip((1.0 - r) * resolusi * 0.5, 0, 1)
    img[..., 3] = np.where(mask, edge, 0.0)

    return img


def scatter_bola(ax, x, y, warna=(0.16, 0.45, 0.78), ukuran_px=48, zoom=0.18, label=None, zorder=4):
    """
    Menggambar scatter plot dengan marker bola 3D proporsional.
    """
    img_bola = _buat_gambar_bola(warna, resolusi=ukuran_px)

    x = np.atleast_1d(x)
    y = np.atleast_1d(y)

    for xi, yi in zip(x, y):
        im = OffsetImage(img_bola, zoom=zoom)
        ab = AnnotationBbox(
            im, (xi, yi),
            frameon=False,
            pad=0.0,
            box_alignment=(0.5, 0.5),
            zorder=zorder,
        )
        ax.add_artist(ab)

    # Dummy scatter transparan untuk pemicu entri legenda Matplotlib
    ax.scatter(
        x, y,
        s=(ukuran_px * zoom * 3.5)**2,
        color=warna,
        alpha=0.0,
        label=label,
        zorder=zorder - 1,
    )
