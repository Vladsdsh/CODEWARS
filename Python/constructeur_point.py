import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx ** 2 + dy ** 2)

# Créez deux points
point1 = Point(2, 3)
point2 = Point(5, 7)

# Calculez la distance entre les deux points
distance = point1.distance(point2)

print(f"La distance entre les points est : {distance}")
