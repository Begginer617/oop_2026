while (True):

    while (True):
        try:
            liczba1 = int(input("Podaj liczbe 1: "))
        except:
            print("podajemy tylko liczby !!!")
        else:
            break
    while (True):
        try:
            liczba2 = int(input("Podaj liczbe 2: "))
        except:
            print("podajemy tylko liczby !!!")
        else:
            break
    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("nie dzilimy przez 0")
