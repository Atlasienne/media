"""Atlasienne - lot 6 (31/10 au 06/11/2026). Ordre = ordre de publication, du moins fort au plus fort.
Changement : accroche = phrase entendue (souvent en darija) dès l'écran 1, plus de mères et de darija."""
import sys, os, json
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v6/"
SCR = "/tmp/claude-0/-home-claude-media/fbc94162-b954-5447-90bd-c9632b6711ce/scratchpad/"
N = " "

REELS = {
 "01_sac-de-sacs": ("ambiance_a_m.wav", [
  dict(photo="courses.jpg", phrase="Dans chaque cuisine marocaine, il y a un sac rempli de sacs.", taille=100),
  dict(photo="courses.jpg", phrase="Personne ne sait quand il a commencé."),
  dict(photo="courses.jpg", phrase="Tu as le droit d'en prendre un. Pas deux.",
       cta="Tag celle qui a le sac des sacs chez elle."),
 ]),
 "02_petites-victoires": ("ambiance_b_m.wav", [
  dict(photo="tel.jpg", flou=10, phrase="Tu as répondu au message que tu repoussais depuis une semaine. Ça compte.", taille=96),
  dict(photo="tel.jpg", flou=10, phrase="Tu as dit non une fois. Sans t'excuser trois fois."),
  dict(photo="tel.jpg", flou=10, phrase=f"Personne n'a applaudi. Alors{N}on le fait ici.",
       cta="Envoie-le à celle qui ne s'applaudit jamais."),
 ]),
 "03_juste-les-pointes": ("ambiance_c_m.wav", [
  dict(photo="ciseaux.jpg", zones_flou=[(820, 150, 1080, 900, 24), (0, 0, 260, 520, 24)], phrase="« Juste les pointes, s'il te plaît. »", taille=108),
  dict(photo="ciseaux.jpg", zones_flou=[(820, 150, 1080, 900, 24), (0, 0, 260, 520, 24)], phrase=f"Elle a entendu : dix{N}centimètres."),
  dict(photo="ciseaux.jpg", zones_flou=[(820, 150, 1080, 900, 24), (0, 0, 260, 520, 24)], phrase=f"Et toi, tu dis : « C'est très{N}joli, merci. »",
       cta="Tag celle qui dit merci quand même."),
 ]),
 "04_pause-allaitement": ("ambiance_a_m.wav", [
  dict(photo="the_atlas.jpg", fy=.55, phrase=f"1{N}heure payée par jour pour allaiter.", sous="C'est le Code du travail marocain.", taille=108),
  dict(photo="the_atlas.jpg", fy=.55, phrase="Une demi-heure le matin, une demi-heure l'après-midi."),
  dict(photo="the_atlas.jpg", fy=.55, phrase=f"Pendant 12{N}mois après ta reprise. Payée comme du temps de travail.",
       cta="Envoie-le à ta collègue qui revient de congé."),
 ]),
 "05_salon-des-invites": ("ambiance_b_m.wav", [
  dict(photo="salon_riad.jpg", phrase="Le salon des invités. Toi, tu n'avais pas le droit de t'y asseoir.", taille=96),
  dict(photo="salon_riad.jpg", phrase="Les coussins sont alignés au millimètre."),
  dict(photo="salon_riad.jpg", phrase="Il ouvrait deux fois par an. Et ce jour-là, c'était toi qui faisais le ménage.",
       cta="Tag ta sœur, elle connaît le règlement."),
 ]),
 "06_a-20-ans": ("ambiance_c_m.wav", [
  dict(photo="fenetre.jpg", phrase=f"À 20{N}ans, je pensais que tout le monde me regardait.", taille=100),
  dict(photo="fenetre.jpg", phrase=f"À 30{N}ans, j'ai compris : chacun est occupé à se regarder soi-même."),
  dict(photo="fenetre.jpg", phrase="Alors mets le caftan. Danse au mariage. Ris fort.",
       cta="Envoie-le à ta petite sœur."),
 ]),
 "07_kouli": ("ambiance_a_m.wav", [
  dict(photo="gateaux.jpg", phrase=f"« Kouli a{N}benti, kouli{N}! »", taille=116),
  dict(photo="gateaux.jpg", phrase=f"« Safi khalti, chb3t, lah{N}ykhallik. »", taille=104),
  dict(photo="gateaux.jpg", phrase=f"« Ghir had lbriwa. »", taille=112),
  dict(photo="gateaux.jpg", phrase=f"« Ana daba ghadi nterte9. »", taille=108,
       cta="Siftiha l sa7btek lli dima katgoul chb3t."),
 ]),
 "08_mariage-horaires": ("ambiance_b_m.wav", [
  dict(photo="plafond.jpg", zones_flou=[(0, 0, 1080, 760, 22)], phrase=f"Invitation au mariage : 20{N}h. Le{N}dîner : 2{N}h du matin.", taille=100),
  dict(photo="plafond.jpg", zones_flou=[(0, 0, 1080, 760, 22)], phrase="Entre les deux, la mariée change de tenue. Encore. Et encore."),
  dict(photo="plafond.jpg", zones_flou=[(0, 0, 1080, 760, 22)], phrase=f"Tu rentres à 5{N}h, les pieds en feu : « C'était trop beau. »",
       cta="Tag ta copine de mariage."),
 ]),
 "09_famille-et-silence": ("ambiance_c_m.wav", [
  dict(photo="rideau.jpg", phrase="Tu peux aimer ta famille et avoir besoin de silence.", taille=104),
  dict(photo="rideau.jpg", phrase="Les deux sont vrais en même temps.", taille=104,
       cta="Envoie-le à celle qui s'enferme dans la salle de bains pour souffler."),
 ]),
 "10_la-boite": ("ambiance_a_m.wav", [
  dict(photo="boites.jpg", phrase=f"Ta mère, en te donnant un plat : « W{N}reddi{N}liya{N}l3elba. »", sous="Et tu me ramènes la boîte.", taille=96),
  dict(photo="boites.jpg", phrase="Trois mois plus tard, la boîte est toujours chez toi."),
  dict(photo="boites.jpg", phrase="Elle n'a pas oublié. Elle n'oublie jamais.",
       cta="Tag celle qui a une boîte de sa mère dans le placard."),
 ]),
 "11_bchhal": ("ambiance_b_m.wav", [
  dict(photo="pieces.jpg", flou=9, phrase=f"Ta mère, devant ton nouveau sac : « Bchhal{N}? »", sous="Combien ?", taille=100),
  dict(photo="pieces.jpg", flou=9, phrase="Toi : la moitié du prix. Par sécurité."),
  dict(photo="pieces.jpg", flou=9, phrase=f"Elle : « Chfrouk{N}! »", sous="Ils t'ont volée.", taille=116,
       cta="Envoie-le à celle qui ment aussi sur les prix."),
 ]),
 "12_fin-ghadia": ("ambiance_c_m.wav", [
  dict(photo="salon.jpg", phrase=f"« Fin ghadia{N}? »", sous="Mama mlli katchoufek katlbsi sbbatek.", taille=120),
  dict(photo="salon.jpg", phrase=f"« M3a men{N}? »", taille=120),
  dict(photo="salon.jpg", phrase=f"« Fo9ach ghadi terj3i{N}? »", taille=110),
  dict(photo="salon.jpg", phrase=f"« W 3ayti liya mnin tewsli. »", taille=104,
       cta="Siftiha l khtek."),
 ]),
 "13_ma-mere": ("ambiance_a_m.wav", [
  dict(photo="menthe.jpg", phrase=f"Ma mère : « Ma{N}kayn{N}lli{N}bhalek. »", sous="Personne n'est comme toi.", taille=100, fy=.45),
  dict(photo="menthe.jpg", phrase=f"Ma mère, le lendemain : « Chouf{N}bent{N}khaltek. »", sous="Regarde ta cousine.", taille=96, fy=.45,
       cta="Envoie-le à ta cousine. Elle aussi, elle l'entend."),
 ]),
 "14_klti": ("ambiance_b_m.wav", [
  dict(photo="the_biscuits.jpg", phrase=f"Ta mère au téléphone, avant même bonjour : « Klti{N}? »", sous="Tu as mangé ?", taille=100),
  dict(photo="the_biscuits.jpg", phrase=f"Toi : « Iyeh, mama. »", taille=112),
  dict(photo="the_biscuits.jpg", phrase=f"Elle : « Chnou klti{N}? »", sous="Tu as mangé quoi ?", taille=112),
  dict(photo="the_biscuits.jpg", phrase="Tu as un travail, un loyer, des factures. Elle vérifie encore.",
       cta="Envoie-le à ta mère. Elle va rire."),
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
        sh.save(SCR + f"r6_{slug}.png")
        print(slug, len(ecr), tot, flush=True)
