class Shape:
    def __init__(self, num_sides, area=0):
        self.num_sides = num_sides
        self.area = area

    def get_info(self):
        return f"Sides: {self.num_sides}, Area: {self.area}"

class Triangle:
    def __init__(self, base, height):
        self.num_sides = 3
        self.base = base
        self.height = height
        self.area = 0

    def get_info(self):
        return f"Sides: {self.num_sides}, Base: {self.base}, Height: {self.height}, Area: {self.area}"

    def calculate_area(self):
        self.area = 0.5 * self.base * self.height
