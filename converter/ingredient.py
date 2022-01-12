import json

class Ingredient:

    def __init__(self, quantity, unit, ingredient):
        self.quantity = quantity
        self.unit = unit
        self.ingredient = ingredient 
        self.grams = None
        self.ounces = None

    def to_json(self):
        ingredient_dict = {'quantity': self.quantity, 'unit' : self.unit, 'ingredient': self.ingredient, 'grams' : self.grams, 'ounces' : self.ounces}
        return ingredient_dict

    def calculateGrams(self):
        if self.grams:
            return
        if self.ounces:
            self.grams = self.ounces * 28.3495
            return
        #check database
        
    
    def calculateOunces(self): 
        if self.ounces:
            return
        if self.grams:
            self.ounces = self.grams / 28.3495
            return
        
    
