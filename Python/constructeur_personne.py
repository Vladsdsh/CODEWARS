class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def presentation(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

# Créez une instance de la classe Personne
une_personne = Personne("Alice", 30)

# Appelez la méthode presentation pour afficher les détails de la personne
print(une_personne.presentation())
