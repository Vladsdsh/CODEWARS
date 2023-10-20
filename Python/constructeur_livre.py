class livre:
    def __init__(self,titre,auteur,annee):
        self.titre=titre
        self.auteur=auteur
        self.annee=annee
    

    def info(self):
        return f"le livre {self.titre} écrit par {self.auteur}, edite en {self.annee} est le meilleur"

logi=livre ("le passeur","Pierre Colmart",2045)

titre_= str(input("quel est le titre du livre ?"))
auteur_= str(input("quel est le nom de l'auteur ?"))
annee_= str(input("quel est l'année du livre ?"))
print (f"le livre {titre_} écrit par {auteur_}, edite en {annee_} est le meilleur")