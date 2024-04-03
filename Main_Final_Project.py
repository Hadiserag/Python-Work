from Recipe_manager import RecipeManager

def main():
    manager = RecipeManager()
    manager.load_recipes()

    while True:
        choice = manager.display_menu()

        if choice == '1':
            recipe_data = manager.ui.get_recipe_info()  
            manager.add_recipe(recipe_data)
        elif choice == '2':
            manager.search_recipe()
        elif choice == '3':
            manager.display_categories()
        elif choice == '4':
            try:
                manager.save_recipes()
                print("Recipes saved successfully.")
            except Exception as e:
                print("Error: Could not save recipes.")
                print(e)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
