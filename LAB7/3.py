def Print_numbers(n, current=1):
    if current > n:
        return
    print(current)
    Print_numbers(n, current + 1)

num = int(input("Enter a number: "))
if num > 0:
    Print_numbers(num)
else:
    print("Please enter a positive number.")
