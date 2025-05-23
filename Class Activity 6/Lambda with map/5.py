func = lambda lst: list(map(len, lst))

input_data = input("Enter text: ").split()
print(func(input_data))