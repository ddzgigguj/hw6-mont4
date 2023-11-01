from bs4 import BeautifulSoup as BS
import requests
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.olx.uz/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_="css-qfzx1y")
    olx_products = []

    for item in items:
        olx_products.append(
            {
                'title_name': item.find("h3", class_="css-16v5mdi er34gjf0").get_text(),
                'price': item.find("p", class_="css-112xsl6 css-10b0gli er34gjf0").get_text(),
                'title_url': URL + item.find("a").get("href"),
                'image': item.find("div", class_="css-1av34ht").find("img").get("src"),
            }
        )
    return olx_products

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_products = []
        for page in range(0, 1):
            html = get_html(f'https://www.olx.uz/elektronika/telefony/', params=page)
            all_products.extend(get_data(html.text))
            return all_products
    else:
        raise Exception('Error parsing ❗️😥')