from os import listdir
from converter.ingredient import Ingredient
import json


class Recipe:
    def __init__(self, url :str, title: str, instructions, ingredients=[]): ## list string? instructions
        self.url = url
        self.title = title
        self.instructions = instructions
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def get_url(self):
        return self.url
    
    def get_title(self):
        return self.title
    
    def get_instructions_json(self): 
        return json.dumps(self.instructions)
    
    def get_ingredients(self):
        return self.ingredients.copy()


    
        
    
