"""Atlasienne - déclinaison du gagnant « hammam » (darija pure, mère, 15/11, 1424 vues, 59,4 % à 3 s, 7 partages).
Même pilier (darija et mères), même accroche (phrase de mère en darija, promesse courte qui grossit), sujet différent : le repas."""
import sys
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v8e/"
SCR = "/tmp/claude-0/-home-claude-media/0ac7d0dd-3351-5849-a9e4-b0e2aba7b42d/scratchpad/"
N = " "

REELS = {
 "01_ghir-chwiya": ("ambiance_a_m.wav", [
  dict(photo="tajine.jpg", fy=.6, phrase=f"Mama f lmakla{N}: «{N}Ghir chwiya, bach tdouqi. »", taille=104),
  dict(photo="tajine.jpg", fy=.6, phrase="W kat3emmer lik tebsil hta lfoq.", taille=104),
  dict(photo="tajine.jpg", fy=.6, phrase=f"W f lekher{N}: «{N}Mal ma klitich walou{N}? »", taille=104,
       cta="Siftiha l khtek. Hta hiya douzatha."),
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
