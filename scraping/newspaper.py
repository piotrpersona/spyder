import logging
from typing import List, Dict

from scraping.scraper import Scraper, Article

import newspaper

LOG = logging.getLogger(__name__)


class Newspaper(Scraper):
    def scrape(self, topics: List[str]) -> List[Article]:
        newspaper_articles = self.__fetch_articles(topics)
        articles = self.__process_articles(newspaper_articles)
        return articles

    def __fetch_articles(self, topics: List[str]):
        articles = {}
        search_url = "https://medium.com/search?q={}"
        papers = [newspaper.build(search_url.format(topic)) for topic in topics]
        newspaper.news_pool.set(papers, threads_per_source=2)
        newspaper.news_pool.join()
        for paper in papers:
            LOG.info(f"Downloading from: {paper.url}")
            for article in paper.articles:
                LOG.debug(f"Article: {article.url}")
                articles[article.url] = article
        return articles

    def __process_articles(
        self, articles: Dict[str, newspaper.Article]
    ) -> List[Article]:
        return [self.__fetch_article_info(article) for url, article in articles.items()]

    def __fetch_article_info(self, article: newspaper.Article) -> Article:
        article.download()
        article.parse()
        article.nlp()
        return Article(
            url=article.url,
            title=article.title,
            publish_date=article.publish_date.strftime("%Y-%m-%d %H:%M:%S"),
            authors=article.authors,
            summary=article.summary,
            text=article.text,
            keywords=article.keywords,
        )
