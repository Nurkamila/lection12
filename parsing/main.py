import requests
from bs4 import BeautifulSoup as BS

# Nastya
base_url = 'https://24.kg'

def get_soup(url):
    if url.startswith('https'):
        html = requests.get(url).text
    else:
        html = requests.get(base_url + url).text

    soup = BS(html, 'html.parser')
    return soup

def get_categories():
    soup = get_soup(base_url)
    cat_block = soup.find('ul', {'class': 'nav navbar-nav'})
    a_tags = cat_block.find_all('a')
    return [tag.get('href') for tag in a_tags]

def get_news_title(cat_url):
    soup = get_soup(base_url + cat_url)
    title_divs = soup.find_all('div', {'class': 'one'})
    return [div.find('a').get('href') for div in title_divs]

def get_news_article(news_url):
    soup = get_soup(news_url)
    article_block = soup.find('div', {'itemprop': 'articleBody'})
    if article_block:
        return article_block.text

def main():
    all_news = []

    # получаем список с ссылками на все категории
    categories_urls = get_categories()
    # проходимся по каждой ссылке
    for category_url in categories_urls:
        print(category_url)
        # получаем все заголовки по данной категории
        news_urls = get_news_title(category_url)
        for n_url in news_urls:
            # получаем текст одной новости
            res_text = get_news_article(n_url)
            all_news.append(res_text)

    return all_news

print(main())