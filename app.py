import os
from flask import Flask,render_template, request, json
from tweetdump import *
# from sentAnalysi import *

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
	
	return url

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

#call to tweetdump with topic hashtag input

#pass tweetdump output to sentAnalysis

#Pass complete tweet topic info to front end for display.

if __name__=="__main__":
    app.run(debug=True)
