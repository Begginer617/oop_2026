import random

# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    # atrybuty KLASY
    # (Cechy wspólne KAŻDEGO Czlowieka)
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec): # atrybuty OBIEKTU (składniki potrawy)
        # (Cechy KONKRETNEJ OSOBY)
        # Konstruktor
        # Akt Istnienia
        # Gotowanie
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec

    def __add__(self, other):
        if isinstance(other, Czlowiek) and self.plec != other.plec:
            return Dziecko(None, random.choice(("M", "K")))


    # Metoda
    # Możność (możliwość), zdolność, umiejętność
    def przedstaw_sie(self):
        print(f"Dzień dobry, mam na imię {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("mężczyzną")
        else:
            print("kobietą")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

class Dziecko(Czlowiek):
    def __init__(self, imie, plec):
        print(f"Powstaje Dziecko o imieniu {imie}")
        super().__init__(imie, plec)

    def __str__(self):
        if self.plec=="M":
            return f"Chłopiec {self.imie}"
        else:
            return f"Dziewczynka {self.imie}"

    def baw_sie(self):
        print("Ale zabawa, juhuu!!!!")
    def przedstaw_sie(self):
        print(f"Ceść, jestem {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("chłopcem")
        else:
            print("dziewczynką")

print (f"Zaimportowano moduł {__name__}")