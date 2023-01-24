
import db 

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
else:
    print('Incorrect! The correct answer is: ' + card_data['pinyin'])

# Give user feedback
