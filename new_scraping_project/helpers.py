def get_attr_value(tag, attr):
    """Получает тег и по аттрибуту возвращает значение: 
    <a href = /product/view/karta-pamyati-micro-sd-apacer-hc10-u3-v30-256gb
    target = '_blank'> 
    get_attr_value(tag, 'href') -> /link/"""
    from scraping_page import BASE_URL
    return BASE_URL + tag.get(attr)

def get_tags(ls_soup, tag_name, attrs=None):
    find_tags = []
    for tag in ls_soup:
        res = tag.find(tag_name, attrs)
        find_tags.append(get_attr_value(res, 'href'))
    return find_tags

from bs4 import BeautifulSoup

def is_disabled(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_obj = soup.find('li', attrs = {'class': 'next'})
    # next disabled
    if 'disabled' in li_obj.get('class'):
        return True
    return False