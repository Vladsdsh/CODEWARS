class Somme:
    def __init__(self, n1, n2=0):
        self.n1 = n1
        self.n2=n2


    def som(self):
        return self.n1+(self.n2)

main = Somme(12)
resultat = main.som()
print(resultat)
