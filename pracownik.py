class Zarzad:
    def __init__(self, imie, nazwisko, pensja, ranga_dyrektora):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.ranga_dyrektora = ranga_dyrektora

    def zwolnij_pracownika(self, pracownik):
        print(f"Pracownik {pracownik.imie} {pracownik.nazwisko} został zwolniony.")

    def zatrudnij_pracownika(self, pracownik):
        print(f"Pracownik {pracownik.imie} {pracownik.nazwisko} został zatrudniony.")


class Manager(Zarzad):
    def __init__(self, imie, nazwisko, pensja, ranga_managera):
        super().__init__(imie, nazwisko, pensja, ranga_managera)


class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def daj_podwyzke(self, kwota):
        self.pensja += kwota
        print(f"{self.imie} {self.nazwisko} otrzymał podwyżkę o {kwota} zł. Nowa pensja: {self.pensja} zł.")


# Tworzenie obiektów
adam_nowak = Pracownik("Adam", "Nowak", 4500)
adam_nowak.daj_podwyzke(100)
anna_nowak = Pracownik("Anna", "Nowak", 4500)
ziomek = Manager("Jan", "Kowalski", 8000, "Manager")
ziomek.zwolnij_pracownika(anna_nowak)

# Manager zatrudnia i zwalnia pracowników
ziomek.zatrudnij_pracownika(anna_nowak)
ziomek.zwolnij_pracownika(adam_nowak)