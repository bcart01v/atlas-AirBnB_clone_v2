#!/usr/bin/python3
""" This is the Flask Module """



from flask import flask

app = flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
