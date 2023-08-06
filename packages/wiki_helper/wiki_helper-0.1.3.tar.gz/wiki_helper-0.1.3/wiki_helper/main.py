from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

class WikiHelper:
    def __init__(self):
        pass


    def get_links_in_page(self, page_url):
        ret = []
        parsed_uri = urlparse(page_url)
        base_url = '{}://{}'.format(parsed_uri.scheme, parsed_uri.netloc)
        r = requests.get(page_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        content_div = soup.find('div', {'id': 'mw-content-text'}).find('div', {'class': 'mw-content-ltr'})
        if content_div is None:
            print('Could not find a content div')
            return []
        for link in content_div.findChildren('a', href=True):
            href = link['href']
            if href[0] == '#':
                continue
            elif href[0] != '/':
                ret.append(href)
            else:
                ret.append('{}{}'.format(base_url, href))
        return ret

if __name__ == '__main__':
    wh = WikiHelper()
    print(wh.get_links_in_page('https://en.wikipedia.org/wiki/Category:Auxiliary_and_educational_artificial_scripts'))

