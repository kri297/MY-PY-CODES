def q1_max_min():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    maximum = minimum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    print("Max:", maximum)
    print("Min:", minimum)

def q2_sum_of_cubes():
    n = int(input("Enter a positive integer: "))
    total = 0
    for i in range(1, n):
        total += i**3
    print("Sum of cubes less than", n, "is", total)

def q3_print_1_to_n():
    def print_numbers(n, current=1):
        if current > n:
            return
        print(current)
        print_numbers(n, current + 1)

    n = int(input("Enter a number: "))
    print_numbers(n)

def q4_fibonacci():
    def fib(a, b, n):
        if n == 0:
            return
        print(a)
        fib(b, a + b, n - 1)

    terms = int(input("Enter number of Fibonacci terms: "))
    fib(0, 1, terms)

def q5_volume_of_cone():
    volume_of_cone = lambda r, h: (1/3) * 3.14 * r**2 * h
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    print("Volume of cone:", volume_of_cone(r, h))

def q6_max_min_lambda():
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    find_max_min = lambda lst: (max(lst), min(lst))
    print("Max and Min:", find_max_min(nums))

def q7_argument_types():
    def roast(name, reason):
        print(f"{name}, you're being roasted because: {reason}")

    def wake_up(name, alarm="at noon"):
        print(f"{name}, please wake up {alarm} 😴")

    def rant(*problems):
        print("Okay, here comes the rant:")
        for p in problems:
            print("😤", p)
        print("Done. I feel better now.")

    print("\na. Keyword Argument – Roast someone")
    print("b. Default Argument – Wake-up call")
    print("c. Variable-Length Argument – Rant session")
    sub = input("Choose a sub-option (a/b/c): ")

    if sub == 'a':
        name = input("Enter name: ")
        reason = input("Reason to roast: ")
        roast(reason=reason, name=name)

    elif sub == 'b':
        name = input("Enter sleepyhead's name: ")
        alarm = input("When should they wake up? (press Enter for default): ")
        if alarm.strip() == "":
            wake_up(name)
        else:
            wake_up(name, alarm)

    elif sub == 'c':
        print("Tell me all your problems. Type 'done' to stop.")
        problems = []
        while True:
            p = input("> ")
            if p.lower() == "done":
                break
            problems.append(p)
        rant(*problems)

    else:
        print("Wrong choice. Back to main menu!")

def show_menu():
    print("\n🎉 Python Concept Comedy Menu 🎉")
    print("1. Max and Min without built-in functions")
    print("2. Sum of cubes less than a number")
    print("3. Print 1 to n using recursion")
    print("4. Print Fibonacci series using recursion")
    print("5. Volume of cone using lambda (with 3.14)")
    print("6. Tuple of max and min using lambda")
    print("7. Keyword, Default & Variable-Length Arguments (funny)")
    print("8. Exit")

while True:
    show_menu()
    choice = input("Pick your topic (1-8): ")

    if choice == '1':
        q1_max_min()
    elif choice == '2':
        q2_sum_of_cubes()
    elif choice == '3':
        q3_print_1_to_n()
    elif choice == '4':
        q4_fibonacci()
    elif choice == '5':
        q5_volume_of_cone()
    elif choice == '6':
        q6_max_min_lambda()
    elif choice == '7':
        q7_argument_types()
    elif choice == '8':
        print("Okay bye! Keep coding and don't forget to laugh 😄")
        break
    else:
        print("Invalid choice! Try again.")
