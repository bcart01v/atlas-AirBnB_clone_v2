#!/usr/bin/python3
"""
Flask Module for HBNB project.

This module creates a simple Flask web application with a single route.
The application listens on 0.0.0.0, port 5000, and returns "Hello HBNB!"
when the root URL (/) is accessed. The use of `strict_slashes=False`
in the route definition allows the URL to be accessed with or without
a trailing slash.

Additionally, will also handle /hbnb routes.

On top of that, /c/<text> routes. Surprised? I'm not.
"""


from flask import Flask # Removed Comment, it was too long for Pep8.


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Index route handler.

    Returns:
        str: The string "Hello HBNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB route handler.

    Returns
        str: HBNB. Can you imagine?
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    C Route handler. Displays 'C', Followed by text entered.

    Args:
        text(str): Text from the URL.

    Returns:
        str: The formatted string.
    """

    display_text = text.replace('_',' ')
    return f"C {display_text}"


if __name__ == '__main__':
    # Runs the Flask application on 0.0.0.0, listening on port 5000.
    app.run(host='0.0.0.0', port=5000)
