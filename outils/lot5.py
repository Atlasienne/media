"""Atlasienne - lot 5 (23 au 27/10/2026) : format animé court avec musique originale.
Ordre = ordre de publication, du moins fort au plus fort."""
import sys, os, json
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v5/"
SCR = "/tmp/claude-0/-home-claude/80f0fa8b-2fe2-5065-ba69-adce18957eea/scratchpad/"

REELS = {
 "01_plaisirs-50dh": ("ambiance_c_m.wav", [
  dict(photo="the_atlas.jpg", phrase="5 petits plaisirs à moins de 50 DH.", taille=104, fy=.55),
  dict(photo="menthe.jpg", phrase="Un thé en terrasse. Le hammam du quartier."),
  dict(photo="rideau.jpg", phrase="Des fleurs au marché. Un masque au ghassoul."),
  dict(photo="the_atlas.jpg", phrase="Et une heure rien que pour toi. Ça, c'est 0 DH.", fy=.55,
       cta="Envoie-le à celle qui ne pense jamais à elle."),
 ]),
 "02_hammam-therapie": ("ambiance_a_m.wav", [
  dict(photo="hammam.jpg", phrase="Le hammam du dimanche, c'est ma thérapie.", taille=104, fy=.45),
  dict(photo="hammam.jpg", phrase="En plus, c'est moins cher.", taille=104, fy=.45,
       cta="Tag celle avec qui tu y vas."),
 ]),
 "04_rien-a-me-mettre": ("ambiance_b_m.wav", [
  dict(photo="armoire.jpg", phrase="« Je n'ai rien à me mettre. »", taille=108, fy=.5),
  dict(photo="armoire.jpg", phrase="Moi, devant une armoire pleine.", taille=104, fy=.5,
       cta="Envoie-le à ta sœur, elle connaît l'armoire."),
 ]),
 "05_ma-mere": ("ambiance_c_m.wav", [
  dict(photo="menthe.jpg", phrase="Ma mère : « Ma\u00a0kayn\u00a0lli\u00a0bhalek. »", sous="Personne n'est comme toi.", taille=100, fy=.45),
  dict(photo="menthe.jpg", phrase="Aussi ma mère, le lendemain : « Chouf\u00a0bent\u00a0khaltek. »", sous="Regarde ta cousine.", taille=96, fy=.45,
       cta="Envoie-le à ta cousine. Elle aussi, elle l'entend."),
 ]),
 "06_pain": ("ambiance_a_m.wav", [
  dict(photo="pain.jpg", phrase="Je suis sortie acheter du pain.", taille=108, fy=.5),
  dict(photo="pain.jpg", phrase="Je suis rentrée avec trois sacs. Et pas de pain.", taille=100, fy=.5,
       cta="Tag celle qui fait pareil."),
 ]),
 "07_whatsapp-famille": ("ambiance_b_m.wav", [
  dict(photo="tel.jpg", flou=10, phrase="Le groupe WhatsApp de la famille, en vrai.", taille=100),
  dict(photo="tel.jpg", flou=10, duree=3.0, phrase="6 h du matin. Ton oncle envoie « Sbah\u00a0lkhir » avec une rose."),
  dict(photo="tel.jpg", flou=10, duree=3.0, phrase="Ta tante transfère une info « très importante ». Elle date de 2017."),
  dict(photo="tel.jpg", flou=10, duree=3.0, phrase="Ta mère : un vocal de 4 minutes pour dire qu'elle t'a appelée."),
  dict(photo="tel.jpg", flou=10, phrase="Toi : un « ok » à 23 h. Et le groupe passe en sourdine.",
       cta="Tag la cousine qui a mis le groupe en silencieux."),
 ]),
 "08_salaire": ("ambiance_c_m.wav", [
  dict(photo="pieces.jpg", flou=9, phrase="Mon salaire arrive le 1er.", taille=110, fy=.5),
  dict(photo="pieces.jpg", flou=9, phrase="Il repart le 5. Une relation courte mais intense.", taille=100, fy=.5,
       cta="Envoie-le à ta collègue qui compte les jours."),
 ]),
 "09_tante-mariage": ("ambiance_a_m.wav", [
  dict(photo="plafond.jpg", phrase="Ta tante, au mariage : « W\u00a0nti,\u00a0imta\u00a0? »", sous="Et toi, c'est pour quand ?", taille=100, fy=.45),
  dict(photo="plafond.jpg", phrase="Réponse polie : « Inchallah,\u00a0khalti. »", fy=.45),
  dict(photo="plafond.jpg", phrase="Réponse honnête : « Dès que je finis mes gâteaux. »", fy=.45),
  dict(photo="plafond.jpg", phrase="En vrai : sourire, prendre une corne de gazelle, changer de table.", fy=.45,
       cta="Tag la cousine qui l'a entendu trois fois cette année."),
 ]),
 "10_phrases-meres": ("ambiance_b_m.wav", [
  dict(photo="tajines.jpg", phrase="Les phrases que toutes les mères marocaines disent.", taille=96, fy=.6),
  dict(photo="tajines.jpg", phrase="« Chkoun\u00a0lli\u00a0gal\u00a0lik\u00a0? »", sous="Qui t'a dit ça ?", taille=116, fy=.6),
  dict(photo="tajines.jpg", phrase="« Ghir sber. »", sous="Patiente. Ça marche pour un rhume, un chagrin et une fin de mois.", taille=120, fy=.6),
  dict(photo="tajines.jpg", phrase="« Rah ana mok. »", sous="Je suis ta mère. Fin de la discussion.", taille=120, fy=.6,
       cta="Laquelle tu entends le plus ? Dis-le en commentaire."),
 ]),
}

if __name__ == "__main__":
    only = sys.argv[1:] or list(REELS)
    info = {}
    for slug in only:
        mus, ecr = REELS[slug]
        out, tot, apercus = reel_anime(slug, R, ecr, musique=mus)
        info[slug] = dict(ecrans=len(ecr), duree=tot)
        tw, th = 270, 480
        sh = Image.new("RGB", (len(apercus) * (tw + 6), th), "white")
        for i, f in enumerate(apercus):
            sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
        sh.save(SCR + f"r5_{slug}.png")
        print(slug, info[slug], flush=True)
