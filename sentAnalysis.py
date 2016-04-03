#run tweets throught nltk
import tweepy #https://github.com/tweepy/tweepy
import codecs
import csv
import json
from sentiment import sentiment_score
def preprocessTweets(data):
  processed = []
  for i in data:
    tmp = []
    tmp.append(i[0].decode("utf-8"))
    tmp.append(i[1])
    tmp.append(len(i[0]))
    tmp.append(i[2])
    tmp.append(i[3])
    tmp.append(i[-1])
    processed.append(tmp)
  return processed

def sentimentAnalysis(data): #fill topicData with class tweet elements and return.
  analysed = []
  for i in data:
    i.append(sentiment_score(i[0]))
    analysed.append(i)
  return analysed



    
  
  
  
  
