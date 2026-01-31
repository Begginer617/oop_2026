class Zloty(float):
    # Złoty to też float
    def __add__(self, other):
        # Złoty ma swoją wersję operatora "+"
        return Zloty(super().__add__(other))
    def zamien_na_euro(self):
        # Ma też metodę zamieniającą na EURO
        return self / 4.21

a = float(2.0) # a = 2.0
b = float(3.0)
c = Zloty(6.0)
d = Zloty(7.0)

wynik = c + d
print(wynik)
print(type(wynik))
print(wynik.zamien_na_euro())