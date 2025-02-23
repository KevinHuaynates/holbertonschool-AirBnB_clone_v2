#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route that displays 'n is a number' only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that displays an HTML page only if n is an integer:
    - H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that displays an HTML page only if n is an integer:
    - H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
