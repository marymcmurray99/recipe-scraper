from scraper.allrecipes import Allrecipes

a = Allrecipes("https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/")

x = a.scrape()

print(x)