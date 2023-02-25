import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost"
    user = "HackRU"
    password = "RU26"
    database = "mydatabase"
)

mycursor = mydb.cursor()

# Insert into val: (id, name) values
val = [
    
]

mycursor.executemany(sql, val)

mydb.commit()