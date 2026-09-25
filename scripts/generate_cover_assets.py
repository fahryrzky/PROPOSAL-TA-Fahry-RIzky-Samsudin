import os
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

def generate_cover_background():
    output_path = "Gambar/cover_bg_gilang.png"
    target_w, target_h = 2880, 1620
    
    # Base canvas dark navy (#08101E)
    base = Image.new("RGBA", (target_w, target_h), (8, 16, 30, 255))
    
    # Try to load real lab photos from Lampiran
    photo_candidates = [
        "Gambar/Lampiran/lampiran_Statif.jpg",
        "Gambar/Lampiran/Statif.jpg",
        "Gambar/Lampiran/lampiran_Tampak_Depan.jpg",
        "Gambar/Lampiran/Tampak Depan.jpg"
    ]
    
    photo_path = None
    for p in photo_candidates:
        if os.path.exists(p):
            photo_path = p
            break
            
    if photo_path:
        img = Image.open(photo_path).convert("RGBA")
        # Resize preserving aspect ratio or fill canvas
        img_w, img_h = img.size
        scale = max(target_w / img_w, target_h / img_h)
        new_w = int(img_w * scale)
        new_h = int(img_h * scale)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Crop center
        left = (new_w - target_w) // 2
        top = (new_h - target_h) // 2
        img = img.crop((left, top, left + target_w, top + target_h))
        
        # Dim photo: reduce contrast and brightness, blur slightly
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(0.35)
        img = img.filter(ImageFilter.GaussianBlur(radius=4))
        
        # Overlay with 82% opacity navy (#08101E)
        navy_overlay = Image.new("RGBA", (target_w, target_h), (8, 16, 30, int(255 * 0.82)))
        composite = Image.alpha_composite(img, navy_overlay)
    else:
        composite = base

    # Create subtle vignette / lighting gradient
    vignette = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(vignette)
    
    # Top and bottom darkening
    draw.rectangle([0, 0, target_w, 200], fill=(4, 8, 16, 120))
    draw.rectangle([0, target_h - 250, target_w, target_h], fill=(4, 8, 16, 160))
    
    final = Image.alpha_composite(composite, vignette).convert("RGB")
    final.save(output_path, "PNG", quality=95)
    print(f"[SUKSES] Latar belakang cover dibuat: {output_path} ({target_w}x{target_h})")

def generate_logo_pill():
    output_path = "Gambar/Logo/logo_uin_fisika_pill.png"
    # If already exists and valid, report it
    if os.path.exists(output_path):
        print(f"[INFO] Logo pill sudah ada: {output_path}")
        return
        
    uin_logo = "Gambar/Logo/Logo UIN.png"
    fisika_logo = "Gambar/Logo/Logo Fisika UIN.png"
    
    pill_w, pill_h = 700, 260
    pill = Image.new("RGBA", (pill_w, pill_h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(pill)
    
    # White rounded rectangle
    draw.rounded_rectangle([10, 10, pill_w - 10, pill_h - 10], radius=40, fill=(255, 255, 255, 255))
    
    # Paste logos if present
    if os.path.exists(uin_logo):
        u_img = Image.open(uin_logo).convert("RGBA")
        u_img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        pill.paste(u_img, (50, (pill_h - u_img.height) // 2), u_img)
        
    if os.path.exists(fisika_logo):
        f_img = Image.open(fisika_logo).convert("RGBA")
        f_img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        pill.paste(f_img, (pill_w - f_img.width - 50, (pill_h - f_img.height) // 2), f_img)
        
    pill.save(output_path, "PNG")
    print(f"[SUKSES] Logo pill dibuat: {output_path}")

if __name__ == "__main__":
    generate_cover_background()
    generate_logo_pill()
