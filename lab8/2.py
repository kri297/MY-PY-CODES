def process_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    print(max(numbers))  
    print(sum(numbers) / len(numbers))  
    print(sum(1 for number in numbers if number > 100))  

process_numbers("numbers.txt")
