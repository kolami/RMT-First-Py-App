class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_personne(self):
        print(f"\nBienvenue {self.nom}, tu as {self.age} ans, déjà....")


