func = lambda lst: [x for x in lst if x.startswith("a")]

input_data = input("Enter some text: ").split()
print(func(input_data))