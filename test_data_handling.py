
import unittest
from unittest.mock import patch, mock_open
from data_handling import DataHandler

class TestDataHandler(unittest.TestCase):

    def setUp(self):
        self.data_handler = DataHandler('test_recipes.json')

    @patch('builtins.open', new_callable=mock_open, read_data='[{"title": "Test Recipe"}]')
    def test_load_data(self, mock_file):
        # Test if load_data correctly loads data from a file
        data = self.data_handler.load_data()
        self.assertEqual(data, [{"title": "Test Recipe"}])
        mock_file.assert_called_with('test_recipes.json', 'r')

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_data(self, mock_json_dump, mock_file):
        # Test if save_data correctly saves data to a file
        test_data = [{"title": "Test Recipe"}]
        self.data_handler.save_data(test_data)
        mock_file.assert_called_with('test_recipes.json', 'w')
        mock_json_dump.assert_called_with(test_data, mock_file(), indent=4)

    # Additional tests for error cases and exceptions can be added here

if __name__ == '__main__':
    unittest.main()
