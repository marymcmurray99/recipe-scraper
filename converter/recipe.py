from os import listdir
from converter.ingredient import Ingredient
import json

def generate_recipe_from_dictionary(recipe :dict): 
    ingredients = []
    for i in recipe['ingredients']:
        ingredients.append(Ingredient(i['quantity'], i['unit'], i['ingredient'], i['grams'], i['ounces']))
    return Recipe(recipe['url'], recipe['title'], recipe['instructions'], ingredients)

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
    
    def get_ingredients_json(self):
        json_ingredients = []
        for i in self.ingredients:
            json_ingredients.append(i.to_json())
        return json.dumps(json_ingredients)
    
    def get_dictionary_version_with_json(self):
        return {'url': self.get_url(), 'title': self.get_title(), 'instructions': self.get_instructions_json(), 'ingredients': self.get_ingredients_json()}



    
        
    
