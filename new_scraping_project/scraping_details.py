# Название
# описание
# цена
# фотка

from scraping_page import get_html
from bs4 import BeautifulSoup

# links_on_products = get_all_links()

def get_item_details(url):
    data = {}
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    # ищем title
    title = soup.find('h1').text
    data['title'] = title

    # ищем описание
    desc_div = soup.find('div', {'class': 'shop_text'})
    desc = desc_div.find('span', {'itemprop': 'description'}).text
    data['description'] = desc

    # ищем цену
    price = soup.find('span', {'itemprop':'price'}).text.strip()
    data['price'] = price

    img_div = soup.find('div', {'class': 'img_full'})
    img = img_div.find('img').get('content')
    data['photo'] = img

    return data

res = get_item_details('https://www.kivano.kg/product/view/televizionnaya-pristavka-iptv-wrtech-wr330')
print(res)