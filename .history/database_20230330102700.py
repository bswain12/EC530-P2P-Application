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
              password TEXT NOT NULL,
              status TEXT NOT NULL DEFAULT 'offline',
              friend_ids TEXT)''')

# create Message table
c.execute('''CREATE TABLE Message
             (id INTEGER PRIMARY KEY,
              sender_id INTEGER NOT NULL,
              recipient_id INTEGER NOT NULL,
              message_text TEXT NOT NULL,
              status TEXT NOT NULL,
              FOREIGN KEY(sender_id) REFERENCES Friend(id),
              FOREIGN KEY(recipient_id) REFERENCES Friend(id))''')

# create Friend table
c.execute('''CREATE TABLE Friend
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL)''')


# commit the changes and close the connection
conn.commit()
conn.close()