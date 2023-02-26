import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

def menu_to_array(campus):
    # URL editing
    URL = "http://menuportal.dining.rutgers.edu/foodpro/pickmenu.asp?sName=+University+Dining&locationNum=0"
    URL += str(campus)

    # Web Scraping 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    mydivs = soup.find_all("div", {"class": "col-1"})

    # Array to hold menu items
    menu_items = []

    for i in mydivs:
        menu_items.append(str(i)[96:-6])

    # Cleaning the data
    for i in range(len(menu_items)):
        if (menu_items[i][0] == '>'):
            menu_items[i] = menu_items[i][1:]
    
    return menu_items
    



def array_to_database(conn, menu_items):
    # Create an empty database if it doesn't already exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            rating REAL NOT NULL
        );
    ''')

    # Deletes database if existing already          
    conn.execute('DELETE FROM menu_items')

    # Resets index to 1
    conn.execute('UPDATE sqlite_sequence SET seq=0 WHERE name="menu_items"')
    conn.commit()

    # Insert menu items into menu_items.db
    for i in menu_items:
        conn.execute('''
            INSERT INTO menu_items (name, rating)
            VALUES (?, ?);
        ''', (i, 0))

    conn.commit()
    conn.close()

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Connect to the database
busch_conn = create_connection('hackruthing/DB/busch_items.db')
livi_conn = create_connection('hackruthing/DB/livi_items.db')
neilson_conn = create_connection('hackruthing/DB/neilson_items.db')
brower_conn = create_connection('hackruthing/DB/brower_items.db')

array_to_database(busch_conn, menu_to_array(4))
array_to_database(livi_conn, menu_to_array(3))
array_to_database(neilson_conn, menu_to_array(5))
array_to_database(brower_conn, menu_to_array(1))

