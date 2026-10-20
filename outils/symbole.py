"""Symbole Atlasienne : le losange tissé avec un A qui se lève."""
import sys; sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import *
from PIL import Image, ImageDraw, ImageChops

def symbole(n=1080, fond=CEDRE, cadre=PAPIER, a_col=ROSE, point=ROSE, disque=True, ss=4):
    N = n * ss; k = N / 1000
    P = lambda pts: [(x * k, y * k) for x, y in pts]
    img = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if disque:
        d.ellipse([0, 0, N - 1, N - 1], fill=fond)
    outer = P([(500, 150), (770, 500), (500, 850), (230, 500)])
    inner = P([(500, 248), (694, 500), (500, 752), (306, 500)])
    # cadre = extérieur moins intérieur
    m = Image.new("L", (N, N), 0); dm = ImageDraw.Draw(m)
    dm.polygon(outer, fill=255); dm.polygon(inner, fill=0)
    img.paste(Image.new("RGBA", (N, N), cadre), (0, 0), m)
    # chevron A en onglet, découpé sur le losange intérieur
    ch = Image.new("L", (N, N), 0); dc = ImageDraw.Draw(ch)
    dc.polygon(P([(500, 292), (318, 760), (682, 760)]), fill=255)
    dc.polygon(P([(500, 455), (380, 760), (620, 760)]), fill=0)
    clip = Image.new("L", (N, N), 0); ImageDraw.Draw(clip).polygon(inner, fill=255)
    ch = ImageChops.multiply(ch, clip)
    img.paste(Image.new("RGBA", (N, N), a_col), (0, 0), ch)
    # point
    r = 32 * k; cy = 648 * k; cx = 500 * k
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=point)
    return img.resize((n, n), Image.LANCZOS)

if __name__ == "__main__":
    s = symbole()
    bg = Image.new("RGB", s.size, CEDRE); bg.paste(s, (0, 0), s); bg.save("logos/symbole_final.png")
    b = Image.new("RGB", (2000, 1100), "white"); d = ImageDraw.Draw(b)
    b.paste(s.resize((520, 520), Image.LANCZOS), (40, 40), s.resize((520, 520), Image.LANCZOS))
    for sz, x in [(110, 600), (64, 740), (40, 840)]:
        t = s.resize((sz, sz), Image.LANCZOS); b.paste(t, (x, 250), t)
    inv = symbole(520, fond=PAPIER, cadre=CEDRE, a_col=MURE, point=VIF)
    b.paste(inv, (960, 40), inv)
    d.ellipse([958, 38, 1482, 562], outline="#DDD", width=2)
    # bloc logo
    d.rectangle([40, 620, 1000, 1060], fill=PAPIER)
    t = s.resize((300, 300), Image.LANCZOS); b.paste(t, (80, 690), t)
    d.text((420, 840), "atlasienne", font=serif(120, 620), fill=CEDRE, anchor="lm")
    d.rectangle([1040, 620, 1960, 1060], fill=MURE)
    t = s.resize((90, 90), Image.LANCZOS); b.paste(t, (1100, 950), t)
    d.text((1205, 995), "atlasienne", font=serif(46, 620), fill=PAPIER, anchor="lm")
    d.text((1100, 680), "Pied de post", font=serif(64), fill=PAPIER, anchor="lt")
    b.save("logos/planche_symbole.png"); print("ok")
