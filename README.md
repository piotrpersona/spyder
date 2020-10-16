# spyder

Crawler fetching Medium article infos based on provided topics.

```bash
./spyder.py -h                                                                                                      (base) 22:29:02
usage: spyder.py [-h] TOPICS [TOPICS ...] out

Fetch Medium articles by topic

positional arguments:
  TOPICS      List of topics to fetch articles
  out         Save articles .json to a file

optional arguments:
  -h, --help  show this help message and exit
```

Fetch articles of title `nlp` and save to `data.json`:

```bash
./spyder.py -t nlp
```

or save to `/path/to/articles.json`:

```bash
./spyder.py -t nlp -o /path/to/articles.json
```
