import sqlite3
import time

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
    if rows is not None:
        card_data = {
            'card_id': rows[0],
            'chinese_character': rows[1],
            'translation_english': rows[2],
            'pinyin': rows[3],
            'hsk_level': rows[4]
        }
        # Commit changes
        conn.commit()
        # Close connection
        conn.close()
        # Return the dictionary
        return card_data
    else:
        conn.commit()
        # Close connection
        conn.close()
        # Return None if no results
        return None

def commit_and_close_connection(conn):
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def add_card_to_status_table(card_id):
    conn, c = connect_database()
    current_date = time.strftime("%Y-%m-%d")
    c.execute(f"INSERT INTO card_status (card_id, date_last_reviewed, ladder_status_id, next_review_date) VALUES ({card_id}, '{current_date}', 1, CURRENT_TIMESTAMP + INTERVAL 10 MINUTE);")
    commit_and_close_connection(conn)