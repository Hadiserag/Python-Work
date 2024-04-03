class UserInterface:
    def display_menu(self):
        print("Recipe Organizer Menu:")
        print("1. Add Recipe")
        print("2. Search Recipe")
        print("3. Display Categories")
        print("4. Exit")
        return input("Enter your choice: ")

    def get_recipe_info(self):
        title = input("Recipe Title: ")
        ingredients = input("Ingredients (comma-separated): ").split(',')
        category = input("Category: ")
        return {"title": title, "ingredients": ingredients, "category": category}

    def get_search_option(self):
        print("Search by:")
        print("1. Ingredient")
        print("2. Category")
        return input("Enter your choice: ")

    def get_ingredient(self):
        return input("Enter ingredient to search: ")

    def get_recipe_category(self): 
        return input("Enter category to search: ")

    def display_search_results(self, results):
        if not results:
            print("No recipes found.")
        else:
            print("Search results:")
            for idx, recipe in enumerate(results, start=1):
                print(f"{idx}. {recipe['title']} - {recipe['category']}")

    def display_categories(self, unique_categories):  
        print("Categories:")
        for category in unique_categories:
            print(f"- {category}")

