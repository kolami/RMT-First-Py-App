import Personne as p
import datetime

prenom = str(input("Quel est ton prénom ?"))
annee = int(input("Quel est ton année de naissance ?"))
mois = int(input("Quel est ton mois de naissance ?"))
jour = int(input("Quel est ton jour de naissance ?"))

date_actuelle = datetime.datetime.now()
date_naissance = datetime.datetime(annee, mois, jour)

age = date_actuelle.year - date_naissance.year - ((date_actuelle.month, date_actuelle.day) < (date_naissance.month, date_naissance.day))

personne2 = p.Personne(prenom, age)
personne2.afficher_personne()

print("\nVoilà déjà",date_actuelle-date_naissance, "jour(s) que tu existes, je sais on s'en fou mais bon c'est marrant :D")