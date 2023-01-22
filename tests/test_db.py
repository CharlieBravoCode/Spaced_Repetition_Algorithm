import unittest
import db

class TestDB(unittest.TestCase):

    def test_connect_database(self):
        conn, c = db.connect_database()
        self.assertIsNotNone(conn, "The connection should not be None")
        self.assertIsNotNone(c, "The cursor should not be None")

    def test_execute_query(self):
        query = 'SELECT * FROM cards_chinese'
        conn, c = db.connect_database()
        db.execute_query(query)
        # Check that rows have been fetched
        self.assertTrue(c.fetchall() is not None, "The query should return rows")

if __name__ == '__main__':
    unittest.main()