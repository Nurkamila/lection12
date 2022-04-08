# Web Scraping - 
# Web Crowling - пауки, которые лазают по сайтам и ищут данные
# Web Parsing - получение и обработка данных

# 'hello  '.strip()

# virtual 

# import imp
# import re
# from urllib import request
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# response = requests.get('https://amazon.com')
# print(response.text)
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print(response.cookies)
# print(response.content)
# print(response.text)

from scraping_page import get_all_links, BASE_URL
from scraping_details import get_item_details
import json

def main():
    products = []
    # получаем ссылки на все продукты
    all_products_links = get_all_links()
    
    for product_url in all_products_links:
        # получаем данные по-каждому продукту и добавляем в список
        product_details = get_item_details(product_url)
        products.append(product_details)
    print(len(products))
    
    with open('db.json', 'w', encoding='utf8') as file:
        # записываем полученный список с информацией о продуктах в файл
        json.dump(products, file, ensure_ascii=False)

if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup as BS
import requests

def get_html(url):
    response = requests.get(url)
    print(response.status_code)


def main():
    accessories_url = 'https://kg.wildberries.ru/catalog/aksessuary/bizhuteriya?sort=popular'
    pages = '&page='