from Lab1.Finder import get_html_page, find_articles, publish_report

url3="https://stopgame.ru/news"
resp3 = get_html_page(url3)
top = find_articles(url3)
publish_report(top)
art=[]
for article in top['articles']:
    art.extend(article.values())
print(art)