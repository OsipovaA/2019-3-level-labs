from lab_1.Crawler.Finder import find_articles, publish_report
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def server_run():
    url3 = "https://stopgame.ru/news"
    now = datetime.datetime.now()
    top = find_articles(url3)
    publish_report(top)
    art = []
    for article in top['articles']:
        art.extend(article.values())
    return render_template('news.html', url=url3, date=now, articles=art)


@app.route('/<cmd>')
def refresh(cmd=None):
    if cmd == "Refresh Page":
        server_run()


if __name__ == '__main__':
    app.run(host='localhost', port=9090)
