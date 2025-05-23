def Print_fibonacci(a, b, n):
    if n == 0:
        return
    print(a)
    Print_fibonacci(b, a + b, n - 1)

num = int(input("Enter number of terms: "))
if num > 0:
    Print_fibonacci(0, 1, num)
else:
    print("Enter a positive number.")
