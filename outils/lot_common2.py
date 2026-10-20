"""Atlasienne - lot 1 de lancement (9 posts)."""
import os, sys, json
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
from atl2 import *
from PIL import Image

BASE = "/home/claude/media/posts/lot02/"
DATE = "Point arrêté au 18 octobre 2026"
AV = avatar("/tmp/_av.png")


def vis_picto(kind):
    def f(d, c):
        tone = mix(c["bg"], c["fg"], 0.12) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, 0.07)
        d.ellipse([W - M - 430, 190, W - M, 620], fill=tone)
        picto(d, kind, W - M - 215, 405, 300, c["acc"], t=16)
    return f


def build(slug, fam, label, cover, slides, sources, date=DATE):
    out = BASE + slug + "/"
    os.makedirs(out, exist_ok=True)
    n = len(slides) + 2
    files = []
    p = out + "01.jpg"
    kw = dict(cover)
    kw["titre"] = fr(kw["titre"])
    kw["sous_titre"] = fr(kw.get("sous_titre"))
    couverture(p.replace(".jpg", ".png"), fam, label, pages=f"1/{n}", **kw)
    files.append(p)
    for i, s in enumerate(slides, start=2):
        p = out + f"{i:02d}.jpg"
        if s[0] == "i":
            _, ch, t, tx = s
            interieure(p.replace(".jpg", ".png"), fam, label, fr(ch), fr(t), fr(tx), f"{i}/{n}")
        else:
            _, t, items, note = s[:4]
            taille = s[4] if len(s) > 4 else 42
            liste(p.replace(".jpg", ".png"), fam, label, t, items, f"{i}/{n}", note=note, taille=taille)
        files.append(p)
    p = out + f"{n:02d}.jpg"
    fin(p.replace(".jpg", ".png"), [fr(x) for x in sources] if sources else None, date, AV)
    files.append(p)
    for f in files:
        Image.open(f.replace(".jpg", ".png")).convert("RGB").save(f, quality=92)
        os.remove(f.replace(".jpg", ".png"))
    return files


