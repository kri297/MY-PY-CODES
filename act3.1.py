# Initialize data types
numeric = 123
string = "Hello, World!"
tuple_data = (1, 2, 3)
list_data = [4, 5, 6]
dictionary_data = {'a': 1, 'b': 2, 'c': 3}

# Identify the class using type function
print("Type of numeric:", type(numeric))
print("Type of string:", type(string))
print("Type of tuple:", type(tuple_data))
print("Type of list:", type(list_data))
print("Type of dictionary:", type(dictionary_data))

# Display methods using dir function
print("\nMethods supported by int:", dir(numeric))
print("\nMethods supported by str:", dir(string))
print("\nMethods supported by tuple:", dir(tuple_data))
print("\nMethods supported by list:", dir(list_data))
print("\nMethods supported by dict:", dir(dictionary_data))
# Implement methods

# For numeric (int)
print("\nInteger methods:")
print("Bit length:", numeric.bit_length())
print("To bytes:", numeric.to_bytes(2, byteorder='big'))
print("Conjugate:", numeric.conjugate())
print("Numerator:", numeric.numerator)
print("Denominator:", numeric.denominator)

# For string (str)
print("\nString methods:")
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Title:", string.title())
print("Replace:", string.replace("Hello", "Hi"))
print("Split:", string.split())

# For tuple
print("\nTuple methods:")
print("Count of 1:", tuple_data.count(1))
print("Index of 2:", tuple_data.index(2))
print("Length of tuple:", len(tuple_data))
print("Sum of elements:", sum(tuple_data))
print("Tuple concatenation:", tuple_data + (4, 5))

# For list
print("\nList methods:")
list_data.append(7)
print("Append:", list_data)
list_data.extend([8, 9])
print("Extend:", list_data)
list_data.insert(1, 3.5)
print("Insert:", list_data)
list_data.remove(3.5)
print("Remove:", list_data)
print("Pop:", list_data.pop())

# For dictionary (dict)
print("\nDictionary methods:")
print("Get value for key 'a':", dictionary_data.get('a'))
dictionary_data.update({'d': 4})
print("Update:", dictionary_data)
print("Keys:", dictionary_data.keys())
print("Values:", dictionary_data.values())
print("Items:", dictionary_data.items())
