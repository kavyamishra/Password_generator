import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def start():
    while True:
        choice = input("Press G to generate password and E to exit \n")
        if choice == "G":
            password_length = int(input("Enter password length: "))
            password = generate_password(password_length)
            print("Generated password:", password)
        elif choice == "E":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    start()