from scraping.scraper import Scraper
from scraping.newspaper import Newspaper


class ScraperFactory:
    @staticmethod
    def get(name: str) -> Scraper:
        if name == "newspaper":
            return Newspaper()
        raise NameError(f"Provided scraper `{name}` is not supported")
