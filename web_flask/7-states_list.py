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
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)