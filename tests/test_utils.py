import unittest
from unittest.mock import mock_open, patch
from src.utils import financial_transactions

class TestFinancialTransactions(unittest.TestCase):
    def test_financial_transactions(self):
        mock_data = '{"key": "value"}'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = financial_transactions('dummy_path.json')
            self.assertEqual(result, {"key": "value"})

if __name__ == '__main__':
    unittest.main()
