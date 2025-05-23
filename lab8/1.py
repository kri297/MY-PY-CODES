def process_names(file_name):
    with open(file_name, 'r') as file:
        names = [name.strip() for name in file.readlines()]

    print(len(names))  
    print(sum(1 for name in names if name[0].lower() in "aeiou"))
    print(max(names, key=len)) 

process_names("name.txt")
