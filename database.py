import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('menu_items.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Define a SQL command to create a table for the menu items
create_table_command = '''CREATE TABLE IF NOT EXISTS menu_items (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            description TEXT
                        );'''

# Execute the SQL command to create the table
c.execute(create_table_command)

# Sample data of menu items scraped from a website
menu_items = [
    ('Eggs and bacon', 'Scrambled eggs with crispy bacon'),
    ('Pancakes with syrup', 'Fluffy pancakes served with maple syrup'),
    ('Grilled cheese with tomato soup', 'Toasted bread with melted cheese, served with tomato soup'),
    ('Roasted chicken with vegetables', 'Seasoned chicken roasted to perfection with a side of mixed vegetables')
]

# Define a SQL command to insert the menu items into the table
insert_command = '''INSERT INTO menu_items (name, description)
                    VALUES (?, ?);'''

# Execute the SQL command for each menu item
for item in menu_items:
    c.execute(insert_command, item)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()