
#constructeur numéro 2
class Rectangle:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def surface(self):
        return self.a *(self.b)
appart = Rectangle(3,10)
maison = Rectangle (12,8)
print ("la surface est:",appart.surface())