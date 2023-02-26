import datetime
from markupsafe import escape
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/busch/')
def busch():
    return render_template('busch.html')

@app.route('/livi/')
def livi():
    return render_template('livi.html')

@app.route('/neilson/')
def neilson():
    return render_template('neilson.html')

@app.route('/brower/')
def brower():
    return render_template('brower.html')