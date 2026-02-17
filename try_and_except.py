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
        else:  # blok kodu ktory wykonał się poprawnie
            break
        finally:
            print("blok finally liczba 2")
    try:
        wynik = liczba1 / liczba2
        print(wynik)
    except ZeroDivisionError:
        print("nie dzilimy przez 0")


#
# Można obsługiwać konkretne typy wyjątków
# :except ValueError: zla podana wartpsc int zamiast str i tym podobne
# except ZeroDivisionError: do dzilenia przez 0
# except FileNotFoundError: do polikow
#   except IndexError: do tablic , slownikow
#
# Można też obsłużyć kilka typów naraz:
# except (TypeError, ValueError):
#
# Można również pobrać obiekt wyjątku:
# except ValueError as e:


