import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count=1, length=12):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the length of the password: "))
        password_count = int(input("Enter the number of passwords to generate: "))
        
        if password_length <= 0 or password_count <= 0:
            raise ValueError("Length and count must be positive integers.")
        
        passwords = generate_multiple_passwords(password_count, password_length)
        
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")

    except ValueError as e:
        print(f"Error: {e}")
