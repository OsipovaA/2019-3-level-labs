import unittest
import json
import codecs

class First_test(unittest.TestCase):

    def test_url(self):
        with codecs.open("../Tests/StopGame.json", "r", encoding="utf-8") as json_data:
            jdata = json.load(json_data)
            eds = list(jdata.keys())
            ed = eds[0]
            self.assertEqual(ed, 'url')
        json_data.close()

    def test_data(self):
        with codecs.open("StopGame.json", "r", encoding="utf-8") as json_data:
            jdata = json.load(json_data)
            eds = list(jdata.keys())
            ed = eds[1]
            self.assertEqual(ed, 'creationDate')
        json_data.close()

    def test_articles(self):
        with codecs.open("StopGame.json", "r", encoding="utf-8") as json_data:
            jdata = json.load(json_data)
            eds = list(jdata.keys())
            ed = eds[2]
            self.assertEqual(ed, 'articles')
        json_data.close()

    def test_titles(self):
        with codecs.open("StopGame.json", "r", encoding="utf-8") as json_data:
            jdata = json.load(json_data)
            eds = list(jdata.values())
            list_len = len(eds[2])
            i = 0
            while i < list_len:
                art_list = list(jdata["articles"][i].keys())
                art_single = art_list[0]
                self.assertEqual(art_single, 'Title')
                i += 1
        json_data.close()


if __name__ == '__main__':
    unittest.main()
