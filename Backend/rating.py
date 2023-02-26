import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

busch_conn = sqlite3.connect('hackruthing/DB/busch_items.db')


def db_to_array(conn):
    items = []
    cur = conn.cursor()
    cur.execute("SELECT id, rating FROM menu_items")

    rows = cur.fetchall()

    for row in rows:
        items.append(row)
    
    return items
    
print(db_to_array(busch_conn))