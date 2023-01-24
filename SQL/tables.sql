

CREATE TABLE cards_chinese (
  card_id INTEGER PRIMARY KEY,
  chinese_character TEXT,
  translation_english TEXT,
  pinyin TEXT,
  hsk_level INTEGER
);


CREATE TABLE card_status (
    card_id INTEGER,
    date_last_reviewed DATETIME,
    ladder_status_id INTEGER,
    next_review_date DATETIME
);

