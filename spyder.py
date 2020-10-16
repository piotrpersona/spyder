#!/usr/bin/env python3

import time
import json
import logging
import argparse

import newspaper

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
]

parser = argparse.ArgumentParser(description="Fetch Medium articles by topic")
parser.add_argument(
    "topics",
    metavar="TOPICS",
    type=string,
    nargs="+",
    help="List of topics to fetch articles",
    default=default_topics,
)
parser.add_argument("out", default="data.json", help="Save articles .json to a file")

args = parser.parse_args()


def fetch_articles(topics):
    articles = {}
    search_url = "https://medium.com/search?q={}"
    papers = [newspaper.build(search_url.format(topics)) for topic in topics]
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
    topics = parser.topics
    LOG.info(f"Downloading articles for topics: {topics}")
    articles = fetch_articles(topics)
    processed_articles = process_articles(articles)

    LOG.info(f"Downloaded {len(articles)} articles")

    with open(parser.out, "w", encoding="utf-8") as file_handle:
        json.dump(processed_articles, file_handle, ensure_ascii=False, indent=0)


if __name__ == "__main__":
    main()
