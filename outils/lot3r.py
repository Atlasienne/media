import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
from atl2 import *
from reel import reel
OUT = "/home/claude/media/reels_v3/"
os.makedirs(OUT, exist_ok=True)
av = avatar("/tmp/_av3.png")
D = "Point arrêté au 20 octobre 2026"
SRC = ["Le Brief, 19 octobre 2026", "Médias24, 19 octobre 2026", "Yabiladi, 19 octobre 2026"]

def post(slug, fam, lab, cover, slides, sources):
    d = OUT + slug + "/"; os.makedirs(d, exist_ok=True); fs = []
    p = d + "01.jpg"; couverture(p, fam, lab, cover["titre"], cover["sous_titre"], None, cover["chiffre"]); fs.append(p)
    for i, s in enumerate(slides, 2):
        p = d + f"{i:02d}.jpg"
        if s[0] == "i": interieure(p, fam, lab, s[1], fr(s[2]), fr(s[3]), None)
        else: liste(p, fam, lab, fr(s[1]), [fr(x) for x in s[2]], None, note=fr(s[3]) if s[3] else None)
        fs.append(p)
    p = d + f"{len(fs)+1:02d}.jpg"; fin(p, sources, D, av); fs.append(p)
    reel(fs, OUT + slug + ".mp4", first=2.6, each=3.6, last=2.6)
    return fs

A = post("veuves-100", "Argent", "Retraite",
  dict(chiffre="100 %", titre="de la pension du mari pour les veuves ? La promesse du gouvernement", sous_titre="Programme présenté au Parlement le 19 octobre 2026"),
  [("i", "50 %", "pour une veuve aujourd'hui", "La pension de réversion versée à la veuve correspond aujourd'hui à la moitié de la pension principale du mari décédé."),
   ("i", "100 %", "l'objectif annoncé le 19 octobre", "Fatima Ezzahra El Mansouri l'a inscrit dans le programme du gouvernement présenté au Parlement. Les droits des orphelins seraient préservés."),
   ("i", "3 000 DH", "de pension minimale par mois, à terme", "Le programme prévoit de l'atteindre progressivement dans les différents régimes de retraite."),
   ("l", "Ce qu'il faut retenir", ["C'est un engagement du programme 2026-2031, pas encore une loi.", "Aucune date d'entrée en vigueur n'a été annoncée.", "Pour l'instant, rien ne change sur les pensions versées."], None)],
  SRC)
B = post("aide-1000", "Argent", "Aides",
  dict(chiffre="1 000 DH", titre="d'aide sociale par mois : ce que promet le nouveau gouvernement", sous_titre="Ce qui est annoncé, et ce qui ne l'est pas encore"),
  [("i", "500 DH", "le minimum versé aujourd'hui par ménage", "Le programme présenté au Parlement le 19 octobre 2026 vise 1 000 DH d'ici la fin du mandat, en 2031."),
   ("i", "100 DH", "de facture d'électricité prise en charge", "Pour les ménages éligibles, quand la facture mensuelle de la résidence principale ne dépasse pas 100 DH. Automatique et sans dossier, selon l'annonce."),
   ("i", "40 000 DH", "d'aide pour construire ou rénover en milieu rural", "100 000 logements visés pendant le mandat, avec un accompagnement technique gratuit."),
   ("l", "Ce qu'on ne sait pas encore", ["Le calendrier de la hausse de l'aide sociale.", "La date de départ pour l'électricité.", "Les conditions exactes pour chaque aide."], "Les critères seront revus selon les revenus réels, d'après le programme.")],
  SRC)
from PIL import Image
for name, fs in (("A", A), ("B", B)):
    tw, th = 432, 540
    sh = Image.new("RGB", (len(fs) * (tw + 6), th), "white")
    for i, f in enumerate(fs): sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
    sh.save(f"/tmp/rev_{name}.png")
print("ok")
