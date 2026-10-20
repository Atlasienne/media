# Atlasienne - passation (état au 20/10/2026, 21h30)

Pour reprendre dans une nouvelle conversation du projet R.Sociaux : lire cette fiche, puis claude/atlasienne/feuille-de-route.md (ligne éditoriale en vigueur depuis le 21/10 : copine marocaine, pas chaîne d'info), puis claude/atlasienne/bareme-formats.md.

## Identité
- Instagram @atlasienne_com, média anonyme pour les Marocaines. Le propriétaire n'apparaît jamais, aucun lien avec Peu le savent.
- Claude décide et produit. Le propriétaire publie les Reels à la main depuis l'appli (Metricool bloqué par Instagram depuis le 18/10).
- Règles d'écriture : pas de tiret cadratin ni demi-cadratin, pas de point-virgule, pas de gras, pas d'emoji, aucune mention d'IA, tutoiement, typographie française, sources datées en fin de légende, non partisan.

## Où sont les fichiers
- Tout est sur GitHub Atlasienne/media (commit 7774530) : outils/ (scripts, polices Fraunces et Readex, photos Unsplash eq/hd + idx.json, kit, logos, avatar), posts/, reels/, reels_src/, reels_v2/, reels_v3/.
- Remise en route dans une nouvelle session : add_repo (owner Atlasienne, repo media, access push), cloner dans /home/claude/media, puis copier outils/ vers /home/claude/atlasienne et outils/fonts vers le dossier fonts attendu par atl2.py (variable D en ligne 6, à repointer vers /home/claude/atlasienne/fonts/). Commits au nom Atlasienne <contact@atlasienne.com>, sans ligne d'attribution.
- Connecteurs au niveau du compte (restent actifs) : Metricool (blogId 7495879, toujours fuseau "UTC"), Unsplash (search_photos puis download_asset obligatoire). Domaine images.unsplash.com autorisé dans Capacités.
- Ne jamais contourner l'allowlist réseau (pas de GitHub Actions pour aller chercher des images).

## Moteurs
- atl2.py : carrousels info 1080x1350 (couverture, interieure, liste, fin). anchor "la" pour le multiligne, espace insécable (\u00a0) contre les mots orphelins.
- entre_nous.py : format « Entre nous » (duo photo couleur / noir et blanc, couverture_photo, fin_partage). pages=None pour les Reels.
- reel.py : reel(slides, out, first, each, last, fade) vers 1080x1920. Info : each=4.2. Actu courte : each=3.4 à 3.6.
- lot3r.py (veuves-100, aide-1000), en03r.py (respect), en01r.py (en silence sans pagination, reels_v3/en-silence.mp4, à publier le 21/10 au soir en remplacement de l ancien Reel).

## Publié
- 18-19/10 via Metricool : carrousels lot 1 et lot 2, Entre nous 01 et 02 (0 à 2 vues).
- 20/10 à la main : 10 Reels de reels_v2 + Touria en carrousel.
- 20/10 vers 21h30 : les 3 Reels de reels_v3 publiés d'un coup (veuves-100, respect, aide-1000). Soit 13 publications le 20/10 : rien d'autre avant le 22/10 pour éviter un nouveau blocage.
- Grille au 20/10 21h35 : 22 publications, 0 abonné. Vues : caftan 117, Moudawana 109, congé 101, SMIG 39, henné 33, octobre rose 17, phrases 13, en silence 11, ASD 9, respect 3, 100 % 2, 1 000 DH 2, dire non 2, carrousels 0 à 2.

## Résultats 20/10 20h40
Moudawana 107, congé maternité 51, SMIG 32, henné 30, caftan 19, octobre rose 16, en silence 11, phrases 10, ASD 4, dire non 2. Carrousels 0 à 2.

## Grille : archivage conseillé le 20/10
Seuls doublons encore visibles : carrousels Moudawana et Caftan, à archiver. Le Reel « Ce que tu fais en silence » garde « Glisse » et 1/9 sur sa couverture (ancienne version d'essai), à remplacer plus tard si besoin. Garder en carrousel : HCP, SRM, Gouvernement, Huile d'olive, Zineb El Adaoui, 150 min, Touria.

## Barème Reel ou carrousel
Voir claude/atlasienne/bareme-formats.md.

## Publicité
Pas avant le bilan du 22/10 et au moins 15 Reels en ligne. Ensuite boost d'un Reel déjà gagnant en organique, non politique, sans musique sous droits, objectif visites du profil, femmes 18-44 au Maroc, environ 50 DH par jour pendant 4 jours.

## Rappels
- L'ancienne conversation est supprimée : le rappel du 22/10 n'existe plus. Faire le bilan du 22/10 dans la nouvelle conversation.
- Plus tard : connecter Metricool via une page Facebook pour retrouver la programmation.
