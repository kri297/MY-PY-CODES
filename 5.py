def flatten(*lists: list[int]) -> list[int]:
    output = []
    for lst in lists:
        for item in lst:
            output.append(item)

    return output

n = int(input("How many lists to use: "))
if n <= 1:
    print("Number must be greater than 1")
lists = []

for _ in range(n):
    inp = input("Enter numbers: ")
    numbers = list(int(x) for x in inp.split())
    lists.append(numbers)

print("Flattened list: ", flatten(*lists))