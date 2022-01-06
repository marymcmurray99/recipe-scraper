import requests
from bs4 import BeautifulSoup

class Allrecipes():
    def __init__(self, url):
        self.url = url

    def scrape(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(class_="ingredients-section")
        ingredients = results.find_all("div", class_="checkbox-list")
        print(ingredients)
        return self.parse(ingredients)

    def parse(self, ingredients):
        parsed = {}
        for i in ingredients:
            curr = {}
            curr['quantity'] = i.find('data-init-quantity')
            curr['unit'] = i.find('data-unit')
            curr ['ingredient'] = i.find('data-ingredient')
            parsed.add(curr)
        return parsed
