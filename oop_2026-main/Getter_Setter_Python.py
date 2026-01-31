# W Pythonie nie musisz używać getterów i setterów tak często
# jak w językach typu Java czy C#,
# bo Python pozwala na bezpośredni dostęp do atrybutów obiektu.
# Ale… czasem warto kontrolować, co się dzieje przy odczycie
# lub zapisie wartości.
# I tu wchodzą:
# - getter – metoda wywoływana, gdy pobierasz wartość
# - setter – metoda wywoływana, gdy ustawiasz wartość
# W Pythonie robi się to elegancko dzięki @property.

class KontoBankowe:
    def __init__(self):
        self.__stanKonta = 0

    # ta funka bedzie uzywana jako atrybut
    @property
    def stanKonta(self):
        return f"stan konta: {self.__stanKonta} zł"

    @stanKonta.setter
    def stanKonta(self, zmiana):
        # sprawdzamy, czy po zmianie saldo nie będzie ujemne
        if self.__stanKonta + zmiana < 0:
            raise ValueError("Stan konta nie może być ujemny")

        # dodajemy zmianę do poprzedniego salda
        self.__stanKonta += zmiana


konto = KontoBankowe()

print(konto.stanKonta)  # 0 zł

konto.stanKonta = 50  # +50
print(konto.stanKonta)  # 50 zł

konto.stanKonta = -20  # -20
print(konto.stanKonta)  # 30 zł

# inny przykład
# class Osoba:
#     def __init__(self, wiek):
#         self._wiek = wiek  # atrybut "chroniony"
#
#     @property
#     def wiek(self):
#         return self._wiek  # getter
#
#     @wiek.setter
#     def wiek(self, nowy_wiek):
#         if nowy_wiek < 0:
#             raise ValueError("Wiek nie może być ujemny")
#         self._wiek = nowy_wiek  # setter
