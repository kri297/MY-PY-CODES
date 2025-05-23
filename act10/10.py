# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Derived class
class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major

    def get_major(self):
        return f"Major: {self.major}"
