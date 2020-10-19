from scraping.scraper import Scraper
from scraping.newspaper import Newspaper
from scraping.bs4 import BS4


class ScraperFactory:
    @staticmethod
    def get(name: str) -> Scraper:
        if name == "newspaper":
            return Newspaper()
        elif name == "bs4":
            return BS4()
        raise NameError(f"Provided scraper `{name}` is not supported")
