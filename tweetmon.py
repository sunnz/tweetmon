#!/usr/bin/env python3

"""
Usage:
    tweetmon.py [-w] <handle>

Options:
    -w            Number of seconds to wait for javascript to load tweets.
"""

from docopt import docopt
from scrapper import scrape_recent_tweets
import schedule
import time
import datetime


def tweetmon(username):
    print(f'Searching for five most recent tweets from {username}')
    tweets = scrape_recent_tweets(username)
    print_tweets(tweets)
    print(datetime.datetime.now().isoformat())

def print_tweets(tweets):
    print('=================================')
    print("\n----------------\n".join(tweets))
    print('=================================')

if __name__ == "__main__":
    args = docopt(__doc__)
    username = args['<handle>']
    schedule.every(10).minutes.do(tweetmon, username=username)
    # run first one straight away before running every ten minutes
    tweetmon(username)

    while True:
        schedule.run_pending()
        time.sleep(1)
