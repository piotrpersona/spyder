#!/usr/bin/env python3

import sys
import time
import json
import logging
import argparse

import newspaper

from scraping.factory import ScraperFactory
from topics import default_topics

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

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
    "-s",
    "--scraper",
    default="newspaper",
    choices=["newspaper", "bs4"],
    type=str,
    help="Scraper that will be used to fetch articles",
)

args = parser.parse_args()


def main():
    topics = args.topics
    scraper_name = args.scraper
    try:
        LOG.info(f"Downloading articles for topics: {topics}")

        scraper = ScraperFactory().get(scraper_name)
        LOG.info(f"Using scraper: {scraper_name}")

        LOG.info("Fetching articles")
        articles = [article._asdict() for article in scraper.scrape(topics)]
        LOG.info(f"Downloaded {len(articles)} articles")

        LOG.info(f"Writing {len(articles)} to {args.out}")
        with open(args.out, "w", encoding="utf-8") as file_handle:
            json.dump(articles, file_handle, ensure_ascii=False, indent=2)
        LOG.info(f"Done!")
    except NameError as name_error:
        LOG.error(name_error)
        sys.exit(1)
    except Exception as exception:
        LOG.error(f"Cannot process articles, err: {exception}")
        sys.exit(1)


if __name__ == "__main__":
    main()
