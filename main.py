from flask import Flask, url_for, request

i = 0
app = Flask(__name__)


@app.route('/index')
def slogan():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="/static/css/style.css">
                        <title>Девиз</title>
                      </head>
                      <body>
                        <h1>Наш девиз</h1>
                        <h1>И на Марсе будут яблони цвести!</h1>
                        <button onclick="window.location.href = '/';" color="#ffcc00">На главную</button>
                      </body>
                    </html>"""


@app.route('/promotion')
def promotion():
    lines = ""
    with open('static/texts/promotion.txt', mode='rt', encoding='utf-8') as file:
        for line in file.read().split('\n'):
            lines += f"<h2>{line}</h2><br>"
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="/static/css/style.css">
                            <title>Рекламная кампания</title>
                          </head>
                          <body>
                            <h1>Наша кампания</h1>
                            {lines}
                            <button onclick="window.location.href = '/';" color="#ffcc00">На главную</button>
                          </body>
                        </html>"""


@app.route('/image_mars')
def show_image():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="/static/css/style.css">
                            <title>Привет, Марс!</title>
                          </head>
                          <body>
                            <h1 class=surprise>Жди нас, Марс!</h1>
                            <div class="mars_image">
                            <img src="{url_for('static', filename='img/mars.png')}" width=600 height=600
                            alt="здесь должна была быть картинка, но не нашлась">
                            <p>Вот она какая - красная планета!</p>
                            </div>
                            <button onclick="window.location.href = '/';" color="#ffcc00">На главную</button>
                          </body>
                        </html>"""


@app.route('/')
def start_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="/static/css/style.css">
                    <title>Миссия</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                    <button onclick="window.location.href = '/index';" color="#ffcc00">Наш девиз!</button>
                    <br>
                    <button onclick="window.location.href = '/promotion';" color="#ffcc00">Наша компания!</button>
                    <br>
                    <button onclick="window.location.href = '/image_mars';" color="#ffcc00">Фото марса</button>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
