# Przekazywanie argumentów do funkcji
# Argumenty pozycyjne
def dodaj(a, b):
    return a+b
dodaj(6, 4)

# *args - wiele argumentów
def dodaj2(*args):
    # Zmienna lokalna wynik
    wynik = 0
    for arg in args:
        wynik += arg
    return wynik
# Mogę podawać wiele argumentów
print(dodaj2(2, 3))
print(dodaj2(2,4,5))
print(dodaj2(2,4,5,5,6,7))

# #Argument 'verbose' o domyślnej wartości
def dodaj3(*args, verbose=False):
    if verbose == True:
        print(f"Wykonam działanie dodawania. Dodam {args}")
    wynik = 0
    for arg in args:
        wynik += arg
    return wynik
#
print(dodaj3(2, 3))
print(dodaj3(2,4,5))
print(dodaj3(2,4,5,5,6,7))
print(dodaj3(2,4,5,5,6,7, verbose=True))

# Argumenty słownikowe
def funkcja(**kwargs):
    print(type(kwargs))
    print(kwargs)

funkcja(verbose=True, parametr="wartosc")
funkcja(verbose=True)
#
# Zmienna globalna wynik
wynik = dodaj3(1, 2, 3, 4, verbose=True)
print(wynik)


# Przykład na funkcji wbudowanej print
print("Adam")
print("Adam", "Ewa")
print("Adam", "Ewa", sep="przerwa")
print("Adam", "Ewa", sep="przerwa", end="koniec")
print("Adam", sep=" ", end="\n")