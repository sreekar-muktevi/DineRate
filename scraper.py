import requests
from bs4 import BeautifulSoup
import sqlite3

URL = "http://menuportal.dining.rutgers.edu/foodpro/pickmenu.asp?sName=Rutgers+University+Dining&locationNum=04"
# results = soup.find(="col-1")
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
mydivs = soup.find_all("div", {"class": "col-1"}
                       )
thing = []
for i in mydivs:
    thing.append(str(i)[96:-6])
for i in range(len(thing)):
    
    if(thing[i][0] == '>'):
        thing[i] = thing[i][1:]
    if(thing[i][0] == '/'):
        thing[i] = ''
for i in thing:
    print(i)