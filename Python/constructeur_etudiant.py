class Etudiant:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.notes = []  # Créez une liste pour stocker les notes

    def ajouter_note(self):
        note = float(input(f"Entrez la note pour {self.nom} : "))
        self.notes.append(note)  # Ajoutez la note à la liste des notes

    def moyenne(self):
        if len(self.notes) > 0:
            moy = sum(self.notes) / len(self.notes)
            return f"La moyenne de {self.nom} est : {moy}"
        else:
            return f"{self.nom} n'a pas encore de notes."

# Créez une instance de la classe Etudiant
etudiant1 = Etudiant("Bertran", 19)

# Ajoutez des notes à l'étudiant
etudiant1.ajouter_note()
etudiant1.ajouter_note()
etudiant1.ajouter_note()

# Calculez la moyenne des notes de l'étudiant et affichez-la
print(etudiant1.moyenne())
