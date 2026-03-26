'''
# 🔐 Secure Offline Password Vault
A simple command-line password manager built in Python to securely store, view, and manage credentials locally.
import os

Author : Shrestha Sarangi
'''
import base64
import os
#This uses base64 encoding, not real encryption (for learning purposes)

VAULT_FILE = "vault.txt"

#Encoding and Decoding the data
def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

#Checking the password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any (c.isupper() for c in password)
    has_digit = any (c.isdigit() for c in password)
    has_special = any (c in "!@#$%&*.,()<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_special])
    return["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]

#User interface
def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    strength = check_password_strength(password)

    line = f"{website}|{username}|{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(encoded_line + "\n")

    print("✅ Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found.")
        return

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("|")
            hidden_password = '*' * len(password)
            print(f"{website} | {username.title()} | {hidden_password}")

def update_password():
    website = input("Enter website: ").strip()
    new_password = input("Enter new password: ").strip()

    lines = []

    with open(VAULT_FILE, "r") as f:
        for line in f:
            decoded = decode(line.strip())
            w, u, p = decoded.split("|")

            if w == website:
                new_line = f"{w}|{u}|{new_password}"
                lines.append(encode(new_line))
            else:
                lines.append(line.strip())

    with open(VAULT_FILE, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print("✅ Password updated")

def main():
    while True:
        print("===🔐 Credential Manager===")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Update Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1": add_credential()
            case "2": view_credentials()
            case "3": update_password()
            case "4": break
            case _: print("Invalid choice.")

if __name__ == "__main__":
    main()
    