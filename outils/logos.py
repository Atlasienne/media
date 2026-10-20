import math, sys
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
from atl2 import *
from PIL import Image, ImageDraw

S = 4  # suréchantillonnage pour l'anticrénelage
OUTL = "/home/claude/atlasienne/logos/"
import os
os.makedirs(OUTL, exist_ok=True)


def canvas(n=1080, bg=CEDRE):
    img = Image.new("RGB", (n * S, n * S), bg)
    return img, ImageDraw.Draw(img), n * S


def done(img, n=1080):
    return img.resize((n, n), Image.LANCZOS)


def sommet(d, cx, cy, h, col, cut, sun=None, sun_col=ROSE):
    """A-montagne : sommet pointu, jambes épaisses, barre en ligne de crête découpée."""
    w = h * 0.98
    top = (cx, cy - h / 2)
    bl, br = (cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2)
    d.polygon([top, br, bl], fill=col)
    # contre-forme (vallée intérieure)
    t = h * 0.20
    it = (cx, cy - h / 2 + t * 2.05)
    ib = cy + h / 2
    k = (ib - it[1]) / h
    d.polygon([it, (cx + w / 2 * k - t * 0.55, ib), (cx - w / 2 * k + t * 0.55, ib)], fill=cut)
    if sun:
        r = h * 0.105
        sy = it[1] + (ib - it[1]) * 0.50
        d.ellipse([cx - r, sy - r, cx + r, sy + r], fill=sun_col)
    # barre = crête en zigzag, découpée dans les jambes
    by = cy + h * 0.14
    zz = [(cx - w * 0.36, by + h * .03), (cx - w * 0.16, by - h * .06), (cx - w * 0.04, by + h * .00),
          (cx + w * 0.08, by - h * .09), (cx + w * 0.22, by - h * .01), (cx + w * 0.36, by + h * .03)]
    d.line(zz, fill=cut, width=int(h * 0.05), joint="curve")


def c1_sommet():
    img, d, n = canvas()
    sommet(d, n / 2, n * 0.52, n * 0.56, PAPIER, CEDRE, sun=True)
    return done(img)


def losange(d, cx, cy, r, col, lw):
    pts = [(cx, cy - r), (cx + r * 0.78, cy), (cx, cy + r), (cx - r * 0.78, cy)]
    d.line(pts + [pts[0]], fill=col, width=lw, joint="curve")
    return pts


def c2_losange():
    img, d, n = canvas()
    cx, cy, r = n / 2, n / 2, n * 0.34
    lw = int(n * 0.034)
    losange(d, cx, cy, r, PAPIER, lw)
    losange(d, cx, cy, r * 0.70, PAPIER, int(lw * 0.6))
    # chevron intérieur = A / sommet
    hh = r * 0.42
    d.line([(cx - hh * 0.9, cy + hh * 0.55), (cx, cy - hh * 0.75), (cx + hh * 0.9, cy + hh * 0.55)],
           fill=ROSE, width=int(lw * 1.25), joint="curve")
    d.ellipse([cx - lw * .9, cy + hh * 0.55 - lw * .9, cx + lw * .9, cy + hh * 0.55 + lw * .9], fill=ROSE)
    # petits losanges aux pointes, comme sur les tapis
    for (x, y) in [(cx, cy - r * 1.17), (cx, cy + r * 1.17)]:
        q = n * 0.03
        d.polygon([(x, y - q), (x + q * .78, y), (x, y + q), (x - q * .78, y)], fill=ROSE)
    return done(img)


def arche_shape(cx, top, w, bottom, steps=90):
    """Arc outrepassé (fer à cheval) marocain."""
    r = w / 2
    ccy = top + r
    pts = []
    a0, a1 = math.radians(180 + 28), math.radians(360 - 28)
    # contour : du bas gauche, en montant, l'arc dépasse le demi-cercle
    start = math.radians(150)
    end = math.radians(390)
    for i in range(steps + 1):
        a = start + (end - start) * i / steps
        pts.append((cx + r * math.cos(a), ccy - r * math.sin(a) * -1 if False else ccy + r * math.sin(a) * -1))
    pts = [(cx - r * math.cos(math.radians(30)), bottom)] + pts + [(cx + r * math.cos(math.radians(30)), bottom)]
    return pts


def c3_arche():
    img, d, n = canvas()
    cx = n / 2
    w = n * 0.50
    top, bottom = n * 0.20, n * 0.80
    r = w / 2
    ccy = top + r
    pts = []
    for i in range(121):
        a = math.radians(-210 + 240 * i / 120)
        pts.append((cx + r * math.cos(a), ccy + r * math.sin(a)))
    x_end = pts[-1][0]
    x_start = pts[0][0]
    shape = [(x_start, bottom)] + pts + [(x_end, bottom)]
    d.polygon(shape, fill=PAPIER)
    # intérieur : soleil + massif
    d.ellipse([cx + r * 0.05, ccy - r * 0.15, cx + r * 0.55, ccy + r * 0.35], fill=ROSE)
    prof = [(0, .55), (.18, .25), (.32, .45), (.50, 0.0), (.64, .30), (.80, .12), (1, .5)]
    mx0, mx1, base, hh = x_start, x_end, ccy + r * 0.95, r * 0.95
    m = [(mx0 + (mx1 - mx0) * px, base - hh * (1 - py)) for px, py in prof]
    d.polygon([(mx0, bottom)] + m + [(mx1, bottom)], fill=CEDRE)
    # base de l'arche recoupée proprement
    d.rectangle([0, bottom, n, n], fill=CEDRE)
    return done(img)


def c4_sceau():
    img, d, n = canvas()
    cx = cy = n / 2
    R = n * 0.43
    d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=ROSE, width=int(n * 0.012))
    R2 = n * 0.30
    d.ellipse([cx - R2, cy - R2, cx + R2, cy + R2], outline=ROSE, width=int(n * 0.006))
    sommet(d, cx, cy + n * 0.01, n * 0.36, PAPIER, CEDRE, sun=True)
    # texte circulaire
    def ring(text, radius, start_deg, span_deg, size, top=True):
        f = sans(size, 600)
        chars = list(text)
        widths = [d.textlength(ch, font=f) for ch in chars]
        tot = sum(widths) + (len(chars) - 1) * size * 0.25
        ang_span = tot / radius
        a = math.radians(start_deg) - (ang_span / 2 if top else -ang_span / 2)
        for ch, wch in zip(chars, widths):
            step = (wch + size * 0.25) / radius
            mid = a + (step / 2 if top else -step / 2)
            x = cx + radius * math.cos(mid)
            y = cy + radius * math.sin(mid)
            tile = Image.new("RGBA", (size * 2, size * 2), (0, 0, 0, 0))
            ImageDraw.Draw(tile).text((size, size), ch, font=f, fill=PAPIER, anchor="mm")
            rot = -math.degrees(mid) - 90 if top else -math.degrees(mid) + 90
            tile = tile.rotate(rot, resample=Image.BICUBIC)
            img.paste(tile, (int(x - size), int(y - size)), tile)
            a += step if top else -step
    ring("ATLASIENNE", n * 0.365, -90, 0, int(n * 0.062), top=True)
    ring("MÉDIA DES MAROCAINES", n * 0.38, 90, 0, int(n * 0.040), top=False)
    for sx in (-1, 1):
        x = cx + sx * n * 0.365
        q = n * 0.012
        d.polygon([(x, cy - q), (x + q, cy), (x, cy + q), (x - q, cy)], fill=ROSE)
    return done(img)


concepts = {
    "1_sommet": c1_sommet(),
    "2_losange": c2_losange(),
    "3_arche": c3_arche(),
    "4_sceau": c4_sceau(),
}
for k, im in concepts.items():
    im.save(OUTL + k + ".png")

# planche : chaque concept en grand, en 110 px, en 40 px, et en bloc logo
BW, BH = 2400, 1700
b = Image.new("RGB", (BW, BH), "#FFFFFF")
d = ImageDraw.Draw(b)
names = {"1_sommet": "1. Le Sommet", "2_losange": "2. Le Losange", "3_arche": "3. L'Arche", "4_sceau": "4. Le Sceau"}
for i, (k, im) in enumerate(concepts.items()):
    x = 60 + i * 590
    d.text((x, 50), names[k], font=sans(44, 600), fill=ENCRE, anchor="lt")
    def circ(sz):
        a = im.resize((sz, sz), Image.LANCZOS)
        m = Image.new("L", (sz * 4, sz * 4), 0)
        ImageDraw.Draw(m).ellipse([0, 0, sz * 4, sz * 4], fill=255)
        return a, m.resize((sz, sz), Image.LANCZOS)
    a, m = circ(480); b.paste(a, (x, 130), m)
    a, m = circ(110); b.paste(a, (x, 660), m)
    a, m = circ(40); b.paste(a, (x + 140, 695), m)
    d.text((x, 790), "110 px et 40 px", font=sans(26, 400), fill="#666", anchor="lt")
    # bloc logo horizontal sur papier
    d.rectangle([x, 860, x + 540, 1100], fill=PAPIER)
    a, m = circ(150); b.paste(a, (x + 25, 905), m)
    d.text((x + 195, 985), "atlasienne", font=serif(64, 620), fill=CEDRE, anchor="lm")
    # en filigrane sur un post sombre
    d.rectangle([x, 1130, x + 540, 1640], fill=MURE)
    a, m = circ(70); b.paste(a, (x + 30, 1545), m)
    d.text((x + 115, 1580), "atlasienne", font=serif(40, 620), fill=PAPIER, anchor="lm")
    d.text((x + 30, 1200), "Exemple de pied", font=serif(52), fill=PAPIER, anchor="lt")
    d.text((x + 30, 1265), "de post", font=serif(52), fill=PAPIER, anchor="lt")
b.save(OUTL + "planche_logos.png")
print("ok")
