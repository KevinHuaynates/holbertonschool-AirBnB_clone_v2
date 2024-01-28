#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask
from html import escape  # Importar correctamente la función escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route that displays 'C ', followed by the value of the text variable
    Replace underscores (_) with spaces
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text="is cool"):
    """
    Route that displays 'Python ', followed by the value of the text variable
    Replace underscores (_) with spaces. Default text is "is cool".
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
