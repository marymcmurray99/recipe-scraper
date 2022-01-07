from os import listdir
from converter.ingredient import Ingredient


class Recipe:
    def __init__(self, title: str, instructions): ## list string? instructions
        self.title = title
        self.instructions = instructions
        self.ingredients = []
    
    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)
    
        
    
