from tweetdump import *
from senti_classifier import senti_classifier
import nltk
#call to tweetdump with topic hashtag input
opinions = get_all_tweets("fidelity")
#pass tweetdump output to sentAnalysis
opinions = preprocessTweets(opinions)
opinions = sentimentAnalysis(opinions)
print opinions
#Pass complete tweet topic info to front end for display.
