def mean(*numbers: int) -> float:
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return 0
    
inp = input("Enter numbers: ")
input_data = [int(x) for x in inp.split()]
print("The mean of the numbers is:", mean(*input_data))