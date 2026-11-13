import json, re
H1 = "#Marocaines #Maroc"
L = {
"01_photocopie": dict(
 ig="Tu as tous tes papiers, rangés dans une pochette, et il manque toujours une photocopie. Tu la fais, et c'est la photo d'identité qui manque.\n\nC'était quoi, le papier qui te manquait la dernière fois ? Envoie-le à celle qui a toujours une photocopie de trop dans son sac.\n\n#Papiers #VieAuMaroc " + H1,
 tt="Il manque une photocopie. Tu la fais, et il manque la photo d'identité. Ça t'est déjà arrivé ?\n\n#Papiers #VieAuMaroc " + H1,
 yt="« Khassek copie. » Il manque toujours un papier"),
"02_hammam": dict(
 ig="Mama f lhammam katgoul ghir dahrek, w katkemmel lik kolchi. W f lekher, katwerrik lwsekh b ferha.\n\nChkoun lli kaykessel lik f lhammam ? Siftiha l khtek.\n\n#Hammam #Darija #Mama " + H1,
 tt="Mama katgoul ghir dahrek. Arba3in dqiqa men b3d, mazal katkessel. Chkoun lli kaykessel lik ?\n\n#Hammam #Darija " + H1,
 yt="Mama f lhammam : « Ghir nkemmel lik dahrek »"),
"03_fleurs": dict(
 ig="Acheter des fleurs pour toi, sans fête, sans anniversaire, sans personne à qui les offrir. Ce n'est pas du gaspillage, c'est une façon de te dire merci.\n\nTu t'es offert quoi, la dernière fois, juste pour toi ? Envoie-le à celle qui ne s'achète jamais rien.\n\n#ToiDabord #Confiance " + H1,
 tt="Des fleurs pour toi, sans occasion. Ce n'est pas du gaspillage, c'est un merci à toi-même. Tu l'as déjà fait ?\n\n#ToiDabord #Confiance " + H1,
 yt="Des fleurs pour toi, sans occasion"),
"04_conge-mariage": dict(
 ig="Au Maroc, une salariée du privé a droit à 4 jours de congé pour son mariage, en plus de ses congés annuels. Si tu es payée au mois, ces jours sont payés en entier. Le justificatif, c'est l'acte de mariage, et ces jours se prennent autour de la date du mariage.\n\nTu le savais ? Envoie-le à ta copine qui se marie bientôt.\n\n#DroitDuTravail #Mariage " + H1,
 tt="4 jours de congé pour ton mariage, en plus de tes vacances. Ils sont payés en entier si tu es payée au mois. Tu le savais ?\n\n#DroitDuTravail #Mariage " + H1,
 yt="4 jours de congé pour ton mariage, tu le savais ?",
 sources="Sources : Code du travail marocain (loi 65-99), article 274. ClicPaie, « Congé de mariage au Maroc 2026 : 4 jours et droits », mis à jour le 11/03/2026, clicpaie.ma/blogs/conge-de-mariage-au-maroc. Humantal, « Congés payés au Maroc », revu le 09/01/2026, humantal.ma/blog/conges-payes-maroc-guide."),
"05_voisin-mariage": dict(
 ig="Le voisin du dessous se marie, tu ne l'as jamais vu, mais à 3 h du matin tu connais toute la playlist. Et à 4 h, tu fais les youyous depuis ton lit.\n\nLa chanson qui passe à tous les mariages, c'est laquelle ? Envoie-le à ta voisine, elle n'a pas dormi non plus.\n\n#MariageMarocain #Voisins " + H1,
 tt="Le voisin se marie. Tu ne le connais pas, mais à 3 h du matin tu connais toutes les chansons. La plus jouée, c'est laquelle ?\n\n#MariageMarocain #Voisins " + H1,
 yt="Le voisin se marie et tu connais toutes les chansons"),
"06_gateaux": dict(
 ig="À la fin du mariage, on te dit « juste quelques gâteaux ». Et tu rentres avec deux boîtes pleines sur les genoux.\n\nC'est quoi le gâteau que tu gardes pour la fin ? Envoie-le à celle qui repart toujours avec la boîte.\n\n#MariageMarocain #Gateaux " + H1,
 tt="« Ghir chwiya dyal lhelwa », dit la tante de la mariée. Tu rentres avec deux boîtes. Ton gâteau préféré, c'est lequel ?\n\n#MariageMarocain #Gateaux " + H1,
 yt="« Ghir chwiya dyal lhelwa » et deux boîtes pleines"),
"07_train-seule": dict(
 ig="Prendre le train seule pour un week-end, avec un sac léger et la fenêtre pour toi. Ce n'est pas une fuite, c'est une façon de revenir vers toi.\n\nTu irais où, seule, ce week-end ? Envoie-le à celle qui attend toujours une copine pour partir.\n\n#ToiDabord #Voyage " + H1,
 tt="Un week-end seule en train. Ce n'est pas une fuite, c'est revenir vers toi. Tu irais où ?\n\n#ToiDabord #Voyage " + H1,
 yt="Prendre le train seule pour un week-end"),
"08_wselti": dict(
 ig="Mama : « Wselti ? » Ana : « Mazal, ghir khrejt. » W 3echr dqayeq men b3d, nefs ssou2al.\n\nChhal men merra katsewwlek mok mli katsafri ? Siftiha liha.\n\n#Darija #Mama " + H1,
 tt="« Wselti ? » « Mazal, ghir khrejt. » W 3echr dqayeq men b3d : « Wselti ? » Mok tahiya ?\n\n#Darija #Mama " + H1,
 yt="Mama : « Wselti ? »"),
"09_sbah-lkhir": dict(
 ig="Tous les matins à 6 h, ta tante envoie une rose qui brille, avec de la musique, dans le groupe famille. Tout le monde répond « Sbah nnour ». Sauf toi, tu dors encore.\n\nChez toi, c'est qui la tante du bonjour ? Envoie-le à ta cousine du groupe famille.\n\n#GroupeFamille #FamilleMarocaine " + H1,
 tt="6 h du matin, une rose qui brille et « Sbah lkhir » dans le groupe famille. Tout le monde répond, sauf toi. C'est qui chez toi ?\n\n#GroupeFamille #FamilleMarocaine " + H1,
 yt="Ta tante, la rose et « Sbah lkhir » à 6 h"),
"10_coiffeuse": dict(
 ig="Rendez-vous à 14 h chez la coiffeuse, mariage à 20 h. À 18 h tu es encore sur la chaise, et tu arrives à 22 h, pile à l'heure comme tout le monde.\n\nTon record chez la coiffeuse, c'était combien d'heures ? Envoie-le à celle qui se prépare avec toi.\n\n#MariageMarocain #Coiffeuse " + H1,
 tt="Coiffeuse à 14 h, mariage à 20 h. À 18 h, tu es encore sur la chaise. Ton record, c'est combien ?\n\n#MariageMarocain #Coiffeuse " + H1,
 yt="Coiffeuse à 14 h, mariage à 20 h, encore assise à 18 h"),
"11_fin-kenti": dict(
 ig="Cinq minutes de retard et ta mère a déjà appelé ta sœur, ta cousine et ta copine. Et le lendemain, elle te rappelle qu'elle n'a pas dormi avant ton retour.\n\nTa mère appelle qui en premier quand tu es en retard ? Envoie-le-lui, elle va dire que c'est normal.\n\n#MamaMarocaine #Darija " + H1,
 tt="Cinq minutes de retard. Ta mère a déjà appelé ta sœur, ta cousine et ta copine. Elle appelle qui en premier, la tienne ?\n\n#MamaMarocaine #Darija " + H1,
 yt="Ta mère : « Fin kenti ? »"),
"12_bl3in": dict(
 ig="Tu demandes la recette à ta mère, et chaque quantité, c'est « bl3in ». Tu fais pareil, et ton tajine n'a jamais le même goût que le sien.\n\nC'est quoi le plat de ta mère que tu n'arrives pas à refaire ? Envoie-le-lui, elle va dire que c'est facile.\n\n#MamaMarocaine #CuisineMarocaine " + H1,
 tt="Chaque quantité de la recette de ta mère, c'est « bl3in ». Et ton plat n'a jamais le même goût. Le plat que tu n'arrives pas à refaire, c'est lequel ?\n\n#MamaMarocaine #CuisineMarocaine " + H1,
 yt="La recette de ta mère : « Bl3in »"),
"13_cinema-seule": dict(
 ig="Aller seule au cinéma un mardi soir, avec le pop-corn rien que pour toi. Ce n'est pas bizarre, c'est ton film, ton fauteuil, ton moment.\n\nLe dernier film que tu as vu seule, c'était lequel ? Envoie-le à celle qui attend toujours quelqu'un pour sortir.\n\n#ToiDabord #Confiance " + H1,
 tt="Seule au cinéma un mardi soir. Ce n'est pas bizarre, c'est ton moment. Tu l'as déjà fait ?\n\n#ToiDabord #Confiance " + H1,
 yt="Seule au cinéma un mardi soir, c'est ton moment"),
"14_moul-lhanout": dict(
 ig="Tu descends deux minutes chez moul lhanout, en pyjama sous la djellaba. Et ce jour-là, tu croises tout le quartier.\n\nTu as croisé qui, toi, le jour où tu n'étais pas prête ? Envoie-le à celle qui fait pareil le dimanche matin.\n\n#VieAuMaroc #Quartier " + H1,
 tt="Deux minutes chez moul lhanout, en pyjama sous la djellaba. Et tu croises tout le quartier. Tu as croisé qui ?\n\n#VieAuMaroc #Quartier " + H1,
 yt="En pyjama chez moul lhanout, tu croises tout le quartier"),
}
def fr(t):
    t = t.replace("'", "’")
    t = re.sub(r"(\d) (h|ans|mois|heure|minutes|DH|%|jours)\b", "\\1\u00a0\\2", t)
    t = re.sub(r" ([?!:])", "\u00a0\\1", t)
    t = t.replace("« ", "«\u00a0").replace(" »", "\u00a0»")
    return t
out = {}
for k, v in L.items():
    o = {kk: fr(vv) for kk, vv in v.items()}
    assert len(o["yt"]) <= 60, (k, len(o["yt"]))
    for vv in v.values():
        assert not re.search("[;—–]", vv), k
    out[k] = o
json.dump(out, open("/home/claude/media/reels_v8/legendes.json", "w"), ensure_ascii=False, indent=1)
print("ok", len(out))
