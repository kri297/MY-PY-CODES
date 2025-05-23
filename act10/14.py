class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")
