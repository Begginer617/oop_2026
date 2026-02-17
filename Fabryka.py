class Fabryka:
    def __init__(self, antiinfantry, antitank):
        self.antiinfantry = antiinfantry
        self.antitank = antitank

    def produkuj_rpg(self):
        print("Produkuję RPG o parametrach:")
        print(f" - przeciwpiechotne: {self.antiinfantry}")
        print(f" - przeciwpancerne: {self.antitank}")


