from tweetdump import *
from senti_classifier import senti_classifier
import nltk
nltk.download('movie_reviews')
nltk.download('sentiwordnet')
nltk.download('wordnet')
nltk.download('twitter_samples')
nltk.download('punkt')
sentences = ['Fuck this', 'I love you']
pos_score, neg_score = senti_classifier.polarity_scores(sentences)
print (pos_score, neg_score)
