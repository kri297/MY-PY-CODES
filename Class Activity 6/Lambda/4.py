func = lambda lst: [item["name"] for item in lst if item["age"] < 18]

input_data = [
    {
        "name" : "Nandu",
        "age" : 19
    },
    {
        "name" : "Viraj",
        "age" : 17
    },
    {
        "name" : "Deepak",
        "age" : 18
    },
    {
        "name" : "Rohit",
        "age" : 16
    }
]

print("Under 18:", func(input_data))