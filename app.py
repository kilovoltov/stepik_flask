from flask import Flask
from flask import render_template

import data


app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html')


@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html')


@app.route('/data/')
def render_data():
    return render_template('all_tours.html', data=data.tours)


@app.route('/data/departures/<departure>/')
def filter_departures(departure):
    items = dict(filter(lambda tour: tour[1]["departure"] == departure, data.tours.items()))
    return render_template('tours_by_departure.html', data=items, departure=data.departures[departure])


@app.route('/data/tours/<int:id>/')
def render_data_tour(id):
    return render_template('single_tour.html', item=data.tours[id])


if __name__ == '__main__':
    app.run(dabug=True)
