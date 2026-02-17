
def zmien(a):
    a = 8
    return a


# Python przekazuje KOPIĘ argumentu lub ORYGINAŁ
# NON-MUTABLE
a = 7
print(a)
# Python KOPIUJE a
zmien(a)
# Oryginalne a zostało nietknięte
print(a)


# MUTABLE
def zmien_liste(lista):
    lista.append("HAHA!")
    return lista
lista = [1,2]
# Tutaj nie jest przekazywana KOPIA, lecz ORYGINAŁ
print(lista)
zmien_liste(lista)
# Lista uległa zmianie
print(lista)