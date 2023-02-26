import sqlite3

# Connect to the database
conn = sqlite3.connect('menu_items.db')

# Execute a query to select all menu items
result_set = conn.execute('SELECT * FROM menu_items')

# Fetch the results and print them
for row in result_set:
    print(row)

# Close the connection
conn.close()