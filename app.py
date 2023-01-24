import db 
import time

# Welcome message for user in Terminal
print('Welcome back to learning Chinese Words!')

# Serve user with a random card and print the column 'translation_english'
card_data = db.execute_query('SELECT * FROM cards_chinese ORDER BY RANDOM() LIMIT 1')
print('What is English translation of the word "' + card_data['translation_english'] + '"?')


# Take User input
user_input = input()

# Process user input
# compare user input to the column 'pinyin'
if user_input == card_data['pinyin']:
    print('Correct!')
    # Calculate next review date (10 minutes)
    next_review_date = time.time() + 10*60
    # update card_status table
    # Connect to the database
    conn, c = db.connect_database()
    db.execute_query(f"UPDATE card_status SET ladder_status_id = ladder_status_id + 1, next_review_date = '{next_review_date}' WHERE card_id = {card_data['card_id']}")
    db.commit_and_close_connection(conn)
else:
    print('Incorrect! The correct answer is: ' + card_data['pinyin'])
    # Calculate next review date (10 seconds)
    next_review_date = time.time() + 10
    # update card_status table
    # Connect to the database
    conn, c = db.connect_database()
    db.execute_query(f"UPDATE card_status SET ladder_status_id = 1, next_review_date = '{next_review_date}' WHERE card_id = {card_data['card_id']}")
    db.commit_and_close_connection(conn)

# Give user feedback
print('You have successfully updated the card status!')