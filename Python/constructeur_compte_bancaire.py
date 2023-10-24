class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self.solde = solde

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return f"{montant} € ont été retirés de {self.nom}. Nouveau solde : {self.solde} €"
        else:
            return f"Solde insuffisant pour effectuer le retrait de {montant} €."

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            return f"{montant} € ont été déposés sur le compte de {self.nom}. Nouveau solde : {self.solde} €"
        else:
            return "Le montant du dépôt doit être supérieur à zéro."

# Créez une instance de la classe CompteBancaire
banque = CompteBancaire("Sisoko", 100)

# Effectuez un retrait
montant_retrait = float(input("Entrez le montant à retirer : "))
print(banque.retirer(montant_retrait))

# Effectuez un dépôt
montant_depot = float(input("Entrez le montant à déposer : "))
print(banque.deposer(montant_depot))
