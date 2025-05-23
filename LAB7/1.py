def find_max_min(sequence):
    if len(sequence) == 0:
        return "Sequence is empty"
    
    max_num = sequence[0]
    min_num = sequence[0]
    
    for num in sequence[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return max_num, min_num

user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
maximum, minimum = find_max_min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
