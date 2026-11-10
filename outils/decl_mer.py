"""Atlasienne - déclinaison du gagnant « café seule » (pilier confiance et toi d'abord)."""
import sys
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v7d/"
SCR = "/tmp/claude-0/-home-claude-media/e434ee05-477c-5565-8d40-48f305b12364/scratchpad/"
N = "\u00a0"

REELS = {
 "01_mer-seule": ("ambiance_c_m.wav", [
  dict(photo="mer1w.jpg", fy=.4, phrase="Marcher seule au bord de la mer, un dimanche matin, sans rien prévoir.", taille=100),
  dict(photo="mer1w.jpg", fy=.4, phrase="Ce n'est pas que tu n'aies personne."),
  dict(photo="mer1w.jpg", fy=.4, phrase="C'est que tu as envie d'être avec toi.",
       cta=f"Envoie-le{N}à{N}celle qui{N}ne{N}sort{N}jamais{N}seule."),
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
