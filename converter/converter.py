from unit import Unit
import scraper.allrecipes as allrecipes
from ingredient import Ingredient


def convert(self, url: str, unit: Unit):
    #### check website and use right file 

    #recipe is a Recipe from converter.recipe
    recipe = allrecipes.scrape_recipe(url)
    
    
