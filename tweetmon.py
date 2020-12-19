#!/usr/bin/env python3

"""
Usage:
    tweetmon.py [-w] <handle>

Options:
    -w            Number of seconds to wait for javascript to load tweets.
"""

from docopt import docopt
from scrapper import scrape_recent_tweets

import json


if __name__ == "__main__":
    args = docopt(__doc__)
    username = args['<handle>']
    tweets = scrape_recent_tweets(username)
    print(json.dumps(tweets, indent=2))
