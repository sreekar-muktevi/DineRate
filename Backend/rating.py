import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

busch_conn = sqlite3.connect('hackruthing/Backend/busch_items.db')


def db_to_array(conn):
    items = []
    cur = conn.cursor()
    cur.execute("SELECT rating FROM busch_items")

    rows = cur.fetchall()

    for row in rows:
        items.append(row)
    
    return items

def rating_to_db(conn, selected_id, new_rating):
    if(conn.execute('''SELECT rating FROM busch_items WHERE id = databaseFilePath''')):
        x = 0
        

    conn.execute('''UPDATE busch_items
                    SET rating = new_rating
                    WHERE id = selected_id;''')
    
print(db_to_array(busch_conn))