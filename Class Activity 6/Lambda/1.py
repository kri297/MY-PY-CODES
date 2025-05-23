func = lambda x: [num ** 2 for num in x]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))