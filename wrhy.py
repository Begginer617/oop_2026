class KontoBankowe:
    def __init__(self, saldo):
        self.__saldo = saldo  # Prywatna


konto = KontoBankowe(1000)

#################
print(konto.__saldo)