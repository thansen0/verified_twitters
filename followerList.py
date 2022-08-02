#!/usr/bin/env python
# encoding: utf-8

# Ensures the API keys are correct
import tweepy
import configparser
import time

# Twitter API credentials
config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config["DEFAULT"]["CONSUMER_KEY"].strip("'\"")
CONSUMER_SECRET = config["DEFAULT"]["CONSUMER_SECRET"].strip("'\"")
ACCESS_TOKEN = config["DEFAULT"]["ACCESS_TOKEN"].strip("'\"")
ACCESS_TOKEN_SECRET = config["DEFAULT"]["ACCESS_TOKEN_SECRET"].strip("'\"")
BEARER_TOKEN = config["DEFAULT"]["BEARER_TOKEN"].strip("'\"")

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)


f = open("usernames.txt", "w")

for response in tweepy.Paginator(client.get_users_following, 63796828, max_results=1000):
    print(response.data[0])

    for d in response.data:
        f.write(str(d) + "\n")
    

f.close()

