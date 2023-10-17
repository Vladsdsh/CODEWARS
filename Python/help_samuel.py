class Humain:
    def __init__(self, taille, poids, couleur, age, est_fille):
        self.taille = taille
        self.poids = poids
        self.couleur = couleur
        self.age = age
        self.est_fille = est_fille

    def manger(self):
        return "miam miam"

    def calcul_imc(self):
        return self.poids / (self.taille ** 2)

    def est_une_fille(self):
        return f"L'humain est une fille : {self.est_fille}"

kevin = Humain(1.85, 96.3, "noir", 26, False)

print(kevin.poids)
print(kevin.est_une_fille())
