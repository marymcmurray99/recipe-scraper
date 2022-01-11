import sqlite3
from sqlite3 import Error
import os
import json
from converter.ingredient import Ingredient

from converter.recipe import Recipe

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
            conn = sqlite3.connect("recipe_converter.db")
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return conn

    def add_or_update_recipe(self, recipe: Recipe):
        self.cursor.execute('INSERT OR REPLACE INTO recipes (url, title, instructions, ingredients) VALUES ("{url}", "{title}", {instructions}, "{ingredients}")'
        .format(url = recipe.get_url(), title = recipe.get_title(), instructions = recipe.get_instructions_json(), ingredients = recipe.get_ingredients()))
    
    # check if a recipe exists -- if it does, return Recipe otherwise return None
    def get_recipe(self, url : str) -> Recipe:
        self.cursor.execute('SELECT * FROM recipe_converter.recipies where url = {URL}'
            .format(URL = url))
        rows = self.cursor.fetchall()
        if len(rows) < 1:
            return None
        # will only be one row
        row = rows[0]
        title = row[2]
        instructions = json.loads(row[3])
        ingredients = json.loads(row[4])
        return Recipe(url, title, instructions, ingredients)
            



