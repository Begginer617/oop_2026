import datetime
import time


#  Metoda statyczna — najprościej
# 🔹 Co to jest?
# To funkcja w klasie, która nie potrzebuje niczego z tej klasy.
# 🔹 Jak to wykorzystasz w testach?
# Do rzeczy pomocniczych, np.:
# • 	generowanie losowych danych,
# • 	walidacje,
# • 	proste obliczenia,
# • 	formatowanie tekstu,
# • 	konwersje.
# 🔹 Przykład z automatyzacji

#metoda statyczna
class DataUtils:
    @staticmethod
    def email_for_test():
        return "test_" + str(int(time.time())) + "@example.com"


email = DataUtils.email_for_test()
# Nie musisz tworzyć obiektu klasy — wygodne i czyste.


#metoda klasowa
# 2. Metoda klasowa — najprościej
# 🔹 Co to jest?
# To metoda, która działa na poziomie klasy, a nie obiektu.
# Dostaje " cls " zamiast " self. "
# Jak to wykorzystasz w testach ?
# Najczęściej jako alternatywny konstruktor.
# Przykład: chcesz tworzyć obiekt API clienta na różne sposoby:

class ApiClient:
    def __init__(self, token):
        self.token = token

    @classmethod
    def from_env(cls):
        return cls(token=os.getenv("API_TOKEN"))

client = ApiClient.from_env()