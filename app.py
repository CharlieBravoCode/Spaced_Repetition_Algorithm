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
    # update card_status table
    db.execute_query(f"UPDATE card_status SET ladder_status_id = ladder_status_id + 1, next_review_date = CURRENT_TIMESTAMP + INTERVAL '6' DAY WHERE card_id = {card_data['card_id']}")
else:
    print('Incorrect! The correct answer is: ' + card_data['pinyin'])
    # update card_status table
    db.execute_query(f"UPDATE card_status SET ladder_status_id = ladder_status_id + 1, next_review_date = CURRENT_TIMESTAMP + INTERVAL '6' DAY WHERE card_id = {card_data['card_id']}")

# Give user feedback