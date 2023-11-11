class polygon:
    color = 'piros'

    def __init__ (self, sides):
        self.sides = sides
        self.oldal = 2


    def __str__(self):
        return f"polygon {self.sides} oldallal"


p1 = polygon (3)

print(p1)