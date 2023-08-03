#!/usr/bin/python3
"""Simple script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    """Display “C ”, followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text="is cool"):
    """Display “Python ”, followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    """Display “n is a number” only if n is an integer"""
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
