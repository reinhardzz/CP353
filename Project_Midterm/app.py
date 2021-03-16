from urllib import parse
from flask import Flask,render_template,request

import requests


from urllib.parse import quote
from urllib.request import urlopen
import json

import socket

app = Flask(__name__)





@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/genre')
def news():
    return render_template('genre.html')


@app.route('/info')
def info():
    return render_template('Info.html')



@app.route('/aboutus')
def aboutme():
    return render_template('aboutus.html')

def searchNews(tag,API_KEY):
    query = quote(tag)
    url = NEWS_URL.format(query, API_KEY)
    print(url)
    data = urlopen(url).read()
    parsed = json.loads(data)
    news = parsed.get('articles')
    
    return news
    

    
def getCovidNews():
    url = "https://newsapi.org/v2/top-headlines?q=covid&page=1&apiKey=ebcd985b9a2d4aefb0e99d7b45bf8b3d"
    res = requests.get(url)
    news = res.json()
    list_news = list()
    
    for i in range(0,5):
        list_news.append(news['articles'][i])
    
    return list_news

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)