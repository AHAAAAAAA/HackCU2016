import os
from flask import Flask,render_template, request, jsonify
from tweetdump import *
from sentAnalysis import *
import json

app = Flask(__name__)

@app.route('/')
def hello():
	# data = get_all_tweets('#Bahrain')
	# # tweets = sentimentAnalysis(data)
	# str = ''
	# for i in data:
	# 	str += i[2]+'\n'
	data = trending_topics()
	return render_template('dalvonic-home.html', page_title='Dalvonic', data=data)

@app.route('/graph')
def hi():
	query =  '#'+request.args.get('q')
	user =  request.args.get('u')
	cleanUserTweets = []
	if user!='None':
		userTweets = get_user_tweets(user)
		for i in userTweets:
			if i[0].decode("utf-8").find(query)!= -1:
				cleanUserTweets.append(i)
	outTweets = get_all_tweets(query)
	outTweets.extend(cleanUserTweets)
	#searches throught user tweets and matches querys
	data = preprocessTweets(outTweets)
	return render_template('graph.html', page_title='Dalvonic', data=map(json.dumps, data))
#call to tweetdump with topic hashtag input

#pass tweetdump output to sentAnalysis

#Pass complete tweet topic info to front end for display.
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
if __name__=="__main__":
    app.run(debug=True)
