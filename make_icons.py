# Genera los iconos de la app (assets/icon-*.png). Se ejecuta solo dentro de GitHub Actions.
from PIL import Image, ImageDraw
import os
S = 1024
os.makedirs('assets', exist_ok=True)
bg = Image.new('RGB', (S, S))
px = bg.load()
c1, c2 = (168, 85, 247), (13, 10, 26)
for y in range(S):
    for x in range(S):
        t = (x + y) / (2 * S - 2)
        px[x, y] = tuple(int(c1[i] * (1 - t) + c2[i] * t) for i in range(3))
fg = Image.new('RGBA', (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(fg)
kw, gap, kh, n = 104, 10, 340, 5
x0 = (S - (n * kw + (n - 1) * gap)) // 2
y0 = (S - kh) // 2
for i in range(n):
    x = x0 + i * (kw + gap)
    d.rounded_rectangle([x, y0, x + kw, y0 + kh], radius=22, fill=(250, 248, 255, 255))
for i in (0, 1, 3):
    x = x0 + (i + 1) * (kw + gap) - gap // 2 - 34
    d.rounded_rectangle([x, y0, x + 68, y0 + int(kh * .6)], radius=14, fill=(13, 10, 26, 255))
only = bg.convert('RGBA')
only.alpha_composite(fg)
only.save('assets/icon-only.png')
fg.save('assets/icon-foreground.png')
bg.save('assets/icon-background.png')
print('Iconos generados')
