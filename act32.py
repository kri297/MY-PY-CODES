# Numeric (int) - Immutable
numeric = 123
numeric_copy = numeric
numeric += 1
print("Original numeric:", numeric_copy)  # 123
print("Modified numeric:", numeric)       # 124

# String (str) - Immutable
string = "Hello"
string_copy = string
string += ", World!"
print("Original string:", string_copy)  # "Hello"
print("Modified string:", string)       # "Hello, World!"

# Tuple (tuple) - Immutable
tuple_data = (1, 2, 3)
tuple_copy = tuple_data
tuple_data += (4,)
print("Original tuple:", tuple_copy)  # (1, 2, 3)
print("Modified tuple:", tuple_data)  # (1, 2, 3, 4)

# List (list) - Mutable
list_data = [4, 5, 6]
list_copy = list_data[:]
list_data.append(7)
print("Original list:", list_copy)  # [4, 5, 6]
print("Modified list:", list_data)  # [4, 5, 6, 7]

# Dictionary (dict) - Mutable
dictionary_data = {'a': 1, 'b': 2, 'c': 3}
dictionary_copy = dictionary_data.copy()
dictionary_data['d'] = 4
print("Original dictionary:", dictionary_copy)  # {'a': 1, 'b': 2, 'c': 3}
print("Modified dictionary:", dictionary_data)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
