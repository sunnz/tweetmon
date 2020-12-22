#!/usr/bin/env python3

"""
Usage:
    tweetmon.py [-s] <handle>

Options:
  -h --help  Show this screen.
  -s         Starts API service to dump all tweets collected so far in JSON format.

"""

from docopt import docopt
from flask import Flask
from flask import jsonify
from threading import Thread
from scrapper import scrape_recent_tweets
import schedule
import time
import datetime


# prepare flask and thread to run a simple api
app = Flask(__name__)
collected_tweets = []
app_thread = None

def tweetmon(username):
    """Calls scrapper module, continously print new tweets and updates shared memory for Simple API"""
    print(f'Searching for five most recent tweets from {username}')
    tweets = scrape_recent_tweets(username)
    print_tweets(tweets)
    collected_tweets.clear()
    collected_tweets.extend(tweets)

def print_tweets(tweets):
    print('=================================')
    print("\n----------------\n".join(tweets))
    print('=================================')
    print(datetime.datetime.now().isoformat())

def app_run():
    """Function to run flask app in a separate thread, reads collected_tweets"""
    app.run(host='0.0.0.0')
    # listening on 0.0.0.0 so that it works on local docker
    # TODO find better ways to get this to work on docker

@app.route('/', methods=['GET'])
def get_collected_tweets():
    """Reads tweets collected so far in JSON format"""
    return jsonify(collected_tweets)

if __name__ == "__main__":
    args = docopt(__doc__)
    username = args['<handle>']
    schedule.every(10).minutes.do(tweetmon, username=username)
    # run first one straight away before running every ten minutes
    tweetmon(username)
    if args['-s']:
        # creates separate thread for running the flask app
        app_thread = Thread(target=app_run)
        app_thread.start()

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except:
            break

    if app_thread is not None:
        app_thread.join()
