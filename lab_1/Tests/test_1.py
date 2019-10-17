from lab_1.Crawler.Finder import get_html_page, publish_report, find_articles
import unittest
import json
import codecs

'''Test file structure'''


class First_test(unittest.TestCase):

    def test_url(self):
        url3 = "https://stopgame.ru/news"
        resp3 = get_html_page(url3)
        top = find_articles(url3, resp3)
        publish_report(top)
        with codecs.open("StopGame.json", "r", encoding="utf-8") as json_data:
            jdata = json.load(json_data)
            self.assertEqual(jdata['url'], url3)
            for article in jdata["articles"]:
                for art in article.values():
                    self.assertTrue(art)
        json_data.close()


if __name__ == '__main__':
    unittest.main()
