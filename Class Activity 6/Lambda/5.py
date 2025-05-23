func = lambda string: "".join([value.upper() if index % 2 != 0 else value.lower() for index, value in enumerate(string)])

input_data = input("Enter a string: ")
print(func(input_data))