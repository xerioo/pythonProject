class Allat:

    def __init__(self, nev):
        self._nev = nev

    def nevetmond(self):
        print(f"A nevem {self._nev}")


class Kutya (Allat):

    def __init__(self, nev, faj):
        super().__init__(nev)
        self.faj = faj

    @staticmethod
    def ugat():
        print('Vau!')

    def nevetmond(self):
        print(f"Vau, a nevem {self._nev}")


bodri = Kutya('Bodrikutya', 'Puli')

bodri.nevetmond()
