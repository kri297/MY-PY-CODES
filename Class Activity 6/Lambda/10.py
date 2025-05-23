func = lambda string: "".join(x for x in string if x.lower() not in ('a', 'e', 'i', 'o', 'u'))

input_data = input("Enter text: ")
print(func(input_data))