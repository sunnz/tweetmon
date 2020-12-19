#!/usr/bin/env python3

from requests_html import HTMLSession


SLEEP=5
MAX_NUMBER_OF_SCROLLDOWNS=5
SESSION = HTMLSession()

def scrape_recent_tweets(username, count=5):
    """
    Scrapes tweet from a twitter's user profile until getting count number of tweets.

    Each time scrolls down a little in the browser to get more tweets from the html dom tree.
    Will keep trying until getting count number of tweets or reaching MAX_NUMBER_OF_SCROLLDOWNS.

    Parameters
    ----------
    username : string
        Twitter username
    count : int
        Number of tweets to scrape

    Returns
    -------
    list
        A list of tweet strings ordered by most recent first.

    """
    tweets = []
    url = f'https://twitter.com/{username}'

    for scrolldown in range(MAX_NUMBER_OF_SCROLLDOWNS):
        # we are done, break out of loop
        if len(tweets) >= count:
            break

        tweet_texts = list(scrape_tweet_texts(url, scrolldown))

        if len(tweets) == 0:
            # first round of tweets
            tweets = tweet_texts
        else:
            # add tweets that we haven't got yet
            last_tweet = tweets[-1]
            if last_tweet == tweet_texts[-1]:
                # no new tweets found in this round
                continue
            elif last_tweet not in tweet_texts:
                continue
            index = tweet_texts.index(last_tweet)
            new_tweets = tweet_texts[index+1:]
            tweets += new_tweets

    return tweets[:count]

def scrape_tweet_texts(url, scrolldown=False):
    """Return an iterator of the text of tweets scraped from the url"""
    tweet_elements = scrape_tweet_elements(url, scrolldown)
    return map(get_tweet_text_from_tweet_element, tweet_elements)

def scrape_tweet_elements(url, scrolldown=False):
    """
    Return a list of requests-html.Element objects from url using request-html library.

    requests-html is used to scrape the html after running Javascript that belongs to the page
    using chromium.
    """
    r = SESSION.get(url)
    r.html.render(sleep=SLEEP, scrolldown=scrolldown)
    tweet_elements = r.html.find('section:first article div[data-testid="tweet"]')
    return tweet_elements

def get_tweet_text_from_tweet_element(tweet_element):
    """Return a text of a tweet given a top tweet element scraped from html"""
    second_child = get_div_children(tweet_element)[1]
    second_child_of_second_child = get_div_children(second_child)[1]
    return second_child_of_second_child.text

def get_div_children(element):
    """Helper function to get children div elements given a requests-html.Element object"""
    return element.find(':root > div > div')
