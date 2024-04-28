import unittest
from user import UserInterface

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        """Setup that runs before each test."""
        self.user_interface = UserInterface()

    def test_login_valid_user(self):
        """Test logging in with valid credentials."""
        expected_output = "Login successful"  # Adjust based on actual functionality
        actual_output = self.user_interface.login('valid_user', 'valid_password')
        self.assertEqual(actual_output, expected_output)

    def test_login_invalid_user(self):
        """Test logging in with invalid credentials."""
        expected_output = "Login failed"  # Adjust based on actual functionality
        actual_output = self.user_interface.login('invalid_user', 'wrong_password')
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
