class Student:
    def __init__(self, name, id_number, grades):
        self.name = name
        self.id_number = id_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def grade_summary(self):
        return f"Name: {self.name}, ID: {self.id_number}, Grades: {self.grades}, Average: {self.average_grade()}"
