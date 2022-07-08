# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, redirect
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def index():
    adress_photos = './static/img/photo'
    photo = os.listdir(adress_photos)
    photos = []
    for ph in photo:
        photos.append(adress_photos + '/' + ph)
    prev = """Python – это не просто язык программирования. Это целый мир со своими возможностями, трудными задачами и способами их решений. На курсах направления 'Программирование на Python' ученики познакомятся от основ синтаксиса языка, до разработки приложений в одной из областей программирования."""
    pit1_1 = "Программирование для Python для начинающих (Питоняши) 6-7 классы, 2 семестра"
    pit1_2 = "Желательно пройти один из наших курсов детского программирования. В курсе: изучение синтаксиса Python, стандартная библиотека, функции, программирование физических объектов. Что потом: может служить подготовкой для курса Python в Яндекс.Лицее."
    pit2_1 = 'Основы программирования на Python 7-11 классы, 4 семестра'
    pit2_2 = 'Этот курс — классическое программирование, включающее всю необходимую теорию и много практики. Первый год — знакомство с языком, модулями, ООП. Второй год — графический интерфейс, работа с базами данных, веб-проекты, боты и промышленное программирование. Что потом: можно работать junior-программистом, изучать ИИ, использовать Python во множестве областей науки и техники.'
    pit3_1 = 'Программа «Яндекс.Лицей»'
    pit3_2 = 'Для учеников 9 класса, но в отдельных случаях возможны исключения для учеников 8 и 10 классов. 2 года обучения. Контроль обучения и сертификат об окончании от «Яндекс.Лицея». Заявку на обучение нужно оставить на сайте проекта «Яндекс.Лицей» до 10 сентября.'
    content = {
        "photos": photos,
        "pit1_1": pit1_1,
        "pit1_2": pit1_2,
        'pit2_1': pit2_1,
        'pit2_2': pit2_2,
        'pit3_1': pit3_1,
        'pit3_2': pit3_2,
        'prev': prev
    }
    return render_template('index.html', title='Главная страница', content=content)


@app.route('/timetable')
def timetable():
    timetable_info = {'line1': ['PY-1/22-1', 'PYJ-1/22-2', 'PY-2/22-5'],
                      'line2': ['PY-3/22-2', 'PY-1/21-4', 'PY-3/22-1'],
                      'line3': ['PY-3/22-5', 'PY-5/20-2', 'PY-3/22-1'],
                      'line4': ['Yandex-2', 'Yandex-3', 'Yandex-1']}
    return render_template('timetable.html', title='Расписание', timetable=timetable_info)


@app.route('/adress')
def adress():
    adress_info = {'adress': 'г.Норильк, ул.50 лет Октября, д.10',
                   'map': '../static/img/way_to_сube.jpg'}
    return render_template('adress.html', title='Где мы находимся', adress=adress_info)


@app.route('/contacts')
def contacts():
    contacts_info = {"user_name": 'Егор'}
    return render_template('contacts.html', title='Контакты', user=contacts_info)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == "__main__":
    main()
