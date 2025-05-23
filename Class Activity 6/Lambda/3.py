func = lambda lot: [first * second for (first, second) in lot]

input_data = [(10, 20), (30, 40), (50, 60)]
print("Input:", input_data)
print("Output:", func(input_data))