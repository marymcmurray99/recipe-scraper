# recipescraper

# About this project
This project is the backend of a recipe scraper with the following functionality
- Ability to scrape a recipe from a supported website (utilizing BeautifulSoup). Currently, only AllRecipes.com is supported, but the the functionality for adding more scrapers is implemented.
- Ability to convert the ingredient amounts from the recipe to weights (grams and ounces for now) by using conversions stored in the SQLite database (database/recipe_converter.db).
- Ability to save recipes including the calculated weights to the SQLite database so they can be reused.

# Running
Running this project can be done locally from the command line so long as Python and SQLite are supported on your device. To run, clone the code and try 
```$ python run.py https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/ ounces``` 
Or run with any allrecipes link and either ounces or grams. 

# Conversions
Conversions ratios are sourced from the King Aurthur website and can be found [on this page](https://www.kingarthurbaking.com/learn/ingredient-weight-chart). 