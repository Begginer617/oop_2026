class Ciasto:
    BAZA_BISZKOPTU = ["mąka", "jajka", "cukier"]

    def __init__(self, nazwa_ciasta):
        self.nazwa_ciasta = nazwa_ciasta
        self.skladniki = self.BAZA_BISZKOPTU.copy()

    def dodaj_skladnik(self, skladnik):
        self.skladniki.append(skladnik)

    def kopiuj(self):
        nowe = Ciasto(self.nazwa_ciasta)
        nowe.skladniki = self.skladniki.copy()
        return nowe

    def __str__(self):
        return f"Ciasto: {self.nazwa_ciasta}, składniki: {', '.join(self.skladniki)}"


# ⬇️ TO MUSI BYĆ POZA KLASĄ
ciasto1 = Ciasto("Czekoladowe")
ciasto1.dodaj_skladnik("kakao")
ciasto1.dodaj_skladnik("czekolada")

ciasto2 = ciasto1.kopiuj()
ciasto2.dodaj_skladnik("orzechy")

print(ciasto1)
print(ciasto2)