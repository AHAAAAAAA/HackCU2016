#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import codecs
import csv
import json
from keys import *


def get_all_tweets(topic):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	#ahmed was here
	#make initial request for most recent tweets (200 is the maximum allowed count)
	page_count = 0  
	for tweets in tweepy.Cursor(api.search, q=topic, count=100,
                result_type="recent", include_entities=True).pages():  
		page_count += 1  
		# print just the first tweet out of every page of 100 tweets  
		print tweets[0].text.encode('utf-8')  
		if page_count >= 200:  
			break
	# new_tweets = tweepy.Cursor(api.search(q=topic)).items(200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	# #keep grabbing tweets until there are no tweets left to grab
	# while len(new_tweets) > 0:
	# 	#all subsiquent requests use the max_id param to prevent duplicates
	# 	new_tweets = api.search(q=topic, rpp=200)	
		
	# 	#save most recent tweets
	# 	alltweets.extend(new_tweets)
		
	# 	#update the id of the oldest tweet less one
	# 	oldest = alltweets[-1].id - 1
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8"), tweet.id_str, tweet.author._json['screen_name'], tweet.created_at,] for tweet in alltweets]
	
	return outtweets
def trending_topics():
	topics = []
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	#2367231
	loc = api.trends_closest(40.014828, -105.258176)[0]
	trends = api.trends_place(id=loc['woeid'])[0]
	for i in trends['trends']:
		topics.append(i['name'].encode('utf-8'))
	return topics