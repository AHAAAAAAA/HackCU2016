import os
from flask import Flask,render_template, request,json
from tweetdump import *
from sentAnalysi import *

app = Flask(__name__)
class tweet:
	tweet   = ''
	tweetId = ''
	x       = 0
	y       = 0

@app.route('/')
def hello():
	data = get_all_tweets(anything)
	tweets = sentimentAnalysis(data)
    return 'Welcome to Python Flask!'

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

if __name__=="__main__":
    app.run()
