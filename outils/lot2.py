"""Atlasienne - lot 2 (6 posts), publication le 18/10/2026 au soir."""
exec(open("/home/claude/atlasienne/lot_common2.py").read())

POSTS = {}

# 1. Zineb El Adaoui (publié en premier : bas à droite de la nouvelle ligne)
POSTS["01_zineb-el-adaoui"] = build("01_zineb-el-adaoui", "Société", "Portrait",
    dict(titre="Zineb El Adaoui, la femme qui contrôle les comptes de l'État", sous_titre="Deux premières historiques en 5 repères", visuel="paysage"),
    [("i", "1960", "Naissance près d'El\u00a0Jadida", "Zineb El Adaoui naît en 1960 dans la province d'El Jadida."),
     ("i", "1984", "Juge à la Cour des comptes", "Elle y fait ses armes pendant près de 30 ans, au cœur du contrôle des finances publiques."),
     ("i", "2014", "Première femme wali du Maroc", "Le 20 janvier 2014, elle est nommée wali de la région Gharb-Chrarda-Béni Hssen et gouverneure de Kénitra. Elle devient ensuite wali de Souss-Massa en 2015."),
     ("i", "2021", "Première femme à la tête de la Cour des comptes", "En mars 2021, le Roi la nomme Première présidente de la Cour des comptes. Aucune femme n'avait occupé ce poste avant elle."),
     ("i", "629 MDH", "d'effet financier estimé", "Le 3 février 2026, elle présente au Parlement le bilan 2024-2025 des juridictions financières. Leurs observations ont eu un effet financier estimé à 629 millions de dirhams."),
     ],
    ["Jeune Afrique, 25 mars 2021", "TelQuel, 22 janvier 2014", "Le360, janvier 2014", "Le Matin, 4 février 2026", "Cour des comptes, 3 février 2026"])

# 2. Huile d'olive
POSTS["02_huile-olive"] = build("02_huile-olive", "Vie", "Cuisine",
    dict(titre="Huile d'olive : le prix a fondu cette année", sous_titre="Ce qu'on sait de la prochaine récolte, et comment bien la choisir. Point au 18 octobre 2026.", visuel=vis_picto("goutte")),
    [("i", "2 Mt", "d'olives récoltées en 2025-2026", "Plus de 2 millions de tonnes, plus du double de la campagne précédente. Les prix ont chuté après les records de 2024-2025, entre 90 et 120 DH le litre."),
     ("i", "40-50 DH", "le litre en janvier 2026 dans les régions productrices", "Contre environ 70 DH en moyenne début décembre 2025, selon les relevés de presse. Les prix varient beaucoup d'une région à l'autre."),
     ("i", "-40 %", "d'olives attendues en 2026-2027", "C'est la prévision de l'interprofession au niveau national, alors que le Nord annonce une bonne récolte. Les stocks devraient limiter les hausses."),
     ("l", "Reconnaître une bonne huile", ["Choisis « vierge extra » (acidité de 0,8 % au plus) ou « vierge ».", "Préfère une huile conditionnée au vrac, avec l'origine et l'autorisation ONSSA sur l'étiquette.", "L'huile lampante n'est pas comestible en l'état.", "Le test du frigo ne prouve rien : une huile coupée peut figer aussi."], None),
     ("l", "La conserver", ["À l'abri de la lumière, entre 13 et 25 °C, bien fermée.", "À consommer dans les 1 à 3 mois après ouverture.", "Loin de la cuisinière et des sources de chaleur."], "Conservation : Conseil oléicole international."),
     ],
    ["Médias24, 11 décembre 2025", "Le Matin, 1er décembre 2025", "Le360, 24 janvier 2026", "Le360, 29 août 2026", "Conseil oléicole international"])

# 3. Henné noir
POSTS["03_henne-noir"] = build("03_henne-noir", "Style", "Beauté",
    dict(titre="Henné noir : pourquoi il peut te laisser une allergie à\u00a0vie", sous_titre="Ce que disent les autorités sanitaires", visuel=vis_picto("alerte")),
    [("i", "PPD", "le colorant caché dans le henné noir", "La paraphénylènediamine est une teinture pour cheveux. Elle n'est pas autorisée dans les produits appliqués sur la peau, mais on la retrouve dans des hennés très noirs."),
     ("l", "Les risques", ["Rougeurs, démangeaisons, cloques, de quelques heures à deux semaines après.", "Une allergie qui peut rester à vie.", "Ensuite, des réactions possibles aux teintures pour cheveux, au caoutchouc, à certains vêtements."], "Selon l'ANSM et Santé Canada."),
     ("l", "Reconnaître un produit douteux", ["Une couleur très noire.", "Un noir qui apparaît en très peu de temps.", "Aucune étiquette ni liste d'ingrédients."], None),
     ("i", "Orange", "la vraie couleur du henné naturel", "Le henné pur colore la peau en orange, brun ou brun-rouge, et la pâte doit poser plusieurs heures pour foncer. Pas de noir instantané."),
     ("l", "Si tu as déjà réagi", ["Ne refais plus de henné noir.", "Signale cette réaction à ton coiffeur et à ton médecin avant toute coloration capillaire.", "Consulte un médecin ou un pharmacien en cas de réaction."], None),
     ],
    ["FDA, 15 octobre 2024", "ANSM, affiche de mise en garde", "Santé Canada, 2026", "Anses, VigilAnses, avril 2026", "Pan African Medical Journal, 18 mai 2018"])

# 4. Aide sociale directe
POSTS["04_aide-sociale-directe"] = build("04_aide-sociale-directe", "Argent", "Aides",
    dict(titre="par enfant : l'aide sociale directe en 2026", sous_titre="Une revalorisation prévue au budget 2027", chiffre="250 DH"),
    [("i", "17 oct.", "Une revalorisation au budget 2027", "Le premier Conseil des ministres depuis la nomination du gouvernement El Mansouri, présidé par le Roi, a adopté les orientations du projet de loi de finances 2027, dont la revalorisation de l'aide sociale directe. Aucun montant ni calendrier n'est encore donné."),
     ("l", "Les montants depuis fin novembre 2025", ["500 DH par mois au minimum par ménage.", "250 DH pour chacun des 3 premiers enfants, de moins de 6 ans ou scolarisés.", "175 DH par enfant non scolarisé.", "375 DH pour chacun des 3 premiers orphelins de père.", "100 DH de plus par enfant en situation de handicap."], "Prime de naissance : 2 000 DH pour le 1er enfant, 1 000 DH pour le 2e."),
     ("i", "3,92 M", "de ménages bénéficiaires", "Soit 12,56 millions de personnes fin 2025, dont environ 396 000 veuves. L'aide représente 18 % de leur revenu, selon une enquête de l'ANSS auprès des bénéficiaires."),
     ("l", "Pour en bénéficier", ["S'inscrire au Registre national de la population, puis au Registre social unifié (RSU).", "Avoir un indice socio-économique sous le seuil fixé par décret.", "Déposer la demande sur asd.ma."], None),
     ("i", "2026", "Un emploi ne coupe plus l'aide d'un coup", "Avec la loi 41-26, appliquée depuis son décret au BO du 30 juillet 2026, un ménage qui perd l'aide grâce à un emploi déclaré à la CNSS reçoit une allocation du même montant, pendant 12 mois au plus. S'il perd cet emploi, il retrouve l'aide sans attendre 12 mois."),
     ],
    ["Médias24, 17 octobre 2026", "Maroc.ma, barème 2025", "Médias24, 9 juin 2026", "Médias24, 24 juillet 2026", "TelQuel, 17 août 2026"])

# 5. Activité physique
POSTS["05_activite-physique"] = build("05_activite-physique", "Bien-être", "Sport",
    dict(titre="d'activité par semaine : la recommandation de l'OMS", sous_titre="Et pourquoi les femmes bougent moins", chiffre="150 min"),
    [("i", "26 %", "des Marocaines adultes ne bougent pas assez", "Contre 16,1 % des hommes, selon l'enquête nationale STEPS 2017-2018 du ministère de la Santé, la dernière disponible."),
     ("l", "Ce que recommande l'OMS", ["150 à 300 minutes d'activité modérée par semaine, ou 75 à 150 minutes d'activité soutenue.", "Du renforcement musculaire au moins 2 jours par semaine.", "Toute activité compte, même par petites séquences."], None),
     ("l", "Y arriver sans salle de sport", ["30 minutes de marche rapide, 5 jours par semaine.", "Les escaliers plutôt que l'ascenseur.", "Danser, jardiner, faire le ménage à bon rythme.", "Des exercices au poids du corps, 2 fois par semaine."], None),
     ("i", "20 à 30 %", "de risque de décès en plus quand on bouge trop peu", "Selon l'OMS, l'activité physique est associée à moins de maladies cardiovasculaires, de diabète de type 2 et de certains cancers, et à un meilleur sommeil."),
     ("i", "4e", "place des Lionnes à la CAN 2026", "Organisée au Maroc du 25 juillet au 16 août 2026, la compétition a vu l'équipe nationale atteindre les demi-finales. Le Cameroun l'a remportée."),
     ],
    ["OMS, aide-mémoire, 26 juin 2024", "OMS Europe, 17 juillet 2025", "EMHJ, 2025 (enquête STEPS)", "CDC, Preventing Chronic Disease, 14 mai 2026", "CAF, 13 août 2026"])

# 6. Congé maternité et paternité (publié en dernier : haut à gauche)
POSTS["06_conge-maternite"] = build("06_conge-maternite", "Société", "Droits",
    dict(titre="semaines de congé maternité. Et pour les pères ?", sous_titre="Ce que dit la loi en 2026, dans le privé et le public", chiffre="14"),
    [("i", "100 %", "du salaire, versé par la CNSS", "Dans le privé, les 14 semaines sont indemnisées à 100 % du salaire journalier moyen, dans la limite d'un plafond. Condition : 54 jours de cotisation dans les 10 mois avant l'arrêt."),
     ("l", "Tes droits au travail", ["Pas de travail pendant les 7 semaines qui suivent l'accouchement.", "Protection contre le licenciement pendant la grossesse et les 14 semaines après, sauf faute grave.", "1 heure d'allaitement payée par jour pendant 12 mois.", "Un congé non payé jusqu'à 1 an possible, avec l'accord de l'employeur."], "Code du travail, articles 152 à 161."),
     ("i", "3 jours", "de congé paternité dans le privé", "C'est toujours la règle de l'article 269 du Code du travail, à prendre dans le mois qui suit la naissance."),
     ("i", "15 jours", "pour les pères fonctionnaires", "Depuis septembre 2022, la loi 30.22 accorde 15 jours aux pères de la fonction publique. Le congé maternité y est aussi de 14 semaines à plein salaire."),
     ("i", "Juin 2026", "Une proposition de loi pour 20 semaines", "Déposée à la Chambre des représentants, elle propose 20 semaines de congé maternité, et 22 semaines à partir du 3e enfant. Elle n'a pas été votée à ce jour."),
     ],
    ["Femmes du Maroc, 9 octobre 2026", "Code du travail, articles 152 à 161 et 269", "LeSiteinfo, 16 juin 2026", "LeSiteinfo, 7 septembre 2022"])

json.dump(POSTS, open(BASE + "index.json", "w"), indent=1, ensure_ascii=False)

# Grille complète : lot 2 au-dessus du lot 1
prev = json.load(open("/home/claude/media/posts/lot01/index.json"))
order = list(POSTS.keys())[::-1]
covers = [POSTS[k][0] for k in order] + [prev[k][0] for k in list(prev.keys())[::-1]]
gw, gh = 300, 400
g = Image.new("RGB", (3 * gw + 4, 5 * gh + 8), "white")
for k, f in enumerate(covers):
    im = Image.open(f)
    cw = int(1350 * 3 / 4)
    im = im.crop(((1080 - cw) // 2, 0, (1080 + cw) // 2, 1350)).resize((gw, gh))
    r, c = divmod(k, 3)
    g.paste(im, (c * (gw + 2), r * (gh + 2)))
g.save("/home/claude/atlasienne/lot2_grille.png")
for k, fs in POSTS.items():
    tw, th = 432, 540
    sh = Image.new("RGB", (4 * (tw + 6), 2 * (th + 6)), "white")
    for i, f in enumerate(fs):
        r, c = divmod(i, 4)
        sh.paste(Image.open(f).resize((tw, th)), (c * (tw + 6), r * (th + 6)))
    sh.save(f"/home/claude/atlasienne/review2_{k}.png")
print("ok")
