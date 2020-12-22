Simple Python program to monitor five most recent tweets given a Twitter handle
as a command-line argument.

This is done over a weekend for fun and attempts to scrape the tweets from the
user's profile page rather than through Twitter's API to avoid authentication
with a developer account. As the tweets are downloaded into Twitter's React
frontend, this Python program needs to scrape on the JS rendered html dom tree.

Note, it will download Chromium into your home directory (e.g. ~/.pyppeteer/),
if you haven't run anything that uses pyppeteer on before. This used to execute
the Javascript that on the Twitter profile page. This will download Chromium only
once.

Setup::

    pip install -r requirements.txt

Example::

    ./tweetmon.py sammyjcomedian

Simple API service (via flask)::

    ./tweetmon.py -s sammyjcomedian
    # to build docker image and run the entire headless chromium and script in docker
    docker build -t sunnz/tweetmon .
    docker run -p 5000:5000 -it --rm sunnz/tweetmon sammyjcomedian
    # to view tweets collected so far as a JSON string
    curl http://127.0.0.1:5000/
    # see headers (to check if Content-Type is set appropriately, for example)
    curl -i http://127.0.0.1:5000/

Scope
=====

Developed on Python 3.9, should work with Python 3.6 or higher.

User authentication and Twitter developer account are out of scope, so Twitter API are not used
as all Twitter API methods now require authentication (including Search API).

Twitter to RSS and similiar third party services and open source libraries such as
Twint and Tweepy are out of the scope.

requests-html with Javascript rendering is required for scrapping the JS rendered html dom for
tweets.

Edge cases of non-existing user and users with too little or no tweets are out of the
scope in the current state, however some edge cases closer to the happy path may work.
