# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("./templates/index.html", static_folder="./static")

if __name__ == '__main__':
    app.run()