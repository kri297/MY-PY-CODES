func = lambda x: [len(s) for s in x]

input_data = input("Enter text: ").split()
print(func(input_data))