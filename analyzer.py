#!/usr/bin/env python3
import sys
import json

from scraping.scraper import Article
from topics import topics_categories


if __name__ == "__main__":
    with open(sys.argv[1]) as file_handle:
        articles = []
        for raw_article in json.load(file_handle):
            raw_article['cathegory'] = topics_categories[raw_article['cathegory']]
            articles.append(Article(**raw_article))
        with open(sys.argv[2], 'w') as out_file:
            json.dump([article._asdict() for article in articles], out_file, ensure_ascii=False, indent=2)
