from converter.recipe import Recipe
import importlib
import pprint
from database.operations import DBOperations
import converter.recipe

# dictionary of website : scraper file name (without .py)
websites = {
    'www.allrecipes.com': 'allrecipes'
}

def convert(url: str, unit: str):
    # check if URL is in database 

    # get the recipe
    recipe = get_recipe(url)
    if unit.upper() == "GRAMS":
        recipe.calculate_grams()
    elif unit.upper() == "OUNCES":
        recipe.calculate_ounces()
    pprint.pprint(recipe.get_dictionary_version_with_json())


def get_recipe(url) -> Recipe:
    #### check website and use right file 
    scraper = None
    for key, value in websites.items():
        if key in url:
            scraper = importlib.import_module("converter.scraper." + value)

    #recipe is a Recipe from converter.recipe
    if not scraper:
        print("Not a supported website: url given " + url)
        return
    
    dbop = DBOperations()
    db_recipe = dbop.get_recipe(url)
    if db_recipe:
        return converter.recipe.generate_recipe_from_dictionary(db_recipe)
    else:
        recipe = scraper.scrape_recipe(url)
        return recipe



    
