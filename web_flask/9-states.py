#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a HTML page with a list of all State objects present in DBStorage sorted by name (A->Z)"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    """Displays a HTML page with information about a specific state and its cities"""
    state = storage.get(State, id)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

