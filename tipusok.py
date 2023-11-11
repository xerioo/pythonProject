import copy

class Valami:

    def __init__(self, parameter):
        self.parameter = parameter
        self.egyes = 1


a = 5
print(type(a))

szo = 'Hi'
print(type(szo))

so2 = szo
# so2 += "hossz"
print(szo)
print(so2)
print(id(szo))
print(id(so2))

v = Valami(66)
print(f'Ebbe itt {v.parameter} került')
