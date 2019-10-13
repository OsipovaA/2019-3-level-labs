from lab_1.Crawler.Finder import get_html_page
import unittest

'''URL status'''


class Third_test(unittest.TestCase):
    def test_url(self):
        url = "https://stopgame.ru/news"
        resp = get_html_page(url)
        self.assertEqual(resp.status_code, 200) # status code == 200 or not


if __name__ == '__main__':
    unittest.main()
