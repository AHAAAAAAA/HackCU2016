# from sentiment import sentiment_score
# print sentiment_score(u"I love you")
from tweetdump import *
# import senti_classifier
# import nltk
# nltk.download('movie_reviews')
# nltk.download('sentiwordnet')
# nltk.download('wordnet')
# nltk.download('twitter_samples')
# nltk.download('punkt')
# sentences = ['Fuck this', 'I love you']
# pos_score, neg_score = senti_classifier.polarity_scores(sentences)
# print pos_score, neg_score

# data =  trending_topics()
# for i in data:
# 	print i
def get_user_tweets(screen_name): #could also be a user ID for user's tweets.
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
	auth.set_access_token(access_key2, access_secret2)
	api = tweepy.API(auth)

	alltweets = []	
	if api.rate_limit_status()['resources']['search']['/search/tweets']['remaining']==0:
		auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
		auth.set_access_token(access_key2, access_secret2)
		api = tweepy.API(auth2)
	#initialize a list to hold all the tweepy Tweets
	#ahmed was here
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name, count=1)
	
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
	# outtweets = [[tweet.text, tweet.id_str.encode('utf-8'), tweet.author._json['screen_name'].encode('utf-8'), tweet.created_at, "true".encode('utf-8')] for tweet in alltweets]
	return new_tweets
print get_user_tweets('waishda')
# import nltk

# #call to tweetdump with topic hashtag input
# opinions = get_all_tweets("fidelity")
# print opinions
# print '\n'
# #pass tweetdump output to sentAnalysis
# opinions = preprocessTweets(opinions)
# for i in opinions:
# 	print i[0]
# opinions = sentimentAnalysis(opinions)
# print opinions
#Pass complete tweet topic info to front end for display.
