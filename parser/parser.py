from handler.html_handler import *


def parse(leaks, url):
    # Check connection and parse all pages
    html = get_tor_html(url)
    result = None
    if html.status_code == 200:
        last_page = get_pages_count(html)
        for page in range(1, last_page):
            print(f'Parse page {page} of {last_page}...')
            html = get_tor_html(url + '/page/' + str(page))
            result = get_content(html, page, leaks, url)

    else:
        print('Error connection')
    return result
