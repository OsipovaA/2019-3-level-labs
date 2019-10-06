# Лабораторная работа №1

## Задача №0. Выбрать онлайн-ресурс для обработки

Требуется выбрать уникальный в рамках потока сайт (проще всего будет работать с новостными источниками).

## Задача №1. HTML Crawler [2 балла]

Требуется сделать программу, которая по заданному в ней URL получает список 
заголовков этой страницы и сохраняет в файл в формате json: `articles.json`.

```json
{
    "url": "http://",
    "creationDate": "Jan 1, 1970. 9:30",
    "articles": [
        {
            "title": "Amazing news about MMA"
        }
    ]
}
```

Рекомендация: разбить код на следующие логические блоки (функции):

1. `get_html_page(url)` - должна быть валидным HTML
2. `find_articles(html_page)` - возвращает массив заголовков
3. `publish_report(path, articles)` - сохраняет массив заголовков в виде JSON 

Для получения страницы использовать модуль `requests`, для обработки страницы `BeautifulSoup`,  для сохранения в JSON - модуль `json`, а для даты модуль `datetime`.

## Задача №2. Unit tests for Crawler [2 балла]

Требуется написать unit test-ы на Crawler:
    1. тест на структуру файла - должен содержать УРЛ, список статей с как минмум одним элементом, который содержит заголовок.
    2. тест, что на тестовой странице обнаруживаются все заголовки (предполагается, что типовая страница будет сохранена)
    3. тест, что get_html_page получает страницу для работающего УРЛА

## Задача №3. Automate unit tests for Crawler [2 балла]

Требуется автоматизировать unit tests - с использованием Travis CI. Репозиторий должен быть зарегистрирован на этом сервисе, на каждый коммит в репозиторий происходит запуск юнит тестов. 

## Задача №4. Web-server [2 балла]

Требуется реализовать веб-сервер. Сервер - программа, которая реагирует на внешние запросы из браузера. При запуске сервера обязательно запускается crawler. Больше json не меняется, до следующего запуска сервера.  

## Задача №5. HTML report built on templates [2 балла]

Рекомендация: использовать flask в качестве фреймворка для написания сервера.

Требуется реализовать шаблонную HTML страницу. При заходе на `http://localhost:8000` открывается HTML страница, содержащая URL источника и нумерованный список заголовков

```html
<ol>
    <li>Amazing news about MMA</li>
</ol>
```