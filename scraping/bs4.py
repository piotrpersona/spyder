from typing import List, Dict

import requests
import newspaper
from bs4 import BeautifulSoup

from scraping.scraper import Scraper, Article


class BS4(Scraper):
    def scrape(self, topics: List[str]) -> List[Article]:
        search_url = "https://medium.com/search?q={}"
        search_urls = [search_url.format(topic) for topic in topics]
        for search_url in search_urls:
            topic_html = self.__fetch_html(search_url)
            articles_urls = self.__parse_articles_urls(topic_html)
            return self.__fetch_articles(articles_urls[:2])

    def __fetch_articles(self, articles_urls: List[str]) -> List[Article]:
        return [self.__fetch_article(url) for url in articles_urls]

    def __fetch_article(self, url: str) -> Article:
        html = self.__fetch_html(url)
        article = self.__parse_article(url, html)
        return article

    def __parse_article(self, url: str, html: str) -> Article:
        return Article(
            url=url,
            title=self.__parse_title(html),
            publish_date=self.__parse_publish_date(html),
            authors=self.__parse_authors(html),
            summary="",
            text=self.__parse_text(html),
            keywords=[],
        )

    @staticmethod
    def __parse_title(html):
        soup = BeautifulSoup(html,'lxml')
        title = soup.find_all('strong', class_='be')
        if len(title) > 0:
            return title[0].text
        title = soup.find('h1')
        if title:
            return title.text
        return ""

    @staticmethod
    def __parse_publish_date(html):
        soup = BeautifulSoup(html, 'html.parser')
        publish_date = soup.find_all('span', class_='gb')
        if len(publish_date) > 0:
            return publish_date[0].text
        publish_date = soup.find_all('span', class_='bb b bc bd cc gt cb gu gv gw gx be')
        if len(publish_date) > 0:
            pd = publish_date[0]
            print(pd)
            div = pd.get("div")
            a = div.get("a") if div else None
            return a.text if a else ""
        return ""

    @staticmethod
    def __parse_authors(html):
        soup = BeautifulSoup(html, 'html.parser')
        authors = []
        parsed = soup.find_all('img', {'width': 48, 'height': 48})
        if len(parsed) > 0:
            name = parsed[0].get('alt')
            authors.append(name)
        return authors

    @staticmethod
    def __parse_text(html):
        soup = BeautifulSoup(html, 'lxml')
        parsed = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'li'])
        return ' '.join([par.text for par in parsed if par])


    @staticmethod
    def __fetch_html(search_url: str) -> str:
        response = requests.get(search_url)
        return response.text

    @staticmethod
    def __parse_articles_urls(topic_html: str) -> List[str]:
        urls = []
        soup = BeautifulSoup(topic_html, 'html.parser')
        for a in soup.find_all('a', {'data-action': 'open-post'}, href=True):
            href = a.get('href')
            if href:
                urls.append(href)
        return list(set(urls))
