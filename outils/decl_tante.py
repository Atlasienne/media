"""Atlasienne - déclinaison du gagnant « gâteaux » (situations vécues, 17/11, 140 vues, 42,2 % à 3 s, 1 partage).
Même pilier (situations vécues), même accroche (« juste un peu » qui devient beaucoup), sujet différent : la visite chez la tante."""
import sys
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v8f/"
SCR = "/tmp/claude-0/-home-claude-media/c163fa71-2f35-5a4c-b84d-11388916b70b/scratchpad/"
N = " "

REELS = {
 "01_cinq-minutes": ("ambiance_c_m.wav", [
  dict(photo="the_verre.jpg", fy=.45, phrase=f"Tu passes chez ta tante pour «{N}juste{N}cinq{N}minutes{N}».", taille=104),
  dict(photo="the_verre.jpg", fy=.45, phrase="Elle sort le thé, puis les msemen, puis le tajine."),
  dict(photo="the_verre.jpg", fy=.45, phrase="Tu repars à minuit, avec un sac de restes à la main.",
       cta=f"Envoie-le à ta cousine. Elle{N}connaît{N}cette{N}tante."),
 ]),
}

if __name__ == "__main__":
    for slug, (mus, ecr) in REELS.items():
        out, tot, apercus = reel_anime(slug, R, ecr, musique=mus)
        tw, th = 270, 480
        sh = Image.new("RGB", (len(apercus) * (tw + 6), th), "white")
        for i, f in enumerate(apercus):
            sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
        sh.save(SCR + f"d_{slug}.png")
        print(slug, len(ecr), tot, apercus, flush=True)
