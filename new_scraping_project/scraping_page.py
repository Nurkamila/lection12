import time
import requests
from bs4 import BeautifulSoup
from helpers import get_attr_value, get_tags, is_disabled 

# find - return soup object
# find_all() - return list(python list) of find object

BASE_URL = 'https://kivano.kg'

def get_last_page():
    html = get_html(BASE_URL + '/elektronika')
    soup = BeautifulSoup(html, 'html.parser')
    last_page = soup.find('li', {'class':'last'}).text
    return last_page

def get_html(url):
    """Получает ссылку и возвращает его структуру html в виде текста"""
    sleep = 1
    while True:
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            print(f'Error Http Connection and time sleep {sleep} seconds')
            time.sleep(sleep)
            sleep += 3

def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links_container = soup.find('div', attrs = {'class': 'list-view'})
    res = links_container.find_all('div', attrs = {'class': 'listbox_title'})
    list_of_a = get_tags(res, 'a', attrs={})
    return list_of_a

def get_all_links():
    all_links= []
    last_page = get_last_page()
    url = BASE_URL + '/elektronika?page={}'

    # проходимся по каждой странице
    for page in range(115, (int(last_page) + 1)):
        html = get_html(url.format(page))
        print(page)
        # добавляем в список новые ссылки на продукты
        all_links += get_links(html)
        return all_links


    # while status:
    #     print(count)
    #     url = BASE_URL + "/elektronika?page={}"
    #     html = get_html(url.format(count))
    #     all_links.append(get_links(html))
    #     count += 1
    #     if is_disabled(html):
    #         break

if __name__ == '__main__':
    print(get_all_links())


# links = get_links(html)