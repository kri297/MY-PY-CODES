func = lambda lst: [x for x in lst if x["email"].endswith("@gmail.com")]

input_data = [
    {"name": "Ethan Reynolds", "email": "ethan.reynolds@gmail.com"},
    {"name": "Sophia Carter", "email": "sophia.carter@yahoo.com"},
    {"name": "Liam Bennett", "email": "liam.bennett@gmail.com"},
    {"name": "Ava Mitchell", "email": "ava.mitchell@outlook.com"},
    {"name": "Noah Simmons", "email": "noah.simmons@yahoo.com"},
    {"name": "Isabella Hayes", "email": "isabella.hayes@gmail.com"},
    {"name": "Mason Brooks", "email": "mason.brooks@gmail.com"},
    {"name": "Olivia Turner", "email": "olivia.turner@yahoo.com"},
    {"name": "Lucas Murphy", "email": "lucas.murphy@gmail.com"},
    {"name": "Emma Richardson", "email": "emma.richardson@outlook.com"}
]

print(func(input_data))