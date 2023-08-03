#!/usr/bin/python3
"""Script that starts a Flask application"""

from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays "Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Display "HBNB!"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """Display "C" followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"c {escape(text)}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """Display "python", followed by the value of the variable"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
