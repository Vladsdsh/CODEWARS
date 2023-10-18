
#constructeur numéro 2
# valeurs de surchage est à la fin 
class Rectangle:
    def __init__(self, a, b=2):
        self.a=a
        self.b=b

    def surface(self):
        return self.a *(self.b)
appart = Rectangle(4)
maison = Rectangle(12,10)
print ("la surface est:",maison.surface())