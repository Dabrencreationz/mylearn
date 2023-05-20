#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Welcome to MyLearn, online personalized learning platform!'

@app.route('/courses')
def courses():
    return "Browse available courses here.'
