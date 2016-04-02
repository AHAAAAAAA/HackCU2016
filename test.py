from tweetdump import *
topic = '#Trump'
data =  get_all_tweets(topic)
for i in data:
	print i[2]
