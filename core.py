"""
Core module providing encryption and decryption functionalities.
"""

from cryptography.fernet import Fernet

def generate_key():
    """Generate a Fernet key."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    """Decrypt an encrypted message using the provided key."""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted

def encrypt_file(file_path, key):
    """Encrypt a file using the provided key."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            encrypted_content = encrypt_message(content, key)
            with open(file_path + '.enc', 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)
            print(f"\nFile '{file_path}' encrypted successfully.")
    except FileNotFoundError:
        print("\nFile not found.")

def decrypt_file(file_path, key):
    """Decrypt an encrypted file using the provided key."""
    try:
        with open(file_path, 'rb', encoding='utf-8') as file:
            encrypted_content = file.read()
            decrypted_content = decrypt_message(encrypted_content, key)
            decrypted_file_path = file_path[:-4]  # Remove the '.enc' extension
            with open(decrypted_file_path, 'w', encoding='utf-8') as decrypted_file:
                decrypted_file.write(decrypted_content)
            print(f"\nFile '{file_path}' decrypted successfully.")
    except FileNotFoundError:
        print("\nFile not found.")
    except ValueError:
        print("\nInvalid decryption key or file content.")
