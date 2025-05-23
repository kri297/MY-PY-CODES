func = lambda lst: list(filter(lambda string: len(string) >= 5, lst))

input_data = input("Enter text: ").split()
print(func(input_data))