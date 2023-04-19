from flask import Flask, render_template
import requests
from decouple import config


API_KEY = config('NEWS_API_KEY')

app = Flask(__name__)

country = 'us'

@app.route('/')
def news_headlines():
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    res = requests.get(url).json()
    news_articles = res['articles']
    return render_template('index.html', news_articles=news_articles)


