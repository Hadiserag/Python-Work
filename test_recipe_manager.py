
import unittest
from unittest.mock import patch
from Recipe_manager import RecipeManager

class TestRecipeManager(unittest.TestCase):

    def setUp(self):
        self.manager = RecipeManager()

    def test_load_recipes(self):
        # Test if load_recipes correctly loads recipes into the manager
        self.manager.load_recipes()
        self.assertIsInstance(self.manager.recipes, list)

    def test_add_recipe(self):
        # Test if add_recipe correctly adds a recipe to the manager
        test_recipe = {'title': 'Test Recipe', 'ingredients': ['Ingredient1', 'Ingredient2'], 'category': 'Test Category'}
        self.manager.add_recipe(test_recipe)
        self.assertIn(test_recipe, self.manager.recipes)

    @patch('user_interface.UserInterface.get_search_option', return_value='1')
    @patch('user_interface.UserInterface.get_ingredient', return_value='Ingredient1')
    @patch('user_interface.UserInterface.display_search_results')
    def test_search_recipe_by_ingredient(self, mock_display_results, mock_get_ingredient, mock_get_search_option):
        # Test searching recipes by ingredient
        self.manager.recipes = [{'title': 'Recipe1', 'ingredients': ['Ingredient1', 'Ingredient2'], 'category': 'Category1'}]
        self.manager.search_recipe()
        mock_display_results.assert_called_once()

    @patch('user_interface.UserInterface.display_categories')
    def test_display_categories(self, mock_display_categories):
        # Test display_categories method
        self.manager.recipes = [{'title': 'Recipe1', 'ingredients': ['Ingredient1', 'Ingredient2'], 'category': 'Category1'}]
        self.manager.display_categories()
        mock_display_categories.assert_called_once()

    # Additional tests for other methods can be added here

if __name__ == '__main__':
    unittest.main()
