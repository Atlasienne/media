"""Atlasienne - déclinaison du gagnant « juste une minute » (voisine, 13/11, 164 vues, 48,5 %, 1 partage).
Même pilier (situations vécues), même accroche (phrase entendue en darija, promesse courte qui s'allonge), sujet différent."""
import sys
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v8d/"
SCR = "/tmp/claude-0/-home-claude-media/bb4ae4e5-04a1-5935-a8f9-7ad1363b5b5c/scratchpad/"
N = " "
Z = [(600, 1580, 740, 1720, 18)]

REELS = {
 "01_joj-kelmat": ("ambiance_b_m.wav", [
  dict(photo="appel.jpg", fy=.5, zones_flou=Z, phrase=f"Ta cousine t'appelle{N}: « Ghir joj kelmat. »", sous="Juste deux mots.", taille=104),
  dict(photo="appel.jpg", fy=.5, zones_flou=Z, phrase="Une heure plus tard, tu connais toute la vie de sa voisine."),
  dict(photo="appel.jpg", fy=.5, zones_flou=Z, phrase=f"«{N}Safi, nkhellik. »", sous="Bon, je te laisse.", taille=112),
  dict(photo="appel.jpg", fy=.5, zones_flou=Z, phrase="Et elle te raconte encore une dernière histoire.",
       cta="Envoie-le à ta cousine. Elle va dire que ce n'est pas elle."),
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
