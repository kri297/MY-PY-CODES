func = lambda lst: list(map(lambda item: (item, item.update({"age" : item["age"] + 1}))[0], lst))

input_data = [
    {"name": "Ethan Reynolds", "age": 34},
    {"name": "Sophia Carter", "age": 27},
    {"name": "Liam Bennett", "age": 32},
    {"name": "Ava Mitchell", "age": 31},
    {"name": "Noah Simmons", "age": 29},
    {"name": "Isabella Hayes", "age": 54},
    {"name": "Mason Brooks", "age": 44},
    {"name": "Olivia Turner", "age": 41},
    {"name": "Lucas Murphy", "age": 26},
    {"name": "Emma Richardson", "age": 30}
]

print(func(input_data))