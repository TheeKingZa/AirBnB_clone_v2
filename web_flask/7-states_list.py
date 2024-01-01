#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

# Teardown method to close the SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

@app.route('/states_list', methods=['GET'])
def states_list():
    # Fetch all State objects from storage and sort by name
    states = sorted(storage.all(State).values(), key=lambda x: x.name)

    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

