from user_interface import UserInterface
from data_handling import DataHandler

class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.ui = UserInterface()
        self.data_handler = DataHandler()

    def load_recipes(self):
        self.recipes = self.data_handler.load_data()

    def add_recipe(self, recipe_data):
        self.recipes.append(recipe_data)

    def search_recipe(self):
        search_option = self.ui.get_search_option()
        if search_option == '1':
            ingredient = self.ui.get_ingredient()
            results = [recipe for recipe in self.recipes if ingredient in recipe['ingredients']]
        elif search_option == '2':
            category = self.ui.get_recipe_category()  
            results = [recipe for recipe in self.recipes if category.lower() == recipe['category'].lower()]
        else:
            print("Invalid search option.")
            return
        self.ui.display_search_results(results)

    def display_categories(self):
        unique_categories = set(recipe['category'] for recipe in self.recipes)  
        self.ui.display_categories(unique_categories)

    def save_recipes(self):
        self.data_handler.save_data(self.recipes)

    def display_menu(self):
        return self.ui.display_menu()
