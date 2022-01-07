from os import listdir
from converter.ingredient import Ingredient


class Recipe:
    def __init__(self, title: str, instructions: listdir[str]):
        self.title = title
        self.instructions = instructions
        self.ingredients = []
        self.weighted_ingredients = []
    
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
    
    def calculate_weighted_ingredients(self):
        
    
