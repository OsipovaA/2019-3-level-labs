from lab_1.Crawler.Finder import get_html_page, publish_report, find_articles
import unittest
import json
import codecs

'''Test file structure'''


class First_test(unittest.TestCase):

    def test_url(self):
        url3 = "https://stopgame.ru/news"
        resp3 = get_html_page(url3)#status
        top = find_articles(url3, resp3)#Parcer
        publish_report(top)#write json
        with codecs.open("StopGame.json", "r", encoding="utf-8") as json_data:#open json
            jdata = json.load(json_data)#load json
            self.assertEqual(jdata['url'][0], url3)#url ink == url link(https://stopgame.ru/news" == https://stopgame.ru/news")
            for article in jdata["articles"]:
                for art in article.values():
                    self.assertTrue(art)#titles in son not empty
        json_data.close()


if __name__ == '__main__':
    unittest.main()
