func = lambda lst: (result := 1, *[result := result * x for x in lst])[-1]

inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("Product:", func(input_data))