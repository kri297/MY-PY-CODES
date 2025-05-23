def max_diff(*numbers: int) -> int:
    if numbers:
        return abs(max(numbers) - min(numbers))
    else:
        return 0
    
inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("Max difference:", max_diff(*input_data))