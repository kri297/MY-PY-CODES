def print_info(**kwargs: str) -> None:
    for k, v in kwargs.items():
        print(f"{k}: {v}")

n = int(input("Enter number of key value pairs: "))
if n < 1:
    print("Number should be 1 or greater!")
    exit(-1)

pairs = {}
print("Enter key value pairs separated by `:` (colon)")

for _ in range(n):
    inp = input("> ")
    if ":" not in inp:
        print("Invalid key value pair!")
        exit(-1)
    
    key, value = inp.split(":", 1)
    pairs[key.strip()] = value.strip()

print_info(**pairs)    