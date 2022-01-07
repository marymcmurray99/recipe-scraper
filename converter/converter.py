from unit import Unit
from ingredient import Ingredient
import importlib


# dictionary of website : scraper file name (without .py)
websites = {
    'www.allrecipes.com': 'allrecipies'
}

def convert(self, url: str, unit: Unit):
    # get the recipe
    recipe = get_recipe(url)

def get_recipe(url):
    #### check website and use right file 
    scraper = None
    for key, value in websites.items():
        if key in url:
            scraper = importlib.import_module("scraper." + value)


    #recipe is a Recipe from converter.recipe
    if not scraper:
        print("Not a supported website: url given " + url)
        return
    
    recipe = scraper.scrape_recipe(url)
    return recipe



    
