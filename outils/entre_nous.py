"""Atlasienne - format "Entre nous" : photo couleur en haut, même photo en noir et blanc en bas."""
import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import *
from PIL import Image, ImageDraw, ImageFilter, ImageOps

EQ = "/home/claude/atlasienne/eq/hd/"
HALF = H // 2  # 675


def crop_to(im, w, h, fx=0.5, fy=0.5, zoom=1.0):
    """Recadre im au ratio w/h autour du point focal (fx, fy)."""
    iw, ih = im.size
    r = w / h
    if iw / ih > r:
        ch = ih / zoom
        cw = ch * r
    else:
        cw = iw / zoom
        ch = cw / r
    x0 = min(max(fx * iw - cw / 2, 0), iw - cw)
    y0 = min(max(fy * ih - ch / 2, 0), ih - ch)
    return im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((w, h), Image.LANCZOS)


def ombre_bas(img, y0, y1, force=0.62):
    """Dégradé sombre entre y0 et y1 pour lisibilité du texte."""
    ov = Image.new("L", (1, y1 - y0))
    for y in range(y1 - y0):
        t = y / max(1, (y1 - y0 - 1))
        ov.putpixel((0, y), int(255 * force * (t ** 1.6)))
    ov = ov.resize((W, y1 - y0))
    noir = Image.new("RGB", (W, y1 - y0), (12, 12, 10))
    zone = img.crop((0, y0, W, y1))
    zone = Image.composite(noir, zone, ov)
    img.paste(zone, (0, y0))


def texte_centre(img, txt, ybas, size=60, wght=720, col=(255, 255, 255)):
    """Texte centré dont la dernière ligne s'arrête à ybas, avec ombre portée douce."""
    d = ImageDraw.Draw(img)
    f = sans(size, wght)
    lines = wrap(d, fr(txt), f, W - 2 * 90)
    lh = int(size * 1.18)
    y = ybas - lh * len(lines)
    sh = Image.new("L", (W, H), 0)
    sd = ImageDraw.Draw(sh)
    for i, ln in enumerate(lines):
        sd.text((W / 2, y + i * lh + 4), ln, font=f, fill=200, anchor="ma")
    sh = sh.filter(ImageFilter.GaussianBlur(9))
    img.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), sh.point(lambda v: int(v * 0.55)))
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        d.text((W / 2, y + i * lh), ln, font=f, fill=col, anchor="ma")


def marque(img, pages, rub="Entre nous"):
    haut = Image.new("L", (1, 140))
    for y in range(140):
        haut.putpixel((0, y), int(255 * 0.65 * (1 - y / 139) ** 1.3))
    haut = haut.resize((W, 140))
    img.paste(Image.new("RGB", (W, 140), (12, 12, 10)), (0, 0), haut)
    d = ImageDraw.Draw(img)
    chevron(d, 64, 54, 22, ROSE)
    d.text((98, 50), rub, font=sans(32, 520), fill=PAPIER, anchor="la")
    s = 46
    sym = symbole(s)
    img.paste(sym, (64, H - 64 - s + 8), sym)
    logotype(d, 64 + s + 12, H - 58, 32, PAPIER)
    if pages:
        d.text((W - 64, H - 58), pages, font=sans(28, 420), fill=PAPIER, anchor="rs")


def duo(path, photo, haut, bas, pages, fx=0.5, fy=0.5, zoom=1.0):
    src = Image.open(EQ + photo).convert("RGB")
    c = crop_to(src, W, HALF, fx, fy, zoom)
    from PIL import ImageEnhance, ImageStat
    lum = ImageStat.Stat(ImageOps.grayscale(c)).mean[0]
    if lum > 120:
        c = ImageEnhance.Brightness(c).enhance(120 / lum)
    img = Image.new("RGB", (W, H))
    img.paste(c, (0, 0))
    nb = ImageOps.autocontrast(ImageOps.grayscale(c), cutoff=1)
    if ImageStat.Stat(nb).mean[0] > 115:
        nb = ImageEnhance.Brightness(nb).enhance(115 / ImageStat.Stat(nb).mean[0])
    nb = nb.convert("RGB")
    img.paste(nb, (0, HALF))
    ombre_bas(img, HALF - 320, HALF, 0.66)
    ombre_bas(img, H - 360, H, 0.74)
    # filet de séparation
    ImageDraw.Draw(img).line([(0, HALF), (W, HALF)], fill=(20, 20, 18), width=3)
    texte_centre(img, haut, HALF - 70)
    texte_centre(img, bas, H - 120)
    marque(img, pages)
    img.save(path, quality=92)
    return path


def couverture_photo(path, photo, titre, sous_titre, pages, fx=0.5, fy=0.4, zoom=1.0):
    src = Image.open(EQ + photo).convert("RGB")
    img = crop_to(src, W, H, fx, fy, zoom)
    ombre_bas(img, 420, H, 0.82)
    d = ImageDraw.Draw(img)
    f = serif(118, 560)
    lines = wrap(d, fr(titre), f, W - 2 * M)
    y = 1010 - 124 * len(lines)
    for ln in lines:
        d.text((M, y), ln, font=f, fill=PAPIER, anchor="la")
        y += 124
    yy = y + 26
    for ln in wrap(d, fr(sous_titre), sans(40, 420), W - 2 * M):
        d.text((M, yy), ln, font=sans(40, 420), fill=ROSE, anchor="la"); yy += 52
    marque(img, pages)
    img.save(path, quality=92)
    return path


def fin_partage(path, l1, l2, avatar_img):
    img = Image.new("RGB", (W, H), CEDRE)
    d = ImageDraw.Draw(img)
    f = serif(92, 560)
    y = 250
    for ln in wrap(d, fr(l1), f, W - 2 * M):
        d.text((M, y), ln, font=f, fill=PAPIER, anchor="la")
        y += 102
    y += 40
    for ln in wrap(d, fr(l2), sans(42, 400), W - 2 * M):
        d.text((M, y), ln, font=sans(42, 400), fill=ROSE, anchor="la")
        y += 58
    av = avatar_img.resize((130, 130))
    mk = Image.new("L", (130, 130), 0)
    ImageDraw.Draw(mk).ellipse([0, 0, 130, 130], fill=255)
    img.paste(av, (M, 960), mk)
    d.ellipse([M, 960, M + 130, 1090], outline=ROSE, width=4)
    d.text((M + 160, 1000), "Suis @atlasienne_com", font=sans(40, 560), fill=PAPIER, anchor="lt")
    d.text((M + 160, 1052), "Le média des Marocaines, clair et sourcé.", font=sans(34, 360), fill=ROSE, anchor="lt")
    pied(d, FAMILLES["Société"], None, CEDRE, img)
    grain(img).convert("RGB").save(path, quality=92)
    return path
