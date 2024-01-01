"""
Test cases for the Flask app endpoints.
"""

import unittest
from app import app
from core import encrypt_message, decrypt_message, generate_key

class TestFlaskApp(unittest.TestCase):
    """
    Test cases for the Flask app endpoints.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        """
        Test the index route.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_generate_key_route(self):
        """
        Test the key generation route.
        """
        response = self.app.get('/generate_key')
        self.assertEqual(response.status_code, 200)

        # Assertion for key generation
        generated_key = response.data.decode('utf-8')

        # Check if the key is of the expected length
        self.assertEqual(len(generated_key), 44)

    def test_encrypt_route(self):
        """
        Test the encryption route.
        """
        # Generate a key for testing
        key = generate_key()

        # Test message to encrypt
        original_message = 'Test message'

        data = {
            'text': original_message,
            'key': key.decode('utf-8')
        }

        response = self.app.post('/encrypt', json=data)
        self.assertEqual(response.status_code, 200)

        # Assertions for encryption
        encrypted_text = response.data.decode('utf-8')

        # Decrypt the message using the same key locally
        decrypted_text = decrypt_message(encrypted_text, key)

        # Check if the original text matches the locally decrypted text
        self.assertEqual(original_message, decrypted_text)

    def test_decrypt_route(self):
        """
        Test the decryption route.
        """
        # Generate a key for testing
        key = generate_key()

        # Test message to encrypt and decrypt
        original_message = 'Test message'

        # Encrypt the message using the key
        encrypted_message = encrypt_message(original_message, key)

        data = {
            'text': encrypted_message.decode('utf-8'),
            'key': key.decode('utf-8')
        }

        response = self.app.post('/decrypt', json=data)
        self.assertEqual(response.status_code, 200)

        # Assertions for decryption
        decrypted_text = response.data.decode('utf-8')

        # Check if the decrypted text matches the original message
        self.assertEqual(decrypted_text, original_message)

if __name__ == '__main__':
    unittest.main()
