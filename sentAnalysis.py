#run tweets throught nltk
import tweepy #https://github.com/tweepy/tweepy
import codecs
import csv
import json
from sentiment import sentiment_score
def preprocessTweets(data):
  processed = {}
  for i in data:
    tmp = {}
    tmp['tweet']=(i[0].decode("utf-8"))
    tmp['id']=(i[1])
    tmp['y']=(len(i[0]))
    tmp['user']=(i[2])
    tmp['createdAt']=(i[3])
    tmp['isUser']=(i[-1])
    tmp['sentiment']=(sentiment_score(i[0].decode("utf-8")))
    processed[i[1]]= tmp
  return processed


    
  
  
  
  
