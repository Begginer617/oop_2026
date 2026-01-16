from hmac import digest_size


class Animal:
    def __init__(self, name, age, id):
        self.id = id  # 123 / #234
        self.name = name
        self.age = age

    def robi_kupe(self):
        print("robi kupe")


class Pies(Animal):

    def __init__(self, dog_size, weight, name, age, id):
        super().__init__(name, age, id)
        self.dog_size = dog_size
        self.weight = weight

    dog_size = ["big", "medium", "small"]

    def voice(self, voice_text):
        print(f"{voice_text}")

    def merda_ogonem():
        print("merda ogonem")


class Kot(Animal):
    def voice(self, voice_text):
        print(f"{voice_text}")


Mruczus_kot = Kot("Mruczus", 2, 33,)

Zenek_kot = Kot("zenek", 1, 654)
Zenek_kot.voice("miał miał")

Grubcio_pies = Pies('small', 78, "Grubcio", 2, 555)
Grubcio_pies.voice("haw haw haw")
print(Grubcio_pies.dog_size[0])
