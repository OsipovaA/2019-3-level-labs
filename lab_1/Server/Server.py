from lab_1.Crawler.Finder import find_articles, publish_report
import codecs
import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def server_run():
    url3 = "https://stopgame.ru/news"
    resp = requests.get(url3)
    top = find_articles(url3, resp)
    publish_report(top)
    with codecs.open("StopGame.json", "r", encoding="utf-8") as outfile:
        jdata = json.load(outfile)
        outfile.close()
    return render_template('news.html', articles=jdata)


@app.route('/<cmd>')
def refresh(cmd=None):
    if cmd == "Refresh Page":
        server_run()


if __name__ == '__main__':
    app.run(host='localhost', port=9090)
