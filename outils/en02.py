exec(open("/home/claude/atlasienne/entre_nous.py").read())
OUT = "/home/claude/media/posts/entre-nous/02_phrases/"
os.makedirs(OUT, exist_ok=True)
N = 8
P = lambda i: f"{i}/{N}"
fs = [couverture_photo(OUT + "01.jpg", "q0.jpg", "Les phrases qu'on a toutes entendues.", "Et ce qu'on aurait aimé répondre.", P(1), fx=0.5, fy=0.4)]
S = [
    ("q1.jpg", "« Mazal ma tzewjti ? »", "Je construis ma vie d'abord. Le reste suivra.", 0.5, 0.35),
    ("q2.jpg", "« Nti bent, ma tkhrjich f lil. »", "Je suis prudente. Fais-moi confiance.", 0.5, 0.4),
    ("q3.jpg", "« Chnou ghadi ygoulou nnas ? »", "Les gens parleront de toute façon.", 0.5, 0.4),
    ("q4.jpg", "« Kbrti, khassek dir chi wlad. »", "Mon horloge, c'est moi qui la regarde.", 0.5, 0.35),
    ("q5.jpg", "« Khddama w ma kat3rfich ttiybi ? »", "J'ai appris à gagner ma vie. La cuisine, ça s'apprend aussi.", 0.5, 0.4),
    ("q6.jpg", "« Ma tqrayech bzzaf, rjal kayhrbou. »", "Ceux qui fuient ne m'intéressaient pas.", 0.5, 0.45),
]
for k, (ph, a, b, fx, fy) in enumerate(S):
    fs.append(duo(OUT + f"{k + 2:02d}.jpg", ph, a, b, P(k + 2), fx, fy))
av = avatar("/tmp/_av.png")
fs.append(fin_partage(OUT + "08.jpg", "Laquelle tu entends le plus ?", "Réponds en commentaire, et envoie-le à ta copine qui l'a déjà entendue.", av))
tw, th = 432, 540
sh = Image.new("RGB", (4 * (tw + 6), 2 * (th + 6)), "white")
for i, f in enumerate(fs):
    r, c = divmod(i, 4)
    sh.paste(Image.open(f).resize((tw, th)), (c * (tw + 6), r * (th + 6)))
sh.save("/home/claude/atlasienne/review_en02.png")
print("ok")
