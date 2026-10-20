# Atlasienne - passation (état au 20/10/2026, 22h45)

Pour reprendre dans une nouvelle conversation du projet R.Sociaux : lire cette fiche, puis claude/atlasienne/feuille-de-route.md (ligne éditoriale en vigueur depuis le 21/10 : copine marocaine, pas chaîne d'info), puis claude/atlasienne/bareme-formats.md.

## Identité
- Instagram @atlasienne_com, média anonyme pour les Marocaines. Le propriétaire n'apparaît jamais, aucun lien avec Peu le savent.
- Claude décide et produit. Le propriétaire publie les Reels à la main depuis l'appli (Metricool bloqué par Instagram depuis le 18/10).
- Règles d'écriture : pas de tiret cadratin ni demi-cadratin, pas de point-virgule, pas de gras, pas d'emoji, aucune mention d'IA, tutoiement, typographie française, sources datées en fin de légende, non partisan.

## Où sont les fichiers
- Tout est sur GitHub Atlasienne/media (commit a1c6049) : outils/ (scripts, polices Fraunces et Readex, photos Unsplash eq/hd + idx.json et eq/l4, kit, logos, avatar), posts/, reels/, reels_src/, reels_v2/, reels_v3/, reels_v4/.
- Remise en route dans une nouvelle session : add_repo (owner Atlasienne, repo media, access push), cloner dans /home/claude/media, puis copier outils/ vers /home/claude/atlasienne. Dans outils/atl2.py, la variable D (ligne 6) pointe déjà vers /home/claude/atlasienne/ (polices dans fonts/). Commits au nom Atlasienne <contact@atlasienne.com>, sans ligne d'attribution.
- Connecteurs au niveau du compte (restent actifs) : Metricool (blogId 7495879, toujours fuseau "UTC"), Unsplash (search_photos puis download_asset obligatoire). Domaine images.unsplash.com autorisé dans Capacités.
- Ne jamais contourner l'allowlist réseau (pas de GitHub Actions pour aller chercher des images).

## Moteurs
- atl2.py : carrousels info 1080x1350 (couverture, interieure, liste, fin). anchor "la" pour le multiligne, espace insécable ( ) contre les mots orphelins.
- phrase.py (nouveau, lot 4) : format « la phrase qu'on envoie à sa copine ». Photo plein cadre 1080x1920 sous voile chaud, phrase Fraunces blanche centrée, sous-ligne et consigne finale en rose, marque discrète au-dessus de la zone de légende. reel_phrase(slug, dossier, écrans) fabrique les JPEG et le MP4 (fondus 0,35 s, durée par écran 2 à 3,6 s selon le nombre de mots). noorph() lie les petits mots et les deux derniers mots, à utiliser aussi sur les carrousels. Option flou=10 pour masquer un écran de téléphone.
- entre_nous.py : format « Entre nous » (duo photo couleur / noir et blanc). reel.py : carrousel 1080x1350 vers Reel 1080x1920.
- lot4.py (6 Reels) et lot4c.py (carrousel CNSS) : modèles à copier pour les lots suivants.

## Lot 4 (produit le 20/10, relu par un relecteur indépendant, corrigé)
Fichiers : reels_v4/*.mp4 (+ dossiers JPEG), reels_v4/legendes.json, posts/lot04/07_retraite-cnss-1320-jours/01-08.jpg, posts/lot04/legendes.json (texte + commentaire sources).
Calendrier de publication, à la main, 13h et 21h :
- 22/10 13h : 01_tante-mariage (Reel situation)
- 22/10 21h : 03_phrases-meres (Reel rigolade darija)
- 23/10 13h : 02_avant-30-ans (Reel motivation)
- 23/10 21h : 07 carrousel CNSS 1 320 jours (info utile, mettre la légende puis les sources en premier commentaire)
- 24/10 13h : 05_whatsapp-famille (Reel situation)
- 24/10 21h : 04_plaisirs-50dh (Reel féminité)
- 25/10 13h : 06_dire-non-famille (Reel confiance)
Ajouter un son tendance dans l'appli. Garder les MP4 muets du dépôt comme versions sponsorisables.
Point à confirmer : le délai spécial de 24 mois (60 ans atteints entre 01/2023 et 04/2025) court probablement jusqu'à fin avril 2027, une seule source le dit (Clicpaie, 20/03/2026). Le carrousel reste prudent et renvoie au 3939.

## Publié
- 18-19/10 via Metricool : carrousels lot 1 et lot 2, Entre nous 01 et 02 (0 à 2 vues).
- 20/10 à la main : 10 Reels de reels_v2 + Touria en carrousel.
- 20/10 vers 21h30 : les 3 Reels de reels_v3 (veuves-100, respect, aide-1000). 13 publications le 20/10 : rien d'autre avant le 22/10.
- Grille au 20/10 21h35 : 22 publications, 0 abonné. Vues : caftan 117, Moudawana 109, congé 101, SMIG 39, henné 33, octobre rose 17, phrases 13, en silence 11, ASD 9, respect 3, 100 % 2, 1 000 DH 2, dire non 2, carrousels 0 à 2.

## Grille : archivage conseillé le 20/10
Doublons encore visibles : carrousels Moudawana et Caftan, à archiver. Le Reel « Ce que tu fais en silence » est remplacé le 21/10 à 20h par reels_v3/en-silence.mp4. Garder en carrousel : HCP, SRM, Gouvernement, Huile d'olive, Zineb El Adaoui, 150 min, Touria.

## Barème Reel ou carrousel
Voir claude/atlasienne/bareme-formats.md. Lot 4 : les 6 Reels font 4 ou 5 points Reel, le CNSS fait 3 points carrousel (et assez de points Reel pour une version Reel courte plus tard).

## Publicité
Pas avant le bilan du 22/10 et au moins 15 Reels en ligne. Ensuite boost d'un Reel déjà gagnant en organique, non politique, sans musique sous droits, objectif visites du profil, femmes 18-44 au Maroc, environ 50 DH par jour pendant 4 jours.

## Rappels
- 21/10 20h : publier le nouveau en-silence.mp4 à la place de l'ancien.
- 22/10 : bilan vues, partages, enregistrements à partir des captures du tableau de bord professionnel, dans cette conversation.
- Plus tard : connecter Metricool via une page Facebook pour retrouver la programmation.
