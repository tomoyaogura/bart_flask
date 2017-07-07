from flask import Flask, render_template
from flask_wtf import Form
from flask_bootstrap import Bootstrap

from bart_api import bart_api
from tokens import BART_TOKEN

app = Flask(__name__)
bootstrap = Bootstrap(app)

if BART_TOKEN == 'TOKEN_HERE':
    bart = bart_api.BartApi()
else:
    bart = bart_api.BartApi(BART_TOKEN)

def bart_departures(station):
    info = bart.etd(station)
    lines = {}
    for dest in info:
        dest['destination']
        departures = []
        for est in dest['estimates']:
            train = (est['length'], est['minutes'])
            departures.append(train)
        lines[dest['destination']] = departures
    return lines

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/station/<station>")
def bart_page(station):
    print(station)
    return render_template('bart.html', info=bart_departures(station))

if __name__ == "__main__":
    app.run()

