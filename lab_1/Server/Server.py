from lab_1.Crawler.Finder import find_articles, publish_report
import datetime
import codecs
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def server_run():
    url3 = "https://stopgame.ru/news"
    now = datetime.datetime.now()
    top = find_articles(url3)
    publish_report(top)
    with codecs.open("StopGame.json", "r", encoding="utf-8") as outfile:
        jdata = json.load(outfile)
        eds=jdata['articles']
        list_len = len(eds)
        art = []
        i = 0
        while i < list_len:
            art_list = list(jdata["articles"][i].values())
            art.extend(art_list)
            i += 1
        outfile.close()
    return render_template('news.html', url=url3, date=now, articles=art)


@app.route('/<cmd>')
def refresh(cmd=None):
    if cmd == "Refresh Page":
        server_run()


if __name__ == '__main__':
    app.run(host='localhost', port=9090)
