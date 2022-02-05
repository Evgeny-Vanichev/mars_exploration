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

@app.route('/promotion_image')
def promotion_image():
    alerts = ["primary", "secondary", "success", "danger", "warning", "info", "light"]
    lines = ""
    with open('static/texts/promotion.txt', mode='rt', encoding='utf-8') as file:
        for line in file.read().split('\n'):
            lines += f'<div class="alert alert-{__import__("random").choice(alerts)}">{line}</div>'
    return f"""<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" 
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                crossorigin="anonymous">
                                <link rel="stylesheet" href="/static/css/style.css">
                                <title>Привет, Марс!</title>
                              </head>
                              <body>
                                <h1 class=surprise>Жди нас, Марс!</h1>
                                <img src="{url_for('static', filename='img/mars.png')}" width=600 height=600
                                alt="здесь должна была быть картинка, но не нашлась">
                                {lines}
                                <button onclick="window.location.href = '/';" color="#ffcc00">На главную</button>
                              </body>
                            </html>"""

@app.route('/form', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':

        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align=center>Анкета претендента</h1>
                            <h2 align=center>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="password" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <br>
                                     <p>Какие у Вас есть профессии</p>
                                     <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="1" name="1">
                                        <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="2" name="2">
                                        <label class="form-check-label" for="acceptRules">пилот</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="3" name="3">
                                        <label class="form-check-label" for="acceptRules">строитель</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="4" name="4">
                                        <label class="form-check-label" for="acceptRules">экзобиолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="5" name="5">
                                        <label class="form-check-label" for="acceptRules">врач</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="6" name="6">
                                        <label class="form-check-label" for="acceptRules">инженер по терраформированию</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="7" name="7">
                                        <label class="form-check-label" for="acceptRules">климатолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="8" name="8">
                                        <label class="form-check-label" for="acceptRules">специалист по радиационной защите</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="9" name="9">
                                        <label class="form-check-label" for="acceptRules">астрогеолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="10" name="10">
                                        <label class="form-check-label" for="acceptRules">гляциолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="11" name="11">
                                        <label class="form-check-label" for="acceptRules">инженер жизнеобеспечения</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="12" name="12">
                                        <label class="form-check-label" for="acceptRules">метеоролог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="13" name="13">
                                        <label class="form-check-label" for="acceptRules">оператор марсохода</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="14" name="14">
                                        <label class="form-check-label" for="acceptRules">киберинженер</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="15" name="15">
                                        <label class="form-check-label" for="acceptRules">штурман</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="16" name="16">
                                        <label class="form-check-label" for="acceptRules">пилот дронов</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return '''<h1>Форма отправлена</h1><button onclick="window.location.href = '/';" color="#ffcc00">На главную</button>'''

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
                    <br>
                    <button onclick="window.location.href = '/promotion_image';" color="#ffcc00">Красивая реклама</button>
                    <br>
                    <button onclick="window.location.href = '/form';" color="#ffcc00">Подать заявку</button>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
