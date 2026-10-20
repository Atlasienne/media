exec(open("/home/claude/atlasienne/entre_nous.py").read())
OUT = "/home/claude/media/reels_src/en01/"
os.makedirs(OUT, exist_ok=True)
N = 9
P = lambda i: None
fs = []
fs.append(couverture_photo(OUT + "01.jpg", "p0.jpg", "Ce que tu fais en silence.", "Tu vas te reconnaître.", P(1), fx=0.5, fy=0.35))
S = [
    ("p1.jpg", "Tu aides tes parents chaque fin de mois.", "Sans jamais le dire.", 0.5, 0.45, 1.0),
    ("p2.jpg", "Tu reprends tes études à 30\u00a0ans.", "Pendant qu'on te demande quand tu te maries.", 0.5, 0.5, 1.0),
    ("p3.jpg", "Tu rentres du travail et tu enchaînes avec la maison.", "Personne n'appelle ça une deuxième journée.", 0.45, 0.5, 1.0),
    ("p4.jpg", "Tu souris au mariage de ta\u00a0cousine.", "Alors que ta semaine a été lourde.", 0.55, 0.35, 1.0),
    ("p5.jpg", "Tu mets de l'argent de côté, dirham par dirham.", "Pour ta liberté, pas pour une fête.", 0.5, 0.5, 1.0),
    ("p6.jpg", "Tu écoutes tout le monde.", "Et personne ne te demande comment tu vas.", 0.5, 0.35, 1.0),
    ("p7.jpg", "Personne ne te dit merci.", "Nous, on te le dit.", 0.5, 0.4, 1.0),
]
for k, (ph, a, b, fx, fy, z) in enumerate(S):
    fs.append(duo(OUT + f"{k + 2:02d}.jpg", ph, a, b, P(k + 2), fx, fy, z))
av = avatar("/tmp/_av.png")
fs.append(fin_partage(OUT + "09.jpg", "Envoie-le à celle qui fait tout ça.", "Elle a besoin de l'entendre aujourd'hui.", av))
tw, th = 432, 540
sh = Image.new("RGB", (5 * (tw + 6), 2 * (th + 6)), "white")
for i, f in enumerate(fs):
    r, c = divmod(i, 5)
    sh.paste(Image.open(f).resize((tw, th)), (c * (tw + 6), r * (th + 6)))
sh.save("/home/claude/atlasienne/review_en01r.png")
print("ok")
sys.path.insert(0, "/home/claude/atlasienne")
from reel import reel
reel(fs, "/home/claude/media/reels_v3/en-silence.mp4", first=2.6, each=3.4, last=3.4)
print("reel ok")
