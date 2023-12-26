#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

# Route for the root URL ('/')
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
