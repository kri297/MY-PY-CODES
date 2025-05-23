def Sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

num = int(input("Enter a positive integer: "))
if num > 0:
    result = Sum_of_cubes(num)
    print("Sum of cubes:", result)
else:
    print("Please enter a positive integer.")
