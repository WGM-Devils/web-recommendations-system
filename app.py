from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"