import requests
from bs4 import BeautifulSoup
from typing import List
from abc import ABC, abstractmethod

# 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

# Git remote set-url origin https://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@github.com/FarRza111/web_scrape_bbc_headlines


class WebCheck(ABC):
    @abstractmethod
    def get_response(self):
        pass
    @abstractmethod
    def get_soup(self):
        pass

class WEBScraper(WebCheck):
    def __init__(self, url):
        self.url = url
        self.headers: dict = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    def get_response(self)-> str:
        try:
            request = requests.get(url=self.url, headers=self.headers)
            html = request.content
            return html
        except requests.RequestException as e:
            return f'this is the error returned from response {e}'

    def get_soup(self) -> BeautifulSoup:
        htm = self.get_response()
        soup = BeautifulSoup(htm, 'html.parser')
        return soup

    def get_news_headlines(self)-> List[str]:

        headlines = []
        for he in self.get_soup().find_all('h3', class_='gs-c-promo-heading__title'):
            headline = he.contents[0]
            headlines.append(headline)
        return headlines


if __name__ == "__main__":
    cs = WEBScraper('https://www.bbc.com/news')
    # print(cs.get_response())
    # print(cs.get_soup())
    print(cs.get_news_headlines())

