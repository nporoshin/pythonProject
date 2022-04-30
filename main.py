import json

import requests
from flask import Flask

import datetime


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    text = '<h1>Курс валют</h1>'
    text += '<table>'
    text += '<tr>'
    for _ in valutes[0]:
        text += f'<th><th>'
    text += '</tr>'
    for valute in valutes:
        text += '<tr>'
        for v in valute.values():
            text += f'<td>{v}</td>'
        text += '</tr>'

    text += '</table>'
    # добавим текущую дату
    я = '<h1>-Я-</h1>' \
        + '<h1>' \
        + str(datetime.datetime.now()) \
        + '</h1>'
    return я + text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    now = datetime.datetime.now()
    print("Текущая дата и время:")
    print(now)
    x = now
    app.run()
