from datetime import date, timedelta
import random

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.price = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=20000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, ar=30000)

class Foglalas:
    def __init__(self, szoba, foglalas_datuma):
        self.szoba = szoba
        self.foglalas_datuma = foglalas_datuma

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def SzobaHozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def Foglal(self, szobaszam, foglalas_datuma):
        szoba = self.SzobakeresesSzammal(szobaszam)

        if not szoba:
            print("Ilyen számú szobánk nincs.")
            return None

        if not self.JoADatum(foglalas_datuma):
            print("Nem stimmel a dátum, a jövőben kéne lennie.")
            return None

        if not self.SzabadASzoba(szoba, foglalas_datuma):
            print("Ez a szoba ezen a napon már foglalt.")
            return None

        #foglalas = Foglalas(szoba, foglalas_datuma)
        self.foglalasok.append(Foglalas(szoba, foglalas_datuma))
        print(f"A {szoba.szobaszam}. szoba lefoglalva erre a dátumra: {foglalas_datuma}.")
        return szoba.price

    def FoglalasTorlese(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            print("Foglalás törölve.")
        else:
            print("Váratlan hiba történt.")

    def FoglalasokListazasa(self):
        print("\nFoglalások:")
        for i, fogl in enumerate(self.foglalasok, start=1):
            print(f"{i}. foglalás, szobaszám: {fogl.szoba.szobaszam}. - dátum: {fogl.foglalas_datuma}")

    def SzobakeresesSzammal(self, szobaszam):
        for sz in self.szobak:
            if sz.szobaszam == szobaszam:
                return sz
        return None

    def JoADatum(self, fogl_datum):
        return fogl_datum > date.today()

    def SzabadASzoba(self, szoba, fogl_datum):
        for fogl in self.foglalasok:
            if fogl.szoba == szoba and fogl.foglalas_datuma == fogl_datum:
                return False
        return True

hotel = Szalloda("Waczak Szálló")
szoba1 = EgyagyasSzoba(1)
szoba2 = KetagyasSzoba(2)
szoba3 = EgyagyasSzoba(3)

hotel.SzobaHozzaadasa(szoba1)
hotel.SzobaHozzaadasa(szoba2)
hotel.SzobaHozzaadasa(szoba3)

for i in range (1, 6):
    fogl = hotel.Foglal(random.randint(1, 3), date.today() + timedelta(days=random.randint(1, 50)))

while True:
    print("\nNapi menü:")
    print("1. Szobafoglalás")
    print("2. Foglalás törlése")
    print("3. Foglalások listázása")
    print("4. Kilépés")

    valasztas = input("Válassz (1-4): ")

    if valasztas == "1":
        szobaszam = int(input("A szobaszám: "))
        foglalas_datuma_str = input("A foglalás dátuma (ÉÉÉÉ-HH-NN): ")

        try:
            foglalas_datuma = date.fromisoformat(foglalas_datuma_str)
        except ValueError:
            print("Nem jó a dátum formátuma, légyszi ÉÉÉÉ-HH-NN alakban.")
            continue

        hotel.Foglal(szobaszam, foglalas_datuma)

    elif valasztas == "2":
        hotel.FoglalasokListazasa()
        fogl_azon = int(input("Add meg a törlendő foglalás sorszámát: "))

        if 1 <= fogl_azon <= len(hotel.foglalasok):
            hotel.FoglalasTorlese(hotel.foglalasok[fogl_azon - 1])
        else:
            print("Nincs ilyen sorszám. A sorszámot a sor elején találod.")

    elif valasztas == "3":
        hotel.FoglalasokListazasa()

    elif valasztas == "4":
        print("Viszlát.")
        break

    else:
        print("1, 2, 3 és 4 a választható lehetőségek.")
