"""Atlasienne - lot 7 (07/11 au 14/11/2026). Ordre = ordre de publication, du moins fort au plus fort.
Changements : retour à 7 situations (elles retiennent de nouveau 30 à 52 % avec l'accroche phrase entendue),
darija mixte avec traduction (mieux que la darija pure), tous les cta en « Envoie-le à » (0 partage la semaine passée)."""
import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v7/"
SCR = "/tmp/claude-0/-home-claude-media/5bd1851a-678c-5bc9-a886-3a377d222e0e/scratchpad/"
N = " "

REELS = {
 "01_heures-sup": ("ambiance_a_m.wav", [
  dict(photo="bureau.jpg", flou=12, phrase=f"+25{N}% sur une heure sup faite en semaine entre 6{N}h et 21{N}h.", sous="C'est le Code du travail marocain.", taille=100),
  dict(photo="bureau.jpg", flou=12, phrase=f"Entre 21{N}h et 6{N}h, c'est +50{N}%."),
  dict(photo="bureau.jpg", flou=12, phrase=f"Au-delà de{N}44{N}h par{N}semaine, ton heure en plus n'est pas un cadeau.",
       cta="Envoie-le à ta collègue qui reste toujours tard."),
 ]),
 "02_ttilifoun": ("ambiance_b_m.wav", [
  dict(photo="tel.jpg", flou=8, phrase=f"Mama{N}: « Had ttilifoun t5ser. »", taille=108),
  dict(photo="tel.jpg", flou=8, phrase="Ana : ch3eltou.", taille=112),
  dict(photo="tel.jpg", flou=8, phrase=f"Mama{N}: « Chefti{N}? Nti lli katfehmi f had chi. »", taille=100,
       cta="Siftiha l lli dima katsle7 ttilifounat f ddar."),
 ]),
 "03_peur-quand-meme": ("ambiance_c_m.wav", [
  dict(photo="fenetre.jpg", phrase="Tu avais peur. Tu y es allée quand même.", taille=108),
  dict(photo="fenetre.jpg", phrase="Le courage, ce n'est pas ne plus avoir peur."),
  dict(photo="fenetre.jpg", phrase="C'est avoir peur, et y aller avec.",
       cta="Envoie-le à celle qui a un entretien cette semaine."),
 ]),
 "04_shampoing": ("ambiance_a_m.wav", [
  dict(photo="douche.jpg", phrase=f"Le 1er du mois{N}: « Je mérite le soin à 300{N}DH. »", taille=100),
  dict(photo="douche.jpg", phrase=f"Le 25{N}: tu rajoutes de l'eau dans le flacon."),
  dict(photo="douche.jpg", phrase=f"Et tu le secoues la tête en bas pour la{N}dernière{N}goutte.",
       cta="Envoie-le à celle qui fait pareil."),
 ]),
 "05_cafe-seule": ("ambiance_b_m.wav", [
  dict(photo="cafe_livre.jpg", phrase="Un café seule, ton livre, ton téléphone posé à l'envers.", taille=100),
  dict(photo="cafe_livre.jpg", phrase="Ce n'est pas de la solitude."),
  dict(photo="cafe_livre.jpg", phrase="C'est un rendez-vous avec toi.",
       cta="Envoie-le à celle qui n'ose pas encore y aller seule."),
 ]),
 "06_lpull": ("ambiance_c_m.wav", [
  dict(photo="pulls.jpg", phrase=f"« Fin howa lpull dyali{N}? »", taille=116),
  dict(photo="pulls.jpg", phrase=f"Khti{N}: « Ma 3reftch. »", taille=112),
  dict(photo="pulls.jpg", phrase="Lghedda, lqitou f tsawer dyalha.", taille=108,
       cta="Siftiha l khtek. Hiya 3arfa."),
 ]),
 "07_tghttiti": ("ambiance_a_m.wav", [
  dict(photo="plaid.jpg", phrase=f"Mal{N}à{N}la{N}tête{N}? Ta{N}mère{N}: «{N}Hit{N}ma tghettitich. »", sous="C'est parce que tu ne t'es pas couverte.", taille=96),
  dict(photo="plaid.jpg", phrase=f"Mal{N}au{N}ventre{N}? Pareil{N}: «{N}Hit{N}ma tghettitich. »"),
  dict(photo="plaid.jpg", phrase=f"Mal au genou après le sport{N}? Tu connais déjà la réponse.",
       cta="Envoie-le à ta mère. Elle va dire que c'est vrai."),
 ]),
 "08_ghadi-yjiw-dyaf": ("ambiance_b_m.wav", [
  dict(photo="salon.jpg", phrase=f"Ta mère{N}: « Ghadi yjiw dyaf. »", sous="Des invités vont venir.", taille=104),
  dict(photo="salon.jpg", phrase="Elle lave les rideaux, les tapis, et la chambre où personne n'entrera."),
  dict(photo="salon.jpg", phrase="Les invités restent vingt minutes. Au salon.",
       cta="Envoie-le à ta sœur. Elle a aussi frotté le balcon."),
 ]),
 "09_vocal-de-ta-tante": ("ambiance_c_m.wav", [
  dict(photo="rideau.jpg", phrase="Un vocal de 4 minutes de ta tante dans le groupe de la famille.", taille=96),
  dict(photo="rideau.jpg", phrase=f"Tu le passes en vitesse{N}×2."),
  dict(photo="rideau.jpg", phrase="Elle parle encore plus vite. Et à la fin : « Safi, bslama. »",
       cta="Envoie-le à ta cousine du groupe famille."),
 ]),
 "10_couturiere": ("ambiance_a_m.wav", [
  dict(photo="couture.jpg", phrase=f"La couturière{N}: «{N}Ghadi ykoun wajed nhar{N}lkhmis. »", sous="Ce sera prêt jeudi.", taille=96),
  dict(photo="couture.jpg", phrase=f"Jeudi{N}: « Daba daba. »", sous="Tout de suite.", taille=112),
  dict(photo="couture.jpg", phrase="Le caftan est prêt la veille du mariage. Et il est magnifique.",
       cta="Envoie-le à la copine qui t'accompagne aux mariages."),
 ]),
 "11_fakhoura-bik": ("ambiance_b_m.wav", [
  dict(photo="the_atlas.jpg", fy=.55, phrase="Garde la copine qui t'envoie un vocal juste pour dire :", taille=96),
  dict(photo="the_atlas.jpg", fy=.55, phrase=f"«{N}Ana{N}fakhoura{N}bik.{N}»", sous="Je suis fière de toi.", taille=100),
  dict(photo="the_atlas.jpg", fy=.55, phrase="Sans raison. Juste parce que tu existes.",
       cta="Envoie-le à cette copine-là."),
 ]),
 "12_tswira-wa7da": ("ambiance_c_m.wav", [
  dict(photo="salon_riad.jpg", phrase=f"Ta tante{N}: « Ghir tswira wa7da. »", sous="Juste une photo.", taille=108),
  dict(photo="salon_riad.jpg", phrase="47 photos plus tard, personne ne sourit au même moment."),
  dict(photo="salon_riad.jpg", phrase=f"Et elle envoie au groupe celle où tu as les{N}yeux{N}fermés.",
       cta="Envoie-le à celle qui ferme toujours les yeux en photo."),
 ]),
 "13_ghir-dqiqa": ("ambiance_a_m.wav", [
  dict(photo="menthe.jpg", fy=.45, phrase=f"La voisine sonne{N}: « Ghir dqiqa. »", sous="Juste une minute.", taille=108),
  dict(photo="menthe.jpg", fy=.45, phrase="Elle enlève ses chaussures."),
  dict(photo="menthe.jpg", fy=.45, phrase="Deux heures et trois verres de thé plus tard : « Safi, ghadi nmchi. »", sous="Bon, j'y vais."),
  dict(photo="menthe.jpg", fy=.45, phrase="Elle reste encore trente minutes. Sur le pas de la porte.",
       cta="Envoie-le à ta mère. Elle sait de qui on parle."),
 ]),
 "14_ila-jit": ("ambiance_b_m.wav", [
  dict(photo="cle.jpg", phrase=f"Toi{N}: « Mama, ma lqitch ssarout. »", sous="Maman, je ne trouve pas la clé.", taille=100),
  dict(photo="cle.jpg", phrase=f"Elle, depuis la cuisine{N}: « Ila jit w lqitou, 3ndek{N}! »", sous="Si je viens et que je la trouve, gare à toi.", taille=96),
  dict(photo="cle.jpg", phrase=f"Elle arrive. Elle la trouve en deux secondes. Là où tu as déjà regardé.",
       cta="Envoie-le à celle qui ne trouve jamais rien."),
 ]),
}

if __name__ == "__main__":
    only = sys.argv[1:] or list(REELS)
    for slug in only:
        mus, ecr = REELS[slug]
        out, tot, apercus = reel_anime(slug, R, ecr, musique=mus)
        tw, th = 270, 480
        sh = Image.new("RGB", (len(apercus) * (tw + 6), th), "white")
        for i, f in enumerate(apercus):
            sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
        sh.save(SCR + f"r7_{slug}.png")
        print(slug, len(ecr), tot, flush=True)
