import unittest
from unittest.mock import patch
from user_interface import UserInterface

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.ui = UserInterface()

    @patch('builtins.input', return_value='1')
    def test_display_menu(self, mock_input):  # Accept the mock object as an argument
        choice = self.ui.display_menu()
        self.assertEqual(choice, '1')

    @patch('builtins.input', side_effect=['Test Recipe', 'Ingredient1,Ingredient2', 'Test Category'])
    def test_get_recipe_info(self, mock_input):  # Accept the mock object as an argument
        expected_info = {
            'title': 'Test Recipe',
            'ingredients': ['Ingredient1', 'Ingredient2'],
            'category': 'Test Category'
        }
        recipe_info = self.ui.get_recipe_info()
        self.assertEqual(recipe_info, expected_info)

    # Additional tests for other methods can be added here

if __name__ == '__main__':
    unittest.main()
