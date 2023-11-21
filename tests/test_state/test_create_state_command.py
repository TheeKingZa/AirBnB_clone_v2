import unittest
import MySQLdb

class TestCreateStateCommand(unittest.TestCase):
    def test_before_create(self):
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")

        # Create a cursor object
        cursor = db.cursor()

        # Execute query to count records in the states table
        cursor.execute("SELECT COUNT(*) FROM states;")

        # Get the count of records
        before_count = cursor.fetchone()[0]

        # Close cursor and database connection
        cursor.close()
        db.close()

        # Assert the count is as expected
        self.assertEqual(before_count, expected_count)

