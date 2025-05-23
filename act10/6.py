class Restaurant:
    def __init__(self, name, cuisine_type, number_of_seats):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_of_seats = number_of_seats

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cuisine_type(self):
        return self.cuisine_type

    def set_cuisine_type(self, cuisine_type):
        self.cuisine_type = cuisine_type

    def get_number_of_seats(self):
        return self.number_of_seats

    def set_number_of_seats(self, number_of_seats):
        self.number_of_seats = number_of_seats

    def restaurant_summary(self):
        return f"Name: {self.name}, Cuisine: {self.cuisine_type}, Seats: {self.number_of_seats}"
