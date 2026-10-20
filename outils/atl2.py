"""Atlasienne - moteur de rendu des visuels (v2)."""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

D = "/home/claude/atlasienne/"
OUT = "/home/claude/atlasienne/out3/"
F_SERIF = D + "fonts/Fraunces.ttf"
F_SANS = D + "fonts/Readex.ttf"

# Palette v2
CEDRE = "#17332C"   # seul fond très sombre, couleur signature
PAPIER = "#F2F0EB"
ROSE = "#E8B4A3"    # rose argile
ARDOISE = "#3E5C8A" # argent et carrière
MURE = "#8C4A72"    # style
VIF = "#D9466F"     # accent vif, chiffres et pastilles, jamais en fond
ENCRE = "#1A1A18"

# 5 familles fixes
FAMILLES = {
    "Société": dict(bg=CEDRE, fg=PAPIER, acc=ROSE),
    "Argent": dict(bg=ARDOISE, fg=PAPIER, acc=ROSE),
    "Bien-être": dict(bg=ROSE, fg=CEDRE, acc=CEDRE),
    "Vie": dict(bg=PAPIER, fg=CEDRE, acc=VIF),
    "Style": dict(bg=MURE, fg=PAPIER, acc=ROSE),
}

W, H, M = 1080, 1350, 100


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    a, b = hexrgb(a), hexrgb(b)
    return "#%02X%02X%02X" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def _font(path, size, wght, soft=100, wonk=1, opsz=None):
    f = ImageFont.truetype(path, int(size))
    vals = []
    for a in f.get_variation_axes():
        n = a["name"].decode() if isinstance(a["name"], bytes) else a["name"]
        if n == "Weight":
            vals.append(wght)
        elif n == "Optical Size":
            vals.append(opsz or max(a["minimum"], min(a["maximum"], size * 0.8)))
        elif n == "Softness":
            vals.append(soft)
        elif n == "Wonky":
            vals.append(wonk)
        else:
            vals.append(a["default"])
    f.set_variation_by_axes(vals)
    return f


def serif(size, wght=600):
    return _font(F_SERIF, size, wght)


def sans(size, wght=400):
    return _font(F_SANS, size, wght)


def wrap(d, text, font, width):
    words, lines, cur = [w for w in text.split(" ") if w], [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# Silhouette de crête : sommets inégaux, toujours la même pour la marque
CRETE = [(0, .55), (.06, .48), (.12, .60), (.20, .30), (.27, .45), (.33, .18), (.39, .38),
         (.46, 0.0), (.52, .25), (.57, .14), (.64, .42), (.72, .28), (.80, .50), (.88, .36), (.95, .52), (1, .46)]


def massif(d, x0, x1, ybase, haut, col, profil=CRETE, shift=0.0, sol=None):
    pts = []
    for px, py in profil:
        p = (px + shift) % 1.0 if shift else px
        pts.append((x0 + (x1 - x0) * px, ybase - haut * (1 - py)))
    if shift:
        pts = [(x0 + (x1 - x0) * px, ybase - haut * (1 - profil[(i + int(shift * len(profil))) % len(profil)][1]))
               for i, (px, py) in enumerate(profil)]
    fy = sol if sol is not None else ybase + 2000
    d.polygon([(x0, fy)] + pts + [(x1, fy)], fill=col)


def grain(img, amount=0.035, seed=7):
    rng = np.random.default_rng(seed)
    a = np.asarray(img).astype(np.float32)
    n = rng.normal(0, 255 * amount, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def chevron(d, x, y, h, col):
    w = h * 1.2
    d.line([(x, y + h), (x + w / 2, y), (x + w, y + h)], fill=col, width=max(3, int(h * 0.24)), joint="curve")
    return x + w


def logotype(d, x, y, size, col, anchor="ls"):
    d.text((x, y), "atlasienne", font=serif(size, 620), fill=col, anchor=anchor)


def rubrique(d, c, fam, label):
    xe = chevron(d, M, 92, 30, c["acc"])
    f1 = sans(44, 520)
    d.text((xe + 20, 122), fam, font=f1, fill=c["fg"], anchor="ls")
    if label and label != fam:
        x2 = xe + 20 + d.textlength(fam, font=f1) + 26
        d.text((x2, 122), label, font=sans(44, 340), fill=mix(c["fg"], c["bg"], 0.35), anchor="ls")


def pied(d, c, pages, img_bg):
    # bande de massif pleine, ton voisin du fond
    tone = mix(c["bg"], c["fg"], 0.10) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, 0.08)
    massif(d, 0, W, H - 70, 150, tone)
    logotype(d, M, H - 62, 42, c["fg"])
    if pages:
        d.text((W - M, H - 62), pages, font=sans(30, 400), fill=c["fg"], anchor="rs")


def titre_bloc(d, c, titre, sous_titre, bas=1040, taille=124, maxl=4):
    ts = taille
    f = serif(ts)
    lines = wrap(d, titre, f, W - 2 * M)
    while len(lines) > maxl:
        ts -= 6
        f = serif(ts)
        lines = wrap(d, titre, f, W - 2 * M)
    lh = int(ts * 1.03)
    st_lines = wrap(d, sous_titre, sans(38, 380), W - 2 * M) if sous_titre else []
    total = lh * len(lines) + (24 + 52 * len(st_lines) if st_lines else 0)
    y = bas - total
    for ln in lines:
        d.text((M, y), ln, font=f, fill=c["fg"], anchor="la")
        y += lh
    if st_lines:
        y += 24
        for ln in st_lines:
            d.text((M, y), ln, font=sans(38, 380), fill=c["fg"], anchor="la")
            y += 52
    return bas - total


def couverture(path, fam, label, titre, sous_titre=None, pages=None, chiffre=None, visuel=None):
    c = FAMILLES[fam]
    img = Image.new("RGB", (W, H), c["bg"])
    d = ImageDraw.Draw(img)
    if visuel == "paysage":
        # crêtes en couches, façon papier découpé
        sun = c["acc"] if fam != "Vie" else ROSE
        d.ellipse([W * 0.60, 200, W * 0.60 + 190, 390], fill=sun)
        for k, t in enumerate([0.30, 0.17, 0.0]):
            tone = mix(c["bg"], c["fg"], t) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, t * 0.7)
            prof = CRETE[k * 3:] + CRETE[:k * 3]
            prof = [(i / (len(prof) - 1), p[1]) for i, p in enumerate(prof)]
            massif(d, -40, W + 40, 470 + k * 55, 250 - k * 40, tone, prof)
        d.rectangle([0, 600, W, H], fill=c["bg"])
        titre_bloc(d, c, titre, sous_titre, bas=1075, taille=92)
    elif visuel:
        visuel(d, c)
        titre_bloc(d, c, titre, sous_titre, bas=1060, taille=104)
    elif chiffre:
        col = c["acc"] if fam not in ("Vie",) else VIF
        cs = 470
        while d.textlength(chiffre, font=serif(cs, 520)) > W - 2 * M and cs > 120:
            cs -= 10
        d.text((M - 14, 175 + (470 - cs) * 0.5), chiffre, font=serif(cs, 520), fill=col, anchor="lt")
        titre_bloc(d, c, titre, sous_titre, bas=1060, taille=104, maxl=3)
    else:
        ghost = mix(c["bg"], c["fg"], 0.12)
        picto(d, PICTOS[fam], W - M - 180, 400, 360, ghost, t=18)
        titre_bloc(d, c, titre, sous_titre, bas=1060, taille=146, maxl=3)
    rubrique(d, c, fam, label)
    pied(d, c, pages, c["bg"], img)
    img = grain(img)
    img.save(path)
    return img


# Pictogrammes au trait (même épaisseur que le chevron)
def picto(d, kind, cx, cy, s, col, t=None):
    t = t or max(4, int(s * 0.07))
    if kind == "balance":
        d.line([(cx, cy - s * .45), (cx, cy + s * .42)], fill=col, width=t)
        d.line([(cx - s * .45, cy - s * .30), (cx + s * .45, cy - s * .30)], fill=col, width=t)
        for sx in (-1, 1):
            x = cx + sx * s * .45
            d.line([(x, cy - s * .30), (x - s * .16, cy + s * .05)], fill=col, width=t)
            d.line([(x, cy - s * .30), (x + s * .16, cy + s * .05)], fill=col, width=t)
            d.arc([x - s * .18, cy - s * .08, x + s * .18, cy + s * .2], 0, 180, fill=col, width=t)
        d.line([(cx - s * .22, cy + s * .42), (cx + s * .22, cy + s * .42)], fill=col, width=t)
    elif kind == "piece":
        d.ellipse([cx - s * .42, cy - s * .42, cx + s * .42, cy + s * .42], outline=col, width=t)
        d.text((cx, cy + s * .02), "DH", font=sans(s * .34, 600), fill=col, anchor="mm")
    elif kind == "feuille":
        import math
        pts = []
        for i in range(41):
            u = i / 40
            pts.append((cx + s * .30 * math.sin(math.pi * u), cy - s * .48 + s * .96 * u))
        for i in range(41):
            u = 1 - i / 40
            pts.append((cx - s * .30 * math.sin(math.pi * u), cy - s * .48 + s * .96 * u))
        d.line(pts + [pts[0]], fill=col, width=t, joint="curve")
        d.line([(cx, cy - s * .30), (cx, cy + s * .48)], fill=col, width=t)
    elif kind == "soleil":
        import math
        d.arc([cx - s * .30, cy - s * .12, cx + s * .30, cy + s * .48], 180, 360, fill=col, width=t)
        d.line([(cx - s * .5, cy + s * .18), (cx + s * .5, cy + s * .18)], fill=col, width=t)
        for a in (180 + 22, 180 + 56, 270, 360 - 56, 360 - 22):
            r = math.radians(a)
            d.line([(cx + s * .40 * math.cos(r), cy + s * .18 + s * .40 * math.sin(r)),
                    (cx + s * .54 * math.cos(r), cy + s * .18 + s * .54 * math.sin(r))], fill=col, width=t)
    elif kind == "alerte":
        d.line([(cx, cy - s * .48), (cx + s * .5, cy + s * .40), (cx - s * .5, cy + s * .40), (cx, cy - s * .48)], fill=col, width=t, joint="curve")
        d.line([(cx, cy - s * .16), (cx, cy + s * .12)], fill=col, width=t)
        d.ellipse([cx - t * .7, cy + s * .24 - t * .7, cx + t * .7, cy + s * .24 + t * .7], fill=col)
    elif kind == "goutte":
        import math
        pts = []
        for i in range(61):
            a = math.radians(-30 + 240 * i / 60)
            pts.append((cx + s * .30 * math.cos(a), cy + s * .14 + s * .30 * math.sin(a) * -1 * -1))
        d.line([(cx, cy - s * .5)] + [(cx + s * .30 * math.cos(math.radians(a)), cy + s * .16 + s * .30 * math.sin(math.radians(a))) for a in range(-30, 211, 4)] + [(cx, cy - s * .5)], fill=col, width=t, joint="curve")
    elif kind == "ruban":
        d.arc([cx - s * .22, cy - s * .52, cx + s * .22, cy - s * .02], 180, 360, fill=col, width=t)
        d.line([(cx - s * .22, cy - s * .27), (cx + s * .26, cy + s * .48)], fill=col, width=t)
        d.line([(cx + s * .22, cy - s * .27), (cx - s * .26, cy + s * .48)], fill=col, width=t)
    elif kind == "ampoule":
        d.ellipse([cx - s * .32, cy - s * .5, cx + s * .32, cy + s * .14], outline=col, width=t)
        d.line([(cx - s * .14, cy + s * .14), (cx - s * .14, cy + s * .30), (cx + s * .14, cy + s * .30), (cx + s * .14, cy + s * .14)], fill=col, width=t)
        d.line([(cx - s * .12, cy + s * .42), (cx + s * .12, cy + s * .42)], fill=col, width=t)
        d.line([(cx - s * .08, cy - s * .05), (cx, cy - s * .18), (cx + s * .08, cy - s * .05)], fill=col, width=max(3, t - 2))
    elif kind == "bol":
        d.chord([cx - s * .45, cy - s * .35, cx + s * .45, cy + s * .45], 0, 180, outline=col, width=t)
        d.line([(cx - s * .5, cy + s * .05), (cx + s * .5, cy + s * .05)], fill=col, width=t)
        for dx in (-.15, .1):
            d.arc([cx + s * dx - s * .08, cy - s * .45, cx + s * dx + s * .08, cy - s * .1], 90, 270, fill=col, width=max(3, t - 1))
    elif kind == "cintre":
        d.arc([cx - s * .08, cy - s * .48, cx + s * .1, cy - s * .28], 180, 90, fill=col, width=t)
        d.line([(cx, cy - s * .2), (cx - s * .48, cy + s * .25), (cx + s * .48, cy + s * .25), (cx, cy - s * .2)], fill=col, width=t, joint="curve")
    elif kind == "a":
        d.text((cx, cy + s * .05), "a", font=serif(s * .9, 600), fill=col, anchor="mm")


PICTOS = {"Société": "balance", "Argent": "piece", "Bien-être": "soleil", "Vie": "bol", "Style": "cintre"}


def interieure(path, fam, label, chiffre, titre, texte, pages, frise=None):
    c = FAMILLES[fam]
    img = Image.new("RGB", (W, H), PAPIER)
    d = ImageDraw.Draw(img)
    cc = dict(bg=PAPIER, fg=CEDRE, acc=c["bg"] if fam not in ("Vie", "Bien-être") else VIF)
    rubrique(d, dict(bg=PAPIER, fg=ENCRE, acc=cc["acc"]), fam, label)
    cs = 230
    while d.textlength(chiffre, font=serif(cs, 520)) > W - 2 * M and cs > 100:
        cs -= 10
    d.text((M - 8, 200), chiffre, font=serif(cs, 520), fill=cc["acc"], anchor="lt")
    y = 470
    for ln in wrap(d, titre, serif(76), W - 2 * M):
        d.text((M, y), ln, font=serif(76), fill=ENCRE, anchor="la")
        y += 82
    y += 28
    for ln in wrap(d, texte, sans(40, 360), W - 2 * M - 30):
        d.text((M, y), ln, font=sans(40, 360), fill=ENCRE, anchor="la")
        y += 60
    if frise:
        fy = 1060
        d.line([(M, fy), (W - M, fy)], fill=mix(PAPIER, CEDRE, .45), width=5)
        n = len(frise)
        for i, (yr, on) in enumerate(frise):
            x = M + (W - 2 * M) * i / (n - 1)
            r = 16 if on else 10
            d.ellipse([x - r, fy - r, x + r, fy + r], fill=CEDRE if on else mix(PAPIER, CEDRE, .45))
            d.text((x, fy + 54), yr, font=sans(32, 600 if on else 420), fill=ENCRE, anchor="mm")
    pied(d, dict(bg=PAPIER, fg=CEDRE, acc=cc["acc"]), pages, PAPIER, img)
    img = grain(img)
    img.save(path)
    return img


def fin(path, sources, date, avatar):
    c = FAMILLES["Société"]
    img = Image.new("RGB", (W, H), CEDRE)
    d = ImageDraw.Draw(img)
    y = 230
    for ln in ["Garde-le pour plus tard,", "envoie-le à celle", "qui en a besoin."]:
        d.text((M, y), ln, font=serif(84), fill=PAPIER, anchor="la")
        y += 92
    y += 90
    if sources:
        d.text((M, y), "Sources", font=sans(34, 600), fill=ROSE, anchor="lt")
        y += 58
    else:
        sources = []
    for s in sources:
        d.text((M, y), s, font=sans(34, 360), fill=PAPIER, anchor="la")
        y += 50
    d.text((M, y + 18), date, font=sans(32, 360), fill=ROSE, anchor="lt")
    # bloc abonnement
    av = avatar.resize((130, 130))
    mk = Image.new("L", (130, 130), 0)
    ImageDraw.Draw(mk).ellipse([0, 0, 130, 130], fill=255)
    img.paste(av, (M, 960), mk)
    d.ellipse([M, 960, M + 130, 1090], outline=ROSE, width=4)
    d.text((M + 160, 1000), "Suis @atlasienne_com", font=sans(40, 560), fill=PAPIER, anchor="lt")
    d.text((M + 160, 1052), "Le média des Marocaines, clair et sourcé.", font=sans(34, 360), fill=ROSE, anchor="lt")
    pied(d, c, None, CEDRE, img)
    img = grain(img)
    img.save(path)
    return img


def avatar(path, s=1080):
    img = Image.new("RGB", (s, s), CEDRE)
    d = ImageDraw.Draw(img)
    size = s * 0.66
    for _ in range(6):
        f = serif(int(size), 600)
        bb = d.textbbox((0, 0), "a", font=f, anchor="lt")
        size *= (s * 0.50) / (bb[3] - bb[1])
    f = serif(int(size), 600)
    bb = d.textbbox((0, 0), "a", font=f, anchor="lt")
    gw, gh = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((s - gw) / 2 - bb[0], (s - gh) / 2 - bb[1] - s * 0.02), "a", font=f, fill=PAPIER, anchor="lt")
    img.save(path)
    return img


def lum(h):
    r, g, b = [x / 255 for x in hexrgb(h)]
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ---------- Kit profil (v2.1) ----------

def filigrane(d, x, y, col, size=42, anchor="ls"):
    """Filigrane officiel : logotype "atlasienne" en bas à gauche, à 100 px des bords.
    Toujours présent sur chaque visuel (déjà intégré dans pied())."""
    logotype(d, x, y, size, col, anchor)


def filigrane_png(path, col=PAPIER, size=120):
    """Filigrane transparent pour poser sur une photo ou une vidéo."""
    f = serif(size, 620)
    tmp = Image.new("RGBA", (10, 10))
    bb = ImageDraw.Draw(tmp).textbbox((0, 0), "atlasienne", font=f, anchor="lt")
    img = Image.new("RGBA", (bb[2] + 20, bb[3] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((10, 10), "atlasienne", font=f, fill=col, anchor="lt")
    img.save(path)
    return img


def couverture_une(path, fam):
    """Couverture de story à la une, 1080x1920, picto centré dans la zone ronde."""
    c = FAMILLES.get(fam, dict(bg=CEDRE, fg=PAPIER, acc=ROSE))
    img = Image.new("RGB", (1080, 1920), c["bg"])
    d = ImageDraw.Draw(img)
    if fam in PICTOS:
        picto(d, PICTOS[fam], 540, 960, 420, c["acc"], t=26)
    else:
        f = serif(560, 600)
        bb = d.textbbox((0, 0), "a", font=f, anchor="lt")
        d.text((540 - (bb[2] - bb[0]) / 2 - bb[0], 960 - (bb[3] - bb[1]) / 2 - bb[1] - 20), "a", font=f, fill=PAPIER, anchor="lt")
    img = grain(img, 0.025)
    img.save(path, quality=95)
    return img


# ---------- Symbole v3 : le losange tissé (18/10/2026) ----------
from PIL import ImageChops


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



def pied(d, c, pages, img_bg, img=None):
    tone = mix(c["bg"], c["fg"], 0.10) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, 0.08)
    massif(d, 0, W, H - 70, 150, tone)
    s = 66
    sym = symbole(s)
    if img is not None:
        img.paste(sym, (M, H - 62 - 50), sym)
        logotype(d, M + s + 16, H - 62, 42, c["fg"])
    else:
        logotype(d, M, H - 62, 42, c["fg"])
    if pages:
        d.text((W - M, H - 62), pages, font=sans(30, 400), fill=c["fg"], anchor="rs")


def avatar(path, s=1080):
    sym = symbole(s)
    img = Image.new("RGB", (s, s), CEDRE)
    img.paste(sym, (0, 0), sym)
    img.save(path)
    return img


def filigrane_png(path, col=PAPIER, size=120):
    f = serif(size, 620)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bb = tmp.textbbox((0, 0), "atlasienne", font=f, anchor="lt")
    sz = int(size * 1.6)
    img = Image.new("RGBA", (sz + 30 + bb[2] + 20, sz + 20), (0, 0, 0, 0))
    sym = symbole(sz)
    img.paste(sym, (10, 10), sym)
    ImageDraw.Draw(img).text((sz + 30, 10 + sz / 2), "atlasienne", font=f, fill=col, anchor="lm")
    img.save(path)
    return img


def couverture_une(path, fam):
    c = FAMILLES.get(fam, dict(bg=CEDRE, fg=PAPIER, acc=ROSE))
    img = Image.new("RGB", (1080, 1920), c["bg"])
    d = ImageDraw.Draw(img)
    if fam in PICTOS:
        picto(d, PICTOS[fam], 540, 960, 420, c["acc"], t=26)
    else:
        sym = symbole(760)
        img.paste(sym, (160, 580), sym)
    img = grain(img, 0.025)
    img.save(path, quality=95)
    return img


def fr(t):
    """Typographie française : espaces insécables."""
    if t is None:
        return t
    NB = "\u00a0"
    import re
    for a, b in [(" :", NB + ":"), (" ?", NB + "?"), (" !", NB + "!"), (" %", NB + "%"), ("« ", "«" + NB), (" »", NB + "»"), (" DH", NB + "DH"), (" kWh", NB + "kWh"), ("'", "\u2019")]:
        t = t.replace(a, b)
    t = re.sub(r"(\d) (\d{3})", "\\1" + NB + "\\2", t)
    return t


def liste(path, fam, label, titre, items, pages, note=None, chiffre=None, taille=42):
    c = FAMILLES[fam]
    acc = c["bg"] if fam not in ("Vie", "Bien-être") else VIF
    img = Image.new("RGB", (W, H), PAPIER)
    d = ImageDraw.Draw(img)
    rubrique(d, dict(bg=PAPIER, fg=ENCRE, acc=acc), fam, label)
    y = 200
    if chiffre:
        d.text((M - 8, y), chiffre, font=serif(200, 520), fill=acc, anchor="lt")
        y += 230
    for ln in wrap(d, fr(titre), serif(64), W - 2 * M):
        d.text((M, y), ln, font=serif(64), fill=ENCRE, anchor="la")
        y += 72
    y += 30
    f = sans(taille, 380)
    lh = int(taille * 1.38)
    for it in items:
        chevron(d, M, y + taille * 0.2, taille * 0.52, acc)
        for ln in wrap(d, fr(it), f, W - 2 * M - 56):
            d.text((M + 56, y), ln, font=f, fill=ENCRE, anchor="la")
            y += lh
        y += int(taille * 0.6)
    if note:
        y += 6
        for ln in wrap(d, fr(note), sans(32, 380), W - 2 * M):
            d.text((M, y), ln, font=sans(32, 380), fill=mix(ENCRE, PAPIER, .30), anchor="la")
            y += 44
    if y > H - 230:
        print("ATTENTION débordement", path, y)
    pied(d, dict(bg=PAPIER, fg=CEDRE, acc=acc), pages, PAPIER, img)
    grain(img).save(path)
