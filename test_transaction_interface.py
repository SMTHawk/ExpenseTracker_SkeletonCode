import unittest
from unittest.mock import MagicMock
from transaction import TransactionInterface
import sqlite3

class TestTransactionInterface(unittest.TestCase):
    def setUp(self):
        """Setup that runs before each test."""
        self.db_mock = MagicMock()
        self.master_mock = MagicMock()
        self.transaction_interface = TransactionInterface(self.master_mock, self.db_mock)

    def test_add_valid_transaction(self):
        """Test adding a valid transaction."""
        self.db_mock.execute_query.return_value = None  # execute_query should return 'None' if successful, testing this
        result = self.transaction_interface.add_transaction(1, 100.50, 'Groceries', '2021-04-21')
        self.assertEqual(result, "Transaction added successfully")

    def test_add_transaction_with_invalid_data(self):
        """Test handling of an SQL error during transaction addition."""
        self.db_mock.execute_query.side_effect = sqlite3.Error("Database error")  # Simulate a database error
        result = self.transaction_interface.add_transaction(1, None, 'Groceries', '2021-04-21')
        self.assertTrue("Error" in result)

if __name__ == '__main__':
    unittest.main()
