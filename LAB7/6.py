Find_Max_Min = lambda numbers: (max(numbers), min(numbers))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = Find_Max_Min(numbers)
print("Max and Min:", result)
