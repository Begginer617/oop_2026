
class Kalkulator:
    def dodawanie(self):
        a = int(input("Podaj pierwszą liczbę dodawania: "))
        b = int(input("Podaj drugą liczbę dodawania: "))
        return a + b

    def odejmowanie(self):
        a = int(input("Podaj pierwszą liczbę odejmowania: "))
        b = int(input("Podaj drugą liczbę odejmowania: "))
        return a - b

nowy_kalkulator = Kalkulator()
print(nowy_kalkulator.dodawanie())
print(nowy_kalkulator.odejmowanie())
