#!/usr/bin/env python3

from requests_html import HTMLSession


SLEEP=5
SESSION = HTMLSession()

def scrape_tweet_contents(url, scrolldown=False):
    tweets = scrape_tweets(url, scrolldown)
    return map(get_tweet_content, tweets)

def scrape_tweets(url, scrolldown=False):
    r = SESSION.get(url)
    r.html.render(sleep=SLEEP, scrolldown=scrolldown)
    tweets = r.html.find('section:first article div[data-testid="tweet"]')
    return tweets

def get_tweet_content(tweet_element):
    second_children = get_element_children(tweet_element)[1]
    second_children_of_second_children = get_element_children(second_children)[1]
    return second_children_of_second_children.text

def get_element_children(element):
    return element.find(':root > div > div')
