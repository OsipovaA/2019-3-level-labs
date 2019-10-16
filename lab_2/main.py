from lab_1.Crawler.Finder import get_html_page, find_articles, publish_report

url3 = "https://stopgame.ru/news"
resp3 = get_html_page(url3)
top = find_articles(url3,resp3)
publish_report(top)
