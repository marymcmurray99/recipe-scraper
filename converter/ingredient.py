class Ingredient:
    def __init__(self, quantity, unit, ingredient):
        self.quantity = quantity
        self.unit = unit
        self.type = ingredient 
        self.grams = None
        self.ounces = None
        self.setGrams()
        self.setOunces()

    def setGrams(self):
        if self.grams:
            return
        if self.ounces:
            self.grams = self.ounces * 28.3495
        self.grams = 0
    
    def setOunces(self): 
        self.ounces = 0

    
