def count_values(*args: int):
    output = {}
    for item in args:
        output[item] = output.get(item, 0) + 1 
    
    print(output)

inp = input("Enter some numbers: ")
numbers = (int(x) for x in inp.split())

print(count_values(*numbers))