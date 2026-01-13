from abc import ABC, abstractmethod

# Interfejs na bazie Abstract Base Class
class FiguraGeometryczna(ABC):
    @abstractmethod
    def policz_pole(self):
        pass
    @abstractmethod
    def policz_obwod(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def policz_pole(self):
        return self.a * self.b

    def policz_obwod(self):
        return 2*self.a + 2*self.b


class Kwadrat(Prostokat):
    # Wsytarczy tylko tyle dzięki OOP,
    # co interfejs WYMUSI
    def __init__(self, a):
        super().__init__(a, a)  #


class Klasa:
    def __init__(self):
        self._a = 8
        self.__costam = 9

    # Sugestia żeby tego nie używać
    # Sugeruję tego nie ruszać
    def _hello(self):
        print("Hello world")
        self.__hej()

    # Faktycznie ukrycie metody
    def __hej(self):
        print("Hej!")

obiekt = Klasa()
obiekt._hello()
# obiekt.__init__()