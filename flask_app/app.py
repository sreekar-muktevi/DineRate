import datetime
from markupsafe import escape
from flask import Flask, render_template, abort, request
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

def ratings_to_array(conn):
    items = []
    cur = conn.cursor()
    cur.execute("SELECT rating FROM menu_items")
    rows = cur.fetchall()

    for row in rows:
        items.append(row[0])

    return items


@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/busch-apply-rating', methods=['POST'])
# def applyrating():
#     new_rating = int(request.form['rating'])
#     ratings = ratings_to_array(busch_conn)
#     avg = (sum(ratings[1]) + new_rating) / (len(ratings[1]) + 1)
#     busch_conn.execute('''UPDATE menu_items
#                     SET rating = ?
#                     WHERE 1''', (avg))

@app.route('/busch-apply-rating', methods=['POST'])
def buschapplyrating():
    new_rating = int(request.form['rating'])
    ratings = ratings_to_array(busch_conn)
    avg = (sum(ratings) + new_rating) / (len(ratings) + 1)
    busch_conn.execute('UPDATE menu_items SET rating = ?', (avg,))
    busch_conn.commit()
    return busch()

@app.route('/livi-apply-rating', methods=['POST'])
def liviapplyrating():
    new_rating = int(request.form['rating'])
    ratings = ratings_to_array(livi_conn)
    avg = (sum(ratings) + new_rating) / (len(ratings) + 1)
    livi_conn.execute('UPDATE menu_items SET rating = ?', (avg,))
    livi_conn.commit()
    return livi()

@app.route('/neilson-apply-rating', methods=['POST'])
def neilsonapplyrating():
    new_rating = int(request.form['rating'])
    ratings = ratings_to_array(neilson_conn)
    avg = (sum(ratings) + new_rating) / (len(ratings) + 1)
    neilson_conn.execute('UPDATE menu_items SET rating = ?', (avg,))
    neilson_conn.commit()
    return neilson()

@app.route('/brower-apply-rating', methods=['POST'])
def browerapplyrating():
    new_rating = int(request.form['rating'])
    ratings = ratings_to_array(brower_conn)
    avg = (sum(ratings) + new_rating) / (len(ratings) + 1)
    brower_conn.execute('UPDATE menu_items SET rating = ?', (avg,))
    brower_conn.commit()
    return brower()


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
    return render_template('brower.html', results=db_to_array(brower_conn))
