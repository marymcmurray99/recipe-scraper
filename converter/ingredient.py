from database.operations import DBOperations

TEASPOONS_IN_CUP = 48 
TABLESPOONS_IN_CUP = 16
TEASPOONS_IN_TABLESPOON = 3

def generate_ingredient_from_dict(ingredient: dict):
    return Ingredient(ingredient['quantity'], ingredient['unit'], ingredient['ingredient'], ingredient['grams'], ingredient['ounces'])

class Ingredient:
    def __init__(self, quantity :float, unit :str, ingredient :str, grams=None, ounces=None):
        self.quantity = quantity
        self.unit = unit
        self.ingredient = ingredient 
        self.grams = grams
        self.ounces = ounces

    def get_quantity(self):
        return self.quantity
    
    def get_unit(self):
        return self.unit
    
    def get_ingredient(self):
        return self.ingredient

    def get_grams(self):
        return self.grams

    def get_ounces(self):
        return self.ounces

    def to_json(self):
        ingredient_dict = {'quantity': self.quantity, 'unit' : self.unit, 'ingredient': self.ingredient, 'grams' : self.grams, 'ounces' : self.ounces}
        return ingredient_dict

    def calculate_grams(self):
        if self.grams:
            return
        if self.ounces:
            self.grams = self.ounces * 28.3495
            return
        #check database
        dbop = DBOperations()
        conversion = generate_ingredient_from_dict(dbop.get_conversion(self.ingredient))
        if conversion.get_unit() == self.get_unit():
            self.grams = (conversion.get_grams() * self.get_quantity()) / conversion.get_quantity()
            return 
        else:
            if conversion.get_unit().upper() == "CUP":
                new_quantity = self.to_cup()
                if new_quantity:
                    self.grams = (conversion.get_grams() * new_quantity) / conversion.get_quantity()
            elif conversion.get_unit().upper() == "TABLESPOON":
                new_quantity = self.to_tablespoon()
                if new_quantity:
                    self.grams = (conversion.get_grams() * new_quantity) / conversion.get_quantity()
            elif conversion.get_unit().upper() == "TEASPOON":
                new_quantity = self.to_teaspoon()
                if new_quantity:
                    self.grams = (conversion.get_grams() * new_quantity) / conversion.get_quantity()

    def calculate_ounces(self): 
        if self.ounces:
            return
        if self.grams:
            self.ounces = self.grams / 28.3495
            return
    
    def to_cup(self):
        if self.unit.upper() == "TEASPOON":
            return self.quantity / TEASPOONS_IN_CUP
        elif self.unit.upper() == "TABLESPOON":
            return self.quantity / TABLESPOONS_IN_CUP
        else: 
            return None
    
    def to_tablespoon(self):
        if self.unit.upper() == "TEASPOON":
            return self.quantity / TEASPOONS_IN_TABLESPOON
        elif self.unit.upper() == "CUP":
            return self.quantity * TABLESPOONS_IN_CUP
        else: 
            return None
    
    def to_teaspoon(self):
        if self.unit.upper() == "TABLESPOON":
            return self.quantity * TEASPOONS_IN_TABLESPOON
        elif self.unit.upper() == "CUP":
            return self.quantity * TABLESPOONS_IN_CUP
        else: 
            return None
        
    
