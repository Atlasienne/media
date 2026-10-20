exec(open("/home/claude/atlasienne/entre_nous.py").read())
from reel import reel
OUT = "/home/claude/media/reels_v3/respect/"
os.makedirs(OUT, exist_ok=True)
fs = [couverture_photo(OUT + "01.jpg", "s1.jpg", "« Tout mon respect »", "Le message de la première cheffe du gouvernement aux femmes.", None, fx=0.5, fy=0.35)]
S = [
 ("s0.jpg", "19 octobre 2026, au Parlement.", "Fatima Ezzahra El Mansouri sort de son texte.", 0.5, 0.35),
 ("q2.jpg", "« Que cette femme soit au foyer, en train d'élever ses enfants »", "Elle commence par toutes les femmes.", 0.5, 0.5),
 ("s2.jpg", "« Pour avoir moi-même connu ce parcours, je sais à quel point il peut être difficile »", "Elle parle des femmes en politique.", 0.5, 0.4),
 ("s3.jpg", "« Je leur adresse toutes mes salutations et tout mon respect »", "Aux élues et aux militantes.", 0.5, 0.45),
]
for k, (ph, a, b, fx, fy) in enumerate(S):
    fs.append(duo(OUT + f"{k+2:02d}.jpg", ph, a, b, None, fx, fy))
av = avatar("/tmp/_av4.png")
fs.append(fin_partage(OUT + "06.jpg", "Envoie-le à une femme qui fait bouger les choses.", "Source : Hespress, 20 octobre 2026.", av))
reel(fs, "/home/claude/media/reels_v3/respect.mp4", first=2.6, each=3.4, last=2.8)
tw, th = 432, 540
sh = Image.new("RGB", (len(fs) * (tw + 6), th), "white")
for i, f in enumerate(fs): sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
sh.save("/tmp/rev_C.png"); print("ok")
