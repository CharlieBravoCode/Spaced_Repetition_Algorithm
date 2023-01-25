import db 
import time

# Welcome message for user in Terminal
print('Welcome back to learning Chinese Words!')

# Serve user with a random card and print the column 'translation_english'
card_data = db.execute_query('SELECT * FROM cards_chinese ORDER BY RANDOM() LIMIT 1')
print('What is English translation of the word "' + card_data['translation_english'] + '"?')

# Connect to database and start a database transaction
conn, c = db.connect_database()
c.execute("BEGIN TRANSACTION")

# Check if an entry with the same card_id already exists in card_status
c.execute(f"SELECT * FROM card_status WHERE card_id = {card_data['card_id']}")
rows = c.fetchone()

# Add an entry to card_status if it does not already exist
if rows is None:
    current_date = time.strftime("%Y-%m-%d")
    c.execute(f"INSERT INTO card_status (card_id, date_last_reviewed, ladder_status_id, next_review_date) VALUES ({card_data['card_id']}, '{current_date}', 1, CURRENT_TIMESTAMP);")

# Take User input
user_input = input()

# Process user inpu
# compare user input to the column 'pinyin'
if user_input == card_data['pinyin']:
    print('Correct!')
    # Calculate next review date
    next_review_date = time.time() + 10*60
    # update card_status table
    c.execute(f"UPDATE card_status SET ladder_status_id = ladder_status_id + 1, next_review_date = '{next_review_date}' WHERE card_id = {card_data['card_id']}")
else:
    print('Incorrect! The correct answer is: ' + card_data['pinyin'])
    # Calculate next review date
    next_review_date = time.time() + 10*60
    # update card_status table
    c.execute(f"UPDATE card_status SET ladder_status_id = ladder_status_id + 1, next_review_date = '{next_review_date}' WHERE card_id = {card_data['card_id']}")

# Commit and close connection
db.commit_and_close_connection(conn)

# Give user feedback
print('You have successfully updated the card status!')