class etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar
    def __str__(self):
        return f'Étel: {self.nev}, ára: {self.ar} Ft'

class etlap:
    pass

class Etterem:
    def __init__(self, etteremnev, etlap:list[etel]):
        self.etteremnev = etteremnev
        self.etlap = etlap

    def __str__(self):
        return f'Az étterem neve: {self.etteremnev}'

    def etlaplista(self):
        for k in self.etlap:
            print (f'{k.nev}{"." * (20 - len(k.nev) - len(str(k.ar)))}{k.ar} Ft')

    def __add__(self, ujetel:etel):
        self.etlap.append(etel(ujetel.nev, ujetel.ar))

kaja1 = etel("Húsleves", 1500)
kaja2 = etel('Hotdog', 1100)
kaja3 = etel('Gyros', 1600)
etlap1 = [kaja1, kaja2, kaja3]

ett1 = Etterem('Kisrabló', etlap1)

for i in range(2):
    ujetel_nev = input('Add meg az étel nevét: ')
    ujetel_ar = int(input('És az árát: '))
    if ujetel_ar<0 or ujetel_ar>100000:
        print('Nem megfelelő ár')
        break
    else:
        ett1 + etel(ujetel_nev,ujetel_ar)

ett1.etlaplista()


