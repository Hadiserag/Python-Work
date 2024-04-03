import json

class DataHandler:
    def __init__(self, filename="recipes.json"):
        self.filename = filename

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data):
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)
        except IOError:
            raise Exception("Error: Could not save data.")
