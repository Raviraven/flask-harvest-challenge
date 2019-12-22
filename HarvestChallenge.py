import os
import sys
from flask import Flask, render_template, redirect, url_for, request

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "Hello world"


if __name__ == '__main__':
    app.run(debug=True)