import unittest
from unittest.mock import patch
from db import add_event
from bson import ObjectId
from models import Event


class TestDatabaseOperations(unittest.TestCase):

    @patch('db.events_collection')
    def test_add_event(self, mock_collection):
        # Mock the insert_one method
        mock_collection.insert_one.return_value.inserted_id = ObjectId('507f1f77bcf86cd799439011')  # noqa: E501
        # Create an Event instance
        test_event = Event("Test Title", "Test Date", "Test Location", "Test Description")  # noqa: E501
        # Call add_event with the Event instance
        result = add_event(test_event)
        # Assert that the result is as expected
        self.assertEqual(str(result), '507f1f77bcf86cd799439011')


if __name__ == '__main__':
    unittest.main()
