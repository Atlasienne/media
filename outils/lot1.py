"""Atlasienne - lot 1 de lancement (9 posts)."""
import os, sys, json
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
from atl2 import *
from PIL import Image

BASE = "/home/claude/media/posts/lot01/"
DATE = "Point arrêté au 18 octobre 2026"
AV = avatar("/tmp/_av.png")


def vis_picto(kind):
    def f(d, c):
        tone = mix(c["bg"], c["fg"], 0.12) if c["bg"] != PAPIER else mix(PAPIER, CEDRE, 0.07)
        d.ellipse([W - M - 430, 190, W - M, 620], fill=tone)
        picto(d, kind, W - M - 215, 405, 300, c["acc"], t=16)
    return f


def build(slug, fam, label, cover, slides, sources, date=DATE):
    out = BASE + slug + "/"
    os.makedirs(out, exist_ok=True)
    n = len(slides) + 2
    files = []
    p = out + "01.jpg"
    kw = dict(cover)
    kw["titre"] = fr(kw["titre"])
    kw["sous_titre"] = fr(kw.get("sous_titre"))
    couverture(p.replace(".jpg", ".png"), fam, label, pages=f"1/{n}", **kw)
    files.append(p)
    for i, s in enumerate(slides, start=2):
        p = out + f"{i:02d}.jpg"
        if s[0] == "i":
            _, ch, t, tx = s
            interieure(p.replace(".jpg", ".png"), fam, label, fr(ch), fr(t), fr(tx), f"{i}/{n}")
        else:
            _, t, items, note = s[:4]
            taille = s[4] if len(s) > 4 else 42
            liste(p.replace(".jpg", ".png"), fam, label, t, items, f"{i}/{n}", note=note, taille=taille)
        files.append(p)
    p = out + f"{n:02d}.jpg"
    fin(p.replace(".jpg", ".png"), [fr(x) for x in sources] if sources else None, date, AV)
    files.append(p)
    for f in files:
        Image.open(f.replace(".jpg", ".png")).convert("RGB").save(f, quality=92)
        os.remove(f.replace(".jpg", ".png"))
    return files


POSTS = {}

# 1. Touria Chaoui (publié en premier, bas à droite de la grille)
POSTS["01_touria-chaoui"] = build("01_touria-chaoui", "Société", "Portrait",
    dict(titre="Touria Chaoui, première aviatrice marocaine", sous_titre="Elle avait 15 ans. Son histoire en 5 repères.", visuel="paysage"),
    [("i", "1936", "Naissance à Fès", "Touria Chaoui naît le 14 décembre 1936, en plein protectorat français."),
     ("i", "1951", "Son brevet de pilote, à 15 ans", "Elle apprend à piloter à l'aérodrome de Tit Mellil, près de Casablanca, une école alors réservée aux Européens."),
     ("i", "1re", "Marocaine aux commandes d'un avion", "On la présente souvent comme la première du monde arabe. L'Égyptienne Lotfia El Nadi volait pourtant dès 1933."),
     ("i", "1956", "Assassinée à 19 ans", "Le 1er mars 1956, elle est tuée par balle au volant de sa voiture, à Casablanca, à la veille de l'indépendance. Le meurtre n'a jamais été élucidé."),
     ("i", "2026", "Héroïne d'une série d'animation", "Pendant le Ramadan 2026, la série « Maghariba Fi Samae », diffusée sur 2M, fait d'elle son fil rouge. Son frère lui a aussi consacré un livre, « Ma sœur Touria »."),
     ],
    ["Le360, 20 février 2026", "Le Courrier de l'Atlas, 13 juillet 2026", "Yabiladi, 8 mars 2018", "Salah Eddine Chaoui, « Ma sœur Touria », L'Harmattan"])

# 2. Emploi des femmes, HCP
POSTS["02_emploi-femmes-hcp"] = build("02_emploi-femmes-hcp", "Argent", "Carrière",
    dict(titre="des femmes sont actives au Maroc, contre 66,5 % des hommes", sous_titre="Derniers chiffres du HCP, 2e trimestre 2026", chiffre="18,1 %"),
    [("i", "3 août", "Le HCP publie ses chiffres du 2e trimestre", "C'est la deuxième note tirée de sa nouvelle enquête sur la main-d'œuvre, après celle du 1er trimestre en mai. Désormais, seul le travail rémunéré compte comme un emploi."),
     ("l", "Ce que disent les chiffres", ["18,1 % des femmes sont actives, contre 66,5 % des hommes.", "Le chômage touche 14,8 % des femmes, contre 8,1 % des hommes.", "Les femmes ne pèsent que 21,5 % de la main-d'œuvre."], "Taux d'activité : part des personnes qui travaillent ou cherchent un emploi."),
     ("i", "139e", "Le rang du Maroc sur 145 pays", "Dans le classement 2026 du Forum économique mondial sur l'égalité femmes-hommes, publié en septembre. Le pays est 143e pour la participation des femmes au marché du travail."),
     ("l", "Attention aux comparaisons", ["La méthode du HCP a changé en 2026.", "Ces chiffres ne se comparent pas directement à ceux de 2025.", "Le HCP a recalculé les années 2017 à 2025 avec la nouvelle méthode : ce sont les seuls chiffres comparables."], None),
     ("i", "Nov.", "La prochaine note est attendue début novembre", "D'habitude, le HCP publie les chiffres du 3e trimestre début novembre. On te les décrypte dès leur sortie."),
     ],
    ["HCP, note du 2e trimestre 2026, 3 août 2026", "Hespress, 3 août 2026", "Le360, 18 septembre 2026", "Le Matin, 4 octobre 2026"])

# 3. Dire non au travail
POSTS["03_dire-non"] = build("03_dire-non", "Bien-être", "Confiance",
    dict(titre="Dire non au travail sans se griller", sous_titre="4 phrases à garder sous la main"),
    [("i", "1", "Gagner du temps", "« Je regarde mon planning et je te réponds avant 17 h. » Tu évites le oui réflexe et tu réponds à froid."),
     ("i", "2", "Dire non à la tâche, pas à la personne", "« Je ne peux pas le prendre cette semaine, mais je peux t'aider à trouver quelqu'un. »"),
     ("i", "3", "Faire arbitrer", "« Si je prends ce dossier, lequel je mets en pause ? » La décision revient à ton manager, pas à ta soirée."),
     ("i", "4", "Proposer une version réduite", "« Je ne peux pas faire le rapport complet, mais je t'envoie les chiffres clés jeudi. »"),
     ("l", "Ce qui affaiblit ton non", ["Te justifier pendant cinq minutes.", "Dire « je vais essayer » quand c'est non.", "Répondre dans l'urgence, sous pression.", "T'excuser trois fois."], None),
     ],
    None, date="Fiche pratique de la rédaction")

# 4. SRM eau et électricité
POSTS["04_srm-factures"] = build("04_srm-factures", "Vie", "Maison",
    dict(titre="Lydec, Redal : qui t'envoie ta facture ?", sous_titre="Eau et électricité, ce qui change et ce qui ne change pas", visuel=vis_picto("ampoule")),
    [("i", "12", "régions, une société par région", "Depuis octobre 2024, des sociétés régionales multiservices (SRM) reprennent la distribution de l'eau et de l'électricité, région par région."),
     ("l", "Les dates de démarrage", ["Casablanca-Settat : 1er octobre 2024", "Souss-Massa : 15 octobre 2024", "Marrakech-Safi : 1er novembre 2024", "Rabat-Salé-Kénitra : 1er juin 2025", "Tanger-Tétouan-Al Hoceima : 1er septembre 2025"], "Les autres régions ont suivi jusqu'à fin 2025. À Rabat et dans une partie de Tanger-Tétouan, l'ancien gestionnaire garde son périmètre historique."),
     ("i", "0", "hausse de tarif liée aux SRM", "Les SRM appliquent les mêmes grilles que les anciens distributeurs, a assuré le ministre de l'Intérieur devant le Parlement le 2 juin 2025."),
     ("i", "150 kWh", "le seuil à surveiller chaque mois", "Jusqu'à 150 kWh, tu restes dans les tranches sociales, les moins chères, et chaque tranche est payée à son prix. Au-delà, selon le ministère de l'Énergie, tout le mois passe au prix de la tranche atteinte."),
     ("l", "Si ta facture te paraît trop élevée", ["Compare l'index de ton compteur avec celui de la facture.", "Une facture estimée est normalement régularisée au relevé suivant.", "Dépose une réclamation et demande une vérification du compteur.", "Demande un paiement échelonné si besoin."], "Dans le Grand Casablanca : application 7/24 de la SRM."),
     ],
    ["Hespress, 2 juin 2025", "Médias24, 5 juin 2025", "Le Matin, 3 septembre 2025", "TelQuel, 24 février 2026", "FNH, 1er octobre 2026"])

# 5. Femmes au gouvernement
POSTS["05_femmes-gouvernement"] = build("05_femmes-gouvernement", "Société", "Actu",
    dict(titre="femmes sur 32 membres du nouveau gouvernement", sous_titre="Nommé par le Roi le 16 octobre 2026", chiffre="7"),
    [("i", "16 oct.", "Le Roi nomme le gouvernement", "32 membres au total : la cheffe du gouvernement, 19 ministres, 11 ministres délégués et le secrétaire général du gouvernement."),
     ("l", "Les 7 femmes du gouvernement", ["Fatima Ezzahra El Mansouri, cheffe du gouvernement", "Charafat Afailal, Énergie, Mines et Développement durable", "Najwa Koukouss, Famille, Développement social et Égalité", "Kouloub Faitah, Relations avec le Parlement et la société civile", "Madiha Khayr, Formation professionnelle", "Fatima Saadi, Habitat et Politique de la ville", "Aïcha Guellaa, Réforme de l'administration"], "Seules Charafat Afailal et Najwa Koukouss dirigent un ministère. Les quatre dernières sont ministres déléguées.", 34),
     ("i", "21,9 %", "du gouvernement est féminin", "Moins qu'en octobre 2021, où les 7 femmes de l'équipe Akhannouch en représentaient environ 28 %. Le nombre, lui, reste le même."),
     ("i", "0", "femme à un ministère régalien", "Intérieur, Affaires étrangères, Justice, Habous : tous sont dirigés par des hommes. Les Finances, confiées à Nadia Fettah en 2021, repassent aussi à un homme."),
     ("i", "1re", "femme cheffe du gouvernement", "Nommée le 29 septembre 2026, Fatima Ezzahra El Mansouri est la première femme à ce poste dans l'histoire du Maroc."),
     ],
    ["Maroc.ma, 16 octobre 2026", "Médias24, 16 octobre 2026", "Hespress, 16 octobre 2026", "TelQuel, 8 octobre 2021"])

# 6. Caftan UNESCO
POSTS["06_caftan-unesco"] = build("06_caftan-unesco", "Style", "Patrimoine",
    dict(titre="Le caftan marocain, patrimoine de l'humanité", sous_titre="Ce que l'UNESCO a reconnu, et ce que tu ne savais peut-être pas", visuel=vis_picto("cintre")),
    [("i", "10 déc.", "Inscrit à l'UNESCO en 2025", "« Le caftan marocain : art, traditions et savoir-faire » rejoint la Liste représentative du patrimoine culturel immatériel, lors de la 20e session du Comité, à New Delhi."),
     ("l", "Caftan ou takchita ?", ["Le caftan se porte seul, en une seule pièce.", "La takchita en superpose au moins deux : un caftan de dessous et une pièce légère par-dessus.", "Il existe aussi un caftan masculin, plus sobre."], None),
     ("l", "Les savoir-faire derrière un caftan", ["La sfifa, le galon tressé qui borde les coutures.", "Les aakad, les petits boutons faits main.", "Les âayoun, les boutonnières.", "Le fessal coupe, les ttrazate brodent, le zeradkhi tisse le brocart."], None),
     ("l", "Ce que l'inscription change", ["Ce n'est ni une marque déposée ni un titre de propriété.", "C'est la reconnaissance internationale d'un savoir-faire vivant.", "Dans son dossier, le Maroc s'engage à le transmettre : coopératives, formations, musées."], None),
     ("i", "2026", "Le caftan défile sous le signe de l'Atlas", "En mai 2026, la Caftan Week de Marrakech avait pour thème « Souffle de l'Atlas ». 12 stylistes ont défilé pour sa 26e édition."),
     ],
    ["UNESCO, 20e session du Comité, décembre 2025", "MAP, 10 décembre 2025", "Médias24, 8 décembre 2022", "Le360, 10 avril 2025", "Hespress, 10 mai 2026"])

# 7. SMIG 2026
POSTS["07_smig-2026"] = build("07_smig-2026", "Argent", "Salaire",
    dict(titre="DH brut par mois : le SMIG en 2026", sous_titre="Ce que tu touches vraiment, et ce que dit la loi", chiffre="3 422"),
    [("i", "17,92 DH", "de l'heure depuis le 1er janvier 2026", "Soit 3 422,72 DH brut pour 191 heures par mois. C'est la deuxième hausse de 5 % prévue par l'accord social d'avril 2024."),
     ("i", "3 190 DH", "net par mois, environ", "Après les cotisations CNSS et AMO (environ 6,7 %), un SMIG à temps plein donne autour de 3 190 DH net. À ce niveau, pas d'impôt sur le revenu."),
     ("i", "97,44 DH", "par jour pour le SMAG", "Le salaire minimum agricole a augmenté de 5 % le 1er avril 2026. Sur 26 jours, cela fait 2 533,44 DH brut par mois."),
     ("l", "Ce que dit la loi", ["À travail de valeur égale, salaire égal entre femmes et hommes (article 346 du Code du travail).", "Être payée sous le SMIG à temps plein est interdit : l'employeur doit te verser la différence.", "Tu peux saisir l'inspection du travail de ta région, puis le tribunal si besoin."], None),
     ("i", "18 oct.", "Aucune nouvelle hausse annoncée", "À ce jour, le gouvernement El Mansouri n'a rien annoncé sur le salaire minimum. Prochain rendez-vous : la présentation de son programme devant le Parlement."),
     ],
    ["Décret n° 2.25.983, adopté le 18 décembre 2025", "Hespress, 18 décembre 2025", "EcoActu, 22 décembre 2025", "Hespress, 17 avril 2026", "Taux CNSS 4,48 % et AMO 2,26 %"])

# 8. Octobre rose
POSTS["08_octobre-rose"] = build("08_octobre-rose", "Bien-être", "Santé",
    dict(titre="Octobre rose : où te faire dépister ce mois-ci", sous_titre="Campagne nationale du 1er au 31 octobre 2026", visuel=vis_picto("ruban")),
    [("i", "31 oct.", "La campagne nationale dure jusqu'au 31 octobre", "Le ministère de la Santé mène sa campagne de sensibilisation et de détection précoce des cancers du sein et du col de l'utérus."),
     ("i", "1er", "cancer chez les femmes", "Le cancer du sein représente 39,1 % des cancers féminins, selon le registre des cancers de Casablanca-Settat (2018-2021)."),
     ("l", "Où t'adresser", ["Ton centre de santé de proximité, pour un premier examen.", "Les centres de référence de santé reproductive, 57 dans le pays.", "Les unités mobiles de mammographie, 27, qui se déplacent dans les régions."], "Derniers chiffres officiels disponibles, campagne 2025."),
     ("i", "11 ans", "l'âge de la vaccination HPV des filles", "La campagne rappelle aussi ce vaccin contre le papillomavirus, en cause dans le cancer du col de l'utérus."),
     ("l", "Le bon réflexe", ["Parles-en à un médecin ou à une sage-femme, même sans symptôme.", "Demande quel examen est prévu pour ton âge.", "Le message central de la campagne : la détection précoce."], None),
     ],
    ["Hespress, 1er octobre 2026", "SantéMag, 1er octobre 2026", "MAP, 7 octobre 2025", "FNH, 13 octobre 2026"])

# 9. Moudawana (corrigée après contre-étude)
POSTS["09_moudawana"] = build("09_moudawana", "Société", "Actu",
    dict(titre="Moudawana : la réforme, c'est pour quand ?", sous_titre="Nouveau gouvernement, même ministre de la Justice. Point au 18 octobre 2026."),
    [("i", "16 oct.", "Abdellatif Ouahbi reste ministre de la Justice", "Le 16 octobre 2026, le Roi reçoit le gouvernement de Fatima Ezzahra El Mansouri. Le dossier du Code de la famille reste entre les mains du même ministre, en poste depuis 2021."),
     ("i", "12 août", "La réforme glisse à la nouvelle législature", "Le 12 août 2026, le ministre déclare : « Il reste encore quelques derniers ajustements ». Il dit espérer un examen du texte au cours de la première année de la nouvelle législature. L'objectif annoncé au départ était fin 2025."),
     ("i", "0", "projet de loi déposé au Parlement à ce jour", "Le texte n'a été ni voté ni publié au Bulletin officiel. La seule loi applicable reste le Code de la famille de 2004. Méfie-toi des posts qui annoncent « ce qui change en 2026 »."),
     ("l", "Ce qui est proposé sur la garde des enfants", ["La garde partagée entre les deux parents pendant le mariage, et après le divorce s'ils sont d'accord.", "La mère qui se remarie garde ses enfants.", "Le logement de l'enfant mieux protégé, chez le parent qui en a la garde.", "La mère associée à la tutelle légale, aujourd'hui confiée d'abord au père."], "Propositions présentées le 24 décembre 2024. Le texte final peut encore changer."),
     ("l", "Ce que dit la loi aujourd'hui", ["Après le divorce, la garde revient d'abord à la mère, puis au père, puis à la grand-mère maternelle (art. 171).", "Si la mère se remarie, elle peut perdre la garde d'un enfant de plus de 7 ans, sauf exceptions (art. 175).", "À 15 ans, l'enfant choisit chez quel parent il vit (art. 166).", "La tutelle légale revient d'abord au père, la mère seulement en son absence : école, banque, papiers (art. 231, 236 et 238)."], None, 38),
     ("l", "Ce qu'il faut surveiller", ["La présentation du programme du gouvernement El Mansouri devant le Parlement : la réforme y sera-t-elle prioritaire ?", "Une date de dépôt du projet de loi au Parlement.", "La publication de l'avis du Conseil supérieur des oulémas, réclamée notamment par Kif Mama Kif Baba."], "Dans un entretien diffusé le 14 octobre, Me Ghizlaine Mamouni (Kif Mama Kif Baba) dit espérer l'annonce du projet de loi dans les 100 premiers jours du gouvernement."),
     ],
    ["Morocco World News, 16 octobre 2026", "Le Matin, 16 octobre 2026", "Médias24, 12 août 2026", "Médias24, 24 décembre 2024", "Code de la famille, loi 70-03 (2004)"])

json.dump(POSTS, open(BASE + "index.json", "w"), indent=1, ensure_ascii=False)

# planche grille (ordre d'affichage Instagram : le dernier publié en haut à gauche)
order = list(POSTS.keys())[::-1]
gw, gh = 360, 480
g = Image.new("RGB", (3 * gw + 4, 3 * gh + 4), "white")
for k, slug in enumerate(order):
    im = Image.open(POSTS[slug][0])
    cw = int(1350 * 3 / 4)
    im = im.crop(((1080 - cw) // 2, 0, (1080 + cw) // 2, 1350)).resize((gw, gh))
    r, c = divmod(k, 3)
    g.paste(im, (c * (gw + 2), r * (gh + 2)))
g.save("/home/claude/atlasienne/lot1_grille.png")
print("ok")
