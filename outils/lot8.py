"""Atlasienne - lot 8 (14/11 au 21/11/2026). Ordre = ordre de publication, du moins fort au plus fort.
Changements : photos toutes neuves (les Reels à 0 vue réutilisaient des photos déjà publiées), plus de scènes
« toi seule » sur le modèle café seule et mer seule (50 % de rétention), cta « Envoie-le à » une personne précise."""
import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
from phrase2 import reel_anime
from PIL import Image

R = "/home/claude/media/reels_v8/"
SCR = "/tmp/claude-0/-home-claude-media/189d302b-0741-5121-bd5e-b458e2aecc26/scratchpad/"
N = "\u00a0"

REELS = {
 "01_photocopie": ("ambiance_a_m.wav", [
  dict(photo="papiers.jpg", phrase=f"Tu arrives avec tous tes papiers. Au guichet{N}: « Khassek copie. »", sous="Il te manque une photocopie.", taille=96),
  dict(photo="papiers.jpg", phrase=f"Tu cours à la librairie d'en{N}face. Fermée pour le déjeuner."),
  dict(photo="papiers.jpg", phrase="Tu reviens avec ta copie. Maintenant, il manque une photo d'identité.",
       cta="Envoie-le à celle qui a toujours une photocopie de trop dans son sac."),
 ]),
 "02_hammam": ("ambiance_b_m.wav", [
  dict(photo="hammam2.jpg", phrase=f"Mama f lhammam{N}: «{N}Ghir nkemmel lik dahrek. »", taille=104),
  dict(photo="hammam2.jpg", phrase="Arba3in dqiqa men b3d, mazal katkessel.", taille=104),
  dict(photo="hammam2.jpg", phrase=f"W f lekher{N}: « Chofti chhal dyal lwsekh{N}? »", taille=104,
       cta="Siftiha l khtek. Hiya 3arfa."),
 ]),
 "03_fleurs": ("ambiance_c_m.wav", [
  dict(photo="fleurs2.jpg", fy=.45, phrase="Acheter des fleurs pour toi. Sans occasion, sans personne à qui les offrir.", taille=96),
  dict(photo="fleurs2.jpg", fy=.45, phrase="Ce n'est pas du gaspillage."),
  dict(photo="fleurs2.jpg", fy=.45, phrase="C'est une façon de te dire merci.",
       cta="Envoie-le à celle qui ne s'achète jamais rien."),
 ]),
 "04_conge-mariage": ("ambiance_a_m.wav", [
  dict(photo="henne.jpg", phrase=f"4{N}jours de congé pour ton mariage. En plus de tes vacances.", sous="Code du travail marocain, secteur privé.", taille=100),
  dict(photo="henne.jpg", phrase="Si tu es payée au mois, ces 4 jours sont payés en entier."),
  dict(photo="henne.jpg", phrase="L'acte de mariage sert de justificatif. Prends ces jours autour du mariage.",
       cta="Envoie-le à ta copine qui se marie bientôt."),
 ]),
 "05_voisin-mariage": ("ambiance_b_m.wav", [
  dict(photo="cour_nuit.jpg", phrase="Le voisin du dessous se marie. Tu ne le connais même pas.", taille=98),
  dict(photo="cour_nuit.jpg", phrase=f"À 3{N}h du matin, tu connais toutes les chansons."),
  dict(photo="cour_nuit.jpg", phrase=f"À 4{N}h, tu fais les youyous depuis ton lit.",
       cta="Envoie-le à ta voisine. Elle n'a pas dormi non plus."),
 ]),
 "06_gateaux": ("ambiance_c_m.wav", [
  dict(photo="gateaux2.jpg", phrase=f"Fin du mariage. La tante de la mariée{N}: «{N}Ghir{N}chwiya dyal lhelwa. »", sous="Juste quelques gâteaux.", taille=94),
  dict(photo="gateaux2.jpg", phrase="Elle remplit une boîte. Puis une deuxième."),
  dict(photo="gateaux2.jpg", phrase="Tu rentres en taxi avec deux kilos de gâteaux sur les genoux.",
       cta="Envoie-le à celle qui repart toujours avec la boîte."),
 ]),
 "07_train-seule": ("ambiance_a_m.wav", [
  dict(photo="train.jpg", phrase="Prendre le train seule pour un week-end. Juste toi et la fenêtre.", taille=98),
  dict(photo="train.jpg", phrase="Ce n'est pas une fuite."),
  dict(photo="train.jpg", phrase="C'est une façon de revenir vers toi.",
       cta="Envoie-le à celle qui attend toujours une copine pour partir."),
 ]),
 "08_wselti": ("ambiance_b_m.wav", [
  dict(photo="route.jpg", phrase=f"Mama{N}: « Wselti{N}? »", taille=120),
  dict(photo="route.jpg", phrase=f"Ana{N}: « Mazal, ghir khrejt men ddar. »", taille=104),
  dict(photo="route.jpg", phrase=f"3echr dqayeq men b3d{N}: « Wselti{N}? »", taille=104,
       cta="Siftiha l mok. Ghadi tdhek."),
 ]),
 "09_sbah-lkhir": ("ambiance_c_m.wav", [
  dict(photo="matin.jpg", phrase=f"6{N}h du matin. Ta tante dans le groupe famille{N}: une rose et « Sbah lkhir ».", taille=92),
  dict(photo="matin.jpg", phrase="L'image brille. Il y a de la musique. Et un chaton."),
  dict(photo="matin.jpg", phrase=f"Tout le groupe répond « Sbah nnour ». Sauf{N}toi. Tu dors.",
       cta="Envoie-le à ta cousine du groupe famille."),
 ]),
 "10_coiffeuse": ("ambiance_a_m.wav", [
  dict(photo="coiffeuse.jpg", phrase=f"Rendez-vous chez la coiffeuse à 14{N}h. Le mariage est à 20{N}h.", taille=96),
  dict(photo="coiffeuse.jpg", phrase=f"À 18{N}h, tu es encore sur la chaise. Les cheveux à moitié lissés."),
  dict(photo="coiffeuse.jpg", phrase=f"Tu arrives au mariage à 22{N}h. Pile à l'heure, comme tout le monde.",
       cta="Envoie-le à celle qui se prépare avec toi."),
 ]),
 "11_fin-kenti": ("ambiance_b_m.wav", [
  dict(photo="porte_nuit.jpg", phrase=f"Tu rentres à 21{N}h{N}05. Ta mère{N}: « Fin kenti{N}? »", sous="Tu étais où ?", taille=98),
  dict(photo="porte_nuit.jpg", phrase=f"Tu avais dit 21{N}h. Elle a déjà appelé ta sœur, ta cousine et ta copine."),
  dict(photo="porte_nuit.jpg", phrase=f"Le lendemain{N}: « Ma n3estch hta dkhelti. »", sous="Je n'ai pas dormi avant ton retour.",
       cta="Envoie-le à ta mère. Elle va dire que c'est normal."),
 ]),
 "12_bl3ine": ("ambiance_c_m.wav", [
  dict(photo="epices.jpg", fy=.6, phrase=f"Tu demandes la recette à ta mère. «{N}Chhal{N}dyal lkamoun{N}? »", sous="Combien de cumin ?", taille=96),
  dict(photo="epices.jpg", fy=.6, phrase=f"Elle{N}: « Bl3in. »", sous="À l'œil.", taille=116),
  dict(photo="epices.jpg", fy=.6, phrase="Tu fais tout « bl3in ». Ton tajine n'a pas du tout le même goût.",
       cta="Envoie-le à ta mère. Elle va dire que c'est facile."),
 ]),
 "13_cinema-seule": ("ambiance_a_m.wav", [
  dict(photo="cinema.jpg", phrase=f"Aller seule au cinéma un mardi{N}soir. Le pop-corn rien que pour toi.", taille=98),
  dict(photo="cinema.jpg", phrase="Ce n'est pas bizarre."),
  dict(photo="cinema.jpg", phrase="C'est ton film, ton fauteuil, ton moment.",
       cta="Envoie-le à celle qui attend toujours quelqu'un pour sortir."),
 ]),
 "14_moul-lhanout": ("ambiance_b_m.wav", [
  dict(photo="hanout.jpg", flou=10, phrase=f"Tu descends juste chez moul{N}lhanout. En pyjama, une djellaba par-dessus.", taille=94),
  dict(photo="hanout.jpg", flou=10, phrase="Tu croises ta voisine, ton ancienne prof et la moitié du quartier."),
  dict(photo="hanout.jpg", flou=10, phrase="Le seul jour où tu ne t'es pas coiffée.",
       cta="Envoie-le à celle qui fait pareil le dimanche matin."),
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
        sh.save(SCR + f"r8_{slug}.png")
        print(slug, len(ecr), tot, flush=True)
