"""
Script providing a user interface for encryption and decryption operations.
"""

from core import generate_key, encrypt_message, decrypt_message, encrypt_file, decrypt_file

def generate_new_key():
    """
    Generate a new encryption key.
    
    Returns:
    - bytes: New encryption key.
    """
    key = generate_key()
    print(f"\nGenerated Key: {key.decode()}")
    return key

def enter_user_key():
    """
    Prompt user to enter a key.
    
    Returns:
    - bytes: User-entered key.
    """
    print("\nEnter the key:")
    return input().encode()

def encrypt_user_message(key):
    """
    Encrypt a user-entered message.
    
    Parameters:
    - key (bytes): Encryption key.
    """
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

def decrypt_user_message(key):
    """
    Decrypt a user-entered message.
    
    Parameters:
    - key (bytes): Decryption key.
    """
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

def encrypt_text_from_file(key):
    """
    Encrypt text from a file.
    
    Parameters:
    - key (bytes): Encryption key.
    """
    if key is None:
        print("\nPlease generate or enter a key first.")
    else:
        print("\nEnter the file path to encrypt:")
        file_path = input()
        encrypt_file(file_path, key)

def decrypt_text_from_file(key):
    """
    Decrypt text from a file.
    
    Parameters:
    - key (bytes): Decryption key.
    """
    if key is None:
        print("\nPlease generate or enter a key first.")
    else:
        print("\nEnter the file path to decrypt:")
        file_path = input()
        decrypt_file(file_path, key)

def handle_user_choice(choice, key):
    """
    Handle user choices and perform corresponding operations.
    
    Parameters:
    - choice (str): User's selected option.
    - key (bytes): Encryption/Decryption key.
    
    Returns:
    - bytes: Updated encryption/decryption key.
    """
    if choice == '1':
        key = generate_new_key()
    elif choice == '2':
        key = enter_user_key()
    elif choice == '3':
        encrypt_user_message(key)
    elif choice == '4':
        decrypt_user_message(key)
    elif choice == '5':
        encrypt_text_from_file(key)
    elif choice == '6':
        decrypt_text_from_file(key)
    else:
        print("\nInvalid choice. Please enter a valid option (1-7).")

    return key

def main():
    """
    Main function for user interaction.
    """
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
