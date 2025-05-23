def intersection(list_1: list[int], *lists: list[int]) -> list[int]:
    output = []
    for item in list_1:
        if all(item in lst for lst in lists):
            output.append(item)

    return output

n = int(input("How many lists to use: "))
if n <= 1:
    print("Number must be greater than 1")
    exit(-1)
    
lists = []

for _ in range(n):
    inp = input("Enter numbers: ")
    numbers = list(int(x) for x in inp.split())
    lists.append(numbers)

print((*intersection(lists[0], *lists[1:])) or "Nothing in common!")