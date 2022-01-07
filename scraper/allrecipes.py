import requests
from bs4 import BeautifulSoup

class Allrecipes():
    def __init__(self, url):
        self.url = url

    def scrape(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="ingredients-section")
        ingredients = results.find_all(class_="checkbox-list")
        print(results)
        return self.parse(ingredients)

    def parse(self, ingredients):
        parsed = []
        for i in ingredients:
            curr = {}
            label = i.find(class_="checkbox-list-input")
            curr['quantity'] = label["data-init-quantity"]
            curr['unit'] = label["data-unit"]
            curr ['ingredient'] = label["data-ingredient"]
            parsed.append(curr)
        return parsed
