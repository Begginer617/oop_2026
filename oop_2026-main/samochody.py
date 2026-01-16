class Pojazd:
    def jedz(self):
        print("Jadę...")
    def hamuj(self):
        print("Hamuję...")

class Samochod(Pojazd):
    # Samochód też jest pojazdem
    def __init__(self, marka, model):
        # Samochód posiada markę i model
        self.marka = marka
        self.model = model


class Honda(Samochod):
    def __init__(self, model):
        # Wiadomo, że marka to Honda, użyjmy zatem konstruktor z klasy Samochód
        super().__init__("Honda", model)



audi = Samochod("Audi", "A4")
audi.jedz()

honda = Honda("Civic")
honda.hamuj()