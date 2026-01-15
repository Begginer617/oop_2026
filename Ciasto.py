class Ciasto:
    # WSPÓLNA baza biszkoptu dla wszystkich ciast
    BAZA_BISZKOPTU = ["mąka", "jajka", "cukier"]

    def __init__(self, nazwa_ciasta, skladniki=None):
        self.nazwa_ciasta = nazwa_ciasta
        # jeśli nie podasz składników → używa bazy biszkoptu
        self.skladniki = list(skladniki) if skladniki else list(self.BAZA_BISZKOPTU)

    def dodaj_skladnik(self, skladnik):
        self.skladniki.append(skladnik)

    def __str__(self):
        return f"Ciasto: {self.nazwa_ciasta}, składniki: {', '.join(self.skladniki)}"


ciasto_czekoladowe = Ciasto("Czekoladowe")
ciasto_czekoladowe.dodaj_skladnik("kakao")

ciasto_truskawkowe = Ciasto("Truskawkowe")
ciasto_truskawkowe.dodaj_skladnik("truskawki")

print(ciasto_czekoladowe)
print(ciasto_truskawkowe)