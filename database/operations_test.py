from operations import DBOperations
from converter.recipe import Recipe
from converter.ingredient import Ingredient
import json

URL = "www.test.com"
TITLE = "test recipe"
INSTRUCTIONS = ['test1', 'test2', 'test3']
INGREDIENTS = [Ingredient(1, "cup", "flour"), Ingredient(1, "cup", "milk")]

def test_add_or_update_recipe():
    dbop = DBOperations()
    test_recipe = Recipe(URL, TITLE, INSTRUCTIONS, INGREDIENTS)
    # add recipe
    dbop.add_or_update_recipe(test_recipe)
    #get recipe for testing
    recipe = dbop.get_recipe(URL)
    assert(recipe.get_url() == URL)
    assert(recipe.get_title() == TITLE)
    assert(recipe.get_instructions_json() == test_recipe.get_instructions_json())
    assert(recipe.get_ingredients_json() == test_recipe.get_ingredients_json())
    #cleanup -- delete the record
    dbop.delete_recipe(URL)

if __name__ == "__main__":
    test_add_or_update_recipe()
    print("Everything passed")
