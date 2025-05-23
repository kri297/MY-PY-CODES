func = lambda lst: list(map(lambda x: x+1, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))