class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student:
    def __init__(self, name, age, gender, major):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Major: {self.major}"

    def get_major(self):
        return f"Major: {self.major}"
