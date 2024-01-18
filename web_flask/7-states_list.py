#!/usr/bin/python3
"""
Script que inicia una aplicación web Flask
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Maneja la ruta '/states_list' y muestra una lista de estados.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Cierra la sesión de SQLAlchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

