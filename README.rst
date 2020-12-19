Setup::

    pip install -r requirements.txt

Example::

    ./tweetmon.py sammyjcomedian

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
