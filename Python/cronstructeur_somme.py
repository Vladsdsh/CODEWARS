class Somme:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def som(self):
        return self.n1 + self.n2
    
    def div(self):
        return self.n1 / self.n2

# Dans la méthode principale (main), demandez à l'utilisateur d'entrer deux entiers
n1 = int(input("Entrez le premier entier : "))
n2 = int(input("Entrez le deuxième entier : "))

# Créez une instance de la classe Somme en passant les deux nombres à son constructeur
calcul = Somme(n1, n2)

# Appelez la méthode som() pour calculer la somme et affichez le résultat
resultat = calcul.som()
print(f"La somme de {n1} et {n2} est égale à : {resultat}")

result = calcul.div()
print(f"La division de {n1} et {n2} est égale à : {result}")