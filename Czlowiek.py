# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    # Atrybuty klasy
    gatunek = "Homo Sapiens"

    def __init__(self, imie, wzrost, plec):
        # Konstruktor
        # Akt Istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.wzrost = wzrost
        self.plec = plec


# Powstawanie obiektu
# Gotowanie z przepisu

adam = Czlowiek("adam", 185, "meżczyzna")  # a = 4 # a = int(4)
ewa = Czlowiek("ewa", 190, "kobieta")
print(adam.wzrost, adam.imie, adam.plec)
print(ewa.wzrost, ewa.imie, ewa.plec)

def przedstaw_sie(self, imie, wiek):
    print(f"Dzien dobry, mam na imie {self.imie}")
