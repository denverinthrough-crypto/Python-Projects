import os
import json
from cryptography.fernet import Fernet

# Generate or load key

def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            key = key_file.read()

    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return key

key = load_key()
fernet = Fernet(key)

# Load existing passwords

def load_passwords():
    if os.path.exists("password.json"):
        with open("passwords.json", "r") as f:
            return json.load(f)
        
    return {}


# Save passwords

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)


# Add a password

def add_password():
    account = input("Account name: ")
    password = input("Paswword: ")
    encrypted_password = fernet.encrypt(password.encode()).decode()
    passwords[account] = encrypted_password
    save_passwords(passwords)
    print(f"Password for {account} saved!")

# Retrieve a password

def get_password():
    account = input("Account name to retrieve: ")
    if account in passwords:
        decrypted_password = fernet.decrypt(passwords[account].encode()).decode()
        print(f"Password for {account}: {decrypted_password}")
    else:
        print(f"No password found for  {account}")

# Main menu

passwords = load_passwords()
while True:
    print("\n1. Add Password\n2. Get Password\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        break
    else:
        print("Invalid option")