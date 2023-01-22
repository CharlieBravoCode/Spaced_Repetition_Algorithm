import sqlite3

def connect_database():
  # Create a connection to the database
  conn = sqlite3.connect('my_database.db')
  # Create a cursor 
  c = conn.cursor()
  return conn, c

# Execute a query
def execute_query(query):
    conn, c = connect_database()
    c.execute(query)
    rows = c.fetchall()
    # Print each row
    for row in rows:
        print(row)

def commit_and_close_connection(conn):
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

conn, c = connect_database()

commit_and_close_connection(conn)