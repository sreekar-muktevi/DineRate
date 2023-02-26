import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

# Connect to the database
conn = sqlite3.connect('menu_items.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rating REAL NOT NULL
    );
''')

x = input("which campus?: ")
if (x == "busch"):
    x = 4
if (x == "livi"):
    x = 3
if (x == "neilson"):
    x = 5
if (x == "brower"):
    x = 1
y = input("how many days? (0 for today, up to 7 in advance):")
URL = "http://menuportal.dining.rutgers.edu/foodpro/pickmenu.asp?sName=+University+Dining&locationNum=0"
URL += str(x)
# results = soup.find(="col-1")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
mydivs = soup.find_all("div", {"class": "col-1"}
                       )
thing = []
for i in mydivs:
    thing.append(str(i)[96:-6])
    conn.execute('''
        INSERT INTO menu_items (name, rating)
        VALUES (?, ?);
    ''', (str(i)[96:-6], 0))

    
for i in range(len(thing)):
    if(thing[i][0] == '>'):
        thing[i] = thing[i][1:]
    # if(thing[i][0] == '/'):
    #     thing.pop(i)
    #     i -= 2
for i in thing:
    print(i)

conn.commit()

result_set = conn.execute('SELECT * FROM menu_items')

# Fetch the results and print them
for row in result_set:
    print(row)
    
conn.close()
