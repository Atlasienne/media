"""Atlasienne - lot 4 : 6 Reels « copine » + 1 carrousel CNSS. A publier du 22 au 25/10/2026."""
import sys, os, json
sys.path.insert(0, "/home/claude/atlasienne")
from phrase import reel_phrase
from PIL import Image

R = "/home/claude/media/reels_v4/"
os.makedirs(R, exist_ok=True)

REELS = {
 "06_tante-mariage": [
  dict(photo="plafond.jpg", phrase="Mariage de ta cousine. Ta tante arrive avec son sourire spécial.", fy=.45),
  dict(photo="plafond.jpg", phrase="« W nti, imta ? »", sous="Et toi, c'est pour quand ?", taille=118, fy=.45, duree=2.6),
  dict(photo="plafond.jpg", phrase="Réponse polie : « Inchallah, khalti. »", fy=.45),
  dict(photo="plafond.jpg", phrase="Réponse honnête : « Dès que je finis mon assiette de gâteaux. »", fy=.45),
  dict(photo="plafond.jpg", phrase="En vrai : sourire, prendre une corne de gazelle et changer de table.", fy=.45,
       cta="Tag la cousine qui l'a entendu trois fois cette année."),
 ],
 "02_avant-30-ans": [
  dict(photo="fenetre.jpg", phrase="Rappel : tu n'as pas à tout réussir avant 30 ans.", taille=96, fy=.3),
  dict(photo="fenetre.jpg", phrase="Ni le mariage, ni la maison, ni le poste parfait.", fy=.3),
  dict(photo="fenetre.jpg", phrase="Des femmes ont tout recommencé à 35, à 40, à 50 ans.", sous="Et elles vont très bien.", fy=.3),
  dict(photo="fenetre.jpg", phrase="Ta vie n'est pas en retard. Elle avance à ton rythme.", fy=.3,
       cta="Envoie-le à celle qui compte les années un peu trop fort."),
 ],
 "07_phrases-meres": [
  dict(photo="tajines.jpg", phrase="Les phrases que toutes les mères marocaines disent.", taille=92, fy=.6),
  dict(photo="tajines.jpg", phrase="« Chkoun lli gal lik ? »", sous="Qui t'a dit ça ? Même quand c'est elle qui l'a dit hier.", taille=112, fy=.6),
  dict(photo="tajines.jpg", phrase="« Ghir sber. »", sous="Patiente. Ça marche pour un rhume, un chagrin et une fin de mois.", taille=118, fy=.6),
  dict(photo="tajines.jpg", phrase="« Rah ana mok. »", sous="Je suis ta mère. Fin de la discussion.", taille=118, fy=.6),
  dict(photo="tajines.jpg", phrase="« Ma kayn lli bhalek. » Le lendemain : « Chouf\u00a0bent\u00a0khaltek. »", sous="Personne n'est comme toi. Regarde ta cousine.", fy=.6,
       cta="Laquelle tu entends le plus ? Dis-le en commentaire."),
 ],
 "03_plaisirs-50dh": [
  dict(photo="the_atlas.jpg", phrase="5 petits plaisirs à moins de 50 DH.", taille=104, fy=.55),
  dict(photo="menthe.jpg", phrase="1. Un thé à la menthe en terrasse, seule, sans téléphone.", fy=.5),
  dict(photo="rideau.jpg", phrase="2. Le hammam du quartier, avec ton savon beldi.", fy=.5),
  dict(photo="salon.jpg", phrase="3. Un bouquet de menthe et de fleurs au marché, pour toi.", fy=.5),
  dict(photo="rideau.jpg", phrase="4. Un masque au ghassoul, le\u00a0dimanche\u00a0soir.", fy=.5),
  dict(photo="the_atlas.jpg", phrase="5. Une heure rien que pour toi. Ça, c'est 0 DH.", fy=.55,
       cta="Envoie-le à celle qui ne pense jamais à elle."),
 ],
 "05_whatsapp-famille": [
  dict(photo="tel.jpg", flou=10, phrase="Le groupe WhatsApp de la famille, en vrai.", taille=96),
  dict(photo="tel.jpg", flou=10, phrase="6\u00a0h du matin. Ton oncle envoie « Sbah lkhir » avec une rose."),
  dict(photo="tel.jpg", flou=10, phrase="Ta tante transfère une info « très importante ». Elle date de 2017."),
  dict(photo="tel.jpg", flou=10, phrase="Ta mère : un vocal de 4 minutes pour dire qu'elle t'a appelée."),
  dict(photo="tel.jpg", flou=10, phrase="Toi : un « ok » à 23\u00a0h. Et le groupe passe en sourdine.",
       cta="Tag la cousine qui a mis le groupe en silencieux."),
 ],
 "01_dire-non-famille": [
  dict(photo="salon.jpg", phrase="Tu as le droit de dire non. Même à la famille.", taille=96, fy=.45),
  dict(photo="salon.jpg", phrase="Non à la troisième assiette qu'on te ressert.", fy=.45),
  dict(photo="salon.jpg", phrase="Non à la question sur ton salaire devant tout le monde.", fy=.45),
  dict(photo="salon.jpg", phrase="Non au week-end organisé sans te demander ton avis.", fy=.45),
  dict(photo="salon.jpg", phrase="Dire non avec le sourire, c'est te respecter aussi.", fy=.45,
       cta="Envoie-le à celle qui dit oui à tout le monde, sauf à elle."),
 ],
}

if __name__ == "__main__":
    only = sys.argv[1:] or list(REELS)
    info = {}
    for slug in only:
        fs, durs, out = reel_phrase(slug, R, REELS[slug])
        info[slug] = dict(ecrans=len(fs), duree=round(sum(durs), 1))
        tw, th = 270, 480
        sh = Image.new("RGB", (len(fs) * (tw + 6), th), "white")
        for i, f in enumerate(fs):
            sh.paste(Image.open(f).resize((tw, th)), (i * (tw + 6), 0))
        sh.save(f"/tmp/claude-0/-home-claude/80f0fa8b-2fe2-5065-ba69-adce18957eea/scratchpad/rev_{slug}.png")
    print(json.dumps(info, ensure_ascii=False))
