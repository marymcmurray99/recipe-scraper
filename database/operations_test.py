from operations import DBOperations
from converter.recipe import Recipe
import converter.recipe
from converter.ingredient import Ingredient
import converter.ingredient

URL = "www.test.com"
TITLE = "test recipe"
INSTRUCTIONS = ['test1', 'test2', 'test3']
INGREDIENTS = [Ingredient(1, "cup", "flour"), Ingredient(1, "cup", "milk")]

def test_add_or_update_recipe():
    dbop = DBOperations()
    test_recipe = Recipe(URL, TITLE, INSTRUCTIONS, INGREDIENTS)
    # add recipe
    dbop.add_or_update_recipe(test_recipe.get_dictionary_version_with_json())
    #get recipe for testing
    recipe = dbop.get_recipe(URL)
    recipe = converter.recipe.generate_recipe_from_dictionary(recipe)
    assert(recipe.get_url() == URL)
    assert(recipe.get_title() == TITLE)
    assert(recipe.get_instructions_json() == test_recipe.get_instructions_json())
    assert(recipe.get_ingredients_json() == test_recipe.get_ingredients_json())
    #cleanup -- delete the record
    dbop.delete_recipe(URL)

def test_get_conversion():
    dbop = DBOperations()
    conversion = dbop.get_conversion("all-purpose flour")
    conversion = converter.ingredient.generate_ingredient_from_dict(conversion)
    print(conversion.get_ounces())
    assert(conversion.get_ounces() == 4.25)

if __name__ == "__main__":
    test_add_or_update_recipe()
    test_get_conversion()
    print("Everything passed")
