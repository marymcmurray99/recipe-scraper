class Ingredient:
    def __init__(self, quantity, unit, ingredient):
        self.quantity = quantity
        self.unit = unit
        self.type = ingredient 
        self.grams = None
        self.ounces = None

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
        
    
