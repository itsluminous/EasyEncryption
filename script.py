from core import *

def handle_user_choice(choice, key):
    if choice == '1':
        key = generate_key()
        print(f"\nGenerated Key: {key.decode()}")
    elif choice == '2':
        print("\nEnter the key:")
        key = input().encode()
    elif choice == '3':
        if key is None:
            print("\nPlease generate or enter a key first.")
        else:
            print("\nEnter a message to encrypt (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            user_input = '\n'.join(lines)
            encrypted_message = encrypt_message(user_input, key)
            print(f"\nEncrypted message: {encrypted_message}")
    elif choice == '4':
        if key is None:
            print("\nPlease generate or enter a key first.")
        else:
            print("\nEnter the encrypted message (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            encrypted_input = '\n'.join(lines)
            decrypted_message = decrypt_message(encrypted_input.encode(), key)
            print(f"\nDecrypted message: \n{decrypted_message}")
    elif choice == '5':
        if key is None:
            print("\nPlease generate or enter a key first.")
        else:
            print("\nEnter the file path to encrypt:")
            file_path = input()
            encrypt_file(file_path, key)
    elif choice == '6':
        if key is None:
            print("\nPlease generate or enter a key first.")
        else:
            print("\nEnter the file path to decrypt:")
            file_path = input()
            decrypt_file(file_path, key)
    elif choice == '7':
        print("\nExiting the program...")
        return
    else:
        print("\nInvalid choice. Please enter a valid option (1-7).")

    return key
    
def main():
    key = None
    while True:
        print("\nChoose an action:")
        print("1. Generate Key")
        print("2. Enter Key")
        print("3. Encrypt Message")
        print("4. Decrypt Message")
        print("5. Encrypt Text from File")
        print("6. Decrypt Text from File")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("\nExiting the program...")
            break

        key = handle_user_choice(choice, key)

if __name__ == "__main__":
    main()
