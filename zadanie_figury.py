# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()


class FiguraGeometryczna:
    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

# Napisz klasę Prostokąt
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_pole(self):
        return self.a * self.b

    def policz_obwod(self):
        return 2*self.a + 2*self.b

class Kwadrat(Prostokat):
    def __init__(self, a):
        super().__init__(a, a) # to jest jak Prostokat(a, a)

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r
class Trojkat(FiguraGeometryczna):
    pass
# Stwórz instancję tej klasy i sprawdź jej działanie

# +Kwadrat, Koło i Trójkąt*

kwadrat = Kwadrat(3)