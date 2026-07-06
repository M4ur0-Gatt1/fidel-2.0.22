"""Genera fidel.ico con el logo del diseño: cuadrado verde redondeado + estrella roja.
Uso: python make_icon.py
"""
import math

from PIL import Image, ImageDraw

GREEN = (78, 140, 95, 255)    # --green del handoff
RED = (229, 50, 45, 255)      # #E5322D


def star_points(cx, cy, r_out, r_in, rotation=-math.pi / 2):
    pts = []
    for i in range(10):
        r = r_out if i % 2 == 0 else r_in
        a = rotation + i * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_logo(size):
    ss = 4  # supersampling para bordes suaves
    n = size * ss
    img = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    radius = int(n * 0.30)
    d.rounded_rectangle([0, 0, n - 1, n - 1], radius=radius, fill=GREEN)
    r_out = n * 0.33
    d.polygon(star_points(n / 2, n / 2 + n * 0.02, r_out, r_out * 0.42), fill=RED)
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    sizes = [16, 24, 32, 48, 64, 128, 256]
    base = draw_logo(256)
    base.save("fidel.ico", sizes=[(s, s) for s in sizes],
              append_images=[draw_logo(s) for s in sizes[:-1]])
    base.save("fidel_256.png")
    print("OK: fidel.ico y fidel_256.png generados")
