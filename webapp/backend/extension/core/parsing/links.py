from timeit import default_timer as timer
import requests
from bs4 import BeautifulSoup
import urllib
import re
import lxml


def measure_time(func):
    def wrap(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print(f'Время исполнения функции {func.__name__}: {end - start}')

    return wrap


class Links:

    def __init__(self, search_request):
        self.search_request = search_request.lower()
        self.results = []
        self.filter = ['wikipedia.org', 'sites.google.com', 'youtube.com', 'math24.ru', 'zftsh.online']

    @measure_time
    def get_links(self):
        query = self.search_request
        query = query.replace(' ', '+')
        URL = f"https://google.com/search?q={query}"
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "lxml")
            for g in soup.find_all('div', class_='yuRUbf'):
                anchors = g.find_all('a')
                if anchors:
                    counter = 0
                    link = anchors[0]['href']
                    for ex in self.filter:
                        if ex in link:
                            counter += 1
                    if counter == 0 and len(self.results) < 3:
                        self.results.append(link)


