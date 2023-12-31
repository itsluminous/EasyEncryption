import unittest
from cryptography.fernet import Fernet, InvalidToken
from io import StringIO
from core import generate_key, encrypt_message, decrypt_message

class TestCoreFunctions(unittest.TestCase):
    def test_generate_key(self):
        # Check if generate_key() returns a non-None value
        key1 = generate_key()
        key2 = generate_key()
        self.assertIsNotNone(key1)
        self.assertIsNotNone(key2)
        self.assertNotEqual(key1, key2)  # Check if consecutive keys are different
        self.assertEqual(len(key1), 44)  # Assuming Fernet key length

    def test_encrypt_decrypt(self):
        # Test encrypting and decrypting an empty string
        key = generate_key()
        empty_message = ''
        encrypted_empty = encrypt_message(empty_message, key)
        decrypted_empty = decrypt_message(encrypted_empty, key)
        self.assertEqual(empty_message, decrypted_empty)

        # Test encrypting and decrypting a string with special characters
        special_message = '!@#$%^&*()_+{}|:"<>?`-=[]\;\',./'
        encrypted_special = encrypt_message(special_message, key)
        decrypted_special = decrypt_message(encrypted_special, key)
        self.assertEqual(special_message, decrypted_special)

        # Test encrypting and decrypting a multiline string
        multiline_message = 'Line 1\nLine 2\nLine 3'
        encrypted_multiline = encrypt_message(multiline_message, key)
        decrypted_multiline = decrypt_message(encrypted_multiline, key)
        self.assertEqual(multiline_message, decrypted_multiline)

    def test_decrypt_with_incorrect_key(self):
        key = generate_key()
        incorrect_key = generate_key()  # Different key
        encrypted_message = encrypt_message('Test message', key)

        # Ensure decrypting with incorrect key raises InvalidToken
        fernet = Fernet(incorrect_key)
        with self.assertRaises(InvalidToken) as context:
            fernet.decrypt(encrypted_message)

if __name__ == '__main__':
    unittest.main()
