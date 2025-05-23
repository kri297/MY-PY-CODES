filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: You do not have permission to access this file.")

except IsADirectoryError:
    print("Error: The specified path is a directory, not a file.")

except IOError as e:
    print("IO Error:", e)

except Exception as e:
    print("Unexpected error:", e)
