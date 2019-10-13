import unittest
from lab_1.Crawler.Finder import find_articles
import requests


'''Test articles not empty'''

class Second_test(unittest.TestCase):
    def test_crawler(self):
        url = 'https://stopgame.ru/news'
        resp = requests.get(url) #Status
        articl = find_articles(url, resp)#Parcer
        c = 0
        list_len = len(articl["articles"])#length
        while c < list_len:
            art_list = list(articl["articles"][c].values())#titles
            self.assertTrue(art_list)#titles in parcer list not empty
            c += 1


if __name__ == '__main__':
    unittest.main()
