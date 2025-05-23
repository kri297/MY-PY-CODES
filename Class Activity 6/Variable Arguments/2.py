def concatenate(*strings: str) -> str:
    output = ""
    for s in strings:
        output += s
    
    return output

inp = input("Enter a sentence: ")
print(concatenate(*inp.split()))