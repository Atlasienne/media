import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
from atl2 import *
from PIL import Image, ImageDraw

OUTP = "/home/claude/atlasienne/posts/01_moudawana/"
os.makedirs(OUTP, exist_ok=True)
FAM, LAB, N = "Société", "Actu", 8


def liste(path, chiffre, titre, items, pages, note=None):
    c = FAMILLES[FAM]
    img = Image.new("RGB", (W, H), PAPIER)
    d = ImageDraw.Draw(img)
    rubrique(d, dict(bg=PAPIER, fg=ENCRE, acc=CEDRE), FAM, LAB)
    y = 200
    if chiffre:
        d.text((M - 8, y), chiffre, font=serif(200, 520), fill=CEDRE, anchor="lt")
        y += 230
    for ln in wrap(d, titre, serif(64), W - 2 * M):
        d.text((M, y), ln, font=serif(64), fill=ENCRE, anchor="lt")
        y += 72
    y += 34
    f = sans(42, 380)
    for it in items:
        lines = wrap(d, it, f, W - 2 * M - 56)
        chevron(d, M, y + 8, 22, CEDRE)
        for ln in lines:
            d.text((M + 56, y), ln, font=f, fill=ENCRE, anchor="lt")
            y += 58
        y += 26
    if note:
        y += 10
        for ln in wrap(d, note, sans(32, 380), W - 2 * M):
            d.text((M, y), ln, font=sans(32, 380), fill=mix(ENCRE, PAPIER, .30), anchor="lt")
            y += 44
    pied(d, dict(bg=PAPIER, fg=CEDRE, acc=CEDRE), pages, PAPIER, img)
    grain(img).save(path)


# 1. Couverture
couverture(OUTP + "01.png", FAM, "Actu", "Moudawana : la réforme, c'est pour quand ?",
           "Nouveau gouvernement, même ministre de la Justice. Point au 18 octobre 2026.", f"1/{N}")

# 2 à 4. Les faits datés
interieure(OUTP + "02.png", FAM, "Actu", "16 oct.", "Abdellatif Ouahbi reste ministre de la Justice",
           "Le 16 octobre 2026, le Roi reçoit le gouvernement de Fatima Ezzahra El Mansouri. Le dossier du Code de la famille reste entre les mains du même ministre, en poste depuis 2021.", f"2/{N}")
interieure(OUTP + "03.png", FAM, "Actu", "12 août", "La réforme glisse à la nouvelle législature",
           "Le 12 août 2026, le ministre déclare : « Il reste encore quelques derniers ajustements ». Selon lui, le texte sera examiné au cours de la première année de la nouvelle législature. L'objectif annoncé au départ était fin 2025.", f"3/{N}")
interieure(OUTP + "04.png", FAM, "Actu", "0", "projet de loi déposé au Parlement à ce jour",
           "Le texte n'a été ni voté ni publié au Bulletin officiel. La seule loi applicable reste le Code de la famille de 2004. Méfie-toi des posts qui annoncent « ce qui change en 2026 ».", f"4/{N}")

# 5. Ce qui est proposé
liste(OUTP + "05.png", None, "Ce qui est proposé sur la garde des enfants",
      ["La garde partagée entre les deux parents, même après le divorce.",
       "La mère qui se remarie garde ses enfants.",
       "Le logement de l'enfant mieux protégé, chez le parent qui en a la garde.",
       "La mère associée à la tutelle légale, aujourd'hui réservée au père."],
      f"5/{N}", note="Propositions présentées le 24 décembre 2024. Le texte final peut encore changer.")

# 6. Ce que dit la loi aujourd'hui
liste(OUTP + "06.png", None, "Ce que dit la loi aujourd'hui",
      ["Après le divorce, la garde revient d'abord à la mère, puis au père, puis à la grand-mère maternelle (art. 171).",
       "Si la mère se remarie, elle peut perdre la garde d'un enfant de plus de 7 ans, sauf exceptions (art. 175).",
       "À 15 ans, l'enfant choisit chez quel parent il vit (art. 166).",
       "La tutelle légale reste au père : école, banque, papiers (art. 231 et 236)."],
      f"6/{N}")

# 7. Et maintenant
liste(OUTP + "07.png", None, "Ce qu'il faut surveiller",
      ["La déclaration de politique générale du gouvernement El Mansouri : la réforme y figurera-t-elle en priorité ?",
       "Une date de dépôt du projet de loi au Parlement.",
       "La publication de l'avis du Conseil supérieur des oulémas, réclamée par les associations."],
      f"7/{N}", note="Le 16 octobre, Me Ghizlaine Mamouni (Kif Mama Kif Baba) a demandé un texte dans les 100 premiers jours.")

# 8. Fin
av = avatar(OUTP + "_avatar.png")
fin(OUTP + "08.png", ["Morocco World News, 16 octobre 2026", "Le Matin, 16 octobre 2026", "Médias24, 12 août 2026",
                      "Médias24, 24 décembre 2024", "Code de la famille, loi 70-03 (2004)"],
    "Point arrêté au 18 octobre 2026", av)
os.remove(OUTP + "_avatar.png")

# planche de contrôle
ims = [Image.open(OUTP + f"{i:02d}.png") for i in range(1, N + 1)]
sheet = Image.new("RGB", (4 * 540 + 50, 2 * 675 + 30), "white")
for i, im in enumerate(ims):
    r, c = divmod(i, 4)
    sheet.paste(im.resize((540, 675), Image.LANCZOS), (10 + c * 550, 10 + r * 685))
sheet.save(OUTP + "planche.png")
print("ok")
