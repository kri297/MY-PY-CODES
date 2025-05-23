func = lambda lst: list(map(str.upper, lst))

input_data = input("Enter text: ").split()
print(func(input_data))