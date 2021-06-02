import requests
from bs4 import BeautifulSoup


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
           'accept': '*/*'}


def get_tor_html(url, params=None):
    # Connect to cite in TOR
    proxies = {'http': 'socks5h://127.0.0.1:9150',
               'https': 'socks5h://127.0.0.1:9150'}
    data = requests.get(url, headers=HEADERS, params=params, proxies=proxies)
    return data


def get_pages_count(html):
    # Count of pages of leaks on cite
    soup = BeautifulSoup(html.text, 'lxml')
    pages_count = soup.find('ul', class_='pages').find_all('a')
    last_page = int(pages_count[-1].get('href').replace('/page/', ''))
    return last_page


def get_content(html, page_count, leaks, url):
    # Get content from each page and add to leaks list
    soup = BeautifulSoup(html.text, 'lxml')
    items = soup.find_all('div', class_='card')
    for item in items:
        description = item.find('i', class_='fa-comment-dots')
        if description:
            description = description.find_next('span').get_text().replace('\r\n', '')
        else:
            description = 'No descriptions '
        leaks.append({
            'cite_page': url + '/page/' + str(page_count),
            'date': item.find('div', class_='footer').find_next('div').get_text(),
            'title': item.find('div', class_='title').get_text().replace('”', '').replace('“', ''),
            'company_url': item.find('a').get('href'),
            'description': description,
            'links': url + item.find('div', class_='footer').find_next('a').get('href'),
        })
    return leaks
