func = lambda lst: [x for x in lst if x % 2 == 0]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))