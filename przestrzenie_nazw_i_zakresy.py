#samochod.py

# To jest przestrzeń nazw modułu - cały ten plik
class Samochod:
    def __init__(self, marka, model):
        # To jest atrybut instancji, każda instancja ma swoje własne wartości
        self.marka = marka
        self.model = model

    def wyswietl_info(self):
        # To jest metoda - w jej wnętrzu mamy dostęp do atrybutów instancji
        print(f"Samochód to {self.marka} {self.model}")

def zrob_cos():
    # To jest przestrzeń nazw funkcji - zmienne lokalne
    marka = "Honda"
    model = "Civic"
    print(f"W funkcji: {marka} {model}")

# Tworzenie obiektu
auto = Samochod("Toyota", "Corolla")
auto.wyswietl_info()

# Wywołanie funkcji
zrob_cos()
