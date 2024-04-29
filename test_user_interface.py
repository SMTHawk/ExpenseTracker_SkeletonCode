import unittest
from unittest.mock import MagicMock
from user import UserInterface

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        """Setup that runs before each test."""
        # Create a mock object for the 'master' argument
        master_mock = MagicMock()
        self.user_interface = UserInterface(master_mock)

    def test_login_valid_user(self):
        """Test logging in with valid credentials."""
        expected_output = "Login successful"  # Adjust based on actual functionality
        # Assuming 'login' method requires username and password
        actual_output = self.user_interface.login_user('valid_user', 'valid_password')
        self.assertEqual(actual_output, expected_output)

    def test_login_invalid_user(self):
        """Test logging in with invalid credentials."""
        expected_output = "Login failed"  # Adjust based on actual functionality
        # Assuming 'login' method requires username and password
        actual_output = self.user_interface.login_user('invalid_user', 'wrong_password')
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
