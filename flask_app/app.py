import datetime
from markupsafe import escape
from flask import Flask, render_template, abort
import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file, check_same_thread=False)
    return conn


# Connect to the database

busch_conn = create_connection('../DB/busch_items.db')
livi_conn = create_connection('../DB/livi_items.db')
neilson_conn = create_connection('../DB/neilson_items.db')
brower_conn = create_connection('../DB/brower_items.db')

app = Flask(__name__)


def db_to_array(conn):
    items = []
    cur = conn.cursor()
    cur.execute("SELECT name, rating FROM menu_items")

    rows = cur.fetchall()

    for i in range(len(rows)):
        items.append([rows[i][0], rows[i][1]])
        items[i][1] = int(items[i][1])

    return items


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/busch/')
def busch():
    return render_template('busch.html', results=db_to_array(busch_conn))


@app.route('/livi/')
def livi():
    return render_template('livi.html', results=db_to_array(livi_conn))


@app.route('/neilson/')
def neilson():
    return render_template('neilson.html', results=db_to_array(neilson_conn))


@app.route('/brower/')
def brower():
    return render_template('brower.html', results=db_to_array(neilson_conn))
