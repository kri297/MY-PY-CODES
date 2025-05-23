class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car:
    def __init__(self, make, model, year, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.num_doors = num_doors

    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Doors: {self.num_doors}"

    def get_doors(self):
        return f"Number of doors: {self.num_doors}"
