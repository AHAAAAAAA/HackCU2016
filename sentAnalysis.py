#run tweets throught nltk
import tweepy #https://github.com/tweepy/tweepy
import codecs
import csv
import nltk
import json
from sentiment import sentiment_score
print sentiment_score(u"I love you")

class tweet:
  def __init__(self):
    tweet     = ''
    tId       = ''
    x         = 0
    y         = 0
    user      = ''
    createdAt = ''

def preprocessTweets(data):
  processed = []
  for i in data:
    tmp = tweet()
    tmp.tweet     = i[0]
    tmp.tId       = i[1]
    tmp.y         = len(i[0])
    tmp.user      = i[2]
    tmp.createdAt = i[3]
    processed.append(tweet)
  return processed

def sentimentAnalysis(data): #fill topicData with class tweet elements and return.
  topicData = []
    
  
  
  
  
