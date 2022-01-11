from operations import DBOperations
from converter.recipe import Recipe
from converter.ingredient import Ingredient

URL = "www.test.com"
TITLE = "test recipe"
INSTRUCTIONS = ["test1", "test2", "test3"]
INGREDIENT = Ingredient(1, "cup", "flour")

def test_add_or_update_recipe():
    dbop = DBOperations()
    test_recipe = Recipe(URL, TITLE, INSTRUCTIONS)
    test_recipe.add_ingredient(INGREDIENT)
    dbop.add_or_update_recipe(test_recipe)
    recipe = dbop.get_recipe(URL)
    assert(recipe.get_url() == URL)
    assert(recipe.get_title() == TITLE)

if __name__ == "__main__":
    test_add_or_update_recipe()
    print("Everything passed")
