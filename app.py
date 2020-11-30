"""
Author : Yong Kang

Web App that turns Youtube URL into nice transcript
"""

import os
from flask import Flask, render_template,request
# from flask_sqlalchemy import SQLAlchemy
import youtube_transcript
import json 
import logging

# from models import Result
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/transcript/', methods=['GET', 'POST'])
def transcript():
    url = request.form["url"]
    app.logger.info("helloworld")
    try:
        transcript = youtube_transcript.get_transcript(url)[0]
        results = youtube_transcript.extract(transcript)
        app.logger.info(results)
        return render_template('index.html',results=results)
    except:
        return render_template("404.html")



if __name__ == '__main__':
    app.run(debug=False)