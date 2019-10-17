from lab_2.Finder import find_articles, publish_report
import codecs
import json
import requests
import os
from flask import Flask, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def server_run():
    url3 = "https://stopgame.ru/news"
    resp = requests.get(url3)
    top = find_articles(url3, resp)
    publish_report(top)
    with codecs.open("StopGame.json", "r", encoding="utf-8") as outfile:
        jdata = json.load(outfile)
        outfile.close()
    return render_template('news.html', articles=jdata)


@app.route('/refresh', methods=['POST'])
def save():
    return redirect(url_for('server_run'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run()
