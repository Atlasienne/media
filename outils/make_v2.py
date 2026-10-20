import os, sys
sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import *
from PIL import Image, ImageDraw

os.makedirs(OUT, exist_ok=True)
for fam, c in FAMILLES.items():
    print(fam, "texte %.1f" % contrast(c["fg"], c["bg"]), "accent %.1f" % contrast(c["acc"], c["bg"]))
print("vif/papier %.1f" % contrast(VIF, PAPIER))


def vis_picto(kind):
    def f(d, c):
        tone = mix(c["bg"], c["fg"], 0.12) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, 0.07)
        d.ellipse([W - M - 430, 190, W - M, 620], fill=tone)
        picto(d, kind, W - M - 215, 405, 300, c["acc"], t=16)
    return f


av = avatar(OUT + "avatar.png")
posts = [
    dict(fam="Société", label="Portrait", titre="Fatima-Ezzahra El Mansouri, première femme cheffe du gouvernement", sous_titre="Son parcours en 7 dates", pages="1/7", visuel="paysage"),
    dict(fam="Argent", label="Carrière", titre="Négocier son salaire : le script", sous_titre="À copier avant ton entretien", pages="1/6", chiffre="4"),
    dict(fam="Bien-être", label="Confiance", titre="Dire non au travail sans se griller", pages="1/7"),
    dict(fam="Vie", label="Cuisine", titre="Une harira légère, prête en 30 minutes", pages="1/6", visuel=vis_picto("bol")),
    dict(fam="Style", label="Style", titre="Basiques d'automne à moins de 300 DH", sous_titre="Prix relevés en octobre", pages="1/7", chiffre="5"),
    dict(fam="Société", label="Droits", titre="Moudawana : qui a la garde des enfants ?", pages="1/8"),
    dict(fam="Bien-être", label="Bien-être", titre="Petits changements pour mieux dormir", pages="1/8", chiffre="7"),
    dict(fam="Argent", label="Argent", titre="CDD, CDI, ANAPEC : ce qui change pour toi", pages="1/7", visuel=vis_picto("piece")),
    dict(fam="Vie", label="Bons plans", titre="Sorties gratuites à Casablanca ce week-end", pages="1/5"),
]
tiles = [couverture(OUT + f"post_{i}.png", **p) for i, p in enumerate(posts)]
interieure(OUT + "interieure.png", "Société", "Portrait", "2009", "Élue maire de Marrakech",
           "Un premier mandat local, avant la scène nationale. Chaque date tient en deux lignes, sources en fin de carrousel.", "3/7",
           frise=[("1976", False), ("2009", True), ("2016", False), ("2021", False), ("2026", False)])
fin(OUT + "fin.png", ["TelQuel, 29 septembre 2026", "Euronews, 30 septembre 2026"], "Mis à jour le 18 octobre 2026", av)

# Maquette téléphone
PW = 1170
ph = Image.new("RGB", (PW, 3200), "#FFFFFF")
d = ImageDraw.Draw(ph)
d.text((PW / 2, 150), "atlasienne_com", font=sans(54, 600), fill="#000", anchor="mm")
a = av.resize((250, 250)); mk = Image.new("L", (250, 250), 0); ImageDraw.Draw(mk).ellipse([0, 0, 250, 250], fill=255)
ph.paste(a, (60, 240), mk)
for k, (n, l) in enumerate([("124", "publications"), ("18,4 k", "followers"), ("12", "suivi(e)s")]):
    x = 470 + k * 230
    d.text((x, 330), n, font=sans(50, 600), fill="#000", anchor="mm")
    d.text((x, 395), l, font=sans(36, 350), fill="#000", anchor="mm")
y = 540
d.text((60, y), "Atlasienne - Média féminin", font=sans(42, 600), fill="#000", anchor="lt"); y += 58
d.text((60, y), "Média/Actualités", font=sans(38, 350), fill="#737373", anchor="lt"); y += 56
BIO = ["Le média des Marocaines, clair et sourcé.", "Société, argent, bien-être, vie, style. En DH.", "Partenariats : écris-nous en message privé"]
for ln in BIO:
    d.text((60, y), ln, font=sans(40, 350), fill="#000", anchor="lt"); y += 54
y += 46
hl = list(FAMILLES.keys()) + ["Qui on est"]
for k, lab in enumerate(hl):
    cx = 110 + k * 190
    c = FAMILLES.get(lab, dict(bg=CEDRE, fg=PAPIER, acc=ROSE))
    d.ellipse([cx - 74, y, cx + 74, y + 148], outline="#DBDBDB", width=4)
    d.ellipse([cx - 64, y + 10, cx + 64, y + 138], fill=c["bg"])
    if lab == "Qui on est":
        sy = symbole(128); ph.paste(sy, (cx - 64, y + 10), sy)
    else:
        picto(d, PICTOS[lab], cx, y + 74, 76, c["acc"], t=6)
    d.text((cx, y + 190), lab, font=sans(32, 400), fill="#000", anchor="mm")
y += 260
gw = (PW - 4) // 3; gh = int(gw * 4 / 3)
for i, t in enumerate(tiles):
    r, col = divmod(i, 3)
    cw = int(H * 3 / 4)
    crop = t.crop(((W - cw) // 2, 0, (W + cw) // 2, H)).resize((gw, gh))
    ph.paste(crop, (col * (gw + 2), y + r * (gh + 2)))
ph = ph.crop((0, 0, PW, y + 3 * (gh + 2)))
ph.save(OUT + "phone.png")
small = ph.resize((390, int(ph.height * 390 / PW)))
small.save(OUT + "phone_reel.png")
row = Image.new("RGB", (W * 3 + 40, H), "white")
for k, f in enumerate(["post_4.png", "interieure.png", "fin.png"]):
    row.paste(Image.open(OUT + f), (k * (W + 20), 0))
row.save(OUT + "slides.png")
print("ok")
