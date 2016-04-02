from csv import DictReader, DictWriter

import numpy as np
import re
from numpy import array

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
import nltk
# nltk.download()
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

kTARGET_FIELD = 'spoiler'
kTEXT_FIELD = 'sentence'

#Online implementation found
class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]
def removepunc(text):
    punctuation = re.compile(r'[,.?!\':\)\(`";|0-9]')
    text = punctuation.sub('', text)
    return text

class Featurizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
          analyzer = 'word',
          max_df=0.5,
          preprocessor = removepunc,
          ngram_range=(1,3),
          stop_words = 'english',
          strip_accents = 'ascii',
          tokenizer = LemmaTokenizer(),
          sublinear_tf=True,
          smooth_idf=True
          )

    def train_feature(self, examples):
        return self.vectorizer.fit_transform(examples)

    def test_feature(self, examples):
        return self.vectorizer.transform(examples)

    def show_top10(self, classifier, categories):
        feature_names = np.asarray(self.vectorizer.get_feature_names())
        if len(categories) == 2:
            top10 = np.argsort(classifier.coef_[0])[-10:]
            bottom10 = np.argsort(classifier.coef_[0])[:10]
            print("Pos: %s" % " ".join(feature_names[top10]))
            print("Neg: %s" % " ".join(feature_names[bottom10]))
        else:
            for i, category in enumerate(categories):
                top10 = np.argsort(classifier.coef_[i])[-10:]
                print("%s: %s" % (category, " ".join(feature_names[top10])))

if __name__ == "__main__":

    # Cast to list to keep it all in memory
    train = list(DictReader(open("../data/spoilers/train3.csv", 'r')))
    test = list(DictReader(open("../data/spoilers/test3.csv", 'r')))

    feat = Featurizer()

    labels = []
    for line in train:
        if not line[kTARGET_FIELD] in labels:
            labels.append(line[kTARGET_FIELD])

    print("Label set: %s" % str(labels))
    x_train = feat.train_feature(x[kTEXT_FIELD] for x in train)
    x_test = feat.test_feature(x[kTEXT_FIELD] for x in test)

    y_train = array(list(labels.index(x[kTARGET_FIELD])
                         for x in train))

    print(len(train), len(y_train))
    print(set(y_train))

    # Train classifier
    lr = SGDClassifier(loss='log', penalty='l2', shuffle=True)
    lr.fit(x_train, y_train)

    feat.show_top10(lr, labels)

    predictions = lr.predict(x_test)
    o = DictWriter(open("predictions.csv", 'w'), ["id", "spoiler"])
    o.writeheader()
    for ii, pp in zip([x['id'] for x in test], predictions):
        d = {'id': ii, 'spoiler': labels[pp]}
        o.writerow(d)