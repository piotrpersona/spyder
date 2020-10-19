# spyder

Crawler fetching Medium article infos based on provided topics.

```bash
usage: spyder.py [-h] [-t TOPICS [TOPICS ...]] [-o OUT] [-s {newspaper,bs4}]

Fetch Medium articles by topic

optional arguments:
  -h, --help            show this help message and exit
  -t TOPICS [TOPICS ...], --topics TOPICS [TOPICS ...]
                        List of topics to fetch articles (default: ['natural language processing', 'machine learning', 'neural networks', 'text processing', 'python
                        nltk', 'python stemming', 'python scraping', 'deep learning', 'lemmatize', 'natural language', 'python tokenizer', 'tokenizer', 'text
                        classification', 'probability concepts', 'tensor flowpytorch', 'python numpy', 'python pandas', 'beautiful soup python', 'machine learning
                        cost function'])
  -o OUT, --out OUT     Save articles .json to a file (default: data.json)
  -s {newspaper,bs4}, --scraper {newspaper,bs4}
                        Scraper that will be used to fetch articles (default: newspaper)
```

Fetch articles of title `nlp` and save to `data.json`:

```bash
./spyder.py -t nlp
```

or save to `/path/to/articles.json`:

```bash
./spyder.py -t nlp -o /path/to/articles.json
```

Use scraper

```bash
./spyder.py -t nlp -o /path/to/articles.json -s bs4
```
