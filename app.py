
# Import sqlite3 library
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('my_database.db')

# Create a cursor 
c = conn.cursor()

# Execute a query
c.execute('SELECT * FROM cards_chinese')

# Fetch all rows from the query
rows = c.fetchall()

# Print each row
for row in rows:
    print(row)

# Commit changes
conn.commit()

# Close connection
conn.close()