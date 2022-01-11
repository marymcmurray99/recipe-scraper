from converter.recipe import Recipe
import requests
from bs4 import BeautifulSoup
from converter.ingredient import Ingredient
from converter.recipe import Recipe

# Scrapes the webpage for the recipe ingredients 
# RETURNS: a recipe
def scrape_recipe(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # get directions and title 
    title = soup.find(class_="headline heading-content elementFont__display").text.strip()
    instructions = parse_instructions(soup.find_all(class_="subcontainer instructions-section-item"))
    recipe = Recipe(url, title, instructions)
    # get ingredients
    parse_ingredients(recipe, soup)
    return recipe

def parse_instructions(instructions):
    parsed = []
    for i in instructions:
        text = i.find(class_="paragraph").text.strip()
        parsed.append(text)
    return parsed

def parse_ingredients(recipe: Recipe, soup: BeautifulSoup):
    results = soup.find(class_="ingredients-section")
    ingredients = results.find_all(class_="checkbox-list")
    for i in ingredients:
        label = i.find(class_="checkbox-list-input")
        quantity = label["data-init-quantity"]
        unit = label["data-unit"]
        ingredient = label["data-ingredient"]
        curr = Ingredient(quantity, unit, ingredient)
        recipe.add_ingredient(curr)
