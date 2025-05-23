func = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))