#!/usr/bin/python3
"""
Flask Module for HBNB project.
This module creates a simple Flask web application with a single route.
The application listens on 0.0.0.0, port 5000, and returns "Hello HBNB!"
when the root URL (/) is accessed. The use of `strict_slashes=False`
in the route definition allows the URL to be accessed with or without
a trailing slash.
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all("State").values(),
                           cities=storage.all('City').values())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)