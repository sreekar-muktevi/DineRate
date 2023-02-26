import sqlite3

# Connect to the database
conn = sqlite3.connect('menu_items.db')

# Create a table to hold the menu items
conn.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rating REAL NOT NULL
    );
''')

# Insert a menu item
conn.execute('''
    INSERT INTO menu_items (name, rating)
    VALUES (?, ?);
''', ('Cheeseburger', 9))

# Delete a menu item
conn.execute('DELETE FROM menu_items WHERE id = ?', (1,))

# Commit the changes and close the connection
conn.commit()
conn.close()