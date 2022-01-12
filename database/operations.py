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
            conn = sqlite3.connect("database/recipe_converter.db")
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return conn

    def add_or_update_recipe(self, recipe: Recipe):
        query = 'INSERT OR REPLACE INTO recipes (url, title, instructions, ingredients) VALUES (:url, :title, :instructions, :ingredients)'
        print(query)
        try:
            self.cursor.execute(query, {"url" : recipe.get_url(), "title" : recipe.get_title(), "instructions" : recipe.get_instructions_json(), "ingredients" : recipe.get_ingredients_json()})
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])


    # check if a recipe exists -- if it does, return Recipe otherwise return None
    def get_recipe(self, url : str) -> Recipe:
        try:
            self.cursor.execute('SELECT * FROM recipes where url = :url', {"url": url})
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        rows = self.cursor.fetchall()
        if len(rows) < 1:
            return None
        # will only be one row
        row = rows[0]
        title = row[1]
        instructions = json.loads(row[2])
        ingredients = []
        for i in json.loads(row[3]):
            print("here")
            print(i)
            ingredients.append(Ingredient(i['quantity'], i['unit'], i['ingredient']))
        return Recipe(url, title, instructions, ingredients)
            
    def delete_recipe(self, url: str):
        try:
            self.cursor.execute('DELETE FROM recipes where url = :url', {"url": url})
            self.connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    
    #def get_conversion(ingredient :str):
     #   try:
            #self.cursor.execute('SELECT * FROM conversions where ingredient = :ingredient', {"ingredient": ingredient}) ##### how to check for ingredient ?? 
            #self.connection.commit()
      #  except sqlite3.Error as e:
      #      print("An error occurred:", e.args[0])


