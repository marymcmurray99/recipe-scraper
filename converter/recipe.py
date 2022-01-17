from typing import List
from converter.ingredient import Ingredient
import json
from database.operations import DBOperations


def generate_recipe_from_dictionary(recipe :dict): 
    ingredients = []
    for i in recipe['ingredients']:
        ingredients.append(Ingredient(i['quantity'], i['unit'], i['ingredient'], i['grams'], i['ounces']))
    return Recipe(recipe['url'], recipe['title'], recipe['instructions'], ingredients)

class Recipe:
    def __init__(self, url :str, title: str, instructions: List[str], ingredients: List[Ingredient] = []): ## list string? instructions
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
    
    def get_ingredients_json(self):
        json_ingredients = []
        for i in self.ingredients:
            json_ingredients.append(i.to_json())
        return json.dumps(json_ingredients, indent=2)
    
    def get_dictionary_version_with_json(self):
        return {'url': self.get_url(), 'title': self.get_title(), 'instructions': self.get_instructions_json(), 'ingredients': self.get_ingredients_json()}
    
    def calculate_grams(self): 
        for i in self.ingredients:
            i.calculate_grams()
        self.save_recipe()
        
    
    def calculate_ounces(self): 
        for i in self.ingredients:
            i.calculate_ounces()
        self.save_recipe()
    
    def save_recipe(self):
        dbop = DBOperations()
        dbop.add_or_update_recipe(self.get_dictionary_version_with_json())




    
        
    
