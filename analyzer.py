#!/usr/bin/env python3
import sys
import json

from scraping.scraper import Article


if __name__ == "__main__":
    with open(sys.argv[1]) as file_handle:
        articles = json.load(file_handle)
        categories = set([Article(**raw_article).cathegory for raw_article in articles])
        print(categories)
