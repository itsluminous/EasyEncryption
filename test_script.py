"""
Tests cases to check if user choices are handled correctly.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from script import handle_user_choice

class TestHandleUserChoice(unittest.TestCase):
    """
    Test cases for handle_user_choice function in script.py.
    """

    def test_generate_key_option(self):
        """Test generate key option (choice '1')."""
        key = None
        # Simulate user input '1' then '7'
        with patch('builtins.input', side_effect=['1', '7']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('1', key)

            output.seek(0)
            # Check if key generation output is printed
            self.assertIn("Generated Key:", output.getvalue().strip())

    def test_invalid_choice(self):
        """Test invalid choice handling."""
        key = None
        # Simulate user input '8' (invalid) then '7' to exit
        with patch('builtins.input', side_effect=['8', '7']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('8', key)

            output.seek(0)
            # Check if invalid choice error message is printed
            self.assertIn("Invalid choice", output.getvalue().strip())

    def test_enter_key_option(self):
        """Test enter key option (choice '2')."""
        key = None
        # Simulate user input '2', then enter a key, then '7' to exit
        with patch('builtins.input', side_effect=['2', 'mysecretkey', '7']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('2', key)

            output.seek(0)
            # Check if prompt for key is printed
            self.assertIn("Enter the key:", output.getvalue().strip())

    def test_encrypt_message_option(self):
        """Test encrypt message option (choice '3')."""
        key = "xcazPGCMPW0nm6z5QL4e80367ZEWT2jmjToLsZLJ1zQ="
        # Simulate user input '3', 'Hello', Enter, then '7' to exit
        with patch('builtins.input', side_effect=['3', 'Hello', '', '7']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('3', key)

            output.seek(0)
            # Check if encryption output is printed
            self.assertIn("Encrypted message:", output.getvalue().strip())

    def test_exit_option(self):
        """Test exit option (choice '7')."""
        key = None
        result = handle_user_choice('7', key)
        # Check if the function returns None upon exit
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
