import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from atl2 import *
from PIL import Image, ImageDraw
BW, BH = 2400, 1500
b = Image.new("RGB", (BW, BH), PAPIER); d = ImageDraw.Draw(b)
P = 110
logotype(d, P, 230, 150, CEDRE)
d.text((P, 300), "Le média des Marocaines, clair et sourcé.", font=sans(44, 380), fill=ENCRE, anchor="lt")
massif(d, P, 1150, 520, 120, mix(PAPIER, CEDRE, .12), sol=540)
av = Image.open(OUT + "avatar.png").resize((300, 300)); mk = Image.new("L", (300, 300), 0); ImageDraw.Draw(mk).ellipse([0, 0, 300, 300], fill=255)
b.paste(av, (1300, 110), mk)
d.text((1450, 450), "Photo de profil", font=sans(30, 400), fill=ENCRE, anchor="mm")
d.text((1700, 130), "Typographies", font=sans(32, 600), fill=ENCRE, anchor="lt")
d.text((1700, 185), "Fraunces", font=serif(90), fill=CEDRE, anchor="lt")
d.text((1700, 290), "Titres, chiffres, logo. Doux 100, Wonky 1.", font=sans(28, 380), fill=ENCRE, anchor="lt")
d.text((1700, 350), "Readex Pro", font=sans(70, 500), fill=CEDRE, anchor="lt")
d.text((1700, 440), "Texte et rubriques. Prête pour l'arabe.", font=sans(28, 380), fill=ENCRE, anchor="lt")
d.text((P, 640), "Couleurs", font=sans(32, 600), fill=ENCRE, anchor="lt")
cols = [("Cèdre", CEDRE, "Signature, Société"), ("Ardoise", ARDOISE, "Argent"), ("Rose argile", ROSE, "Bien-être"), ("Papier", PAPIER, "Vie, fonds clairs"), ("Mûre", MURE, "Style"), ("Vif", VIF, "Accent, jamais en fond")]
for i, (n, h, u) in enumerate(cols):
    x = P + i * 360
    d.rounded_rectangle([x, 700, x + 320, 900], radius=18, fill=h, outline=mix(PAPIER, CEDRE, .3), width=2)
    d.text((x, 925), n, font=sans(32, 560), fill=ENCRE, anchor="lt")
    d.text((x, 968), h, font=sans(28, 380), fill=ENCRE, anchor="lt")
    d.text((x, 1006), u, font=sans(28, 380), fill="#555", anchor="lt")
d.text((P, 1110), "Familles et pictogrammes", font=sans(32, 600), fill=ENCRE, anchor="lt")
for i, (fam, c) in enumerate(FAMILLES.items()):
    x = P + 90 + i * 430
    d.ellipse([x - 85, 1170, x + 85, 1340], fill=c["bg"], outline=mix(PAPIER, CEDRE, .25), width=3)
    picto(d, PICTOS[fam], x, 1255, 90, c["acc"], t=7)
    d.text((x, 1385), fam, font=sans(32, 500), fill=ENCRE, anchor="mm")
b = grain(b, 0.02)
b.save(OUT + "charte.png")
print("board ok")
