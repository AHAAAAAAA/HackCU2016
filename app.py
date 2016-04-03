import os
from flask import Flask,render_template, request, json
from tweetdump import *
from sentAnalysis import *

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
	if user!='':
		userTweets = get_user_tweets(user)
		for i in userTweets:
			if i[0].find(query)!= -1:
				cleanUserTweets.append(i)


	outTweets = get_all_tweets(query)
	outTweets.append(cleanUserTweets)

	#searches throught user tweets and matches querys
	processedTweets = preprocessTweets(outTweets)
	data = sentimentAnalysis(processedTweets)
	return render_template('graph.html', page_title='Graph', data=data)

#call to tweetdump with topic hashtag input

#pass tweetdump output to sentAnalysis

#Pass complete tweet topic info to front end for display.

if __name__=="__main__":
    app.run(debug=True)
