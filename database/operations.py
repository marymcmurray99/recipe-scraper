import sqlite3
from sqlite3 import Error
import json

# Database operations for recipe_converter database

CONNECTION = None

class DBOperations:
    def __init__(self):
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()
    
    #for testing
    def get_connection(self):
        return self.connection
    
    #for testing
    def get_cursor(self):
        return self.cursor

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect("database/recipe_converter.db")
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return conn

    def add_or_update_recipe(self, recipe): # recipe should be of format Recipe.get_dictionary_version_with_json()
        query = 'INSERT OR REPLACE INTO recipes (url, title, instructions, ingredients) VALUES (:url, :title, :instructions, :ingredients)'
        print(query)
        try:
            self.cursor.execute(query, {"url" : recipe['url'], "title" : recipe['title'], "instructions" : recipe['instructions'], "ingredients" : recipe['ingredients']})
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])


    # check if a recipe exists -- if it does, return dictionary or recipe values otherwise return None
    def get_recipe(self, url : str):
        try:
            self.cursor.execute('SELECT * FROM recipes where url = :url', {"url": url})
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        rows = self.cursor.fetchall()
        if len(rows) < 1:
            return None
        # will only be one row
        row = rows[0]
        title = row[1]
        instructions = json.loads(row[2])
        ingredients = json.loads(row[3])
        return {'url': url, 'title': title, 'instructions': instructions, 'ingredients': ingredients}
            
    def delete_recipe(self, url: str):
        try:
            self.cursor.execute('DELETE FROM recipes where url = :url', {"url": url})
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    
    def get_conversion(self, ingredient :str):
        split = ingredient.split()
        rows = []
        try:
            for word in enumerate(split):
                curr = self.cursor.execute('SELECT * FROM conversions WHERE UPPER(ingredient) LIKE UPPER("%{ingredient}%")'.format(ingredient = ingredient))
                rows.extend(curr)
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])

        # find best match result 
        best_match = None
        num_matches = 0
        for row in rows:
            curr_matches = 0
            for word in split:
                if word.upper() in row[0].upper():
                    curr_matches += 1
            if curr_matches > num_matches:
                num_matches = curr_matches
                best_match = row
        
        return {'quantity': best_match[1], 'unit': best_match[2], 'ingredient': best_match[0], 'grams': best_match[4], 'ounces': best_match[3]}

                


