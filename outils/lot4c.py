"""Atlasienne - lot 4 : carrousel CNSS 1 320 jours."""
import sys, os
sys.path.insert(0, "/home/claude/atlasienne")
from atl2 import *
from PIL import Image
from phrase import noorph
OUT = "/home/claude/media/posts/lot04/04_retraite-cnss-1320-jours/"
os.makedirs(OUT, exist_ok=True)
av = avatar("/tmp/_av4.png")
F, L = "Argent", "Retraite"
fs = []
def p(i): return OUT + f"{i:02d}.jpg"
couverture(p(1), F, L, noorph("de cotisation CNSS suffisent pour une retraite à 60 ans"),
           noorph("Tu as travaillé quelques années puis tu as arrêté ? Lis ça, et montre-le à ta mère."), None, fr("1 320 jours")); fs.append(p(1))
interieure(p(2), F, L, fr("1 320"), noorph("jours déclarés, au lieu de 3 240 avant"),
           noorph("C'est le nouveau seuil pour une pension de vieillesse CNSS, soit un peu plus de 4 ans de cotisation à plein temps. En vigueur depuis le 1er\u00a0mai 2025."), None); fs.append(p(2))
liste(p(3), F, L, noorph("Les 3 conditions"), [noorph(x) for x in [
    "Avoir au moins 1 320 jours déclarés à la CNSS.",
    "Avoir 60 ans, atteints à partir du 1er\u00a0janvier 2023.",
    "Avoir arrêté toute activité salariée."]], None,
    note=noorph("Le texte : décret n° 2.25.265, pris en application de la loi 02.24.")); fs.append(p(3))
interieure(p(4), F, L, fr("600 à 1 000 DH"), noorph("de pension minimale par mois"),
           noorph("Le minimum dépend du nombre de jours déclarés, pour les carrières entre 1 320 et 3 239 jours. La couverture maladie AMO est incluse."), None); fs.append(p(4))
liste(p(5), F, L, noorph("Comment faire la demande"), [noorph(x) for x in [
    "En ligne via Taawydati, dans l'appli MaCNSS ou sur macnss.ma.",
    "Ou directement en agence CNSS.",
    "Pièces : copie de la CIN, RIB ou spécimen de chèque, et justificatif ou déclaration sur l'honneur d'arrêt d'activité."]], None,
    note=noorph("Une question sur ton dossier ? Centre d'appel CNSS : 3939.")); fs.append(p(5))
interieure(p(6), F, L, fr("6 mois"), noorph("pour déposer ta demande après tes 60 ans"),
           noorph("Dans ce délai, les mois précédents sont payés. En retard, la pension démarre le mois suivant la demande, sans rappel. Celles qui ont eu 60 ans entre janvier 2023 et avril 2025 ont un délai spécial de 24 mois, avec les arriérés. Renseigne-toi vite au 3939."), None); fs.append(p(6))
liste(p(7), F, L, noorph("Moins de 1 320 jours ?"), [noorph(x) for x in [
    "Tu peux cotiser en assurance volontaire, sous conditions, pour atteindre le seuil.",
    "Ou récupérer à 60 ans tes cotisations, part de l'employeur comprise, avec les intérêts.",
    "Si un proche décédé avait au moins 1 320 jours, sa famille peut demander une pension de survivant."]], None); fs.append(p(7))
fin(p(8), ["Communiqué CNSS relayé par la MAP, 7 avril 2025", "Médias24, 19 mai 2025"], "Point arrêté au 20 octobre 2026", av); fs.append(p(8))
tw, th = 432, 540
sh = Image.new("RGB", (4 * (tw + 6), 2 * (th + 6)), "white")
for i, f in enumerate(fs):
    r, c = divmod(i, 4); sh.paste(Image.open(f).resize((tw, th)), (c * (tw + 6), r * (th + 6)))
sh.save("/tmp/claude-0/-home-claude/80f0fa8b-2fe2-5065-ba69-adce18957eea/scratchpad/rev_cnss.png")
print("ok", len(fs))
