from flask import Flask, render_template
from flask_wtf import Form
from flask_bootstrap import Bootstrap

from bart_api import bart_api
from tokens import BART_TOKEN
from python_nextbus.nextbus import api

app = Flask(__name__)
bootstrap = Bootstrap(app)

stop_id = '1030970'
route = 'BSD'

if BART_TOKEN == 'TOKEN_HERE':
    bart = bart_api.BartApi()
else:
    bart = bart_api.BartApi(BART_TOKEN)

def bus_departures():
    departures = api.predictions(agency='actransit', route=route, s=stop_id)
    if departures:
        return departues
    else:
        return ['No departure estimate']

def bart_departures(station):
    info = bart.etd(station)
    lines = {}
    for dest in info:
        dest['destination']
        departures = []
        for est in dest['estimates']:
            if est['minutes'] == 'Leaving':
                msg = '{} car train leaving now'.format(est['length'])
            else:
                msg = '{} car train leaving in {} minutes'.format(est['length'], est['minutes'])
            departures.append(msg)
        lines[dest['destination']] = departures
    return lines

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/station/<station>")
def bart_page(station):
    print(station)
    return render_template('bart.html', info=bart_departures(station))

@app.route("/broadwaybus")
def bus_page():
    return render_template('bus.html', busses=bus_departures())

if __name__ == "__main__":
    app.run()

