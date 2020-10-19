#!/usr/bin/env python3

import sys
import time
import json
import logging
import argparse

import newspaper

from scraping.factory import ScraperFactory

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

default_topics = [
    "natural language processing",
    "machine learning",
    "neural networks",
    "text processing",
    "python nltk",
    "python stemming",
    "python scraping",
    "deep learning",
    "lemmatize",
    "natural language",
    "python tokenizer",
    "tokenizer",
    "text classification",
    "probability concepts",
    "tensor flow" "pytorch",
    "python numpy",
    "python pandas",
    "beautiful soup python",
    "machine learning cost function",
]

parser = argparse.ArgumentParser(
    description="Fetch Medium articles by topic",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "-t",
    "--topics",
    type=str,
    nargs="+",
    help="List of topics to fetch articles",
    default=default_topics,
)
parser.add_argument(
    "-o", "--out", default="data.json", type=str, help="Save articles .json to a file"
)
parser.add_argument(
    "-s", "--scraper", default="newspaper", choices=["newspaper"], type=str, help="Scraper that will be used to fetch articles"
)

args = parser.parse_args()


def fetch_articles(topics):
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


def fetch_article_info(article):
    article.download()
    article.parse()
    article.nlp()
    return dict(
        url=article.url,
        title=article.title,
        publish_date=article.publish_date.strftime("%Y-%m-%d %H:%M:%S"),
        authors=article.authors,
        summary=article.summary,
        text=article.text,
        keywords=article.keywords,
    )


def process_articles(articles):
    return [fetch_article_info(article) for url, article in articles.items()]


def main():
    topics = args.topics
    scraper_name = args.scraper
    try:
        LOG.info(f"Downloading articles for topics: {topics}")

        scraper = ScraperFactory().get(scraper_name)
        articles = scraper.scrape(topics)

        LOG.info(f"Downloaded {len(articles)} articles")

        with open(args.out, "w", encoding="utf-8") as file_handle:
            json.dump(processed_articles, file_handle, ensure_ascii=False, indent=2)
    except NameError as name_error:
        LOG.error(name_error)
        sys.exit(1)
    except Exception as exception:
        LOG.error(f'Cannot process articles, err: {exception}')
        sys.exit(1)

if __name__ == "__main__":
    main()
