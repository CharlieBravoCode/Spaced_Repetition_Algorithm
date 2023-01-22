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
    rows = c.fetchone()

    # Create a dictionary from the data
    card_data = {
        'card_id': rows[0],
        'chinese_character': rows[1],
        'translation_english': rows[2],
        'pinyin': rows[3],
        'hsk_level': rows[4]
    }

    # Print the dictionary
    # print(card_data)
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    # Return the dictionary
    return card_data

def commit_and_close_connection(conn):
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

conn, c = connect_database()

commit_and_close_connection(conn)