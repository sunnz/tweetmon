#!/usr/bin/env python3

"""
Usage:
    tweetmon.py [-w] <handle>

Options:
    -w            Number of seconds to wait for javascript to load tweets.
"""

from docopt import docopt
from scrapper import scrape_tweet_contents


if __name__ == "__main__":
    args = docopt(__doc__)
    username = args['<handle>']
    url = f'https://twitter.com/{username}'
    tweet_contents = list(scrape_tweet_contents(url, scrolldown=5))
    print('first tweet:')
    print(tweet_contents[0])
    print()
    print('last tweet:')
    print(tweet_contents[-1])
    print()
    print(f'{len(tweet_contents)} tweets scrapped')
