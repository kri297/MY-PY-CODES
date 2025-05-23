func = lambda lst: list(filter(lambda x: x > 5, lst))
func2 = lambda lst: list(map(lambda x: x if x > 5 else None, lst))

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print(func(input_data))
print(func2(input_data))