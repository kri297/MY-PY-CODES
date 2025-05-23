def generate_password(length):
    legal_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    password = []
    # Ensure at least one character from each category is included
    password.append('A')  # Uppercase
    password.append('a')  # Lowercase
    password.append('1')  # Digit
    password.append('@')  # Special character
    # Fill the rest of the password
    for i in range(length - 4):
        password.append(legal_chars[i % len(legal_chars)])
    # Convert list to string
    return ''.join(password)

def validate_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()" for c in password)
    return has_upper and has_lower and has_digit and has_special

def main():
    choice = input("Enter 'generate' to create a password or 'validate' to check a password: ").lower()
    if choice == 'generate':
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
        if validate_password(password):
            print("Password is valid.")
        else:
            print("Password is invalid.")
    elif choice == 'validate':
        password = input("Enter the password to validate: ")
        if validate_password(password):
            print("Password is valid.")
        else:
            print("Password is invalid.")
    else:
        print("Invalid choice. Please enter 'generate' or 'validate'.")

if __name__ == "__main__":
    main()
