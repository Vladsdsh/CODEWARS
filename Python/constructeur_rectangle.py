class rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur 
        self.largeur = largeur 

    def aire(self):
        return (self.longueur * self.largeur)
    def perimetre(self):
        return (2*(self.longueur + self.largeur))

tableau = rectangle (12,4)
print("L'aire du tableau est : ", tableau.aire())
print("Le périmètre du tableau est : ", tableau.perimetre())