import sqlite3

# create a connection to the database
conn = sqlite3.connect('mydatabase.db')

# create a cursor object to execute SQL commands
c = conn.cursor()

# create User table
c.execute('''CREATE TABLE User
             (id INTEGER PRIMARY KEY,
              username TEXT NOT NULL,
              email TEXT NOT NULL,
              password TEXT NOT NULL)''')

# commit the changes and close the connection
conn.commit()
conn.close()