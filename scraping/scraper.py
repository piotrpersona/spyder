import abc
from typing import List
from collections import namedtuple


Article = namedtuple("Article", "url title publish_date authors summary text keywords")


class Scraper(abc.ABC):
    @abc.abstractmethod
    def scrape(self, topics: List[str]) -> List[Article]:
        raise NotImplemented
