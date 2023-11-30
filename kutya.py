class Kutya:
    def __init__(self, nev, kor, faj):
        self.nev = nev
        self.kor = kor
        self.faj = faj

    def emberi_evekben(self):
        emberi_kor = self.kor * 7  # Alapért.: 1 kutyaév = 7 emberi év

        if self.faj.lower() == 'tacskó':
            emberi_kor = self.kor * 8  # Ha tacskó: 1 kutyaév = 8 emberi év

        print(f"{self.nev} kutya {self.faj} fajta és {self.kor} kutyaéves, ami emberi években {emberi_kor} év.")

# Tesztelés
kutya1 = Kutya("Reggio", 10, "Golden Retriever")
kutya1.emberi_evekben()

kutya2 = Kutya("Maszlag", 5, "Tacskó")
kutya2.emberi_evekben()
