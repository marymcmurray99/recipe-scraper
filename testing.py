import importlib

a = importlib.import_module("converter.scraper." + "allrecipes")
a.scrape_recipe("https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/")