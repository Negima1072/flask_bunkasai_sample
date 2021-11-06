# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__, static_folder='html/static', template_folder='html/templates')

@app.route('/')
def index():
    return render_template("index.html", static_folder="./static")

if __name__ == '__main__':
    app.run()