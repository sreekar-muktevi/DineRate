import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3
import numpy as np

busch_conn = sqlite3.connect('DineRate/DB/busch_items.db')


def db_to_array(conn):
    items = []
    cur = conn.cursor()
    cur.execute("SELECT rating FROM menu_items")

    rows = cur.fetchall()

    for i in range(len(rows)):
        items.append(rows[i][0])
    
    return items

def new_rating(conn, id, new_rating):
    ratings = db_to_array(conn)
    avg = (ratings[id] + new_rating) / 2
    conn.execute('''UPDATE menu_items
                    SET rating = avg
                    WHERE id''')

