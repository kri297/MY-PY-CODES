func = lambda lst: list(filter(lambda string: "a" in string.lower(), lst))

input_data = input("Enter text: ").split()
print(func(input_data))