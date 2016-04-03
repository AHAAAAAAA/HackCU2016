# from sentiment import sentiment_score
# print sentiment_score(u"I love you")
from tweetdump import *
# import senti_classifier
# import nltk
# nltk.download('movie_reviews')
# # nltk.download('sentiwordnet')
# # nltk.download('wordnet')
# # nltk.download('twitter_samples')
# # nltk.download('punkt')
# # sentences = ['Fuck this', 'I love you']
# # pos_score, neg_score = senti_classifier.polarity_scores(sentences)
# # print pos_score, neg_score

data =  get_all_tweets('#jack')
# for i in data:
	# print i
print data
# from senti_classifier import senti_classifier
# import nltk

# #call to tweetdump with topic hashtag input
# opinions = get_all_tweets("fidelity")
# print opinions
# #pass tweetdump output to sentAnalysis
# opinions = preprocessTweets(opinions)
# print opinions
# opinions = sentimentAnalysis(opinions)
# print opinions
#Pass complete tweet topic info to front end for display.
