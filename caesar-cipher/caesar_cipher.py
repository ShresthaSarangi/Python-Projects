"""
Caesar Cipher Encryption Tool
Author: Shrestha Sarangi
Description: Encrypts and decrypts messages and text files using the Caesar Cipher technique.
"""

def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)

def main():
    while True: 
        print("=== Caesar Cipher Encryption Tool ===")
        print("1. Encrypt message")
        print("2. Decrypt message")
        choice = input("Choose option (1 or 2): ").strip()

        if choice == "1":
            text = input("Enter your message: ")

            try:
                key = int(input("Enter your key (between 1 and 25): "))
                if key < 1 or key > 25:
                    print("Key must be between 1 and 25")
                    continue
                key = key % 26
                encrypted = encrypt(text, key)
                print("\nEncrypted message: ")
                print(encrypted)

            except ValueError:
                print("Invalid key. Please enter a number.")

        elif choice == "2":
            text = input("Enter your encrypted message: ")

            try:
                key = int(input("Enter your key (between 1 and 25): "))
                if key < 1 or key > 25:
                    print("Key must be between 1 and 25")
                    continue
                key = key % 26
                decrypted = decrypt(text, key)
                print("Decrypted message: ")
                print(decrypted)

            except ValueError:
                print("Invalid key. Please enter a number.")
        else: 
            print("Invalid choice. Please select 1 or 2.")

        again = input("\nDo you want to try again? (y/n): ").lower()
        if again != "y":
            print("Program finished.")
            break

if __name__ == "__main__":
    main()