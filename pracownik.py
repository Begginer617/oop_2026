#   Program do zarządzania małą firmą

# Bez programowania obiektowego:
pracownik1_imie = "Adam"
pracownik1_nazwisko = "Nowak"
pracownik1_pensja = 4500

pracownik2_imie = "Anna"
pracownik2_nazwisko = "Nowak"
pracownik2_pensja = 4500

pracownik2_pensja = pracownik2_pensja + 100

## OOP
class Pracownik:
    def __init__(self, imie, nazwisko,pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def daj_podwyzje(self, kwota):
        self.pensja = self.pensja + kwota

adam_nowak = Pracownik("Adam", "Nowak", 4500)
adam_nowak.daj_podwyzje(100)