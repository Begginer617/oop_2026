def cwiczenie():  # TEGO NIE ZMIENIAJ, TO MUSI BYĆ NA SAMEJ GÓRZE

    dane = ["Programowanie", "w", "Pythonie"]

    while True:
        try:
            index = int(input("Podaj index listy do odczytania wartości: "))
            print(index)
            wynik = dane[index]
            print(wynik)

        except ValueError:
            wynik = "podajemy tylko liczby"
            break

        except IndexError:
            wynik = "przekroczono rozmiar listy"
            break

        else:
            break

    return wynik

print(cwiczenie())