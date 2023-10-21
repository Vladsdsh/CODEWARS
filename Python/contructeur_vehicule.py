class vehicule:
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur
    
    def description(self):
        return f"Ce vehicule est une {self.marque} de couleur {self.couleur}"

citadine = vehicule("toyota","rouge")
print (citadine.description())