#! /usr/bin/env python
from flask import Flask, render_template

app = Flask(__name__)

app.config['FREEZER_DESTINATION_IGNORE'] = ['CNAME', ]

@app.route("/")
def home():
    return render_template("main.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
