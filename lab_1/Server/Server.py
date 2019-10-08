from Lab1.Finder import get_html_page, find_articles, publish_report
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def server_run():
    url3 = "https://stopgame.ru/news"
    now = datetime.datetime.now()
    resp3 = get_html_page(url3)
    top = find_articles(url3)
    publish_report(top)
    art=[]
    for article in top['articles']:
        art.extend(article.values())

    return render_template('news.html', url = url3 , date = now, articles = art)


if __name__ == '__main__':
    app.run(host='localhost', port=9090)