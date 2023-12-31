import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from script import handle_user_choice

class TestHandleUserChoice(unittest.TestCase):
    # Test generate key option (choice '1')
    def test_generate_key_option(self):
        key = None
        with patch('builtins.input', side_effect=['1', '7']):  # Simulate user input '1' then '7'
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('1', key)
            
            output.seek(0)
            self.assertIn("Generated Key:", output.getvalue().strip())  # Check if key generation output is printed

    # Test invalid choice handling
    def test_invalid_choice(self):
        key = None
        with patch('builtins.input', side_effect=['8', '7']):  # Simulate user input '8' (invalid) then '7' to exit
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('8', key)
            
            output.seek(0)
            self.assertIn("Invalid choice", output.getvalue().strip())  # Check if invalid choice error message is printed

    # Test enter key option (choice '2')
    def test_enter_key_option(self):
        key = None
        with patch('builtins.input', side_effect=['2', 'mysecretkey', '7']):  # Simulate user input '2', then enter a key, then '7' to exit
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('2', key)
            
            output.seek(0)
            self.assertIn("Enter the key:", output.getvalue().strip())  # Check if prompt for key is printed

    # Test encrypt message option (choice '3')
    def test_encrypt_message_option(self):
        key = "xcazPGCMPW0nm6z5QL4e80367ZEWT2jmjToLsZLJ1zQ="
        with patch('builtins.input', side_effect=['3', 'Hello', '', '7']):  # Simulate user input '3', 'Hello', Enter, then '7' to exit
            output = StringIO()
            with patch('sys.stdout', new=output):
                handle_user_choice('3', key)
            
            output.seek(0)
            self.assertIn("Encrypted message:", output.getvalue().strip())  # Check if encryption output is printed

    # Test exit option (choice '7')
    def test_exit_option(self):
        key = None
        result = handle_user_choice('7', key)
        self.assertIsNone(result)  # Check if the function returns None upon exit

if __name__ == '__main__':
    unittest.main()
