class hermetyzacja_testowa:
    lista = []

    def dodaj(self,arg):
        self.lista.append(arg)

    def zdejmij(self):
        if len(self.lista)>0:
            return self.lista.pop(len(self.lista)-1) # pop zdemuje po indeksie. tuttaj indeks to self.
        else:
            return



obj_hermetyzacji_testowej=hermetyzacja_testowa()
obj_hermetyzacji_testowej.dodaj("A")
obj_hermetyzacji_testowej.dodaj("B")
obj_hermetyzacji_testowej.dodaj("C")
print(obj_hermetyzacji_testowej.zdejmij())
print(list(obj_hermetyzacji_testowej.lista))

# _ 1 lub __ 2 podłogi wskazuje ze ta metoda lub z zmienna jest ala prywatna
# _lista[]
#__lista[]
# aby odwloac sie do zmiennej prywatnej nalezy odwołac sie do klasy z pojedyncza podłoga



class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self._wiek = wiek  # "prywatne" wg konwencji. 1 _ podłoga przed wiek

o = Osoba("Ala", 20)
print(o.imie)     # OK
print(o._wiek)    # Technicznie działa, ale nie powinno się tak robić


# Podwójny podkreślnik: __zmienna
# „To jest naprawdę prywatne”
# Jeśli użyjesz dwóch podkreślników, Python zmienia nazwę zmiennej (tzw. name mangling), żeby utrudnić dostęp z zewnątrz.

class Konto:
    def __init__(self, saldo):
        self.__saldo = saldo  # bardziej prywatne

    def pokaz_saldo(self):
        return self.__saldo

k = Konto(100)
print(k.pokaz_saldo())  # OK
print(k.__saldo)        # Błąd: nie ma takiego atrybutu

