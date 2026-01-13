while True:
    try:
        liczba1= int(input("Podaj liczbe 1: "))
        liczba2= int(input("Podaj liczbe 2: "))
        wynik = liczba1 / liczba2
        print(wynik)
    except  ValueError:
        print("podajemy tylko liczby !!!")
    except  ZeroDivisionError:
        print("Nie dzielimy przez 0 !!!")