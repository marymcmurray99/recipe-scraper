from ingredient import Ingredient


def test_calculate_grams():
    same_unit = Ingredient(1, "cup", "all-purpose flour")
    same_unit.calculate_grams()
    assert(same_unit.get_grams() == 120)
    different_unit = Ingredient(1, "tablespoon", "all-purpose flour")
    different_unit.calculate_grams()
    print(different_unit.get_grams())
    assert(different_unit.get_grams() == 7.5)

if __name__ == "__main__":
    test_calculate_grams()
    print("Everything passed")
